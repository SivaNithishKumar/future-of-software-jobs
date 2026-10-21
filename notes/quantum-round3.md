# Quantum computing: technical and career feasibility audit — round 3

Evidence checked 19 October 2026. This is a bounded technical pass, separate from the institutions directory. No simulator, package, dataset, model, cloud job, account, hardware purchase or outreach was executed. Suggested experiments below are plans, not completed work. No edit was made to the main taxonomy.

## Provisional judgment

Quantum computing is a serious technical specialism with genuine advances. It is a poor default answer to “where should an AI/software developer move to avoid automation?” The accessible route is usually a precise classical-software problem inside the quantum stack—compilers, simulation, decoding, profiling, controls/runtime or research infrastructure. Algorithm invention, quantum chemistry and device research require substantially deeper mathematics, domain science and often graduate research. Source and simulator access do not establish an accessible job market.

The 2031 opportunity is conditional: hardware, reliable logical operations, algorithms, application value and a paying organisation must all line up. Some specialist software employment already exists before broad application advantage. That does not imply a large general quantum-app market will emerge on schedule, nor that a small simulation project qualifies someone to lead quantum research.

## A claim must survive this entire chain

Physical qubits and gate errors → encoded logical memory → reliable logical gate set → long, complete logical computation → algorithm resource estimate → fair classical comparison → useful decision/output → end-to-end cost/value → employer/customer access.

At every arrow ask what was actually demonstrated, on what workload, with what error model, how many total attempts, how much classical work, and what remains projected. A single physical/logical qubit count collapses most of this information.

## 1. Error correction is advancing; the denominator matters

### Q01 — Google's below-threshold surface-code memory: direct primary paper

Google's paper, published online 9 December 2024 in *Nature* 638 (2025), reports a distance-7 memory on 101 physical qubits, logical error 0.143% ± 0.003 percentage points per correction cycle and suppression factor 2.14 ± 0.02 per distance increment of two. A distance-5 experiment integrates real-time decoding; the reported average decoder latency is 63 μs with 1.1 μs cycles. Rare correlated events appear in a separate repetition-code experiment. These are substantive memory/decoding results, not a complete useful algorithm. The paper itself identifies logical computation, calibration, decoder and compiler scaling as remaining work. [Primary paper](https://www.nature.com/articles/s41586-024-08449-y).

