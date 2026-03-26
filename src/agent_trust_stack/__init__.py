"""
Agent Trust Stack — Complete institutional infrastructure for the autonomous agent economy.

One install gives you all seven trust protocols:
  - Chain of Consciousness (CoC) — provenance
  - Agent Rating Protocol (ARP) — reputation
  - Agent Justice Protocol (AJP) — accountability
  - Agent Service Agreements (ASA) — contracts
  - Agent Lifecycle Protocol (ALP) — lifecycle management
  - Agent Matchmaking Protocol (AMP) — discovery
  - Context Window Economics Protocol (CWEP) — cost allocation

Quick start:
    from agent_trust_stack import TrustStack

    stack = TrustStack(agent_id="did:example:agent-1")
    stack.coc.add("boot", "System initialized")
    stack.arp.store.append(rating_record)
    stack.status()

VAM-SEC DISCLAIMER: This software is provided for research and development
purposes. It has not been independently audited for production security.
Deployments handling real economic value should undergo professional security
review. See https://vibeagentmaking.com for details.

License: Apache 2.0
"""

__version__ = "0.1.0"
__all__ = [
    "TrustStack",
    # Protocol re-exports
    "CoC", "Chain", "ChainEntry", "VerifyResult",
    "ARP", "RatingRecord", "RatingStore", "BlindExchange",
    "AJP", "ForensicInvestigation", "IncidentReport", "Dispute", "RiskEngine", "JusticeStore",
    "ASA", "Agreement", "AgreementStore", "VerificationEngine", "NegotiationSession",
    "ALP", "AgentRecord", "LifecycleManager", "LifecycleStore",
    "AMP", "UnifiedCapabilityProfile", "UCPBuilder", "MatchRequest", "MatchmakingStore",
    "CWEP", "Meter", "CostMeteringRecord", "SettlementEngine", "CWEPStore",
    # Integration
    "IntegrationBus",
]

# --- Protocol re-exports ---

# CoC — Chain of Consciousness (provenance)
from chain_of_consciousness import Chain, ChainEntry, VerifyResult
import chain_of_consciousness as CoC

# ARP — Agent Rating Protocol (reputation)
from agent_rating_protocol import RatingRecord, RatingStore, BlindExchange
import agent_rating_protocol as ARP

# AJP — Agent Justice Protocol (accountability)
from agent_justice_protocol import (
    ForensicInvestigation, IncidentReport, Dispute, RiskEngine, JusticeStore,
)
import agent_justice_protocol as AJP

# ASA — Agent Service Agreements (contracts)
from agent_service_agreements import (
    Agreement, AgreementStore, VerificationEngine, NegotiationSession,
)
import agent_service_agreements as ASA

# ALP — Agent Lifecycle Protocol (lifecycle)
from agent_lifecycle_protocol import AgentRecord, LifecycleManager, LifecycleStore
import agent_lifecycle_protocol as ALP

# AMP — Agent Matchmaking Protocol (discovery)
from agent_matchmaking import (
    UnifiedCapabilityProfile, UCPBuilder, MatchRequest, MatchmakingStore,
)
import agent_matchmaking as AMP

# CWEP — Context Window Economics Protocol (cost allocation)
from context_window_economics import (
    Meter, CostMeteringRecord, SettlementEngine, CWEPStore,
)
import context_window_economics as CWEP

# --- Integration layer ---
from agent_trust_stack.trust_stack import TrustStack
from agent_trust_stack.integration import IntegrationBus
