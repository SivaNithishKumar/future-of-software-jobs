# Software maintenance after initial AI completion: a bounded primary-methods audit

Prepared 20 October 2026; historical publication cutoff 19 October 2026. Author `/root/labor_market`. This is source inspection and a proposed report refinement, not a reproduced benchmark or executed maintenance study.

The new evidence is **CodeThread**, a controlled two-step **agent** experiment. It asks whether a downstream agent resolves the same issue on two different starting implementations. It adds a useful contrast after initial implementation, while leaving the human repair-time and production-lifecycle bridge open. There is no basis here to assume AI-assisted software is uniformly worse, or to infer a future human-review moat.

## Census and bounded selection

I first read the saved Cui/METR/Trio/DORA summaries, the TCS denominator review, and the existing maintenance audit. `human-verification-economics-round8.md` already covers Echoes of AI’s later-human-maintenance experiment, RevMate, Meta’s landed-diff/outage analysis and the opposing automated-review mechanism. `software.md` already covers SlopCodeBench. Those are not new independent findings in this pass. Exact CodeThread/title/arXiv strings were absent from the inspected source-index snapshot.

Six targeted discovery queries led to one distinct study. Only three new primary URLs were opened: the exact v1 paper, the authors’ repository landing/README and companion dataset README. Other leads were not fully audited or substituted for the question. A quality-gate lead carried a January2027 issue label without an established eligible version; it was excluded. No broad survey/news conclusion was used.

## Exact study and measured outcome

