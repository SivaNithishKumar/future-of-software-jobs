# Capability-data access checkpoint — round 7

Owner: sectors_business. Saved **20 October 2026** after interruption. Research scope remains the **19 October 2026** evidence cutoff. This checkpoint records observations already made; it adds no new model runs, installations, accounts, paid services, private-system access, outreach or external writes. The round 6 report remains frozen.

## Result and boundary

The public METR page rendered successfully in an existing browser and revealed two exact official YAML export URLs that the text-only web reader had not resolved. **No export bytes, download path, parsed record or checksum were returned before the retrieval call was interrupted.** The raw-data gap is therefore narrowed to known endpoints, not closed. No fitted horizon, observed success rate, cost distribution or fresh economic-benchmark table was calculated in round 7.

The parent requested an immediate bounded checkpoint and a stop to network/browser retrieval. No additional retrieval, polling, browser recovery, endpoint retry or download inspection was attempted after that instruction. There was no running shell/model evaluation in this pass. The browser download call was the pending operation; its completion or partial-download state is **unverified**.

## Exact route ledger

| Sequence | Read-only route / action | Observed result | What may be concluded |
|---|---|---|---|
| 1 | Existing CUA runtime: create hidden in-app tab at `https://metr.org/time-horizons/` | In-app browser unavailable | That browser route was unavailable; says nothing about the public endpoint |
| 2 | List enabled browsers | Existing Brave browser profiles were available | An existing public-page reader could be used; no installation or login needed |
| 3 | Select existing Brave browser and create a new tab at the same public METR URL | Page rendered and returned a detailed accessibility tree | Official chart labels, controls, links and FAQ text were directly inspected |
| 4 | Read the two visible Download data link targets | Exact benchmark and task export URLs below | Official page links these resources; their contents/schema were not yet read |
| 5 | `a#download-btn` download operation, followed in the same pending call by the intended task-export download | Tool eventually reported **aborted after 2,993.3 seconds**; no intermediate file-path result reached the agent | First download completion is unverified; the second operation may never have started. No bytes or success should be inferred |
| 6 | Parent recovery instruction | Stop retrieval and save observed evidence | No repeat cycle performed |

The unexpectedly long pending call exceeded its requested timeout in practice. This is an access/tooling interruption, not evidence that METR denies public access or that the YAML files are absent. No CAPTCHA, paywall, security warning or authentication gate was bypassed.

## Newly observed official references

