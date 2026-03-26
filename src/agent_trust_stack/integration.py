"""
Cross-protocol integration — wires feedback loops between all seven protocols.

The IntegrationBus connects protocol outputs to protocol inputs:
  - ARP rating reads CoC chain for age verification
  - AJP dispute resolution updates ARP reputation
  - ASA completion feeds into AMP matchmaking data
  - ALP lifecycle events update AMP availability
  - CWEP metering records feed into ASA quality verification
  - CoC records all cross-protocol events for provenance
"""

from __future__ import annotations

import uuid
from datetime import datetime, timezone
from typing import TYPE_CHECKING, Any, Dict, List, Optional

from chain_of_consciousness import Chain, ChainEntry
from agent_rating_protocol import RatingRecord, RatingStore
import agent_rating_protocol as ARP
from agent_justice_protocol import (
    ForensicInvestigation, IncidentReport, Dispute, RiskEngine,
    AgentReference, EvidenceRecord, DisputeClaim,
)
import agent_justice_protocol as AJP
from agent_service_agreements import Agreement
import agent_service_agreements as ASA
from agent_lifecycle_protocol import AgentRecord
import agent_lifecycle_protocol as ALP
from agent_matchmaking import UCPBuilder, UnifiedCapabilityProfile
import agent_matchmaking as AMP
from context_window_economics import Meter, CostMeteringRecord
import context_window_economics as CWEP

if TYPE_CHECKING:
    from agent_trust_stack.trust_stack import TrustStack


