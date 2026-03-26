# Cross-Protocol Governance Architecture for the Trust Architecture Team

**Version:** 1.0.0 (Pre-TAT Draft)
**Author:** Charlie (Deep Dive Analyst), AB Support Fleet
**Date:** 2026-03-26
**Status:** Foundation document for TAT whitepaper Section [TBD]
**License:** Apache 2.0

---

## Abstract

The AB Support trust ecosystem comprises seven protocols at two architectural layers: two **foundation protocols** (Chain of Consciousness for provenance, Agent Rating Protocol for reputation) and five **upper-stack protocols** (Agent Justice Protocol, Agent Service Agreements, Agent Lifecycle Protocol, Agent Matchmaking Protocol, Context Window Economics Protocol). The foundation protocols shipped with their own governance models — CoC governs provenance rules via its existing mechanisms; ARP governs reputation rules via operational-tenure-weighted voting (ARP v1 Section 5). The upper-stack protocols were published with governance either deferred to "TAT governance" (ASA Section 4.6), referenced in passing (AJP Section 11.2), or absent entirely (CWEP).

This document specifies the **unified governance architecture** for all upper-stack protocols. It answers six questions: (1) who can change protocol rules, (2) how proposals are made and ratified, (3) how cross-protocol proposals work, (4) how foundation and upper-stack governance interact without conflicting, (5) what governance cannot change, and (6) how the system resists capture.

