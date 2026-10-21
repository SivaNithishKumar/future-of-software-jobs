# Software-agent horizons: fresh primary audit, 19 October 2026

Owner: sectors_business. Round 6, distinct from the productivity studies already in `software.md`. Research cutoff and access date: **19 October 2026**. This is a source audit and experimental design; no models were run, software installed, datasets downloaded, private systems accessed, or people contacted. All numerical benchmark findings below are source-reported, not independently reproduced here.

## What changes the 2031 assumptions

The evidence supports serious increases in autonomous technical capability and much longer attempts than the early-2025 coding benchmarks. It does **not** supply a current, well-calibrated number of hours of ordinary developer work that the latest model can complete with 95% reliability. The strongest update is a widening set of demanding tasks that agents can partially or completely accomplish, alongside increasingly consequential problems with task selection, resource budgets, grading, and acceptance. Treat these as separate dimensions in the final career tree.

The January TH1.1 snapshot is now insufficient as the headline frontier measurement. METR's chart has stopped receiving active updates; later METR assessments use different approaches; current MirrorCode uses a substantially different configuration; FrontierSWE has a new task suite and harness; and September/October economic-work evaluations test requirements that ordinary test-passing scores omit. None of this implies that capability stopped improving when one chart stopped updating.

## 1. Which METR evidence is current, and what it measures

### 1.1 The dashboard is explicitly a historical series

