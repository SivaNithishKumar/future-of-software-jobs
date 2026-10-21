# Software, ML systems and AI agents: research track

Status: working notes from the initial extended research pass, checked 19 October 2026. This is one input to the ongoing 24-hour research programme, not a completed forecast or final mind map. No experiments below have been executed. Public primary sources were read; model campaigns and study analyses were not independently replicated. No packages were installed and no external systems were changed.

## Working conclusion and boundaries

The defensible career bet is to get unusually good at turning model capability into a useful, measurable and dependable outcome in a domain. The evidence supports falling implementation costs and changing work allocation. It does not establish a date when software engineering disappears, a guaranteed number of jobs, or a permanently safe occupation.

For the reader, the known starting point is AI engineering, software development, automation and product building. That makes applied ML systems, agent reliability, workflow integration and inference engineering plausible adjacent paths. Current tenure, mathematics proficiency, research experience and production ownership have not been assessed; the learning paths below use demonstrations of mastery as gates rather than assuming those skills.

Three distinctions must survive the final synthesis:

- Technical ability is different from reliable, permitted, economically useful deployment.
- More code, PRs, tokens or agent runtime is different from more accepted customer value.
- Human responsibility does not guarantee large demand for human labour. Accountability could be concentrated in fewer people, and currently difficult specifications and reviews may themselves become easier to automate.

## Evidence and methods ledger

### S01 — Enterprise coding experiments: what the headline estimates

