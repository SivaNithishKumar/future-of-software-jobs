# Six conditional cross-field transfer paths, round 15

Derived 20 October 2026 from saved projects, preparation modules and role contracts. No fresh web research, learner assessment or implementation. These are proposed crosslinks, not a personalized ranking, curriculum or claim of lower hiring barriers.

**Reusable means demonstrated somewhere else.** A job title, broad familiarity or the existence of a proposed project does not establish that evidence. For each path, first inspect an actual artifact, a reproducible result and an explanation of its limits. None of the saved project designs is treated as a completed personal skill assessment. The shared preparation modules remain conditional dependencies.

Each fresh probe below is an **alternative, single-sitting diagnostic**, capped at one hour with existing paper/stdlib tools. A setter should choose a new fixture and record expected answers before the attempt. Visible examples are design diagnostics, not unseen tests. The probe can identify a missing concept or invalidate a proposed transfer; it cannot establish mastery, job qualification or physical capability. Existing full-project budgets are not added together or restarted.

## 1. Data migration / CDC → health interoperability

**What could carry over:** if `data-r13.copy-log-oracle` has actually demonstrated committed-cut reconciliation, source-scoped identifiers, revision/deletion handling and independent per-field checks, reuse those habits and ordinary SQL/API/test engineering. Relevant modules are `data-meaning`, `production`, `authority` and `oracles` under `preparation-round8.module.*`. Proposed destination: `health-r12.synthetic-reconciliation`.

**Added depth:** FHIR resource versus business-person identity; version-specific implementation guides and profile constraints; terminology/code-system versions; unit semantics and date precision; consent/authorization and clinical workflow meaning. A source log position is not a universal clinical revision order. Opaque FHIR version identifiers cannot simply be numerically sorted as CDC sequence numbers. Native parser/profile validation and an ordinary explicit mapping are the first comparators.

**Fresh probe:** supply six new synthetic updates across two identifier issuers, including the same identifier value, an opaque version, a partial date and a nonclinical absent-versus-zero observation. Ask for the current projection, quarantined records and a field-level evidence ledger at one declared cut. A separate expected table must expose a wrong-person merge or invented precision. No patient data or medical terminology is needed. Correct replay demonstrates meaning-preservation on this tiny contract; it does not validate clinical interpretation.

**Where transfer fails:** syntactically valid fields may still carry the wrong clinical meaning. Terminology rights, an inaccessible workflow oracle or patient-data authorization can stop real deployment. The saved NHS Epsom example is **closed**, with degree-or-equivalent language; the Guy's sample is historical/indexed and describes Epic/integration and office attendance. These do not establish a current opening or waive domain experience. HAPI/Smile and OHDSI channels are contribution routes, not job access.

Saved anchors: `health-r12.nhs`, `health-r12.hapi-smile`; [health note](<health-interoperability-option-round12.md>), [CDC contract](<data-migration-option-round13-proposals.json>).

## 2. Model serving / evaluation → GPU operator and compiler work

**What could carry over:** only if `science-enrichment-round5.project.ecg90` or another real serving artifact has demonstrated matched-quality comparisons, cold/warm boundaries, queue/resource diagnosis and complete failure counts. Reuse `preparation-round8.module.serving`, `.runtime`, `.oracles` and `.measurement`. Destination: `gpu-round14.project.softmax-contract`.

**Added depth:** floating-point rounding and reduction error, conditioning, shape/layout/stride contracts, memory traffic, SIMT execution and synchronization. A compiler/backend path further adds C++/IR/dataflow/legal-transform reasoning; service profiling alone does not supply that. CUDA/Triton/device tooling and a compatible target are separate access gates. Use native eager/compiled operations and mature adversarial checks before proposing a new harness.

**Fresh probe:** a setter gives a supposedly correct softmax and a timing ledger. Require a new nonuniform two-value reference, a constant-shift variant, one unsupported-layout case and a corrected interpretation of compilation versus warm device-event time. A mass-preserving uniform answer must fail the nonuniform reference. Existing stdlib arithmetic can test that contract; it cannot measure GPU speed, float32 parity, memory safety or backward gradients.