1. [METR public horizon page](https://metr.org/time-horizons/).
2. [Benchmark-level TH1.1 YAML export](https://metr.org/assets/benchmark_results_1_1.yaml), observed on the page's first Download data link (`id="download-btn"`).
3. [Task-level TH1.1 YAML export](https://metr.org/assets/task_results_1_1.yaml), observed beneath the per-task fit/timeline visualization.

**Retrieval provenance:** these URLs and visible page facts were observed in the browser before the 20 October recovery checkpoint. An exact wall-clock timestamp was not captured at observation time, so a precise retrieval date/time must not be invented. The page itself stated **last updated 8 September 2026**. The checkpoint date is known; the raw-export retrieval date is **null because no completed raw retrieval was verified**. The manifest preserves this distinction.

## New visible configuration facts, distinguished from raw data

The chart displayed **TH1.1**, both **50% Success** and **80% Success** controls, and the warning that measurements above **16 hours are unreliable with the current suite**. Its detailed task visualization defaulted to **Claude Mythos Preview (early)**, with a rounded displayed p50 prediction of **17 hr** and a timeline label **7 April 2026**. This is a publisher-displayed fitted value outside the page's stated reliable range; it is **not** a newly supported 17-hour measurement, an observed solve rate or an independent estimate. It is retained only as an interface observation.

The model selector exposed 23 named options, preserved verbatim in the manifest. A menu option proves inclusion in that visualization, not complete frontier coverage, identical run budgets, robust estimates or an October model ranking. Model release dates, evaluation dates and publication dates must remain distinct.

The page's evaluation FAQ described **six independent runs per task**, dev-set elicitation followed by a separate larger test set, review of reward hacks and token sufficiency, and infrastructure/task repairs that can require restarts. This is a description of the stated protocol, **not a count reconstructed from either export**. The raw denominator, exclusions and per-model exceptions remain unknown here. The method text describes contracted human successful completion times and geometric averaging, with expert estimates or QA timings used when reliable human measurements are unavailable. The exported records were not inspected, so no task was classified here as measured versus estimated.

### What is and is not known about schema

- The official filenames distinguish benchmark-level and task-level exports; their extensions are YAML. **No YAML keys, nesting, units, null rules or run records were inspected.** Filenames alone do not establish schema.
- Earlier round 6 inspected the separate public analysis repository README, which describes a JSONL schema containing `task_id`, `task_family`, `alias`, `score_binarized`, `score_cont`, `human_minutes` and `invsqrt_task_weight`. That is **README-described schema from another artifact**, not a verified schema for these YAML exports. [METR analysis repository](https://github.com/METR/eval-analysis-public)
- The relationship among YAML aggregations, the repository JSONL data, task revisions and any current fit remains unverified. No row counts, task hashes or commit hashes can be assigned without the actual artifacts.

## Quantities that cannot be estimated from this checkpoint

| Quantity | Missing evidence | Hard reporting boundary |
|---|---|---|
| Per-model observed acceptance | Task/run records, score definitions, invalid-run handling and task weights | Do not derive it from a fitted horizon, chart position or model menu |
| Fresh p50/p80 leaderboard | Export bytes, exact configuration/version, fitting and uncertainty metadata | No current model ranking or refit supplied |
| p95/p99 horizon | Suitable task support, independent failures, validated grader and high-reliability fit | No percentile invented or converted mechanically from p50 |
| Horizons above 16 hours | Long-task support and method validation beyond the official warning | Do not refit or extrapolate the shown 17-hour value into a claim |
| Human-equivalent duration quality | Per-task measured/estimated flag, participants, successes/failures and timing protocol | Do not label every `human_minutes` value a measured human baseline |
| Cost per accepted result | Inference/experiment costs, rejected attempts, preparation/review/repair and final acceptance | No economic savings or return estimated |
| Partial reward versus full acceptance | Per-trial partial score, strict solve definition, blocker rubric and accepted artifact review | Mean score cannot be relabelled automation rate |
| Maintainer mergeability | Independent maintainer decision and associated repair/support effort | No test-pass-to-merge conversion |
| Model-only effect | Frozen harness, resources, task mix and API versions | No attribution of all changes to the underlying model |

Visible labels and links can establish where to look and which claims need qualification. They do not supply missing numeric observations. No confidence intervals are generated because there is no valid newly retrieved sample to analyse.

## Routes deliberately not taken

No repeated download attempts; no browser installation or extension changes; no login; no paid Browserbase session; no paid inference; no model execution; no private developer endpoints; no hidden application state extraction; no interception of authenticated traffic; no broad download-folder or personal-file search; no guessed endpoint sweep. Earlier round 6's failed terminal DNS route and text-reader raw-link errors are recorded in that report and were not recycled here as new trials.

The compact JSON manifest is a **provenance/status artifact**, not derived benchmark data. Its source-byte hashes are null. A future worker may retrieve the exact observed public URLs using an approved functioning reader, but this checkpoint does not authorize installation, payment, private access or a retry loop.

## Distinct economic measurement question for a later refill

**When a software agent earns partial benchmark credit, how much independent human review and repair is required before its artifact is actually accepted, and does that remaining labour erase the measured cost advantage?**

This is distinct from recovering a horizon export. A bounded research pass could audit public, current primary studies or released trajectories that expose all four denominators: autonomous first-attempt output, strict final acceptance, reviewer/repair time, and total inference plus experiment cost. Compare autonomous, assisted and human-only conditions only where the source actually measures them. Separate maintainer acceptance from rubric prediction, and exclude price-only or self-reported-output studies from a numerical savings estimate. If no study exposes the full bridge, return the missing fields and a proposed measurement design rather than inventing net productivity.