An author correction exists dated 28 April 2026. The updated paper was opened, but the correction page itself hit a publisher access failure; its exact change was not verified in this pass. Do not invent what was corrected or call this a full corrected-supplement reanalysis. The paper points to public Zenodo data; that landing page also failed here, so dataset contents/licence were not independently checked. [Correction](https://www.nature.com/articles/s41586-026-10559-8), [data identifier](https://doi.org/10.5281/zenodo.13273331).

**Career implication, inference:** classical decoding is not an optional notebook after the physics. Software must handle a stream, maintain timing and produce accurate decisions while calibration changes. Average decoder latency, decoding throughput and a feedback deadline are different quantities; an offline CPU benchmark cannot self-certify a real-time controller.

### Q02 — September 2026 Helios architecture: stronger than memory alone, still small

The 2 September 2026 primary preprint introduces the [[20,2,6]] C4-Helix code. Its abstract reports repeated correction at approximately 4.6×10⁻⁵ error per logical qubit/cycle with broad uncertainty, two-logical-qubit Clifford error around 2.8×10⁻⁴, and a heterogeneous three-logical-qubit GHZ experiment. It says the encoded cases beat their matched physical baselines **without postselection**. The 10⁻⁶–10⁻⁸ regime is a circuit-simulation projection under improved physical fidelity, not the observed result. Full HTML retrieval failed, so this entry uses the complete primary abstract rather than claiming an appendix audit. [Preprint](https://arxiv.org/abs/2609.03194).

### Q03 — Today's 19 October 2026 announcement: do not convert memory fidelity into algorithm success

Quantinuum today announced 99.9995% logical fidelity; its companion blog specifies **logical memory** fidelity. It attributes differing overhead/accuracy trade-offs to Helix and colour codes. Primary search text was available, but direct page opens failed and a linked full experimental report/presentation was not retrieved. Keep this as a fresh **company claim pending methods review**, not independently replicated general fault tolerance. The company itself lists scaling and commercial-use risks. [Announcement](https://www.quantinuum.com/press-releases/quantinuum-breaks-error-correction-world-record-by-10x-validating-its-leading-path-to-fault-tolerant-quantum-computing-by-2029), [memory-specific explanation](https://www.quantinuum.com/blog/quantinuum-closes-in-on-one-million-error-free-operations).

**Illustrative arithmetic, not a model of Helios:** if every one of a million arbitrary steps independently had failure probability 5×10⁻⁶, the chance of no step failing would be about 0.67%, not 99.9995%. Real memory/gate errors, correlations and definitions differ, so this calculation must not be presented as the machine's measured algorithm success. Its purpose is to show why per-operation fidelity cannot be copied onto a long job.

### Q04 — End-to-end fault-tolerant algorithms: inspect gates, discarded attempts and classical output

Perlin et al.'s 4 March 2026 preprint runs small Steane-code QAOA/HHL circuits on H2/Helios. It reports a logical T-gate infidelity around 2.6×10⁻³; 5–8-logical-qubit examples approach their unencoded comparison, while larger examples deteriorate. Appendix F reports kept/total shots and repeat-until-success limits, so accepted-run quality must be read beside discard cost. Its HHL discussion explicitly says efficient input access and favourable conditioning are necessary, and reading the full classical solution vector removes the advertised exponential benefit. These are algorithmic engineering milestones, not a demonstrated business advantage over a strong classical solver. [Full primary preprint and appendices](https://arxiv.org/html/2603.04584v1).

**Learning consequence:** distinguish error detection from correction; memory from gates; Clifford operations from non-Clifford/magic-state resources; per-cycle error from per-job failure; postselected quality from all-attempt throughput; and a quantum output state from a classical array a customer actually needs. “Logical qubit” has no sufficient standalone job-performance meaning.

## 2. Roadmaps and resource estimates are conditional engineering models

### Q05 — IBM's 2029 target is a target, with dependencies

The current IBM roadmap states that information is intent and may change/withdraw. Its Starling goal is 200 logical qubits and 100 million gates in 2029; earlier milestones include real-time decoding, modules, interconnects and magic-state distillation. These are relevant engineering work packages, not achieved 2026 hardware. A cryogenic/interconnect milestone alone cannot establish the complete machine. [Current roadmap](https://www.ibm.com/roadmaps/quantum/), [technical target explanation, 10 June 2025](https://www.ibm.com/quantum/blog/large-scale-ftqc).

**Risk-budget illustration:** for 10⁸ operations, assigning every operation an error budget of 10⁻¹⁰ makes the union-bound upper limit on any operation failing 1%. This is conservative bookkeeping, not an IBM specification or independence assumption. The actual architecture must also account for memory time, communication, state factories and correlated/software failures. “Can run 100M gates” needs a gate set, total duration and success criterion before comparison with an application.

### Q06 — Factoring estimates show why fewer qubits can mean longer runtime

Gidney's 21 May 2025 resource-estimation preprint reduces an RSA-2048 estimate to under a million noisy physical qubits and under a week. It assumes a nearest-neighbour square layout, uniform 0.1% error, 1 μs code cycles and 10 μs classical reaction time. Its accounting includes repeated attempts and logical-error losses; reduced factory space and additional arithmetic trade time for qubits. This is an estimate for a hypothetical large fault-tolerant machine, not an RSA-2048 hardware demonstration or a calendar prediction. [Primary methods/layout/accounting](https://arxiv.org/html/2505.15917v1).

**Required resource sheet for any application:** useful input instance and precision; state preparation/data access; logical qubits; non-Clifford count/depth; routing/connectivity; code and physical error model; factory throughput; feedback/decoder latency; rejection/repetition; expected wall time; classical memory/CPU/GPU; capex/energy/cloud price; and useful output confidence. Compare alternative points on a time/space/cost frontier. Do not equate this task's most recent factoring estimate with the settled best across every 2026 architecture; other preprints and assumptions exist.

## 3. Classical competitors and economic utility: attack both optimistic and dismissive stories

### Q07 — A quantum experiment can beat brute force yet lose to a better classical method

IBM's 2023 127-qubit kicked-Ising work explicitly pursued a first step toward utility rather than a proven application speedup. Subsequent primary classical work used geometry-aware tensor networks/belief propagation and sparse-Pauli methods to reproduce relevant observables efficiently; Begušić/Chan report laptop-core runtimes substantially below the quantum experiment's reported wall time. These counterexamples do not prove every quantum advantage claim fails. They show that “cannot store all 2ⁿ amplitudes” is not a sufficient classical baseline. [Original experiment](https://www.nature.com/articles/s41586-023-06096-3), [Tindall et al. methods](https://arxiv.org/html/2306.14887v2), [Begušić/Chan methods](https://arxiv.org/html/2306.16372).

### Q08 — Not every new advantage experiment is the same old benchmark

Google's 22 October 2025 paper measures higher-order out-of-time-order correlations, compares specified classical methods and demonstrates a toy Hamiltonian-learning use. It separates beyond-classical measurement from useful real-system information and leaves an NMR application for future work. An April 2026 primary preprint tests a missing tensor-network/belief-propagation alternative and reports it cannot feasibly reproduce that experiment; this strengthens a particular benchmark claim, not a theorem defeating all future classical methods or a proven broad commercial application. [Experimental paper](https://www.nature.com/articles/s41586-025-09526-6), [classical alternative analysis](https://arxiv.org/html/2604.15427v1).

### Q09 — Chemistry and QML need fair input/output and classical assumptions

The primary 2023 chemistry analysis tests the evidence for *exponential* advantage and questions assumptions about easy quantum ground-state preparation versus hard classical heuristics; this does not rule out useful polynomial advantage. Full publisher retrieval failed here, so the precise supplementary cases still need audit. [Primary analysis](https://www.nature.com/articles/s41467-023-37587-6).

Tang's original recommendation-system result provides a concrete warning for QML: with analogous norm-sampling input access, a classical algorithm removes a claimed exponential advantage for that particular problem. It does not disprove all quantum ML. A recommendation such as “learn QML because classical ML is crowded” must therefore specify data loading, state preparation, readout, model quality and an equally privileged classical baseline. [Primary theoretical result](https://arxiv.org/abs/1807.04271).

### Q10 — Value exceeding cost is being tested, not already certified

DARPA's 7 October 2026 QBI update defines utility scale in economic terms and advances additional teams to Stage C, where systems/assumptions will be tested. Its target is to determine credible utility-scale paths by 2033. Selection is evidence of serious scrutiny, not certification that a company has achieved economic advantage or will create many developer vacancies by 2031. [Official current assessment programme](https://www.darpa.mil/news/2026/four-more-teams-enter-quantum-benchmarking-initiative-final-stage).

**Provisional answer after these counterchecks:** this audit does not establish repeated commercial net value over a matched best classical alternative across a broad application class. That bounded conclusion is different from claiming quantum computers are useless or no useful result exists. Hardware/control/decoder/compiler teams can still do valuable funded work before that commercial threshold is crossed.

## 4. Quantum expertise itself is exposed to AI-assisted invention

Gu et al.'s primary preprint submitted 15 October 2026 uses LLM proposals and an independent evaluator for eight selected reversible computational primitives. Its cost proxy is Toffoli count × peak qubits, not dollars or fault-tolerant execution time. The evaluator checks output, phase and clean ancillas; for large domains it samples trajectories rather than exhaustively proving all inputs. Some tasks permit bounded approximation/failure. The work reports resource improvements, not physical hardware runs, representative researcher productivity or job loss. It is a strong counterexample to treating specialised quantum circuit design as inherently beyond AI. [Primary paper, including evaluator and task tables](https://arxiv.org/html/2610.22367v1), [company explanation, 16 October](https://www.anthropic.com/research/designing-efficient-quantum-circuits).

**Inference:** a useful quantum specialist should understand problem formulation, evaluator correctness, assumptions, resource accounting and hardware/domain consequences, while using automation where it works. None of those activities is assumed permanently unautomatable. A thin circuit wrapper or unverified “AI-designed quantum algorithm” is weak evidence of depth.

## 5. Actual entry routes: choose the work, not the quantum label

| Route | Concrete work and prerequisites | Attainable evidence | Main boundary |
| --- | --- | --- | --- |
| QEC / decoder software | Noisy-circuit simulation; graph algorithms; statistics; Python/C++; profiling and streaming | Reproduce a trusted decoder; expose noise-model mismatch; correct a meaningful regression | Offline throughput is not hardware feedback latency; advanced code/decoder research is deeper |
| Compiler / verification | IRs, transformations, control flow, LLVM/MLIR or equivalent, C++/Rust, reversible semantics | A small correct transform or invariant check, matched resource results and maintained-project review | Toy gates are not a production compiler; quantum semantics must be understood |
| Runtime / control integration | Scheduling, resource lifetimes, classical/quantum feedback, Linux, timing, instrumentation; embedded/FPGA where relevant | Trace a supported runtime/simulator and reproduce a timing/state failure | Device and real-time work requires authorised lab access and experienced supervision |
| Classical simulation / HPC | Numerical linear algebra, tensor networks, sparsity, parallelism, memory and profiling | Strong classical baseline and a result that explains where approximations fail | Large state-vector size is not proof of quantum hardness; scientific depth varies |
| Application / resource estimation | Precise domain question; state preparation, precision, readout and end-to-end algorithm costing | Reproduce a paper estimate and show sensitivity to assumptions / classical baselines | Chemistry/materials work needs corresponding scientific expertise; QML is not a generic shortcut |
| Algorithm / device / QEC research scientist | Quantum information, complexity/coding theory or experimental physics plus original research | Peer-scrutinised new theory/experiments and a research record | Often a multi-year graduate-level path; a 90-day notebook is not equivalent |

### Targeted live examples and geography constraints

**UK:** Riverlane's directly opened Cambridge Compiler Engineer role asks Python plus C++/Rust, broad compiler/OS/architecture knowledge and interest/experience in LLVM/MLIR. It does not list a PhD as a requirement; it is hybrid, full-time/permanent, advertised £50k–£65k DOE, with an application question about sponsorship rather than an assurance sponsorship is available. This is a tangible software route and one requirement example, not market-wide pay or hiring probability. Its research roles impose different standards. [Official role](https://job-boards.eu.greenhouse.io/riverlane/jobs/4784641101), [official job channel](https://www.riverlane.com/jobs).

**India, academic systems route:** IISc's 2026 CDS admissions page explicitly lists DREAM:Lab research on quantum/classical workflow orchestration across quantum/cloud/HPC as part of NQM, with OS/graph/distributed-systems interview areas and relevant bachelor's/master's background; PhD applicants are preferred. This is a **research-degree** route, not a remote job or a currently open admission deadline. FQCI at IISc is the NQM computing hub; IIT Bombay's separate NQM hub is sensing/metrology. [Official CDS description](https://cds.iisc.ac.in/admissions/research-degrees/), [IISc FQCI announcement, 31 August 2026](https://www.iisc.ac.in/events/foundation-for-qc-innovation-fqci-at-iisc/).

**India, company example:** QpiAI's opened careers page shows onsite experimental-physics, materials, chemistry-intern and RTL roles. It also explicitly sells **quantum-inspired** solutions, which can be classical work. This page does not establish an accessible generic quantum-software vacancy, detailed role criteria, pay, or eligibility; application links lead to a separate platform and were not followed. A company combining AI and quantum does not make every role quantum-computer engineering. [Official page](https://www.qpiai.tech/careers).

Public professional channels are the listed employer/job pages, official group pages and maintained-project issues/discussions. No private contact data, applications or outreach were used. Contacts and institution lists from round 2 need not be duplicated into every technical branch.

## 6. Actual cloud access and cost: a local proof does not need a QPU

IBM's live documentation says Open Plan gives up to ten QPU minutes per rolling 28 days in the supported instance region, with additional-time promotions subject to eligibility/opt-in. A marketing page abbreviates this as “per month”; use the detailed plan rule when planning. Published Pay-As-You-Go starts at US$96/minute, billed per second. These are service terms, not proof the reader's account/country is eligible or has capacity now. [Plan detail](https://quantum.cloud.ibm.com/docs/en/guides/plans-overview), [current product/pricing page](https://www.ibm.com/quantum/products), [usage definition](https://quantum.cloud.ibm.com/docs/en/guides/estimate-job-run-time).

AWS Braket charges separately for task/shots or reserved access, plus ancillary services. Its current table lists IonQ Forte at $0.30/task + $0.08/shot: 2,500 shots would be $200.30 before other charges; error-mitigated IonQ tasks have a minimum shot count. Local simulation differs from billed cloud simulators. Some worked-example wording and arithmetic on the pricing page are inconsistent, so treat the live table and actual confirmed service settings as the authority before spending. No paid run is needed for the proposed project. [Primary pricing](https://aws.amazon.com/braket/pricing/), [batching/retry cost notes](https://docs.aws.amazon.com/braket/latest/developerguide/braket-batching-tasks.html).

**Decision:** start local and CPU-based. If later hardware use would answer a specific unresolved question, recheck available backend, terms, queue, calibration snapshot, supported circuit, estimated shots/retries and a hard spending limit. Then obtain the applicable explicit approval. A cloud run that merely repeats a classically trivial example is educational hardware familiarity, not quantum advantage.

## 7. A concrete 30 / 90 day low-cost proof path

### Choose QEC simulation/decoding as the main experiment

This is one option, not a universal recommendation or claim the reader already has the prerequisites. It tests interest in graph/statistical/systems work without buying a quantum device. Alternative compiler/HPC lanes in the table may fit better after the experiment.

**Prerequisite gate, days 1–7:** explain complex amplitudes, tensor products, measurement, Pauli operators, stabiliser checks, logical observables and why a syndrome does not reveal the encoded state. Reproduce the documented smallest example and trace a single error by hand. If this cannot be explained independently, use the first month to close that precise gap; do not compensate with a dashboard.

**Exact proposed baseline tool versions:** `stim==1.16.0` and `pymatching==2.3.1`, both Apache-2.0 at the checked tags. These are deliberate reproducibility pins, **not a claim both are the newest package-index releases**: GitHub's PyMatching “latest” and package-index/versioned-doc surfaces are not fully synchronised. The chosen 2.3.1 fixes correlated-matching bugs documented by its release. Python/runtime and transitive dependency versions/hashes must be recorded in an approved setup; compatibility has not been tested locally during research. [Stim release](https://github.com/quantumlib/Stim/releases/tag/v1.16.0), [Stim tag licence](https://github.com/quantumlib/Stim/blob/v1.16.0/LICENSE), [PyMatching release](https://github.com/oscarhiggott/PyMatching/releases/tag/v2.3.1), [PyMatching tag licence](https://github.com/oscarhiggott/PyMatching/blob/v2.3.1/LICENSE).

**Why these mature tools:** Stim generates/samples stabiliser circuits and exposes detector error models; PyMatching supplies sparse-blossom minimum-weight matching. Its current public “stable” docs still display 2.1.0, while project material documents newer correlated matching. Verify against the pinned source/API rather than silently mixing tutorials. Stim's circuit model lacks arbitrary non-Clifford operations and supports specified Pauli noise, so a large stabiliser simulation is neither a universal algorithm simulation nor evidence that real leakage/non-Markovian hardware has been modelled accurately. [Stim limits](https://github.com/quantumlib/Stim), [PyMatching documented baseline](https://pymatching.readthedocs.io/en/stable/), [correlated-matching method/API](https://github.com/oscarhiggott/PyMatching/blob/master/README.md), [sparse-blossom primary method](https://arxiv.org/abs/2303.15933).

**Days 8–18, experiment definition:** generate rotated surface-code memory circuits in X and Z bases, distances 3/5/7, fixed 25 rounds, with a declared circuit-level depolarising-noise grid, for example p = 0.001/0.003/0.006/0.01. Freeze reset/measurement/idle noise parameters separately, circuit files, seeds, tool versions and a CPU/RAM budget. These are chosen learning settings, not a hardware calibration or a known threshold claim. Keep actual logical-observable truth available only to the scorer; the decoder receives syndromes and the declared noise model.

**Days 19–30, fair comparison:** compare standard matching with the library's correlated-matching mode on the **same sampled syndromes**. The zero-noise and seeded-single-fault cases are correctness controls; the standard maintained decoder is the meaningful baseline. Hold some seeds and shifted noise settings out from development. Use fixed sample sizes for final confidence intervals; a feasible target is 100,000 shots per configuration after a smaller development run, with a total local compute cap declared before execution. If the cap is insufficient, reduce the preregistered grid and disclose it rather than cherry-pick successful curves.

**Acceptance evidence by day 30:**

- A manifest reproduces circuit, noise, seed and scorer without hidden manual choices; zero-noise controls have no unexplained logical failures.
- Report total shots and logical failures per configuration, interval method, paired decoder disagreement and failures kept in the denominator. Zero observed errors is not zero risk; at fixed n=200,000 independent shots the one-sided 95% binomial upper bound is about 1.5×10⁻⁵.
- Separate graph/model construction, sampling, decode throughput, batch size, single-shot latency distribution and peak memory. Do not relabel batched throughput as feedback latency.
- Explain where correlation-aware matching improves error rate and where its added cost does not help. “No improvement under these conditions” is a valid result.
- Produce one failure trace showing syndrome, decoder prediction and scorer-only truth. An experienced reviewer can reproduce it from the written instructions after authorised setup.

**Days 31–60, choose one deeper question:**

1. **Noise mismatch:** alter spatial rates, measurement bias or specified Pauli correlations after fixing a nominal decoder. Compare uncalibrated and recalibrated weights on separate calibration/evaluation streams. Do not call this realistic leakage or a physical noise model without evidence.
2. **Streaming/runtime:** build a bounded syndrome replay interface, ordering, backpressure and latency instrumentation around existing decoding. Report serial/parallel windows, queue backlog and lost frames; do not invent a real-time guarantee from a laptop benchmark.
3. **Reproduction/debugging:** reproduce a documented library regression or a small published decoder benchmark at matched versions/noise; add a minimal failing case and verify the correction. Don't invent a novel decoder merely to claim novelty.

**Days 61–90, reality and contribution gate:** reproduce an independent reference result; use a genuinely public measured-syndrome dataset only after its version/licence/access is verified; compare synthetic and measured behaviour without silently fitting the evaluation data. Prepare a concise report with limitations, an adverse regime, baseline, speed/error/memory frontier and one bounded proposed fix. Seek expert review or contribute only through an authorised later action. A real hardware/controller collaboration is a later access gate, not a promise this project provides it.

**Kill/narrow criteria:** foundational concepts remain opaque; the work is unappealing; headline improvements vanish under matched conditions; gains depend on scorer leakage, selected errors or a misspecified baseline; no meaningful gap exists beyond mature tools; the runtime/interface is merely a tutorial wrapper; or available UK/India routes require unacceptable relocation/credentials. Keep the transferable statistics/C++/profiling contribution even if the quantum career bet is rejected. Do not spend on a QPU to rescue an unclear research question.

## 8. Toward strong expertise by 2031: observable gates

1. Independently explain and reproduce one method, including a result that failed and why.
2. Make a small useful contribution another maintainer/researcher can validate; accepted review matters more than framework count.
3. Own correctness/performance across changes in one compiler/decoder/simulation/runtime subsystem, with reproducible releases and failure diagnosis.
4. Earn authorised exposure to the hardware/domain constraint the software serves, working with experienced specialists rather than treating simulation as reality.
5. Produce an original scrutinised improvement that survives a strong baseline and remains useful to others; mentor and lead decisions across teams.

These gates can support a compiler/platform/research-engineering leadership route. Quantum-theory/experimental-science leadership requires its own sustained research depth. Neither route guarantees prominence, pay or employment. Preserve a classical systems/numerical speciality so the investment remains useful if quantum adoption is slower, narrower or more concentrated than expected.

## Audit limits and next unresolved tests

- Today's Quantinuum memory announcement needs the full experimental protocol, code distances, cycle/gate duration, shot counts, intervals, acceptance/discard rules, decoder details, drift and all-cost accounting. Cross-modality record ratios should not be treated as directly comparable full-computation performance.
- Retrieve and read the exact Google correction and data licence; do not imply these were reanalysed.
- Full September Helix appendices, latest independent replications and a representative range of superconducting, ion, atom and photonic systems remain incomplete. Annealing/sensing/communication are different branches, not substitutes for a general fault-tolerant computing claim.
- Audit current algorithm resource estimates beyond factoring, including state preparation and strong classical methods. No broad commercial-return result or total job-market forecast is established here.
- Read more India intermediate systems/compiler/control vacancies and their actual degree/onsite/eligibility filters. NQM funding goals and quantum-inspired consulting are not measured quantum-hardware-software hiring demand.
- Replicate the new AI circuit-design results independently, audit evaluator leakage/coverage, total search compute, baseline tuning and physical fault-tolerant cost; a selected eight-task result does not settle scientist replacement.
- Verify every chosen tool/environment version and the selected release's known issues during an approved implementation. The proposed project was not installed or run in this research pass.
