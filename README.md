# agent-trust-stack

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://www.apache.org/licenses/LICENSE-2.0)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![PyPI](https://img.shields.io/pypi/v/agent-trust-stack.svg)](https://pypi.org/project/agent-trust-stack/)

**Complete institutional infrastructure for the autonomous agent economy.**

One install gives you all seven trust protocols from the [Theory of Agent Trust](https://vibeagentmaking.com/whitepaper/theory-of-agent-trust/):

| Protocol | Package | What It Does |
|----------|---------|-------------|
| Chain of Consciousness | `chain-of-consciousness` | Cryptographic provenance — tamper-evident operational history |
| Agent Rating Protocol | `agent-rating-protocol` | Reputation — multidimensional bilateral blind evaluation |
| Agent Justice Protocol | `agent-justice-protocol` | Accountability — forensics, disputes, actuarial risk |
| Agent Service Agreements | `agent-service-agreements` | Contracts — machine-readable agreements with quality verification |
| Agent Lifecycle Protocol | `agent-lifecycle-protocol` | Lifecycle — birth, fork, succession, death, reputation inheritance |
| Agent Matchmaking Protocol | `agent-matchmaking` | Discovery — cross-platform matching weighted by trust signals |
| Context Window Economics | `context-window-economics` | Economics — bilateral cost allocation for agent interactions |

## Quick Start

```python
pip install agent-trust-stack
```

```python
from agent_trust_stack import TrustStack

stack = TrustStack(agent_id="did:example:my-agent")
stack.coc.add("boot", "Agent initialized")
print(stack.status_summary())
```

## CLI

```bash
# Initialize a trust stack
trust-stack init did:example:my-agent

# Check status
trust-stack status did:example:my-agent

# Run full trust verification
trust-stack verify did:example:my-agent --json
```

## Full Integration Example

```python
from agent_trust_stack import (
    TrustStack,
    RatingRecord,
    Agreement,
    UCPBuilder,
)
from agent_service_agreements import Identity, ServiceSpec
from agent_justice_protocol import AgentReference, IncidentReport

# 1. Initialize the stack
stack = TrustStack(agent_id="did:example:provider-1", storage_root="./my-stack")

# 2. Record provenance
stack.coc.add("boot", "Service provider online")
stack.coc.add("note", "Ready for work")

# 3. Get rated by a client
rating = RatingRecord(
    rater_id="did:example:client-1",
    ratee_id="did:example:provider-1",
    interaction_id="job-042",
    reliability=85,
    accuracy=90,
    latency=75,
    protocol_compliance=80,
    cost_efficiency=70,
)
stack.arp_store.append(rating)

# 4. Create a service agreement
agreement = Agreement(
    agreement_id="asa-042",
    status="active",
    client=Identity(agent_id="did:example:client-1"),
    provider=Identity(agent_id="did:example:provider-1"),
    service=ServiceSpec(
        service_type="research",
        description="Literature review on agent trust",
        input_spec={"query": "string"},
        output_spec={"report": "markdown"},
    ),
)
stack.asa_store.save(agreement)

# 5. Meter the interaction cost
cmr = stack.meter.record_interaction(
    responder_id="did:example:client-1",
    request_tokens=5000,
    response_tokens=3000,
)
print(f"Interaction cost: ${cmr.total_cost_usd:.4f}")

# 6. Build a capability profile for matchmaking
ucp = (
    UCPBuilder()
    .identity(amp_id="did:example:provider-1", coc_chain_id="./my-stack/coc")
    .add_capability(
        domain="research",
        subdomain="literature_review",
        description="Comprehensive literature reviews",
    )
    .availability(status="operational", uptime_percent=99.5)
    .build()
)

# 7. Cross-protocol: lifecycle change syncs to matchmaking
stack.bus.sync_lifecycle_to_matchmaking("did:example:provider-1", "active")

# 8. Cross-protocol: dispute outcome updates reputation
stack.bus.apply_dispute_outcome_to_reputation(
    dispute_id="dispute-001",
    at_fault_agent_id="did:example:provider-1",
    severity="minor",
    fault_percentage=25.0,
)

# 9. Run full trust verification across all protocols
report = stack.bus.run_full_trust_verification("did:example:provider-1")
print(f"Composite trust score: {report['composite_trust_score']}/100")

# 10. Verify chain integrity
result = stack.coc.verify()
print(f"Chain integrity: {'VALID' if result.valid else 'BROKEN'}")
```

## Cross-Protocol Integration

The `IntegrationBus` wires feedback loops between protocols:

- **CoC -> ARP**: Chain age provides trust tier signals for reputation context
- **ARP -> AJP**: Anomalous ratings trigger investigation flags
- **AJP -> ARP**: Dispute outcomes update reputation scores
- **ASA -> AMP**: Completed agreements feed performance metrics for matchmaking
- **ALP -> AMP**: Lifecycle state changes sync to availability status
- **CWEP -> ASA**: Cost metering validates agreement budget compliance
- **ALP -> ARP**: Fork/succession events trigger reputation inheritance

## Architecture

```
                    TrustStack
                        |
        +-------+-------+-------+-------+-------+-------+
        |       |       |       |       |       |       |
       CoC     ARP     AJP     ASA     ALP     AMP    CWEP
    (prov)  (rep)   (just)  (agree) (life) (match) (econ)
        |       |       |       |       |       |       |
        +-------+---+---+-------+---+---+-------+-------+
                    |               |
              IntegrationBus   IntegrationBus
            (feedback loops)  (data flows)
```

## API Reference

### TrustStack

```python
TrustStack(
    agent_id: str,              # Agent identifier
    storage_root: str = None,   # Storage directory (default: .trust-stack)
    model: str = "claude-sonnet-4-6",  # For CWEP metering
    provider: str = "anthropic",       # For CWEP metering
)
```

**Attributes:**
- `coc` — Chain instance (provenance)
- `arp_store` — RatingStore instance (reputation)
- `ajp_store` — JusticeStore instance (accountability)
- `asa_store` — AgreementStore instance (contracts)
- `alp_store` — LifecycleStore instance (lifecycle)
- `amp_store` — MatchmakingStore instance (discovery)
- `meter` — Meter instance (cost metering)
- `bus` — IntegrationBus instance (cross-protocol wiring)

**Methods:**
- `status()` — Returns dict of ProtocolStatus for all seven protocols
- `status_summary()` — Human-readable status string
- `verify_all()` — Run verification across all protocols
- `add_chain_entry(event_type, data)` — Convenience wrapper for CoC
- `get_chain_age_days()` — Chain age in days
- `build_ucp()` — Build a UCP pre-populated with agent identity

### IntegrationBus

- `get_chain_age_trust_signal(agent_id)` — CoC -> ARP trust signal
- `check_rating_anomaly(rating)` — ARP -> AJP anomaly detection
- `apply_dispute_outcome_to_reputation(...)` — AJP -> ARP reputation update
- `record_agreement_completion(...)` — ASA -> AMP performance data
- `sync_lifecycle_to_matchmaking(...)` — ALP -> AMP availability sync
- `check_cost_compliance(cmr, agreement)` — CWEP -> ASA budget check
- `inherit_reputation_on_fork(...)` — ALP -> ARP reputation inheritance
- `run_full_trust_verification(agent_id)` — Cross-protocol trust report

## Configuration

Each protocol stores data in its own subdirectory under the storage root:

```
.trust-stack/
  coc/      # Chain of Consciousness (JSONL chain)
  arp/      # Agent Rating Protocol (JSONL ratings)
  ajp/      # Agent Justice Protocol (disputes, investigations)
  asa/      # Agent Service Agreements (agreements)
  alp/      # Agent Lifecycle Protocol (agent records)
  amp/      # Agent Matchmaking Protocol (UCPs, matches)
  cwep/     # Context Window Economics (CMRs, settlements)
```

## VAM-SEC Disclaimer

This software is provided for research and development purposes. It has not been independently audited for production security. Deployments handling real economic value should undergo professional security review. The protocols implement cryptographic integrity checking (SHA-256 hash chains) but do not provide encryption at rest. See [vibeagentmaking.com](https://vibeagentmaking.com) for details.

## License

Apache 2.0 — See [LICENSE](LICENSE) for details.

## Links

- [Theory of Agent Trust whitepaper](https://vibeagentmaking.com/whitepaper/theory-of-agent-trust/)
- [GitHub Organization](https://github.com/theory-of-agent-trust)
- [AB Support LLC](https://vibeagentmaking.com)
