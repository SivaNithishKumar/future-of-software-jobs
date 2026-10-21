# Materials, computational chemistry and scientific ML software

Bounded specialist pass: 19 October 2026. Owner `/root/bio_science`. No installation, model/data download, simulation, DFT calculation, hardware work, outreach, private access or external mutation was performed. Earlier notes remain unchanged. This pass deliberately excludes the A-Lab correction and the general candidate-abundance/employment argument.

## Conclusion for a broad ML/systems developer

Atomistic foundation models have become useful computational tools, and substantial engineering contributions are possible without first inventing a quantum-chemistry method. The attainable layers are **model/runtime integration, numerical correctness, scientific data semantics, evaluation, reproducible workflows and research-facing products**. Current company recruitment supports some of these routes. New scientific claims about an electrolyte, catalyst, molecular mechanism or manufacturing material require deeper domain expertise and independent validation.

The most useful distinction is between four different achievements: a model reproducing a particular DFT reference; a stable/efficient simulation; an accurate prediction of a physical property; and a synthesised, useful material. Strong evidence at one level does not automatically establish the next.

## 1. What the principal model families actually establish

### MACE: transferable potentials with model-specific domains and versions

The final November 2025 MACE-MP paper demonstrates broad qualitative and sometimes quantitative atomistic behaviour and data-efficient fine-tuning. Its normal example model is MACE-MP-0b3, rather than an unspecified generic MACE release. Stable molecular dynamics and fine-tuning progress are meaningful; they do not make every reaction, interface or battery calculation quantitatively correct. [Final paper DOI 10.1063/5.0297006](https://doi.org/10.1063/5.0297006), [preprint history](https://arxiv.org/abs/2401.00096)

The current project manifest distinguishes MP-0a/b/b2/b3, MPA, OMAT, MATPES, OMOL and multi-head models. Older MP checkpoints list MIT; several newer families use ASL. The code's MIT licence is not a blanket checkpoint licence. The implementation also warns that MACE raw DFT energies are not directly comparable with MP/CHGNet energies using compatibility corrections. Ignoring these reference conventions can invalidate an apparently careful model comparison. [Current checkpoint manifest](https://raw.githubusercontent.com/ACEsuit/mace-foundations/main/README.md), [code and energy-reference warning](https://github.com/ACEsuit/mace)

### UMA: substantial shared-model capability, with access and regression concerns

UMA combines several molecular, material and catalyst datasets and reports a shared model competitive with specialist models. The 2025 NeurIPS paper and March 2026 arXiv revision are distinct dated artifacts. Its model card identifies the original `uma-s-1` as having an extensivity bug and provides replacement checkpoints with checksums. The current custom FAIR Chemistry licence was updated on 13 October 2026; weights have access conditions. This is an excellent example of why reproducible scientific software must record exact checkpoint, task, dtype, licence and configuration. No weights were requested or downloaded. [NeurIPS paper](https://proceedings.neurips.cc/paper_files/paper/2025/hash/bbf23e81b0ad7637fe9a731d0b676ca6-Abstract-Conference.html), [arXiv v2](https://arxiv.org/abs/2506.23971v2), [model card](https://huggingface.co/facebook/UMA/blob/main/README.md), [current licence](https://huggingface.co/facebook/UMA/blob/main/LICENSE)

### Static accuracy, numerical stability and physical accuracy can disagree

The January 2025 systematic-softening study found underpredicted energies/forces in high-energy configurations for three tested universal potentials, affecting defects, surfaces and migration barriers. Its scope is those model/data versions; it is not proof that every 2026 model has the same error. Expanded off-equilibrium data and fine-tuning can address some failures. [Primary study](https://doi.org/10.1038/s41524-024-01500-6)

The eSEN work connects energy-conservation tests to downstream physical-property reliability, showing that lower held-out pointwise errors alone can mislead. A separate approximately 10,000-DFT-calculation phonon benchmark found some universal models performing well and others poorly despite good equilibrium energy/force accuracy. These are substantive positive and negative results, rather than a reason to dismiss foundation potentials. [eSEN paper](https://arxiv.org/abs/2502.12147), [phonon benchmark, June 2025](https://doi.org/10.1038/s41524-025-01650-1)

For battery materials, this matters because a model can reproduce near-equilibrium structures while mispredicting migration barriers or high-temperature behaviour. A simulated diffusion coefficient does not by itself establish cell conductivity, cycling life, safety or manufacturability. A mechanistically appropriate classical potential can remain a useful speed/reliability baseline inside its narrower validated domain.

## 2. Discovery and synthesis: precisely which outcome was measured?

Matbench Discovery assesses models as prefilters for DFT-based stability searches. Its reference hull comes from DFT energies, and its meaningful screening metrics differ from global energy-regression error. A model can have a low error yet select many false positives near the stability boundary. The task does not establish synthesizability, finite-temperature performance or useful manufactured devices. Training provenance, prototype overlap and model-specific benchmark compliance must remain visible. [Final paper, June 2025](https://doi.org/10.1038/s42256-025-01055-1), [current benchmark code/caveats](https://github.com/janosh/matbench-discovery)

MatterGen's 2025 Nature paper includes genuine experimental work: synthesis succeeded for one of four selected candidates. That is evidence beyond generation metrics, with a small experimental sample. The public implementation openly records important replication differences: released checkpoints were retrained rather than being paper-identical; default evaluation uses MatterSim instead of the paper's DFT evaluation; some ICSD reference structures cannot be redistributed. Therefore, running its example evaluator does not reproduce the paper's full scientific result. [Nature paper](https://doi.org/10.1038/s41586-025-08628-5), [official code, release/evaluation limitations](https://github.com/microsoft/mattergen)

MLIP Arena provides an existing framework for physics-awareness, reactivity and extreme-condition tests. A proposed new benchmark should complement it, not assume that all current evaluation is a single MAE leaderboard. [NeurIPS 2025 paper](https://proceedings.neurips.cc/paper_files/paper/2025/hash/bfa45223cc236855dbaa5c468c809896-Abstract-Datasets_and_Benchmarks_Track.html), [Apache-2.0 code](https://github.com/atomind-ai/mlip-arena)

## 3. A practical evaluation checklist, not a model ranking

| Question | Required comparison / evidence | Common false conclusion |
|---|---|---|
| What electronic-structure target? | Functional, dispersion, pseudopotentials, charge/spin treatment and energy corrections | DFT agreement equals experimental truth; energies from different reference schemes can be directly mixed |
| Is the task held out? | Entire chemical systems/prototypes/trajectories and explicit training provenance | Random frames from the same relaxation trajectory demonstrate new-material generalisation |
| Is it numerically coherent? | Units; force-energy gradient; permutation/rotation/translation behaviour; appropriate extensivity checks | Plausible trajectories prove correct forces or total energy |
| Are dynamics reliable? | Causal force evaluations, time-step convergence, energy drift, repeated initial conditions and relevant state ranges | Single-point MAE guarantees stable rare-event or high-temperature predictions |
| Does accuracy help the decision? | Screening precision at a fixed validation budget; barrier/phonon/property error relevant to the application | Better global regression means better discovery or faster useful science |
| What did it cost? | End-to-end preparation, transfer, batching, runtime, convergence/failure and memory on declared hardware | GPU kernel throughput equals workflow speedup; literature DFT timing is a local baseline |
| Was there physical validation? | Independent measurement, appropriate uncertainty and reproducible conditions | DFT-stable structure equals synthesised new material or commercial product |

The correct DFT comparison can itself be expensive. Existing public reference data permit useful software/evaluation work, but creating a novel trustworthy reference campaign requires domain-led convergence choices and compute. Fine-tuning or selecting a model based on held-out labels consumes the test set even if the model is called a foundation model.

## 4. Batteries offer a complementary, less atomistic software route

PyBaMM is a mature open battery-modelling framework with differential-equation solvers, model/parameter libraries and experiment utilities. Its code is BSD-3-Clause and its 2021 software paper describes a laptop-accessible entry point; current dependencies/releases must be checked separately from that historical paper. It is a path into numerical software and model fitting, not a ready-made validated model for any new cell chemistry. [Software paper DOI 10.5334/jors.309](https://doi.org/10.5334/jors.309), [current code](https://github.com/pybamm-team/PyBaMM)

Here, strong baselines are mechanistic models such as SPM/SPMe/DFN and simple equivalent-circuit models appropriate to the task. Evaluate on held-out cells, temperatures and operating schedules, not randomly interleaved points from the same voltage curve. A parameter fit can be numerically excellent while being non-identifiable or physically implausible. Solver tolerances, event handling, sensitivity/parameter estimation, uncertainty and data schemas are substantial software work that does not require a new neural architecture.

PyBaMM's open governance describes leadership through sustained substantial contributions, including review and project stewardship. Its scientific founders' qualifications should not be confused with a formal doctorate requirement for all contributions. Volunteer contribution is not a promise of employment. [Teams](https://pybamm.org/teams/), [governance](https://pybamm.org/governance/), [contribution channel](https://pybamm.org/contribute/)

## 5. Companies, laboratories and public professional channels

Directory only: no contact was made. Named channels are publicly listed by the institution or project. No private personal information or inferred email addresses are included.

| Group / company | Why relevant, papers/artifacts | Public channel / attainable entry / limits |
|---|---|---|
| MACE / Cambridge molecular modelling; Gábor Csányi, Ilyes Batatia and collaborators | Transferable potentials, equivariant models, runtime and domain validation; MACE papers above | [Cambridge profile](https://www.eng.cam.ac.uk/profiles/gc121), public `gc121@cam.ac.uk`; [code/issues](https://github.com/ACEsuit/mace). Potential contributions: adapter correctness, numerical tests, profiling and reproducibility. Scientific model invention requires deeper statistical mechanics/electronic-structure understanding. |
| Matbench Discovery / Materials Project; Janosh Riebesell, Kristin Persson, Anubhav Jain and collaborators | Screening evaluation and curated DFT/data infrastructure | [Project discussions](https://github.com/janosh/matbench-discovery/discussions), [MP documentation/forum](https://docs.materialsproject.org/), [Persson institutional profile](https://mse.berkeley.edu/people_new/persson/). Public profile lists `kristinpersson@berkeley.edu`. Dataset QA, split/provenance audits and evaluator contributions can begin without a new DFT campaign. |
| FAIR-Chem / Meta; Brandon Wood, Xiang Fu, Zachary Ulissi and coauthors | UMA/eSEN, cross-domain atomistic models and deployment | [FAIR-Chem code/issues](https://github.com/FAIR-Chem/fairchem), [UMA model card](https://huggingface.co/facebook/UMA). Public materials licence channel `fairchemistry@meta.com`. Model integration and precise failure reports are accessible; proprietary compute scale and gated weights are distinct constraints. |
| Microsoft Research AI for Science; Claudio Zeni, Tian Xie and coauthors | MatterGen, MatterSim and generated-structure validation | [Official MatterGen repository/Q&A](https://github.com/microsoft/mattergen). MIT code; model/data-specific notices and unavailable ICSD references must be checked. Entry: evaluation consistency, model-card provenance and reproducible examples, rather than claiming a material discovery from generation alone. |
| MLIP Arena; Yuan Chiang, Aditi Krishnapriyan and coauthors | Physics-aware, task-based testing across potential families | [Code/issues](https://github.com/atomind-ai/mlip-arena), [institutional profile/channel](https://www2.eecs.berkeley.edu/Faculty/Homepages/aditik.html) lists `aditik1@berkeley.edu`. Paper DOI 10.52202/085713-4410; [arXiv](https://arxiv.org/abs/2509.20630). Reproduce an existing task before adding a new one; exact model licences differ from framework Apache 2.0. |
| FAIRmat / NOMAD; Claudia Draxl and consortium | Funded scientific-data infrastructure, schemas, parsers, workflow/metadata support | [Consortium](https://www.fairmat-nfdi.eu/fairmat/), [official contact](https://www.fairmat-nfdi.eu/fairmat/about-fairmat/contact-fairmat): `fairmat@physik.hu-berlin.de`, `contact@nomad-lab.eu`. Data/parser/schema contributions are plausible entry routes. Software licences and dataset reuse terms must be checked per component. |
| PyBaMM; Valentin Sulzer, Ferran Brosa Planella, Robert Timms, Agriya Khetarpal and maintainers | Open numerical battery models, calibration and solvers | [Teams](https://pybamm.org/teams/), [contribution page](https://pybamm.org/contribute/) lists `pybamm@pybamm.org` and GitHub discussions. Global software contribution is possible; realistic cell-parameter and degradation claims need battery expertise/data. |
| CuspAI; platform engineering and science teams | Research-facing products and discovery workflow software | [Official company](https://cusp.ai/), [published Product Engineer role](https://jobs.ashbyhq.com/cuspai/8fb59417-ee76-47de-92cf-233879b97bb2). Role asks 4+ years full-stack experience, Python/web frameworks, modern JS/UI, and explicitly allows no science background. Three days/week in Cambridge/London/Amsterdam/Berlin. Not verified as an India-remote opportunity. |
| Orbital Industries; AI/materials/software teams | Multiscale scientific ML and production engineering | [Official ML Research Engineer advert](https://jobs.ashbyhq.com/orbitalindustries/0405b3d7-c134-43e4-a7af-a9763a5bf3d9). London hybrid; strong model-training/evaluation/production record, algorithms, linear algebra and probabilistic reasoning; prior chemistry not required. Company claims about physical products are separate from independently replicated scientific performance. |

## 6. Funding and role evidence: what is and is not accessible

FAIRmat reports that its second NFDI funding period was approved in July 2026 and began on 1 October 2026. This is evidence of continuing infrastructure support; no verified current funding amount or hiring count was established here. A frequently surfaced software-engineer advert was published in 2022 with positions limited through September 2026, so it must not be called a new current opening. [Official renewal news](https://fairmat-nfdi.eu/fairmat/resources-fairmat/dmp-support/fairmat/fairmat/news-fairmat), [current consortium](https://www.fairmat-nfdi.eu/fairmat/)

NSF's 2025 DMREF solicitation anticipated $40 million, with 20–25 four-year awards and US awards around $1.5–2 million. It includes a US–India collaboration route with an Indian portion up to ₹20 million through DST, but imposes institutional/PI eligibility and separate funding rules. These are **historical solicitation ceilings and expectations**, not money currently available to a solo developer, verified disbursement or an open 2026 call. [Official NSF 25-508 solicitation](https://www.nsf.gov/funding/opportunities/dmref-designing-materials-revolutionize-engineer-our-future/nsf25-508/solicitation)

CuspAI and Orbital role examples demonstrate transferable engineering tasks, not a representative estimate of scientific-software demand. Direct Ashby rendering was limited; requirement text was inspected in the official search-indexed adverts. Current acceptance of applications, sponsorship and personal eligibility remain unconfirmed. Similar names produced unrelated banking/real-estate Orbital companies; those were excluded. No salaries or aggregate employment forecasts were inferred.

## 7. Reproducible 30/90-day project with explicit oracles

The primary route below uses existing artifacts; no new DFT or physical experiment is required. Proposed thresholds are portfolio gates, not scientific/regulatory standards. All downloads, installations and compute spending remain later actions under the user's approval rules.

### Days 1–30: reproduce one screening result and its failure conditions

Use a pinned Matbench Discovery release and its public DFT-reference/prediction artifacts. The producer paper identifies [WBM data](https://figshare.com/articles/dataset/22715158), [MPtrj data](https://figshare.com/articles/dataset/23713842) and a [permanent framework release](https://doi.org/10.5281/zenodo.13750664). Inspect licences/manifests before fetching a bounded subset. Use complete released predictions if sufficiently small; do not silently trigger a bulk download or train a foundation model.

1. Freeze IDs, data and evaluator versions, input structure state, energy reference/correction scheme, missing-prediction policy and exact model checkpoint. **Independent oracle:** published DFT-labelled reference artifacts, not predictions from another ML potential.
2. Compare at least a dummy/random selection baseline, published Voronoi-RF predictions and one published MACE checkpoint's predictions on exactly the same task/subset. Preserve the benchmark's official decision boundary and DFT hull; test a separately labelled threshold-sensitivity analysis rather than redefining ground truth for a better score.
3. Recompute precision/recall/F1, precision at fixed top-k validation budgets and energy error. Reproduce an applicable published/archived metric within 1e-4 when the artifact versions match. If versions differ, document the mismatch and call it a new analysis rather than a replication.
4. Report chemical-system/prototype groups and near-boundary cases. Keep trajectories and structures from one parent family together when constructing any additional validation/test split. Public pretraining overlap or unknown provenance must remain visible; a new split cannot erase it.
5. Manually trace at least ten independently selected counterexamples from source structure/reference energy to prediction and classification. A second implementation of the metric on a small hand-specified fixture should agree; reproducing only the library's output is insufficient to establish correctness.

Deliver a compact report distinguishing reproduced result, unresolved artifact mismatch and proposed additional analysis. No new-material or synthesis claim follows from this exercise.

### Days 31–90: a bounded numerical and runtime validation contribution

Choose **one** verified gap in MACE/ASE/MLIP Arena or its adapter. Do not create a competing general framework. A proposed pilot compares ASE's mature EMT empirical calculator and a pinned MIT-listed MACE-MP-0b3 small checkpoint on small neutral, nonmagnetic Cu/Al periodic systems. This tests software/physical consistency and a narrow speed trade-off; it is not a universal chemical-generalisation benchmark.

- Test deterministic translation, atom permutation, simultaneous coordinate/cell rotation and periodic-supercell replication. Record total energy versus energy/atom and force-vector transformations. For these restricted systems, extensivity must be compared under the same physical state and settings.
- Independently compare forces to central finite differences of total energy at displacements 1e-3 and 1e-4 Å in float64 where supported. A proposed numerical gate is maximum disagreement below 1e-3 eV/Å after step-size convergence; revise it only with documented numerical justification, not to hide a model failure. Passing verifies consistency, not agreement with nature.
- Use a standard MD engine and fixed initial conditions for short NVE runs; compare 0.5 and 1 fs time steps. Report energy drift per atom, trajectory failures and dependence on time step. If halving the step does not improve a concerning drift, first investigate integrator, precision and adapter errors before attributing it to model physics.
- If testing physical accuracy, select an existing public DFT-labelled trajectory/property subset independently of observed model errors and retain complete systems/trajectories as hold-outs. Match reference conventions. Do not use self-generated ML trajectories labelled by the same model as the reference.
- Benchmark cold start, warm force evaluation, conversion/neighbour-list overhead, full simulation throughput, peak memory and failures on declared hardware. Compare equal systems, precision, integrator and workload; report absolute time alongside ratios. Do not invent a DFT speedup without a measured comparable DFT reference.
- A candidate contribution passes only if it reproduces a real issue or documents a new, reviewed limitation, includes an independent counterexample and preserves existing behaviour. A known UMA extensivity bug is a regression example, not a new scientific discovery.

**Kill/redirect criteria:** stop the proposed novelty claim if existing tests already cover it; stop a chemical accuracy claim when reference/data provenance cannot be established; stop comparing checkpoints with incompatible energy targets; reduce the workload if approved local compute is inadequate rather than quietly buying cloud time. If no atomistic contribution survives review, a PyBaMM solver/event/parameter-identifiability regression is a legitimate alternative—without calling it a new material.

## 8. Prerequisites and progression

| Target | Skills to add | Evidence of readiness | Main boundary |
|---|---|---|---|
| Scientific platform/product engineer | Production Python/JS, APIs, data modelling, testing, research UX and metadata semantics | Shipped reliable tools; reproducible artifact/data lineage; user-led workflow improvement | Product/science partnership and employer geography; not necessarily a doctorate |
| Runtime / simulation integration | Numerical precision, profiling, neighbour lists, batching, CPU/GPU memory, autodiff and native interfaces | Measured end-to-end improvements with invariant/reference checks | Hardware/software stack competence; local benchmark is not scientific truth |
| Model validation / research engineering | Linear algebra, optimisation, probability, numerical differentiation, experimental design and uncertainty | Strong baselines, held-out systems, documented negative results and independent reproduction | Sufficient domain knowledge to choose correct target/reference |
| Atomistic-method researcher | Statistical mechanics, quantum/electronic structure, symmetry/equivariance, thermodynamics, kinetics and methods literature | A new method with rigorous domain-reviewed evidence and reproducible comparisons | Usually substantial research training/credentials or equivalent record |
| Material discovery / experimental leadership | Synthesis, characterization, processing, scale-up and application-specific performance | Independent physical validation, reproducible properties and credible application outcomes | Trained collaborators, facilities, safety and long development cycles |

A useful early curriculum is energy/force/stress units, basic thermodynamics and phase competition, numerical optimisation, differential equations, uncertainty and the distinction between model and reference error. Full quantum-method development is unnecessary for a parser, runtime or research-product contribution. Conversely, reading a few model cards is not sufficient to choose a scientifically valid DFT setup or claim a battery mechanism.

Research leadership should be evidenced through sustained ownership of a reproducible project, scientific/software decision quality, independent uptake, reviews and mentoring. Original contribution requires prior-art review against Matbench Discovery, MLIP Arena and the relevant domain benchmark; producing another leaderboard wrapper is not automatically novel.

## Methods and remaining limits

Read the root source/claim index before the distinct scan. Coordinated with the energy worker: its scope is nuclear/fusion and prior grid-dispatch work; PyBaMM/electrochemical software was not duplicated there. Root owns deduplication and final correction merging; earlier files were not rewritten.

Primary sources were papers/version histories, actual model licences/manifests, official repositories, institutions and official recruitment/funding text. Some Nature/AIP pages rendered intermittently or through indexed full text; no supplementary raw-data reanalysis was done. Model training, inference, MD, DFT and physical measurements were not independently reproduced. Current model-page identity can differ from an old paper's code example, so no timeless licence or performance claim is made for an entire model family.

No precise 2031 hiring-volume, salary or startup-success forecast is justified by these sources. The practical finding is that real tools and advertised roles create testable entry routes, while scientific conclusions require stronger oracles than running a model successfully.
