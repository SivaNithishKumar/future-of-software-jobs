# Robot demonstration data: transfer is real; access is a separate contract

**Open X-Embodiment reports useful real-robot transfer, but it does not establish transfer to an unseen robot or a hardware-free reproduction of that result.** A common data format is not a common physical action meaning, and an “open” aggregate is not a blanket code/data/model licence. This pass closes a bounded source-method question and leaves asset, physical-reproduction and paid-access gates open.

The study was selected before new calls. The held census contained DROID metadata and DROID-trained policy evaluations, but no named Open-X methods audit in the queried notes/catalogues/index. This is a bounded census, not archive-wide absence. Exactly three new primary surfaces were read: [arXiv metadata](https://arxiv.org/abs/2310.08864), [exact v9 methods](https://arxiv.org/html/2310.08864v9) and the [official collection/project overview](https://robotics-transformer-x.github.io/). The metadata dates v9 to 14 May 2025 and first submission to 13 October 2023. This is historical evidence, not a 2026 frontier ceiling or a matched current data-release manifest. Same-page text windows are disclosed separately; no fourth source, dataset sheet or code/model asset was opened.

## Keep the populations separate

| Reported unit | What it describes | What it does not establish |
|---|---|---|
| 1M+ trajectories; 60 datasets; 22 embodiments | The expanded pooled collection, from 34 research labs | Frames, hours, successful attempts, operators or 22 individual machines |
| 21 institutions; 527 skills; 160,266 tasks | Reported collaboration/annotation-level aggregates | One common institution/lab unit, independent task trials or verified task deduplication |
| Nine manipulator embodiments from 12 named datasets | The actual experimental training mixture | Use of every released dataset or all 22 embodiments |
| 3600 evaluation trials across six robots | Overall reported physical evaluation | Per-cell attempt counts, success count or six held-out new embodiments |

The paper explicitly says the collection grew after the training experiments. Institution, lab, author-affiliation and embodiment counts are different units. Dataset composition is uneven: the text describes Franka's broad scene diversity and the caption notes large xArm/Google trajectory contributions. Exact figure-bar values were not recomputed. [v9 §§III–V](https://arxiv.org/html/2310.08864v9).

No complete collection-attempt manifest was inspected. The 1M+ figure must not become “one million successful teleoperated demonstrations.” Collection modes, failed/aborted/cancelled attempts, operator experience, resets and privacy/consent handling may differ across constituent datasets. Those distributions were not established. Trajectory lengths, frame counts and collection hours were not recovered; the paper's 3–10 Hz is inference rate, not a dataset recording clock. There is no leakage accusation or inference that unreported attempts were hidden.

## Format portability is not physical portability

RLDS/tfrecord supplies a useful common storage structure while accommodating different sensors and action spaces. The studied policies choose one canonical camera view, resize it and normalize actions by dataset. The exact methods state that coordinate frames are **not aligned** across datasets and actions may mean absolute/relative positions or velocities. The same seven-dimensional vector can therefore imply different motion. [v9 §IV-A](https://arxiv.org/html/2310.08864v9).

The overview's simpler gripper-frame description is not enough to settle a chosen converter's units, reference frame, control mode or normalization. This is a specification/granularity join to resolve, not a proven paper contradiction or faulty converter. No converter code or calibration files were read. A seven-number schema passing validation would not alone prove safe portability.

At the same time, the positive policy result is a counterweight to assuming every representation difference must be hand-engineered away before learning can help. A sufficiently capable model can use heterogeneous experience productively. The source does not isolate embodiment identity from every change in data quantity, visual diversity, task mix or pretraining.

## Transfer, controls and counterevidence

RT-1-X reportedly beats the original per-dataset method on four of five small-data domains, with a reported mean relative improvement around 50%. Its same-architecture RT-1 comparator helps assess co-training. That result should remain positive and scoped, rather than becoming a universal 50-point gain.

The strongest printed skill-transfer contrast uses the 55B RT-2-X: 75.8% versus 27.3% for RT-2; removing Bridge drops it to 42.8%. The evaluated Google Robot was already represented in training. These skills/objects were absent from its RT-2 dataset but present in another robot's Bridge data. This supports skill transfer **onto a represented embodiment**, not zero-shot deployment on a new robot. The paper expressly says it does not study generalization to new robots or very different sensing/actuation modalities. [v9 TableII and §§V-B–VI](https://arxiv.org/html/2310.08864v9).

The other visual-generalization axis is roughly unchanged: 62% for RT-2 versus 61% for RT-2-X. Printed large-data TableI also supplies useful negative evidence:

| Setting | RT-1 | RT-1-X | RT-2-X 55B |
|---|---:|---:|---:|
| Bridge / Stanford IRIS |40%|27%|50%|
| Bridge / Berkeley RAIL |30%|27%|30%|
| Google Robot, six skills |92%|73%|91%|

Thus the smaller multi-robot policy loses to per-robot RT-1 in all three printed settings; the larger policy does not strictly win every comparison either. The actual cells qualify generic outperformance prose. No per-cell N, intervals, paired-trial significance or corrected score is inferred. Own arithmetic gives 75.8/27.3 ≈ 2.78, consistent with the authors' approximate 3× description, not a reporting error.

Per-domain evaluations use the respective publication robots/setups, but exact hardware calibration, control backend, run/reset/operator lineage, acceptance labels and intervention time were not acquired. RT-1 is 35M and runs locally; RT-2 uses 5B/55B web-pretrained models and cloud-hosted inference. That is substantive model/resource context, not laptop parity or an entitlement to the matching 55B model/service. Physical task success does not automatically supply intervention-free useful work.

## Rights and an accessible reproduction tier

The exact article displays CC BY 4.0. That covers the article, not every inherited dataset, code dependency, checkpoint, model pretraining source or service. The project overview links a per-dataset sheet and collection-enrollment route, but displays no complete constituent licence, privacy or commercial-use terms in the inspected text. Those links were not followed under the three-surface cap. No blanket commercial permission—or blanket noncommercial prohibition—is inferred.

The paper announces RT-1-X and selected resources/checkpoints; no immutable code/model/data-card/release bundle was matched here. No rights-cleared bounded trajectory/byte subset was established in this pass, which does not mean none exists. The immediately completed device-free work is source/version/population and printed-table checking. It is not reproduction of the physical-transfer result.

Stronger reproduction would separately require exact selected assets and grants, action/camera/calibration semantics, a matched runtime/controller, authorized target hardware/operator, independent task-success/allowed-effect truth and an all-attempt reset/intervention/resource ledger. Public access to a dataset cannot supply those automatically. The official page's technical-bug and enrollment links are professional discovery, not a response promise, contribution acceptance, work right or permission to submit; no channel or form was used.

## Project and career disposition

**No exact existing project/cap is attached.** State 18/19's clock/frame/OpenVINS contract is not an RT-X training or robot-evaluation arm, and a SAFE/other project cannot be relabeled to absorb this work. Related geometry, provenance, data engineering and evaluation fundamentals may transfer only if already demonstrated. No new hardware arm, exercise, course, hours, credential or canonical route is created.

A native per-robot policy, converter or mature loader may already meet the legitimate need. Without a measured residual and an actual receiver, the paper does not establish a custom data-platform business or paid work. If terms, runtime, physical observation or receiving access cannot close, retain the source-only result. This is an exploration gap, not a failed developer or a forecast of robot job volume.

Twenty-five source-anchor, table-arithmetic and input checks passed; all seven census inputs stayed exact. No dataset, frame, video, code, model, weights, package, robot, cloud account, private system or physical experiment was acquired or run. Source/index files remain frozen. Different review and ROOT disposition are pending; no source-world, hardware, rights, role or personal-readiness acceptance is claimed.
