# Human verification, repair and accepted software: economics audit

Owner: sectors_business. Round 8. Prepared **20 October 2026**, using publications available by **19 October 2026**. Public primary-source research only; no model calls, code execution from third parties, installations, data downloads, private access, outreach or shared-catalogue changes. The experiment below is proposed, not run.

## Finding

The bounded search found credible evidence that people spend time inspecting generated material, that selected AI-assisted code can be maintained without an obvious penalty, and that stronger automated reviewers can improve the review process. **It did not find a study that jointly identifies current-agent generation cost, independent human verification and repair, strict acceptance, and later maintenance cost for the same randomly assigned tasks.** There is no defensible general percentage of AI coding gains “cancelled by review” in these sources.

Two direct workflow studies are useful but have limited timing/selection designs. A large industrial study adds context and actual landing/outage outcomes, while measuring waiting-for-review rather than active reviewer labour. An automated-review deployment provides an opposing mechanism, with an incomplete causal and cost denominator. These are four studies, not four interchangeable estimates.

Read first: `software.md` (Cui/METR findings and accepted-output accounting), `agent-capability-horizons-round6.md`, `ai-evaluation-source-audit-round10.md`, and the existing preparation hour caps. No broad productivity scan or horizon-export retry was repeated. Root independently tried the two official METR YAML URLs; its reader rejected the `application/x-yaml` response, so no raw bytes or new percentiles were established.

## Four primary sources, with observation dates kept separate

### V1 — Downstream maintenance: Echoes of AI

