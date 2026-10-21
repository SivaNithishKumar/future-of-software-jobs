# AI / ML enrichment — unresolved checks and merge guidance

Checked 19 October 2026. Companion to `ai-ml-enrichment-round5.json`; ongoing research, not a final acceptance or forecast. The JSON is a separate catalogue and does not modify `taxonomy-draft.json`, `domain-institutions-round2.json` or frozen reports.

The enrichment contains **154 records**: 23 institutions, 23 official professional channels, 9 teams, 6 researchers, 29 papers, 17 code artefacts, 5 data candidates, 32 claims and 10 proposed projects. These counts describe the curated directory, not market size, confirmed open roles, independent replications or an exhaustive global census. Some paper labels deliberately remain descriptive/short titles; their exact identifiers and title-status fields prevent treating those as fully reconciled bibliography.

## Provenance and validation

The pass read the taxonomy, existing institution JSON and `CATALOG_SCHEMA.md`; it curated `software.md`, `ai-labs-companies-round2.md`, `ml-round3-learning-inference.md`, `actionability-review-round4.md` and `methods-review-round4-hardware.md`. Source-note SHA-256 values are saved in the JSON. Existing files were not edited.

Only one class of source revisit was undertaken: **bibliographic reconciliation**, to obtain exact titles/version dates and distinguish the audited methods version from later metadata. Exact arXiv metadata was opened for 2408.03314v1, 2507.14417v2, 2504.13837v5, 2506.02355v2, 2604.15149v1, 2502.08606v2, 2604.03616v1, 2606.09410v1, 2404.01413v2, 2506.10943v2, 2512.24695v1, 2507.16806v2 and 2609.32470v1. No new performance conclusion was promoted from an abstract. Earlier full-methods findings and review corrections remain attributed to their saved notes.

Validation passed using the saved standard-library builder/validator `build-ai-ml-enrichment-round5.py`:

- JSON parses; all 154 record IDs are unique; none collide with the inspected existing domain directory.
- All **306 internal typed references** resolve to the expected record kind.
- All **405 technical/foundation node references** exist in the taxonomy snapshot.
- Required common fields exist; 194 primary-reference occurrences have HTTPS URL shape. This is not a global link-health or source-content recheck.
- All project records are proposed/not launched and contain launch, hours, resource and oracle gates. All 2031 hypotheses have counterarguments and falsifiers.
- The source-file hashes were unchanged at the validation check. This confirms the builder did not mutate them; it does not freeze future root edits.

No model/data package was downloaded, software installed, benchmark executed, compute entitlement tested, role applied for, researcher contacted or external system changed.

## Highest-priority gaps before a project starts

| Affected IDs | Missing primary check | Consequence / allowed narrow result |
|---|---|---|
| `project.multilingual`, `data.indictrans-eval`, `data.vaani` | Exact permitted files/version, task labels beyond transcription, reviewer-supported languages, blinded 20-case label pilot and annotation-hours estimate | Limit to one task and one or two supported languages. Without valid labels/reviewer, measure tooling/scorer consistency rather than multilingual accuracy or business savings. |
| `project.serving`, `code.vllm`, `code.sglang`, `code.kleidiai` | Existing supported hardware/runtime/model, exact commits, dependencies and per-file licences; workload/arrival process and independent output truth | CPU profiling is an accessible fallback but does not prove CUDA or multi-node competence. Include scheduled-arrival latency, queueing, failures and correct outputs in the denominator. |
| `project.evaluation`, `code.harness`, `code.inspect` | One exact task/result and independently written correct/incorrect cases; final untouched source families and scorer error audit | 25–50 cases establish a scorer stress test, not representative population reliability. A useful negative result is acceptable. |
| `project.routing-calibration`, `data.rlcr-outputs`, `code.calibsft` | Exact released output/checkpoint/data revisions, labels and base-model terms; no-training baseline; calibration/test independence and full rollout cost | Recompute available metrics before any RL run. Low ECE alone can hide no error discrimination. Fallback/review costs cannot be assumed zero. |
| `project.embodied-data`, `paper.smolvla`, `paper.lerobot` | One permitted complete episode fixture with timestamp/state/action/units, decoder versions and any model/data restrictions | Data/format/simulation evidence is useful; physical transfer, online recovery or avoided operator labor remain unproved. Robotics track owns deeper physical constraints. |
| `project.search-verifier`, `code.alphaevolve-results` | Exact tractable result/commit, verifier assumptions, independently valid/invalid candidates and full bounded run cost | Apache-2.0 result artefacts are not the complete internal system. A verifier reproduction or independent small search extension is a precise claim. |
| `project.adaptive-compute` | Approved model/output access, independent fresh generator correctness, real selector and full controller/formatting cost | Oracle pass@k is an upper bound. Do not inherit R01's excluded 2,048-sample difficulty-estimation cost as a free controller. |
| `project.reward-oracle` | A transparent rule world with a checker that rejects shortcuts and accepts equivalent valid rules | Stop before expensive training if the checker fails. Teacher guidance and verifier calls belong in the budget. |
| `project.memory-adaptation` | Truly new random facts/corrections, strong retrieval/context baselines, retained-tail oracle and permitted small update resources | CPU mechanism reproduction can start without claiming HOPE/SEAL replication. Weight updates may lose on quality, retention or full cost. |
| `project.productivity` | Eligible task set, independent acceptance, counterbalanced familiarity, incomplete/review accounting and delayed transfer checks | Personal diagnostic only. Do not interpret it as a general causal productivity estimate or 2031 hiring forecast. |

