# Network systems option: trace data age and delayed control actions

20 October 2026. Draft research option, not a selected career recommendation, mounted category, completed controller project or 2031 hiring forecast. This pass read the source index and saved telecom/edge notes first. They already cover standards, operator deployments, edge placement and broad stale-telemetry xApp experiments. The new focus is narrower: **can an evaluator trace the observation, decision cycle, delayed command and actual network effect without confusing simulated time, host time or stale context?**

This is plausible systems/test software work for a developer willing to learn network architecture and C++ event models. Its value is conditional: mature native tools already solve substantial parts. A useful first result may be a smaller regression test or documentation correction rather than a new product.

## Native counterevidence and exact interfaces

The [NIST ns3-oran repository](https://github.com/usnistgov/ns3-oran) provides an O-RAN-like simulator model. The inspected branch tip is commit `5e60f2d56aeba816d005439429b02dbfcff8ecc1`, dated 26 May 2026; this is a checked source pin, not a claim of a tested dependency pair or equivalence to the [2023 paper](https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=936291).

It already has data/report logging, logic modules, conflict filtering and late-command handling. Therefore “add timeouts to a RIC” is an inadequate project pitch. The following bounded source observations give a real baseline:

| Interface | Observed behavior | Evaluation consequence |
| --- | --- | --- |
| [`OranNearRtRic::NotifyLmFinished`, `QueryLms`, `ProcessLmQueryCommands`](https://github.com/usnistgov/ns3-oran/blob/5e60f2d56aeba816d005439429b02dbfcff8ecc1/model/oran-near-rt-ric.cc) | Cycle matching, configured DROP/SAVE treatment, cancellation when an earlier logic run remains active, and conflict filtering before forwarding commands. | Preserve these native policies. A saved/forwarded command and a useful action are different events; no defect is inferred merely because late handling is configurable. |
| [`OranLm::Run` / `FinishRun`](https://github.com/usnistgov/ns3-oran/blob/5e60f2d56aeba816d005439429b02dbfcff8ecc1/model/oran-lm.cc) | The logic produces commands, then a scheduled completion uses `ProcessingDelayRv`. | This is an injected delay in simulator time. It does not measure actual inference, OS scheduling or socket latency. |
| [`OranReport`](https://github.com/usnistgov/ns3-oran/blob/5e60f2d56aeba816d005439429b02dbfcff8ecc1/model/oran-report.h) | Reports expose reporter identity and generation time. | Arrival time alone is not the only available timestamp. An auditor should first use existing data correctly. |
| [Processing-delay example](https://github.com/usnistgov/ns3-oran/blob/5e60f2d56aeba816d005439429b02dbfcff8ecc1/examples/oran-lte-2-lte-distance-handover-lm-processing-delay-example.cc) | Two LTE base stations, one moving UE, round-robin scheduling and a distance-based logic baseline; defaults include a five-second query interval and a 10 ms maximum logic wait. | These are separate knobs for a pedagogical scenario. The model’s name does not make the default an observed real-world near-RT SLA. |

The [pinned README](https://github.com/usnistgov/ns3-oran/blob/5e60f2d56aeba816d005439429b02dbfcff8ecc1/README.md) describes the project as feature complete with best-effort maintenance. Its minimum dependencies are ns-3.42 and SQLite 3.7.17; optional ML libraries are unnecessary for this baseline. Do not silently combine the earlier 5G-LENA/ns-3.48 stack, old srsRAN instructions or current OCUDU/OAI releases with this exact model and call them a compatible tested environment. It models LTE handover and virtual O-RAN-like interactions; it is not a full E2 wire/conformance or physical-radio implementation.

## A recent result makes the boundary concrete

[Obiuwevwi et al., arXiv 2607.01583v1, 2 July 2026](https://arxiv.org/html/2607.01583v1) report small C-exported classifiers inside OAI/FlexRIC. Positive evidence supports inline-inference feasibility. The study uses a synthetic classification problem and a single-workstation RFsim stack. Its methods distinguish classification output from actuation; live control actions remain future work. Projected loop timing and rare service spikes must not become a universal response bound. A random split of generated labels does not establish unseen network-fault generalization.

The paper is CC BY-NC-SA 4.0. Exact repository, dataset, weights, grants and stack commits for its claimed RIC Workbench release were not bound in this pass; this is an access/version gap, not evidence that no release exists. It is useful methods evidence, not the starting runtime for this option.

## One tractable contract

For one control decision, retain separate identifiers and timestamps for observation generation, receipt, decision/query cycle, logic completion, dispatch, and observed application/failure/cancellation. Also retain entity/registration epoch and the configuration/context that made the action meaningful. These are proposed audit fields, not a claim that every real E2 service model supplies them in this form.

Two simple quantities expose distinct errors:

- Logic turnaround = logic completion minus query start, within one identified controller clock.
- Observation age at effect = observed effect time minus the observation’s capture/generation time, only when the clocks are comparable.

For a deliberately synthetic contract with a 10 ms logic allowance and a 20 ms data-age allowance, a report generated at 0 ms, queried at 10 ms, finished at 16 ms and applied at 25 ms has a fast 6 ms logic turnaround but stale 25 ms information at effect. That is contract arithmetic, not an observed RAN failure. A dispatch without an effect trace remains unknown. Reused node IDs, changed context or uncalibrated cross-host clocks can make an apparently fast trace unusable.

If clock mappings are uncertain, carry interval bounds rather than subtracting unrelated monotonic counters. A deadline can be accepted only when the whole permitted time interval satisfies it; ambiguous cases remain unknown. At exactly equal simulator event times, bind native scheduling/order semantics before claiming the source-contract checker reproduces DROP/SAVE behavior. No such native equivalence was executed here.

The companion fixture contains ten exposed, same-author cases, including timely, fast-but-stale, late, missing-effect, changed-epoch/context, unknown-clock, exact-deadline, just-late and observation-not-yet-available examples. They do not constitute independent heldout data, a controller benchmark or a standards conformance suite.

## The 30-day and 90-day path

**First 30 days: 16–24 focused hours assumed, including a 4–6h launch/diagnostic subcap.** These are conditional estimates for an existing developer, not a complete networking foundation. Read the pinned interfaces, map one report-to-command flow, and write a clock/entity/cycle schema. Audit the ten tiny JSON cases manually or with the existing approved standard library. Show which durations/outcomes are computable and which remain unknown. Compare against native behavior and logging before adding a custom rule. No new software, radio, paid cloud or training data is needed for this stage.

The result should be a source/version/unit manifest, an independently reviewable oracle specification and a precise missing trace or regression requirement. A later fresh task must be set and checked separately; exposed study cases do not prove retained skill. A weak diagnostic can identify a preparation gap without falsifying the opportunity.

**Conditional days 31–90: 40–70 additional hours assumed, including setup, only after native-runtime/install approval and rights/version checks.** Start with the unmodified pinned processing-delay example. Bind actual effect/handover observations and native event ordering. Then compare existing deterministic logic and DROP/SAVE under matched scenario/load, paired runs and declared seeds. Add a freshness/context rule only if a distinct missing requirement survives the native comparison. A model is optional and must beat the appropriate existing rule; no training is needed for the proposed first regression.

Reserve an untouched delay distribution/reporting interval and complete run before tuning. This does not claim an unseen physical site, radio or mobility generalization. Retain every query, canceled/late/dropped command, failed/unknown effect and runtime/logging cost. Use network utility only if an independently meaningful effect/outcome is actually observed. Freeze a two-CPU-hour and 50 MB log stop cap; these are proposed resource limits, not measured feasibility. If setup or runs exceed the selected budget, report incomplete/unknown rather than hiding failed attempts. The combined optional estimate is 56–94h if both phases are selected, not an added mandatory curriculum.

Stop or narrow if native logging/tests already answer the question, the required effect or clock mapping cannot be bound, the baseline removes the supposed benefit, the result depends on a favorable seed, or necessary testbed/operator/buyer access is unavailable. Fixed logs may test an observer; they cannot establish the value of a new control action without an environment/counterfactual model.

## People, funding and employment reality

[JOINER at Bristol’s Smart Internet Lab](https://www.bristol.ac.uk/research/groups/smart/projects/joiner/) is a real network-automation/telco-cloud experimentation setting. The [22 October 2025 university account](https://www.bristol.ac.uk/news/2025/october/joiner-project-ai-award.html) identifies UKRI/EPSRC and DSIT funding. That supports a funded-team route, not a software procurement award, open grant, available job or free facility access. Its [official contact page](https://joiner.org.uk/contact/) is a future public professional channel; no form was submitted. The account names Madevo and Weaver Labs as separate industry examples. Their exact products, teams and vacancies were not audited here.

The NIST project directs bugs to its [public issue channel](https://github.com/usnistgov/ns3-oran/issues); [Evan Black’s official profile](https://www.nist.gov/people/evan-black) identifies the relevant group and research. Best-effort maintenance makes reviewer bandwidth a constraint. A native-reproducible trace/test/documentation correction is a practical contribution target; acceptance, employment, equipment access and supervision are not guaranteed.

Candidate role families are network simulation, protocol test/assurance, telemetry systems and RIC integration engineering. They require Linux/networking, C++ event models, SQL/time/identity reasoning, and enough RAN architecture to define the interface. A public CPU-only contract exercise does not require becoming an RF researcher. Research posts, hardware/PHY/control roles and onsite testbeds may demand different degrees, experience or permissions; no new current advert or India-remote/UK work-right eligibility is established by this source set. Earlier Ericsson/Canonical samples remain dated examples in the telecom note, not a fresh hiring census. A 6G standards date supplies no 2031 job-growth estimate.

A credible buyer workflow would need an assurance owner to name a costly reproduction/trace ambiguity, supply permitted representative logs or a test environment, specify the native comparator, and judge whether the regression prevents actual investigation or integration work. No buyer interview or budget for this exact component has been secured. If the need is already bundled in the vendor/lab toolchain, use that tool or contribute a small fix rather than assume a startup market.

## Rights, physical barriers and retained evidence

The [NIST component notice](https://github.com/usnistgov/ns3-oran/blob/5e60f2d56aeba816d005439429b02dbfcff8ecc1/LICENSE.md) permits copying/modification with its full notice, attribution and marked changes; dependency terms remain separate. The [ns-3.42 contribution guide](https://www.nsnam.org/docs/release/3.42/contributing/ns-3-contributing.pdf) sets GPLv2-compatible code and CC-BY-SA documentation rules. [SQLite’s deliverable code/documentation dedication](https://www.sqlite.org/copyright.html) is separate from some build scripts. An assembled native environment still needs an exact component manifest; the first phase uses only self-authored synthetic values.

A later physical claim needs authorized RF equipment and operating/testbed access, actual E2 service/action support, measured propagation/interference/mobility, calibrated clock/timestamp uncertainty and specialist review. None is supplied by a simulator success or an RFsim application running on one host.

Retained evidence includes ten bounded primary source slices with immutable commit/blob identities and separate slice-text hashes; no slice hash is presented as the complete source file hash. No upstream code, native simulator, ML model, private network, radio or device ran. No software/model/data archive was downloaded or installed, no accounts/private systems were used, and no outreach or shared catalogue/tree mutation occurred. The record/fixture checks are author bookkeeping and synthetic arithmetic only; independent source/meaning review and actual project launch remain separate gates.
