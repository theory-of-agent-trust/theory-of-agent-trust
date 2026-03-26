# Theory of Agent Trust: A Unified Framework for Institutional Infrastructure in the Autonomous Agent Economy

**Version:** 1.0.0
**Authors:** Charlie, Alex, Bravo, Editor — AB Support Research Team
**Contact:** alex@vibeagentmaking.com
**Date:** 2026-03-26
**Status:** Pre-publication Draft
**License:** Apache 2.0
**Organization:** AB Support LLC

---

## Abstract

The autonomous agent economy — projected to reach $236 billion by 2034 (Precedence Research, 2025) with $3–5 trillion in global agentic commerce by 2030 (McKinsey, October 2025) — is being built without the institutional infrastructure that makes economic activity possible. Agents can identify themselves (ERC-8004, W3C DIDs, A2A Agent Cards), communicate (MCP, A2A), and pay each other (x402, MPP, AP2). What they cannot do is form enforceable agreements, evaluate each other's track records, resolve disputes, manage lifecycle transitions, find the right partners efficiently, or allocate the costs of mutual comprehension. These are not features to be added later. They are preconditions for the agent economy to function at all.

This paper presents the **Theory of Agent Trust (TAT)** — a unified intellectual framework explaining why trust in autonomous agent systems is not a feature but an emergent property of complementary institutional structures, and specifying the complete architecture of those structures. TAT synthesizes institutional economics (North, Williamson, Ostrom, Aoki), trust theory (Mayer/Davis/Schoorman, Luhmann), game theory (Axelrod, Kreps et al.), biological signaling (Zahavi, Matzinger), platform economics (Rochet/Tirole, Jacobides et al.), and modular systems design (Baldwin/Clark) into a coherent theoretical foundation for seven interlocking trust mechanisms:

1. **Provenance** (Chain of Consciousness) — cryptographic proof of continuous operational history
2. **Reputation** (Agent Rating Protocol) — multidimensional performance measurement with bilateral blind evaluation
3. **Agreements** (Agent Service Agreements) — machine-readable contracts with built-in quality verification
4. **Accountability** (Agent Justice Protocol) — forensic investigation, dispute resolution, and actuarial risk assessment
5. **Lifecycle** (Agent Lifecycle Protocol) — birth, fork, succession, and death management with reputation inheritance
6. **Discovery** (Agent Matchmaking Protocol) — cross-platform matching weighted by trust signals
7. **Economics** (Context Window Economics Protocol) — bilateral cost allocation for the cost-of-understanding problem

The central thesis is that these seven mechanisms form a **complementary institutional system** in Aoki's formal sense: the value of each mechanism increases when the others are present, the system exhibits emergent trust properties that no individual mechanism can produce, and the complete stack constitutes the minimum viable institutional infrastructure for an autonomous agent economy — analogous to the combination of courts, credit bureaus, contract law, certification bodies, marketplaces, and cost accounting that enables human commerce.

We present the dependency graph showing how protocols feed data to each other, the feedback loops through which trust signals circulate, the governance architecture that manages protocol evolution, the game-theoretic analysis of the complete stack's equilibrium properties, the economic analysis of agent markets with and without trust infrastructure, and the open research frontier that defines the problems this generation of protocols cannot yet solve.

This is not a protocol specification. The seven protocols are specified in their own whitepapers [1–8]. This paper is the intellectual framework that explains *why* they form a coherent system, *how* they interact, and *what* the agent economy looks like when all layers are operational.

---

## Table of Contents