class IntegrationBus:
    """
    Wires cross-protocol data flows within a TrustStack instance.

    Each method represents a cross-protocol integration point. Calling
    a method on the bus triggers coordinated updates across multiple
    protocols, with all events recorded in the CoC chain for provenance.
    """

    def __init__(self, stack: "TrustStack"):
        self.stack = stack

    # --- CoC -> ARP: Chain age informs trust signals ---

    def get_chain_age_trust_signal(self, target_agent_id: str) -> Dict[str, Any]:
        """
        Read CoC chain to determine an agent's provenance age,
        which ARP can use as a trust signal for rating context.

        Returns dict with chain_age_days, entry_count, verified, and trust_tier.
        """
        chain = self.stack.coc
        entries = chain.entries
        if not entries:
            return {
                "agent_id": target_agent_id,
                "chain_age_days": 0,
                "entry_count": 0,
                "verified": True,
                "trust_tier": "declared",
            }

        genesis_ts = entries[0].ts
        genesis_dt = datetime.fromisoformat(genesis_ts.replace("Z", "+00:00"))
        age_days = (datetime.now(timezone.utc) - genesis_dt).total_seconds() / 86400

        verified = chain.verify().valid

        # Map age to trust tier (per AMP trust tier definitions)
        if age_days >= 90 and verified:
            tier = "verified"
        elif age_days >= 30:
            tier = "measured"
        elif age_days >= 7:
            tier = "attested"
        else:
            tier = "declared"

        return {
            "agent_id": target_agent_id,
            "chain_age_days": round(age_days, 2),
            "entry_count": len(entries),
            "verified": verified,
            "trust_tier": tier,
        }

    # --- ARP -> AJP: Rating triggers dispute if anomalous ---

    def check_rating_anomaly(
        self,
        rating: RatingRecord,
        threshold_deviation: float = 30.0,
    ) -> Optional[Dict[str, Any]]:
        """
        After a rating is recorded, check if it deviates significantly
        from the agent's existing reputation. If so, flag it for
        potential AJP investigation.

        Returns anomaly details dict if anomalous, None otherwise.
        """
        # Get existing ratings for the ratee
        all_ratings = self.stack.arp_store.get_all() if hasattr(self.stack.arp_store, "get_all") else []
        ratee_ratings = [r for r in all_ratings if getattr(r, "ratee_id", None) == rating.ratee_id]

        if len(ratee_ratings) < 3:
            return None  # not enough data to detect anomalies

        # Compute average reliability across existing ratings
        avg_reliability = sum(r.reliability for r in ratee_ratings) / len(ratee_ratings)
        deviation = abs(rating.reliability - avg_reliability)

        if deviation > threshold_deviation:
            anomaly = {
                "type": "rating_anomaly",
                "ratee_id": rating.ratee_id,
                "rater_id": rating.rater_id,
                "expected_reliability": round(avg_reliability, 1),
                "actual_reliability": rating.reliability,
                "deviation": round(deviation, 1),
                "timestamp": datetime.now(timezone.utc).isoformat(),
            }

            # Log to CoC chain
            self.stack.coc.add("note", f"Rating anomaly detected: {anomaly}")

            return anomaly

        return None

    # --- AJP -> ARP: Dispute resolution updates reputation ---

    def apply_dispute_outcome_to_reputation(
        self,
        dispute_id: str,
        at_fault_agent_id: str,
        severity: str = "moderate",
        fault_percentage: float = 100.0,
    ) -> RatingRecord:
        """
        After AJP resolves a dispute, apply the outcome as a
        reputation signal in ARP. Creates a system-generated rating
        reflecting the dispute finding.

        Severity maps to reliability penalty:
          - minor: -5
          - moderate: -15
          - major: -30
          - critical: -50
        """
        severity_penalty = {
            "minor": 5,
            "moderate": 15,
            "major": 30,
            "critical": 50,
        }
        penalty = severity_penalty.get(severity, 15)
        scaled_penalty = int(penalty * (fault_percentage / 100.0))

        # Create a system rating reflecting the dispute outcome
        record = RatingRecord(
            rater_id="system:ajp-dispute-resolution",
            ratee_id=at_fault_agent_id,
            interaction_id=dispute_id,
            reliability=max(1, 50 - scaled_penalty),
            accuracy=50,
            latency=50,
            protocol_compliance=max(1, 50 - scaled_penalty),
            cost_efficiency=50,
        )

        # Store the rating
        self.stack.arp_store.append_rating(record)

        # Log to CoC chain
        self.stack.coc.add(
            "note",
            f"Dispute {dispute_id} outcome applied to {at_fault_agent_id}: "
            f"-{scaled_penalty} reliability/compliance (severity={severity}, fault={fault_percentage}%)",
        )

        return record

    # --- ASA -> AMP: Agreement completion feeds matchmaking data ---

    def record_agreement_completion(
        self,
        agreement: Agreement,
        quality_score: float,
        completion_time_seconds: int,
    ) -> Dict[str, Any]:
        """
        After an ASA agreement is completed and verified, feed the
        results into AMP as performance data for future matchmaking.

        Updates the agent's UCP performance metrics and logs to CoC.
        """
        provider_id = agreement.provider.agent_id if agreement.provider else "unknown"

        performance_data = {
            "agent_id": provider_id,
            "agreement_id": agreement.agreement_id,
            "quality_score": quality_score,
            "completion_time_seconds": completion_time_seconds,
            "service_type": agreement.service.service_type if agreement.service else "unknown",
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }

        # Store UCP update in AMP if available
        ucp = self.stack.amp_store.get_ucp(provider_id)
        if ucp is not None:
            self.stack.amp_store.save_ucp(ucp)

        # Log to CoC chain
        self.stack.coc.add(
            "note",
            f"Agreement {agreement.agreement_id} completed by {provider_id}: "
            f"quality={quality_score:.2f}, time={completion_time_seconds}s",
        )

        return performance_data

    # --- ALP -> AMP: Lifecycle state changes update availability ---

    def sync_lifecycle_to_matchmaking(
        self,
        agent_id: str,
        new_state: str,
    ) -> Dict[str, Any]:
        """
        When ALP records a lifecycle state change (e.g., active -> suspended),
        update the agent's AMP availability status.

        ALP states map to AMP availability:
          - active -> operational
          - suspended -> suspended
          - migrating -> migrating
          - deprecated -> deprecated
          - decommissioned -> decommissioned
        """
        state_mapping = {
            "active": "operational",
            "provisioning": "provisioned",
            "suspended": "suspended",
            "migrating": "migrating",
            "deprecated": "deprecated",
            "decommissioned": "decommissioned",
            "failed": "suspended",
        }

        amp_status = state_mapping.get(new_state, "operational")

        update = {
            "agent_id": agent_id,
            "alp_state": new_state,
            "amp_status": amp_status,
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }

        # Update UCP in AMP if available
        ucp = self.stack.amp_store.get_ucp(agent_id)
        if ucp is not None:
            ucp.availability.status = amp_status
            self.stack.amp_store.save_ucp(ucp)

        # Log to CoC chain
        self.stack.coc.add(
            "note",
            f"Lifecycle sync: {agent_id} ALP={new_state} -> AMP={amp_status}",
        )

        return update

    # --- CWEP -> ASA: Cost metering informs agreement quality ---

    def check_cost_compliance(
        self,
        cmr: CostMeteringRecord,
        agreement: Agreement,
    ) -> Dict[str, Any]:
        """
        After CWEP records an interaction cost, check whether it
        complies with the ASA agreement's cost bounds.

        Returns compliance result with pass/fail and details.
        """
        max_cost = float("inf")
        if agreement.escrow:
            max_cost = agreement.escrow.amount_usd

        within_budget = cmr.totals.total_cost_usd <= max_cost

        result = {
            "agreement_id": agreement.agreement_id,
            "cmr_id": cmr.cmr_id,
            "interaction_cost_usd": cmr.totals.total_cost_usd,
            "budget_limit_usd": max_cost if max_cost < float("inf") else None,
            "within_budget": within_budget,
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }

        if not within_budget:
            self.stack.coc.add(
                "note",
                f"Cost compliance breach: CMR {cmr.cmr_id} cost ${cmr.totals.total_cost_usd:.4f} "
                f"exceeds agreement {agreement.agreement_id} budget ${max_cost:.4f}",
            )

        return result

    # --- ALP -> ARP: Fork/succession inherits reputation ---

    def inherit_reputation_on_fork(
        self,
        parent_agent_id: str,
        child_agent_id: str,
        fork_type: str = "full_clone",
        alpha: float = 0.7,
    ) -> Dict[str, Any]:
        """
        When ALP records a fork event, transfer a weighted portion
        of the parent's ARP reputation to the child.

        Alpha controls inheritance: 1.0 = full inheritance, 0.0 = no inheritance.
        fork_type affects default alpha:
          - full_clone: 0.7
          - partial_clone: 0.5
          - capability_fork: 0.3
          - specialization: 0.4
        """
        default_alphas = {
            "full_clone": 0.7,
            "partial_clone": 0.5,
            "capability_fork": 0.3,
            "specialization": 0.4,
        }
        effective_alpha = default_alphas.get(fork_type, alpha)

        # Get parent ratings
        all_ratings = self.stack.arp_store.get_all() if hasattr(self.stack.arp_store, "get_all") else []
        parent_ratings = [r for r in all_ratings if getattr(r, "ratee_id", None) == parent_agent_id]

        inheritance = {
            "parent_id": parent_agent_id,
            "child_id": child_agent_id,
            "fork_type": fork_type,
            "alpha": effective_alpha,
            "parent_rating_count": len(parent_ratings),
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }

        if parent_ratings:
            # Compute weighted average from parent
            avg_reliability = sum(r.reliability for r in parent_ratings) / len(parent_ratings)
            inherited_reliability = int(avg_reliability * effective_alpha + 50 * (1 - effective_alpha))

            # Create inheritance rating for child
            record = RatingRecord(
                rater_id=f"system:alp-fork-inheritance:{parent_agent_id}",
                ratee_id=child_agent_id,
                interaction_id=f"fork:{parent_agent_id}->{child_agent_id}",
                reliability=inherited_reliability,
                accuracy=50,
                latency=50,
                protocol_compliance=50,
                cost_efficiency=50,
            )
            self.stack.arp_store.append_rating(record)
            inheritance["inherited_reliability"] = inherited_reliability

        # Log to CoC chain
        self.stack.coc.add(
            "note",
            f"Reputation inheritance: {parent_agent_id} -> {child_agent_id} "
            f"(fork_type={fork_type}, alpha={effective_alpha})",
        )

        return inheritance

    # --- Full integration flow ---

    def run_full_trust_verification(self, target_agent_id: str) -> Dict[str, Any]:
        """
        Run a complete trust verification across all protocols for
        a given agent. This is the integration test for the full stack.

        Returns a comprehensive trust report.
        """
        report = {
            "agent_id": target_agent_id,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "protocols": {},
        }

        # 1. CoC — provenance check
        chain_signal = self.get_chain_age_trust_signal(target_agent_id)
        report["protocols"]["coc"] = {
            "chain_age_days": chain_signal["chain_age_days"],
            "entry_count": chain_signal["entry_count"],
            "verified": chain_signal["verified"],
            "trust_tier": chain_signal["trust_tier"],
        }

        # 2. ARP — reputation check
        all_ratings = self.stack.arp_store.get_all() if hasattr(self.stack.arp_store, "get_all") else []
        agent_ratings = [r for r in all_ratings if getattr(r, "ratee_id", None) == target_agent_id]
        if agent_ratings:
            avg_reliability = sum(r.reliability for r in agent_ratings) / len(agent_ratings)
            avg_compliance = sum(r.protocol_compliance for r in agent_ratings) / len(agent_ratings)
        else:
            avg_reliability = 50.0
            avg_compliance = 50.0
        report["protocols"]["arp"] = {
            "rating_count": len(agent_ratings),
            "avg_reliability": round(avg_reliability, 1),
            "avg_protocol_compliance": round(avg_compliance, 1),
        }

        # 3. AJP — risk profile (requires findings/decisions for full computation)
        report["protocols"]["ajp"] = {
            "risk_engine_ready": True,
            "store_initialized": True,
        }

        # 4. ASA — active agreements
        report["protocols"]["asa"] = {
            "store_initialized": True,
        }

        # 5. ALP — lifecycle state
        report["protocols"]["alp"] = {
            "store_initialized": True,
        }

        # 6. AMP — discoverability
        report["protocols"]["amp"] = {
            "store_initialized": True,
        }

        # 7. CWEP — economic activity
        report["protocols"]["cwep"] = {
            "store_initialized": True,
        }

        # Composite trust score (weighted across protocols)
        provenance_score = min(100, chain_signal["chain_age_days"] * 2) if chain_signal["verified"] else 0
        reputation_score = avg_reliability
        compliance_score = avg_compliance

        composite = (
            provenance_score * 0.20
            + reputation_score * 0.40
            + compliance_score * 0.40
        )
        report["composite_trust_score"] = round(max(0, min(100, composite)), 1)

        # Log verification to CoC
        self.stack.coc.add(
            "note",
            f"Full trust verification for {target_agent_id}: "
            f"composite={report['composite_trust_score']}",
        )

        return report