**Source:** Cui et al., *The Effects of Generative AI on High-Skilled Work: Evidence from Three Field Experiments with Software Developers*. June 2025 author manuscript; online in *Management Science*, 27 February 2026. [Author-hosted manuscript](https://economics.mit.edu/sites/default/files/inline-files/draft_copilot_experiments.pdf), printed pp. 4–12, sections 2–4.2; [published paper](https://pubsonline.informs.org/doi/10.1287/mnsc.2025.00535).

The experiments study mostly 2022–2024 Copilot completion assistance, not present autonomous agents. The observation unit is developer-week; outcomes include completed PRs, commits and builds. Randomized access or rollout timing instruments adoption. The headline **26.08% more PRs, SE 10.3%**, is a precision-pooled weighted instrumental-variable estimate. It is not the raw intention-to-treat effect of distributing licences. The adoption indicator switches on after initial adoption and remains on; weighting favours periods with larger treatment–control adoption differences. Fixed effects and assignment-level clustering address some variation, not every possible interpretation problem. PR scope, hours worked and long-term customer value are not fixed. Company-selected settings and incomplete adoption limit transportability. Less experienced developers had greater adoption and estimated gains.

**Use:** evidence that meaningful gains can occur among induced adopters in enterprise settings, with the estimand stated explicitly.

### S02 — Published supplement: denominators, access effects and excluded evidence

**Source:** [Official online appendix](https://pubsonline.informs.org/doi/suppl/10.1287/mnsc.2025.00535/suppl_file/mnsc.2025.00535.sm1.pdf), Appendix A; B/Table 5; D.1/D.4; E/Table 8.

The final analysis contains **1,521 Microsoft, 316 Accenture and 3,030 anonymous-company developers: 4,867 total**. Exclusions include nondevelopers, departures, missing outcomes and pre-access adopters. Restricted early-window intention-to-treat PR effects are Microsoft **+3.91% (SE 3.83)**, Accenture **+9.41% (9.65)** and pooled **+4.66% (3.56)**, none statistically significant. These use 29 and 21 weeks before substantial control adoption; they must not be contrasted mechanically with the full-period weighted-IV headline as if windows and estimands matched. A separate Accenture experiment, affected by 42% layoffs and incomplete adoption logs, has an uncertain negative PR estimate, **−39.18% (SE 36.78)**. Company-run experiments were not preregistered by the analysts; registration was retrospective. Compilation success is a limited quality measure.

**Use:** adoption, rollout support and study exclusions belong in the account of productivity, not just tool capability.

### S03 — METR's original real-repository randomized experiment

**Source:** [Paper, version 2](https://arxiv.org/html/2507.09089v2), sections 2.1–2.3; Appendices C.2.7, C.3.3–C.3.5, D.1–D.2, E.1 and G.6. [Public research summary, 10 July 2025](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/).

February–June 2025: **16 analyzed developers, 246 completed issues; 136 AI-allowed and 110 disallowed**. Developers generally had over ten years of engineering and five years in their repositories; recruitment favoured active contributors to popular mature projects. Compensation was $150/hour; only 44% previously used Cursor. Issues and difficulty forecasts preceded mostly fair-coin task randomization; 25 early issues used another procedure, with robustness checks. Treatment was permission to use AI. Active implementation time, including normal-review changes, was self-reported and checked against recordings; 27 unfinished-review cases required imputation. Estimated time increased **19%, 95% CI +2% to +39%**. There were 13 uncompleted assigned issues and 24 intentionally dropped issues; sensitivity analyses retained slowdown. Three developers were excluded: two repository pauses and one widespread cheating case. Quality comparability was qualitative and based partly on post-review time, not blinded long-term defect measurement.

**Use:** strong evidence in a narrow setting; neither a universal anti-AI result nor a contemporary frontier-agent estimate.

### S04 — METR's follow-up does not cleanly overturn S03

**Source:** [METR, 24 February 2026](https://metr.org/blog/2026-02-24-uplift-update/), opening estimates, “Wider adoption” and “Details.”

The later experiment included 800-plus tasks, 143 repositories and 57 developers: ten returning and 47 new. New settings included smaller, less mature and greenfield projects; compensation fell to $50/hour. Completion-time estimates were **−18% [−38%, +9%]** for returning developers and **−4% [−15%, +9%]** for newcomers. Both intervals include no effect. Developers declined no-AI work, 30–50% reported withholding some tasks, completion selection differed and concurrent agents complicated time accounting. METR calls the productivity signal unreliable and evidence about the size of improvement very weak. Its intuition that selection suppresses measured benefit depends partly on whether expectations predict actual gain; S03 demonstrates why enthusiasm cannot establish that magnitude by itself.

**Use:** improving capabilities and adoption are plausible, while a clean current causal productivity multiplier remains unsettled.

### S05 — Autonomous task horizons are rising, with a specific meaning

**Source:** [METR TH1.1, 29 January 2026](https://metr.org/blog/2026-01-29-time-horizon-1-1/), task-suite changes, trend comparisons and appendices.

TH1.1 expands the suite from 170 to 228 tasks and long tasks from 14 to 31. Only **five long tasks have measured human baselines**; the rest use estimated durations. The fitted post-2023 50% task-horizon doubling time is **131 days**, compared with roughly seven months on the longer stitched history. This is the human-equivalent task length at which modeled success is 50%, not dependable unattended work for that duration. The distribution targets software/research tasks and changes across suite versions. Scaffold and task selection affect estimates; uncertainty remains wide.

**Use:** prepare for longer delegation. Do not project one exponential mechanically onto entire occupations or claim a precise 2031 capability level.

### S06 — Sensitivity and a correction to horizon modelling

**Source:** [METR research note, 20 March 2026](https://metr.org/notes/2026-03-20-impact-of-modelling-assumptions-on-time-horizon-results/), summary and uncertainty table.

A regularization correction reduced recent 50% horizon estimates by up to 20%. Reasonable alternate fits can lower recent 50% estimates and raise 80% estimates. Task-distribution uncertainty is particularly important; the suite contains only about 230 tasks across a broad duration range and none above 30 hours. Human task-duration noise is another unresolved source of bias. Confidence intervals are wide; this is a research note with less review than METR's main publications.

**Use:** distinguish historical trend direction from exact level, probability threshold and forecasting confidence.

### S07 — MirrorCode: impressive work under an unusually strong oracle

**Source:** [Epoch AI/METR, 10 April 2026](https://epoch.ai/publications/mirrorcode-preliminary-results), methodology, limitations, Appendices B–C and notes 1–4, 8–11, 20–21.

Agents reimplement deterministic, stateless command-line programs from documentation and execute-only reference binaries, without source or internet access. Independent scoring is container-separated. Gotree coverage includes 2,001 cases across 48 of 74 commands; 102 cases are hidden. The original toolkit is about 16,000 Go lines; “2–17 human weeks” is researchers' informal estimation, not a measured long-task baseline. Runs use a simple Inspect/ReAct scaffold with compaction and budgets up to one billion input-plus-output tokens. Pkl remained unsolved: a persistent eager-versus-lazy evaluation error survived extensive diagnosis and patching. The main results are preliminary, focus on four Claude generations and acknowledge contamination and selected-program limitations. Tests and reference behaviour provide much richer feedback than most product briefs.

**Use:** strong evidence for some long autonomous implementation, not proof of general weeks-long employee replacement or a production-quality full toolkit.

### S08 — DORA: system-level complementarity, observational evidence

**Source:** [DORA report page](https://dora.dev/research/2025/dora-report/); [Google's primary summary, 23 September 2025](https://blog.google/innovation-and-ai/technology/developers-tools/dora-report-2025/); [official errata](https://dora.dev/research/2025/errata/).

Nearly 5,000 technology professionals were surveyed. DORA associates AI adoption with higher delivery throughput, reversing its preceding year's direction, and describes AI as amplifying organizational strengths and weaknesses. Adoption and perceived gains are not randomized deployment outcomes. The current report version is 2025.2; an erratum corrects “stability” to “instability” in a platform-engineering passage. The public download routes to a lead form; a partner-hosted full PDF exceeded the web tool's size limit. Full methodology and raw data were therefore **not independently audited in this pass**.

**Use:** support investment in delivery feedback and organizational practices; avoid presenting conditional associations as causally proven percentage returns.

### S09 — Public benchmark scores can overstate or understate capability

**Source:** [OpenAI audit, 23 February 2026](https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/).

OpenAI audited 138 frequently failed SWE-bench Verified problems and found at least 59.4% of **that audited subset**, not the entire benchmark, had flawed tests rejecting functionally correct submissions. It also reports contamination evidence across frontier models. This is a model vendor's analysis and recommendation; it is not an independent estimate of all real-world engineering correctness. False rejection and false acceptance are separate problems.

**Use:** versioned, private, representative tasks and human-grounded acceptance checks matter more than small leaderboard differences. The article's historical recommendation of another benchmark must not be treated as an independently verified current endorsement.

### S10 — SWE-Proof: specifications remain a research problem

**Source:** [SWE-Proof, submitted 18 September 2026](https://arxiv.org/html/2609.21190v1), sections 3–5 and Appendix B.

This preprint constructs formal versions of 500 SWE-bench Verified issues using known correct patches, specification/implementation bundles and assumptions about unchanged callees. The authors report counterexamples for a quarter to a half of test-passing patches across two models. Supplying correct specifications helps; requiring agents to produce their own does not improve resolution over the unaided baseline. The “62%” specification-audit result is model-specific in detailed tables, not universal. Crucially, the paper says its verify-implies-resolve claim is **not itself a proof**: callee-axiom soundness and refinement fidelity rely on execution, fuzzing and adversarial audit. Known-correct-patch construction, public benchmark exposure, limited models and trust assumptions constrain generalization.

**Use:** a concrete frontier for specification synthesis, differential testing and formal methods. A verified implementation is only as relevant as its specification and environmental assumptions.

### S11 — Repeated success is a different question from one successful attempt

**Source:** [τ-bench, June 2024](https://arxiv.org/html/2406.12045v1), section 3, Table 2 and Figure 4.

The benchmark models customer-service interactions with policies, tools, a simulated user and end-state database checks. It defines pass@k as at least one success in k trials, and pass^k as all k trials succeeding, averaged across tasks. Its original GPT-4o retail result was 61.2% single-run success but below 25% for all eight runs. These are **2024 configurations**, not a current frontier ceiling. The paper explicitly acknowledges that matching the final database may still miss a policy violation such as acting without required confirmation.

**Use:** repeated outcomes, authorization and final state need separate measurement. A convenient machine-checkable reward can omit important parts of correctness.

### S12 — τ²-bench: distributing control changes the problem

**Source:** [τ²-bench, 9 June 2025](https://arxiv.org/html/2506.07982v1), sections 3.2–4.3 and Appendix E.

The telecom domain gives both agent and simulated user tools. Fifteen atomic subtask groups produce 2,285 combinations; 114 tasks are subsampled to balance intent and complexity. Retail and airline contain 115 and 50 tasks. Each task runs four times at temperature zero with GPT-4.1 simulating users. Ablations compare ordinary dual control, agent control of all tools and an oracle plan. Removing user coordination raises success by roughly 20 percentage points in the reported settings. User-simulator errors persist: reported telecom errors are 16%, with 6% critical, versus retail's 40% and 12%. Thus failures cannot all be assigned to the agent's reasoning, and an LLM user is not a human population.

**Use:** workflows involving customer action, missing information and shared control need their own evaluation. More autonomy is not always authorized or possible.

### S13 — Independent reliability decomposition

**Source:** Rabanser et al., [*Towards a Science of AI Agent Reliability*](https://arxiv.org/html/2602.16666v1), submitted 18 February 2026; page carries an August 2026 preprint date. Sections 4, 6 and Appendix D.

The study evaluates 14 model configurations across GAIA and τ-bench, decomposing consistency, robustness, predictability and safety. In this setup, capability gains across model releases yield only modest reliability gains. It inspects perturbations and confidence/abstention rather than only task accuracy. Limitations are unusually relevant: two benchmarks, one scaffold per benchmark, LLM-based safety judging and subjective metric/aggregation choices. It does not evaluate every contemporary production harness; the authors explicitly propose extending to tools such as Claude Code and Codex. Safety is reported separately, so the aggregate reliability score omits some tail-risk information.

**Use:** evidence for measuring multiple operational dimensions, not a timeless theorem that more capable models cannot become reliable.

### S14 — Cost-controlled evaluation is older than the current agent hype

**Source:** Kapoor et al., [*AI Agents That Matter*, 1 July 2024](https://arxiv.org/abs/2407.01502); [authors' reproducibility dashboard](https://benediktstroebl.github.io/agent-eval-webapp/); [HAL methodology](https://hal.cs.princeton.edu/about).

The research identifies accuracy-only evaluation, conflation of model-developer and application-developer goals, inadequate holdouts and reproducibility failures. It demonstrates that considering cost can change which agent designs are attractive. HAL standardizes execution while retaining traces and cost tracking. Its older model comparisons are methodological evidence, not current procurement recommendations.

**Use:** compare simple and elaborate systems on a cost–quality frontier at matched budgets and representative workloads.

### S15 — Cheap constant capability does not mean cheap whole workflows

**Source:** [Stanford AI Index 2025 primary summary, 7 April 2025](https://hai.stanford.edu/news/ai-index-2025-state-of-ai-in-10-charts).

At a fixed GPT-3.5-level MMLU threshold, reported inference price fell more than 280-fold between November 2022 and October 2024. This historical constant-capability metric differs from the cost of the newest frontier model or an agent's total token/tool/review budget. Small models also crossed older capability thresholds with far fewer parameters.

**Use:** model access alone is a fragile moat. Do not extrapolate the historical rate to exact 2031 prices, or infer that higher demand cannot consume the savings.

### S16 — Small-model agents: distinguish a position from an established result

**Source:** NVIDIA researchers, [*Small Language Models are the Future of Agentic AI*, 2 June 2025](https://arxiv.org/abs/2506.02153).

The authors argue that repeated narrow calls often suit smaller models and heterogeneous systems. They explicitly describe a position/value statement and propose conversion approaches. This does not prove small models universally match larger ones on long-horizon reasoning, robustness or total deployment cost.

**Use:** routing, specialization and local inference deserve measured experiments. Open weights are not zero-cost operations, and small parameter counts alone do not establish acceptable performance.

### S17 — Useful vendor engineering guidance, with attribution

**Source:** [Anthropic, 9 January 2026](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents).

The guidance recommends repeated trials, outcome grading, transcript inspection, regression suites and domain-expert contributions. It distinguishes capability from consistency and emphasizes inspecting the complete agent/environment interaction. This is operational vendor guidance, not independent evidence of labor demand or a controlled comparison of evaluation frameworks.

### S18 — A very recent frontier workplace case study

**Source:** [Anthropic, 16 October 2026](https://www.anthropic.com/research/employment-at-anthropic).

Anthropic reports junior technical hires' share falling from 27% to 9%, while technical headcount still grows absolutely. Within-person observational analyses associate agent adoption with more measured output. Agent active runtime reaches six times assumed human work hours; that ratio is **not a productivity multiplier**. Adoption is nonrandom, the company is growing exceptionally fast, and code/output proxies are incomplete. Revert/deletion rates do not prove comprehensive quality equivalence. The case describes human attention bottlenecks and hiring emphasis on autonomy and judgment.

**Use:** a possible leading case of work reorganization, not a representative causal forecast for all employers.

### S19 — Learning and immediate task completion can diverge

**Source:** Shen and Tamkin, [*How AI Impacts Skill Formation*, 28 January 2026](https://arxiv.org/html/2601.20245v1), sections 4–7; [public summary, 29 January](https://www.anthropic.com/research/AI-assistance-coding-skills).

Main RCT: 52 analyzed participants, 26 per group, new to Trio but experienced with Python; **most had seven-plus years of coding**, not “mostly junior.” GPT-4o chat assisted two tasks in 35 minutes, followed immediately by an unaided 14-question, 27-point quiz. The reported gap is **4.15 quiz points**, d=0.738, p=0.01; completion-time improvement is not significant. The paper calls the gap 17%, but 4.15/27 is 15.4 percentage points: retain the raw score rather than silently choosing a different percentage interpretation. The six interaction patterns are exploratory small clusters, not randomized interventions. Immediate comprehension in one library is different from demonstrated years-long skill atrophy.

**Use:** test independent transfer and debugging ability while learning; do not equate an assisted finished artefact with acquired expertise.

### S20 — Current developer adoption and trust are conditional

**Source:** [Stack Overflow's primary survey release, 6 October 2026](https://stackoverflow.co/company/press/archive/stack-overflow-annual-developer-survey-ai-trust-conditional).

The survey has over 30,000 respondents across 169 countries. It reports coding assistants/agents used by 66%, automated workflows by 26.2%, and only 6.6% prepared to trust AI for important decisions. These are self-selected survey responses, not population-weighted hiring counts or measured defect rates. The release has a prose inconsistency about usefulness being “around a third” beside percentages of 45% and 50%; do not repeat that phrasing as precise evidence.

**Use:** distinguish assisted adoption from automated workflow adoption; verification remains salient to respondents.

### S21 — Iterative maintenance is still poorly measured

**Source:** [SlopCodeBench paper, submitted 25 March 2026](https://arxiv.org/abs/2603.24755); [official repository](https://github.com/SprocketLab/slop-code-bench); [official benchmark site](https://www.scbench.ai/).

The initial paper evaluates evolving specifications, code extension and structural quality rather than a single patch. The abstract reports 20 problems and 93 checkpoints; the current public repository/site describes 36 problems and 196 checkpoints. Those denominators and model/harness versions cannot be mixed. “Erosion” and verbosity are proposed proxies, not direct measurements of future human maintenance cost. The authors describe the release as an evolving evaluation primitive. A separate public audit exists but was not independently reproduced in this pass.

**Use:** add change requests, regressions and maintenance effort to local evaluations. Do not cite an old failure percentage as the current frontier's general software-development ceiling.

### S22 — Inference systems have substantive computer-systems foundations

**Sources:** [PagedAttention/vLLM, 12 September 2023](https://arxiv.org/abs/2309.06180); [SGLang, 12 December 2023](https://arxiv.org/abs/2312.07104).

PagedAttention applies virtual-memory ideas to dynamic KV-cache management and batching. SGLang studies structured multi-call execution, prefix sharing and constrained output. Their historical throughput improvements compare specific systems/workloads of that period; they are not current universal speedup guarantees. The durable knowledge is memory, scheduling, caching, sequence-length effects and workload-aware measurement.

**Use:** an inference engineer needs systems reasoning and profiling, not just a serving API tutorial.

## What can and cannot be inferred from these sources

S01–S04 are not measuring the same treatment or outcome. Fixed, familiar-repository tasks with active time differ from developer-week PR output after an adoption encouragement. Neither captures the full long-run equilibrium: which work becomes economical, how customers change demand, how firms reorganize, and what share of savings is captured by employees versus customers or owners.

S05–S07 and S21 are selected task distributions. Benchmarks preferentially include tasks that can be described and scored. Simulated users, visible tests, known reference executables, held-out cases and access to source change what is being measured. The right question is not “which benchmark is real?” but “which elements of this intended deployment are present, absent or simplified?”

An independent grader is not automatically a correct grader. A hardcoded expected path can reject a correct implementation; a final-state check can accept an unauthorized action; an LLM judge can share the actor's errors. Tests, policies, human adjudication and downstream observations give complementary evidence. Grader failures and indeterminate cases should remain explicit rather than silently disappearing from the denominator.

No source establishes that prompt engineering, architecture, evaluation or customer contact is permanently beyond AI. The recommendation is to combine current complements and keep measuring where the bottleneck moves.

## Reliability: useful mathematics and common category errors

Let p_i be the probability of success on task i under a fixed deployed system and environment. For independent repeated runs of that same task, at-least-one success in k attempts is 1−(1−p_i)^k; all-k success is p_i^k. Across tasks, average these task-specific quantities. **Do not substitute the overall mean p into either expression without checking heterogeneity.** For k>1, convexity means E[p_i^k] can exceed (E[p_i])^k. Correlated failures require empirical joint measurements; there is no universal direction correction that can be pasted onto a leaderboard average.

Repeated attempts are also different from sequential steps in a workflow. The familiar p^n calculation assumes independent indispensable steps with no recovery. Real agents can retry, detect errors or take alternative routes; they can also carry one mistaken premise through many steps. Measure the terminal outcome, the path's permitted actions, resources and recoveries. Do not claim that a 95% tool-call score implies a particular session-success rate without those assumptions.

Zero observed bad outcomes is weak evidence at small sample sizes. Under representative independent Bernoulli trials, the one-sided 95% upper bound after zero failures in N trials is 1−0.05^(1/N), approximately 3/N. Thus 100 clean cases still permit roughly a 3% underlying failure rate; about 3,000 clean cases are needed to put that bound near 0.1%. This calculation does not cover distribution shift, correlated cases or a faulty grader. Those need additional evidence.

A practical evaluation should retain separate denominators for:

- All eligible input cases, including abstentions, timeouts and incomplete attempts.
- Correct accepted outcomes, and outcomes accepted only after human repair.
- Permission/policy violations and severity, even when the requested state was achieved.
- Human attention, rework, latency, compute/tool spend and downstream defects.
- Coverage and error conditional on a confidence/escalation rule.

Treat any target below as a proposed engineering gate, not a measured capability or universal safety threshold.

## Adoption economics: the unit that matters

A useful decision model is:

**Net expected value per eligible case = accepted outcome value − compute/tool cost − human attention cost − allocated integration/operations cost − expected failure loss.**

This is an accounting framework, not an empirically fitted forecast. Include latency and error-severity limits separately when a mean hides unacceptable tails. A cheaper model may be more expensive per accepted outcome if it causes more review, retries or customer abandonment. A costly model may be worthwhile on rare difficult cases. Self-hosting adds utilization, hardware, maintenance and operational responsibility; “open” does not remove those costs.

For retries, expected attempts approaching 1/p assumes success can be recognized, attempts behave suitably and retry budgets are unconstrained. An unreliable verifier or irreversible action breaks the simple argument. Model routing must be evaluated as a whole system: routing errors, fallback cost and delayed completion count.

The engineering opportunity is conditional: a buyer must have a valuable repeated problem, usable inputs, authority to act and a budget. Technical need alone is not a business model.

## Three nonobvious, falsifiable implications

### H1 — Cheap trustworthy feedback may matter more than nominal task length

**Inference:** the economically automatable frontier depends strongly on how cheaply correctness can be recognized. A long deterministic translation with an executable reference may be easier to delegate than a short ambiguous customer decision. This suggests work in executable specifications, differential testing, contracts, data provenance and state-based acceptance—not a claim that writing natural-language specifications is an eternal human moat. S07, S09–S12 motivate the hypothesis.

**Counterarguments:** stronger models can infer intent and create their own tests; platforms can commoditize verification; a beautifully checked wrong specification can make errors more persuasive. Some products need approximate usefulness rather than exact equivalence.

**Falsifier for the local career/product bet:** on held-out representative work, an off-the-shelf system matches the bespoke evidence/verification layer's accepted outcomes, human attention and failure severity at lower full cost. Another failure is spending heavily on checks that do not change a decision or reduce loss.

**Test:** compare an unchanged base agent with a version receiving explicit invariants and independent state checks. Hold model, task set and total budget fixed; include hidden perturbations and measure both rejected-correct and accepted-incorrect outcomes. Audit the verifier as well as the actor.

### H2 — Human oversight becomes a queueing and prioritization problem

**Inference:** adding agents can move the constraint from implementation to attention. If incoming exceptions demand more review time than a team can supply, backlogs and latency rise. A human-in-the-loop box does not by itself define a scalable operating model. S12–S13 and S18 motivate testing interrupt quality and uncertainty filtering.

**Counterarguments:** agents can batch, summarize, review one another and resolve routine exceptions; human contact is sometimes intrinsically the valuable service. A human review bottleneck may indicate poor interface design rather than a durable job category.

**Falsifier:** accepted outcomes scale tenfold with approximately flat human attention and stable loss/latency, using a simpler or generic system. Alternatively, more oversight might have negligible effect on actual error detection, invalidating the review layer's value.

**Test:** increase concurrency at a fixed human-review budget. Track useful interventions per interruption, minutes per accepted outcome, backlog, delay and missed severe errors. Compare calibrated escalation against “ask the human about everything” and agent self-confidence alone.

### H3 — Preserving independent competence is an investment, not nostalgia

**Inference:** learning should optimize future transfer and diagnosis as well as today's completion. Fast assisted output can hide weak mental models; a leader needs enough depth to discover when the tools, specification or team are wrong. S19 is narrow but directly relevant.

**Counterarguments:** people can develop new higher-level expertise while delegating syntax; old skills can become obsolete; AI tutoring may improve learning. The study does not establish long-run deskilling, and exploratory interaction clusters do not prove an optimal learning policy.

**Falsifier:** after equivalent learning time, assisted learners solve delayed unseen tasks and diagnose realistic failures as well as or better than alternatives, while producing more useful work. If independently implementing a particular component never improves transferable diagnosis or decisions, it may be the wrong practice target.

**Test:** alternate generation-first and explanation/prediction-first learning sessions. Use fresh transfer problems, code-reading and injected-bug diagnosis without assistance after one day and one week. Record time and explanations, not only whether a generated application runs.

## Foundations and mastery gates

These are proposed study directions, not software installation requests or a claim that every lane must be mastered at once. Choose one primary depth area and one adjacent area; use the shared core across them.

| Foundation | Learn enough to reason about | Observable proof of mastery |
|---|---|---|
| Empirical ML and statistics | Probability, conditional error, calibration, confidence intervals, sampling, linear algebra, differentiation/optimization, overfitting and distribution shift | Build a strong simple baseline; explain leakage; use grouped/time-based splits where needed; distinguish an effect estimate from noise; reproduce a result with uncertainty |
| Software and distributed state | Data modelling, transactions, concurrency, cancellation, retries, idempotency, eventual consistency and authorization | Recover a multi-step workflow after process death without duplicate effects; diagnose a race; explain invariants and failure semantics |
| Data and retrieval | SQL, schema contracts, temporal joins, versioning, lineage, search/embedding tradeoffs and access filtering | Show which retrieved evidence supported each accepted outcome; measure misses and stale/forbidden retrieval; compare lexical/hybrid/embedding baselines |
| Model internals and inference | Tokens, loss, attention, KV cache, prefill/decode, batching, memory bandwidth, quantization and scheduling | Predict memory/latency bottlenecks, verify with a profiler, and improve a fixed workload without silently reducing quality |
| Evaluation and decision systems | Independent oracles, metamorphic/property tests, differential checks, risk–coverage tradeoffs, traces and drift | Produce a held-out evaluation with reproducible failures, judge audits, severity classes and operating cost; make a justified release/rollback decision |
| Product/domain economics | Customer workflow, outcome value, incentives, constraints, procurement and operating budget | A domain expert uses the output to make a real decision; demonstrate improvement over the previous process and account for integration/support costs |

Useful arithmetic before buying hardware: parameter count × bytes per stored parameter gives a **weights-only lower bound**. Runtime buffers, activations, KV caches, concurrency and implementation overhead add memory. Active parameters in a mixture-of-experts model concern computation; they are not the same as all weights that must be stored or moved. Always profile the actual workload and runtime.

For a deeper language-model systems path, [Stanford CS336 Spring 2026](https://cs336.stanford.edu/) publicly covers tokenization, architectures, kernels/Triton, training, inference, data and evaluation with assignments. It is a demanding sequence rather than an introductory API course. For distributed systems, [MIT 6.5840 Spring 2026](https://pdos.csail.mit.edu/6.5840/) provides the relevant fault-tolerance and coordination grounding. These are learning resources, not credentials that establish readiness by themselves. Coursework that requires downloads, packages or compute would require the user's normal approval before execution.

## Realistic role families and technical differentiation

Current employer examples and geographic caveats are maintained in [labor.md](labor.md). Role names here describe existing families, not forecast vacancy counts or guaranteed entry levels.

1. **Applied AI / forward-deployed / product ML engineer.** Strong full-stack and integration ability, empirical evaluation and a domain workflow. Differentiator: repeatable useful outcomes in messy customer environments, with measured human effort and cost. Entry proof can be one narrow end-to-end system; leadership requires managing cross-team requirements, incidents and adoption.
2. **ML platform / inference / performance engineer.** Systems programming, profiling, GPU/accelerator architecture, scheduling and serving. Differentiator: reproducible improvements at matched latency/quality/cost, not a cherry-picked tokens-per-second chart. A credible path starts with smaller fixed workloads before distributed large-model infrastructure.
3. **Evaluation / AI reliability / model behaviour engineer or research engineer.** Statistics, test/oracle design, dataset construction and production diagnosis. Differentiator: finding important failures that existing evaluations miss and demonstrating that fixes generalize to held-out cases. S10 suggests a more research-intensive formal-specification branch.
4. **Data / retrieval / ML infrastructure engineer.** Schemas, state, permissions, lineage, indexing, temporal consistency and operations. Differentiator: making the right current evidence available to decisions and showing that data changes improve downstream outcomes. This can remain conventional software/data engineering with AI-specific demands.
5. **ML research engineer.** Strong mathematics, experimental discipline, implementation depth and the ability to reproduce and extend research. Differentiator: an independently reproducible improvement with honest negative results and ablations. Training frontier models from scratch is not the only route, but generic API orchestration alone does not establish this skill set.

Security, robotics and physical-domain specializations cross these families; their deeper prerequisites belong to the corresponding research tracks. Avoid splitting attention across every field merely because all are advancing.

## Concrete first 30 days: choose one main experiment

### Experiment A — Establish an honest personal productivity baseline

Choose a narrow recurring development workflow and define 20–30 eligible tasks before choosing tools. Randomize or counterbalance similar tasks across existing approved approaches; do not solve the same task twice and pretend the second attempt is independent. Record prior familiarity, difficulty forecast, excluded tasks, incomplete attempts, concurrent activity, prompting/waiting, review and repair. Use blinded acceptance when feasible.

**Proof metrics:** accepted outcomes per total human hour; elapsed delivery time; post-acceptance rework; full tool cost; uncertainty and task mix. A small sample is a diagnostic, not a universal causal claim. The output is a concise methods/result report with counterexamples, not a “10× engineer” assertion.

### Experiment B — Build a measurable reliability slice

Using an existing permitted environment, specify one local/synthetic state-changing workflow with at least 100 varied cases. Compare a simple baseline with a model-assisted system. Repeat selected cases, inject transient failures, duplicate requests, missing fields, stale state and permission denials. Keep the grader separate and include cases where a superficially completed result is wrong.

**Proof metrics:** correct accepted outcomes; false acceptance/rejection; duplicate effects; recovery after interruption; human minutes; latency and cost distributions. Report the zero-failure sample-size limitation. The aim is a reliable measurement instrument and a failure taxonomy, not a small-sample claim of 99.9% autonomy.

### Experiment C — Identify one inference bottleneck

On hardware and models already available and authorized, replay a fixed workload at varying input length, output length and concurrency. Compare an existing simple service with one measured change, such as batching, caching or model routing. If the required model/runtime is unavailable, produce the benchmark protocol first; installing or downloading it is a separate approval-dependent step.

**Proof metrics:** time to first token, completion latency, throughput under an explicit latency target, peak memory, cost per accepted task and fixed-task quality. Explain bottlenecks from first principles before adding infrastructure. A target such as a 20% improvement is a proposed goal, not a promised or observed result.

### Learning practice alongside any experiment

Twice weekly, explain a component and diagnose an unfamiliar injected fault without AI. Ask the assistant for challenges, counterexamples and critiques after making a prediction. Revisit a new problem one week later. Track transfer rather than typing speed or hours of video watched. Maintain a short record of incorrect beliefs and the evidence that corrected them.

## A 90-day proof project, with branches

**Applied automation branch:** one domain workflow, a strong conventional baseline, representative held-out cases, observability, repair and a small supervised pilot only when authorized. Measure the entire eligible-case denominator. A proposed gate is materially lower human effort and total cost at a specified correctness/severity level, demonstrated over more than a single happy-path session. Publish only permitted, anonymized artefacts.

**ML systems branch:** a reproducible serving/data pipeline experiment with fixed traces and a clear cost–latency–quality frontier. Include one adverse regime where the proposed optimization loses. A technical report explaining why a simpler baseline wins in some cases can be stronger evidence than an elaborate demo.

**Evaluation/research branch:** a small high-quality benchmark of 10–20 distinct repository or workflow issues with independent acceptance criteria, including permission and maintenance constraints. Hold back part of the suite; keep correct patches and hidden tests away from the actor. Compare ablations at matched budgets and audit the oracle. This is a tractable start, not a substitute for larger-scale validation. A formal-methods extension can verify a narrow component with explicit assumptions and differential tests against its real environment.

**Required artefacts:** a runnable reproducibility path, versioned data/task definitions, baseline, failure traces, uncertainty, ablations, operating costs, assumptions and a short product-impact account. Evidence of another competent person reproducing the result is a stronger gate than certificates, repository stars or self-described seniority.

## Becoming a strong expert or leader by 2031: gates, not promises

- **2026–2027:** close foundational gaps and own one working system through development, realistic testing and operations. Demonstrate independent diagnosis. Build a reference-quality case study rather than many disconnected prototypes.
- **2027–2028:** deepen a primary specialty, contribute a reproducible technical improvement and mentor another engineer. Own a cross-system decision including tradeoffs, measurement and failure handling. Seek external technical review.
- **2028–2029:** establish a domain and a repeatable technical method others adopt. Leadership evidence is better decisions and higher team capability, not just personal output. Reassess whether platforms have commoditized the original advantage.
- **2029–2031:** lead a consequential product/platform/research area with demonstrated adoption, trustworthy evidence and sustainable economics. Develop others who can reason independently. Maintain an adjacent specialty so movement in the technology frontier does not strand the career.

This sequence can support strong expertise; it cannot guarantee becoming a field leader. Access to real problems, mentors, collaborators, capital and market conditions also matters. Revisit the bet at least quarterly using actual outcomes and changing demand.

## Open gaps for subsequent scheduled research passes

1. Replicate selected study calculations from public data rather than relying on reported coefficients; especially compare equivalent windows/estimands for enterprise trials. The narrow methods audit above is source inspection, not reanalysis.
2. Obtain and inspect the full current DORA methodology/measurement model through an ungated primary or official partner copy; assess sampling, missingness, model specification and availability of raw data.
3. Verify whether MirrorCode has a subsequent full release, more model families, genuinely held-out programs and measured long-task human baselines. The April preliminary report must not be labelled latest simply because it is the source read here.
4. Inspect full reproducibility materials and independent replication of SWE-Proof and iterative-maintenance benchmarks. Test oracle fidelity and version-specific denominators before using their headline rates.
5. Find longitudinal, real-work evidence on skill formation and maintenance cost, including AI tutoring counterexamples and downstream defect burden; immediate quizzes and static complexity proxies are insufficient.
6. Separate current posted roles from filled roles, compensation, hiring volumes and geographic eligibility. Use labor-track evidence; selected job ads alone cannot establish future demand.
7. Quantify full deployment economics with real workload traces, utilization and human review. Historical constant-capability token-price trends are not the total-cost forecast.
8. Identify where improved model reliability, platform tooling or customer adoption falsifies H1–H3. Keep contrary evidence and unsuccessful experiments visible.

## Integration instructions for the final synthesis

Use this track as branches for software/ML foundations, inference systems, evaluation/reliability, data infrastructure and applied product engineering. Cross-link robotics and science where feedback, uncertainty, state and domain knowledge become more demanding. The final map should let the reader choose a primary path, see prerequisites and proof tasks, understand counterarguments, and know what evidence would change the choice. It should not imply that a list of fashionable tools equals expertise or that any title is future-proof.