Published **9 June 2026**; collection **October 2024–January 2025**. The preregistered Java study retained **151 successful submissions**. Its second phase randomized developers to evolve valid prior solutions without AI: **75/225 assigned participants completed**, yielding **72 usable completion times**. Initial AI use followed preference/experience rather than random assignment. Failed acceptance-test submissions were excluded; across phases, **67 timings were reconstructed from participant estimates**, and eleven values above 16 hours were removed. Second-phase median times were **136 versus 173 minutes**, with negligible rank effect and **p=0.56**; this does not establish a maintenance difference. Provenance blinding was not established by the inspected methods. [Paper, methods §§3.1–3.4, results §4.2 and limitations §6](https://link.springer.com/article/10.1007/s10664-026-10889-1)

**Interpretation:** this challenges the claim that AI-assisted code necessarily transfers an immediate maintenance penalty to another developer. It also challenges the opposite claim of equivalence: incomplete-task selection, imprecise timings and limited sample size prevent a strong bound on moderate effects. A successful follow-up feature is a useful maintenance endpoint, but it does not observe months of operational support or establish the original generation-to-maintenance cost balance. A selected set of usable artifacts should not represent the cost of all attempts that failed to produce one.

### V2 — Actual inspection of generated review comments: RevMate

The paper is **arXiv v1, 11 November 2024**; Mozilla's library page is dated January 2026. It covers **57 reviewers and 587 patch reviews**. Accepted generated comments were **34/418 evaluated at Mozilla** and **85/1,185 at Ubisoft**; uncertain cases were excluded. Ubisoft did not require evaluating every comment. There, opening-to-evaluation timestamps give a **42.9-second median per patch**, explicitly an **upper bound including distractions**, not isolated active work. **36/119 accepted comments were edited**. A downstream comparison retains **69 accepted comments on finished Ubisoft reviews** versus **1,211 human comments**; changed-hunk rates were similar, but the authors caution that revisions need not be caused by those comments. Reviewers knew they were evaluating tool suggestions. [Paper, Tables III–IV, VII–VIII and §§VI–VII](https://www.mozillafoundation.org/documents/462/2411.07091v1.pdf), [version history](https://arxiv.org/abs/2411.07091)

**Interpretation:** this is directly relevant to the cost of consuming suggestions, including rejected ones. It is not the cost of verifying AI-generated application code. Publishing a review comment is one acceptance gate; fixing a real defect and shipping correct software are later gates. The interval cannot be multiplied by all patches and called paid labour saved or lost without knowing concurrency, active attention and the counterfactual review. Likewise, low comment acceptance need not imply zero benefit: a suggestion may prompt a useful check without becoming a posted comment. The source does not quantify that indirect benefit as money.

### V3 — Industrial review and landing: Meta's context-aware analysis

Published **5 October 2026**, using approximately two months in **spring 2025**, this observational completion-tool study covers over **10,000 developers and 400,000 diffs**; roughly half have the detailed provenance used in analysis. Instrumentation coverage varies by ecosystem. “Review time” is the **interval while an author waits for review**, not reviewer active effort. Adjusted associations show somewhat faster review with more landed AI code, with centrality, size and other context explaining important variation; review-model adjusted R² is **14%**. Outages are attributed to changes through internal investigation. The tools and landed sample are pre-agentic; no randomized review assignment or full human-cost ledger is provided. [Paper, §§2.2–3, Table 1 and §4.2](https://drops.dagstuhl.de/storage/00lipics/lipics-vol394-esem2026/LIPIcs.ESEM.2026.93/LIPIcs.ESEM.2026.93.pdf), [publisher date and metadata](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ESEM.2026.93)

**Interpretation:** the strong lesson is that risky/core changes and routine changes cannot be treated as exchangeable AI/non-AI samples. A short review interval may reflect reviewer availability, priority, familiarity, an easy artifact, or less inspection. It is neither proof of lower labour nor proof of negligent rubber-stamping. Character provenance improves authorship measurement but does not randomize tool use. Conditioning on code that landed also omits the effort spent rejecting or abandoning suggestions. The analysis therefore belongs in the matrix as a workflow-latency and quality association, not a direct reviewer-time experiment.

### V4 — Opposing explanation: strong automated review can reduce the burden

OpenAI's **1 December 2025** deployment report describes a trained repository-aware reviewer with execution access and precision-oriented settings. Authors changed code after **52.7% of comments** in deployment; that is comment actionability, not a measured accepted-PR percentage. An inference-budget experiment recovers **previously human-verified issues** at less token spend than generation, but its issue set cannot assess unknown missed defects or validate newly proposed findings. Generator and reviewer share an underlying model. The report acknowledges distribution bias and no clean direct measurement of the generator–verifier advantage. It supplies no randomized active-human-time or complete downstream cost comparison. [A Practical Approach to Verifying Code at Scale](https://alignment.openai.com/scaling-code-verification/)

**Interpretation:** a diff-only, noisy reviewer is an inadequate baseline for predicting permanent human demand. Repository tools, execution, specialized training, severity filtering and automated repair are plausible substitutes for some current inspection. Conversely, known-bug recall and an author changing code cannot certify that the system finds all severe defects or that every change is correct. The discriminating comparison must give a strong native reviewer appropriate context and measure what remains, at a matched acceptance standard.

## Evidence matrix

The accompanying JSON is a compact evidence matrix, **not a meta-analysis or a dataset of individual participants**. Numerical details appear above, avoiding artificial pooling across unlike denominators.

| Source | Direct endpoint | Assignment / selection | Timing meaning | Economic quantity still missing |
|---|---|---|---|---|
| V1 | New developer completes a later feature on accepted code | Randomized follow-up; preferred initial workflow; completers retained | Mixed recorded and reconstructed task duration | Failed-attempt burden; complete lifecycle cost |
| V2 | Reviewer consumes/publishes generated comments; later revisions | Live tool study; evaluation and finished-review filters | Timestamp interval upper bound | Active counterfactual effort and defect savings |
| V3 | Code lands; review interval; attributed outages | Context-adjusted observational covered sample | Waiting interval | Reviewer attention and rejected-work cost |
| V4 | Reviewer findings and code changes; known-issue recovery | Deployment plus selected known-issue experiment | Model inference budget; no direct human-time comparison | Incremental accepted-output cost and escaped-error loss |

None measures every required bridge. V1 is the closest direct later-maintenance test; V2 the closest inspected-suggestion effort measure. V3 is useful precisely because its scale does not cure the estimand mismatch. V4 makes a blanket “humans must review everything” forecast less credible, while leaving the full economics unanswered.

## What cannot be pooled or concluded

**Generated-code review, generated-review-comment inspection and later maintenance are different treatments.** A reviewer checking a suggested warning has already been directed toward a possible issue. A maintainer changing unfamiliar code may need to build a model of the system first. A later production incident may include diagnosis, coordination, rollback and customer work. Combining their minutes as if all measured the same overhead would be misleading.

**Comprehension is a potential mechanism, not money.** The already-audited comprehension/skill-formation study in `software.md` remains relevant, but an immediate quiz score does not determine subsequent repair hours or multiyear competence. This pass adds no unsupported conversion from comprehension scores to wages or productivity.

**Subjective workslop and effort surveys answer a different question.** They can show perceived burden and identify hypotheses. They do not provide matched active-review times, independently accepted outputs, random assignment or a complete failed-attempt denominator. No survey percentage was used here to estimate cancellation of coding gains.

**Minutes are not automatically cash costs.** Salaried time saved may increase throughput, reduce delay, free scarce expert attention, improve wellbeing or be absorbed by another bottleneck. The result depends on what the person could actually do with the released time. Queue waiting is calendar delay, and must not be charged as uninterrupted reviewer labour. Review may also create learning and prevent losses; treating all inspection as waste would omit its benefit.

**A current burden need not be irreducible.** Better specifications, tests, context, reviewer models and escalation interfaces can reduce it. Human review can also fail. The relevant question is the cheapest process achieving the agreed correctness, severity and maintenance contract, including a strong automated baseline—not the amount of human activity for its own sake.

No source here establishes that October-2026 autonomous agents erase all generation gains through review. No source establishes the reverse. Their observation periods are an additional reason to avoid a single current-agent multiplier.

## A measurement contract for an actual cost comparison

Use the **planned task** as the accounting unit. For every task, retain preparation, authoring, failed generations, model/tool/experiment use, review, repair, independent acceptance and a later changed-requirement check. Unfinished attempts remain visible; do not report only successful tasks. Distinguish first-attempt acceptance from acceptance after repair and from eventual abandonment.

Keep three ledgers separate:

1. **Attention:** active minutes by person and activity; interruptions and switching recorded separately; overlapping intervals counted once per person.
2. **Calendar:** start, ready-for-review, first response, accepted/rejected, and later maintenance completion. This exposes queues without pretending they consume continuous labour.
3. **Cash/resources:** actual model/tool/compute charges, failed/cancelled usage, preparation and evaluator spend; uncertain or unpriced components remain unknown rather than zero.

Economic scenarios may assign different values to author and specialist-reviewer attention, but report the raw minutes first. Do not present the resulting labour valuation as an invoice or automatically recoverable saving. Quality must be independently assessed; code change after a comment, a green test suite and an absence of complaints are insufficient by themselves.

A useful endpoint is the resource and human-attention frontier **per independently accepted task at a declared severity threshold**, with timeouts and missing costs retained. Rare severe errors and limited follow-up make an expected-loss calculation especially fragile. Report observed error types and denominators instead of claiming a production loss rate from a tiny sample.

## One discriminating proposed experiment, within the existing hours

**Question:** on a fixed permitted patch bank, does strong native automated review reduce active human verification/repair at the same acceptance standard, or merely replace visible defects with harder-to-find residual errors?

This is one extension of the existing agent-evaluation/oracle path, not an additional parallel portfolio commitment. Preserve its limits: **first 30–50 focused hours**, and **another 90–150 hours only if the probe passes its gates**. Calendar dates do not guarantee those hours. No implementation or participant recruitment is authorized by this report.

### First 30–50 hours: establish whether the comparison can be measured

Allocate roughly 8–12 hours to define one small owned/public-permitted codebase, twelve candidate patches across at least three task families, independent expected behaviour and a severity taxonomy. Include genuinely correct patches, ordinary defects, a plausible but incorrect assumption and at least one change requiring repository context. The task/oracle author must not be counted as an independent blind reviewer of their own planted defects.

Spend 10–15 hours building the **measurement fixture** using existing approved tools: a versioned task/patch/oracle ledger, active-time start/stop protocol, explicit pause/wait states, review findings, repair edits, final artifact hash, and complete resource accounting. Stress-test at least the existing scorer probe's 25–50 purposive cases where relevant. This validates a local evaluator and ledger, not a population reliability rate. The pinned source audit already found native Inspect cost/role accounting; use it where applicable instead of inventing a missing-cost feature.

Use the remaining 12–23 hours for a small feasibility comparison only if independent review and an approved runtime are actually available. Assign **different matched patches** to two arms: (A) ordinary tests/static checks plus human review; (B) a strong repository-aware, execution-capable native reviewer plus human triage and repair. Give both identical tests, task context, total budget and final independent acceptance. Preserve reviewer outputs before human edits. Randomize or counterbalance task families and review order; no person reviews the same patch in both arms. Mask candidate provenance where feasible, while recording whether reviewers inferred it.

No new paid inference or installation is implied. Without an independently available reviewer or approved model runtime, stop at the measurement/oracle fixture and explicitly leave the economic question unmeasured. Replaying published comments may validate the ledger, but cannot establish live review savings.

**Measure:** active reviewer minutes, active repair minutes, true/false findings against hidden truth, severe misses, first-pass/full acceptance, final correctness on changed inputs, calendar latency, and all known model/evaluator/tool resources. Keep unavailable generation costs null if the bank comes from public artifacts. A review-only study cannot then claim end-to-end generation savings.

### Conditional next 90–150 hours: test the actual economic bridge

If the first probe establishes reliable timing and acceptance, allocate approximately 25–40 hours to a larger unseen task bank and stronger conventional/native baselines; 40–65 hours to independent matched review/repair observations; and 25–45 hours to a later requirement change, analysis and reproducibility package. Fit within the approved total, choosing the low ends if access or complexity binds.

Include human-only versus AI-assisted **authoring** only if actual authoring time and generation resources can be measured without re-solving the same task. Otherwise keep the conclusion limited to verification/repair. Capture all failed and abandoned attempts. Freeze the high-precision automated-review policy on a development set; do not tune it on the final holdout. Different authors and reviewers are preferable, but their availability is a prerequisite, not assumed free labour.

**Discriminating outcomes:** if the strong native-review arm maintains independently assessed acceptance while reducing total active attention and resources, the “review is an unavoidable human bottleneck” explanation weakens. If it lowers comment-handling time but increases missed severe defects, later repair or rejected work, the apparent gain fails the contract. If only context-poor review is slow, invest in context/integration rather than a generic human-oversight product.

**Stop or redirect:** oracle and reviewer share hidden answers; review timestamps conflate waiting with activity; the same reviewer sees the same patch twice; failures disappear from the ledger; unknown cost becomes zero; no independent acceptance is available; or the mature baseline already meets the contract. Small pilots should report ranges and task-specific failures, not a statistically precise universal saving or a p95 reliability claim.

## 2031 implication and remaining gap

The defensible expertise target is **designing and validating a cheaper acceptance process**, with enough domain knowledge to recognize a wrong contract or misleading improvement. “Reviewing AI code” alone is not yet demonstrated as a durable career moat: automated reviewers are an active substitute, and observed burdens vary by artifact, context and workflow. Measuring residual severe errors, maintainability and real specialist attention can create a stronger technical contribution than counting review comments.

The unresolved empirical bridge remains narrow and valuable: a recent, independently assessed, all-attempt comparison with observed active review/repair, full resource cost and follow-up maintenance on the same tasks. This pass located components of that design, not a complete estimate. No further broad search or benchmark retry is needed to state that limitation.

## Provenance and validation

Read-only primary pages/PDFs were inspected through the web reader on 20 October; no full source bytes were retained and no source-content checksum is invented. Source dates, observation dates and the historical cutoff are distinguished above. The matrix records missing fields rather than filling them with assumptions. The cited Meta article is CC-BY 4.0; this pass does not assume reuse rights for private telemetry or participant code.

Frozen local inputs at the start of this pass:

- `software.md`: `29e5ef3ac97cbf51fbfc9c1e77d7c2116666d6a241a96a4f45f567f684c82bbc`
- `agent-capability-horizons-round6.md`: `4693f55502fa5fc6fb3aa59bf3ebf8aa88f23fe6daf743b8ddbc6f2f06821009`
- `ai-evaluation-source-audit-round10.md`: `3962d046fda9a3a7db28332b285b11b3e193870292e609b9bb1e6d38d928bebe`
- `preparation-pathways-round8.md`: `9d637f121369b68110fa1f9d1694c8093a8a89080360f9e12c65e4e497a4d8b5`