**Where transfer fails:** a host-only result says nothing about device execution; a local kernel gain may vanish in a real caller. Saved River AI requirements include C++/Python, GPU architecture/numerics and a bachelor or equivalent practical experience, with Palo Alto location. NVIDIA's indexed India assembler example asks substantial low-level/compiler experience and BS/MS; its direct body/application acceptance was unverified. A one-hour probe does not reduce those barriers.

Saved anchors: `gpu-round14.institution.river`, `gpu-round14.institution.nvidia-assembler`; [GPU audit](<gpu-compiler-option-round14.md>).

## 3. Robotics frames / clocks → embedded sensor acquisition

**What could carry over:** if `state-estimation-round13.project.contract30` has actually demonstrated frame direction, unit conversion, offset/skew distinction, unique support and explicit missing data. Reuse `preparation-round8.module.data-meaning`, `.physical-integration` and `.oracles`. Destination: `embedded-round12.project.trace-ota`, initially its acquisition contract.

**Added depth:** fixed-width C arithmetic/undefined behaviour, interrupt versus thread context, preemption, buffer ownership/lifetime, ABI/endianness, bounded queue work and driver/configuration semantics. A nanosecond field is not measured acquisition accuracy. A known frame transform does not establish sensor calibration. OTA/signing/flash recovery is a separate extension, not implied by correct pose maths.

**Fresh probe:** provide a small FIFO ledger spanning an integer-counter wrap, a **different boot epoch**, a range/calibration change and an overflow drop. Ask which samples are valid at the consumer cut and reconcile arrivals with processed+dropped+pending. A wrap rule must not join measurements across reset, and a software timestamp must not become a physically latched capture instant. This is a state/time diagnostic; host or schedule-model timing remains distinct from MCU timing.

**Where transfer fails:** native_sim is a Linux host target, not a Cortex-M timing oracle. Hard deadlines, DMA/cache behaviour, board bring-up and power interruption need authorized hardware/instrumentation. The saved Samsara senior/staff firmware example asks 8+ years, strong C/RTOS, board and bench work and constrained geography. The Garmin junior example is indexed, not a verified current application. Simulation cannot replace either role's actual criteria.

Saved anchors: `embedded-round12.role.samsara`, `.role.garmin`; [embedded audit](<embedded-realtime-option-round12.md>), [state-estimation audit](<state-estimation-option-round13.md>).

## 4. Scheduling / OR → storage dispatch and grid decision software

**What could carry over:** if `education-quantum-or-round7.project.scheduling` demonstrates formal constraints, independent feasibility/objective checking, solver status/bounds and causally revealed replanning inputs. Reuse `preparation-round8.module.oracles`, `.measurement`, `.ml-math` and `.domain-collaboration`. Destination: `energy-public-round6.project.battery`. The authored OR technical root remains unmounted in the saved main taxonomy; project identity is preserved without pretending it is integrated.

**Added depth:** MW versus MWh and settlement intervals, charge/discharge efficiency, energy/reserve/terminal constraints, fees/degradation and forward versus realized prices. Network/power-flow/protection work adds electrical modelling beyond a small dispatch LP. A valid job-shop schedule does not supply the correct electricity objective or asset constraints.

**Fresh probe:** give two half-hour dispatch intervals and a candidate satisfying its MW limits. Include discharge efficiency and an initial energy low enough that the proposed output makes state of charge negative. Require independent conservation and objective recomputation, plus a decision about whether supplied prices were knowable at the cut. An illustrative case starts at 0.2 MWh and discharges 0.4 MW for half an hour at efficiency 0.8: energy becomes -0.05 MWh. Catching it tests this contract, not physical battery health or market profit.

**Where transfer fails:** ex-post optimal schedules do not establish causal savings or permitted market participation. Saved Hitachi Bengaluru roles sharply distinguish ordinary DevOps/QA from the power-system application specialist requiring electrical/related master's/PhD, five years' power analysis and MATLAB/Simulink. Modo's saved London Python role requires professional Python experience and office attendance; it is different work. OR familiarity cannot waive the specialist filter or asset/operator access.

Saved anchors: `energy-public-round6.institution.hitachi`, `.institution.modo`, `education-quantum-or-round7.claim.amazon-or-role`; [energy role contrasts](<energy-round2.md>).

## 5. Classical compiler / EDA verification → quantum tools

