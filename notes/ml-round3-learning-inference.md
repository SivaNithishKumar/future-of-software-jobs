# ML trajectory: learning, inference and attainable original research — round 3

Checked 19 October 2026. This is a bounded technical research pass, not a completed global forecast. It examines original papers, methods/appendices and public artefacts, without repeating the productivity studies or institutional directory. No model was trained or evaluated, repository installed, private data accessed, paid compute consumed, paper submitted or researcher contacted. Resource requirements below are reported source configurations or explicitly proposed smaller experiments, not a claim that the reader's hardware can reproduce them.

## The technical direction that survives skeptical reading

The strongest opportunity is not an unconditional rule that a small model, more reasoning, synthetic data or continual learning wins. It is the ability to discover which intervention improves a defined task distribution at an honest total budget, and to recognize when the evaluation is rewarding the wrong thing.

The papers below support six research branches with practical connections:

1. **Adaptive inference:** choosing how much computation to use, including when to stop, select another model or obtain better evidence.
2. **Learning from verifiable feedback:** reward design, exploration and independent checking, rather than assuming passing the training verifier establishes general reasoning.
3. **Specialization and distillation:** matching teacher, student, data and objective; including teacher/label production in the cost.
4. **Data efficiency and provenance:** retention, diversity, contamination and tail performance under generated-data feedback.
5. **Continual adaptation:** deciding what should live in retrieved evidence, context, an external memory or weights, while measuring forgetting and update cost.
6. **Uncertainty and selective action:** learning or estimating confidence that remains useful under a changed domain, format or inference policy.

These are plausible areas to build expertise through 2031, not claims of permanent human comparative advantage. Tool vendors and base-model improvements may absorb today's bespoke methods. The durable skill is experimental judgment plus the ability to implement and test the mechanism.

## Paper audit

Each entry identifies the version inspected or the current metadata separately. ArXiv identifiers/DOIs do not establish peer review. A reported improvement is attributed to its authors unless independently replicated. None of these studies is itself a labor-demand forecast.

### R01 — Test-time compute helps conditionally, and its controller is not free

