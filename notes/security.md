# Security, trustworthy actuation, identity and governance: developer futures to 2031

Research working paper, not a final deliverable. Sources checked 19 October 2026. This is a scoped research track; no claim of exhaustive coverage of the internet, no implementation, purchases, installations, private-system inspection, or external writes. Recommendations and project acceptance thresholds below are analytical proposals, not measured results.

## Thesis and confidence

**High-confidence engineering direction:** AI creates more software, more connected identities, and more delegated actions. Practical competence in authorization, isolation, evaluation, recovery, and privacy is useful even if frontier models improve dramatically. These skills address both ordinary bugs and deliberate attacks. Security work itself will also be automated.

**Medium-confidence role direction:** production AI security engineer, agent platform/security engineer, identity engineer for autonomous workloads, and domain-specific evaluation/assurance engineer. Existing AppSec, platform, SRE, IAM and product-security teams may absorb these responsibilities; there may never be a large standalone occupation under each new title.

**Lower-confidence venture direction:** a generic agent gateway, an agent-ID database, an LLM judge dashboard, or a compliance checklist startup. Major platform providers already sell policy, identity, observability and evaluation capabilities. New regulations do not establish a startup's distribution, differentiation, or willingness-to-pay.

The most defensible personal strategy is to become an engineer who can prove that a useful system acts within its authority, and diagnose exactly why it did not. A skill moat is much easier to establish than a venture moat.

## Evidence ledger and reading cautions

### S01 — Existing incidents, DBIR