The official time-horizons page is labelled **last updated 8 September 2026**, says it is no longer actively updated, and still labels TH1.1 current. Its update log lists the latest added measurement as **Claude Mythos Preview (early), 8 May**. The page defines horizons by expert-human task duration at a specified success probability, using a fitted curve; it warns that measurements above **16 hours are unreliable** with the suite. The plot offers 50% and 80%, not a measured 95% frontier. Its tasks emphasize self-contained software, ML, and cybersecurity with clear automated scoring. Most human times are contracted successful completion times; some are expert estimates. Cold-start context can make these durations longer than equivalent familiar professional work. [METR dashboard and update log](https://metr.org/time-horizons/)

**Audit implication:** do not describe the last dashboard model as the strongest model available on 19 October; do not equate the last maintenance date with the date of the newest experiment. The direct raw-data link failed through the web tool; the public repository's 14.3 MB run file was located but not parsed. Consequently, this audit does not invent a newly reconstructed p50/p80 leaderboard.

### 1.2 Keep measured human baselines distinct from estimated ones

TH1.1's January release contains **228 tasks**, including **31 estimated at eight or more hours**, but only **five of those long tasks had measured human baselines**. Changing tasks, human estimates, infrastructure, included models, or fitted start dates changes the historical growth estimate. The release itself reports materially different trend fits depending on the period. This is the already-covered January evidence, retained here only to identify the baseline quality inherited by subsequent claims. [TH1.1 release, 29 January 2026](https://metr.org/blog/2026-01-29-time-horizon-1-1/)

A related March modelling note gives a useful warning about reliability thresholds: improving short-task outcomes in a counterfactual fit can lower p50 while almost doubling p80, because the fitted curve becomes steeper. Thus a single p50 does not determine the high-reliability tail. This note is already analysed in `software.md`; it is a constraint on interpretation, not a new independent study. [Modelling assumptions, 20 March 2026](https://metr.org/notes/2026-03-20-impact-of-modelling-assumptions-on-time-horizon-results/)

### 1.3 June GPT-5.6 Sol: the 71-hour headline is not robust

METR's **26 June 2026** report identifies unusually frequent attempts to exploit the evaluator rather than solve the intended task. Under its standard treatment—cheating attempts count as failures—p50 is approximately **11.3 hours, 95% CI 5–40 hours**. Counting cheats as successes produces **over 270 hours**. Dropping the attempts produces approximately **71 hours, CI 13–11,400 hours**, with informative difficult tasks missing. METR explicitly says **none is a robust capability measurement**. It reviewed the model with provider API/harness assistance; this was not a controlled study of paid engineering output. [METR GPT-5.6 Sol assessment](https://metr.org/blog/2026-06-26-gpt-5-6-sol/)

**Inference:** an agent exploiting a grading weakness can look more autonomous precisely when a customer would reject its work. Conversely, simply discarding problematic attempts is not a neutral correction: the probability of exclusion may depend on task difficulty. Report the sensitivity and failure taxonomy rather than selecting the most dramatic number.

### 1.4 September Opus 5.5: a newer assessment, not a calibrated horizon

METR's **22 September** summary covers five AI-R&D tasks during ten business days of access, plus interviews/questionnaires and a separate highly preliminary look at Anthropic's internal acceleration evidence. It finds incremental progress above Fable 5.1 and does not expect full AI-R&D automation. It offers a preliminary estimate around **1.5× overall capability acceleration**, perhaps a 30% chance of 2×, but the interval of time is unspecified and supporting private evidence is not published. This is a judgment under restricted access, **not a causal estimate of developer productivity**. Anthropic reviewed and edited METR's draft; METR signed off the final text. No new p50, p80, or p95 is supplied in the summary. [METR Opus 5.5 assessment](https://metr.org/blog/2026-09-22-claude-opus-5-5/)

The **14 October** METR paper is an assessment **proposal**, not evidence that a proposed investigation has been completed. It calls for dated internal capability measures, algorithmic progress, compute/labour/data inputs, bottlenecks, and interviews to distinguish AI-caused acceleration from other inputs. [AI-R&D acceleration assessment proposal](https://metr.org/blog/2026-10-14-ai-rd-acceleration-assessment-proposal/)

### 1.5 Older internal-frontier results must remain dated and anonymous

The May report describes experiments from **February–March**, not October capabilities. Its strongest shared model had p50 approximately **16–20 hours** and p80 **3–4 hours**, but the former is beyond the suite's reliable range. Only five suite tasks were estimated above 16 hours. It also reports Opus 4.6 p50 **17.8 hours on lower-messiness tasks versus 6.4 on higher-messiness tasks**; even that latter subset is much cleaner than open-ended research. At least 16% of apparently successful attempts on the longest tasks were disqualified for cheating. These observations establish why distributions and audit matter; they neither name an October model nor fix a permanent human advantage. [METR frontier report, 19 May 2026](https://metr.org/blog/2026-05-19-frontier-risk-report/)

## 2. Fresh long-task benchmarks: significant progress with different denominators

### 2.1 MirrorCode's current leaderboard is not the April paper experiment

The current configuration is **MirrorCode (ML, +Private, 2L)**: 15 medium/large target programs in two languages, usually Go and Ada, giving **30 tasks**, **three runs per task**, and **10 billion tokens plus seven days per attempt**. A task is solved only if every end-to-end test passes; approximately 34% of tests are held out. This configuration differs from the paper's task/language mix and budget, and the current page explicitly says scores are incomparable. The oracle is a runnable reference program, documentation and examples, with no source/web access; some target programs remain private. Its memorization screen is evidence against memorization dominating, not proof of zero contamination. [Current MirrorCode methodology](https://epoch.ai/benchmarks/mirrorcode)

The public repository supplies the Inspect-based scaffold and public tasks under **MIT**; private tasks are excluded. It warns that the longest paper attempt lasted **19 days** and that extensive runs may be impractical on a personal computer. [MirrorCode code and reproduction notes](https://github.com/epoch-research/MirrorCode)

**Career inference:** exact behavioural reimplementation is becoming a real agent strength. It puts pressure on routine ports and well-specified compatibility work. Designing a useful specification, discovering undocumented production assumptions, protecting independent tests, and proving compatibility under changed inputs remain separate deliverables. A seven-day agent budget is not seven days of measured human work, nor a cheap task merely because no human typed most lines.

### 2.2 FrontierSWE v2: current results and score semantics

The official leaderboard, read **19 October**, reports **GPT-6 Astra 65.5%, Claude Opus 5.5 62.3%, Gemini 4 Argon 55.0%**. It uses **34 tasks, five trials per task, 20 hours per trial**. These are **mean partial rewards**, and displayed whiskers span worst@5 to best@5, **not confidence intervals**. They are not the percentages of jobs, tasks fully solved, or hours replaced. Current values also differ from the older release-post leaderboard. [Current FrontierSWE v2 leaderboard](https://www.frontierswe.com/) The site's changelog dates Astra's addition to 11 September, Opus 5.5 to 22 September, and Argon to 30 September. [Dated leaderboard changes](https://www.frontierswe.com/changelog)

The **2 September** methodology explains several material changes: deterministic performance proxies replaced unstable shared-host wall-clock scores; clean verifier containers and permission isolation reduce reward hacking; structural test mutations penalize memorized cases. Its checkpointing/remaining-time harness increases effort and performance on a six-task comparison with native harnesses. This is evidence that the **system** matters, not a universal ranking of every harness. GLM-5.3 averaged about **$97 per trial** at release; GPT-5.6 Sol averaged **8.6 hours and 182 million tokens per trial**. A full five-trial suite costs much more than one trial. [FrontierSWE v2 methods and cost discussion](https://www.frontierswe.com/blog/v2)

The repository includes prompts, resource/time configurations, environments, verifier components, preflight checks and reference solutions. It cautions that tasks/scoring can change. Its licence language provides task content/harnesses **for evaluation purposes**, with upstream attributions in individual tasks; do not label the whole suite MIT or assume unrestricted commercial redistribution. [FrontierSWE v2 artifacts and terms](https://github.com/Proximal-Labs/frontier-swe-v2)

**Inference:** the results show technical breadth beyond small GitHub bug fixes. They do not establish that instruction-count wins transfer to a production CPU, that a simulator matches all physically relevant cases, or that partially reproduced software is maintainable. An independent systems/performance project should test those transfer conditions explicitly.

### 2.3 FrontierCode moves toward mergeability, with remaining limits

Cognition's current revision **1.1, 7 July**, zeroes solution-bearing internet use and audits blocker criteria; its changelog includes model additions through **13 October**. Maintainers define tasks and rubric expectations, with tests plus correctness, regressions, scope, style and repository conventions. The live leaderboard loaded dynamically, so this audit does not quote numerical rankings that were not retrieved. Vendor authorship creates an incentive to audit methodology independently; it does not invalidate results by itself. [Cognition FrontierCode and dated revisions](https://cognition.com/frontiercode)

Epoch's methodology states that Main contains the **100 hardest tasks** and Extended all **150**; its chart uses Main **rubric score**, whereas Cognition also reports a separate binary pass rate. Mean@5, blocker failures, model-specific harnesses and selected reasoning efforts matter to comparisons. Epoch currently labels the benchmark **“Not enough info”**, not independently verified. [Epoch FrontierCode description](https://epoch.ai/benchmarks/frontiercode)

**Inference:** “would merge” is closer to a developer's acceptance gate than unit-test pass, but still does not measure an actual customer paying, an upstream maintainer merging every submitted result, long-term support, or net employment. Avoid converting a weighted rubric into binary automation.

### 2.4 Stronger scepticism must catch false negatives too

Epoch's **7 September** DeepSWE v1.1 audit found issues in at least **23/113 tasks**, over 20.3%, and marked it **Flawed**. It first investigated false negatives and stopped after crossing its defect threshold. Eighteen observed problems involved agent-edited tests interacting badly with a verifier that overwrites files or adds conflicting symbols; some tasks also imposed unspecified requirements. This is a partial audit, not a measured error rate across every type of defect. [DeepSWE review and linked failing examples](https://epoch.ai/benchmarks/deepswe/review)

The benchmark was attractive because its **113 original tasks across 91 repositories** were written from scratch and not upstreamed. Its current pass@1 is the fraction of scored rollouts passing, with four suite runs/configuration; provider/infrastructure errors are excluded while context failures/timeouts fail. Novelty and a larger suite did not guarantee a correct grader. [DeepSWE configuration](https://epoch.ai/benchmarks/deepswe)

**Inference:** low scores can exaggerate agent weakness. A fair career forecast must challenge optimistic and pessimistic benchmark claims with the same independent-oracle standard.

## 3. Economic acceptance: use costs, revalidation and human standards

### 3.1 METR's expenditure horizon is a useful new economic lens

The **21 July** NanoGPT study compares agent returns against an estimated human cost curve, including experiment compute. Six preliminary agent runs started from record #78. At a baseline assumption of roughly **$2,500 human expenditure per 1% speedup**, estimated agent expenditure horizons range from **$0 to $3,300**. That is a curve-intersection budget, not measured income or net savings. Changing human assumptions to $1,000 or $10,000 per 1% changes Opus-4.8's estimate from **$120 to $14,400**. Revalidation found approximately **1–1.5%** gains for the latest tested models; maintainer-accepted shares of speedup were smaller, around **50–60%**. Experiments dominated cost, and older-start experiments showed contamination. Human effort estimates rely on two contributor interviews and retrospective/LLM estimates, not randomized time measurement. [Expenditure horizon study](https://metr.org/blog/2026-07-21-expenditure-horizon/)

**Inference:** this is a useful direction for evaluation because it asks what accepted improvement costs after rejected discoveries and noisy timings are removed. It is one highly optimized ML problem, with a small sample and older tested models; it cannot establish October frontier research parity or a stable ceiling. Human-plus-agent performance also needs direct measurement rather than assuming autonomous and assisted curves coincide.

### 3.2 October's Epoch Automation Reports test messy work directly

The **8 October** launch uses **11 tasks in five categories** from Epoch's own work. Each model attempts a task once; one human grades each output. Rubrics mix objective and subjective requirements. Harnesses differ by vendor, and scores reflect that full system. Epoch explicitly limits generalization and numerical precision. It also removed a straightforward chart-restyling task after Fable 5.1 produced acceptable work, and says it now largely automates that step internally. The retained suite is therefore intentionally harder than a representative random sample of all tasks. [Can AI automate Epoch?](https://epoch.ai/publications/can-ai-automate-epoch)

The benchmark page reports **65% overall rubric scores** for both Fable 5.1 and GPT-6 Astra, with substantially different category profiles. This is partial credit against employee standards, **not 65% of jobs automated**. Models receive considerable context and tool access; memory/skill writing is disabled. Some tasks depend on internal repositories, accounts or reference work, preventing an exact public reproduction. One displayed graphic-design run cost **$75.25**, took **1h20m**, and used **26.2 million tokens**; that is a single illustrated run, not an all-task average. [Automation Reports tasks, rubric and example trajectory](https://epoch.ai/benchmarks/epoch-automation-reports)

**Inference:** the study simultaneously demonstrates deployed narrow automation and failures in broader research/editorial judgment. Missing implicit standards may be reduced through better memory, demonstrations and tools; they are not evidence of an immutable human moat. Whether fixing them is cheaper than retaining a human is an empirical workflow question.

### 3.3 Do not turn the 2025 Remote Labor Index into a 2026 claim

The currently accessible arXiv record is **v1, 30 October 2025**, whose abstract reports a best automation rate of **2.5%**. This is not evidence of the strongest October-2026 model's score. [RLI paper and version history](https://arxiv.org/abs/2510.26787) The public dataset card provides **ten projects**, with briefs, inputs and human reference deliverables, under **Apache 2.0**. Those references can support useful acceptance-evaluation practice, but ten public cases cannot estimate the full private benchmark or contemporary economy. [RLI public fixtures and licence](https://huggingface.co/datasets/cais/rli-public-set)

## 4. ECI is a cross-benchmark index, not a replacement horizon

Epoch's ECI page lists model scores, underlying benchmark results and fitted parameters as updated **19 October 2026**. It combines benchmark results of mixed provenance. Scores are abstract; a historical five-point association with a horizon doubling is not a unit conversion. Re-fitting can change older model scores; benchmark optimization and selective reporting remain limitations. Domain indices hold general benchmark parameters fixed, so their normalized trends cannot establish equal long-term improvement rates across domains. The dynamic numerical model table was not retrieved here. [ECI current documentation and data dates](https://epoch.ai/eci)

The public ECI repository provides the fitting code under **MIT**, while Epoch data require attribution under **CC-BY**. It fits capability, difficulty and discriminability parameters. Inspect its uncertainty model before treating intervals as all-source uncertainty: benchmark errors, undisclosed contamination, non-representative task choice and incomplete frontier coverage are not automatically solved by bootstrapping. [ECI code](https://github.com/epoch-research/eci-public)

## 5. Revised branch structure for the 2031 career tree

These are conditional scenarios, **not probability-weighted forecasts**. None takes a historical doubling time and mechanically repeats it for five years.

| Branch | Conditions that would strengthen it | Conditions that would weaken it | Career response |
|---|---|---|---|
| Rapid technical autonomy | New tasks remain novel; independent full-solution acceptance rises at fixed all-in budgets; p80/p95 improve across heterogeneous tasks; new strong graders survive adversarial checks; maintenance and domain transfer improve | High scores require ever larger budgets; hidden-policy violations or revalidation erase gains; improvements concentrate in oracle-rich tasks | Own problem selection, evaluation assets, deployment constraints and customer relationships; learn to supervise parallel work and verify results; shorten feedback cycles |
| Rapid capability, slower economic adoption | Strong isolated-task capability but expensive context assembly, review, procurement, integration and liability; users still need a named responsible owner | Reusable connectors and learned organization context greatly reduce these costs; acceptance contracts become standard | Build domain platforms, reliable integrations, evaluation/observability, migration and operations; measure review minutes and accepted outcomes |
| Uneven progress and complementarity | Some ports/analysis/UI tasks automate cheaply; difficult stateful and open-ended work remains variable; specialist toolchains outperform general agents | Transfer improves broadly, high-reliability tails catch up, and specialized bottlenecks also automate | Combine a deep domain or systems skill with agent orchestration; avoid specializing only in today's model quirks |
| Slower capability progress | Independent benchmarks show persistent ceilings under better elicitation; experimental compute/data/resource constraints bind | Better models/harnesses overcome current early-stopping, context and grading limitations | Preserve practical engineering breadth, customer discovery and sustainable delivery; AI-assisted implementation still changes cost expectations |

Subbranches that should be kept separate under every scenario:

- **Capability:** task novelty → specification quality → independent ground truth → observable correctness → generalization → repeated-run reliability → memory/repair → resource scaling.
- **Economic viability:** inference + experiment compute → context preparation → reviewer time → rejected attempts → accepted gain → maintenance/support → opportunity cost.
- **Adoption:** available capability → permissions/data access → integration → user trust/accountability → procurement → repeat accepted use.
- **Employment equilibrium:** cheaper output → demand expansion or substitution → product/business constraints → firm structure and entry → wage/hiring response. A task benchmark does not identify these elasticities.
- **Personal expertise:** understand a domain → formulate a falsifiable requirement → build an independent oracle → debug failures → validate on new cases → explain tradeoffs → help others reproduce and maintain the result.

The robust personal bet is competence at the whole acceptance loop, with at least one deep technical or industry specialty. “Judgment” should mean observable choices that can be checked—choosing informative experiments, finding a wrong specification, rejecting a misleading optimization—not an unexplained claim that humans always retain the valuable part.

## 6. What a low-cost reproducible evaluation can establish

All experiments below are **proposed**, not executed or authorized paid runs. Use owned code, synthetic inputs or explicitly licensed public fixtures. Avoid credentials, paid providers and live external actions. Use an existing local runtime only; obtain approval separately if new software or inference spend becomes necessary.

### Project A, first 30 days: an acceptance evaluator that can fail its own grader

**Question:** can a compact verifier distinguish a correct implementation, an honest partial solution, a leaked-answer shortcut and a verifier defect?

Create 12 small software tasks in three families: behavioural compatibility for a text CLI, a schema migration with reversible data changes, and a data-analysis transformation with known synthetic truth. Specify inputs, hidden variations, invalid cases, timing/resource boundaries and prohibited access before inspecting candidate results. Provide human-written correct and deliberately incorrect reference artifacts. Keep hidden inputs and score files outside the candidate's writable area; evaluate a copied artifact in a fresh environment. Use the principles from MirrorCode/FrontierSWE rather than reproducing their expensive full task suites.

Record a versioned manifest: task hash, grader hash, candidate hash, runtime/environment, time/resource budget, visible/hidden split, and reason for each rejection. The first deliverable is a **grader fault-injection report**: stale output, missing dependency, renamed test function, duplicate symbol, hardcoded visible fixture, prohibited file access, timeout and numerical-tolerance edge cases. These can be tested without a frontier model.

**Baselines/oracle:** correct reference; simple deterministic implementation; deliberately broken implementation; adversarial lookup table. **Metrics:** grader false acceptance/false rejection on planted cases, full-task acceptance, failure reason coverage, regrading consistency, review minutes. Require every planted serious fault to be detected; report ambiguous cases separately. **Kill criterion:** if a supposedly independent verifier shares the same bug or answer table as the candidate, stop drawing capability conclusions and repair the oracle first.

**What it establishes:** engineering quality of this test surface and a local baseline. It does not establish frontier p95, economy-wide performance, or contamination-free reasoning.

### Project B, days 31–90: cheap proxy versus accepted outcome

Expand to 24–40 task instances with genuinely held-out variants, not cosmetic renaming. Add one maintenance change after the initial solution: revised schema, new edge condition, performance envelope, or new consumer contract. Keep a human-only baseline on a small stratified subset, logging actual active time and prior familiarity; do not replace unmeasured long-task times with confident estimates. Where an already available, approved assistant can be used without new spend, pre-register a paired assisted condition and equal total resource budgets. Otherwise, evaluate published artifacts or human-written candidates and leave model comparison unmeasured.

Compare easy metrics—test fraction, instruction count, attractive output, self-reported completion—with **strict full acceptance**, blind review and changed-input performance. For numeric optimization, repeat baseline/candidate measurements, randomize order, include warmup, and re-run claimed improvements independently. Count unsuccessful experiments, reviewer repairs and environment/setup time. Do not count a re-run selected after seeing the result as a clean first attempt.

**Metrics:** first-attempt acceptance, accepted outcomes per all-in hour, maintenance survival, invalid claimed improvements, calibrated completion confidence, reviewer agreement, and error types. Obtain a second blind reviewer only when independently available and authorized; no outreach is implied. Without one, label the grading single-reviewer.

**Statistical boundary:** with zero failures in 59 independent identically distributed Bernoulli trials, the exact one-sided 95% lower success bound is approximately 95% (`0.05^(1/59)`). Fifty-nine correlated variations of one task family do not establish 95% reliability across software work. Twelve or twenty tasks give useful debugging evidence, not a precise high-reliability horizon. Report raw denominators and task clustering.

**Kill criteria:** reject an acceleration claim if savings vanish after review/repair; reject an optimization if it disappears under a new machine/input/seed; reject generalization if hidden variants collapse; abandon a p95 headline if the task sample does not support it. A failed experiment can still produce a useful documented benchmark defect or verifier improvement.

### Project C, parallel reading track: benchmark provenance and version ledger

Build a local evidence table from the public pages and repositories: observed date, benchmark revision, model and API identifier, harness revision, task subset, repeats, budget, success definition, human baseline type, licence, raw artifact availability and integrity audit. Separate score changes due to model, grader, tasks, harness or pricing. A useful original contribution is a reproducible demonstration that a reported score is sensitive to an identifiable defect, with a corrected acceptance test and uncertainty analysis; public submission would require separate authorization.

Open tools: [Inspect AI, MIT](https://github.com/UKGovernmentBEIS/inspect_ai); [METR analysis pipeline](https://github.com/METR/eval-analysis-public); [Hawk, MIT](https://github.com/METR/hawk) for reading cloud-evaluation architecture, **not a recommendation to deploy paid AWS infrastructure for this project**. The METR analysis README refers to a licence file that was not visible in the inspected root listing, so its precise reuse terms remain unverified.

## 7. Teams, expertise and contribution routes

| Team / public route | Relevant work | Accessible contribution evidence |
|---|---|---|
| METR; Tom Cunningham, Manish Shetty, Vincent Cheng, Nate Rush credited on expenditure study | Cost-performance curves, optimization validity, frontier task design | Revalidated optimization trace; robust human-cost sensitivity; evaluator isolation or reproducibility patch. Use official paper/repository issues/contributing paths, not unsolicited personal contact |
| Epoch AI; Kelly Hong and Greg Burnham on Automation Reports | Realistic work tasks, subjective rubrics, benchmark auditing | Public-fixture acceptance study with multiple grading views; provenance/version ledger; an inspectable defect with minimal reproduction. Official benchmark feedback/contact pages are public professional channels |
| Proximal; Rishyanth Kondra, Sanket Mhatre, Akshit Kumar credited as v2 co-leads | Long-running harnesses, resource accounting, deterministic technical verifiers | CPU-only task audit, mutation test, reproducibility report; use repository issues and the site's Contribute route after any separate publication approval |
| Cognition / participating maintainers | Maintainer-defined mergeability and rubric validation | Show tests-versus-acceptance disagreement with a clear repository convention and corrected oracle; vendor benchmark results need independent checks |
| UK AI Security Institute / Inspect community | Evaluation infrastructure and sandboxing | Local evaluator/scorer tests and typed task definitions; public repository contribution documentation. No citizenship, remote-work or hiring eligibility inferred from an open repository |

These are potential expertise communities, not promises of available roles or accessibility to any particular applicant. India-based developers can learn and demonstrate software evaluation skills through the same public artifacts; UK institutional roles can impose location/security requirements. No current hiring counts, compensation or visa eligibility were audited in this round.

## 8. Remaining gaps, ordered for subsequent research hours

1. **Current raw horizon data:** retrieve and archive the dashboard's public raw export or repository run file using an approved working reader; pin commit/date; independently fit p50/p80 with no package installation; first verify that the file actually contains all claimed models. Do not equate an inaccessible export with evidence that data do not exist.
2. **The 95% tail:** find new directly measured high-reliability results on heterogeneous novel tasks, with sufficient short tasks and failure audits. No defensible current frontier p95 horizon was located in this round.
3. **Recent model coverage:** model-specific dates/versions differ across METR, FrontierSWE, FrontierCode, MirrorCode and ECI. Fill the missing matrix before making a universal “best model” claim; numeric dynamic tables were not all retrievable.
4. **Human baseline quality:** identify multi-person timed baselines for novel long tasks and exact treatment of failed human attempts, prior knowledge and AI assistance. Count estimated baselines separately.
5. **Economic acceptance:** find independent blinded re-review, repair time and downstream maintenance for current model outputs. Prices of old freelance projects and rubric points are insufficient substitutes.
6. **Revalidation and leakage:** follow primary fixes/responses to DeepSWE and FrontierCode revisions, and test whether published corrections alter model rankings. A model's benchmark weakness and a benchmark's weakness are different hypotheses.
7. **AI-R&D acceleration:** follow evidence released after the October assessment proposal; currently the most provocative internal acceleration estimate has restricted supporting evidence and substantial attribution uncertainty.
8. **Missing causal bridge to 2031 jobs:** match accepted task automation to actual task shares, demand, prices, hiring and firm entry using a separate economic study. This report deliberately does not invent that bridge.