**What could carry over:** only if `eda-hardware-round11.project.constrained-flow` or a real compiler artifact demonstrates representation semantics, independent correctness checks, reproducible builds and constrained resource comparisons. Reuse `preparation-round8.module.implementation`, `.native-specialism`, `.oracles` and `.numerics`. Destination: `domain-institutions-round2.quantinuum.proof` or the existing Qiskit proof route, selected individually.

**Added depth:** complex linear algebra, tensor products, unitary/reversible operations, global versus relative phase, measurement and ancilla cleanup. Physical connectivity, gate/noise/calibration and fault-tolerant resource proxies differ from conventional PPA. Familiar C++/LLVM/MLIR patterns can help tooling work only where those patterns are actually understood.

**Fresh probe:** present a proposed pass that preserves computational-basis output bit probabilities while adding a control-qubit Z phase to CNOT. Require one coherent-input witness and an equivalence verdict up to **one global phase**. For a plus-control/zero-target input, opposite Bell-state relative signs distinguish the circuits even though basis-state bit tests pass. A hand/stdlib two-qubit calculation is enough; no QPU is needed. It proves a tiny semantic distinction, not a useful algorithm, quantum advantage or control timing.

**Where transfer fails:** classical output equality is insufficient for quantum coherence; a toy gate cost is not wall-clock/QPU value. Saved Riverlane Compiler Engineer requirements include Python plus C++/Rust and compiler/OS/architecture knowledge, with LLVM/MLIR interest/experience and hybrid Cambridge work. No PhD was listed, but broader equivalence wording/experience were not fully retained; sponsorship is not assured. Contributor agreements, artifact rights and current policy remain separate gates.

Saved anchors: `role-proof-round14.role.riverlane`, `domain-institutions-round2.ibm-qiskit.proof`; [quantum audit](<quantum-round3.md>), [EDA contract](<eda-hardware-software-option-round11-records.json>).

## 6. Scientific ML evaluation → one weather or battery decision contract

**What could carry over:** if `science-enrichment-round5.project.ecg90` demonstrates group-heldout evaluation, training-only transforms, an explicit label oracle, baseline comparisons and honest uncertainty. Reuse `preparation-round8.module.empirical-ml`, `.scientific-data`, `.measurement` and `.research-design`. Choose **one** destination: `weather-round13.project.archive-decision` or `battery-health-round13.project.telemetry-contract`.

**Added depth depends on that choice.** Weather needs initialization/model vintage, publication/receipt/valid time, analysis versus observation truth, station/grid mapping, event dependence and probability-versus-action scores. Battery work needs capacity/reference-test meaning, nominal versus measured references, cycle/age units, censored/extrapolated endpoints and physical cell/cohort identity. Patient holdout discipline is a useful pattern; patients, weather events and cell prefixes are not exchangeable statistical units.

**Fresh probe:** a setter selects one small new metadata card: either a historically retrieved forecast/corrected observation pair, or a short cell prefix with a changed capacity reference and censored follow-up. Ask which quantities were available at the decision, what the target actually means, which comparison is admissible and what remains unknown. Expected answers must allow refusal. No predictive model is necessary. Correct reasoning establishes the data/target contract on that card, not forecast skill or electrochemical truth.

**Where transfer fails:** station temperature is not crop response, and a capacity proxy is not a standardized health measurement. Real data rights and domain review remain gates; the RWTH paper/code reference mismatch remains unresolved. The saved Met Office 1488 example has code/QA/ML requirements and a role-specific UK residence/work-right screen; its lack of a listed mandatory PhD does not erase that screen or establish urban-scale modelling competence. The battery directory did not verify a currently accessible India/UK software vacancy.

Saved anchors: `role-proof-round14.role.metoffice`, `weather-round13.role.metoffice-foundation`, `battery-health-round13.project.telemetry-contract`; [independent validity review](<independent-weather-battery-review-round14.md>).

## Crosslink and validation boundaries

The companion JSON proposes typed edges between existing authored project, module, technical and role-contract references. Local packet IDs are explicitly distinct from accepted global identities; no node/edge is mounted. Each edge means “potentially reusable if source evidence passes, plus this added domain proof,” not “qualified for target work.”

Input snapshots and exact ID references were checked locally. No live job/policy was refreshed; retained role dates and closed/indexed/undated states stay attached. No fresh probe was administered, learner capability measured, personalized ordering produced, curriculum restarted or aggregate hour budget calculated. No installation, upstream execution, external mutation, outreach or child agent occurred.

