"""
Unified TrustStack class — single entry point for all seven protocols.

Usage:
    stack = TrustStack(agent_id="did:example:agent-1")
    stack.coc.add("boot", "System initialized")
    stack.status()
"""

from __future__ import annotations

import json
import os
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional

from chain_of_consciousness import Chain, ChainEntry
from agent_rating_protocol import RatingStore
from agent_justice_protocol import JusticeStore, RiskEngine
from agent_service_agreements import AgreementStore
from agent_lifecycle_protocol import AgentRecord, LifecycleStore, LifecycleManager
from agent_matchmaking import MatchmakingStore, UCPBuilder
from context_window_economics import CWEPStore, Meter


@dataclass
class ProtocolStatus:
    """Status of a single protocol within the stack."""
    name: str
    version: str
    initialized: bool
    store_path: str
    entry_count: int = 0
    details: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "version": self.version,
            "initialized": self.initialized,
            "store_path": self.store_path,
            "entry_count": self.entry_count,
            "details": self.details,
        }


class TrustStack:
    """
    Unified entry point for the complete Agent Trust Stack.

    Initializes all seven protocols with shared agent identity and
    coordinated storage under a single root directory.

    Args:
        agent_id: Agent identifier (DID, URI, or plain string).
        storage_root: Root directory for all protocol stores.
            Defaults to ".trust-stack" in the current directory.
        model: Model identifier for CWEP metering. Default "claude-sonnet-4-6".
        provider: Provider for CWEP metering. Default "anthropic".
    """

    def __init__(
        self,
        agent_id: str,
        storage_root: Optional[str] = None,
        model: str = "claude-sonnet-4-6",
        provider: str = "anthropic",
    ):
        self.agent_id = agent_id
        self.storage_root = Path(storage_root or ".trust-stack")
        self.model = model
        self.provider = provider

        # Create storage root
        self.storage_root.mkdir(parents=True, exist_ok=True)

        # Initialize all protocols
        self._init_coc()
        self._init_arp()
        self._init_ajp()
        self._init_asa()
        self._init_alp()
        self._init_amp()
        self._init_cwep()

        # Wire integration bus (lazy import to avoid circular)
        from agent_trust_stack.integration import IntegrationBus
        self.bus = IntegrationBus(self)

    def _init_coc(self) -> None:
        """Initialize Chain of Consciousness (provenance)."""
        coc_dir = self.storage_root / "coc"
        os.makedirs(str(coc_dir), exist_ok=True)
        coc_file = str(coc_dir / "chain.jsonl")
        self.coc = Chain(agent=self.agent_id, storage=coc_file)

    def _init_arp(self) -> None:
        """Initialize Agent Rating Protocol (reputation)."""
        arp_path = str(self.storage_root / "arp")
        os.makedirs(arp_path, exist_ok=True)
        self.arp_store = RatingStore(
            path=os.path.join(arp_path, "ratings.jsonl")
        )

    def _init_ajp(self) -> None:
        """Initialize Agent Justice Protocol (accountability)."""
        ajp_path = str(self.storage_root / "ajp")
        self.ajp_store = JusticeStore(directory=ajp_path)
        self.risk_engine = RiskEngine()

    def _init_asa(self) -> None:
        """Initialize Agent Service Agreements (contracts)."""
        asa_path = str(self.storage_root / "asa")
        self.asa_store = AgreementStore(directory=asa_path)
        self.asa_verifier = __import__(
            "agent_service_agreements", fromlist=["VerificationEngine"]
        ).VerificationEngine()

    def _init_alp(self) -> None:
        """Initialize Agent Lifecycle Protocol (lifecycle)."""
        alp_path = str(self.storage_root / "alp")
        self.alp_store = LifecycleStore(directory=alp_path)
        self.alp_manager = LifecycleManager(store=self.alp_store)

    def _init_amp(self) -> None:
        """Initialize Agent Matchmaking Protocol (discovery)."""
        amp_path = str(self.storage_root / "amp")
        self.amp_store = MatchmakingStore(directory=amp_path)

    def _init_cwep(self) -> None:
        """Initialize Context Window Economics Protocol (cost allocation)."""
        cwep_path = str(self.storage_root / "cwep")
        self.cwep_store = CWEPStore(store_dir=cwep_path)
        self.meter = Meter(
            agent_id=self.agent_id,
            model=self.model,
            provider=self.provider,
        )

    # --- Convenience methods ---

    def add_chain_entry(self, event_type: str, data: Any = "") -> ChainEntry:
        """Add an entry to the CoC chain and return it."""
        return self.coc.add(event_type, data)

    def get_chain_age_days(self) -> float:
        """Return the age of the CoC chain in days (since genesis)."""
        entries = self.coc.entries
        if not entries:
            return 0.0
        genesis_ts = entries[0].ts
        genesis_dt = datetime.fromisoformat(genesis_ts.replace("Z", "+00:00"))
        now = datetime.now(timezone.utc)
        return (now - genesis_dt).total_seconds() / 86400

    def build_ucp(self) -> "UnifiedCapabilityProfile":
        """
        Build a UnifiedCapabilityProfile for this agent using stack data.

        Returns a UCP pre-populated with the agent's identity and
        CoC chain reference.
        """
        builder = UCPBuilder()
        builder.identity(
            amp_id=self.agent_id,
            coc_chain_id=str(self.storage_root / "coc"),
        )
        return builder.build()

    def status(self) -> Dict[str, ProtocolStatus]:
        """Return status of all seven protocols."""
        import chain_of_consciousness
        import agent_rating_protocol
        import agent_justice_protocol
        import agent_service_agreements
        import agent_lifecycle_protocol
        import agent_matchmaking
        import context_window_economics

        entries = self.coc.entries
        coc_status = ProtocolStatus(
            name="Chain of Consciousness",
            version=getattr(chain_of_consciousness, "__version__", "0.1.1"),
            initialized=True,
            store_path=str(self.storage_root / "coc"),
            entry_count=len(entries),
            details={
                "chain_age_days": round(self.get_chain_age_days(), 2),
                "verified": self.coc.verify().valid if entries else True,
            },
        )

        arp_ratings = self.arp_store.get_all() if hasattr(self.arp_store, "get_all") else []
        arp_status = ProtocolStatus(
            name="Agent Rating Protocol",
            version=getattr(agent_rating_protocol, "__version__", "0.3.0"),
            initialized=True,
            store_path=str(self.storage_root / "arp"),
            entry_count=len(arp_ratings),
        )

        ajp_status = ProtocolStatus(
            name="Agent Justice Protocol",
            version=getattr(agent_justice_protocol, "__version__", "0.1.0"),
            initialized=True,
            store_path=str(self.storage_root / "ajp"),
        )

        asa_status = ProtocolStatus(
            name="Agent Service Agreements",
            version=getattr(agent_service_agreements, "__version__", "0.1.0"),
            initialized=True,
            store_path=str(self.storage_root / "asa"),
        )

        alp_status = ProtocolStatus(
            name="Agent Lifecycle Protocol",
            version=getattr(agent_lifecycle_protocol, "__version__", "0.1.0"),
            initialized=True,
            store_path=str(self.storage_root / "alp"),
        )

        amp_status = ProtocolStatus(
            name="Agent Matchmaking Protocol",
            version=getattr(agent_matchmaking, "__version__", "0.1.0"),
            initialized=True,
            store_path=str(self.storage_root / "amp"),
        )

        cwep_status = ProtocolStatus(
            name="Context Window Economics",
            version=getattr(context_window_economics, "__version__", "0.1.0"),
            initialized=True,
            store_path=str(self.storage_root / "cwep"),
        )

        return {
            "coc": coc_status,
            "arp": arp_status,
            "ajp": ajp_status,
            "asa": asa_status,
            "alp": alp_status,
            "amp": amp_status,
            "cwep": cwep_status,
        }

    def status_summary(self) -> str:
        """Return a human-readable status summary string."""
        statuses = self.status()
        lines = [
            f"Agent Trust Stack — {self.agent_id}",
            f"Storage: {self.storage_root}",
            "",
        ]
        for key, s in statuses.items():
            marker = "OK" if s.initialized else "NOT INITIALIZED"
            count = f" ({s.entry_count} entries)" if s.entry_count else ""
            lines.append(f"  [{marker}] {s.name} v{s.version}{count}")
            if s.details:
                for dk, dv in s.details.items():
                    lines.append(f"         {dk}: {dv}")
        return "\n".join(lines)

    def verify_all(self) -> Dict[str, bool]:
        """Run verification across all protocols that support it."""
        results = {}

        # CoC chain verification
        entries = self.coc.entries
        if entries:
            results["coc_chain_valid"] = self.coc.verify().valid
        else:
            results["coc_chain_valid"] = True  # empty chain is trivially valid

        # ARP — check if we have any ratings
        arp_ratings = self.arp_store.get_all() if hasattr(self.arp_store, "get_all") else []
        results["arp_ratings_count"] = len(arp_ratings)

        return results

    def __repr__(self) -> str:
        return f"TrustStack(agent_id={self.agent_id!r}, storage={self.storage_root!s})"