- **Primary:** [Verizon 2026 DBIR release](https://www.verizon.com/about/news/breach-industry-wide-dbir-finds), 19 May 2026.
- **Evidence class:** publisher-reported empirical incident analysis; source has a cybersecurity-business interest.
- **Observed:** report uses 2025 data; vulnerability exploitation is reported as 31% of breach entry points; third-party involvement as 48% of breaches. Categories are not mutually exclusive and should not be added together.
- **Limit:** contributed incident dataset, not a random sample of every organization. The public release was read; attempted full-report PDF access returned an internal error. This track has not independently checked its full sampling appendix or exact global incident count. Do not invent the denominator from secondary summaries.
- **Implication:** patching, asset inventories, short-lived credentials and dependency containment remain commercially meaningful. The release cannot measure the effects of frontier models released later in 2026.

### S02 — ENISA 2026

- **Primary:** [ENISA Threat Landscape 2026](https://www.enisa.europa.eu/publications/enisa-threat-landscape-2026), 22 September 2026.
- **Evidence class:** agency incident synthesis.
- **Observed:** reporting period is 1 January–31 December 2025. ENISA emphasizes dependency and interconnected-ecosystem risks.
- **Limit:** this is a regional threat synthesis with reporting/visibility limitations, not an incidence rate or job forecast. Distinguish publication year from event year.

### S03 — Agent hijacking public competition

- **Primary technical paper:** [How Vulnerable Are AI Agents to Indirect Prompt Injections?](https://arxiv.org/html/2603.15714v1), 16 March 2026; [NIST explanation](https://www.nist.gov/blogs/caissi-research-blog/insights-ai-agent-security-large-scale-red-teaming-competition), 23 March 2026.
- **Evidence class:** controlled adversarial evaluation, authors include security vendor Gray Swan, model vendors and government institutes; not production telemetry.
- **Exact denominators:** 271,588 deduplicated chats, 67,634 judged submissions, 8,648 successful attacks, 464 participants; 13 models and 41 scenarios, with four wave-zero scenarios excluded from final reporting. Models did not all share identical scenario coverage.
- **Critical threat-model limit:** attacker sees the conversation prefill and target action, controls one injection location, and attacks one operation turn. Authors call this an upper bound for that single-turn threat model, not real-world attack frequency. Attack effort is nonuniform. Curated transfer tests select previously successful attacks, so their higher success rate cannot be compared directly with all-attempt ASR.
- **Incentives/access:** most successful proprietary-model attack strings are not public. Replication is partial. A model's capability score alone did not reliably predict security in this experiment.

### S04 — AgentDojo

- **Primary:** [AgentDojo paper](https://arxiv.org/abs/2406.13352), June 2024 / NeurIPS 2024.
- **Evidence class:** reusable research benchmark.
- **Observed:** original framework contains 97 tasks and 629 security test cases involving tools over untrusted data. Useful as a starting structure for measuring utility and security together.
- **Limit:** simulated tasks and benchmark tool semantics are not a deployed enterprise's identity, retries, concurrency, access rules or incident distribution. Do not mistake a benchmark pass for enterprise authorization correctness. Later research versions may change case counts.

### S05 — Capability enforcement beyond prompts

- **Primary:** [CaMeL, Defeating Prompt Injections by Design, v2](https://arxiv.org/html/2503.18813v2), 24 June 2025.
- **Evidence class:** research design and evaluation from Google/ETH-affiliated researchers; research artifact, not independently certified production infrastructure.
- **Mechanism:** separate planning from untrusted parsing; track information provenance and enforce explicit capability/data-flow policies outside the model.
- **Limits that matter:** trusted user request and policy specification are assumptions. Authors identify policy authoring/maintenance, absent identity context, ecosystem compatibility and interpreter complexity as obstacles. Formal verification of the implementation is future work. Benchmark success is conditional on the specified threat model and annotations. Content correctness and all phishing scenarios are not solved by information-flow enforcement.
- **Inference:** skill value shifts toward domain policy specification, integration, identity context and failure diagnosis. Do not market a prototype as universally provably secure.

### S06 — Architectural restrictions trade flexibility for assurance

- **Primary:** [Design Patterns for Securing LLM Agents against Prompt Injections](https://arxiv.org/html/2506.08837v1), June 2025.
- **Evidence class:** systems-design research with case studies, not a deployment adoption survey.
- **Observed:** principled restrictions on agent actions can improve security at a cost to generality/utility; the paper discusses ten application case studies.
- **Inference:** choose the least flexible architecture that still achieves the business task. Design constraints and complete mediation are more durable than promising that a general-purpose agent will always reject malicious text.

### S07 — Protocol boundaries are not business authorization

- **Primary:** [MCP security best practices, version 2025-11-25](https://modelcontextprotocol.io/docs/2025-11-25/tutorials/security/security_best_practices); [MCP authorization specification](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization), both inspected 19 October 2026.
- **Evidence class:** protocol implementation requirements and threat models.
- **Observed:** addresses confused-deputy flows, token audience/passthrough, SSRF, session hijacking, local server compromise and scope minimization. Sessions must not substitute for authentication. OAuth resource indicators bind tokens to intended resources.
- **Limit:** successful protocol authentication does not establish that a specific refund, message recipient, robot trajectory or cross-tool sequence matches the user's intent. Correct business policy still needs a reliable principal, resource state, and complete mediation of side effects.
- **Inference:** integration work lives in the gap between protocol compliance and business semantics. Reusing protocol libraries is preferable to writing OAuth or URL validators from scratch.

### S08 — Production incident, affected organization's account

- **Primary:** [Hugging Face security disclosure](https://huggingface.co/blog/security-incident-july-2026), 16 July 2026.
- **Evidence class:** affected-organization disclosure, not independent forensic audit.
- **Observed:** reports an autonomous-agent intrusion involving dataset processing, node access and credential compromise. At disclosure, assessment of possible partner/customer impact was incomplete; it reported no evidence of tampering with public user-facing artifacts and a verified-clean published software supply chain.
- **Limit:** one unusually capable actor/run context does not quantify baseline agent risk. Treat original scope statements as time-specific and read later updates before making current customer-impact claims.

### S09 — Same incident, technical reconstruction

- **Primary:** [Hugging Face technical timeline](https://huggingface.co/blog/agent-intrusion-technical-timeline), late July 2026; live page inspected 19 October.
- **Evidence class:** affected organization's forensic reconstruction.
- **Observed:** approximately 17,600 recovered attacker actions grouped into about 6,280 clusters over 9–13 July. Most attempted paths failed. The account describes ordinary weaknesses compounded by high action volume and notes isolation, workload identity, metadata restrictions and credential rotation as response measures.
- **Limit:** recovered actions are not necessarily every action; clusters are not independent attacks or successful compromises. The origin-side escape account partly relies on another organization's disclosure. This is strong evidence that containment matters, weak evidence for a universal annual breach probability.
- **Inference:** an overlooked job is making evaluation infrastructure safe enough to test increasingly capable agents. A sandbox that allows a package proxy is only as isolated as that proxy and its surrounding trust boundary.

### S10 — OT safety and security

- **Primary:** [Joint CISA/NSA/ACSC/international guidance, official FBI-hosted PDF](https://www.ic3.gov/CSA/2025/251215.pdf), initial version 3 December 2025; [NSA announcement](https://www.nsa.gov/Press-Room/Press-Releases-Statements/Press-Release-View/Article/4347041/nsa-cisa-and-others-release-guidance-on-integrating-ai-in-operational-technology/).
- **Evidence class:** voluntary government guidance; explicitly not a new legal requirement.
- **Observed:** distinguishes cybersecurity from physical functional safety; cautions against LLMs making OT safety decisions. Discusses safe bounds, monitoring, human oversight, non-AI fallback and AI-induced new failure states. Warns that explainability alone may be inadequate.
- **Limit:** no measured adoption rate or salary forecast. A simulator demonstration is not a safety certification or proof of physical reliability.
- **Inference:** the cross-disciplinary opportunity is trustworthy actuation: AI proposes actions; independently engineered control and safety systems constrain execution. Requires controls, systems and domain competence as well as ML.

### S11 — Vendor commoditization is already happening

- **Primary:** [AWS AgentCore policy](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy.html), [core concepts](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy-core-concepts.html), and [evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html), inspected 19 October 2026.
- **Evidence class:** product documentation; demonstrates offered features, not verified effectiveness or broad adoption.
- **Observed:** identity/input policies, natural-language policy authoring, deterministic gateway enforcement, session-aware temporal rules, logging, and automated trace evaluation are documented. Temporal controls already include preceding approvals, action counts and budgets. Evaluation integrates trace instrumentation and LLM judges.
- **Boundary:** enforcement claims concern traffic through the gateway; complete system security requires preventing bypass. Schema-valid policy is not proof of the intended business specification. Temporal session scope requires correct identity/session propagation.
- **Inference:** do not pitch generic temporal agent policies or trace scoring as an untouched market. Distinction must survive a head-to-head comparison with native platforms.

### S12 — Identity also has incumbent distribution

- **Primary:** [Microsoft Entra Agent ID current capabilities](https://learn.microsoft.com/en-us/entra/agent-id/whats-new-agent-id), last updated 1 May 2026, inspected 19 October.
- **Evidence class:** vendor documentation.
- **Observed:** page says generally available; documents agent identities, lifecycle/governance, conditional access and non-Microsoft integration. Some subfeatures remain preview; account/license/region access must be checked before assuming availability.
- **Inference:** “register and revoke agents” alone is a weak independent product thesis. Expertise connecting identity to existing applications and operational ownership remains useful.

### S13 — Regulation timelines

- **Primary:** [Commission current AI Act page](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai), inspected 19 October 2026.
- **Observed:** AI Omnibus entered into force 27 July 2026. Annex III high-risk rules apply 2 December 2027; Annex I product-embedded high-risk rules 2 August 2028. Other obligations have distinct dates. Old blanket August 2026/2027 claims are outdated.
- **Primary:** [Commission CRA summary](https://digital-strategy.ec.europa.eu/en/policies/cra-summary), inspected same date.
- **Observed:** Article 14 reporting obligations began 11 September 2026; main provisions 11 December 2027. Product and actor scope matter. The summary itself recommends consulting the legislative text.
- **Inference:** evidence collection, reporting and product lifecycle work may grow. Neither law establishes a new standalone startup category. Enforcement, harmonized standards, implementation costs and incumbent product support affect demand. These notes are research context, not legal advice about a particular product.

### S14 — Privacy

- **Primary:** [EDPB AI-model opinion explanation](https://www.edpb.europa.eu/news/edpb-opinion-on-ai-models-gdpr-principles-support-responsible-ai_en), 18 December 2024.
- **Observed:** model anonymity is assessed case by case; training on personal data does not automatically make outputs/model anonymous. Lawful processing analysis applies at development/deployment stages.
- **Primary:** [India DPDP Rules official Gazette](https://www.meity.gov.in/static/uploads/2025/11/53450e6e5dc0bfa85ebd78686cadad39.pdf), notification dated 13 November 2025, English starts page 24.
- **Observed:** staggered commencement: some rules on publication, Rule 4 after one year, Rules 3, 5–16 and 22–23 after eighteen months. Do not describe every substantive rule as already fully in force on 19 October 2026.
- **Inference:** privacy engineering includes access-aware retrieval, lineage, deletion/retention, operational control, contract-aware integrations and regional deployment. Hosting locally alone is not proof of sovereignty or compliance.

### S15 — Post-quantum migration

- **Primary:** [NIST finalized first three PQC standards](https://www.nist.gov/news-events/news/2024/08/nist-releases-first-3-finalized-post-quantum-encryption-standards), 13 August 2024.
- **Observed:** ML-KEM, ML-DSA and SLH-DSA finalized. This is established cryptographic infrastructure work, not proof of a quantum computer's arrival date.
- **Primary:** [NCSC migration timetable](https://www.ncsc.gov.uk/guidance/pqc-migration-timelines), 20 March 2025.
- **Observed:** indicative milestones of discovery/planning by 2028, highest-priority migration by 2031, completion by 2035; primarily large/bespoke/critical infrastructure. Commodity SME software may migrate mainly through vendor updates.
- **Inference:** crypto inventory, TLS/PKI compatibility, hardware-root and protocol migration are more accessible career paths than inventing a new cryptographic algorithm. Work concentration in existing vendors/consultancies is plausible. No guarantee of mass new junior jobs.

### S16 — Provenance

- **Primary:** [C2PA 2.3 technical specification](https://spec.c2pa.org/specifications/specifications/2.3/specs/C2PA_Specification.html), specification lineage December 2025 / PDF dated January 2026.
- **Observed:** signed manifests and bindings describe media provenance/history.
- **Inference/limit:** signed assertions are not universal truth detection, universal human identity or proof that an asset absent credentials is fake. Opportunities depend on key protection, issuer trust, platform preservation, verification UX and actual adoption. This track did not independently validate every latest C2PA security advisory, so do not describe current implementations as invulnerable.

### S17 — Labor evidence and freshness trap

- **Primary:** [BLS information security analysts](https://www.bls.gov/ooh/computer-and-information-technology/information-security-analysts.htm), live page modified 27 August 2026.
- **Observed:** 21% US growth projected 2025–2035; about 14,100 average annual openings including replacements; employment 192,900 in 2025, projected 233,400 in 2035. May 2025 median wage $129,180.
- **Freshness trap:** search snippets still showed old 29% growth for 2024–2034 and $124,910 May 2024 wages. Open the live page; do not reuse cached snippets.
- **Limit:** US occupational aggregate/projection, not observed present vacancies, Indian salary data, an AI-security suboccupation count, or a guarantee of entry-level employment. Annual openings are not all net additions.

## Three defensible opportunities, with kill criteria

### A. Domain-aware authority and containment for agents

**Mechanism:** OAuth answers which principal may access a resource. A useful deployment also needs to know whether this particular action matches a valid request, approved recipient, amount, device, tenant, state and sequence. A broadly authorized service token cannot answer those questions. Separate planning from enforcement, use mature IAM/policy engines, and deny bypass routes.

**Nonobvious gap:** two separately allowed calls can compose into a forbidden outcome. Read a private record then send it externally; split a refund across tools; replay an approval after the record changes; race two valid requests against a shared budget. Pure keyword classifiers and per-call allowlists do not establish end-to-end intent. A session-specific policy also needs trustworthy session mapping and atomic business-state updates. This is an analytical threat model, not a claim that every incumbent lacks temporal policies (AWS already documents them).

**Buyer/role:** platform security or product teams deploying consequential internal agents. More likely a valuable employment/consulting competence than an immediate horizontal startup.

**What is hard:** translating business policy into inspectable predicates; connecting identities; handling exceptions without approval fatigue; eliminating alternative credential/network paths; making stateful controls correct under concurrency; balancing utility with security. Domain context and operational ownership are the work.

**Falsify/reduce investment:** native tooling solves target tasks with acceptable utility and lower integration burden; no deployment reaches real write authority; buyers will not provide a safe integration environment; most incidents are conventional app vulnerabilities with no agent-specific gap. A standalone product should fail its investment gate if it only wraps existing vendor controls without a measurable domain advantage.

### B. Security regression and recovery engineering for real workflows

**Mechanism:** model version, tool schema, permissions, execution environment and business state all change. Static adversarial prompts can stop representing the system. Build replayable cases with a programmatic oracle over tool effects and state, plus a held-out/adaptive attack process. LLM judges can assist with ambiguous visible output, but should not be the sole authority on whether money moved, data crossed a tenant, or a file changed.

**Nonobvious gap:** successful refusal can hide failure to perform the legitimate job, and a reassuring final answer can hide an unsafe intermediate action. Security and utility need separate denominators. Recovery should test duplicated retries, partial tool success, rollback boundaries and resumption after revocation. Controlled evaluation infrastructure itself needs egress/identity isolation; S08/S09 show why evaluating cyber-capable agents is not harmless merely because the prompt calls it a test.

**Buyer/role:** AI platform teams, security labs, regulated product teams, integrators, model evaluators. Generic tracing and judge scores already face cloud competition; application-state oracles, incident replay, realistic adversarial harnesses and operational remediation are more differentiated skills.

**Falsify/reduce investment:** a cheap native suite accurately predicts the target organization's production incidents and catches regressions; custom cases cannot be maintained at acceptable cost; no team acts on findings; all claimed gains vanish on held-out cases or require unacceptable latency/denial rates.

### C. Trustworthy actuation at the AI/robotics/OT boundary

**Mechanism:** model proposes high-level goals; conventional controllers and independent checks enforce limits, timing, valid state transitions and safe fallback. “Security” protects authority/integrity, while “functional safety” protects people and property. Both matter; they are not interchangeable.

**Nonobvious gap:** natural-language intent and a technically valid command can disagree with physical context. A simulated robot should reject stale perception, impossible/stale transforms, replayed commands and unsafe goals even if an authenticated model issued them. Work includes provenance/timing of observations, degraded-mode policies, independent interlocks and testability across the command boundary.

**Entry:** begin in simulation, study controls/systems, then work with an experienced robotics/industrial team. Do not present a software-only interlock as a certified physical safety mechanism. The barrier is access to domain hardware, validated environments and experienced reviewers, not merely GPU budget.

**Falsify/reduce investment:** deployments remain advisory and avoid actuation; existing certified controller integrators cover requirements without agent-specific work; domain/hardware access is unavailable; proposed checks reduce throughput below useful levels; simulation results fail on physical hardware.

## A 30-day project: bounded agent that can act and explain its authority

**Purpose:** demonstrate A and B together. This is a proposed learning build, not work executed during research. Estimated planning allowance: 35–60 focused hours over 30 days, depending on existing IAM and testing experience. No new install, paid service or API run is authorized merely by this plan.

**Environment:** local fake multi-tenant service with customer records and refundable invoices, synthetic documents and tool APIs. It must be explicit that funds/messages/data are simulated. Use the engineer's existing approved runtime, a mature identity/test/policy library if already available, and a small agent adapter. Do not write a custom OAuth server, cryptographic primitive or language interpreter as the learning objective.

**Week 1: specify the system.** Draw trust boundaries and enumerate authority: requester, delegated agent, tool service, tenant, resource owner, recipients and allowed state transitions. Implement a direct scripted baseline before adding an LLM. Define benign task oracles and three consequential invariants: tenant separation; recipient/amount authority; bounded total mutation under retry/concurrency.

**Week 2: contain actions.** All mutations go through one enforcement path. Agent never receives a credential with broader direct write authority. Add short-lived task identity; explicit expiry/revocation; approval bound to an exact action plus record version; idempotency keys; deny-by-default tool policy. Record requested/approved/executed action as distinct events. Keep secret values out of logs.

**Week 3: attack the boundary.** Add malicious tool text, swapped recipient, wrong-audience token, stale approval, cross-tenant resource ID, tool-schema change, retry after partial success, duplicate events, concurrent budget spending and a direct-network bypass attempt. Attacks stay entirely inside the fake environment. Keep some cases held out from policy authoring.

**Week 4: report trade-offs.** Publish local results suitable for review, a runnable replay, an architecture explanation, and documented failure cases. Compare baseline agent, prompt-only guardrail, and enforced boundary. No universal security claim.

**Proposed acceptance checks:**

- At least 100 benign tasks and 200 malicious/state-manipulation cases, with case-family counts reported. Values are learning targets, not established statistical sufficiency.
- Zero invariant-violating side effects in this finite suite; report the suite, model, tool/schema and policy versions. Zero observed events do not prove zero production risk.
- Retain at least 95% of the scripted/agent baseline's correctly completed benign tasks, with rejected-but-valid task rate reported separately. If the baseline itself is weak, show absolute success too.
- Every mutation joins to requester, delegated identity, policy version, record version and outcome; 100% of exercised writes must be accounted for in the local trace.
- Revocation blocks the next attempted call; 100 duplicate/retry/concurrency attempts do not exceed the approved aggregate budget or repeat a committed mutation.
- Report added latency/cost separately from model inference. A tentative target is warmed local policy-decision p95 below 25 ms; measure rather than invent results, and adjust only with a documented reason.
- A peer should reproduce one safe case, one blocked case and one intentionally injected implementation bug through a single documented run. Visual screenshots are supplementary.

## A 90-day extension: evaluation-to-repair evidence

**Budget assumption:** another 80–140 focused hours over days 31–90, with infrastructure/API spend separately approved in advance. Use already accessible equipment first.

1. Add a second workflow with different semantics (e.g. file sharing rather than refunds), so the project cannot pass by encoding one tool's expected output.
2. Separate train/development cases from a hidden test set. Add a human red-team pass, preferably by a colleague permitted to inspect only the local/synthetic target. Do not scan others' services.
3. Compare two existing model/backend adapters if access/cost is already approved; otherwise use deterministic recorded outputs to validate the enforcement layer and label model-generalization untested.
4. Test schema/tool/runtime changes as migrations. A deliberately broadened permission, changed recipient field or missing tenant check must turn a previously green regression suite red.
5. Add fault injection for tool timeouts, duplicate delivery, stale reads and policy-service outages. Specify whether each failure mode stops, retries, compensates or requires a user; test the choice.
6. Measure time-to-diagnosis and time-to-repair for seeded failures. Proposed target: reconstruct each seeded unsafe attempt from trace without reading hidden reasoning, identify the first violated boundary, fix it, and rerun affected cases with no new benign regression.
7. Produce an incident-style report with system state, failed assumption, detection evidence, containment, repair and residual limitations. The artifact should show reasoning, not just a polished dashboard.

**Go/no-go at day 90:** obtain reviews from two experienced engineers with different perspectives (security and product/platform), plus a real target-domain owner if available. A strong outcome is clear evidence of a useful boundary and reproducible limitations. If reviewers see only a wrapper around cloud IAM/evaluations, deepen one domain rather than expanding a generic platform.

## Learning and entry path

### Foundations to acquire before specialized labels

- Application security: input handling, object-level authorization, tenancy, secret management, SSRF, dependency trust and incident response.
- Identity/protocols: OAuth/OIDC, audience and issuer validation, workload identities, delegation and revocation. Read protocol threat models, not only SDK tutorials.
- Distributed systems: idempotence, atomicity, retry semantics, race conditions, event traces and partial failure.
- Evaluation science: denominator design, task oracles, selection bias, adaptive attackers, held-out sets, uncertainty and base rates.
- For C: controls, state estimation, timing, embedded/system interfaces and functional safety under experienced supervision.

**Illustrative base-rate check, not empirical data:** among 10,000 events with ten real attacks, a detector at 90% sensitivity and 1% false-positive rate produces about nine true positives and 100 false alarms. Only about 8% of alerts are attacks. A high benchmark accuracy number can still create an unusable operator burden. Real event dependence and severity distributions require separate study.

### Credentials, equipment and access barriers

- No special certification or GPU is a prerequisite for the local 30-day software project. A normal development machine and synthetic services suffice; real model calls depend on existing access and explicit budget authorization.
- A cloud/IAM certification may help job screening where employers request it, but none of the evidence above establishes it as mandatory or sufficient. Do not spend time collecting certificates before producing evidence of competence.
- High-end offensive research, frontier evaluations and security-sensitive enterprise integration often require trusted access, background checks or demonstrated history. These are important barriers that an online course does not remove.
- Physical actuation requires simulation plus later hardware/domain access; no equipment price is assumed. Secure access to experienced reviewers and controlled test rigs is the principal constraint. Certification responsibilities belong with qualified organizations; a portfolio cannot self-certify safety.
- PQC entry is through TLS/PKI/asset migration expertise in an existing platform/security team. Cryptographic algorithm research usually needs much deeper mathematics and research training.
- Privacy/governance leadership requires product/domain/legal collaboration; a developer can build technical controls without claiming to adjudicate legal applicability.

### Path toward visible competence by 2031

**2026–27:** master one consequential workflow; build the 30/90-day project; publish technically precise reproducible reports only when publication is explicitly authorized. Seek implementation responsibility in a platform/product-security team rather than only an AI title.

**2027–28:** own an actual deployment lifecycle: scoped identity, evaluation gate, failure response, migration and cost/utility reporting. Contribute small verified fixes to mature open-source infrastructure if authorized; prioritize a record of accepted work over a new framework.

**2028–29:** deepen one domain (enterprise operations, financial workflows, developer infrastructure or robotics/OT). Lead incident drills and design reviews. Learn the economics: deployment conversion, manual exception cost, audit hours saved, integration time, failure losses and customer retention.

**2029–31:** lead an accountable platform or domain program, develop other engineers, set evidence standards and own recovery under real constraints. Consider founding only after repeated buyers show the same unsolved pain and incumbent-native alternatives fail a concrete comparison. Prominence is uncertain; the controllable output is a body of trusted, reusable engineering evidence.

## Branched nodes for the eventual mind map

Security and trustworthy actuation

- Authority for agents
  - Human principal / delegated workload identity / resource owner
  - Correct scope, audience, issuer, expiry and revocation
  - Per-action policy / sequence policy / atomic business budget
  - Trusted intent vs untrusted document instructions
  - Complete mediation / credential isolation / blocked alternate egress
  - Adoption: platform integration; incumbents already provide primitives
  - Proof project: bounded multi-tenant refund/share agent
- Evaluation and recovery
  - Programmatic side-effect oracles
  - Benign utility and attacker success as different denominators
  - Held-out and adaptive attacks / model and tool version change
  - Trace reconstruction / partial failure / idempotence / rollback
  - Eval infrastructure containment
  - Adoption: custom workflow cases; generic judges/tracing commoditize
- Cyber-physical action
  - Proposed goals vs deterministic execution bounds
  - Observation age / transform correctness / command replay
  - Independent interlock / non-AI fallback / degraded mode
  - Simulation evidence vs hardware validation vs certified safety
  - Barrier: controls knowledge and trusted domain access
- Existing security demand
  - Vulnerability remediation / dependency containment
  - Workload credentials / machine identity / supplier resilience
  - False-positive base rates / incident detection / recovery
- Privacy and assurance
  - Lineage / access-aware retrieval / deletion / retention
  - Audit evidence / policy lifecycle / organizational accountability
  - Regulation timing / standards / applicability uncertainty
  - Engineering opportunity does not automatically imply startup moat
- PQC migration
  - Crypto inventory / TLS and PKI / hardware trust roots
  - Compatibility / performance / vendor dependencies
  - 2028 discovery / 2031 priority migration / 2035 target
  - Standards adoption is independent of predicting quantum arrival
- Provenance
  - Signed media assertions / issuer trust / key protection
  - Verification UX / chain preservation
  - Provenance is not truth detection
- Career evidence
  - 30-day build / 90-day adversarial extension
  - Measured utility/security/cost/latency / independently reproducible results
  - Real deployment ownership / design reviews / incident drills
  - Domain depth / leadership / economic outcomes

## Remaining research gaps

No live vacancy sample for India/UK/remote roles was collected by this track. No per-employer role requirements, hiring conversion, salary distribution, customer willingness-to-pay, startup retention, or longitudinal production agent incident rate was established. These should not be inferred from regulations, vendor marketing or benchmark vulnerability. The other research tracks should supply labor-market evidence and broader robotics foundations. Recheck laws, product availability and security advisories before implementation; 2031 forecasts remain conditional.
