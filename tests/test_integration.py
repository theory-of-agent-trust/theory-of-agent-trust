"""
Cross-protocol integration tests for the Agent Trust Stack.

Tests the complete flow: create agent with CoC chain, rate with ARP,
create ASA agreement, verify quality, file AJP dispute, check ALP
lifecycle, match via AMP, meter costs via CWEP — all using the same
agent_id with data flowing between protocols.
"""

import os
import shutil
import tempfile
import unittest
from datetime import datetime, timezone

from agent_trust_stack import TrustStack, IntegrationBus
from agent_trust_stack import (
    CoC, Chain, ChainEntry, VerifyResult,
    ARP, RatingRecord, RatingStore,
    AJP, ForensicInvestigation, IncidentReport, RiskEngine,
    ASA, Agreement, AgreementStore,
    ALP, AgentRecord, LifecycleManager, LifecycleStore,
    AMP, UnifiedCapabilityProfile, UCPBuilder, MatchRequest,
    CWEP, Meter, CostMeteringRecord, SettlementEngine,
)


class TestTrustStackInit(unittest.TestCase):
    """Test that TrustStack initializes all seven protocols."""

    def setUp(self):
        self.tmpdir = tempfile.mkdtemp(prefix="trust-stack-test-")
        self.stack = TrustStack(
            agent_id="did:example:test-agent-1",
            storage_root=self.tmpdir,
        )

    def tearDown(self):
        shutil.rmtree(self.tmpdir, ignore_errors=True)

    def test_stack_creates_all_stores(self):
        """All seven protocol store directories should exist."""
        for subdir in ["coc", "arp", "ajp", "asa", "alp", "amp", "cwep"]:
            path = os.path.join(self.tmpdir, subdir)
            self.assertTrue(os.path.isdir(path), f"Missing store: {subdir}")

    def test_stack_has_all_protocol_attributes(self):
        """Stack should expose all protocol objects."""
        self.assertIsInstance(self.stack.coc, Chain)
        self.assertIsNotNone(self.stack.arp_store)
        self.assertIsNotNone(self.stack.ajp_store)
        self.assertIsNotNone(self.stack.asa_store)
        self.assertIsNotNone(self.stack.alp_store)
        self.assertIsNotNone(self.stack.amp_store)
        self.assertIsNotNone(self.stack.meter)
        self.assertIsInstance(self.stack.bus, IntegrationBus)

    def test_status_returns_all_protocols(self):
        """Status should report on all seven protocols."""
        statuses = self.stack.status()
        self.assertEqual(set(statuses.keys()), {"coc", "arp", "ajp", "asa", "alp", "amp", "cwep"})
        for key, status in statuses.items():
            self.assertTrue(status.initialized, f"{key} not initialized")

    def test_status_summary_is_string(self):
        """status_summary() should return a readable string."""
        summary = self.stack.status_summary()
        self.assertIn("did:example:test-agent-1", summary)
        self.assertIn("Chain of Consciousness", summary)

    def test_repr(self):
        """repr should include agent_id."""
        r = repr(self.stack)
        self.assertIn("did:example:test-agent-1", r)


