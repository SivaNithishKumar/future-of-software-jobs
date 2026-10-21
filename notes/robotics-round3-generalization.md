# Robotics round 3: generalization, measurement and reproducible entry projects

Research cutoff: 19 October 2026. This pass concerns robot policies and evaluation methods, not deployment totals or company economics. It distinguishes peer-reviewed work, preprints, author-reported experiments, artifact availability and experiments proposed here. No packages, code, weights or datasets were installed/downloaded, and no model, simulator or physical robot was run. Public professional channels are research leads only; no outreach occurred.

## Finding: neither a giant model nor a typed architecture settles the question

Some learned policies now transfer behavior that previously required task-specific perception, motion programming or specialist training. That is real contrary evidence against assuming all valuable robotics engineering must preserve a hand-authored world state and skill for every behavior. Yet generalization is multidimensional, and the available tests remain far from interchangeable. A useful engineer must identify the actual shift, distinguish partial progress from completed work, trace the evaluation protocol and compare a simple solution under the same inputs and budget.

The practical opportunity is therefore **measurement, adaptation and constrained execution with access to the necessary artifacts**. It should not be justified by a claim that learned end-to-end control cannot work. Learned models may absorb parts of the integration work; they also create new questions about training distribution, calibration, runtime behavior and the validity of success signals.

## What "generalization" means in the studies

| Axis | A valid held-out test | What does not establish it |
| --- | --- | --- |
| Visual robustness | New lighting, textures, distractors, camera pose or sensor noise while preserving a feasible task | A new seed that reuses the same narrow appearance distribution |
| Spatial/dynamics robustness | Changed object placement, robot initial pose, mass/contact conditions or timing | Different words for an identical trajectory |
| Semantic grounding | Same scene with instructions that require genuinely different targets or relations, scored against the changed goal | Ignoring paraphrases or blank text while still completing the original task |
| Task composition | A combination/order of known skills held out from training, with full workflow success | Each atomic skill succeeding separately |
| Environment transfer | A separate scene/site, with controlled task and interface correspondence | Held-out task names evaluated in training kitchens |
| Embodiment transfer | New robot kinematics/sensors/action space, declaring all adaptation data | No data for a particular task on a robot that is otherwise represented in training |
| Long-horizon execution | Correct conditional steps, memory, recovery and completion under a declared horizon | A short task with many controller ticks or a partial-progress score |
| Sim-to-real predictivity | Paired policies/tasks/trials in simulation and reality, preserving decisions and failure patterns | A photorealistic image or a simulator's published correlation on another policy family |

These distinctions are analytical categories used in this report. Some papers use "compositional" for combinations of perturbations; others mean composition of task skills. Those claims must not be collapsed into one metric.

## Method audits and contrary evidence

### 1. A tiny policy can expose what a benchmark rewards

**MINERVA, arXiv:2609.03715v1, 3 September 2026, preprint.** A 0.54-million-parameter CNN with task-ID conditioning reports about 95% success on standard LIBERO without language understanding. The released one-pass regression variant reports 95.75%. This is a closed-set test: it cannot execute unseen instructions. A three-seed comparison found flow matching's gain over direct regression inside seed variability. Under LIBERO-Plus perturbations, scores fell to roughly 46–56%, with particularly poor photometric robustness. The authors explicitly identify the π0.5 comparison as a reference using a different rollout budget, not a protocol-matched statistical test. [Paper methods and limitations](https://arxiv.org/html/2609.03715v1)

**Implication:** a high standard-LIBERO result does not by itself justify a large language backbone, and a small learned controller can replace explicit hand-coded geometry for a fixed benchmark. This is not evidence that language or large-model pretraining is useless for novel tasks. The useful next comparison is the robustness/latency frontier under a declared deployment distribution, not parameter count alone.

### 2. World-action models provide real evidence for implicit learned control

