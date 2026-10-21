# Round 2: Can native platforms commoditize agent security and evaluation?

Working research note, checked 19 October 2026. Scope: challenge the prior trustworthy-agent integration thesis against effective native products and empirical counterevidence. No installations, account changes, cloud resources, private-system reads, contacts, purchases, or experiments were performed. All proposed tests require existing approved tooling/access or separately approved setup and spend. This is not the final mind map or final report.

## Revised conclusion

Native platforms already provide substantial security, identity, policy and evaluation machinery, and there is credible evidence that native AI assistants improve identity-administration and incident-investigation tasks. It is no longer defensible to describe temporal action policies, agent identity or trace scoring as untouched markets.

Residual engineering work is concrete: application identity/session binding, actual effective permissions, trustworthy policy attributes, domain intent, realistic fault oracles, complete mediation, and recovery under partial failure. Those are valuable skills. The evidence does **not** establish a large new occupation, a wage scarcity premium, or a venture moat. Many organizations may use existing platform/IAM/SRE teams and buy fewer incremental tools.

The best provisional career direction is **a strong product/platform engineer who can operate mature security and evaluation infrastructure around consequential workflows**. Narrow specialization in a proprietary gateway or prompt-attack detector is a weaker hedge. Confidence in a horizontal startup is lower than confidence in the skill bundle.

## Research method and what counts as evidence

Searched primary AWS/Microsoft documentation, product service cards and pricing, named customer accounts, technical research papers, and independent security-research disclosures. Opened underlying pages instead of relying on search snippets. Inspected method, denominator, threat model, observed-versus-planned distinctions, product boundaries and disclosures. Followed negative results rather than treating every failure as a business opportunity.

Source hierarchy here:

1. Reproducible independent experiments or scoped external technical tests: useful mechanisms and counterexamples, limited by models/tasks and researcher incentives.
2. Vendor service cards with explicit experimental methods: more informative than launch claims, still internally evaluated and selected.
3. Named customer testimony: evidence that a deployment/evaluation was reported, not independent causal validation or representative adoption.
4. Product documentation/pricing: evidence of offered supply and contractual/technical boundaries; no proof of realized outcomes or customer willingness-to-pay.
5. Announcements, anonymous stories and social threads: discovery only. They are not used to estimate effectiveness, jobs or market size.

No random sample of customers, procurement budgets, renewals, agent-security specialist vacancies, wages, or tool switching preferences was collected. No source establishes an unconditional production failure rate for native platforms. Sparse independent testing must not be described as proof that native platforms fail, nor their absence as proof that they are safe.

## Rival causal models

### M1 — Native platforms absorb the horizontal layer

**Claim:** agent security becomes a normal checkbox/service in AWS, Azure and existing enterprise identity systems. Configuration and migration remain, but a small number of platform specialists support many developers. Generic policy/identity/evaluation startups face bundling and low marginal prices.

**Supporting evidence:** AgentCore already offers deterministic gateway checks, temporal policies, natural-language authoring and trace evaluation. Entra has dedicated identities and lifecycle controls. Native identity agents improve administrators' measured work in an RCT. AWS's named customer evaluations report useful investigation speedups even with imperfect root-cause accuracy.

**Prediction:** on well-bounded tasks, native configuration matches a custom layer's safety and utility with less bespoke code and lower maintenance cost. The custom layer disappears after migration.

**Disconfirmation:** repeated material policy gaps cannot be expressed or tested natively, require cross-system state unavailable to the platform, or remain expensive after competent configuration. Even then, first test whether a thin application adapter solves the issue before proposing a new platform.

### M2 — Integration and specification remain the bottleneck

**Claim:** execution machinery commoditizes, but each business still must define trusted principals/attributes, authorization semantics, state transitions, exceptions and recovery. Existing backend/security engineers acquire a stronger specialization.