[Patel, Hou, Purohit, Xu, Pan, He and Chen, *Is Agent Code Less Maintainable Than Human Code?*, arXiv:2606.21804v1, 19 June 2026](https://arxiv.org/html/2606.21804v1), §§3–6 and Appendices B–D. Affiliations printed: NYU and CMU. The dated v1 is within cutoff; this pass does not establish the latest version or actual experiment dates.

The compact study facts and all source locators are in the JSON. There are **no recruited follow-on human participants**. A function-stubbing/restoration stage generates an agent-base implementation; the comparator is historical human code. The same downstream agent then attempts the original benchmark issue. Initial test gates and model intersections select the analyzed cases. One run per model/condition/task uses stated 250-step/$3 caps and high reasoning effort. Passing the original tests is the primary outcome. This is sequential benchmark evidence, without a calendar follow-up, human repair clock, deployment exposure or customer outcome.

The main shared-subset table has 12 negative, 3 positive and 1 tied agent-base contrasts. Its largest reported loss is 13.1 percentage points; that scope must stay attached. Initial failures, useful incidental early fixes and stage selection cannot disappear from a whole-workflow utility account. No interval for the main paired gaps or repeated-seed stability is established in the paper. The human baseline is existing code/gold fixes, not contemporaneously randomized maintainers given identical synthetic briefs.

## Denominators and reproducibility boundaries

[The dataset README](https://huggingface.co/datasets/shaswat123/CodeThread/blob/main/README.md) reports 441/641/171/124 instances across its four named splits, totaling 1,377; it describes stub patches and prompts, not a verified all-run result ledger. Its card/schema and the paper’s Table 1 agree at that constructed-task level. They do not supply every model’s eligible downstream denominator.

The JSON separately preserves starting/function-edit counts, per-model conditional counts, shared task-type counts, discordant regression cases and judged attribution cohorts. Authored addition finds 2,560 Appendix A1 model-task cells versus 2,517 reported judge records; the 43-record link is unresolved. Section 6’s 1,409 wording also remains unreconciled with Table 1/card 1,377. These are bounded metadata/coverage gaps, **not proof of a false result**. Different units such as 406 shared tasks and 405 selected regression cases are not automatically contradictory.

[The official repository README](https://github.com/shaswatpatel123/CodeThread) exposes wrapper/environment and metric-toolchain requirements. It calls the harness a vendored mini-swe-agent, while the paper names SWE-Agent; the actual experimental commit/config must resolve that identity before replication. It warns that unavailable non-Python metric binaries can fall back to narrower coverage. No upstream code, results, containers or data rows were acquired or executed here.

The paper prints CC BY 4.0. The README attributes the upstream harness as MIT; that does not establish a blanket CodeThread, benchmark, container or dataset grant. The inspected data card displays no reuse licence. These are unresolved grants, not a claim that licences do not exist. Mutable landings were read 20 October; no full immutable experimental commit, publisher-byte hash or historical main-branch state at 19 October was established. Paper/code/card are one dependent author family, not three replications.

## What the comparison means—and what could reverse it

The controlled starting-code intervention is stronger than correlating AI use with churn. It also bundles whatever behavior and information differ between the two implementations. Passing a selected initial suite does not prove equal observable behavior. The original follow-on issue and test oracle may rely on the original implementation’s implicit contract; a generated restoration brief may preserve some assumptions and omit others. A conditional downstream difference therefore measures compatibility under this task/oracle/agent policy. It does not isolate an intrinsic authorship penalty for every future maintainer.

Selection matters twice. Restricting to initially acceptable restorations omits failed generation cost. Requiring the later issue to remain unfixed omits possibly useful early work. Both can be reasonable for a clean two-step contrast while making it unsuitable for an all-attempt economic claim. Cross-model gating to reduce cost adds another population restriction. Do not transport a selected resolve-rate gap to defect prevalence, developer hours or wages.

The mechanism analysis is weaker than the controlled outcome contrast. It uses selected disagreements, post-edit features and LLM labels. A fitted association or judged trace is not a randomized intervention on validation/error behavior. The attributed 54/262 cohort is specifically selected, rather than all generated code. An extra validation check or different exception can be a legitimate improvement if the actual contract permits it. A causal per-extra-line failure multiplier is not established. Lack of significance for several static metrics does not show that linters or complexity analysis are useless.

The strongest responsible practical inference is to preserve **observable contract compatibility and later change outcomes** alongside initial acceptance. This inference would weaken if repeated all-attempt matched runs remove the gap; a newer competent native policy wins; expert adjudication overturns the claimed drift; or the test oracle merely preserves accidental historical behavior. A human follow-on cohort could find the two implementations equally easy or favor the agent base. Nothing in this agent-only experiment rules that out. A credible production assignment with linked exposure, incidents and complete support cost would answer a further question that the benchmark cannot.

## One report refinement inside the existing workflow

Target: `labor-economics-round6.project.workflow`, the original `labor-economics-enrichment-round6.json#/records/115`, plus the already authored `workflow-extension-round23.extension.workflow`. I authored the original project; another worker authored extension23 and a different worker reviewed it in21. That review does not accept this new proposal. No source or accepted context is edited.

Keep the **same** synthetic request→evidence→controlled-action artifact. Inside its already planned later-change/support block, record **one** provider-schema/revision change with a frozen new observable contract. Include supported legitimate requests and an unknown/malformed-version case whose correct outcome may be abstention. Preserve tenant/authority, operation identity, retry and effect reconciliation. Do not add another bank, project, month or recruited cohort.

The original personal effort remains **null**. Extension 23 borrows one conditional **additional 90–150-hour** staged allowance; the 20–35-hour later-change block and 20–35-hour reproduction/report block already sit inside it. This refinement adds **zero hours**. Actual availability, approved runtime, first-window completion, independent setter/reviewer and concealed answers are unestablished. If those gates fail, keep a proposed measurement contract or exposed local diagnostic; do not label it independent blind proof.

Freeze planned-change and case IDs before attempts, plus base/final hashes, schema/policy/oracle versions, assistance policy and reviewer exposure. Retain every failed initial gate, retry, repair, timeout, abandonment, useful incidental resolution and unsupported outcome. Report all planned eligible changes separately from the selected initially accepted cohort and later accepted outcomes. Preserve pre-repair traces; an abandoned initial attempt still consumes resources.

Separate active author/diagnosis/review/repair minutes from calendar waiting and actual tool/runtime charges. Count overlapping human time once; unknown cost stays null. Report first-pass versus eventual acceptance, actual later regression/repair burden, legitimate completion, false rejection and critical false acceptance. A second task executed in the same session is sequential evidence; a genuinely later observation supplies only its actual elapsed window. No months of support or production reliability exist merely because a report has a day 90 heading.

Use the competent deterministic transaction/idempotency/reconciliation baseline and the properly configured mature native workflow/policy/database route if actually authorized and provisioned. An imitated or documentation-only native path remains labelled as such. At most one warranted custom improvement continues. A model arm is optional. A native baseline that meets the contract more simply is a valid stopping result; do not manufacture its failure or weaken its legitimate utility.

No same-person re-solving of exposed hidden tasks should masquerade as randomization. Without independent assignment/acceptance, report a traceable within-artifact case study. Imprecision alone is not failure. Reject an apparent improvement that removes failed attempts, omits review, lowers acceptance or counts unavailable native execution as a loss. An inspectable change/repair report may demonstrate diagnosis and measurement, while actual deployment, funded demand, role eligibility and sustained accountable ownership remain separate gates.

## Validation and remaining bridge

The JSON retains exact URLs/version scopes, local raw/canonical pins, source dependence, denominator arithmetic, falsifiers and execution/access gaps. Only authored standard-library arithmetic and document guards ran. No repository/data/model acquisition, upstream runtime, human experiment, private work access, account action, install, contact, UI/source edit or gated freshness execution occurred. Plan repair 30 and register 29 remain frozen.

The unresolved bridge is still an all-attempt, contemporary assistance comparison with independently assessed acceptance, observed active human review/repair, complete resources and actual later maintenance on the same artifacts. This pass contributes a narrower controlled agent contrast and a way to report the missing quantities honestly; it does not claim a global absence of relevant research.