**DreamZero, arXiv:2602.15922v1, 17 February 2026, preprint.** The model predicts future video and actions jointly. On unseen DROID-Franka tasks it reports **49% task progress but 22.5% full success**, versus 12.5% full success for GR00T N1.6 and 7.5% for π0.5. Baselines are adapted on the same robot datasets, although pretrained knowledge and backbone architectures differ. Main embodiments are trained separately. Its reported 7 Hz optimized action-chunk generation uses two GB200s; limitations include six-second visual memory and difficult high-precision tasks. [Original study](https://arxiv.org/html/2602.15922v1)

**Contrary evidence:** useful physical transfer need not require an explicit object graph or hand-authored symbolic transition model. **Limit:** future-video consistency can also produce coherent wrong actions; the paper attributes many failures to video-generation errors. A predicted world is a hypothesis about the physical world, not a sensor observation or a certified safety constraint.

### 3. Language coaching can reduce new motor demonstrations, but "zero-shot" needs qualification

**π0.7, company technical release, 16 April 2026.** It combines multimodal conditioning, visual subgoals and diverse robot/autonomous data. In the air-fryer example, an initial zero-shot attempt did not finish; stepwise language coaching improved behavior, and a subsequently trained high-level policy generated subtasks autonomously. The authors found related air-fryer episodes in the training corpus. They also report transferring laundry folding to UR5e without task-specific laundry demonstrations on that embodiment. [Release with disclosed training-overlap caveats](https://www.pi.website/blog/pi07)

This is evidence for reducing task-specific programming/data collection. It does not imply zero relevant prior data, no adaptation, no high-level training or arbitrary embodiment transfer. The interesting skill is specifying what behavior should transfer and verifying it, rather than assuming every task needs a new deterministic skill or that one prompt solves it.

### 4. Human corrections and classical low-level control coexist with strong learned behavior

**HIL-SERL**, Luo, Xu, Wu and Levine; Science Robotics 2025, DOI `10.1126/scirobotics.ads5033`; original [arXiv:2410.21845](https://arxiv.org/abs/2410.21845). The study reports near-perfect performance on its dexterous tasks after approximately 1–2.5 hours of online training, outperforming imitation baselines with matched human-data budgets. This is per-task learning, not a general model completing arbitrary unseen tasks. [Author paper](https://hil-serl.github.io/static/hil-serl-paper.pdf)

The system first trains a binary reward classifier from positive/negative examples, seeds a demonstration buffer and uses corrective human interventions during online learning. These are valuable supervision, not autonomous hours to be omitted from the accounting. The paper's contact-task real-time layer uses impedance control with reference limiting. [System overview](https://hil-serl.github.io/)

**Implication:** learned policies can outperform hand-scripted delicacy without eliminating the need for reward validation, safe hardware interfaces and clear human-intervention records. A successful final policy should be evaluated separately from its assisted training runs.

### 5. Robustness benchmarks reveal shortcut use, not automatically illicit contamination

**LIBERO-PRO, arXiv:2510.03827v2, revised 25 May 2026.** It varies objects, positions, semantics, task targets and environments. Standard-trained models can continue familiar motions after instructions or targets change. The official code describes a configurable perturbation protocol. Its results diagnose reliance on the narrow training/evaluation setup; they are not proof that the authors of every tested model secretly used a forbidden test set. [Paper](https://arxiv.org/abs/2510.03827v2), [official repository](https://github.com/RLinf/LIBERO-PRO)

**LIBERO-Plus**, accepted CVPR 2026 version, tests seven perturbation dimensions, including camera, initial pose and sensor changes. It separately examines blank instructions and replacement targets, and co-occurring perturbations. Its broad conclusions refer to its tested models/protocol; later models must be re-evaluated rather than inheriting a permanent failure label. [Peer-reviewed paper](https://openaccess.thecvf.com/content/CVPR2026/papers/Fei_LIBERO-Plus_A_Progressive_Robustness_Benchmark_for_Visual-Language-Action_Models_CVPR_2026_paper.pdf), [benchmark source](https://github.com/sylvestf/LIBERO-plus)

**Audit rule:** log separate outcomes for visual invariance and instruction selectivity. A policy that ignores both harmless paraphrases and meaningful goal changes is not demonstrating robust language understanding.

### 6. Simulation rankings need validation on the intended policy/task family

**SIMPLER**, CoRL 2024, [arXiv:2405.05941](https://arxiv.org/abs/2405.05941), uses paired simulation/real tests and visual/control matching to evaluate policy ranking. It found validation action MSE to be a poor proxy for real task performance. Its scope emphasizes common robot setups and relatively tractable manipulation dynamics. [Author paper](https://jiajunwu.com/papers/simpler_corl.pdf)

A **June 2026 preprint**, Wang et al., [arXiv:2606.10366v1](https://arxiv.org/html/2606.10366v1), compares five newer VLAs on nine aligned tabletop tasks. It reports 11,800 simulated and 1,115 real rollouts, but each individual policy/task/perturbation condition uses only five real rollouts. Average Pearson correlations are 0.402 for SIMPLER and 0.785 for REALM in this setup. Modest simulator adaptation improves alignment; more adaptation does not monotonically help. The authors limit conclusions to the tested embodiment and tasks.

**Implication:** the old and new results need not conflict. Correlation belongs to a simulator-policy-task-distribution combination. Fine-tuning on target simulator demonstrations is adaptation and must not be relabeled zero-shot testing. Report both rank mistakes and absolute score calibration; small per-cell real samples can leave uncertain rankings despite a large aggregate count.

### 7. Success detection needs failure coverage and an independently defined target

**RoboReward, arXiv:2601.00675v2, 8 January 2026, preprint.** Because its source demonstrations are success-heavy, the authors create negative examples by changing instructions and clipping successful videos, alongside organic RoboArena failures. The benchmark has task-description-disjoint splits and 2,831 human-verified examples. Human verification is performed by one annotator shown the proposed score and an automated rationale. Its trained reward models improve short-horizon RL, but long-horizon reward assignment remains open. [Full protocol](https://arxiv.org/html/2601.00675v2)

**Research questions, not established defects:** do parent-video, scene and equipment identifiers remain disjoint after augmentation; do synthetic near-misses cover actual off-policy failures; and how often does the model incorrectly declare completion? A low average error on ordinal progress labels is not identical to a low false-completion rate. Showing labels/rationales to annotators can create anchoring, so a blinded relabeling subset would be a useful extension.

### 8. Orchestration can matter even with the same planner and motor primitives

**PyRUA-Lean, arXiv:2610.01939**, v1 issued 1 October and v2 revised 13 October 2026, preprint. The 700-instance comparison uses the same GPT-6 Astra planner and underlying primitive library: Python composition raises success from 63.1% to 71.7% relative to tool calling. The 65% input-token reduction is reported on instances both methods solve; it must not be substituted for cost across all attempts. The v1 protocol has one run per agent/instance and no physical-robot test. [Audited v1 protocol and limitations](https://arxiv.org/html/2610.01939v1), [current release and source](https://github.com/DAGroup-PKU/PyRUA-Lean)

This supports the value of local checks, retries and selective feedback. It does not isolate those mechanisms individually, establish robustness across planners, or compare against every classical control alternative. Its later release's additional claims require their own versioned replication.

## What the studies actually compare

| Study | Comparison supported | Comparison not established |
| --- | --- | --- |
| MINERVA | Small regression/flow policies and chunk strategies under its fixed-task protocol | A small closed-set task-ID policy versus general language understanding under equal open-world tests |
| DreamZero | Video/action joint modeling versus specified adapted VLA baselines | Beating an optimized classical planner on every task, or a universal policy across embodiments |
| HIL-SERL | Human-assisted RL versus named imitation/RL baselines on the chosen physical tasks | Broad unassisted task generalization or zero engineering around real-time control |
| SIMPLER / Wang et al. | Whether simulated measurements preserve real-world rankings in declared setups | A simulator's universal correctness or a simulator-only safety certification |
| PyRUA-Lean | Complete execution interfaces using the same planner and primitive stack | The isolated causal contribution of memory, code composition, perception or extra local retry opportunities |
| RoboReward | Reward-label quality and downstream policy improvement in its evaluated tasks | Perfect success detection on arbitrary multi-stage tasks or novel failure distributions |

For a proposed model/classical/hybrid comparison, giving only the classical agent privileged simulator poses invalidates a fairness claim. It is still a useful **oracle upper bound** if labeled explicitly. A realistic classical baseline must receive the same camera/proprioceptive inputs and account for its perception/calibration errors.

## Minimum protocol ledger and failure budget

Before running, freeze parent episode IDs, task families, object assets, scenes, camera calibration, initial-state sampler, simulator/controller versions, checkpoint hashes, action normalization/frame, reset method, horizon, training/adaptation demonstrations, retry/compute budgets and success rubric. Track frames, action chunks, episodes and human sessions as different units.

Do not split adjacent frames or counterfactual labels of the same parent video across training and test. Keep calibration separate from final testing. Validate changed goals and reachable layouts; do not score an impossible perturbation as a model failure. Record any operator intervention, aborted rollout and reset rather than deleting them from the denominator.

Measure full-task completion, progress, false completion, missed failures, recovery latency, retries and useful throughput. Add end-to-end sense-to-act p50/p95/p99 latency and deadline violations, not only neural forward time. Stable repeated actions or low sampling entropy can still be confidently wrong.

For long tasks, report completion of the whole sequence. The exact chain rule involves success conditional on all previous successful steps; it is invalid to exponentiate an unqualified marginal atomic-skill score and call it an observed workflow reliability estimate.

Proposed simulation gate: no forbidden action bounds, no accepted stale response after timeout, no use of scoring-only oracle state and no hidden assisted completion. Zero violations in 200 independent episodes would still leave a one-sided 95% binomial upper bound of about **1.49%**; shared scenes/policies can make independence questionable. This statistical illustration is not a physical-safety claim or an industrial acceptance threshold.

## Artifact audit for an achievable replication

### Best inexpensive starting point: MINERVA on a pinned finite task set

- **Code snapshot:** inspected commit [`64c3cc8be364eb62df4f9fdc4bdccb1be9d1118e`](https://github.com/k1000dai/MINERVA/commit/64c3cc8be364eb62df4f9fdc4bdccb1be9d1118e); code declares Apache-2.0. This is a research fork, not an official LeRobot release.
- **Checkpoint:** `k1000dai/MINERVA`, revision `1b4fb1743f00a7d8eb87c7059c446447907d12bf`, directory `t05_l1_0.54M`; official [model card](https://huggingface.co/k1000dai/MINERVA) declares Apache-2.0 and no physical-robot validation.
- **Data:** `lerobot/libero`, revision `a1aaacb7f6cd6ee5fb43120f673cebb0cfea7dd4`. Its [pinned dataset card](https://huggingface.co/datasets/lerobot/libero/blob/a1aaacb7f6cd6ee5fb43120f673cebb0cfea7dd4/README.md) declares Apache-2.0, whereas original LIBERO declares its dataset CC BY 4.0. These are distinct publisher declarations, not a conclusion that repackaging removes upstream terms. The card records 1,693 episodes, 273,465 frames and 40 tasks.
- **Renderer/runtime:** MuJoCo `3.3.2`; the release says renderer changes affect this scratch-CNN model. Linux, Python `>=3.12,<3.14`, approximately 15GB RAM for the complete four-suite evaluation; a policy-inference GPU is optional, while renderer support must be checked. [Source requirements](https://github.com/k1000dai/MINERVA), [pinned artifact manifest](https://github.com/k1000dai/MINERVA/blob/64c3cc8be364eb62df4f9fdc4bdccb1be9d1118e/ARTIFACTS.md)

The small policy's CPU timing is not the same as an end-to-end renderer/robot timing guarantee. Full benchmark replication still requires an environment setup and permission for dependencies; none was performed here.

### Alternatives and blockers

| Artifact | Access/license and practical boundary |
| --- | --- |
| LIBERO-PRO | [Official source](https://github.com/RLinf/LIBERO-PRO) declares code MIT and data CC BY 4.0. Pin the selected object/position/task perturbations and initialization files; different subsets are not a shared leaderboard denominator. |
| LIBERO-Plus | [Assets](https://huggingface.co/datasets/Sylvest/LIBERO-plus/tree/main) declare MIT and total about 6.4GB. A top-level license was not visible in the inspected code listing, so do not assume all source and third-party assets share the dataset-card license. |
| DreamZero | [Code](https://github.com/dreamzero0/dreamzero) declares Apache-2.0 and minimum two-GPU distributed inference, tested on GB200/H100. The [DROID checkpoint](https://huggingface.co/GEAR-Dreams/DreamZero-DROID) declares **CC BY-NC 4.0**. Released inference examples report different latencies from the paper's maximally optimized Flash path. This is a research comparison requiring serious compute/access, not the default laptop experiment. |
| HIL-SERL | [Source](https://github.com/rail-berkeley/hil-serl) declares Apache-2.0 and provides real-Franka infrastructure. GPU/JAX, suitable physical robot, operator supervision, rewards and resets are required for physical replication. It is inappropriate to promise a no-hardware replication of the main result. |
| RoboReward | [Dataset](https://huggingface.co/datasets/teetone/RoboReward) and [8B model](https://huggingface.co/teetone/RoboReward-8B) declare CC BY 4.0; source corpora and base model have separate terms. The 8B model files total roughly 17.6GB; required runtime memory depends on video sampling and has not been verified here. Use a permitted subset and declared inference configuration before scaling. |
| PyRUA-Lean | [Source](https://github.com/DAGroup-PKU/PyRUA-Lean) declares Apache-2.0; its full stack also depends on primitive/simulation components and planner access. Hosted inference would require credentials and approved spending. A model-independent local baseline can be studied first. |

## Original extension candidate A: the grounding-versus-robustness frontier

This is a proposed study, not a claim of novel results. Its publication novelty would require a focused related-work review after reproduction.

**Question:** can a small model retain finite-task efficiency while becoming robust to visual/spatial changes, and does a larger language-conditioned policy change behavior correctly when the requested target changes?

**First 30 days, after authorization for setup:** reproduce the pinned MINERVA 2,000-rollout protocol and retain its failures. Verify actual memory and end-to-end latency locally. Build a shortcut control that replays a training action sequence without images, and an oracle geometric controller for a few simple tasks as an explicitly privileged reference. The important sanity check is that the evaluator can distinguish a genuine changed target from the original target; no benchmark score should rise because its goal checker stayed unchanged.

**Held-out design:** keep the original training set fixed. Select ten representative existing tasks before tuning. Use five conditions: nominal; new evaluation initial states; camera shift; lighting shift; and joint camera/layout shift. Reserve additional perturbation magnitudes and combinations for the final test. Use twenty fixed episode seeds per condition/task, totaling 1,000 episodes per model. Report each axis separately rather than averaging away failure modes.

**Days 31–90:** compare the released small model, a lightly augmented retraining under three training seeds and a compatible language-conditioned baseline with matched adaptation data. For language selectivity, use a separate paired-scene assay with two valid goals from the known task set. Map MINERVA's valid task IDs explicitly; do not pretend it understands novel text. Add a realistic RGB-based geometric baseline only if its perception pipeline is included and feasible.

**Metrics and decision gate:** task-stratified completion intervals, meaningful-goal-change selectivity, invariance to harmless paraphrases for language models, joint-perturbation degradation, full-stack latency/deadline failures and compute/memory. Require any claimed robustness gain to survive held-out combinations and training-seed variability while preserving nominal performance within a predeclared two-percentage-point tolerance. A regression that invalidates task semantics stops the run. If a replay-only baseline nearly matches the nominal policy, the nominal benchmark is an inadequate demonstration of perception.

**Why useful to an employer:** it demonstrates artifact discipline, computer vision/ML evaluation, latency measurement and falsifiable judgment. **Kill criteria:** no reproducible baseline, renderer mismatch explains the gain, test perturbations influenced tuning, extra privileged state favored one method, or augmentation improvements vanish outside one scene family. A clean negative result can still be a strong portfolio artifact.

## Original extension candidate B: false completion under natural and synthetic failure

**Question:** does a general reward model reliably distinguish a completed task from a plausible-looking near miss, especially when instruction, object or temporal context changes?

**First 30 days:** audit a permitted small RoboReward subset and preserve parent-video identity across all splits. Reproduce a published prompt/configuration on ordinal labels before creating new variants. Compare the model with constant-score, final-frame-only and simple progress heuristics; these are controls, not competitive general robotics solutions. Measure sampling, preprocessing and video-duration effects rather than assuming the model-card label alone reproduces a result.

**Days 31–90:** construct a held-out, blinded-adjudication subset of natural failures, clipped successes and same-video/different-goal pairs. With authorized human participation, obtain independent labels before showing model outputs, then record disagreement. Hold out parent scenes/tasks where metadata permits. Analyze whether a threshold selected only on calibration data meets a declared false-completion budget, and report the coverage/abstention trade-off and uncertainty. Do not reuse the same VLM as both the sole label generator and final judge.

**Metrics:** false-completion rate, missed completion, ordinal MAE, task/embodiment subgroup error, abstention and inference cost. A useful outcome is knowing when the scorer must abstain or request another sensor view. **Kill criteria:** the relevant physical state is unobservable from the videos; labels cannot be independently justified; apparent success comes from parent-episode leakage; or simple baselines equal performance at the chosen error budget.

This route needs less robotics hardware than policy learning, but access to real failure coverage and trustworthy labels is its main constraint. It complements, rather than duplicates, latent-feature failure detection: a black-box video scorer and a white-box policy probe observe different failure signals.

## Authors, groups and professional channels linked to the branches

Current employment/admission availability is not inferred from paper authorship. These are public research channels and prerequisite maps, not messages sent.

| Branch | People/group and primary channel | Prerequisites / reason relevant |
| --- | --- | --- |
| Tiny visuomotor models and capacity measurement | Kohei Sendai, Tatsuya Matsushima, Yusuke Iwasawa; Matsuo-Iwasawa Lab, University of Tokyo. [Paper with institutional author contacts](https://arxiv.org/html/2609.03715v1); [Matsushima professional contact](https://t-matsushima.com/contact/) | PyTorch/CNNs, imitation learning, action chunks, temporal sampling and experiment statistics; direct source of the inexpensive baseline |
| Robustness and language selectivity | LIBERO-PRO authors including Xueyang Zhou and Pan Zhou, HUST; [official project/repository](https://github.com/RLinf/LIBERO-PRO) and public issue channel | Benchmark configuration, valid goal changes, task/asset splits and policy/action interfaces |
| Seven-axis perturbation design | Senyu Fei, Siyin Wang, Junhao Shi, Jingjing Gong, Xipeng Qiu and collaborators; Fudan/Tongji/Shanghai Innovation Institute. [Accepted paper author block](https://openaccess.thecvf.com/content/CVPR2026/papers/Fei_LIBERO-Plus_A_Progressive_Robustness_Benchmark_for_Visual-Language-Action_Models_CVPR_2026_paper.pdf), [public issue channel](https://github.com/sylvestf/LIBERO-plus/issues) | Geometry and rendering, sensor/camera changes, factorial designs; paper lists corresponding institutional emails |
| Sim-real validity | Shuo Wang, Yingdong Hu, Fanqi Lin, Yang Gao; Tsinghua IIIS / Shanghai Qi Zhi Institute. [Paper contacts](https://arxiv.org/html/2606.10366v1); [official Yang Gao profile](https://people.iiis.tsinghua.edu.cn/~gaoyang/) | Calibration/control alignment, paired experiments, rank metrics and uncertainty; paper provides corresponding professional email |
| Reward quality / false completion | Tony Lee, Andrew Wagenmaker, Karl Pertsch and Stanford/Berkeley collaborators. [Paper corresponding-author channels](https://arxiv.org/html/2601.00675v2), [HELM benchmark](https://crfm.stanford.edu/helm/robo-reward-bench/) | Video evaluation, negative data, annotation quality, calibration and downstream RL; avoid treating MAE as a safety metric |
| Real-world intervention-based RL | Jianlan Luo, Charles Xu, Jeffrey Wu and Sergey Levine; Berkeley EECS affiliation in the work. [Project and official Discord link](https://hil-serl.github.io/), [code issues](https://github.com/rail-berkeley/hil-serl/issues) | RL/SAC, demonstrations and replay buffers, impedance-control interfaces, reward classifier and real hardware supervision |
| Video/action joint models | DreamZero team, including Seonghyeon Ye, Yuke Zhu, Jim Fan and Joel Jang; [original paper](https://arxiv.org/abs/2602.15922v1), [source issue channel](https://github.com/dreamzero0/dreamzero/issues) | Video diffusion, dynamics, action alignment, distributed inference and large compute; checkpoint reuse constraints matter. Broader NVIDIA/HF institution mapping belongs to the software/AI research track. |

## What would change the career judgment

If general models consistently perform new task compositions and environments with independent success verification, little adaptation and acceptable runtime on inexpensive hardware, custom behavior programming will shrink. That is a plausible direction, not something to dismiss to protect a preferred architecture. Conversely, if apparent gains disappear under matched instructions, unseen failures and physical evaluation, there remains substantial demand for adaptation and test infrastructure.

For a broad engineer entering now, the strongest evidence is the ability to reproduce a result, explain what it does and does not test, build a simple counterexample and improve a declared failure mode without hiding cost or assistance. That skill remains useful across model-policy, classical and hybrid approaches; its value is demonstrated through measurements, not assumed from a job-title forecast.