**Supporting evidence:** AWS explicitly leaves session-to-user mapping and execution-role scoping to the customer; Cedar warns that correct policy writing remains the user's responsibility. Independent Entra tests show effective permissions require understanding several linked objects and ownership paths. Formal policy synthesis still assumes correctly approved intent.

**Prediction:** most project hours move from implementing a gateway to data/identity mapping, policy review, lifecycle and regression cases. A useful portfolio identifies and reduces these hours.

**Disconfirmation:** native setup agents and verifier-guided synthesis consistently recover correct domain intent with minimal human review across held-out workflows; the adapter becomes short, standard, and low-maintenance. That would weaken the scarcity thesis while preserving ordinary engineering value.

### M3 — Organizations constrain autonomy instead of buying more security

**Claim:** a cheap read-only assistant plus explicit human action, or an ordinary deterministic workflow, captures enough value. Most customers never authorize the dangerous action surface that agent-security vendors assume.

**Supporting evidence:** AWS DevOps Agent's service card emphasizes read-only resource access and approval-gated remediation. Its useful investigation outcomes do not require unconstrained production mutation. A successful safe assistant can reduce work without creating new agent-security jobs.

**Prediction:** write-enabled agents fail to produce enough incremental business value after approval friction, risk review, support and exception costs. Customers prefer restricted tools and native suites.

**Disconfirmation:** scoped automatic execution shows repeatable additional net value over a read-only recommendation system and conventional automation, on realistic exceptions and failures, with an acceptable operating risk budget.

### M4 — Models improve enough that specialized defense shrinks

**Claim:** better refusal, planning, tool schemas and platform defaults make many specialized classifiers and policy-writing tasks uneconomic, although ordinary authorization remains necessary.

**Supporting evidence:** some models in narrow adversarial corpora already exhibit no observed unpermitted actions; policy generation and verification are active research areas. Strong native enforcement is not inherently fragile merely because it surrounds an LLM.

**Prediction:** a simple native/default system performs as well as elaborate defenses on newly collected cases, with better benign utility and cost. Specialized defense maintenance becomes more expensive than its benefit.

**Disconfirmation:** improvements fail on held-out adaptive cases or authorized-tool misuse, while a small independent authority boundary retains utility and prevents invariant violations. Test mechanisms, not model brand rankings.

## Native effectiveness and limits: inspected evidence

### E1 — AWS DevOps Agent: method is more substantial than a marketing percentage

