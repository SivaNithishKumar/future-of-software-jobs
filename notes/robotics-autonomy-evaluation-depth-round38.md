# Robot autonomy evaluation: one unresolved protocol gap, round 38

The new evidence supports some within-policy correction and a useful physical-policy ranking method. It does **not** establish low-attention autonomous recovery or useful work per operator-hour. This is an audit of one bounded study, not a ceiling on all October 2026 policies or an argument that learned policies cannot recover.

## Census and exact study

The saved work already covers MINERVA/LIBERO reset and horizon accounting, π0.7/DreamZero transfer, HIL-SERL human-assisted training, SAFE's no-intervention boundary and state/control/TD-MPC/crane questions. I did not repeat those methods scans. RoboArena appeared only as the provenance of RoboReward's organic failures; its evaluation/operator denominator had not been audited.

The selected study is **RoboArena: Distributed Real-World Evaluation of Generalist Robot Policies**, [arXiv:2506.18123v2](https://arxiv.org/abs/2506.18123), revised **29 November 2025**, originally submitted **22 June 2025**; DOI `10.48550/arXiv.2506.18123`. Atreya, Pertsch and Lee lead implementation/experiment work in its contribution statement. The paper lists Berkeley, Stanford and a wider international collaboration; these are paper-era affiliations, not current employment checks. No separate peer-reviewed conference version was verified.

I used one targeted discovery query and three deliberately opened primary endpoints: the arXiv record, [exact v2 full text](https://arxiv.org/html/2506.18123v2), and the official project page. Repeated windows/finds addressed the same paper. No policy, model, code, robot data, images or video assets were acquired or run.

## The physical protocol and its units

The paper reports seven learned DROID policies, seven universities, 612 pairwise comparisons and 4,284 all-policy rollouts. Evaluators choose tasks/scenes, receive randomly sampled policies with hidden identities, match within-pair initial conditions, and run to completion or timeout. Feedback includes maximum progress, preference and reasons. After each pair, the other five policies are scored for the reference ranking. A trained evaluator screens incoming policies for unsafe behavior. Appendix D includes a reported drop-and-regrasp retry; it also reports 11% preference/progress disagreement. [Protocol, system and experiments, §§3–5; Appendix D](https://arxiv.org/html/2506.18123v2).

The arithmetic is **612 × 2 + 612 × 5 = 4,284**, not 4,284 independent task/environment draws. The reference ranking expands the same comparison contexts across seven policies. “Hundreds of instructions,” dozens of scenes and 32 illustrated environments do not provide exact unique task, object or operator counts. These are author-reported physical trials; I did not inspect their video evidence or recompute dataset totals.

This is substantially stronger evidence than a selected promotional clip: there are many physical comparisons, blinded policy identity and an explicit matched initial-condition requirement. The study's target is policy ranking under its collected distribution. The additional policy evaluations make a useful reference for that target, rather than an independent customer-operating outcome.

## What remains unresolved about autonomous recovery

The drop/regrasp report is positive evidence of within-rollout correction. It would be wrong to erase it or claim that these policies cannot retry. But an example supplies neither the number of eligible recovery opportunities nor an intervention-free continuation rate, sustained usefulness or operator burden. The preference disagreement is not an intervention statistic.

A maximum-progress score and a preference answer different questions from stable accepted output. A preference can reward first-try or smoother behavior even when both policies receive the same progress score. Neither quantity alone identifies how much human setup, monitoring or assistance was required. The paper is not defective for targeting ranking; its metric should simply not be relabelled as an operating-autonomy metric.

The protocol explicitly requires human scene arrangement, matched initial conditions and feedback, and describes safety screening. It also describes cancellation after infrastructure timeout/crash/disconnection. The inspected text does not provide a complete offered/assigned/canceled-session tally or matched hands-on, monitoring, reset, teleoperation, safety-intervention and repair-time totals. The numeric timeout/retry policy in an immutable implementation was not inspected. These are **unknowns**, not evidence of concealed help, cherry-picking or one-to-one teleoperation. Experimental setup/reset burden is also not automatically the production workload.

All seven policies are DROID-finetuned. Reported out-of-box scene diversity remains a positive, but no exact train/eval scene/object/session crosswalk was obtained. Same platform or institution is not proof of leakage; diverse descriptions are not proof of disjointness either. Site/operator/task clustering and changing task selection matter when extending a rank into a deployment claim.

The comparison pool concerns learned action representations. Elo, Bradley–Terry and progress averaging are genuine ordinary **ranking** baselines; they are not classical robot-action or recovery controllers. The study therefore does not establish superiority over a competent state machine/controller under matched information, reset, operator and resource assumptions. Its artificial distribution-shift analysis is useful algorithm evidence, not another physical held-out deployment. [Methods and limitations, §§5–7 and Appendix B](https://arxiv.org/html/2506.18123v2).

## Release, replication and professional route

Algorithm 1 and Appendix B are a publicly available evaluation/ranking protocol. The rendered paper declares **CC BY 4.0**. That article grant does not clear code, rollout videos/data, policy checkpoints or dependencies.

The [official project link](https://robo-arena.github.io/) returned **zero extracted reader lines**. Within the three-endpoint cap, I could not verify an implementation repository, immutable code revision, current release, data/weight licence or operating-service access. This is not proof that the site or release is absent. No guessed GitHub URL, fourth endpoint, browser fallback or account was used. The paper's sponsored-credit/participation description is not a verified current allocation.

The paper and project URL are the public professional discovery route for the named team. Existing Berkeley RAIL context may be reused as institutional context, without merging RoboArena into HIL-SERL or claiming access to every affiliated lab. No new India/UK role, degree waiver, admission, employer requirement or response/funding commitment was verified.

The physical instantiation uses a DROID Franka/Robotiq/ZED setup, trained evaluation personnel and institutional hardware/environment access. Replicating that requires a selected supported robot/controller, calibration/action interfaces, server/runtime/model versions, separate rights and actual approved resources. A software trace audit instead needs event/state modelling, provenance/clock reasoning, complete-denominator joins and paired/clustered statistics. Neither route promises VLA mastery in thirty days, and no specific degree gate is invented from a paper.

## One narrow attachment to an existing artifact

Attach the following as optional evaluation context to **`physical-geospatial-round6.contributionpath.armada`**, `physical-geospatial-enrichment-round6.json#/records/157`. That is already the proposed operational mission failure-cost integration artifact. Keep its existing **40-hour first/120-hour total planning allowance**, first diagnostic and eight-hour setup/narrowing gate; add no project or hours and assume no completed probe.

The narrow question is whether its existing mission/error ledger can distinguish offered work, progress, accepted output and measured human assistance:

- Preserve offered, assigned, started, scored, canceled, aborted and unknown sessions, with parent trial, policy/version and task/site identifiers. Do not infer new environments from labels.
- Distinguish autonomous within-rollout retry, new episode, human reset, assistance and safety stop. A reset is not silently a successful recovery.
- Keep terminal acceptance and eligible failure opportunities separate from maximum progress/preference. Preserve incomplete and missing records in coverage.
- Record human engaged time only when measured, separately from monitoring/standby capacity and infrastructure clocks. Missing time is unknown; zero accepted outputs cannot yield a defined per-output cost.

This is a proposed schema/trace-to-metric diagnostic, **not implemented** RoboArena code or a policy evaluation. Within the existing first diagnostic, one lawful owned mocked trace can have independently specified healthy, failed, canceled and ambiguous expected outcomes. An always-complete or always-block result must fail the opposite cases. No RoboArena data, new model or hardware is needed for that limited contract question. Synthetic timestamps remain synthetic; they cannot establish saved paid labor.

For a stronger recovery claim later, predeclare eligible faults, accepted-output criteria, complete attempt/reset/assistance denominators, held-out task/site/operator coverage and a competent matched prior-policy or deterministic baseline. Actual operator attention and resource costs must be observed. A replay cannot establish physical recovery or safety.

The first falsifier is practical: the released framework may already capture these events. If a pinned schema/log audit shows complete coverage, use a query or documentation rather than invent another layer. If lawful complete records, independent expected behavior or a decision that changes cannot be obtained, retain a source/schema report. If apparent benefit depends on dropped failures, unequal hints or disabled native checks, reject it. If native behavior already meets the contract, stop custom novelty and preserve useful maintenance work.

## Boundary and retained evidence

Complete held-out physical failure trials with competitive total human attention per accepted output would strengthen the autonomy claim and could shrink this integration niche. No permanent human bottleneck, standalone product, job volume or 2031 demand follows from today's missing metric. Missing published workload accounting is an evidence gap, not a finding that low-attention recovery is impossible.

The companion JSON records exact version/source locators, denominator states, release/rights gaps, falsifiers and the proposed existing-artifact attachment. The source receipt contains selected rendered text, not raw HTML/PDF hashes. Only census/guard checks and static arithmetic were performed; no ranking algorithm, simulator, policy, robot, account or shared source was executed or changed.