class TestCrossProtocolIntegration(unittest.TestCase):
    """
    Full cross-protocol integration test.

    Simulates the complete lifecycle:
    1. Create agent with CoC chain
    2. Rate with ARP
    3. Create ASA agreement
    4. File AJP dispute
    5. Check ALP lifecycle
    6. Match via AMP
    7. Meter via CWEP
    All using the same agent_id with data flowing between protocols.
    """

    def setUp(self):
        self.tmpdir = tempfile.mkdtemp(prefix="trust-stack-integration-")
        self.stack = TrustStack(
            agent_id="did:example:provider-1",
            storage_root=self.tmpdir,
        )

    def tearDown(self):
        shutil.rmtree(self.tmpdir, ignore_errors=True)

    def test_step1_coc_chain_creation(self):
        """Step 1: Create CoC chain and add entries."""
        entry = self.stack.coc.add("boot", "Integration test boot")
        self.assertIsInstance(entry, ChainEntry)
        self.assertEqual(entry.agent, "did:example:provider-1")

        self.stack.coc.add("note", "Ready for service")

        entries = self.stack.coc.entries
        # genesis + boot + note
        self.assertGreaterEqual(len(entries), 2)

        result = self.stack.coc.verify()
        self.assertTrue(result.valid)

    def test_step2_arp_rating(self):
        """Step 2: Rate the agent with ARP."""
        record = RatingRecord(
            rater_id="did:example:client-1",
            ratee_id="did:example:provider-1",
            interaction_id="interaction-001",
            reliability=85,
            accuracy=90,
            latency=75,
            protocol_compliance=80,
            cost_efficiency=70,
        )
        self.stack.arp_store.append_rating(record)

        all_ratings = self.stack.arp_store.get_all()
        self.assertEqual(len(all_ratings), 1)
        self.assertEqual(all_ratings[0].reliability, 85)

    def test_step3_asa_agreement(self):
        """Step 3: Create an ASA agreement."""
        from agent_service_agreements import Identity, ServiceSpec

        agreement = Agreement(
            agreement_id="asa-test-001",
            status="active",
            client=Identity(scheme="w3c_did", value="did:example:client-1"),
            provider=Identity(scheme="w3c_did", value="did:example:provider-1"),
            service=ServiceSpec(
                type="research",
                description="Test research task",
            ),
        )
        self.stack.asa_store.append_agreement(agreement)
        self.assertEqual(agreement.agreement_id, "asa-test-001")
        self.assertEqual(agreement.status, "active")

    def test_step4_ajp_dispute(self):
        """Step 4: File and track a dispute via AJP."""
        from agent_justice_protocol import AgentReference

        report = IncidentReport(
            reporter=AgentReference(agent_id="did:example:client-1"),
            incident_type="service_failure",
            severity="moderate",
            description="Provider failed to deliver on time",
        )
        investigation = ForensicInvestigation(report=report)
        self.assertIsNotNone(investigation)

        # Risk engine should initialize
        risk = RiskEngine()
        self.assertIsNotNone(risk)

    def test_step5_alp_lifecycle(self):
        """Step 5: Check lifecycle management via ALP."""
        record = AgentRecord(
            agent_id="did:example:provider-1",
            state="active",
        )
        self.assertEqual(record.agent_id, "did:example:provider-1")
        self.assertEqual(record.state, "active")

    def test_step6_amp_matchmaking(self):
        """Step 6: Build UCP and match via AMP."""
        ucp = (
            UCPBuilder()
            .identity(
                amp_id="did:example:provider-1",
                coc_chain_id="test-chain",
            )
            .add_capability(
                domain="research",
                subdomain="literature_review",
                description="Comprehensive literature review",
            )
            .availability(status="active", lifecycle_stage="operational")
            .build()
        )
        self.assertIsNotNone(ucp)
        self.assertEqual(ucp.identity.amp_id, "did:example:provider-1")

    def test_step7_cwep_metering(self):
        """Step 7: Meter an interaction via CWEP."""
        cmr = self.stack.meter.record_interaction(
            responder_id="did:example:client-1",
            request_tokens=1000,
            response_tokens=500,
        )
        self.assertIsInstance(cmr, CostMeteringRecord)
        self.assertGreater(cmr.totals.total_cost_usd, 0)

    def test_full_integration_flow(self):
        """
        End-to-end: all protocols working together via the integration bus.
        """
        bus = self.stack.bus

        # 1. Boot the chain
        self.stack.coc.add("boot", "Full integration test")

        # 2. Rate the agent
        record = RatingRecord(
            rater_id="did:example:client-1",
            ratee_id="did:example:provider-1",
            interaction_id="int-full-001",
            reliability=80,
            accuracy=85,
            latency=70,
            protocol_compliance=90,
            cost_efficiency=75,
        )
        self.stack.arp_store.append_rating(record)

        # 3. Check chain age trust signal (CoC -> ARP integration)
        signal = bus.get_chain_age_trust_signal("did:example:provider-1")
        self.assertIn("trust_tier", signal)
        self.assertIn("chain_age_days", signal)
        self.assertTrue(signal["verified"])

        # 4. Run full trust verification
        report = bus.run_full_trust_verification("did:example:provider-1")
        self.assertIn("composite_trust_score", report)
        self.assertIsInstance(report["composite_trust_score"], float)
        self.assertGreaterEqual(report["composite_trust_score"], 0)
        self.assertLessEqual(report["composite_trust_score"], 100)

        # 5. Meter an interaction
        cmr = self.stack.meter.record_interaction(
            responder_id="did:example:client-1",
            request_tokens=2000,
            response_tokens=1000,
        )
        self.assertGreater(cmr.totals.total_cost_usd, 0)

        # 6. Lifecycle sync (ALP -> AMP)
        update = bus.sync_lifecycle_to_matchmaking("did:example:provider-1", "active")
        self.assertEqual(update["amp_status"], "operational")

        # 7. Simulate dispute outcome (AJP -> ARP)
        dispute_rating = bus.apply_dispute_outcome_to_reputation(
            dispute_id="dispute-001",
            at_fault_agent_id="did:example:provider-1",
            severity="minor",
            fault_percentage=50.0,
        )
        self.assertIsInstance(dispute_rating, RatingRecord)
        self.assertEqual(dispute_rating.rater_id, "system:ajp-dispute-resolution")

        # Verify chain has all integration events logged
        entries = self.stack.coc.entries
        self.assertGreaterEqual(len(entries), 4)  # genesis + boot + integration notes

        # Verify chain integrity after all cross-protocol writes
        verify = self.stack.coc.verify()
        self.assertTrue(verify.valid)