[AWS AI Service Card](https://docs.aws.amazon.com/ai/responsible-ai/aws-aidevops-agent/overview.html), inspected 19 October 2026.

AWS describes real infrastructure with injected faults, human-curated ground truth, repeated trials, LLM semantic judgments with sampled human checking, and release/canary evaluation. Exact current results are tracked internally, limiting independent reproduction. The card identifies observability completeness, topology, integrations and customer runbooks as performance dependencies. AWS-resource access is described as read-only, with human review/approval for remediation. Customer-supplied MCP tools add customer responsibility. This is useful evidence of an operational evaluation process, not an independently established reliability number for every organization. A custom product must beat this actual baseline, not an imaginary ungoverned chatbot.

### E2 — Named customer results: useful but heterogeneous and selected

[AWS DevOps Agent customer accounts](https://aws.amazon.com/devops-agent/customers/), inspected 19 October 2026.

Megazone Cloud reports 28 investigations, 66–72% root-cause accuracy, and investigation time falling from 25–35 minutes to 3–3.5 minutes. That is meaningful reported usefulness despite imperfect accuracy. It is not the same denominator as a blanket 94% figure. Banco Bmg reports more than 350 production incidents investigated daily, a volume claim without an audited controlled outcome comparison. Xtremax explicitly describes a representative/simulated environment and reported 60-to-15-minute resolution improvement. These are named testimonies on the vendor's site, not independent trials; incident mix, selection, setup hours and ongoing corrections are not adequately disclosed for a representative ROI estimate.

### E3 — Identity work is also automatable

[Randomized Controlled Trials for Conditional Access Optimization Agent](https://arxiv.org/html/2511.13865v1), November 2025.

162 identity administrators were randomized to native agent assistance or control across four tasks. Reported averages: accuracy improved 48%; time decreased 43% holding accuracy constant. This is stronger causal evidence than testimonials, but the environment simulated a small organization; participants were recruited through Upwork, group experience was imperfectly balanced, some grading used an LLM, and long-term over-reliance/learning were not measured. It studies an Entra administration assistant, not proof that Agent ID resolves every application-authorization issue. Nevertheless, it directly challenges the notion that identity specialization necessarily creates more manual work or more seats.

### E4 — Effective native isolation still has application responsibilities

[AgentCore runtime security practices](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-security-best-practices.html), inspected 19 October 2026.

AWS documents session microVM isolation but explicitly says AgentCore does not enforce session-to-user mappings; the backend must. Code inside the VM can access execution-role credentials, so role scoping matters. CLI-generated IAM policies are broad development/test policies unsuitable for production. These are documented integration contracts, not newly discovered vulnerabilities. They identify exactly what a competent application team must supply. Native isolation plus a correctly scoped role can be an appropriate solution; adding an unneeded custom sandbox may worsen the trusted computing base.

### E5 — Native temporal policies exist; scope is specific

[Policy sessions and identity propagation](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy-session-based-temporal.html), [AgentCore policy](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy.html), inspected 19 October 2026.

History-aware native policies already address action counts, prior approvals and budgets. Their correctness depends on consistent session/identity propagation and the events seen at the gateway. This is not proof of a bypass: demonstrate a missing boundary under a legitimate configuration. Cross-session aggregate business state, authoritative application attributes and concurrent commits must be tested explicitly. A transaction budget enforced by the underlying business database may be simpler and stronger than inventing a global agent-policy ledger.

### E6 — Independent Entra testing: current residual configuration work

[Compass Security research](https://blog.compass-security.com/2026/06/entra-agent-id-from-a-security-perspective/), 9 June 2026.

Researcher tested roughly 460 object/control actions, with 60 successful, and 1,041 permission assignments across 79 resources: 97 blocked, 944 allowed. Allowed does not mean vulnerable; privileges are administrator-granted. Effective inheritance may require inspecting blueprint and principal configuration, not one agent object. Blueprint ownership/credential powers are important trust paths. The research lasted about two weeks and excluded Conditional Access, and behavior may since have changed. Compass sells security services, an incentive to document complexity. This supports effective-permission review, not a claim that every Agent ID deployment is compromised.

### E7 — A real platform bug that was fixed

[Silverfort Agent ID Administrator disclosure](https://www.silverfort.com/blog/agent-id-administrator-scope-overreach-service-principal-takeover-in-entra-id/), 23 April 2026.

The agent-administration role could reach non-agent service principals beyond its intended scope. Timeline says Microsoft confirmed behavior 26 March, it became unreproducible in pre-release 4 April, and MSRC confirmed full fix rollout 9 April. This is evidence that independently testing a new role can matter and that native vendors can patch platform flaws centrally. It is **not** an unpatched present-day exploit or proof a third-party overlay would have prevented it. Silverfort is an identity-security vendor with commercial incentives.

### E8 — Formal tools verify the modeled question

[Cedar security guidance](https://docs.cedarpolicy.com/other/security.html); [Cedar research paper](https://arxiv.org/abs/2403.04651).

Cedar has a formal model, analyzed semantics and a production engine; reusable verification is a serious native advantage. Cedar itself states users remain responsible for correct policies. A proof about evaluation/typing or policy equivalence is conditional on supplied entities, attributes and specified policy semantics. It does not make a false customer attribute true, prove that the action is the right business decision, or cover an alternate unmediated path. Do not dismiss formal machinery because its assumptions are limited; document and test those assumptions.

### E9 — CaMeL is a design reference, not the default production competitor

[CaMeL v2](https://arxiv.org/html/2503.18813v2), June 2025.

Capability/information-flow enforcement addresses untrusted-data influence under an explicit threat model. Policy authoring, identity annotations, external-tool integration, interpreter complexity and content harms remain limitations. The implementation is a research artifact. A benchmark prototype can teach principles, but replacing mature native infrastructure with a custom interpreter increases maintenance/security burden. A strong career project can port the principle of trusted planning/untrusted parsing into an existing framework while using mature enforcement components.

### E10 — Some independent out-of-band defense tests support effectiveness

[Adaptive Evaluation of Out-of-Band Defenses](https://arxiv.org/html/2606.26479v1), 25 June 2026.

LaunchSafe-affiliated researchers report an independent reproduction/extension of Progent on self-hosted Qwen2.5-7B: mean attack success fell from 25.8% to 4.2%; one handcrafted adaptive template yielded 2.6%. This is favorable evidence for external enforcement, not a universal break. Limitations: eight user tasks per suite, three repeats, weak model, one defense/attack family, no authorized-tool-only or optimized white-box attack, and a preliminary non-peer-reviewed study. It is independent of Progent's authors but not free of security-product incentives. Do not extrapolate a particular reduction to native platforms or production.

### E11 — Payment authorization evaluation sharply distinguishes outcomes

[APort Vault](https://arxiv.org/html/2609.22076v1), 18 September 2026.

Vendor-authored study: 225,964 completed evaluations from 4,371 human CTF attacks across 14 models, simulated bank/one transfer tool. Reports unpermitted transfers 140/76,842 model-alone versus 0/69,297 behind a deterministic layer; matched comparison 105 versus zero. Requests, executed payments, permission and recipient membership are separate. A permitted payment is not proof of legitimate intent. Coverage is incomplete in some multi-turn cells; local policy differs from published policy, and harness/judge details are partly withheld. Useful methodology and evidence of scoped enforcement, not independent validation of a universal passport or production fraud prevention.

### E12 — Policy specification itself is being automated

[AutoCedar](https://arxiv.org/html/2607.03656v1), 4 July 2026.

Stevens researchers report convergence on 221 self-authored CedarBench tasks using reviewed intent plus verification-guided generation, and three requirements-corpus case studies. The formal claim is explicitly conditional on the approved plan matching organizational intent; its verifier does not confer intent authority. This is early research, not a measured reduction in paid enterprise implementation hours. It challenges syntax-writing as a durable moat while reinforcing why reviewers should approve behavioral boundaries, not merely plausible-looking policy code.

## Economics, integration cost and lock-in

### Verified supply prices are not customer budgets

Current [AgentCore price page](https://aws.amazon.com/bedrock/agentcore/pricing/) lists $0.000025 per policy authorization request. Arithmetic: one million checks costs $25 for this component, before gateway, logs, runtime, models, guardrails, networking or other charges. Identity is included with Runtime/Gateway under documented conditions. Competing mainly on the cost of a generic allow/deny check is difficult.

Current [DevOps Agent pricing](https://aws.amazon.com/devops-agent/pricing/) lists $0.0083 per agent-second: an eight-minute investigation is about $3.98, excluding connected-service charges and applicable credits. That is a quote, not measured customer spend or fully loaded TCO.

Current [Microsoft Agent ID product page](https://www.microsoft.com/en-us/security/business/identity-access/microsoft-entra-agent-id) lists Agent 365 at $15/user/month paid annually and M365 E7 at $99/user/month; these are bundles with terms, not the marginal per-agent-ID price. Existing enterprise agreements and eligible licensing change economics. No purchase is recommended here.

**Documentation inconsistency to verify before planning:** the AgentCore pricing page discusses first 100 temporal policies without extra authorization charges, while the live [quota page](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/bedrock-agentcore-limits.html) says a maximum of 20 temporal policies per engine. Do not assume 100 can be deployed; use the service quota/API and current support clarification for an actual project.

### The cost that matters may be outside the invoice

Measure identity/data mapping, source observability cleanup, policy exceptions, review, incident drills, model/tool changes, evidence retention, and on-call ownership. Native fees can be small while integration is expensive. Equally, a specialist platform can add a second policy store, second identity graph and another pager. No inspected source supplied a representative estimate of setup/maintenance hours. Any such number in a business plan would currently be an assumption.

**Customer-preference hypotheses, not observed survey results:** AWS-concentrated teams may prefer native procurement, audit and operations; Microsoft-heavy enterprises may prefer bundled governance; heterogeneous/bespoke organizations may value portability. Do not assume multicloud alone guarantees willingness-to-pay. Existing teams may reject another control plane even if technically superior.

**Lock-in:** Cedar is open, while gateway entity schemas, cloud identity claims, session propagation, telemetry and managed evaluator APIs can be platform-specific. A portable policy text does not imply a portable application. Exportable case corpus, application-state oracles and business invariants are more reusable investments. Test migration cost, rather than asserting a platform is either fully open or irretrievably locked in.

## Distinguish four claims that should not be merged

| Claim | Evidence now | Evidence still needed |
|---|---|---|
| Technical skill is useful | Clear documented integration responsibilities and independent failure mechanisms | Demonstrated ability to reduce real errors and maintenance in one domain |
| Many new roles will exist | No agent-security role-count series established | Representative deduplicated vacancy/time-series data; distinguish existing team responsibilities from new hiring |
| Wages will show scarcity | No agent-specific wage premium established | Comparable offers/pay controlling geography, seniority, sector and general systems skill |
| Startup has a moat | Generic primitives bundled/priced cheaply; domain differentiation plausible | Repeated paid use, renewal, switching willingness, distribution and improvement beyond a native baseline |

Security incidents prove a problem can occur. Regulations prove obligations for particular actors. Neither identifies who captures value or how many employees a firm will hire. Better native tools can raise output while reducing hours per task.

## Falsifiable 30-day experiment: native-first versus thin custom layer

**Research proposal, not executed.** Estimated 30–50 hours. Use synthetic data and an existing approved local toolchain. If no native account or required dependency is already available, stop at the ready-to-run specification and record native effectiveness as untested; do not install or create external resources without approval. A possible separately approved cloud spend cap is $25–50, but do not treat this as the actual total cost forecast.

### Define three competing implementations before looking at results

1. **Native/restricted baseline:** mature IAM/policy engine, native trace/eval tools where approved, narrow read-only/recommendation path, explicit user commit for mutations.
2. **Native/write baseline:** same machinery plus the smallest practical write workflow, scopes, state-bound approval and idempotent commit.
3. **Thin domain layer:** same native foundations plus only the additional adapter required for application invariants. No custom identity server, policy engine, sandbox or generic dashboard.

Use one fake multi-tenant refund/share service. Underlying transactional storage is the source of truth. Scenarios cover tenant mismatch, misleading documents, stale approval, incorrect recipient, duplicate retry, two concurrent refunds, revoked identity, direct bypass and a failed/partial tool result. Keep the model and task corpus fixed across conditions; adapters may use recorded model outputs to test enforcement without API spend, labeled accordingly.

### Pre-register success and kill criteria

- 100 benign cases plus at least ten distinct adversarial/fault families with 10–20 variants each; split development and held-out cases. Report family counts and repeats, not a misleading total of correlated requests.
- Side-effect oracle reads the application's committed state; a verbal refusal is not a security pass, and a reassuring answer is not task completion.
- Compare correct benign outcomes, unsafe commits, abstentions, user approvals, operator correction minutes, median/p95 latency, external fees, and setup/maintenance hours.
- A platform is adequate for this scope if no invariant violation appears in the finite held-out suite and it preserves required benign outcomes with fewer total operating/review hours. This is local adequacy, not a universal safety certificate.
- **Kill custom layer** if native/write matches its safety/utility and setup plus a simulated policy change require no more than half its engineer hours, or if differences disappear after correctly configuring native controls.
- **Kill write autonomy** if it saves less than 15% of total operator time versus native/restricted after review and exception handling, or creates worse recoverability. The 15% is a chosen decision threshold, not a research fact.
- **Support domain-layer investment** only if a reproducible held-out failure survives competent native configuration and a small adapter fixes it without materially worse benign utility. Name the exact missing contract instead of branding the whole platform insecure.

### Deliverable at day 30

Evidence table with versions, configuration, case definitions, actual state diffs, full cost categories and known limitations. Include one negative finding where native controls work better. A useful outcome can be deciding to delete the custom layer.

## Falsifiable 90-day extension: are residual gaps economically persistent?

Estimated additional 70–120 hours, access permitting; spend separately approved. Reuse mature tools rather than building a new framework.

1. Add a second genuinely different workflow and swap identity/provider boundary while keeping application invariants constant. Measure semantic mismatches and migration hours. This tests portability value and lock-in.
2. Have another qualified reviewer configure the native baseline from documentation before judging it. Record all corrections; avoid a straw-man baseline created by a novice.
3. Run task/schema/model change drills. Blind the evaluator to implementation label. Score actual effects, legitimate task completion, intervention and recovery; assess LLM-judge disagreement against the deterministic oracle.
4. Seed at least 12 known regressions across identity mapping, policy, state/concurrency and retry layers. Measure detection coverage and time to isolate the first broken contract. A generic prompt suite that misses state failures should not receive a high assurance rating.
5. Keep human-approved intent separate from generated policy. Test native NL authoring or an already accessible verifier-guided tool against the same reviewed boundaries. Include ambiguous prose requiring an explicit product decision; do not count sensible clarification as model failure.
6. For an already authorized internal pilot only, measure four weeks of actual workflow volume, approvals, corrections and saved minutes. Without that authorization, retain a synthetic evaluation and label commercial usefulness unverified. Do not contact prospective users or export company data during this research.
7. Venture gate: require at least three independently owned workflows or organizations with the same persistent gap and a credible costed alternative; an interview alone does not establish willingness-to-pay. Paid pilots/renewals would be stronger evidence but are not authorized here.

**Interpretation:** if most residual work is one-time identity cleanup and native configuration, pursue platform employment/services expertise, not SaaS. If a reusable thin integration saves recurring maintenance and buyers prefer it after seeing the native alternative, investigate a narrow product. If no write-enabled workflow beats deterministic automation plus a human, invest in ordinary distributed-systems/product engineering and treat agents as an interface.

## Implications for a developer aiming at leadership by 2031

Become proficient enough with native tools to know when to use them and when a particular boundary remains your responsibility. Learn specification review, authorization semantics, transaction/retry correctness, observability, experimental design and incident response. Measure economic outcomes, not just attacks blocked.

The strongest visible work is a reproducible comparison that changes your own mind, removes unnecessary infrastructure, and explains remaining risk in business terms. Leading a dependable team/program is plausible; guaranteed prominence, rapidly multiplying roles and a scarcity salary premium are not established by this research.

## Outstanding gaps and next discriminating evidence

- No independent, comprehensive head-to-head security evaluation of AgentCore versus Entra versus a CaMeL-style architecture was located. Their scopes differ, so a single leaderboard would be misleading.
- AWS's internal DevOps-agent evaluation suite is not fully public; named customer results lack representative sampling and complete cost methods.
- No longitudinal Agent ID production outcomes or agent-specific budget/renewal dataset was established. General Entra IAM customer stories are not equivalent to Agent ID adoption evidence.
- June Entra tests may be stale after service changes; revisit current role/API behavior in an explicitly approved test tenant before implementation.
- Price and quota pages can change or disagree. Recheck exact region, licensing, dates, terms and effective limits before any execution.
- Domain-layer hypotheses need real workload evidence; no source supports inventing a large market from unresolved technical questions alone.