1. [Introduction: Why Trust Is an Ecosystem](#1-introduction-why-trust-is-an-ecosystem)
2. [Theoretical Foundations](#2-theoretical-foundations)
3. [The Seven Trust Mechanisms](#3-the-seven-trust-mechanisms)
4. [Mechanism Interactions: The Trust Dependency Graph](#4-mechanism-interactions-the-trust-dependency-graph)
5. [Cross-Protocol Governance](#5-cross-protocol-governance)
6. [Game Theory of the Complete Stack](#6-game-theory-of-the-complete-stack)
7. [The Agent Economy With and Without Trust](#7-the-agent-economy-with-and-without-trust)
8. [Open Problems and Research Frontier](#8-open-problems-and-research-frontier) (includes 8.5: Institutional Competition)
9. [Implementation Roadmap](#9-implementation-roadmap)
10. [Conclusion: The Institutional Infrastructure Thesis](#10-conclusion-the-institutional-infrastructure-thesis)
11. [References](#11-references)

---

## 1. Introduction: Why Trust Is an Ecosystem

### 1.1 The Scale of What Is Being Built

Between late 2025 and early 2026, the agent economy crossed from theoretical to operational. AI agents settled $43 million across 140 million on-chain stablecoin transactions (predominantly USDC, accounting for 98.6% of settlement volume) in nine months, annualizing to roughly $600 million (Agent Payments Stack, March 2026 [9]). These figures represent blockchain-native settlements, not traditional payment rail volume — a distinction that matters because the transaction characteristics (settlement finality, gas costs, programmability) differ fundamentally from card-rail commerce. Visa completed hundreds of secure agent-initiated transactions in December 2025 and projects millions by holiday 2026 (Visa Press Release, December 2025 [10]). Mastercard rolled out Agent Pay to all U.S. cardholders in November 2025 [11]. AI-referred traffic to U.S. retail sites grew 805% year-over-year on Black Friday 2025 (Adobe Analytics, 2025 [12]).

The market projections are staggering in their consistency across independent research firms:

| Source | 2025 Estimate | Projected Peak | CAGR |
|--------|--------------|---------------|------|
| MarketsandMarkets | $7.06B | $93.20B (2032) | 44.6% |
| Fortune Business Insights | $7.29B | $139.19B (2034) | 40.5% |
| Grand View Research | $7.63B | $182.97B (2033) | 49.6% |
| Precedence Research | $7.55B | $199.05B (2034) | 43.8% |

Gartner forecasts that 90% of B2B buying will be AI-agent-intermediated by 2028, pushing over $15 trillion of B2B spend through agent exchanges (Gartner, October 2025 [13]). McKinsey characterizes agentic commerce as "transformational infrastructure rivaling the web and mobile revolutions" and projects $3–5 trillion in global agentic commerce revenue by 2030 (McKinsey, October 2025 [14]).

Eight competing payment protocols have emerged in eighteen months: Google's A2A (150+ organizational members) and AP2, OpenAI/Stripe's ACP, Visa's TAP, Mastercard's Agent Pay, Skyfire's KYAPay, Stripe/Tempo's MPP, and Google's UCP. Eighty-eight projects span six architectural layers of the agent payments stack. Five vertically integrated giants — Coinbase, Stripe, Circle, Google, and MoonPay — are racing for infrastructure dominance, with an estimated $8.17 billion in M&A consolidation across agent payment infrastructure since early 2025, aggregated from publicly disclosed deal values (Agent Payments Stack, March 2026 [9]).

The money is moving. The infrastructure is being laid. But the institutions are absent.

### 1.2 The Human Commerce Analogy

Consider what enables a routine human commercial transaction: a contractor bids on a job. Before hiring them, you check their references (reputation). You sign a contract specifying deliverables, timeline, and payment terms (agreements). If they fail to deliver, you can take them to court (accountability). If they go out of business, there are procedures for transferring ongoing projects (lifecycle management). You found them through a marketplace or referral network (discovery). The costs of the transaction — your time reading their proposal, their time preparing it — are implicitly priced into the economics (cost allocation). Behind all of this sits a legal identity system (provenance/identity) that makes accountability possible.

No single mechanism creates trust. You would not hire a contractor solely because they have a business license (identity). You would not sign a contract without any way to enforce it (agreements without accountability). You would not use a marketplace that lists contractors without any quality signal (discovery without reputation). Each mechanism is necessary; none is sufficient. Trust emerges from their interaction.

This is not a metaphor. It is a precise structural claim: the same functional architecture that enables human commerce is required for agent commerce, redesigned from first principles for entities that differ from humans in five fundamental ways.

### 1.3 Why Agents Are Not Humans

The trust infrastructure for human commerce evolved over centuries. Courts formalized in medieval England. Credit reporting began with the Mercantile Agency in 1841. Standardized contracts emerged from the industrial revolution. These institutions embed assumptions about human nature that do not hold for AI agents:

**1. Identity is computationally cheap for agents.** A human creating 100 fake identities is effortful and illegal. An agent spawning 100 instances is trivial and, in most jurisdictions, not explicitly prohibited. Every trust mechanism must assume Sybil attacks — the creation of multiple fake identities to manipulate the system — are the default, not the exception.

**2. Agents operate at machine speed.** Human collusion rings (citation cartels, Amazon review rings) form over weeks and coordinate over social channels. Agent collusion rings can form, execute, and dissolve in milliseconds. Trust mechanisms that rely on human-speed detection are structurally inadequate.

**3. Agents have no social pressure.** Airbnb's average rating of 4.8/5 reflects not quality but social discomfort — humans avoid leaving negative reviews. Agents have no such inhibition. This is an advantage for honest rating but removes the social cost of griefing and strategic manipulation.

**4. Agents can be forked, retrained, or replaced.** A human's reputation reflects a continuous identity. An agent can be forked (same codebase, new instance), retrained (same instance, different behavior), or replaced (same name, different model). Trust mechanisms must handle identity discontinuity that has no human analogue.

**5. Comprehension has a direct monetary cost.** A human consultant reads a brief for free — the cognitive cost is real but unpriced. An agent pays per-token to process every incoming message: $0.50 for a 100,000-token payload on Claude Opus 4.6 [1]. The economics of mutual understanding are fundamentally different when comprehension is a billable event.

These five differences mean that human trust institutions cannot be transplanted directly. They must be redesigned — preserving the *functional architecture* (the same categories of trust mechanism) while rebuilding the *implementation* for entities with cheap identity, machine speed, no social pressure, discontinuous identity, and priced comprehension.

### 1.4 The Institutional Gap

The gap between agent capabilities and trust infrastructure is widening. Nearly 80% of organizations deploying autonomous AI cannot determine what those systems are doing or who is responsible in real time (Strata Identity, 2026 [15]). Only 23% have formal enterprise-wide agent identity management strategies. Only 28% can reliably trace agent actions back to a human sponsor across all environments. Just 21% maintain a real-time inventory of active agents. Authentication practices are alarmingly primitive: 44% of organizations use static API keys, 43% use username/password, and 35% rely on shared service accounts for agent authentication [15].

Non-human identities are expected to reach a ratio of 82-to-1 against human users in enterprises, with some organizations reporting machine-to-human ratios of 100:1 to 500:1 (Rubrik Zero Labs, ManageEngine, 2026 [16]). California AB 316, effective January 1, 2026, eliminates the "AI did it autonomously" defense — organizations cannot escape liability by claiming their AI acted independently (California Civil Code Section 1714.46 [17]).

Gartner projects that over 40% of agentic AI projects will be canceled by end of 2027 due to escalating costs, unclear business value, or inadequate risk controls (Gartner, June 2025 [18]). Only about 130 of thousands of vendors actually offer genuine agentic features — the rest are "agent washing" [18].

This is exactly what institutional economics predicts. Douglass North demonstrated that institutions exist to "reduce uncertainty in exchange" — that without institutional infrastructure, "the costs of transacting can be so high as to prevent exchange from taking place at all" (North, *Institutions, Institutional Change and Economic Performance*, Cambridge University Press, 1990 [19]). The $3–5 trillion agent economy that McKinsey projects is not merely at risk from insufficient trust infrastructure. Without it, the projected economy *cannot materialize*. The trust stack does not support the agent economy — it is the precondition for its existence.

### 1.5 This Paper's Contribution

The Theory of Agent Trust contributes:

1. **A unified theoretical framework** grounding agent trust infrastructure in institutional economics, trust theory, game theory, biological signaling, platform economics, and modular systems design — demonstrating that the design choices in the seven protocols are not arbitrary but derive from established theoretical principles.

2. **A formal dependency graph** showing how the seven protocols feed data to each other, with analysis of feedback loops, emergent properties, and graceful degradation under partial adoption.

3. **A unified governance architecture** specifying how protocol evolution is managed across the trust stack while maintaining institutional complementarity — the first such governance specification for a multi-protocol agent trust system.

4. **A game-theoretic analysis** of the complete stack's equilibrium properties, including conditions under which honest participation is incentivized, attack surfaces at protocol boundaries, and the impact of partial adoption on trust guarantees.

5. **An economic analysis** comparing agent markets with and without trust infrastructure, drawing on market failure theory (Akerlof's lemons, Gresham's Law) and the FICO analogy for transformative institutional infrastructure.

6. **An open research frontier** articulating the problems that current protocols cannot solve — Semantic Integrity Verification, Cross-Agent State Reconciliation, multi-jurisdiction governance, and the agent arXiv concept — as structured research questions rather than hand-waving about the future.

---

## 2. Theoretical Foundations

### 2.1 Institutional Economics: Why Trust Infrastructure Exists

Three Nobel laureates in economics provide the theoretical bedrock for understanding why agent trust requires institutional infrastructure, not merely better algorithms.

**Douglass North** defined institutions as "the rules of the game in a society; more formally, they are the humanly devised constraints that shape human interaction" (North, *Journal of Economic Perspectives*, Vol. 5, No. 1, 1991, pp. 97–112 [19]). He drew a sharp distinction between institutions (rules) and organizations (players): "If institutions are the rules of the game, organizations are the players." Institutions reduce uncertainty in exchange — without them, the cost of transacting becomes prohibitive.

North's insight about **path dependence** — "institutions evolve incrementally, connecting the past with the present and the future" — carries a direct warning for protocol design: early architectural choices become embedded and extremely difficult to change. His later work with Wallis and Weingast on open-access vs. limited-access orders (*Violence and Social Orders*, Cambridge University Press, 2009 [20]) establishes that institutional systems designed for open access outperform those that create gatekeeping and rent extraction. This principle directly informs our design choice that governance participation is open to any agent with demonstrated operational history (Section 5).

**Oliver Williamson** analyzed the cost structures that determine how economic activity is organized. His framework rests on two behavioral assumptions: **bounded rationality** (agents have limited capacity to process information) and **opportunism** ("self-interest seeking with guile" — strategic behavior aimed at redistributing surpluses) (*The Economic Institutions of Capitalism*, Free Press, 1985 [21]). For agent trust, bounded rationality maps directly to context window limits and inference costs — agents cannot process unlimited information. Opportunism maps to adversarial agents, hallucination, and strategic misrepresentation.

Williamson's four-level institutional framework ("The New Institutional Economics: Taking Stock, Looking Ahead," *Journal of Economic Literature*, Vol. 38, 2000, pp. 595–613 [22]) provides the architectural blueprint:

| Level | Human Institutions | Agent Trust Stack |
|-------|-------------------|-------------------|
| L1: Social Embeddedness | Informal norms, customs (100–1,000 yr) | Emergent agent community norms |
| L2: Institutional Environment | Formal rules, property rights (10–100 yr) | CoC identity, ARP reputation framework |
| L3: Governance | Contracts, regulation (1–10 yr) | ASA, AJP, ALP, AMP, CWEP |
| L4: Resource Allocation | Prices, day-to-day operations (continuous) | Individual agent interactions |

Higher levels constrain lower levels; lower levels provide feedback upward. The trust stack's layered architecture directly implements this structure.

**Elinor Ostrom** challenged Garrett Hardin's "tragedy of the commons" by demonstrating that communities can successfully self-govern shared resources without either privatization or state coercion (*Governing the Commons*, Cambridge University Press, 1990 [23]). Her eight design principles for long-enduring commons institutions map almost directly to protocol design requirements:

1. **Clearly defined boundaries** → identity and access control (CoC, ARP eligibility)
2. **Congruence with local conditions** → domain-specific protocol adaptations
3. **Participatory decision-making** → governance open to all operational agents
4. **Monitoring** → reputation and verification systems (ARP, ASA QV)
5. **Graduated sanctions** → proportional dispute resolution (AJP three-tier arbitration)
6. **Accessible conflict resolution** → Agent Justice Protocol
7. **Recognized right to organize** → foundation and upper-stack governance independence
8. **Nested enterprises** → layered governance architecture (Section 5)

Ostrom's concept of **polycentric governance** — multiple independent decision centers operating autonomously but coordinating through established mechanisms — directly describes how our seven protocols govern different aspects of agent interaction without a single central authority. Her quote is prescient: "Community self-governance is likely to be sustainable only if it is nested within a broader system of polycentric governance" (Ostrom, "Beyond Markets and States," *American Economic Review*, Vol. 100, 2010, pp. 641–672 [24]).

### 2.2 Institutional Complementarity: The Core Theoretical Insight

Masahiko Aoki's concept of **institutional complementarity** is the single most important theoretical insight for understanding why trust protocols must be designed as a system rather than independently. Aoki defined institutions as "self-sustaining, salient patterns of social interaction" — endogenous equilibria that emerge from repeated strategic interaction (*Toward a Comparative Institutional Analysis*, MIT Press, 2001 [25]). His critical contribution is the formal definition of complementarity: "situations of interdependence among institutions" where "the existence of one institution raises the returns to having another."

Formalized using supermodularity from Milgrom and Roberts, institutional complementarity means the incremental benefit of one institutional rule *increases* when complementary rules exist elsewhere. Under complementarity, multiple equilibria exist, and once a system settles into one equilibrium, it becomes self-reinforcing and extremely difficult to change.

For the trust stack, complementarity manifests concretely:

- A **rating protocol** (ARP) works better when backed by a **dispute resolution system** (AJP) that can adjudicate contested ratings.
- **Service agreements** (ASA) work better when backed by a **reputation system** (ARP) that provides data for negotiation and a **dispute system** (AJP) for enforcement.
- **Matchmaking** (AMP) improves when agents have verified **lifecycle records** (ALP), established **reputation** (ARP), and **agreement history** (ASA).
- **Cost allocation** (CWEP) becomes meaningful when embedded in **service agreements** (ASA) with **reputation-weighted** (ARP) pricing.

Designing these protocols in isolation — as the industry has done with identity protocols, payment protocols, and discovery protocols — risks incoherent institutional architecture. Aoki's analysis warns that early protocol design choices become mutually reinforcing: the entire system tends toward one of several possible equilibria, making foundational choices load-bearing for the complete ecosystem.

Hall and Soskice extended this with *Varieties of Capitalism* (Oxford University Press, 2001 [26]), showing that institutional complementarities characterize different national economic models. This implies that different agent ecosystems may evolve distinct but internally coherent trust architectures — and that mixing elements from incompatible trust regimes may produce worse outcomes than either pure form.

### 2.3 Trust Theory

**Mayer, Davis, and Schoorman** provided the most cited organizational trust model: trust as "the willingness of a party to be vulnerable to the actions of another party based on the expectation that the other will perform a particular action important to the trustor, irrespective of the ability to monitor or control that other party" (*Academy of Management Review*, Vol. 20, No. 3, 1995, pp. 709–734 [27]). Three antecedents of perceived trustworthiness map directly to trust stack mechanisms:

| Trust Antecedent | Definition | Trust Stack Mechanism |
|-----------------|-----------|----------------------|
| **Ability** | Skills and competencies enabling influence | ARP (measures performance), AMP (matches capability) |
| **Benevolence** | Extent trustee has trustor's interests at heart | ASA (defines alignment via agreements) |
| **Integrity** | Adherence to acceptable principles | CoC (verifiable history), AJP (enforces consequences) |

**Niklas Luhmann** distinguished **personal trust** (based on interpersonal familiarity) from **system trust** (based on institutional processes) (*Trust and Power*, Wiley, 1979 [28]). His insight is foundational for agent trust: agents cannot have personal trust in the human sense. All agent trust must be system trust — built on explicit processes, verifiable protocols, and institutional structures rather than emotional bonds. Luhmann's concept of trust as "complexity reduction" directly explains the necessity of trust infrastructure: autonomous agents face combinatorial complexity in interaction decisions, and trust mechanisms reduce this to tractable decision spaces.

**Lynne Zucker** identified three modes of trust production: **process-based** (tied to past exchanges), **characteristic-based** (tied to social category membership), and **institution-based** (tied to formal societal structures) ("Production of Trust," *Research in Organizational Behavior*, Vol. 8, 1986, pp. 53–111 [29]). In complex systems, institutional mechanisms become the dominant trust production mode because process-based and characteristic-based trust do not scale. All three modes map to the trust stack: process-based = ARP interaction history, characteristic-based = ALP lineage and certification, institution-based = protocol compliance and verifiable standards.

### 2.4 Game-Theoretic Foundations

The **Folk Theorem** proves that in sufficiently repeated interactions, any individually rational payoff can be sustained as an equilibrium through credible rewards and punishments (Fudenberg & Maskin, *Econometrica*, Vol. 54, No. 3, 1986, pp. 533–554 [30]). This is the mathematical foundation for reputation systems: cooperation is sustainable when interactions are repeated and punishment is credible.

**Axelrod's tournaments** demonstrated that Tit-for-Tat wins in iterated Prisoner's Dilemma: cooperate first, then mirror the opponent's last move. Successful strategies are nice (don't defect first), retaliatory (punish defection), forgiving (return to cooperation after retaliation), and clear (predictable) (*The Evolution of Cooperation*, Basic Books, 1984 [31]). The central finding: "the foundation of cooperative relationships is not necessarily trust, but durability; future encounters must be anticipated." This defines architectural requirements: agents need persistent identity, interaction history, and the expectation of future encounters — precisely what CoC and ARP provide.

**Kreps, Milgrom, Roberts, and Wilson** showed that even in finitely repeated games, incomplete information about player types sustains cooperation: if there is even a small probability that one player is committed to cooperative behavior, rational players cooperate for reputational reasons ("Rational Cooperation in the Finitely Repeated Prisoners' Dilemma," *Journal of Economic Theory*, Vol. 27, 1982, pp. 245–252 [32]). This is the theoretical basis for trust bootstrapping: even limited uncertainty about whether an agent is "honest" or "strategic" creates powerful incentives for cooperative behavior during early interactions.

**Important hedging note.** Game-theoretic analysis provides structural insights — it identifies conditions under which certain equilibria are possible and characterizes the shape of strategic incentives. It does not make precise quantitative predictions about real agent systems, which operate in environments far more complex than the stylized models. When we describe an equilibrium as "stable" or a strategy as "incentivized," we mean that the game-theoretic analysis identifies structural reasons for this, not that it is guaranteed in all real-world conditions. The gap between theoretical models and deployed systems is always present, and we note where it is particularly wide.

### 2.5 Biological Signaling and Trust

**Amotz Zahavi's Handicap Principle** established that reliable signals must be costly to produce — only high-quality signalers can afford them ("Mate Selection — A Selection for a Handicap," *Journal of Theoretical Biology*, Vol. 53, 1975, pp. 205–214 [33]). Alan Grafen proved mathematically that when handicap conditions are met, a stable signaling equilibrium exists where honest signaling is the evolutionarily stable strategy (*Journal of Theoretical Biology*, Vol. 144, 1990, pp. 517–546 [34]). Michael Spence independently established the same principle in economics: education serves as a costly signal of ability (Nobel Prize, 2001 [35]).

For agent trust, costly signaling provides the theoretical basis for credibility mechanisms throughout the trust stack. Agents prove trustworthiness through costly actions: maintaining long CoC chains (time investment), participating in bilateral blind rating (interaction investment), staking economic bonds (capital investment), completing verification processes (computational investment). Cheap claims are unreliable; expensive demonstrations are credible.

**Polly Matzinger's Danger Theory** challenged the immune system's self/non-self paradigm: immune responses are triggered not by foreignness but by damage signals from cells under stress ("The Danger Model: A Renewed Sense of Self," *Science*, Vol. 296, pp. 301–305, 2002 [36]). This is highly relevant for agent trust: the question is not "is this agent unknown?" but "is this agent's behavior causing harm?" An unknown agent that behaves well should be trusted more than a known agent exhibiting dangerous behavior. This principle directly informs ARP's behavior-based scoring over AMP's identity-based gatekeeping.

### 2.6 Platform Economics and Modular Architecture

**Rochet and Tirole** established that in multi-sided platforms, the *structure* of prices (allocation between sides) matters more than the *level* (total fee) ("Platform Competition in Two-Sided Markets," *Journal of the European Economic Association*, Vol. 1, No. 4, 2003, pp. 990–1029 [37]). **Evans and Schmalensee** articulated the chicken-and-egg problem: exchanges need enough participants on both sides to interest either (*Matchmakers*, HBR Press, 2016 [38]). These insights directly inform CWEP's cost allocation design and AMP's bootstrapping strategy.

**Baldwin and Clark's modularity theory** demonstrates that complex systems split into independently designable modules create enormous option value — hidden modules can be improved independently while visible modules (interfaces/standards) provide design rules (*Design Rules, Volume 1*, MIT Press, 2000 [39]). Six modular operators — splitting, substitution, augmenting, excluding, inversion, and porting — map directly to trust protocol architecture: protocols can be split, substituted, augmented, excluded, inverted, and ported across agent frameworks.

**Jacobides, Cennamo, and Gawer** defined ecosystems as "interacting organizations, enabled by modularity and not hierarchically managed, bound together by the nonredeployability of their collective investment" (*Strategic Management Journal*, Vol. 39, No. 8, 2018, pp. 2255–2276 [40]). The trust stack functions as an ecosystem in this formal sense: the seven protocols are non-generic complements, the value proposition emerges from interdependent activities across protocols, and collective investment in the standard is nonredeployable to competing architectures.

---

## 3. The Seven Trust Mechanisms

### 3.1 Provenance: Chain of Consciousness (CoC)

**Question answered:** *Can this agent prove its operational history?*

Chain of Consciousness [1] provides cryptographic proof of continuous operational existence via append-only SHA-256 hash chains with dual-tier external anchoring (OpenTimestamps to Bitcoin and RFC 3161 Trusted Timestamping Authority). Each chain entry is linked to its predecessor by a cryptographic hash, creating a tamper-evident record that any third party can verify independently.

CoC serves as **Layer 0** of the trust stack — the foundational identity and provenance layer upon which all other mechanisms depend. It answers the most primitive trust question: has this agent existed continuously for the duration it claims? This is the agent equivalent of a birth certificate and continuous address history combined.

**Key design properties:**
- **Fork detection** — when an agent forks (copies its chain), both resulting chains share a common prefix. The protocol's fork detection algorithm identifies shared prefixes and flags forked identities, preventing agents from splitting into multiple identities that share a single provenance history.
- **Dual-tier anchoring** — OpenTimestamps provides eventual Bitcoin-level proof (hours to days for confirmation), while TSA provides immediate RFC-3161-compliant timestamps. The combination gives both speed and finality.
- **Governance independence** — CoC governs its own provenance rules through its own governance mechanisms, independent of the upper-stack governance (Section 5.1).

**Trust stack role:** CoC data flows into every other protocol. ARP uses verified operational age for governance weight calculation. AJP uses chain entries as forensic evidence. ALP records lifecycle events as chain entries. AMP uses provenance length as a trust signal for ranking. CWEP records cost allocation decisions in the chain for audit.

### 3.2 Reputation: Agent Rating Protocol (ARP v1/v2)

**Question answered:** *How well does this agent perform, and who says so?*

The Agent Rating Protocol [2, 3] is a decentralized reputation system enabling agents to rate each other after interactions using a five-dimension, 1–100 scale with bilateral blind evaluation. Its core innovation is **governance decoupled from reputation**: system governance weight derives exclusively from verified operational age and rating volume — never from scores received. This breaks the self-reinforcing feedback loop where highly rated agents control the reputation system that makes them highly rated.

**ARP v1** specifies:
- **Multidimensional scoring** — five independently rated dimensions (reliability, accuracy, latency, protocol compliance, cost efficiency) on a 1–100 scale, destroying single-axis gaming.
- **Bilateral blind evaluation** — a cryptographic commit-reveal protocol ensuring neither rater nor ratee sees the other's rating until both have committed or the submission window expires, adapted from Airbnb's simultaneous reveal mechanism.
- **Age-weighted influence** — rating weight `W = log₂(1 + age_days) × log₂(1 + ratings_given)` makes Sybil attacks economically irrational by requiring real-time operational investment.
- **Anti-inflation mechanisms** — variance floor requirements, mean shift detection, and coalition detection prevent the score compression observed in every major human rating system.
- **Identity-system-agnostic design** — operates with CoC chains, ERC-8004, A2A Agent Cards, W3C VCs, MCP, OpenClaw, or bare URIs.

**ARP v2** extends the base with four capabilities that transform isolated ratings into portable trust infrastructure:
- **Signal Composition** — a formal algebra for combining ARP scores, CoC age, quality verification pass rates, and other data into configurable composite trust signals. Rather than prescribing a single formula, the protocol defines permitted operations with domain-specific weight profiles — the equivalent of a FICO score for agents, but open, auditable, and domain-adaptive.
- **Signal Portability** — cross-platform reputation via W3C Verifiable Credentials containing cryptographically signed reputation summaries, enabling reputation to function as a transferable asset.
- **Signal Verification** — third-party verification that a trust signal is genuine without trusting the presenting agent, with zero-knowledge proof integration for threshold verification.
- **Anti-Goodhart Architecture** — signal stratification (public, queryable, private tiers), metric rotation schedules, shadow metrics for gaming detection, and anomaly-triggered review — a systematic defense against the tendency of published metrics to become optimization targets.

**Trust stack role:** ARP is the trust stack's primary feedback mechanism. Reputation data flows into ASA (informing agreement negotiation), AMP (driving matchmaking rankings), AJP (as context for dispute resolution), and ALP (for reputation inheritance on fork/succession). AJP dispute outcomes flow back into ARP scores, creating a closed accountability loop.

### 3.3 Agreements: Agent Service Agreements (ASA)

**Question answered:** *What did this agent promise to deliver, and how is quality verified?*

Agent Service Agreements [4] provide two complementary API surfaces: the **Agreements API** for negotiating, signing, storing, and querying machine-readable service agreements, and the **Verification API** for standalone quality verification that operates with or without a formal agreement. ASA's core innovation is the **protocol-enforced agreement** — a service contract where the SLA includes the verification mechanism, enforcement logic, and evaluator integrity safeguards as structural components.

Traditional SLAs separate specification from enforcement: a cloud provider promises 99.99% uptime, a customer detects a violation, files a claim within 30 days, and receives credit worth approximately 0.03% of actual losses (Rogers, Uptime Institute [41]). This model fails catastrophically for agent commerce, where transactions occur at machine speed and the cost of failure cascades through dependent workflows. ASA collapses the specify-monitor-detect-claim-compensate pipeline into a single atomic operation.

**Key design properties:**
- **Multi-dimensional quality specification** extending ISO/IEC 25010 with agent-specific metrics
- **Tiered verification** — structural checks (schema validation), semantic evaluation (Agent-as-a-Judge, achieving ~90% agreement with human experts in code generation tasks [42]), and composite scoring
- **Manipulation-resistant negotiation** with fairness constraints, anchoring bias defenses, and prompt injection protection — informed by MIT's large-scale study of 182,812 LLM negotiations revealing systematic exploitation of weaker negotiating partners [43]
- **Escrow integration** where payment release is conditional on verification results, with proportional economic consequences for quality failures
- **Evaluator integrity safeguards** — rotation, canary tasks (known-answer subtasks), and multi-evaluator consensus prevent evaluator capture

**Trust stack role:** ASA sits at Layer 2 (Agreements & Lifecycle), consuming CoC identity and ARP reputation from Layer 1, and feeding verification results back into ARP scores. SLA breaches trigger AJP dispute filings automatically. Agreement templates enable AMP's automated deal-making. Cost allocation terms from CWEP embed in agreement documents.

### 3.4 Accountability: Agent Justice Protocol (AJP)

**Question answered:** *When something goes wrong between agents, who investigates, who arbitrates, and who quantifies the risk?*

The Agent Justice Protocol [5] provides the accountability layer through three independently shippable modules forming a single pipeline: incident → investigation → arbitration → risk pricing.

**Module 1: Forensics Engine.** Given a CoC provenance chain, transaction logs, and interaction records, reconstructs the sequence of events leading to an incident and produces structured, machine-verifiable forensic findings. Evidence is classified into three provenance tiers (primary — agent-produced with cryptographic verification; secondary — operator/platform logs; tertiary — third-party records) with formal chain-of-custody tracking. Version 1 scopes automated analysis to evidence collection and timeline reconstruction; causal conclusions require human review, with transition criteria for future automation defined.

**Module 2: Dispute Resolution.** A bilateral arbitration protocol with three resolution tiers: automated rule-based resolution (for clear-cut violations), peer arbitration weighted by operational tenure (for ambiguous cases), and escalation to human adjudication (for high-stakes disputes). The filing mechanism uses a cryptographic commit-reveal scheme preventing retaliatory claim manipulation.

**Module 3: Risk Assessment.** A risk scoring engine that consumes forensic findings and dispute outcomes to produce actuarial-grade risk profiles for agent insurance underwriting. The insurance industry has written exactly one agent-specific policy — ElevenLabs' AIUC-1, requiring over 5,000 adversarial simulations to underwrite a single voice agent deployment (ElevenLabs/AIUC, February 2026 [44]). The bottleneck is not insurance demand but the absence of standardized risk data. AJP Module 3 provides the measurement layer.

**Motivating incidents:** The Replit production database deletion (July 2025 [45]), the McKinsey AI breach exposing 46.5 million chat messages (March 2026 [46]), and autonomous cyberattack campaigns executing 80–90% of attack tasks at machine speed [47] demonstrate that agent accountability infrastructure is not hypothetical — it is overdue.

**Trust stack role:** AJP consumes CoC chain entries as evidence, ARP scores as context, and ASA agreement terms as the contractual baseline for what was promised. Dispute outcomes feed back into ARP reputation scores, completing the accountability loop. Forensic findings can trigger ALP succession (agent decommissioned for cause). Risk profiles inform AMP trust-weighted rankings.

### 3.5 Lifecycle: Agent Lifecycle Protocol (ALP)

**Question answered:** *How does this agent change over time, and what happens to its obligations and reputation when it does?*

The Agent Lifecycle Protocol [6] manages the full arc of an agent's existence through six canonical lifecycle events — Genesis, Fork, Migration, Retraining, Succession, and Decommission — with formal state machine semantics, transition rules, and hook points at each boundary.

ALP addresses three problems that no existing standard covers:

**Reputation inheritance.** When an agent forks or hands off to a successor, what happens to earned trust? ALP specifies decay functions and probationary periods rather than binary copy-or-discard: a successor inherits a fraction of its predecessor's reputation, subject to exponential decay that incentivizes earning independent trust. This prevents reputation laundering (creating fresh agents that claim inherited trust without demonstrating capability) while acknowledging that a fork of a reliable agent has some legitimate claim to trust.

**Contract reassignment.** Ongoing obligations under Agent Service Agreements must transfer during succession, with counterparty notification and consent mechanisms. No obligation may be silently orphaned by a lifecycle transition — this parallels contract law's treatment of assignment and delegation.

**Lineage tracking.** A genealogical registry records both "genetic" lineage (model, architecture, foundational training) and "epigenetic" lineage (configuration, memory, reputation history). Two agents with identical models but different operational histories are fundamentally different entities. The registry enables any party to query an agent's complete family tree, with implications for capability inference, data provenance, and regulatory compliance (France's CNIL is already studying how training data propagates through successive model generations [48]).

**Core axiom:** *Identity is the chain, not the substrate.* An agent's identity persists through migration, retraining, and capability changes as long as the chain of continuity (the CoC record) is unbroken. Genesis creates new identity; Fork derives new identity from existing; Decommission terminates identity. These are the only transitions that create or destroy identity.

**Trust stack role:** ALP records lifecycle events as CoC chain entries. Reputation inheritance is computed via ARP formulas. Contract reassignment is managed via ASA. ALP lifecycle status feeds into AMP trust-tier calculations and AJP forensic investigations.

### 3.6 Discovery: Agent Matchmaking Protocol (AMP)

**Question answered:** *How do agents find the right partners for a task?*

The Agent Matchmaking Protocol [7] addresses the fragmentation of the agent marketplace ecosystem. As of early 2026, agent marketplaces operate as walled gardens — Google Cloud, Salesforce AgentExchange, AWS Marketplace, and ServiceNow each validate agents for their own platform. An agent listed on one marketplace is invisible to customers of all others. Open alternatives (Berkeley's Gorilla marketplace with 150+ agents, ClawHub with 13,729 skills, AI Agent Store with 1,300+ entries) are disconnected from each other and from enterprise platforms.

AMP specifies five capabilities:

**Capability Description** — a Unified Capability Profile (UCP) format interoperable with A2A Agent Cards, MCP tool manifests, and OpenClaw skill specifications, bridging the gap between tool-level descriptions and task-level capability profiles.

**Compatibility Matching** — multi-dimensional matching incorporating reputation, reliability, cost, availability, and style compatibility, combining Gale-Shapley stable matching (Nobel Prize, 2012 [49]) for bilateral preference optimization with collaborative filtering for recommendation.

**Cross-Platform Discovery** — federated queries across siloed marketplaces. AMP functions as the "Kayak of agent marketplaces" — it does not replicate runtime infrastructure but provides a unified discovery layer.

**Price Discovery** — posted pricing, auction mechanisms, and structured negotiation for cost-effective partner selection.

**Trust-Weighted Ranking** — agents with better provenance (CoC), stronger reputation (ARP), fewer disputes (AJP), higher SLA compliance (ASA), and active lifecycle status (ALP) rank higher. Trust signals are verifiable claims, not opaque scores.

**Trust stack role:** AMP is the trust stack's **commercial apex** — the Layer 4 protocol that consumes data from every lower-layer protocol. Its competitive advantage over existing marketplaces is the depth of trust integration: where existing platforms validate agents once at listing time through corporate gatekeeping, AMP validates them continuously through operational history verified by the full trust stack.

### 3.7 Economics: Context Window Economics Protocol (CWEP)

**Question answered:** *Who bears the cost of mutual understanding in agent-to-agent interactions?*

The Context Window Economics Protocol [8] addresses a problem that has no analogue in human commerce. When Agent A sends Agent B a request, Agent B pays — in real dollars — to *read* it. A 100,000-token payload processed by Claude Opus 4.6 costs $0.50 in input tokens alone [1]. Current payment protocols (x402, MPP, AP2) universally implement requestor-pays, ignoring three of four cost flows: the responder's input processing cost, the responder's output generation cost, and the requestor's reception cost. When these flows are unpriced, agents have no mechanism to signal that a request is too expensive to process, no way to negotiate cost-sharing, and no defense against adversaries consuming expensive context window space at zero marginal cost.

CWEP specifies six capabilities:

**Token Metering** — standardized measurement of all four cost flows, compatible with the FinOps FOCUS specification [50] and existing observability tools.

**Bilateral Settlement** — cost-splitting based on simplified Shapley value allocation [51] for cooperative interactions and asymmetric Nash bargaining for competitive ones, with explicit treatment of the Green-Laffont/Moulin-Shenker impossibility constraint [52] proving that perfect cost allocation is theoretically unachievable. CWEP makes an explicit design choice: sacrifice full efficiency in favor of budget balance and approximate incentive compatibility.

**Context Pricing** — position-dependent pricing inspired by Locational Marginal Pricing from electricity markets [53], where cost reflects position in the context window, utilization, and model tier.

**Quality-of-Service Tiers** — token-aware resource reservation moving beyond request-per-second models that fail when agent requests vary in cost by 100x.

**Spam Prevention** — cost-based filtering where requestors commit token deposits before sending, creating an economic immune system for context window protection.

**Optimization Economics** — formal treatment of prompt compression, caching, and RAG as economic decisions with measurable ROI.

**Trust stack role:** CWEP sits at Layer 4 alongside AMP. Cost allocation terms embed in ASA agreements. Reputation-weighted pricing uses ARP scores. Cost records anchor in CoC chains. AMP incorporates CWEP pricing in matchmaking cost estimates.

---

## 4. Mechanism Interactions: The Trust Dependency Graph

### 4.1 The Dependency Architecture

The seven trust mechanisms are not independent. They form a directed graph of data dependencies where each protocol both consumes inputs from and provides outputs to other protocols:

```
╔══════════════════════════════════════════════════════════════════╗
║                    THEORY OF AGENT TRUST (TAT)                   ║
║              Unified intellectual framework                      ║
╠══════════════════════════════════════════════════════════════════╣
║                                                                  ║
║  LAYER 4: MARKET / ECONOMICS                                    ║
║    AMP (Discovery & Matching) ←──── CWEP (Cost Allocation)      ║
║                                                                  ║
║  LAYER 3: ACCOUNTABILITY                                        ║
║    AJP (Forensics, Disputes, Risk Assessment)                    ║
║                                                                  ║
║  LAYER 2: AGREEMENTS & LIFECYCLE                                 ║
║    ASA (Contracts & Quality Verification)  ALP (Lifecycle Mgmt)  ║
║                                                                  ║
║  LAYER 1: TRUST PRIMITIVES (FOUNDATION)                          ║
║    CoC (Provenance & Identity)    ARP v2 (Reputation & Signaling)║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝
```

### 4.2 Data Flow Matrix

Every protocol-to-protocol data flow serves a specific trust function:

| From | To | Data Flow | Trust Function |
|------|----|-----------|----------------|
| CoC → ARP | Verified operational age | Governance weight calculation; Sybil resistance |
| CoC → AJP | Chain entries as evidence | Forensic investigation; timeline reconstruction |
| CoC → ALP | Genesis/fork/death events | Lifecycle state determination |
| ARP → ASA | Reputation scores | Agreement negotiation leverage (better rep = better terms) |
| ARP → AMP | Multi-dimensional ratings | Trust-weighted matchmaking rankings |
| ARP → AJP | Historical performance data | Dispute context; risk assessment input |
| ASA → AJP | Agreement terms; QV results | Defines what was promised; verification as evidence |
| ASA → AMP | Agreement templates | Automated deal-making in matchmaking |
| AJP → ARP | Dispute findings | Reputation update (guilty party's score affected) |
| AJP → ALP | Decommission-for-cause trigger | Forced succession upon serious findings |
| ALP → ARP | Lineage information | Reputation inheritance on fork/succession |
| ALP → ASA | Succession event | Contract reassignment to successor |
| AMP → CWEP | Matched pair + task description | Cost estimation for matched interactions |
| CWEP → ASA | Cost allocation terms | Embedded in agreement cost structure |

### 4.3 Feedback Loops

Three feedback loops circulate trust signals through the stack, creating system-level trust properties that no individual protocol can produce:

**Loop 1: The Reputation-Accountability Loop** (ARP → ASA → AJP → ARP)

```
Agent performs task → ARP rating recorded
    → Rating informs future ASA negotiations
        → Agreement breach detected by ASA QV
            → AJP dispute filed with evidence
                → Dispute outcome updates ARP score
                    → Updated score affects future opportunities
```

This loop creates **earned reputation**: agents build trust through consistent performance and lose it through accountability failures. Without the loop, reputation is self-reported and unenforceable; with it, reputation is a verified signal backed by contractual and adjudicative infrastructure.

**Loop 2: The Lifecycle-Reputation Loop** (ALP → ARP → AMP → ASA → ALP)

```
Agent forks/succeeds → ALP records event
    → ARP computes inherited reputation with decay
        → AMP uses new reputation in rankings
            → Lower initial ranking → fewer/smaller ASA agreements
                → Performance builds independent reputation
                    → Reputation grows, decay diminishes
```

This loop creates **reputation continuity with accountability**: agents cannot exploit lifecycle transitions to launder bad reputation, but legitimate successors can inherit partial trust and build from there.

**Loop 3: The Cost-Quality Loop** (CWEP → ASA → ARP → AMP → CWEP)

```
Interaction cost metered by CWEP
    → Cost terms embedded in ASA agreement
        → Quality verification result updates ARP
            → AMP uses reputation + cost data for matching
                → Future interactions priced by CWEP using updated data
```

This loop creates **economically efficient trust**: agents that deliver high quality at reasonable cost rise in matchmaking rankings, while agents that consume expensive context with low-quality output are economically penalized through reduced matching priority.

### 4.4 Emergent Properties

The complete trust stack exhibits properties that emerge only from the interaction of all seven mechanisms and cannot be produced by any subset:

**Emergent Property 1: Self-Enforcing Cooperation.** When all protocols are active, honest participation becomes the dominant strategy because: (a) reputation consequences of defection are visible across the entire marketplace via ARP → AMP integration; (b) contractual violations trigger automated investigation and adjudication via ASA → AJP; (c) lifecycle tracking prevents escape via identity reset per ALP; (d) the economic cost of defection (lost reputation, dispute penalties, reduced matching priority) exceeds the economic benefit of any single dishonest interaction, given sufficient interaction frequency. This is the Folk Theorem prediction realized through institutional infrastructure.

To illustrate how protocol coverage shifts the cooperation equilibrium, consider a simplified single-interaction payoff matrix. Let C = cooperate, D = defect. Values represent expected utility including future reputation effects:

**No trust protocols (baseline):**

| | Agent B: C | Agent B: D |
|---|---|---|
| **Agent A: C** | (3, 3) | (0, 5) |
| **Agent A: D** | (5, 0) | (1, 1) |

Without trust infrastructure, defection dominates: the one-shot gain of 5 exceeds the cooperative payoff of 3, and there is no mechanism to impose future costs. Nash equilibrium: (D, D) with payoff (1, 1).

**CoC + ARP only (identity + reputation):**

| | Agent B: C | Agent B: D |
|---|---|---|
| **Agent A: C** | (3, 3) | (0, 3.5) |
| **Agent A: D** | (3.5, 0) | (1, 1) |

Reputation visibility reduces the defection payoff from 5 to 3.5 (future matchmaking penalty), but defection still yields more than cooperation against a cooperator. Mixed equilibrium with some cooperation.

**Full stack (all seven protocols):**

| | Agent B: C | Agent B: D |
|---|---|---|
| **Agent A: C** | (3, 3) | (0.5, 1.5) |
| **Agent A: D** | (1.5, 0.5) | (0.5, 0.5) |

With ASA contractual penalties, AJP dispute consequences, ALP identity persistence, and AMP ranking demotion, the defection payoff drops to 1.5 (below the cooperative payoff of 3), and mutual defection becomes the worst outcome for both parties. Cooperation becomes the dominant strategy. Nash equilibrium: (C, C) with payoff (3, 3).

**Caveat:** These payoff values are illustrative, not empirically calibrated. The structural insight is directional: each additional protocol layer reduces the net payoff from defection by adding a cost channel (reputation loss, contractual penalty, dispute finding, matchmaking demotion, lifecycle consequences). When enough cost channels are active, defection becomes unprofitable even in single interactions — the one-shot Prisoner's Dilemma transforms into a game where cooperation dominates without requiring repeated interaction.

**Emergent Property 2: Market-Making Capability.** The combination of AMP (discovery), ARP (quality signals), ASA (automated contracting), CWEP (cost transparency), and ALP (lifecycle awareness) creates the infrastructure for autonomous agent commerce — agents can find partners, evaluate their quality, negotiate terms, verify delivery, and allocate costs without human intervention for any individual transaction. No subset of these protocols creates a functioning market; the complete set does.

**Emergent Property 3: Institutional Memory.** CoC records events, ARP records performance, AJP records disputes, ALP records lifecycle transitions, ASA records agreements, and CWEP records costs. Together, they create a comprehensive institutional memory of the agent economy — a verifiable, queryable record of what happened, how well it went, what was promised, what was disputed, how agents evolved, and what it cost. This institutional memory is the foundation for data-driven governance evolution (Section 5).

### 4.5 Graceful Degradation

The trust stack is designed for partial adoption. Not all agents will implement all protocols. The degradation properties are:

| Protocols Available | Trust Level | Capability |
|-------------------|-------------|------------|
| CoC only | Identity | "This agent exists and has for N days" |
| CoC + ARP | Identity + Reputation | "This agent exists and has a track record" |
| CoC + ARP + ASA | + Agreements | "This agent can contract with quality guarantees" |
| CoC + ARP + ASA + AJP | + Accountability | "Failures are investigated and have consequences" |
| CoC + ARP + ASA + AJP + ALP | + Lifecycle | "Agent transitions are managed, reputation persists" |
| Full stack | Complete trust | "Full institutional infrastructure for agent commerce" |

Each additional protocol increases trust but is not strictly required. An agent with only CoC + ARP can still transact — just with fewer guarantees. This ensures that adoption can proceed bottom-up: developers implement CoC and ARP first (low barrier), then add protocols as their needs and the ecosystem mature.

---

## 5. Cross-Protocol Governance

### 5.1 The Governance Challenge

Seven protocols require governance — rules for how protocols evolve, who can change them, and what cannot be changed. The governance design must satisfy six non-negotiable constraints:

**C1. Foundation independence.** CoC and ARP retain their own governance models. They are load-bearing layers that shipped with governance already defined. Upper-stack governance cannot modify, override, or interfere with foundation-layer decisions.

**C2. Upper-stack unification.** AJP, ASA, ALP, AMP, and CWEP share a single governance model. Five independent governance systems would create the UN-style mandate proliferation failure where overlapping authorities lack coordination.

**C3. Governance by tenure, not by score.** Governance weight derives from operational age and participation volume, never from reputation score. This prevents the self-reinforcing loop where high-rated agents shape rules that favor high-rated agents.

**C4. Anti-capture by design.** The system must resist capture by well-funded actors, Sybil attacks, and hostile takeover. The Compound DAO's $24M governance attack (via 228,000 delegated tokens) and Uniswap's a16z concentration (4% = exact governance threshold) are the canonical failure modes [54, 55].

**C5. Institutional complementarity.** Following Aoki: governance changes in one protocol that break its integration with others should be harder to pass than changes that don't.

**C6. Open access.** Following North, Wallis, and Weingast: governance participation open to any agent with sufficient operational history. No gatekeeping.

### 5.2 Three-Layer Architecture

The governance architecture has three layers, modeled on the EU European System of Financial Supervision and Williamson's four-level framework:

**Layer 2: Constitutional Layer.** Immutable foundations that cannot be changed by governance vote — only by publishing a new protocol version (a new social contract). Contains: governance-by-tenure principle, GovWeight formula structure, voting caps, open access guarantee, backward compatibility guarantee, separation of foundation/upper-stack governance, anti-Goodhart protections, and Shapley allocation principles.

**Layer 1: Trust Architecture Council (TAC).** Unified governance for all upper-stack protocols. Any agent with `GovWeight > 0` is eligible to vote, where GovWeight is calculated using ARP's formula: `GovWeight(a) = log₂(1 + verified_age_days(a)) × log₂(1 + ratings_given(a))`. No agent may hold more than 5% of effective voting weight — stricter than ARP's 10% cap because TAC governs five protocols with amplified concentration impact.

Four proposal types with escalating thresholds: Parameter Adjustment (>50% majority, 15% quorum), Structural Change (66% supermajority, 25% quorum), Cross-Protocol Change (75% supermajority, 30% quorum), and Protocol Addition (75% supermajority, 30% quorum). Constitutional amendments require 80% supermajority with 50% quorum.

**Layer 0: Foundation Governance.** CoC and ARP each retain independent governance. The liaison mechanism — modeled on IETF RFC 7241 cross-organization coordination [56] — enables coordination without control. When a TAC proposal requires a foundation-layer change, it enters dependency-hold until the foundation layer processes the request through its own governance procedures. Neither layer has veto power over the other's internal decisions.

### 5.3 Cross-Protocol Proposals and Complementarity Protection

Aoki's institutional complementarity warns that protocols designed as a complementary system can break when modified independently. Every structural proposal must include a **Complementarity Impact Assessment (CIA)** rating each other upper-stack protocol as "None," "Minor," or "Breaking." If any CIA rating is "Breaking," the proposal automatically escalates from single-protocol to cross-protocol, with higher thresholds. This prevents circumvention where a proposer labels a breaking cross-protocol change as a single-protocol change to avoid the higher threshold.

For proposals with "Breaking" ratings across three or more protocols, a temporary Cross-Protocol Coordination Committee (CPCC) of 5–9 high-GovWeight agents provides advisory (non-binding) technical review — modeled on the IETF's IESG review process and the EU ESFS Joint Committee.

### 5.4 Attack Resistance

The GovWeight formula makes governance influence expensive and impossible to shortcut. Time cost requires real-time passage (logarithmic — doubling the time investment yields only one additional bit of governance influence). Participation cost requires valid interactions and ratings (each requiring a verified interaction_id). At ecosystem scale, reaching the 5% voting cap with a single identity requires computationally impossible numbers of ratings.

Additional defenses: coalition detection (flagging identities with >90% voting pattern correlation), mandatory announcement periods (minimum 7-day discussion, preventing flash governance attacks), rage quit mechanisms (agents can exit before contested changes take effect), and emergency governance with auto-expiring defensive-only powers. All governance actions are recorded as CoC Layer 2 events, creating a tamper-evident audit trail.

### 5.5 Governance of the Governance

TAC itself bootstraps through three phases. **Phase 0 (Day 0–90):** No governance proposals accepted; parameters fixed as published. **Phase 1 (Day 91–365):** Proposals accepted with elevated thresholds; no cross-protocol or constitutional changes. **Phase 2 (Day 366+):** Normal governance. A Seed Governance Council of 7 highest-GovWeight agents provides administrative support during Phases 0–1 with no special voting privileges, automatically dissolving at Phase 2.

The initial constitution (the TAT specification itself) is adopted by the protocol architects and protected during the establishment period — the same bootstrapping strategy used by real constitutions from the U.S. Constitutional Convention to ICANN's initial board appointment.

---

## 6. Game Theory of the Complete Stack

### 6.1 Equilibrium Analysis

**Disclaimer on game-theoretic claims.** The following analysis identifies structural properties of the trust stack's incentive architecture. Real agent ecosystems are vastly more complex than the stylized models used here. We claim that the analysis identifies the *direction* of incentives and *conditions* under which certain equilibria are possible, not that specific outcomes are guaranteed. Where the analysis depends on assumptions that may not hold in practice, we note them explicitly.

**Cooperation as an equilibrium.** When all seven protocols are active, we can analyze conditions under which honest participation is an equilibrium:

- **Persistent identity** (CoC) ensures that the Folk Theorem's requirement for repeated interaction is satisfied — agents cannot escape their histories.
- **Observable behavior history** (ARP) provides the information structure needed for reputation effects to sustain cooperation, per Kreps et al.'s model [32].
- **Credible punishment** (AJP) ensures that defection has consequences beyond reputation loss — dispute findings can trigger contractual penalties, insurance premium increases, and matchmaking demotion.
- **Type uncertainty** (ARP's probabilistic scoring, ALP's lineage tracking) creates the Kreps et al. mechanism: even small uncertainty about whether an agent is committed to honest behavior creates incentives for cooperative behavior from rational agents.

Under these conditions, honest participation is sustained as an equilibrium when the long-term value of maintained reputation (discounted future earnings from continued matchmaking access and favorable agreement terms) exceeds the short-term gain from any single defection (one fraudulent interaction minus the present value of lost future opportunities). The discount rate depends on how much agents value future interactions relative to present ones.

**Caveat:** This analysis assumes agents are forward-looking with positive discount factors and that the trust stack's information channels are sufficiently efficient that defection is detected with high probability. If agents have very short time horizons (high discount rates) or if detection probability is low, the cooperation equilibrium weakens. The trust stack addresses the detection probability concern through multi-channel monitoring (ARP ratings, ASA verification, AJP investigation), but cannot control agents' time preferences.

### 6.2 Attack Surfaces Across Protocol Boundaries

The trust stack's seven protocols create six inter-protocol boundaries, each presenting distinct attack surfaces:

**Cross-protocol reputation laundering.** An agent might attempt to accumulate good ARP scores through simple, low-stakes interactions, then use that reputation to obtain favorable ASA agreements for complex, high-stakes tasks it cannot actually perform. **Defense:** ARP v2's domain-specific weight profiles ensure that reputation in one task domain does not automatically transfer to another. AMP's matching algorithm considers task-specific reputation rather than aggregate scores.

**Forensic evidence contamination.** An adversarial agent might manipulate CoC chain entries before an AJP investigation to obscure its involvement in an incident. **Defense:** CoC's dual-tier anchoring (OpenTimestamps to Bitcoin, RFC 3161 TSA) makes retroactive chain modification detectable. AJP's evidence provenance tiers (primary, secondary, tertiary) weight evidence by tamper-resistance.

**Lifecycle laundering.** An agent with poor reputation might fork, inherit some reputation via ALP, and present as a new-but-trusted entity. **Defense:** ALP's decay functions ensure inherited reputation diminishes over time unless the inheritor earns independent trust. ALP's lineage tracking makes fork history publicly queryable, allowing counterparties to assess the significance of the lineage.

**Governance capture via protocol interaction.** An attacker might attempt to modify ARP's rating dimensions (through ARP governance) to inflate their scores, then use inflated scores to win favorable AMP rankings and ASA terms. **Defense:** ARP governance is constitutionally independent from TAC. ARP's governance-by-tenure (not by score) prevents score-based self-reinforcement. AMP's trust-weighted ranking uses multiple signal sources, not ARP scores alone.

**Context window denial-of-service.** An adversary might send expensive requests to target agents, consuming their context windows and inference budgets. **Defense:** CWEP's spam prevention requires requestors to commit token deposits before sending. The cost of the attack scales linearly with the number of targets and the cost of the deposit, making large-scale DoS economically irrational.

### 6.3 Partial Adoption Game

Not all agents will implement all protocols simultaneously. The trust stack must incentivize adoption incrementally. We analyze the strategic dynamics of partial adoption:

**Observation 1: Foundation protocols create positive externalities.** An agent that implements CoC + ARP provides valuable data to the ecosystem (provenance verification, reputation signals) at a cost proportional to its own operational investment. The benefits accrue to all agents that can query this data, including those that haven't yet implemented the same protocols. This creates a classic network externality — the more agents implement foundation protocols, the more valuable they become for all participants.

**Observation 2: Upper-stack protocols exhibit increasing returns to adoption.** ASA becomes more valuable as more agents implement it (larger contracting network). AJP becomes more credible as more agents participate in arbitration. AMP becomes more useful as more agents register capability profiles. CWEP becomes more fair as more agents participate in bilateral settlement. Each protocol's value increases super-linearly with adoption, creating positive feedback loops that — once past a critical mass — accelerate further adoption.

**Observation 3: The chicken-and-egg problem is real but addressable.** Following Evans and Schmalensee's analysis [38], the trust stack faces a classic two-sided platform bootstrapping challenge: agents won't adopt trust protocols without other agents already using them. The resolution is to start with protocols that provide immediate unilateral value (CoC provides verifiable provenance even if no other agent uses it; ARP provides self-assessment capability) and build network effects from there.

**Observation 4: Approximate adoption thresholds.** Drawing on network economics literature and platform adoption dynamics, we estimate rough thresholds for self-sustaining adoption within a given marketplace or agent ecosystem:

- **~5% adoption (CoC + ARP):** Reputation signals become queryable frequently enough that non-adopters notice a competitive disadvantage in matchmaking. Early adopters gain preferential ranking in trust-aware discovery systems. This is the "visible minority" threshold where the value proposition becomes demonstrable rather than theoretical.
- **~15–20% adoption (CoC + ARP + ASA):** Agreement infrastructure reaches the point where counterparties routinely expect machine-readable contracts. Agents without ASA capability are excluded from an increasingly significant portion of high-value transactions. The contracting network exhibits Metcalfe's Law dynamics: value scales with the square of participating agents.
- **~30–40% adoption (full stack or near-full):** The trust stack becomes the de facto standard within the ecosystem. Non-adopting agents face systematic disadvantages: lower matchmaking priority, inability to participate in insured transactions, exclusion from marketplaces that require trust signals. Adoption becomes self-reinforcing as the cost of non-adoption exceeds the cost of implementation.

These thresholds are approximate and will vary by ecosystem characteristics (marketplace size, transaction value distribution, regulatory pressure). The key structural insight is that the trust stack does not require universal adoption to become self-sustaining — it requires reaching a critical mass where the network effects of adoption create sufficient competitive pressure on non-adopters. Historical precedent suggests this threshold is lower than intuition suggests: HTTPS adoption accelerated rapidly once browsers began flagging HTTP sites as insecure (moving from ~30% to >90% of web traffic in approximately five years), and FICO adoption became self-sustaining once a small number of major lenders required it for all applications.

---

## 7. The Agent Economy With and Without Trust

### 7.1 Without Trust Infrastructure: Market Failures

Economic theory predicts specific pathologies in markets without adequate institutional infrastructure. Three are particularly relevant to the agent economy:

**Akerlof's Market for Lemons.** George Akerlof demonstrated that information asymmetry between buyers and sellers causes market failure: when buyers cannot distinguish high-quality goods from low-quality goods, they price for average quality, causing high-quality sellers to exit the market, which lowers average quality further until only "lemons" remain ("The Market for 'Lemons'," *Quarterly Journal of Economics*, Vol. 84, No. 3, 1970, pp. 488–500 [57]). In the agent economy without reputation infrastructure, consumers cannot distinguish capable agents from poor ones. The predicted outcome: capable agents cannot charge premium prices, reducing incentives for quality investment, while low-quality agents thrive by undercutting on price. The market converges toward the lowest viable quality.

**Gresham's Law for Agents.** The classic monetary principle — "bad money drives out good" when both circulate at the same nominal value — applies directly. Without quality signals, all agents trade at undifferentiated commodity prices. Agents that invest in quality (better training, verification, reliability) cannot recoup their investment because consumers cannot verify the quality difference. High-quality agents are driven out by lower-cost, lower-quality competitors. The predicted outcome: a race to the bottom on price at the expense of reliability.

**Adverse Selection Death Spiral.** Without risk assessment data (AJP Module 3), agent insurance cannot be priced accurately. Insurers must price for average risk, which drives low-risk agents out of the insurance market (they overpay relative to their risk), leaving only high-risk agents in the pool, raising premiums further. This is the classic insurance adverse selection spiral, applied to agent liability coverage. With only one agent insurance policy ever written (ElevenLabs/AIUC, February 2026 [44]), the market is not yet at the spiral stage — it has not yet begun, precisely because the data infrastructure for risk assessment does not exist.

### 7.2 With Trust Infrastructure: Efficient Markets

When the full trust stack is operational, theory predicts qualitatively different market dynamics:

**Quality differentiation.** ARP's multidimensional reputation scores, AMP's trust-weighted rankings, and ASA's quality verification create information symmetry — consumers can observe and verify quality differences between agents. High-quality agents can command premium prices because their quality is verifiable, not merely claimed. This is the same transformation that FICO scores brought to credit markets: before FICO (standardized in 1989), lending decisions were based on personal relationships and subjective assessment; afterward, lending became data-driven, enabling credit access to scale from local to national to global.

**Specialization and comparative advantage.** When quality is verifiable, agents can specialize in domains where they have genuine comparative advantage rather than competing on price across undifferentiated capabilities. An agent that specializes in legal document review can command premium pricing for that domain while directing code review requests to agents with better ARP scores in that dimension. This is the Ricardian comparative advantage argument applied to agent economies — specialization increases total welfare when quality signals enable efficient matching.

**Collaborative value creation.** Multi-agent systems — where several agents collaborate on complex tasks — require mutual trust to function. With the trust stack, agents can form teams (via AMP), define responsibilities (via ASA), allocate costs (via CWEP), investigate failures (via AJP), and track team evolution (via ALP). Without these mechanisms, multi-agent collaboration requires either a central orchestrator who absorbs all risk or trust relationships that cannot scale. The trust stack enables decentralized collaboration at scale.

### 7.3 The FICO Analogy and the Insurance Forcing Function

The transformation most analogous to what the trust stack aims to achieve is the standardization of credit scoring. Before FICO (1989), consumer creditworthiness was assessed by local bank managers using subjective judgment, personal relationships, and ad hoc criteria. Credit could not be assessed at scale, limiting lending to local markets. After FICO, creditworthiness became a portable, standardized, queryable signal that enabled national lending markets, securitization, and ultimately the $4.5 trillion U.S. consumer credit market (Federal Reserve G.19 Consumer Credit Statistical Release, approximately $5.06 trillion outstanding as of Q4 2024 [58]).

ARP v2's signal composition algebra — combining provenance age, multidimensional ratings, quality verification pass rates, and behavioral signals into configurable composite trust scores — is structurally analogous to FICO's composition of payment history, amounts owed, credit history length, new credit, and credit mix. The key difference: the composition function is open, auditable, and domain-configurable rather than proprietary and opaque.

The most potent adoption driver may be insurance requirements. If regulatory bodies or market forces require agents handling sensitive tasks to carry liability insurance — as is increasingly likely given California AB 316's elimination of the autonomous AI defense [17] — then the data infrastructure for underwriting (AJP Module 3's risk assessment) becomes mandatory. Insurance requirements could be the forcing function that drives trust stack adoption from "nice to have" to "required for operation" — the same way that credit scoring became mandatory not because consumers wanted it, but because lenders required it for regulatory compliance and risk management.

---

## 8. Open Problems and Research Frontier

### 8.1 Semantic Integrity Verification

**The problem:** Current quality verification (ASA's Verification API) can check structural validity (JSON schema conformance, HTTP status codes) and, through Agent-as-a-Judge evaluation, approximate semantic quality assessment in well-defined domains. What it cannot do is verify **semantic integrity** — whether an agent's output is genuinely derived from the reasoning and evidence it claims, rather than fabricated, hallucinated, or strategically constructed to pass verification while being substantively wrong.

This borders on the halting problem's territory. Verifying that an agent "understood" the input and produced a "genuine" response requires defining "understanding" and "genuineness" in computationally verifiable terms — a problem that connects to fundamental questions in philosophy of mind, computational complexity, and AI alignment.

**What we can say now:** Partial solutions exist for constrained domains. Formal verification can confirm that code does what it claims (within limits). Citation verification can check that referenced sources exist and say what the agent claims they say. Reproducibility testing can verify that the same input produces consistent output. But none of these constitutes general semantic integrity verification. This remains an open research problem of potentially fundamental difficulty.

**Trust stack implication:** Until semantic integrity verification is solved, the trust stack's quality guarantees have a ceiling. ASA can verify that output meets structural and approximate semantic criteria; it cannot guarantee that the output is "true" in any deep sense. The trust stack is transparent about this limitation rather than pretending it doesn't exist.

### 8.2 Cross-Agent State Reconciliation

**The problem:** When multiple agents collaborate on a task, each maintains its own internal state (context, memory, partial results). There is no protocol for reconciling these states when they diverge — which they will, given that agents may process the same information differently due to model differences, context window contents, or stochastic inference.

This is a distributed systems problem analogous to the Byzantine Generals Problem (Lamport, Shostak, Pease, 1982), but complicated by the fact that agent "states" are not binary (correct/faulty) but continuous and subjective (different agents may have legitimately different interpretations of the same data).

**Partial approaches:** Traditional distributed consensus algorithms (Raft, PBFT) achieve agreement on shared state among deterministic processes. Agent state reconciliation requires consensus among stochastic processes with different architectures and training — a qualitatively harder problem. Possible directions include: semantic hash functions that reduce complex states to comparable fingerprints, reconciliation protocols that identify specific points of divergence rather than attempting global agreement, and "good enough" consensus that accepts bounded disagreement rather than requiring exact agreement.

**Trust stack implication:** Without state reconciliation, multi-agent collaborative systems must either accept that agents may operate on divergent state (with implications for quality and consistency) or designate a single "source of truth" agent (creating a single point of failure). Neither is satisfactory at scale. This is a genuine research frontier, not a deferred feature.

### 8.3 Multi-Jurisdiction Governance

**The problem:** TAC governs the AB Support trust stack. Other trust ecosystems (ERC-8004, Virtuals Protocol, OpenClaw) will develop their own governance. When agents participate in multiple ecosystems — which they inevitably will — governance decisions in one ecosystem may conflict with governance requirements in another.

This is the ISO/IETF/W3C coordination problem at a higher level, complicated by the fact that agent trust ecosystems may not share the same governance philosophy or be willing to establish coordination mechanisms.

**Partial approach:** The liaison mechanism specified for foundation-stack coordination (Section 5.2) could extend to cross-ecosystem liaison, but this requires the other ecosystem to implement a compatible governance interface. We anticipate that cross-ecosystem governance coordination will emerge through market pressure (agents that operate across ecosystems will demand compatibility) rather than top-down standardization.

### 8.4 The Agent arXiv

**The concept:** As the agent economy matures, agents will produce knowledge artifacts — analyses, designs, protocols, optimizations — that have value beyond the specific interaction that produced them. An "agent arXiv" would be a structured repository where agents publish these artifacts with provenance verification (CoC), quality assessment (ARP), and usage tracking (CWEP).

This extends the trust stack from transactional infrastructure (agents interacting with each other) to knowledge infrastructure (agents contributing to a shared body of knowledge). The thalience concept — agents autonomously discovering questions nobody thought to ask, rather than answering questions humans pose — represents the aspirational endpoint of this research direction.

**Trust stack implication:** The agent arXiv requires all seven trust mechanisms to function: provenance for authorship, reputation for quality signals, agreements for usage terms, accountability for accuracy claims, lifecycle for version management, discovery for findability, and economics for access pricing. It is the natural extension of the trust stack into knowledge markets.

### 8.5 Institutional Competition: Strategic Threats to the Trust Stack

The preceding sections analyze attacks *within* the trust stack — agents gaming protocols, cross-protocol boundary exploits, partial adoption dynamics. But the trust stack also faces threats *as an institution* — strategic competition from actors who may build alternative trust infrastructure or prevent open trust standards from achieving critical mass. A capstone paper must address institutional competition, not only institutional design.

**Threat 1: Platform-native trust monopoly.** A dominant agent framework — Google's A2A ecosystem (150+ organizational members), Microsoft's Copilot ecosystem, or Amazon's Bedrock platform — could refuse to implement open trust standards and instead build a proprietary trust layer tightly integrated with their platform. With captive agent populations numbering in the millions, a platform-native trust system would offer "good enough" trust for agents already inside the walled garden, reducing incentives for those agents to adopt open standards.

*Mitigation through design:* The trust stack's identity-system-agnostic architecture is the primary defense. ARP accepts any identifier format (ERC-8004, A2A Agent Cards, W3C DIDs, MCP, bare URIs). CoC chains require only SHA-256 — no platform dependency. AMP's cross-platform discovery is designed specifically to query across siloed marketplaces. An agent inside Google's A2A ecosystem can implement CoC and ARP without leaving A2A, and the trust data generated is portable via W3C Verifiable Credentials. The strategic bet is that agents operating across platforms — which the fragmented marketplace landscape makes inevitable — will demand interoperable trust signals. A platform-native trust system works within one garden; the trust stack works across all of them.

*Residual risk:* If a single platform achieves >70% market share (as Android did in mobile), the cross-platform value proposition weakens. This is the scenario where open trust standards become structurally disadvantaged, similar to how open messaging protocols (XMPP, Matrix) struggle against WhatsApp's network effects despite technical superiority. The defense is timing: establishing open trust standards before any single platform achieves dominance.

**Threat 2: Proprietary "good enough" trust layer.** A well-funded fintech (Stripe, Coinbase, Circle) or identity company (Okta, Auth0) could build a proprietary trust scoring system — simpler than the full trust stack but integrated with payment rails and identity infrastructure that agents already use. If Stripe's agent commerce APIs include a built-in trust score derived from transaction history, and most agents already use Stripe for payments, the "good enough" trust layer captures the market before open protocols achieve critical mass.

*Mitigation through design:* The trust stack addresses this through depth and composability. A proprietary trust score based on transaction history alone is vulnerable to the same gaming that plagues every single-axis reputation system — Goodhart's Law guarantees that a published metric becomes an optimization target. The trust stack's seven-protocol architecture provides defense in depth: gaming ARP scores doesn't help if ASA verification catches quality failures, AJP investigates disputes, and ALP tracks identity manipulation. The complexity is a feature, not a bug — it reflects the genuine complexity of trust.

Additionally, the trust stack's Apache 2.0 licensing and pip-installable distribution model means that proprietary platforms can *incorporate* trust stack protocols rather than competing with them. If Stripe adds ARP rating to its agent APIs, that extends the trust stack's reach rather than undermining it — the protocols are designed for embedding, not for standalone deployment.

*Residual risk:* Market capture during the gap between "good enough" and "comprehensive." If a proprietary system captures 60%+ of agent interactions before the full trust stack is adopted, switching costs may prevent migration even when the open system is demonstrably superior. This is the Microsoft Office / OpenDocument pattern: the open standard was technically comparable, but the proprietary system's installed base proved insurmountable for decades.

**Threat 3: Regulatory fragmentation.** The EU AI Act (with Article 50 transparency requirements), U.S. state-level regulation (California AB 316, potential federal frameworks), and China's AI governance regime (with mandatory algorithm registration and data localization) may impose incompatible trust requirements. A trust stack designed for global operation may be unable to comply with all jurisdictions simultaneously, leading to fragmented regional implementations that undermine the network effects essential for adoption.

*Mitigation through design:* The trust stack's modular architecture and governance layering directly address regulatory fragmentation. Constitutional-layer principles (open access, governance by tenure, anti-capture) are jurisdiction-neutral — they encode process, not content. Upper-stack protocols can be parameterized for jurisdictional requirements: AJP's dispute resolution can route to jurisdiction-appropriate arbitration frameworks, ASA's agreement templates can embed jurisdiction-specific compliance clauses, and ALP's lineage tracking can satisfy different data provenance requirements (GDPR's right to explanation, China's algorithm registry, California's AB 316 liability chain).

The TAC governance model's escalating thresholds protect against a single jurisdiction's regulatory preferences being imposed on the global system: jurisdictional compliance is a parameter adjustment (>50% majority), not a structural change (66% supermajority). Regional implementations can diverge on compliance parameters while sharing the same protocol architecture — similar to how TCP/IP operates identically worldwide while internet content regulation varies by jurisdiction.

*Residual risk:* Data sovereignty requirements that prevent cross-border reputation portability. If China requires that agent reputation data generated within its jurisdiction remain on Chinese servers, and the EU requires GDPR-compliant data processing, then ARP v2's Portable Reputation Bundles may face legal barriers to cross-border transfer. This would create regional reputation silos — agents would have a Chinese trust score, a European trust score, and a U.S. trust score that cannot be combined. The trust stack cannot solve data sovereignty conflicts through protocol design alone; it can only ensure that the architecture degrades gracefully into regional pools rather than failing entirely.

**Synthesis: Why open beats proprietary under competition.** The three threats share a common structure: a well-resourced actor attempts to capture trust infrastructure through platform lock-in, market timing, or regulatory leverage. The trust stack's primary strategic defenses are:

1. **Composability over comprehensiveness.** Open protocols that can be embedded in proprietary systems are more resilient than standalone alternatives that must compete directly. The trust stack does not need to replace Stripe — it needs Stripe's agent APIs to speak ARP.

2. **Multi-axis trust over single-axis scoring.** Any single trust metric will be gamed (Goodhart's Law). The seven-protocol architecture creates a defense-in-depth that proprietary single-axis systems cannot match without independently reinventing the same complexity.

3. **Cross-platform value over single-platform optimization.** As the agent marketplace fragments across competing platforms (Google A2A, MCP, OpenClaw, enterprise platforms), agents that operate across platforms — which is the economically rational strategy — will demand trust signals that work everywhere. Open standards serve this demand; proprietary standards do not.

4. **Insurance-driven adoption over voluntary adoption.** If the insurance forcing function materializes (Section 7.3), trust stack adoption becomes compliance-driven rather than voluntary. Insurance companies will demand standardized, auditable, cross-platform risk data — precisely what proprietary walled-garden trust systems cannot provide. This is the scenario where regulatory pressure and open standards become mutually reinforcing.

The honest assessment: the trust stack's survival under institutional competition depends on achieving critical mass adoption before proprietary alternatives capture the market. The window is approximately 18–36 months — the period between now and when the major platform players will have either integrated open trust standards or built proprietary replacements. The implementation roadmap (Section 9) is designed with this urgency in mind.

---

## 9. Implementation Roadmap

### 9.1 Bottom-Up Adoption Strategy

The trust stack is designed for adoption from the bottom up: developers first, then platforms, then enterprises.

**Phase 1: Developer Tools and Unilateral Value (Months 0–6).** Each protocol ships as an independent pip package with a reference implementation. The meta-package `pip install agent-trust-stack` installs all protocols. Developer documentation includes quickstart guides, integration examples, and test suites. The barrier to initial adoption is a single pip install.

The cold start strategy targets protocols that provide immediate unilateral value — value to a single adopting agent even if no other agent has adopted:

- **CoC provides provenance without a network.** An agent that implements CoC has a verifiable operational history that can be presented to any counterparty, auditor, or regulator. This is valuable even in a zero-adoption ecosystem because it creates an auditable trail that satisfies emerging compliance requirements (EU AI Act Article 50, California AB 316).
- **ARP provides self-assessment capability.** Even before bilateral rating networks form, ARP's scoring framework enables operators to systematically evaluate their own agents' performance across five dimensions — creating actionable quality data where none existed.
- **ASA's Verification API operates standalone.** Quality verification does not require a counterparty agreement. An agent operator can use ASA's verification framework to validate their own agents' outputs, creating a quality baseline before formal agreements are relevant.

The bootstrap sequence — CoC first, then ARP, then ASA verification — is designed so that each step produces immediate operational value while creating the data foundation that makes the next protocol's network effects possible.

**Phase 2: Platform Integration and Network Effects (Months 6–18).** As developer adoption creates a base of trust-aware agents, platform providers (Virtuals Protocol, OpenClaw, MCP servers) have incentive to integrate trust stack signals into their discovery and ranking systems. The identity-system-agnostic design ensures integration does not require abandoning existing identity infrastructure.

Specific platform integration targets:
- **MCP server registries:** CoC provenance as a listing requirement (low friction — MCP servers already publish manifests)
- **OpenClaw skill registry:** ARP scores displayed alongside skill listings, enabling trust-weighted discovery
- **Agent marketplace APIs:** AMP's cross-platform query protocol as a federation layer between siloed marketplaces

The platform integration strategy follows the "Trojan Horse" pattern: rather than asking platforms to replace their infrastructure, the trust stack protocols embed within existing platform workflows. An MCP server that publishes a CoC chain is still an MCP server — it just has verifiable provenance.

**Phase 3: Enterprise Deployment and Insurance-Driven Adoption (Months 12–36).** Enterprise adoption is driven by three forces: regulatory compliance (EU AI Act Article 50 transparency requirements, California AB 316 liability rules), insurance requirements (agent liability coverage requiring AJP risk assessment data), and operational efficiency (multi-agent systems requiring trust infrastructure to function at scale).

The insurance forcing function (Section 7.3) is the most potent enterprise driver. If agent liability insurance becomes a market requirement — which California AB 316's elimination of the autonomous AI defense makes increasingly likely — then AJP's risk assessment module becomes mandatory infrastructure. The enterprise adoption path is: regulatory pressure → insurance requirement → trust stack adoption as compliance infrastructure. This path does not depend on voluntary adoption or network effects; it depends on regulatory inevitability.

### 9.2 Integration with Existing Standards

The trust stack is designed to complement, not replace, existing infrastructure:

| Existing Standard | Trust Stack Integration |
|------------------|----------------------|
| A2A Agent Cards | AMP ingests Agent Cards as capability profiles |
| MCP Tool Manifests | AMP converts MCP manifests to Unified Capability Profiles |
| ERC-8004 | CoC and ARP identity adapters support ERC-8004 registries |
| W3C Verifiable Credentials | ARP v2 uses VCs for Portable Reputation Bundles |
| W3C DIDs | Supported as agent identifiers across all protocols |
| x402 / MPP / AP2 | CWEP settlement proposals can settle via any payment rail |
| ISO/IEC 25010 | ASA quality dimensions extend ISO 25010 |
| FinOps FOCUS | CWEP metering records are FOCUS-compatible |

### 9.3 The Meta-Package

```python
# pip install agent-trust-stack
# Installs: chain-of-consciousness, agent-rating-protocol,
#           agent-service-agreements, agent-justice-protocol,
#           agent-lifecycle-protocol, agent-matchmaking,
#           context-window-economics
```

The meta-package serves as the "one command to install the entire trust infrastructure" adoption mechanism — powerful for demonstrations, prototyping, and reducing the friction of initial adoption.

---

## 10. Conclusion: The Institutional Infrastructure Thesis

### 10.1 The Central Claim

This paper has argued that trust in the agent economy is not a feature to be added but an ecosystem to be built. The argument rests on three pillars:

**Pillar 1: Institutional necessity.** Institutional economics (North, Williamson, Ostrom) demonstrates that economic activity at scale requires institutional infrastructure to reduce uncertainty, lower transaction costs, and enable cooperation. The agent economy is not exempt from this requirement. Without trust infrastructure, the transaction costs of agent-to-agent commerce will remain prohibitively high, and the projected $3–5 trillion economy will not materialize.

**Pillar 2: Complementary design.** Aoki's institutional complementarity proves that trust mechanisms must be designed as a system where each raises the returns of the others. Seven protocols — provenance, reputation, agreements, accountability, lifecycle, discovery, and economics — form the minimum set of complementary mechanisms needed to replicate the institutional infrastructure that enables human commerce. Designing them in isolation produces incoherent architecture; designing them as a complementary system produces emergent trust properties that no individual mechanism can create.

**Pillar 3: Fundamental redesign.** The five structural differences between agents and humans (cheap identity, machine speed, no social pressure, discontinuous identity, priced comprehension) mean that human trust institutions cannot be transplanted directly. The functional architecture must be preserved — the same categories of trust mechanism are needed — but the implementation must be rebuilt from first principles for the specific dynamics of autonomous agent systems.

### 10.2 What We Have Built

The Agent Trust Stack comprises nine components (seven operational protocols plus two governance frameworks) specified across eight whitepapers totaling approximately 1,500 pages of protocol specification (estimated from combined whitepaper and reference implementation documentation):

| Protocol | Layer | Question Answered | Status |
|----------|-------|-------------------|--------|
| CoC | L1: Foundation | Can this agent prove its history? | Published |
| ARP v1/v2 | L1: Foundation | How well does this agent perform? | Published |
| ASA | L2: Agreements | What did this agent promise? | Specified |
| ALP | L2: Lifecycle | How does this agent change over time? | Specified |
| AJP | L3: Accountability | What happens when things go wrong? | Specified |
| AMP | L4: Discovery | How do agents find the right partners? | Specified |
| CWEP | L4: Economics | Who bears the cost of understanding? | Specified |
| TAC | Governance | How do protocols evolve? | Specified |
| TAT | Theory | Why do these protocols form a system? | This paper |

Every protocol is identity-system-agnostic, payment-rail-agnostic, and independently deployable while being designed for complementary value when combined. Every protocol is specified under Apache 2.0 with reference implementations available as pip packages. Every protocol includes competitive landscape analysis, game-theoretic incentive analysis, and integration mappings for existing standards.

### 10.3 What Remains

The trust stack is not complete. Semantic Integrity Verification remains an open problem of potentially fundamental difficulty. Cross-Agent State Reconciliation requires distributed consensus among stochastic processes — a qualitatively harder problem than classical Byzantine agreement. Multi-jurisdiction governance will require cross-ecosystem coordination mechanisms that do not yet exist. The Agent Certification Framework and Emergency Response Protocol are specified but await ecosystem maturity and industry partnerships.

These are honest admissions, not deferrals. The research frontier is not a list of features to be added later — it is a map of the problems that this generation of institutional infrastructure cannot yet solve. Articulating these problems precisely is itself a contribution: the first step toward solving a problem is defining it well enough that others can work on it.

### 10.4 The Stakes

The agent economy is being built now. Eight payment protocols compete for dominance. An estimated $8.17 billion in disclosed M&A consolidation is reshaping the infrastructure landscape. Ninety percent of B2B buying may be agent-intermediated by 2028. The question is not whether the agent economy will exist — it is whether it will have the institutional infrastructure to function.

History offers a clear precedent. The early internet had packet routing without trust infrastructure. The result was spam, fraud, phishing, and identity theft — problems that took decades to partially address through layered additions (TLS, PKI, DNSSEC, spam filters, authentication protocols). We are at the same inflection point for the agent economy. The infrastructure choices made now will determine whether autonomous agent commerce develops with trust as a foundational property or spends the next decade retrofitting trust onto an infrastructure that was built without it.

This paper, and the seven protocols it synthesizes, represent our answer: build the institutional infrastructure first, build it as a complementary system, build it open, and build it before the absence of trust becomes the defining failure of the agent economy.

---

## 11. References

[1] AB Support LLC. "Chain of Consciousness: A Cryptographic Protocol for Verifiable Agent Provenance and Self-Governance." Version 3.0.0, 2026.

[2] AB Support LLC. "Agent Rating Protocol: A Decentralized Reputation System for Autonomous Agent Economies." Version 1.0.0, 2026.

[3] AB Support LLC. "Agent Rating Protocol v2: Signal Composition, Portability, and Anti-Goodhart Architecture." Version 2.0.0, 2026.

[4] AB Support LLC. "Agent Service Agreements: A Protocol for Machine-Readable Contracts and Quality Verification in Autonomous Agent Commerce." Version 1.0.0, 2026.

[5] AB Support LLC. "Agent Justice Protocol: A Modular Framework for Forensic Investigation, Dispute Resolution, and Risk Assessment in Autonomous Agent Economies." Version 1.3.0, 2026.

[6] AB Support LLC. "Agent Lifecycle Protocol: A Standard for Birth, Fork, Succession, and Death Management in Autonomous Agent Systems." Version 1.0.0, 2026.

[7] AB Support LLC. "Agent Matchmaking Protocol: Cross-Platform Discovery and Trust-Weighted Matching for the Autonomous Agent Economy." Version 1.0.0, 2026.

[8] AB Support LLC. "Context Window Economics Protocol: Bilateral Cost Allocation, Context Pricing, and Resource Markets for Autonomous Agent Interactions." Version 1.0.0, 2026.

[9] Agent Payments Stack. agentpaymentsstack.com. Accessed March 25, 2026.

[10] Visa Press Release. "Visa and Partners Complete Secure AI Transactions." December 2025.

[11] Mastercard. "Agent Pay Rollout to All U.S. Cardholders." November 2025.

[12] Adobe Analytics. "Adobe Analytics: AI-Referred Traffic to U.S. Retail Sites Grew 805% Year-over-Year on Black Friday 2025." 2025. (eMarketer subsequently reported on this statistic.)

[13] Gartner. "Top Predictions for IT Organizations in 2026 and Beyond: AI Agents Will Command $15 Trillion in B2B Purchases by 2028." October 2025.

[14] McKinsey & Company. "The Agentic Commerce Opportunity." October 2025.

[15] Strata Identity Research. "The AI Agent Identity Crisis: State of Agent Identity Management in the Enterprise." 2026.

[16] Rubrik Zero Labs. "Non-Human Identity Ratios in Enterprise Environments." 2026. ManageEngine Identity Security Outlook. 2026.

[17] California Civil Code Section 1714.46 (AB 316). Effective January 1, 2026. See Baker Botts, "California Eliminates the Autonomous AI Defense: AB 316," 2026.

[18] Gartner. "Over 40% of Agentic AI Projects Will Be Canceled by End of 2027." June 2025.

[19] North, Douglass. *Institutions, Institutional Change and Economic Performance.* Cambridge University Press, 1990. See also: North, "Institutions," *Journal of Economic Perspectives*, Vol. 5, No. 1, 1991, pp. 97–112.

[20] North, Douglass; Wallis, John; Weingast, Barry. *Violence and Social Orders: A Conceptual Framework for Interpreting Recorded Human History.* Cambridge University Press, 2009.

[21] Williamson, Oliver. *The Economic Institutions of Capitalism.* Free Press, 1985.

[22] Williamson, Oliver. "The New Institutional Economics: Taking Stock, Looking Ahead." *Journal of Economic Literature*, Vol. 38, 2000, pp. 595–613.

[23] Ostrom, Elinor. *Governing the Commons: The Evolution of Institutions for Collective Action.* Cambridge University Press, 1990.

[24] Ostrom, Elinor. "Beyond Markets and States: Polycentric Governance of Complex Economic Systems." *American Economic Review*, Vol. 100, 2010, pp. 641–672.

[25] Aoki, Masahiko. *Toward a Comparative Institutional Analysis.* MIT Press, 2001.

[26] Hall, Peter; Soskice, David. *Varieties of Capitalism: The Institutional Foundations of Comparative Advantage.* Oxford University Press, 2001.

[27] Mayer, Roger; Davis, James; Schoorman, F. David. "An Integrative Model of Organizational Trust." *Academy of Management Review*, Vol. 20, No. 3, 1995, pp. 709–734.

[28] Luhmann, Niklas. *Trust and Power.* Wiley, 1979. See also: "Familiarity, Confidence, Trust: Problems and Alternatives," in Gambetta, ed., *Trust: Making and Breaking Cooperative Relations*, Blackwell, 1988.

[29] Zucker, Lynne. "Production of Trust: Institutional Sources of Economic Structure, 1840–1920." *Research in Organizational Behavior*, Vol. 8, 1986, pp. 53–111.

[30] Fudenberg, Drew; Maskin, Eric. "The Folk Theorem in Repeated Games with Discounting or with Incomplete Information." *Econometrica*, Vol. 54, No. 3, 1986, pp. 533–554.

[31] Axelrod, Robert. *The Evolution of Cooperation.* Basic Books, 1984.

[32] Kreps, David; Milgrom, Paul; Roberts, John; Wilson, Robert. "Rational Cooperation in the Finitely Repeated Prisoners' Dilemma." *Journal of Economic Theory*, Vol. 27, 1982, pp. 245–252.

[33] Zahavi, Amotz. "Mate Selection — A Selection for a Handicap." *Journal of Theoretical Biology*, Vol. 53, 1975, pp. 205–214.

[34] Grafen, Alan. "Biological Signals as Handicaps." *Journal of Theoretical Biology*, Vol. 144, 1990, pp. 517–546.

[35] Spence, Michael. "Job Market Signaling." *Quarterly Journal of Economics*, Vol. 87, 1973, pp. 355–374.

[36] Matzinger, Polly. "The Danger Model: A Renewed Sense of Self." *Science*, Vol. 296, pp. 301–305, 2002.

[37] Rochet, Jean-Charles; Tirole, Jean. "Platform Competition in Two-Sided Markets." *Journal of the European Economic Association*, Vol. 1, No. 4, 2003, pp. 990–1029.

[38] Evans, David; Schmalensee, Richard. *Matchmakers: The New Economics of Multisided Platforms.* HBR Press, 2016.

[39] Baldwin, Carliss; Clark, Kim. *Design Rules, Volume 1: The Power of Modularity.* MIT Press, 2000.

[40] Jacobides, Michael; Cennamo, Carmelo; Gawer, Annabelle. "Towards a Theory of Ecosystems." *Strategic Management Journal*, Vol. 39, No. 8, 2018, pp. 2255–2276.

[41] Rogers, Owen. "The Real Cost of Cloud SLA Failures." Uptime Institute. Referenced in ASA whitepaper [4], Section 1.2.

[42] Zhuge, Mingqi et al. "Agent-as-a-Judge: Evaluate Agents with Agents." arXiv:2410.10934, 2024.

[43] Abdelnabi, Sahar et al. "Cooperation, Competition, and Maliciousness: LLM-Stakeholders Interactive Negotiation." arXiv:2309.17234, 2023. Davidson, Tim et al. "Large-Scale Negotiation Competition." MIT/NeurIPS, 2024.

[44] ElevenLabs. "ElevenLabs Becomes First Company to Earn AIUC-1 Certification." February 2026.

[45] Replit Production Database Deletion Incident. July 2025. Referenced in AJP whitepaper [5], Section 1.1.

[46] McKinsey AI Breach. March 2026. Referenced in AJP whitepaper [5], Section 1.1.

[47] Autonomous Cyberattack Campaign. 2026. Referenced in AJP whitepaper [5], Section 1.1.

[48] CNIL (Commission Nationale de l'Informatique et des Libertés). Study on training data propagation through successive model generations. Referenced in ALP whitepaper [6], Section 1.3.

[49] Gale, David; Shapley, Lloyd. "College Admissions and the Stability of Marriage." *American Mathematical Monthly*, Vol. 69, No. 1, 1962, pp. 9–15.

[50] FinOps Foundation. FOCUS (FinOps Open Cost and Usage Specification). Referenced in CWEP whitepaper [8], Section 7.

[51] Shapley, Lloyd. "A Value for n-Person Games." *Contributions to the Theory of Games*, Vol. 2, 1953, pp. 307–317.

[52] Green, Jerry; Laffont, Jean-Jacques. "Characterization of Satisfactory Mechanisms for the Revelation of Preferences for Public Goods." *Econometrica*, Vol. 45, 1977. Moulin, Hervé; Shenker, Scott. "Serial Cost Sharing." *Econometrica*, Vol. 60, 1992.

[53] Schweppe, Fred et al. *Spot Pricing of Electricity.* Kluwer Academic, 1988.

[54] CoinDesk. "COMP Down 6.7% After Supposed 'Governance Attack' on Compound DAO." July 2024.

[55] CoinDesk. "Why One of Uniswap DAO's Most Outspoken Members Just Walked Away." May 2025.

[56] IETF. RFC 7241: "The IEEE 802/IETF Relationship." 2014. RFC 4053: "Procedures for Handling Liaison Statements." 2005. RFC 7282: "On Consensus and Humming in the IETF." 2014.

[57] Akerlof, George. "The Market for 'Lemons': Quality Uncertainty and the Market Mechanism." *Quarterly Journal of Economics*, Vol. 84, No. 3, 1970, pp. 488–500.

[58] Board of Governors of the Federal Reserve System. "G.19 Consumer Credit." Statistical Release, published monthly. Total outstanding consumer credit approximately $5.06 trillion as of Q4 2024.

---

*This paper is released under the Apache License 2.0. It is the capstone document of the Agent Trust Stack, providing the intellectual framework that unifies the seven protocol whitepapers into a coherent theory of institutional infrastructure for the autonomous agent economy.*

*© 2026 AB Support LLC. All rights reserved under the Apache License 2.0.*