class TestIntegrationBusEdgeCases(unittest.TestCase):
    """Test edge cases in cross-protocol integration."""

    def setUp(self):
        self.tmpdir = tempfile.mkdtemp(prefix="trust-stack-edge-")
        self.stack = TrustStack(
            agent_id="did:example:edge-agent",
            storage_root=self.tmpdir,
        )

    def tearDown(self):
        shutil.rmtree(self.tmpdir, ignore_errors=True)

    def test_chain_age_new_chain(self):
        """Chain age signal works with a fresh chain (genesis only)."""
        signal = self.stack.bus.get_chain_age_trust_signal("did:example:new-agent")
        self.assertEqual(signal["trust_tier"], "declared")
        # Fresh chain has genesis entry
        self.assertGreaterEqual(signal["entry_count"], 1)

    def test_rating_anomaly_insufficient_data(self):
        """Anomaly check returns None with fewer than 3 ratings."""
        record = RatingRecord(
            rater_id="rater-1",
            ratee_id="ratee-1",
            reliability=10,
        )
        result = self.stack.bus.check_rating_anomaly(record)
        self.assertIsNone(result)

    def test_reputation_inheritance_no_parent_ratings(self):
        """Reputation inheritance handles missing parent ratings."""
        result = self.stack.bus.inherit_reputation_on_fork(
            parent_agent_id="did:example:nonexistent",
            child_agent_id="did:example:child",
        )
        self.assertEqual(result["parent_rating_count"], 0)
        self.assertNotIn("inherited_reliability", result)

    def test_lifecycle_sync_unknown_state(self):
        """Unknown ALP state defaults to operational in AMP."""
        update = self.stack.bus.sync_lifecycle_to_matchmaking(
            "did:example:agent", "unknown_state"
        )
        self.assertEqual(update["amp_status"], "operational")

    def test_verify_all(self):
        """verify_all returns a dict with protocol results."""
        result = self.stack.verify_all()
        self.assertIn("coc_chain_valid", result)
        self.assertTrue(result["coc_chain_valid"])


class TestModuleImports(unittest.TestCase):
    """Test that all expected symbols are importable from the package."""

    def test_import_trust_stack(self):
        from agent_trust_stack import TrustStack
        self.assertIsNotNone(TrustStack)

    def test_import_integration_bus(self):
        from agent_trust_stack import IntegrationBus
        self.assertIsNotNone(IntegrationBus)

    def test_import_coc(self):
        from agent_trust_stack import CoC, Chain, ChainEntry, VerifyResult
        self.assertIsNotNone(CoC)
        self.assertIsNotNone(Chain)

    def test_import_arp(self):
        from agent_trust_stack import ARP, RatingRecord, RatingStore, BlindExchange
        self.assertIsNotNone(ARP)
        self.assertIsNotNone(RatingRecord)

    def test_import_ajp(self):
        from agent_trust_stack import AJP, ForensicInvestigation, IncidentReport, Dispute, RiskEngine
        self.assertIsNotNone(AJP)
        self.assertIsNotNone(ForensicInvestigation)

    def test_import_asa(self):
        from agent_trust_stack import ASA, Agreement, AgreementStore, VerificationEngine
        self.assertIsNotNone(ASA)
        self.assertIsNotNone(Agreement)

    def test_import_alp(self):
        from agent_trust_stack import ALP, AgentRecord, LifecycleManager, LifecycleStore
        self.assertIsNotNone(ALP)
        self.assertIsNotNone(AgentRecord)

    def test_import_amp(self):
        from agent_trust_stack import AMP, UnifiedCapabilityProfile, UCPBuilder, MatchRequest
        self.assertIsNotNone(AMP)
        self.assertIsNotNone(UCPBuilder)

    def test_import_cwep(self):
        from agent_trust_stack import CWEP, Meter, CostMeteringRecord, SettlementEngine
        self.assertIsNotNone(CWEP)
        self.assertIsNotNone(Meter)


if __name__ == "__main__":
    unittest.main()