IDs in this table abbreviate the JSON prefix `ai-ml-round5.`. Every project assumes approximately 8–12 focused hours/week and sufficient relevant foundations; proposed 30/90-day totals are planning ranges. The first 4–6 focused hours should establish a fixture, baseline and oracle or trigger scope reduction. No future execution, installation, paid compute or external action is authorised by these records.

## Methods and rights reconciliations still open

1. **R01 and R02 final methods:** reconcile the ICLR version of R01 with audited arXiv v1 and TMLR/final v2 of R02 with audited v1. Metadata/venue recognition does not establish that splits, budgets or caveats are unchanged. Primary links are in the corresponding paper records.
2. **R07 final version:** compare ICML/PMLR/v2 against the detailed v1 audit before using fitted coefficients or budgeting an exact distillation campaign. Full study checkpoints/data/hardware remain unverified.
3. **R08 scoring:** inspect the discrepancy between paper scoring prose and the repository's Qwen3-32B judge description. Prefer independent labels and extraction tests; preserve `r08-counter` as a countercase rather than choosing the preferred narrative.
4. **R09 correction:** inspect the linked March 2025 Nature correction and exact public experiment release/rights. No corrected-result replication has been accepted here.
5. **R10 tail and compute claims:** exact original code/licence and any final reviewed version remain unresolved. Retaining a corpus bounds a particular linear error; it does not prove every tail is preserved, and TinyStories is itself synthetic.
6. **R11/SEAL:** distinguish the eight-task few-shot experiment, knowledge-incorporation experiment and different reported GPU settings. Audit exact data/weight terms, labels, forgetting and repeated reward-evaluation cost before an exact reproduction.
7. **R12/HOPE:** no complete official artefact/checkpoint/data/resource route was established. Do not replace this unknown with an unofficial implementation while retaining an exact-reproduction label.
8. **R13/R14:** exact data/checkpoint/base-model terms and independent correctness labels remain unverified. R14's reported 8.8 GPU-hour SFT stage excludes 147 GPU-hours of rollout collection; a separate arithmetic and sample-grid audit is still warranted.
9. **Directory bibliography:** IndicTrans2, VAANI, Olmo3, SmolVLA, LeRobot, AlphaEvolve and the historical serving-paper records retain short/descriptive-title or venue/version gaps where flagged. LeRobot's ICLR assertion still needs conference-page reconciliation. Do not silently promote a repository citation to a verified venue record.
10. **Code/data/model permissions:** `code.indictrans` and `code.qwen3` deliberately do not assign a code licence merely from a checkpoint/model-release statement. vLLM/SGLang/KleidiAI code/file rights were not reconciled in the saved directory and remain null. All code records need immutable commits and complete dependency/third-party manifests before implementation. Paper licence and repository licence do not license every model or input datum.
11. **MLPerf review:** pin formal v6.1 rules/code per selected submission and inspect accuracy/compliance/power boundaries before using scores. The independent review's pinned policy is not asserted to be every submission's official frozen rules. Open/Closed, cached-response performance and separate accuracy cannot be merged into a universal live-service rank.

## Institutional and contact access gaps

The six researcher records deliberately have `officialInstitutionalProfileUrl: null`. They are linked through inspected official group/institutional sources; individual profiles/current roles were not separately verified. These are professional discovery pointers, not outreach targets, endorsement or supervision/compute availability. No inferred private email or unrelated personal information was collected.

- **BOLD/SOFAIR:** exact live adverts, fellowship/studentship deadlines, degree requirements, fees, international funding, visa and supervisor access. Shared programme award and planned cohorts do not establish unfilled funded places.
- **MSR:** India Research Fellows 2026 window is past and excludes PhD students/graduates; the separate research fellowship requires active PhD enrollment for students. Avoid merging the schemes into an unaffiliated-developer grant.
- **Sarvam/BharatGen:** reconcile exact role location and eligibility; externally corroborate customer outcomes and research/model artefacts. BharatGen's functional public-programme category is not a verified legal/grant classification. Senior requirements remain senior.
- **AISI:** recheck current technical research vacancies and role-specific security/residency conditions. Closed grant programmes remain closed in this snapshot; general visa wording is not an accepted offer.
- **Mistral/Hugging Face/Baseten:** dynamic/inaccessible or unspecified job surfaces leave exact roles, degree, visa and India/UK access unknown.
- **IndiaAI/AIRR:** validate applicant category/project eligibility, required documents, budget, queue and actual delivered access only during a separately authorised application. Policy investment and a portal are not personal allocation.
- **All institutions:** current mastery, degree, work authorisation, location constraints, research time and compute were not assessed for the reader. No current ad or repository establishes future hiring volume. Community membership/public contribution is not a paid placement.

## Merge boundaries for the root

Use stable references to connect institutions, papers, code/data and projects; do not copy an institution once per branch. Root should normalize organisation identities across tracks before final delivery. The directory's `industriallab`/`publiclab` types are functional catalogue categories with legal-form uncertainties explicitly retained.

Keep `claimType` distinctions intact: primary-study outcomes, company observations/disclosures, access-policy descriptions, proposed experiments and 2031 hypotheses. The JSON contains no ranked career recommendation, permanent human advantage or demand estimate. A hypothesis becomes stronger only if a later bounded experiment survives the specified counterarguments and economics; a polished tree alone does not accept it.