**Paper:** Snell, Lee, Xu and Kumar, [arXiv:2408.03314v1](https://arxiv.org/html/2408.03314v1), 6 August 2024; [ICLR 2025 paper](https://openreview.net/pdf?id=4FWAwZtd2n). [DOI](https://doi.org/10.48550/arXiv.2408.03314).

The study fine-tunes PaLM 2-S* for revisions/verifiers and evaluates MATH using a 12,000-training/500-test split. More than 4× test-time efficiency and comparisons against a 14× larger model depend on question difficulty, strategy and pretraining/inference workload. Hardest problems often favor additional pretraining. **Section 3.2 estimates difficulty from 2,048 samples per problem**, either using correctness or a learned verifier. Two-fold cross-validation selects strategies, but the additional difficulty-estimation cost is explicitly omitted. Process-reward models trained on another model's outputs were exploitable under distribution shift. This is not a result that any small model can be prompted into replacing a frontier model at four times lower full cost.

**Research opening:** a low-cost, held-out controller that includes its own computation in the budget. Exact proprietary-model replication is not established; an open-model experiment must be labelled an extension.

### R02 — More sequential reasoning can make answers worse

**Paper:** Gema et al., [arXiv:2507.14417v2](https://arxiv.org/abs/2507.14417v2), 15 December 2025; metadata reports **TMLR publication**. Methods were first inspected in [v1 full text](https://arxiv.org/html/2507.14417v1); final-version differences remain to audit. [DOI](https://doi.org/10.48550/arXiv.2507.14417).

The authors deliberately construct inverse-scaling tasks: misleading counting/code framings, spurious-regression features, deduction constraints and risk evaluations. Controlled reasoning budgets and natural-length conditions reveal distraction, framing and focus failures. These are counterexamples to universal monotonic improvement, not an estimate that long reasoning usually hurts ordinary work. Forced extra tokens and selection of failure-revealing tasks limit population generalization. The original open-model campaign used eight H200s; [official code/data generators](https://github.com/safety-research/inverse-scaling-ttc) are MIT licensed. The README itself contains an incorrect arXiv string in its citation; use the paper metadata.

**Research opening:** fresh generated distractor tasks plus matched-budget strategies, with correctness and cost measured before and after a model-specific stopping rule.

### R03 — Verifiable RL is real progress, with a substantial inherited base

**Paper:** DeepSeek-AI, [DeepSeek-R1 repository/report](https://github.com/deepseek-ai/DeepSeek-R1); [Nature version of record](https://doi.org/10.1038/s41586-025-09422-z), 17 September 2025. The Nature full text was inaccessible through the browser in this pass; detailed cost claims from secondary reporting are therefore **not used**.

R1/R1-Zero provide important evidence that outcome-reward RL can improve reasoning behaviour, and distillation transfers behaviour to smaller students. They do not establish that the base model, prior data or training infrastructure was cheap or unnecessary. Released model weights and descriptions do not amount to an independently reproducible complete pretraining/post-training corpus and campaign. Code/weights are described under MIT, while distilled checkpoints inherit Qwen/Llama base-model conditions that must be checked individually. The paper's main mathematical/coding benchmarks are useful tests, not a new private distribution proving general autonomous deployment.

**Research opening:** study a narrow mechanism using available checkpoints; do not claim to reproduce frontier-scale training or infer total system cost from an RL-stage figure.

### R04 — RL's single-answer gain and coverage gain are different questions

**Paper:** Yue et al., [arXiv:2504.13837v5](https://arxiv.org/html/2504.13837v5), 24 November 2025; metadata reports **NeurIPS 2025 Oral**. [Project/code channel](https://limit-of-rlvr.github.io/). [DOI](https://doi.org/10.48550/arXiv.2504.13837).

Across tested base/RL model pairs and math, coding and visual tasks, RL often improves pass@1 while base-model pass@k catches up or wins at larger k. The study interprets this as distribution sharpening rather than new capacity under the tested binary-reward regimes. **Pass@k assumes recognition of at least one correct candidate**; it is not a deployable selection procedure or proof that the base model is preferable at equal cost. Finite sampling, answer-space guessing, decoding and benchmark exposure also limit claims about an absolute reasoning boundary. The authors' own project distinguishes their question from practical utility and does not reject all RL paradigms.

**Research opening:** measure both coverage and selectable performance, especially on generated held-out tasks where answer guessing and contamination are controlled.

### R05 — A counterexample to “RL can only sharpen”

**Paper:** He, Fried and Welleck, [arXiv:2506.02355v2](https://arxiv.org/html/2506.02355v2), 20 June 2025. Peer-review status not independently verified here. [DOI](https://doi.org/10.48550/arXiv.2506.02355).

In Lean theorem proving and a toy environment, the authors identify GRPO rank bias toward probable successful trajectories. Up-weighting rare correct solutions and changing updates per batch improve pass@N over a broader budget range. This is evidence that training recipe and exploration matter; it is not proof of arbitrary new human-level mathematical discovery. A proof checker verifies a formal statement under its assumptions, not whether the statement captures a customer's intent. [Official Apache-2.0 implementation](https://github.com/AndreHe02/rewarding-unlikely-release) integrates veRL, Lean REPL and DeepSeek-Prover tooling. It uses curated sets of theorems already shown provable by other systems, a relevant selection condition.

**Research opening:** reproduce the small rank-bias experiment before considering model training; test coverage improvements on a fresh formal-task family.

### R06 — A verifier can reward the wrong abstraction

**Paper:** Helff et al., [arXiv:2604.15149v1](https://arxiv.org/html/2604.15149v1), 16 April 2026; preprint, venue not verified. [DOI](https://doi.org/10.48550/arXiv.2604.15149).

The study examines logical-rule induction: enumerating instance labels can pass extensional checks while failing to infer the intended rule. Isomorphic Perturbation Testing checks whether a purported rule survives semantics-preserving changes. Controlled reward changes support a causal shortcut mechanism in this setup. The broad association between some publicly released “RL” models and shortcut behaviour does **not** by itself isolate RL from all architecture/data confounds. Independent perturbations can improve a verifier without proving its completeness. A dedicated public code/data release and its licence were not located in the inspected full text; reproducibility is therefore incomplete in this pass.

**Research opening:** implement a small transparent rule world with independently generated isomorphisms and audited valid/invalid programs; this can be explored without frontier compute.

### R07 — Distillation has a capacity gap and a cost boundary

**Paper:** Busbridge et al., [ICML 2025/PMLR publication](https://proceedings.mlr.press/v267/busbridge25a.html); [arXiv metadata v2](https://arxiv.org/abs/2502.08606v2), 25 July 2025. Detailed methods inspected in [v1](https://arxiv.org/html/2502.08606v1); version differences not rederived. [DOI](https://doi.org/10.48550/arXiv.2502.08606).

The scaling fit uses hundreds of runs, English C4 and separate teacher/student splits. Its principal objective is language-model cross-entropy, using the teacher's full token distribution—not merely API-generated answers. The authors note C4 limits reasoning evaluation; some reasoning tests are near random. A teacher can be too strong for the student, and including teacher training can make direct supervised training preferable when producing one student. Teacher cost is easier to amortize across many students. A general AXLearn implementation is referenced, but complete study checkpoints/data and exact replication hardware were not verified.

**Research opening:** compare teacher size, data mixture and label cost on one task. Do not transplant these fitted coefficients directly into agent success or assume the best frontier teacher always yields the best specialist.

### R08 — Typed output is an interface property, not a reasoning guarantee

**Paper:** Lee, D'Antoni and Berg-Kirkpatrick, [The Format Tax, arXiv:2604.03616v1](https://arxiv.org/html/2604.03616v1), 4 April 2026; preprint. [DOI](https://doi.org/10.48550/arXiv.2604.03616).

Across selected open/API models and JSON/XML/LaTeX/Markdown conditions, the study attributes much performance loss to format instructions before decoder constraints. Separating freeform reasoning from final formatting recovers much of it; some structured conditions also help. Most recent closed models in this experiment are comparatively resistant. [MIT code/results](https://github.com/ivnle/the-format-tax) expose the pipeline, but its README says **all results use a Qwen3-32B LLM judge**, while paper prose singles out MATH scoring. Scoring fidelity and prompt/extraction differences deserve an independent audit. Format validity and semantic correctness must be measured separately.

**Counter-evidence:** [Capacity, Not Format, arXiv:2606.09410v1](https://arxiv.org/html/2606.09410v1), 8 June 2026, argues effects depend on capacity, truncation and schema complexity, including a frontier penalty near difficult tasks. This is also a preprint, not a universal causal law.

### R09 — Generated-data feedback can lose tail information

**Paper:** Shumailov et al., [Nature 631, 755–759](https://www.nature.com/articles/s41586-024-07566-y), 24 July 2024; [DOI](https://doi.org/10.1038/s41586-024-07566-y). The article links a March 2025 correction; its details remain to inspect.

The research studies generations of models trained on prior model output and explains how resampling/approximation can erase tails. It covers generative model settings, not all deliberately curated synthetic augmentation or every training mixture. Its public code/data availability statements point to experiment references; the exact current release and licences were not independently inspected. Replacing a corpus, mixing original data, filtering outputs and acquiring new external observations are materially different interventions.

**Research opening:** measure minority/tail performance and data provenance, rather than treating “synthetic” as a sufficient quality label. This paper does not establish an imminent universal end to useful training data.

### R10 — Accumulation is a countercase, not a universal cure

**Paper:** Gerstgrasser et al., [arXiv:2404.01413v2](https://arxiv.org/html/2404.01413v2), 29 April 2024; venue not independently verified because OpenReview was blocked. [DOI](https://doi.org/10.48550/arXiv.2404.01413).

The language experiments use 9–125M models and TinyStories, **itself GPT-3.5/4-generated**: “real” here includes retaining an original reference corpus, not necessarily human-authored text. Accumulation grows the dataset and training steps; the authors also run a size-matched replacement ablation. In the VAE experiment, accumulated data still lose minor features and test error increases slowly. The theoretical “no collapse” statement is a bounded-error result in a linear model, not preservation of every tail or no degradation. These distinctions qualify both “synthetic data inevitably ruin models” and “keep old data and everything is solved.”

**Research opening:** a small controlled mixture/replay experiment with fixed compute and independent tail metrics. The complete original code/licence was not verified in this pass; an independent mathematical reproduction is more attainable than a full multi-generation LM campaign.

### R11 — Self-adaptation is not solved continual learning

**Paper:** Zweiger et al., [SEAL, arXiv:2506.10943v2](https://arxiv.org/html/2506.10943v2), 18 September 2025; [NeurIPS 2025 proceedings PDF](https://papers.neurips.cc/paper_files/paper/2025/file/6b41e04c41726e2a60e456d0a2b961ab-Paper-Conference.pdf). [DOI](https://doi.org/10.48550/arXiv.2506.10943).

SEAL generates self-edits and update directives, then rewards downstream performance after fine-tuning. Few-shot evaluation uses **eight held-out tasks × five configurations**, not the whole ARC distribution. Knowledge incorporation uses 200 SQuAD evaluation articles; disjoint RL passages do not rule out base-pretraining exposure. The paper explicitly reports forgetting, 30–45 seconds per fine-tune/evaluate reward and dependence on labelled downstream tasks. [MIT code](https://github.com/Continual-Intelligence/SEAL) includes data/instructions and recommends 2 A100/H100 GPUs; the paper's small few-shot section reports individual runs on one A100/H100/H200. These are experiment-specific requirements, not contradictions to erase.

**Research opening:** compare sequential updates with retrieval, context and replay on fresh facts, measuring both incorporation and retention plus the reward-computation cost.

### R12 — Nested learning is a research design space, not a deployed replacement

**Paper:** Behrouz et al., [Nested Learning, arXiv:2512.24695](https://arxiv.org/abs/2512.24695); [v1 full text](https://arxiv.org/html/2512.24695v1), 31 December 2025. [Google Research publication account](https://research.google/blog/introducing-nested-learning-a-new-ml-paradigm-for-continual-learning/) identifies NeurIPS 2025. [DOI](https://doi.org/10.48550/arXiv.2512.24695).

The work frames memory/optimization as processes at multiple update timescales and introduces HOPE. It reports language-model, knowledge, long-context and continual-learning experiments. A unifying formulation and selected gains are not proof that ordinary production models now learn indefinitely, maintain privacy boundaries or avoid all forgetting. No official complete HOPE code/checkpoints/data recipe with verified licence and resource estimate was established in this pass. Independent unofficial implementations cannot be silently substituted for the authors' artefact.

**Research opening:** implement a small explicit multi-timescale memory experiment against ordinary recurrent/attention/replay baselines. It is a mechanism study; reproducing an entire new model family is a different project.

### R13 — Confidence can be a training objective, with conditional guarantees

**Paper:** Damani et al., [Beyond Binary Rewards/RLCR, arXiv:2507.16806v2](https://arxiv.org/html/2507.16806v2), 15 May 2026; [official ICLR 2026 project](https://rl-calibration.github.io/). [DOI](https://doi.org/10.48550/arXiv.2507.16806).

RLCR combines correctness with a Brier-score reward on verbalized confidence. Its theorem gives an **incentive at the reward optimum under stated probabilities**, not a guarantee finite training finds a calibrated deployed model under arbitrary shift. Main experiments use Qwen2.5-7B, modified HotpotQA with removed evidence and mathematics, plus other benchmark domains. Out-of-domain means outside the RL dataset, not proven absent from pretraining. [MIT repository](https://github.com/damanimehul/RLCR) supplies checkpoints/data/results, reports 4 A100s for Hotpot and 6 for math, and permits single-GPU inference; full model/data licences still need exact-card checks. Some OOD grading uses an LLM judge.

**Research opening:** evaluate released outputs/checkpoints with independent correctness labels, calibration/discrimination and selective-risk metrics before attempting RL training.

### R14 — Calibrating the confidence prior has a hidden data-collection bill

**Paper:** Wang et al., [CalibSFT, arXiv:2609.32470v1](https://arxiv.org/html/2609.32470v1), 26 September 2026; recent preprint, independent replication/venue not verified. [DOI](https://doi.org/10.48550/arXiv.2609.32470).

The method broadens confidence support before confidence-aware RL, using sampled correctness to construct targets and balancing across confidence levels. It supervises reasoning only on correct examples, confidence on all. The authors report gains across 16 benchmarks and several RL methods, including selective prediction/routing. **Appendix D.8's 6.9% fine-tuning overhead compares 8.8 versus 127.3 GPU-hours but excludes 147 GPU-hours of one-time rollout collection at 50 samples/question.** Data reuse can amortize it; a one-off small product cannot ignore it. [Apache-2.0 code/checkpoints](https://github.com/ml-stat-Sustech/verbalized-confidence-training) are available; the paper's GPU/wall-time accounting warrants a separate arithmetic audit before budgeting.

**Research opening:** start with released outputs or a smaller sample-budget study, keeping data generation, calibration and downstream cost in the comparison.

## What these papers do not settle

**A larger pass@k does not establish a better deployed solver.** It measures whether an oracle could find a success among attempts. The selector may not recognize it, and retries cost time. Conversely, higher pass@1 is often a practical gain even if a large-sampling boundary narrows. Compare token/compute-matched selectable accuracy, not only best-case coverage.

**A public benchmark held out from fine-tuning is not necessarily novel to pretraining.** “OOD” can mean a different benchmark with related content and publicly known answers. Fresh procedural tasks, new external observations, dates/groups withheld from training and independently verified labels give different kinds of evidence; none alone establishes arbitrary generalization.

**Format, typed contracts and semantics are separate.** A schema prevents malformed outputs; it does not ensure a field is correct, a claim is grounded or an action is appropriate. Generating an unconstrained analysis then a constrained final object may help some models and cost more. A pipeline with a strong deterministic checker can still outperform a large model in a narrow domain. R08 is a testable counterexample to a universal rule, not a reason to abandon interfaces.

**More synthetic data is not necessarily more information.** A teacher can repeat its blind spots. Retaining reference data, collecting independent observations, verifying labels and preserving tail coverage are different levers. A toy linear bounded-error theorem is not proof about all facts and subgroups in a production model.

**Changing weights is only one adaptation mechanism.** Retrieval/context can update cheaply and permit source inspection; weights can compress frequent patterns and lower repeated inference costs but introduce update, retention and rollback burdens. The application determines the best mix. A continuously running gradient loop is not evidence of continual useful learning.

**Calibration is not the same as usefulness or discrimination.** A constant confidence equal to base accuracy can be calibrated yet unable to identify any risky case. ECE depends on bins and can hide subgroup errors. Measure Brier/NLL where meaningful, AUROC or precision/recall for errors, risk–coverage curves and the actual action cost. Calibration claims rely on the correctness labels and exchangeability/shift assumptions of the evaluation.

## Artefact and resource readiness

| Mechanism | What can be inspected now | Reported resource / licence / limitation | Feasible starting point |
|---|---|---|---|
| Adaptive test-time compute, R01 | Paper equations, splits, strategies and evaluation budget | Proprietary PaLM 2/Codey campaign; exact open replication not established | Implement a clearly labelled open-model or trace-based controller with its cost counted |
| Inverse scaling, R02 | [Official generators/configs/results tooling](https://github.com/safety-research/inverse-scaling-ttc) | MIT code; original open-model setup 8 H200; API and dependency access required for reproduction | Fresh task generation and one-model budget sweep; campaign not required |
| RL coverage, R04/R05 | [R04 project](https://limit-of-rlvr.github.io/) and [R05 code](https://github.com/AndreHe02/rewarding-unlikely-release) | R05 Apache-2.0; Lean/verifier/veRL/model prerequisites; exact affordable training budget unverified | Reproduce toy bias mechanism or evaluate existing samples before training |
| Format effects, R08 | [Code, results and licence](https://github.com/ivnle/the-format-tax) | MIT; existing-results analysis can avoid model calls; full campaign model/compute cost not verified | Paired score audit, deterministic parser and novel schema-complexity test |
| Synthetic-data retention, R09/R10 | Published equations and ablations | Paper, original data and software licences are distinct; full release not audited | CPU-scale linear/Gaussian model reproduction, explicitly limited to that setting |
| SEAL, R11 | [Official data/code/README](https://github.com/Continual-Intelligence/SEAL) | MIT code; 2 A100/H100 general README, smaller paper configuration varies | Frozen-model/RAG baseline, then permitted small adaptation; do not promise laptop reproduction |
| Multi-timescale learning, R12 | Paper and Google Research account | Complete official artefact/licence/resources unverified | Small mechanism experiment; no claim to reproduce HOPE |
| RLCR, R13 | [Code, saved outputs, model/data collection](https://github.com/damanimehul/RLCR) | MIT code; 4/6 A100 training, single-GPU inference in README; base/weight/data terms separate | Recompute metrics from supplied outputs before training |
| Confidence-prior learning, R14 | [Official code and checkpoints](https://github.com/ml-stat-Sustech/verbalized-confidence-training) | Apache-2.0 code; expensive rollout collection and 8 GPU training setup reported | Smaller rollout-budget ablation or evaluation-only replication |

These are resource descriptions, not GPU product comparisons. The systems track owns device/runtime selection. A smaller model or experiment changes the claim being tested and should be described as an extension, not an exact reproduction.

## Four attainable research projects

Choose one flagship. The timelines assume roughly 8–12 focused hours/week and already sufficient Python/basic ML skills; they are planning ranges, not guarantees. New libraries/weights/compute purchases require approval, and no project execution is authorized by this research document. A successful 90-day result can be an independent failure or a corrected benchmark, not necessarily a publishable new algorithm.

### Q1 — Can a cheap controller spend reasoning only where it pays?

**Papers:** R01, R02, R08. **Hypothesis:** a controller based on cheap observable signals outperforms fixed budgets on a new task mixture after paying for its own predictions and formatting stage.

**First 30 days:** define 200–500 fresh arithmetic/deduction/data-transformation cases from independently validated generators. Include ordinary and distractor versions. Compare direct answer, fixed short/long reasoning, repeated independent sampling with a real selector, and freeform-then-JSON. Hold token budgets, truncation rules, parser and correctness checks explicit. Generate or validate tasks before evaluating candidate policies.

**By 90 days:** learn a small controller on a development split; evaluate on unseen generator seeds, structures and schema complexity. Report paired correctness changes, full tokens/calls, latency distribution and failure categories. An oracle strategy is only an upper bound. Compare a simple routing rule/logistic model with more elaborate control.

**Kill criteria:** gains disappear on fresh structures; controller/selector cost erases savings; changing answer extraction explains the effect; long reasoning only wins because its budget was larger; or a standard runtime's existing policy matches the result. Preserve such findings.

**Potential contribution:** a reproducible benchmark or measured low-cost allocation rule, useful to applied AI and research-engineering teams without pretending to train a frontier model.

### Q2 — Does the reward teach the rule or exploit the checker?

**Papers:** R04–R06. **Hypothesis:** independent isomorphic checks and an exploration-aware recipe improve genuine rule transfer rather than only verifier score.

**First 30 days:** construct a tiny rule-induction or formal puzzle world with an independent solution oracle. Enumerate known-valid and known-invalid candidate rules. Show exactly which shortcuts an extensional verifier accepts, then test semantics-preserving renaming, reordering and fresh instances. If the checker cannot reliably reject shortcuts while accepting valid alternatives, stop before any expensive training.

**By 90 days:** on approved resources, compare a simple learner/bandit or small-model training recipe with identical data and update budgets. Separate train reward, held-out transfer, high-k coverage and selectable performance. Include a no-learning search baseline. Count verifier calls and teacher guidance; do not attribute teacher-injected knowledge solely to RL exploration.

**Kill criteria:** the new checker rejects equivalent valid programs; wins rely on leaking held-out truth; the model simply memorizes generator templates; or a deterministic inducer solves the application more cheaply. A narrow falsified reward is still a useful research output.

**Potential contribution:** a well-characterized reward failure and a testable correction, relevant to evaluation, post-training and verification research.

### Q3 — Can confidence guide action after the prompt and domain change?

**Papers:** R07, R08, R13, R14. **Hypothesis:** a calibration method improves error ranking and selective outcomes across domain/format/inference-budget changes at lower full cost than always using the strongest available system.

**First 30 days:** start from released outputs or an existing approved model. Use independent correctness labels and disjoint fitting/calibration/final-test splits. Compare verbalized confidence, self-consistency, a constant base-rate predictor, a simple post-hoc logistic/isotonic calibrator and supplied RLCR/CalibSFT outputs where available. Audit label and answer extraction errors.

**By 90 days:** evaluate risk–coverage, error-detection precision/recall, Brier score, AUROC and net cost on fresh formats/domains. Fit an escalation rule on calibration data only; include fallback errors, review and extra calls. If adapting a small specialist, compare unchanged small and larger baselines under the same evidence and schema, and include teacher-label generation.

**Kill criteria:** low ECE comes from a constant confidence with no discrimination; gains require the test distribution during calibration; labels come only from the same actor/teacher; or savings disappear after escalations and review. Do not infer a universal guarantee from a proper-scoring theorem or a nominal confidence interval under violated sampling assumptions.

**Potential contribution:** a calibrated operating policy and reproducible shift analysis. This is a stronger expertise signal than adding an unvalidated “confidence” field to JSON.

### Q4 — When should new information go into weights rather than retrieval?

**Papers:** R09–R12. **Hypothesis:** bounded adaptation plus replay offers a useful retention/cost tradeoff on a specific repeated workflow; it does not claim open-ended self-improvement.

**First 30 days:** reproduce the linear/Gaussian accumulation-versus-replacement calculation on CPU. Then define a small synthetic document world with genuinely new random facts, explicit later corrections and independent questions. Keep group/time separation. Compare fixed-model retrieval, long context and a simple external memory; these are strong baselines, not preliminary throwaways.

**By 90 days:** if approved compute permits, add a small weight-update or adapter method and replay. Measure incorporation, prior-fact retention, incorrect carryover after corrections, tail facts, transfer questions, total training/inference cost and rollback behaviour after sequential updates. Match both data volume and training steps, since accumulation can buy gains through more compute.

**Kill criteria:** new knowledge was already in pretraining; retrieval dominates on cost/quality; gains vanish beyond a handful of edit tasks; earlier skills degrade materially; or the method requires downstream labels unavailable in the real use case. If weight updates lose, the result still identifies a useful architecture boundary.

**Potential contribution:** a transparent retention/economics study and a justified adaptation policy, relevant to model-memory research and production knowledge systems.

## Foundations, degree and time constraints

Before attempting post-training research, demonstrate that you can implement and debug a simple gradient-based learner, distinguish sampling noise from an effect, maintain a clean data split and explain how the objective can be gamed. Useful foundations are probability/statistics, linear algebra, optimization, supervised learning, policy gradients, tokenization/decoding, experimental design and software reproducibility. Formal-proof projects add logic and the relevant proof-assistant environment.

The evaluation-only and toy-mechanism slices above can be credible first research contributions without a PhD. That is not a statement that every target lab hires without one. Research-scientist positions may require a doctorate/publication record; a research-engineering path often emphasizes implementation and independent experimental evidence. Exact roles, programmes and geographic constraints are in the round2 directory and labor track. A 90-day portfolio cannot substitute for a role's 5 years of distributed systems or model-training ownership.

For a working developer, original research should start with a question whose answer could be **no**, a strong simple baseline and an artefact another person can inspect. Readings should support that experiment. Completing every paper on this list is not a prerequisite to starting one tractable slice, and none of the projects assumes purchasing a large cluster.

## Official professional/lab channels attached to mechanisms

These are public research discovery channels, not an outreach list. No personal contact information is copied and no messages have been sent.

- **R01:** Google DeepMind/UC Berkeley authors, with [paper](https://arxiv.org/abs/2408.03314) and [DeepMind careers/research route](https://deepmind.google/careers/). Relevant branch: adaptive inference/evaluation, Q1.
- **R02:** Edinburgh/UCL/Anthropic-linked author team; [official project/repository](https://github.com/safety-research/inverse-scaling-ttc) exposes issue and contribution channels. Relevant branch: reasoning evaluation, Q1.
- **R04:** Tsinghua LeapLab/SJTU team; [official project](https://limit-of-rlvr.github.io/) names researchers and links code. Relevant branch: RL exploration/coverage, Q2.
- **R05:** Andre He, Daniel Fried and Sean Welleck, Carnegie Mellon; [official artefact](https://github.com/AndreHe02/rewarding-unlikely-release). Relevant branch: formal-model RL, Q2. Institution affiliation alone does not grant compute or supervision.
- **R06:** TU Darmstadt/hessian.AI/DFKI and collaborators; [paper author/affiliation record](https://arxiv.org/html/2604.15149v1). Relevant branch: logical verification and reward design, Q2; release/contact details still need further inspection.
- **R07:** Apple/Oxford-linked author work; [primary publication record](https://proceedings.mlr.press/v267/busbridge25a.html). Relevant branch: teacher/student efficiency, Q3. No paid placement or access claim.
- **R08:** UC San Diego authors Ivan Yee Lee, Loris D'Antoni and Taylor Berg-Kirkpatrick; [official code](https://github.com/ivnle/the-format-tax). Relevant branch: model-interface evaluation, Q1/Q3.
- **R11/R13:** MIT CSAIL authors and [SEAL](https://github.com/Continual-Intelligence/SEAL) / [RLCR](https://rl-calibration.github.io/) official projects. Relevant branch: adaptation and uncertainty, Q3/Q4. Public code is separate from admission, lab membership or mentoring.
- **R12:** Google Research/Cornell-linked author work; [official research account](https://research.google/blog/introducing-nested-learning-a-new-ml-paradigm-for-continual-learning/). Relevant branch: multi-timescale learning, Q4; complete reproducibility route not yet established.
- **R14:** SUSTech-linked ML/statistics team; [official Apache-2.0 project](https://github.com/ml-stat-Sustech/verbalized-confidence-training). Relevant branch: calibrated post-training, Q3. Current preprint claims need replication.

## Priority gaps and next falsifiers

1. Recompute statistics from released outputs before trusting headline percentages; current pass is source/method inspection, not a replication.
2. Read the final ICLR version of R01 and final TMLR version of R02 alongside the audited arXiv versions; check whether material method/budget changes alter these caveats.
3. Audit R14's rollout/sample-grid and GPU/wall-time arithmetic, task split independence, label quality and held-out calibration. Include no-training baselines and the dominant data-generation cost.
4. Verify exact model/data licences, checkpoints and environment pins for any chosen project. Repository code permission does not automatically license every training example or base model.
5. Inspect R09's correction and trace its precise public experiment release. Check R10's final reviewed version if accessible, especially minor-feature/tail results and compute-matching.
6. Seek robust genuinely fresh held-out tasks, including unsuccessful results, rather than another improvement on a public saturated benchmark. MATH-Beyond's [ICLR 2026 benchmark](https://proceedings.iclr.cc/paper_files/paper/2026/hash/6fdf57c71bc1f1ee29014b8dc52e723f-Abstract-Conference.html) is a useful candidate to audit, but its model-conditioned task selection and source-dataset exposure need examination.
7. Test whether any advantage survives base-model upgrades and simpler native platform support. A project should be abandoned commercially when its added complexity no longer buys a meaningful outcome.
8. Keep the career inference conditional: competence in designing and validating these mechanisms is useful across roles, but no paper proves that owning today's custom training recipe is a permanent moat through 2031.