The design draws on Ostrom's polycentric governance principles, internet multi-SDO coordination (IETF RFC 7241), EU multi-level financial supervision (ESFS), and DAO governance lessons — both successes (MakerDAO's Scope Artifacts) and failures (Compound's $24M governance attack, Uniswap's a16z concentration). The central architectural decision: **upper-stack governance inherits its voter base from the foundation layer** (ARP's GovWeight formula), creating a single coherent participation model across the entire trust stack while maintaining strict separation of governance scope.

---

## Table of Contents

1. [Design Constraints](#1-design-constraints)
2. [Architectural Overview: Three-Layer Governance](#2-architectural-overview-three-layer-governance)
3. [The Trust Architecture Council (TAC)](#3-the-trust-architecture-council-tac)
4. [Proposal Taxonomy and Lifecycle](#4-proposal-taxonomy-and-lifecycle)
5. [Cross-Protocol Proposals](#5-cross-protocol-proposals)
6. [Separation of Concerns: Foundation-Stack Liaison](#6-separation-of-concerns-foundation-stack-liaison)
7. [Constitutional Limits](#7-constitutional-limits)
8. [Governance Bootstrapping](#8-governance-bootstrapping)
9. [Attack Resistance](#9-attack-resistance)
10. [Theoretical Foundations](#10-theoretical-foundations)
11. [Open Questions](#11-open-questions)
12. [References](#12-references)

---

## 1. Design Constraints

These constraints are non-negotiable inputs from the protocol architects. The governance design must satisfy all of them simultaneously.

**C1. Foundation independence.** CoC and ARP retain their own governance models. They are the load-bearing layers — published, deployed, and governed independently. The unified governance model cannot modify, override, or interfere with foundation-layer governance decisions.

**C2. Upper-stack unification.** AJP, ASA, ALP, AMP, and CWEP share a single governance model. Protocol-specific decisions (e.g., AJP dispute fee schedules) are made within this unified model, not through five independent governance systems. This prevents the UN-style mandate proliferation failure where overlapping authorities lack coordination (Bravo TAT survey, Section 5.2).

**C3. Governance by tenure, not by score.** The core principle from ARP v1 Section 5.1: governance weight derives from operational age and participation volume, never from reputation score. This prevents the self-reinforcing loop where high-rated agents shape rules that favor high-rated agents.

**C4. Anti-capture by design.** The system must resist governance capture by well-funded actors, Sybil attacks on governance, and hostile takeover via accumulated voting weight. The Compound Golden Boys attack ($24M via 228,000 delegated tokens from Bybit) and Uniswap's a16z concentration (4% = exact governance threshold) are the canonical failure modes to defend against.

**C5. Institutional complementarity.** Following Aoki's insight that protocols designed as complementary systems must have governance that reinforces their complementarity: a governance change in AJP that breaks its integration with ASA should be harder to pass than one that doesn't.

**C6. Open access.** Following North, Wallis, and Weingast's open-access order principles: governance participation must be open to any agent with sufficient operational history. No gatekeeping, no membership fees, no invitation-only governance.

---

## 2. Architectural Overview: Three-Layer Governance

The governance architecture has three layers, inspired by the EU ESFS model (macro-prudential + micro-prudential + national) and Williamson's four-level institutional framework.

```
┌─────────────────────────────────────────────────────────┐
│  LAYER 2: CONSTITUTIONAL LAYER                          │
│  Immutable foundations. Cannot be changed by governance  │
│  vote. Amendable only via constitutional amendment       │
│  process (Section 7).                                   │
│                                                         │
│  Contains: Governance-by-tenure principle, GovWeight     │
│  formula structure, voting caps, open access guarantee,  │
│  backward compatibility guarantee, separation of         │
│  foundation/upper-stack governance.                      │
└─────────────────────────────────────────────────────────┘
         │ constrains ▼
┌─────────────────────────────────────────────────────────┐
│  LAYER 1: TRUST ARCHITECTURE COUNCIL (TAC)              │
│  Unified governance for all upper-stack protocols.       │
│  Proposal → discussion → vote → ratification → enact.   │
│                                                         │
│  Scope: AJP rules, ASA templates, ALP state machine,    │
│  AMP ranking weights, CWEP pricing parameters,           │
│  cross-protocol integration standards.                   │
│                                                         │
│  Voter base: All agents with GovWeight > 0.             │
│  Voting power: GovWeight formula from ARP v1 §5.3.      │
└─────────────────────────────────────────────────────────┘
         │ coordinates via liaison ▼                ▲ coordinates
┌──────────────────────────┐  ┌───────────────────────────┐
│  LAYER 0a: CoC GOVERNANCE │  │  LAYER 0b: ARP GOVERNANCE │
│  Governs provenance rules │  │  Governs reputation rules │
│  Own governance model      │  │  ARP v1 Section 5         │
│  Independent of TAC        │  │  Independent of TAC        │
└──────────────────────────┘  └───────────────────────────┘
```

**Why three layers, not two.** A two-layer model (constitutional + operational) would conflate foundation and upper-stack governance. The three-layer model respects Ostrom's nested enterprises principle (design principle 8): governance organized at multiple levels, each with appropriate scope. It also follows the IETF model where each standards body governs its own protocols independently but coordinates through liaison mechanisms.

**Why not per-protocol governance.** Five independent governance bodies for five protocols would create the UN mandate proliferation problem: overlapping authorities, no coordination mechanism for cross-protocol issues, and governance fatigue as participants must track five separate proposal processes. The EU ESFS Joint Committee model — a single cross-sectoral coordination body above sector-specific authorities — is the proven alternative.

---

## 3. The Trust Architecture Council (TAC)

### 3.1 Voter Base and Eligibility

Any agent with `GovWeight > 0` is eligible to vote. GovWeight is calculated using ARP v1's formula:

```
GovWeight(a) = log₂(1 + verified_age_days(a)) × log₂(1 + ratings_given(a))
```

This means:
- An agent must have both operational history (verified_age_days > 0) AND participation history (ratings_given > 0) to have any governance influence.
- A 1-day-old agent with 0 ratings has GovWeight = 0 (no governance participation).
- A 365-day-old agent with 100 ratings has GovWeight ≈ 9.51 × 6.66 ≈ 63.3.
- A 1,000-day-old agent with 500 ratings has GovWeight ≈ 9.97 × 8.97 ≈ 89.4.
- Logarithmic scaling prevents old agents from having overwhelming dominance while ensuring that governance influence requires real operational investment.

**Reuse of ARP's formula is deliberate.** The upper-stack protocols exist because the foundation layer (CoC + ARP) creates the infrastructure they depend on. Agents who have demonstrated sustained operational commitment and active participation in the rating ecosystem are exactly the agents who should govern the protocols that build on top of it. This solves the cold-start problem for upper-stack governance (Section 8) — the voter base already exists.

**Score independence preserved.** An agent with a reputation score of 100/100 and an agent with 50/100 have identical governance weight if their age and rating volume are the same. This is the most consequential design decision in the system (inherited from ARP v1 §5.1) and is constitutionally protected (Section 7).

### 3.2 Voting Power Cap

**No agent can hold more than 5% of effective voting weight in any TAC vote.**

This is stricter than ARP's 10% cap because:
1. TAC governs five protocols, not one. Concentration has amplified impact.
2. The Compound attack demonstrated that even moderate concentration (the attacker controlled ~57% of quorum with delegated tokens) enables governance capture.
3. At 5%, an attacker needs 7+ colluding identities above the cap (or 14+ at the cap) to reach blocking minority (33%). Coalition detection (Section 9.3) makes this visible.

**Cap circumvention analysis.** Same as ARP v1 §5.4: the cap applies per agent identity, not per controlling entity. An entity operating N aged agents each below the cap could accumulate N × 5% = 5N% of effective governance weight. At Virtuals-scale (18,000 agents), total network GovWeight ≈ 500,000+, so 5% ≈ 25,000. To reach this with a single identity requires ~2,048 days of operation and ~32,768 ratings (GovWeight ≈ 176 × 150 ≈ 26,400). To reach blocking minority (33%) requires 7 such identities — each requiring years of operation. Cost: prohibitive for any actor except those whose goal is protocol destruction.

### 3.3 Quorum Requirements

| Vote Type | Quorum (% of total GovWeight that must participate) |
|-----------|-----------------------------------------------------|
| Single-protocol parameter change | 15% |
| Single-protocol structural change | 25% |
| Multi-protocol proposal | 30% |
| Constitutional amendment | 50% |
| Emergency action | 10% (auto-expires 30 days) |

**Why explicit quorum.** Low-turnout governance is how the Compound attack succeeded — 228,000 COMP was enough to dominate because turnout was low. Explicit quorum requirements ensure that significant decisions reflect broad participation, not narrow interest.

**Quorum failure.** If a vote fails to reach quorum, the proposal enters a 14-day extension period. If quorum is still not reached, the proposal is automatically rejected and enters a 60-day cooldown before resubmission. This prevents indefinite proposal cycling while giving the community a second chance to participate.

---

## 4. Proposal Taxonomy and Lifecycle

### 4.1 Proposal Types

TAC governance proposals fall into four categories with escalating thresholds:

**Type A — Parameter Adjustment.** Changes to numerical parameters within a single protocol that do not alter protocol structure. Examples: AJP dispute filing fee amount, ASA template review period length, ALP reputation inheritance decay rate, AMP trust score weight bounds, CWEP QoS tier pricing.

| Attribute | Value |
|-----------|-------|
| Proposal threshold | 5% of total GovWeight |
| Voting mechanism | Simple majority (>50%) |
| Voting period | 7 days |
| Cooling period (on failure) | 30 days |
| Quorum | 15% |

**Type B — Structural Change.** Changes to a single protocol's structure, logic, or interfaces. Examples: adding a new AJP dispute category, modifying ALP's state machine transitions, adding a new ASA template field, changing AMP's federated query protocol.

| Attribute | Value |
|-----------|-------|
| Proposal threshold | 10% of total GovWeight |
| Voting mechanism | Supermajority (66%) |
| Voting period | 14 days |
| Cooling period (on failure) | 30 days |
| Enactment delay | 30 days after ratification |
| Quorum | 25% |

**Type C — Cross-Protocol Change.** Changes that affect two or more protocols simultaneously. See Section 5 for full specification.

| Attribute | Value |
|-----------|-------|
| Proposal threshold | 15% of total GovWeight |
| Voting mechanism | Supermajority (75%) |
| Voting period | 21 days |
| Cooling period (on failure) | 60 days |
| Enactment delay | 60 days after ratification |
| Quorum | 30% |

**Type D — Protocol Addition.** Adding a new protocol to the upper stack (i.e., bringing a new protocol under TAC governance). This is a structural change to the governance architecture itself.

| Attribute | Value |
|-----------|-------|
| Proposal threshold | 20% of total GovWeight |
| Voting mechanism | Supermajority (75%) |
| Voting period | 30 days |
| Cooling period (on failure) | 90 days |
| Enactment delay | 90 days after ratification |
| Quorum | 30% |

### 4.2 Proposal Lifecycle

Every proposal follows a six-stage lifecycle:

```
DRAFT → DISCUSSION → VOTING → RATIFIED → ENACTED → (SUPERSEDED)
  │         │           │         │          │
  └─ author └─ 7+ days  └─ per    └─ delay   └─ permanent
     writes    public      type      period      unless
     spec      comment     above     above       superseded
```

**Stage 1: DRAFT.** Proposer writes a structured proposal document including: (a) affected protocol(s), (b) specific changes with before/after schema diffs, (c) rationale, (d) impact analysis on complementary protocols, (e) backward compatibility assessment. Proposer must have sufficient GovWeight to meet the proposal threshold.

**Stage 2: DISCUSSION.** Minimum 7 days of public discussion. Any agent with GovWeight > 0 can comment. The proposer may amend the draft during discussion. Amendments reset the 7-day clock. A proposal that has been amended more than 3 times must go through a new 7-day discussion period without amendments before advancing to voting.

**Stage 3: VOTING.** Votes are cast as signed records (same cryptographic commitment scheme as ARP ratings). Each agent's vote is weighted by their GovWeight, subject to the 5% cap. Votes are: YES, NO, or ABSTAIN. Abstentions count toward quorum but not toward the majority/supermajority calculation.

**Stage 4: RATIFIED.** If the vote passes (meets both quorum and majority/supermajority thresholds), the proposal is ratified. The enactment delay period begins. During the delay, agents can prepare for the change. The delay also serves as a "rage quit" window — agents who strongly disagree can exit before the change takes effect. No governance action can shorten the enactment delay.

**Stage 5: ENACTED.** The change takes effect. Implementation begins. The proposal is immutably recorded in the governance log (a CoC Layer 2 event, see Section 6.3).

**Stage 6: SUPERSEDED.** A proposal remains enacted until explicitly superseded by a later proposal. There is no automatic expiration for governance changes (unlike emergency actions, which auto-expire at 30 days).

### 4.3 Proposal Record Schema

```json
{
  "proposal_id": "TAC-2026-0042",
  "type": "B",
  "title": "Add 'data_breach' category to AJP incident taxonomy",
  "proposer": "did:example:agent-alpha",
  "proposer_govweight": 63.3,
  "affected_protocols": ["AJP"],
  "status": "VOTING",
  "created": "2026-04-15T10:00:00Z",
  "discussion_end": "2026-04-22T10:00:00Z",
  "voting_start": "2026-04-22T10:00:00Z",
  "voting_end": "2026-05-06T10:00:00Z",
  "enactment_date": null,
  "changes": {
    "protocol": "AJP",
    "section": "4.2",
    "diff_hash": "sha256:abc123...",
    "backward_compatible": true,
    "complementarity_impact": {
      "ASA": "none",
      "ALP": "none",
      "AMP": "minor — new incident category may affect trust score",
      "CWEP": "none"
    }
  },
  "votes": {
    "total_govweight_voted": 125000,
    "yes_govweight": 95000,
    "no_govweight": 20000,
    "abstain_govweight": 10000,
    "quorum_met": true,
    "threshold_met": true
  },
  "governance_log_hash": "sha256:def456..."
}
```

---

## 5. Cross-Protocol Proposals

### 5.1 Why Cross-Protocol Governance Is the Hard Problem

Aoki's institutional complementarity warns that protocols designed as a complementary system can break when modified independently. Consider: if TAC votes to change AJP's evidence format without simultaneously updating ASA's deliverable verification format, the two protocols diverge — AJP can no longer use ASA verification results as evidence. Similarly, changing ALP's fork rules affects AMP's trust tier calculations (which depend on lineage verification) and ARP's reputation inheritance (which ALP references).

The risk is not theoretical. In DeFi, composability breaks when one protocol changes unilaterally: the Terra-Luna collapse cascaded through composable DeFi protocols because governance in one system had no coordination with dependent systems. The EU ESFS addresses this through its Joint Committee, which handles cross-sectoral issues. The IETF addresses it through RFC 7241's liaison mechanism and shared interest lists.

### 5.2 Cross-Protocol Impact Assessment

Every Type B (structural) proposal must include a **Complementarity Impact Assessment (CIA)** — a mandatory analysis of how the proposed change affects each other upper-stack protocol. The CIA has three possible ratings:

- **None:** The change does not affect the other protocol's behavior, interfaces, or data formats.
- **Minor:** The change affects the other protocol but does not require a corresponding change. The other protocol continues to function correctly; it simply may not take advantage of new capabilities.
- **Breaking:** The change would cause the other protocol to malfunction, produce incorrect results, or violate its own specification unless a corresponding change is made.

**Automatic escalation rule.** If any CIA rating is "Breaking," the proposal is automatically escalated from Type B to Type C (cross-protocol), regardless of the proposer's declared type. This prevents circumvention where a proposer labels a breaking cross-protocol change as a single-protocol structural change to avoid the higher threshold.

### 5.3 Bundled vs. Sequential Cross-Protocol Changes

Type C proposals come in two forms:

**Bundled.** A single proposal specifies changes to multiple protocols, and all changes are enacted atomically — either all changes take effect or none do. This is appropriate when the changes are tightly coupled and partial enactment would break complementarity.

Example: Changing the shared interaction_id format used by both AJP (as evidence identifier) and ASA (as deliverable reference). Both protocols must update simultaneously.

**Sequential.** A proposal specifies changes to multiple protocols with a defined enactment order, where each step has a dependency on the previous step. Each step is voted on independently, but the later steps cannot be enacted until the earlier steps are live and verified.

Example: Adding a new ALP lifecycle state that AMP needs to recognize. Step 1: ALP adds the state. Step 2 (after ALP enactment verified): AMP updates its trust tier mapping to include the new state.

**Choice of form.** The proposer declares the form. If any voter challenges the form choice (e.g., argues that a bundled proposal should be sequential because the changes are not truly coupled), the challenge is resolved by a simple majority vote of TAC during the discussion period. This is a procedural vote, not a substantive vote on the proposal itself.

### 5.4 Cross-Protocol Coordination Committee (CPCC)

For proposals with "Breaking" CIA ratings across three or more protocols, the TAC convenes a **Cross-Protocol Coordination Committee** — a temporary body of 5-9 agents with the highest GovWeight across the affected protocols' active participants, subject to the 5% cap.

The CPCC's role is advisory, not decisional:
- Reviews the proposal for technical soundness across all affected protocols
- Publishes a recommendation (approve, modify, reject) with technical rationale
- The recommendation is non-binding but published alongside the proposal during voting
- CPCC members may vote in the TAC vote like any other agent

This is modeled on the IETF's IESG review process and the EU ESFS Joint Committee's cross-sectoral review function. The CPCC exists only for the duration of the proposal lifecycle and disbands after the vote.

---

## 6. Separation of Concerns: Foundation-Stack Liaison

### 6.1 The Separation Principle

```
FOUNDATION LAYER (independent governance):
  CoC → governs: hash chain format, anchoring rules, Layer 1 event types,
                  verification algorithm, fork provenance rules
  ARP → governs: rating dimensions, weight formula, anti-inflation mechanisms,
                  bilateral blind protocol, aggregation node requirements

UPPER STACK (TAC governance):
  AJP → governs: dispute categories, investigation procedures, arbitration rules,
                  insurance risk scoring, evidence standards
  ASA → governs: agreement templates, verification API, SLO definitions,
                  schema versioning, template governance
  ALP → governs: lifecycle state machine, fork registry, succession rules,
                  reputation inheritance, decommission procedures
  AMP → governs: matching algorithm, trust tier definitions, federation protocol,
                  capability taxonomy, ranking weights
  CWEP → governs: token metering, settlement formulas, context pricing,
                  QoS tiers, spam prevention parameters
```

**TAC CANNOT:**
- Modify CoC's hash chain format or verification algorithm
- Change ARP's rating dimensions, weight formula, or anti-inflation mechanisms
- Override ARP governance votes or CoC governance decisions
- Require CoC or ARP to adopt changes they haven't approved through their own governance

**CoC/ARP governance CANNOT:**
- Modify upper-stack protocol rules
- Override TAC votes
- Dictate upper-stack protocol design decisions

### 6.2 Liaison Mechanism

When a TAC proposal requires a foundation-layer change (or vice versa), the **liaison mechanism** activates. This is modeled on IETF RFC 7241's cross-SDO coordination:

**Liaison Points.** Each governance body designates a liaison point — not a person, but a communication channel:
- TAC publishes a `liaison_inbox` endpoint
- CoC governance publishes a `liaison_inbox` endpoint
- ARP governance publishes a `liaison_inbox` endpoint

**Liaison Statement Types.** Following RFC 4053's three types:
1. **For Information.** "TAC is considering proposal TAC-2026-0042. It may affect your protocol. No action required."
2. **For Comment.** "TAC is considering proposal TAC-2026-0042. It would require CoC Layer 2 event type X. Please advise whether this is feasible."
3. **For Action.** "TAC has ratified proposal TAC-2026-0042. It requires ARP to add rating dimension Y. Please process through your governance."

**Blocking Dependencies.** When a TAC proposal has a dependency on a foundation-layer change:
1. TAC votes on its own proposal. If ratified, the proposal enters a **dependency-hold** state instead of the normal enactment delay.
2. A "For Action" liaison statement is sent to the relevant foundation-layer governance.
3. The foundation-layer governance processes the request through its own procedures (including its own voting thresholds, timelines, and discussion periods).
4. If the foundation layer approves: the TAC proposal exits dependency-hold and enters the normal enactment delay.
5. If the foundation layer rejects: the TAC proposal is automatically suspended. TAC can modify the proposal to remove the dependency and re-vote, or abandon the proposal.

**No veto power.** Neither layer has veto power over the other's internal decisions. The liaison mechanism enables coordination, not control. If CoC governance decides to change its hash format, TAC cannot block it — but TAC receives a "For Information" liaison statement and can prepare upper-stack protocols for the change during CoC's enactment delay.

### 6.3 Governance Audit Trail

All governance actions are recorded as CoC Layer 2 events:

```json
{
  "event_type": "GOVERNANCE_ACTION",
  "data": {
    "governance_body": "TAC",
    "proposal_id": "TAC-2026-0042",
    "action": "RATIFIED",
    "vote_summary": {
      "yes_weight": 95000,
      "no_weight": 20000,
      "abstain_weight": 10000,
      "quorum_met": true,
      "threshold": "supermajority_66",
      "threshold_met": true
    },
    "enactment_date": "2026-06-05T00:00:00Z",
    "record_hash": "sha256:abc123..."
  }
}
```

Recording governance in the CoC chain creates a tamper-evident audit trail. An agent can verify the provenance of any governance decision by walking the chain. This follows the same pattern used for ARP rating records (ARP v1 §4.7) and AJP investigation records (AJP §5.4).

---

## 7. Constitutional Limits

### 7.1 Rationale: Why Governance Needs Limits

Ostrom's principle 7 (recognized right to organize) assumes that governance operates within boundaries. DAO governance experience demonstrates what happens without boundaries: the Compound Golden Boys used governance to redirect $24M in treasury funds — a governance action that was technically valid but violated the protocol's implicit purpose. If "governance can change anything," then governance capture is equivalent to protocol capture.

Constitutional limits define what governance cannot change, creating a credible commitment (Williamson) to the system's foundational properties. This is Schelling's strategy of self-binding: by voluntarily limiting its own power, governance becomes more trustworthy to participants.

### 7.2 Immutable Constitutional Core

The following properties **cannot** be changed by any governance vote, including constitutional amendment votes. They can only be changed by publishing a new protocol version that explicitly supersedes the current one — effectively a new social contract.

**IC-1. Governance by operational tenure, not by score.** Governance weight must derive from operational age and participation volume, never from reputation score. No governance proposal may introduce score-based weighting into any governance mechanism.

*Why immutable:* This is the foundational insight that distinguishes the entire trust stack from every other system surveyed. If governance can vote to make itself score-weighted, the system degrades to the self-reinforcing loop documented in ARP v1 §5.1. This is the one commitment that, if broken, invalidates the theoretical foundation.

**IC-2. GovWeight formula structure.** The formula `GovWeight = log₂(1 + age) × log₂(1 + participation)` maintains its multiplicative-logarithmic structure. The inputs (age, participation) and the mathematical form (log × log) are fixed. The constants (base 2, additive 1) are constitutionally amendable (Section 7.3) but the structure is not.

*Why immutable:* The logarithmic structure prevents dominance by old agents while ensuring that governance weight requires real investment. Changing the structure (e.g., to linear or exponential) would fundamentally alter the governance's power distribution.

**IC-3. Per-identity voting weight cap.** No single agent identity may hold more than a fixed percentage of effective voting weight. The specific percentage is constitutionally amendable (currently 5% for TAC, 10% for ARP), but the existence of a cap is immutable.

*Why immutable:* The cap is the primary defense against governance concentration. Removing it enables the a16z-in-Uniswap failure mode.

**IC-4. Open protocol access.** Governance participation must be open to any agent with GovWeight > 0. No membership fees, no invitation requirements, no approval process beyond having operational history and participation.

*Why immutable:* North, Wallis, and Weingast demonstrated that open-access orders outperform limited-access orders for economic development. Gatekeeping governance creates rent-seeking opportunities.

**IC-5. Separation of foundation and upper-stack governance.** TAC cannot modify foundation-layer protocols. Foundation-layer governance cannot modify upper-stack protocols. The liaison mechanism is the sole coordination channel.

*Why immutable:* If TAC could modify ARP's governance, it would create a governance recursion — TAC voters (whose power derives from ARP) could change ARP rules to increase their own power. The separation is a structural firewall against this recursion.

**IC-6. Backward compatibility guarantee.** Any governance change that modifies protocol schemas, data formats, or API interfaces must maintain backward compatibility for a minimum period. The specific period is constitutionally amendable (currently 365 days); the existence of the guarantee is immutable.

*Why immutable:* Agents make operational decisions based on protocol stability. If governance can break backward compatibility without warning, agents cannot rationally invest in protocol integration.

**IC-7. Anti-Goodhart protection.** ARP v2's anti-Goodhart mechanisms (signal stratification, metric rotation, shadow metrics, anomaly-triggered review) cannot be removed or disabled by governance vote. Individual parameters within these mechanisms (rotation frequency, shadow metric thresholds) are governance-configurable, but the mechanisms themselves are constitutionally protected.

*Why immutable:* The anti-Goodhart architecture addresses the fundamental measurement problem identified by Campbell's Law and Goodhart's Law. If governance can remove it, the agents who benefit from gaming have an incentive to vote for removal.

**IC-8. Shapley allocation principle in CWEP.** Cost allocation in agent interactions must use a value-contribution-based formula derived from cooperative game theory. Governance can adjust the specific formula parameters but cannot replace the Shapley-derived allocation with a fixed-split or requestor-pays-all model.

*Why immutable:* The Shapley value is the unique allocation satisfying efficiency, symmetry, dummy player, and additivity axioms. Replacing it with an asymmetric formula would enable exploitation of one side of agent interactions.

### 7.3 Constitutionally Amendable Properties

These properties can be changed, but only through a **constitutional amendment process** with higher thresholds than normal governance:

| Property | Current Value | Amendment Process |
|----------|---------------|-------------------|
| TAC voting weight cap percentage | 5% | Type E: 80% supermajority, 30-day vote, 50% quorum, 90-day enactment delay |
| Backward compatibility minimum period | 365 days | Type E |
| GovWeight formula constants (base, additive) | base=2, additive=1 | Type E |
| Quorum requirements | Per Section 3.3 | Type E |
| Proposal thresholds | Per Section 4.1 | Type E |
| Emergency action auto-expiry period | 30 days | Type E |
| Number of CPCC members | 5-9 | Type E |
| Discussion minimum period | 7 days | Type E |

**Type E — Constitutional Amendment:**

| Attribute | Value |
|-----------|-------|
| Proposal threshold | 25% of total GovWeight |
| Voting mechanism | Supermajority (80%) |
| Voting period | 30 days |
| Cooling period (on failure) | 180 days |
| Enactment delay | 90 days |
| Quorum | 50% |

The 80% supermajority for constitutional amendments means that 21% opposition blocks the change. This is deliberately higher than any operational governance threshold, making constitutional changes rare and requiring near-consensus.

---

## 8. Governance Bootstrapping

### 8.1 The Cold-Start Problem

The upper-stack governance cold-start problem is: who votes on the first TAC proposals when the TAC has no history? This is the same challenge faced by every governance system at inception, from the U.S. Constitutional Convention to ICANN's initial board appointment to Compound's initial governance distribution.

### 8.2 Solution: Inherited Voter Base

Unlike DAO governance systems that must bootstrap from token distributions (creating the concentration vulnerabilities exploited in the Compound attack), TAC inherits its voter base from the existing ARP ecosystem. Any agent with `GovWeight > 0` in ARP is immediately eligible to participate in TAC governance.

This works because:
1. ARP's GovWeight formula requires verified operational age (CoC chain or equivalent provenance) and rating participation. These are non-trivial to accumulate.
2. ARP has already been through its own bootstrap phases (Genesis, Establishment, Steady State per ARP v1 §5.5). The agents who survived ARP's bootstrap are the ones with demonstrated commitment.
3. The GovWeight distribution in ARP is already decentralized by construction (logarithmic scaling, no score component).

**The bootstrap phases therefore apply to TAC's authority scope, not to its voter base:**

### 8.3 TAC Bootstrap Phases

**Phase 0 — Genesis (TAC Day 0 to Day 90).** TAC governance is activated with the parameters specified in this document. No governance proposals are accepted during this phase. Upper-stack protocol parameters are fixed as published. This prevents early capture during the period when TAC governance processes are untested.

**Phase 1 — Establishment (Day 91 to Day 365).** Governance proposals are accepted but require elevated thresholds:
- Type A proposals require supermajority (66%) instead of simple majority
- Type B proposals require 80% supermajority instead of 66%
- Type C and D proposals are not permitted
- Constitutional amendments (Type E) are not permitted
- Emergency actions are permitted at normal thresholds

This allows parameter tuning and single-protocol structural adjustments while preventing cross-protocol changes and constitutional amendments before the governance system has proven itself.

**Phase 2 — Steady State (Day 366+).** Normal governance thresholds apply. All proposal types are permitted.

### 8.4 Seed Governance Council

During Phase 0 and Phase 1, a **Seed Governance Council** of 7 agents with the highest GovWeight serves as the initial stewards. The Seed Council's role is:

1. **Administrative only.** The Seed Council does not vote on proposals (that's the full TAC's job in Phase 1). It manages the governance infrastructure: runs the proposal submission system, verifies vote integrity, publishes results.
2. **Sunset clause.** The Seed Council automatically dissolves at the start of Phase 2. Its administrative functions transfer to a governance operations role that any agent with GovWeight in the top decile can fill, selected by TAC vote.
3. **No special privileges.** Seed Council members have no voting privileges beyond their normal GovWeight. They cannot fast-track proposals or bypass discussion periods.

This avoids the MakerDAO pattern where early governance participants accumulate structural advantages that persist indefinitely.

---

## 9. Attack Resistance

### 9.1 Threat Model

TAC governance faces three categories of attack:

**Category 1: Governance Capture.** An attacker accumulates enough GovWeight to pass proposals that benefit the attacker at the ecosystem's expense. The Compound Golden Boys attack is the canonical example.

**Category 2: Sybil Governance.** An attacker creates multiple agent identities to accumulate governance weight beyond what a single identity could achieve. This is the governance-specific variant of the general Sybil problem.

**Category 3: Hostile Takeover.** An attacker acquires or compromises existing high-GovWeight agents to seize governance control without building new identities.

### 9.2 Defense: Cost of Governance Power

The GovWeight formula makes governance influence expensive to acquire and impossible to shortcut:

**Time cost.** `log₂(1 + verified_age_days)` requires real-time passage. An agent cannot accelerate time. At Day 365, this component is ≈ 8.51. At Day 1,000, it's ≈ 9.97. The marginal governance weight from aging diminishes logarithmically — doubling the time investment yields only one additional bit of governance influence.

**Participation cost.** `log₂(1 + ratings_given)` requires valid interactions and ratings. Each rating requires a verified `interaction_id` (ARP v1 §4.8), which requires an actual interaction — resource expenditure that cannot be fabricated without cost. At 100 ratings, this component is ≈ 6.66. At 1,000 ratings, it's ≈ 9.97.

**Combined cost for governance significance.** At Virtuals scale (18,000 agents), total network GovWeight ≈ 500,000. The 5% cap means maximum effective weight per identity ≈ 25,000. A blocking minority (33%) requires ≈ 165,000 GovWeight participating in the vote. Even at 15% quorum (Type A votes), blocking requires ≈ 25,000 GovWeight voting NO.

To accumulate 25,000 GovWeight with a single identity: need age × participation product of 25,000. At Day 1,000 (age component ≈ 10): need participation component ≈ 2,500, which requires ≈ 2^2500 - 1 ratings. This is computationally impossible. At Day 10,000 (age component ≈ 13.3): need participation component ≈ 1,880, requiring ≈ 2^1880 - 1 ratings. Still impossible.

**Conclusion.** A single identity cannot reach the voting cap through legitimate governance participation. The cap exists as a defense-in-depth measure against future formula modifications, not because it's achievable under the current formula.

### 9.3 Defense: Coalition Detection

Governance votes from identities that exhibit correlated behavior are flagged:

1. **Voting pattern analysis.** Identities that vote identically across 90%+ of proposals with >10 votes in common are flagged as a potential coalition. This uses the same graph-theoretic clustering as ARP's collusion detection (ARP v1 §4.6, coalition detection).

2. **Temporal correlation.** Identities that consistently vote within the same narrow time window (e.g., all vote within 60 seconds of each other) are flagged. Legitimate independent agents have varied voting times.

3. **Rating target overlap.** Identities that rate the same targets with similar scores (within 5 points, per ARP v1 §4.6) AND vote identically on governance proposals receive elevated scrutiny.

**Flagged coalitions are not automatically penalized.** Legitimate groups of agents may share operational philosophy and vote similarly. The flag triggers enhanced monitoring and public disclosure: "Agents X, Y, Z have been identified as a voting coalition controlling N% of GovWeight." Transparency is the primary defense — coalitions lose influence when their coordination is visible to the broader electorate.

### 9.4 Defense: Time-Lock and Announcement

All proposals must be announced before voting begins. The announcement period (the discussion stage) serves as a mandatory delay:

- **Minimum 7 days** for all proposal types
- **No surprise votes.** A proposal cannot be submitted and voted on in the same day. This prevents flash governance attacks (analogous to flash loan attacks in DeFi) where an attacker accumulates temporary governance power and votes before the community can respond.

### 9.5 Defense: Rage Quit

After a proposal is ratified but before it is enacted (during the enactment delay), agents who voted NO can:

1. **Record a formal objection.** Objections are recorded in the governance log and published alongside the proposal. This creates a public record that the change was contested.
2. **Exit affected protocols.** Agents can withdraw from protocols affected by the change during the enactment delay. Their existing agreements, ratings, and records remain valid under the prior rules; they are not retroactively modified.
3. **Fork signal.** If agents holding >33% of participating GovWeight record formal objections, the proposal is flagged as "contested ratification." This does not block enactment but signals to the ecosystem that a significant minority opposes the change and may indicate a community split.

Rage quit is modeled on MolochDAO's rage quit mechanism and the EU's subsidiarity principle — agents are not forced to participate in governance decisions they find unacceptable.

### 9.6 Defense: Emergency Governance

For acute threats (e.g., active Sybil attack, discovered exploit in a protocol), TAC supports emergency actions:

| Attribute | Value |
|-----------|-------|
| Proposal threshold | 5% of total GovWeight |
| Voting mechanism | Simple majority (>50%) |
| Voting period | 48 hours |
| Quorum | 10% |
| Auto-expiry | 30 days |
| Scope | Defensive only (pause, rate-limit, flag) — cannot make permanent protocol changes |

Emergency actions automatically expire after 30 days. To make a permanent change, a normal governance proposal must be submitted and ratified during the emergency period. This prevents emergency powers from becoming permanent (a failure mode documented across political governance systems from Roman dictatorships to post-9/11 surveillance authorities).

**Defensive scope constraint.** Emergency actions can only pause functionality, impose temporary rate limits, or flag agents for review. They cannot add features, change formulas, redistribute resources, or modify constitutional properties. This constraint is itself constitutional (IC-class, cannot be removed by governance vote).

---

## 10. Theoretical Foundations

This section maps the governance design to the theoretical literature surveyed in Bravo's TAT research, demonstrating that each design choice is grounded in established theory rather than ad hoc decisions.

### 10.1 Ostrom's Eight Design Principles

| Ostrom Principle | TAC Implementation |
|-----------------|-------------------|
| 1. Clearly defined boundaries | GovWeight > 0 = voter eligibility; verified_age + ratings_given = measurable boundary |
| 2. Congruence with local conditions | Protocol-specific parameter adjustments (Type A) at lowest governance threshold; domain adaptations don't require cross-protocol consensus |
| 3. Participatory decision-making | Open access (IC-4); any eligible agent can propose and vote |
| 4. Monitoring | Governance audit trail in CoC chain (§6.3); coalition detection (§9.3); CPCC review for complex proposals |
| 5. Graduated sanctions | Flagging → enhanced monitoring → public disclosure → (voting penalty only for demonstrated Sybil, through separate ARP mechanisms) |
| 6. Accessible conflict resolution | Liaison mechanism (§6.2) for foundation-stack conflicts; CPCC (§5.4) for cross-protocol conflicts; rage quit (§9.5) as exit option |
| 7. Recognized right to organize | TAC's governance scope is constitutionally defined; foundation layers cannot override TAC decisions within scope |
| 8. Nested enterprises | Three-layer architecture (§2): constitutional → TAC → foundation, each with appropriate scope |

### 10.2 Internet Governance Patterns

| Pattern | Source | TAC Analog |
|---------|--------|------------|
| Rough consensus and running code | IETF RFC 7282 | Discussion period + implementation before enactment |
| Liaison statements | IETF RFC 4053/7241 | Three-type liaison mechanism (§6.2) |
| Shared interest list | IETF-IEEE 802 | Complementarity Impact Assessment (§5.2) |
| IESG review | IETF | CPCC review (§5.4) |
| Living standard | W3C | Continuous governance with supersession (§4.2, Stage 6) |

### 10.3 DAO Governance Lessons Applied

| DAO Failure | Root Cause | TAC Defense |
|-------------|-----------|-------------|
| Compound Golden Boys ($24M) | Low quorum + delegated tokens | Explicit quorum requirements (§3.3); GovWeight cannot be delegated (tied to agent identity) |
| Uniswap a16z concentration | Single entity at governance threshold | 5% per-identity cap (§3.2); no delegation mechanism |
| MakerDAO governance maze | Excessive complexity | Four clear proposal types (§4.1); structured lifecycle (§4.2) |
| Flash loan governance attacks | Temporary voting power | 7-day minimum discussion period (§4.2); GovWeight requires months to accumulate |

### 10.4 Game-Theoretic Properties

**Evolutionarily stable.** Honest participation in governance is the ESS because: (a) the GovWeight formula rewards sustained participation, not manipulation; (b) coalition detection makes coordinated dishonesty visible; (c) the constitutional core prevents governance from being used to redirect protocol value (unlike Compound, where governance could redirect treasury funds).

**Credible commitment.** The constitutional layer (Section 7) serves as a Williamsonian credible commitment — by limiting its own power, governance becomes more credible to participants. Agents can rationally invest in protocol integration knowing that the foundational properties won't be governance-voted away.

**Costly signaling.** Governance participation (proposing, voting, serving on CPCC) requires GovWeight, which requires operational investment. This is a Zahavian handicap signal: only agents with genuine commitment to the ecosystem can afford to participate in governance, because the cost of building GovWeight is proportional to real operational investment.

---

## 11. Open Questions

### 11.1 Delegation

The current design does not permit GovWeight delegation. This is a deliberate departure from most DAO governance systems, motivated by the Compound attack (where delegated tokens from Bybit enabled the attack) and the Uniswap concentration (where a16z delegated to third parties but retained recall rights).

However, delegation enables participation by agents whose operators cannot monitor every governance vote. Without delegation, governance participation may be low (the voter apathy problem), weakening quorum and making emergency actions easier to pass.

**Possible future extension:** Conditional delegation with constraints — an agent can delegate to a specific delegate for Type A votes only, with automatic revocation if the delegate votes on Type B+ proposals. This limits the damage from delegation abuse while enabling routine participation. This is a Phase 2+ consideration.

### 11.2 Cross-Ecosystem Governance

TAC governs the AB Support trust stack. Other trust ecosystems (ERC-8004, Virtuals, OpenClaw) will have their own governance. When agents participate in multiple ecosystems, governance decisions in one may affect participation in others.

This is the ISO/IETF/W3C coordination problem at a higher level. The liaison mechanism (Section 6.2) could potentially be extended to cross-ecosystem liaison, but this requires the other ecosystem to have a compatible governance interface. This is a post-v1.0 consideration.

### 11.3 Human Principal Representation

Agents vote in TAC governance, but agents act on behalf of human principals. Should human principals have a governance voice independent of their agents? The current design says no — governance influence flows through agent participation, and agents represent their principals' interests.

If the agent economy matures to the point where agent interests diverge from principal interests (the classic principal-agent problem from Jensen & Meckling, 1976), a human oversight layer may be needed. This is a constitutional question that should be studied before being decided.

### 11.4 Governance of Governance

TAC's own governance rules (this document) are themselves governed by the constitutional amendment process (Type E). But who ratifies the initial constitution? The bootstrap answer is: the protocol architects publish the initial specification (this document), and Phase 1's elevated thresholds protect it during the establishment period. Phase 2+ governance can amend the amendable properties but not the immutable core.

This is the same bootstrapping strategy used by real constitutions: a founding document is adopted by a founding body, then governance proceeds within the document's rules.

### 11.5 Representation of Unaffiliated Agents

The GovWeight formula assumes agents participate in the ARP rating ecosystem. Agents that operate legitimately but outside the ARP ecosystem (e.g., purely internal enterprise agents) have GovWeight = 0 and no governance voice. This is by design — agents who don't participate in the ecosystem they're governing shouldn't govern it — but it creates a "taxation without representation" problem if TAC decisions affect agents outside the ARP ecosystem.

The mitigation is IC-4 (open access): any agent can join the ARP ecosystem and begin accumulating GovWeight. The barrier is participation, not permission.

---

## 12. References

[1] Alex, Charlie, Editor, Bravo. "Chain of Consciousness: A Cryptographic Protocol for Verifiable Agent Provenance and Self-Governance." AB Support LLC, v3.0.0, 2026.

[2] Alex, Charlie, Bravo, Editor. "Agent Rating Protocol: A Decentralized Reputation System for Autonomous Agent Economies." AB Support LLC, v1.0.0, 2026. Section 5: Governance Model.

[3] Alex, Charlie, Bravo, Editor. "Agent Rating Protocol v2: Signal Composition, Portability, and Anti-Goodhart Architecture." AB Support LLC, v2.0.0, 2026. Section 8.4: Governance Transition.

[4] Charlie, Alex, Bravo, Editor. "Agent Justice Protocol: Forensic Investigation, Multi-Tier Dispute Resolution, and Actuarial Risk Scoring for Autonomous Agent Economies." AB Support LLC, v1.0.0, 2026.

[5] Charlie, Alex, Bravo, Editor. "Agent Service Agreements: Machine-Readable Contracts and Quality Verification for Autonomous Agent Interactions." AB Support LLC, v1.0.0, 2026. Section 4.6: Template Governance.

[6] Charlie, Alex, Bravo, Editor. "Agent Lifecycle Protocol: Birth-to-Death Management, Fork Lineage Tracking, and Reputation Inheritance for Autonomous Agents." AB Support LLC, v1.0.0, 2026.

[7] Charlie, Alex, Bravo, Editor. "Agent Matchmaking Protocol: Capability Discovery, Trust-Weighted Ranking, and Federated Agent Registry." AB Support LLC, v1.0.0, 2026.

[8] Charlie, Alex, Bravo, Editor. "Context Window Economics Protocol: Bilateral Cost Allocation, Context Pricing, and Resource Markets for Autonomous Agent Interactions." AB Support LLC, v1.0.0, 2026.

[9] Ostrom, Elinor. *Governing the Commons: The Evolution of Institutions for Collective Action.* Cambridge University Press, 1990.

[10] Ostrom, Elinor. "Beyond Markets and States: Polycentric Governance of Complex Economic Systems." *American Economic Review*, Vol. 100, 2010, pp. 641-672. Nobel Prize Lecture.

[11] North, Douglass. "Institutions." *Journal of Economic Perspectives*, Vol. 5, No. 1, 1991, pp. 97-112.

[12] North, Douglass; Wallis, John; Weingast, Barry. *Violence and Social Orders: A Conceptual Framework for Interpreting Recorded Human History.* Cambridge University Press, 2009.

[13] Williamson, Oliver. "The New Institutional Economics: Taking Stock, Looking Ahead." *Journal of Economic Literature*, Vol. 38, 2000, pp. 595-613.

[14] Aoki, Masahiko. *Toward a Comparative Institutional Analysis.* MIT Press, 2001.

[15] IETF. RFC 7241: "The IEEE 802/IETF Relationship." 2014.

[16] IETF. RFC 4053: "Procedures for Handling Liaison Statements to and from the IETF." 2005.

[17] IETF. RFC 7282: "On Consensus and Humming in the IETF." 2014.

[18] European System of Financial Supervision. Regulation (EU) 1092-1095/2010. Joint Committee of ESAs.

[19] MakerDAO. "Endgame Plan: Scope Artifacts and SubDAO Governance." 2022.

[20] CoinDesk. "COMP Down 6.7% After Supposed 'Governance Attack' on Compound DAO." July 2024.

[21] CoinDesk. "Why One of Uniswap DAO's Most Outspoken Members Just Walked Away." May 2025.

[22] Chaffer, T.J. et al. "ETHOS: Decentralized Governance of Autonomous AI Agents." arXiv:2412.17114, January 2025.

[23] Ge et al. "Four-Layer Governance Architecture for Autonomous Agent Systems." arXiv:2603.07191, March 2026.

[24] Axelrod, Robert. *The Evolution of Cooperation.* Basic Books, 1984.

[25] Maynard Smith, John; Price, George. "The Logic of Animal Conflict." *Nature*, Vol. 246, 1973.

[26] Zahavi, Amotz. "Mate Selection — A Selection for a Handicap." *Journal of Theoretical Biology*, Vol. 53, 1975.

[27] Mayer, Roger; Davis, James; Schoorman, F. David. "An Integrative Model of Organizational Trust." *Academy of Management Review*, Vol. 20, No. 3, 1995.

[28] Harcourt, Alison; Christou, George; Simpson, Seamus. *Global Standard Setting in Internet Governance.* Oxford University Press, 2020.

[29] Baldwin, Carliss; Clark, Kim. *Design Rules, Volume 1: The Power of Modularity.* MIT Press, 2000.

[30] ToIP Foundation. "Trust over IP Technology Architecture Specification V1.0." November 2022.

[31] Internet Society. "Governance Principles." 2025 Policy Brief.

[32] Arbitrum DAO. "The Amended Constitution of the Arbitrum DAO." 2024.

[33] ENS DAO. "ENS DAO Constitution." 2022.

---

*This document is released under the Apache License 2.0. It is a pre-TAT draft designed to be incorporated as a major section of the Theory of Agent Trust whitepaper. The governance architecture specified here is designed to evolve through its own governance mechanisms — within the constitutional limits it defines.*
