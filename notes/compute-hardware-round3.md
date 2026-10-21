# Compute hardware and unconventional computing: software opportunities after a system-level audit

Cutoff: 19 October 2026. Scope: memory/interconnect/accelerators, photonic computing, analog/in-memory computing and neuromorphic systems. Quantum is deliberately separate. This extends the systems research without repeating its general compiler/database overview. No software/model/data downloads, installations, hardware purchases, rented compute, private access, outreach or external writes occurred. All projects are proposed; none was executed here.

## Decision-relevant finding

The strongest accessible career path is **software that makes specialised hardware useful, testable and economically credible**: workload characterisation, kernels/operator support, simulation, firmware/control, numerical validation, profiling and systems integration. This can benefit from both conventional accelerator growth and unconventional hardware. It does not require personally inventing a device or building a fabrication company.

The fields are at different stages. Conventional accelerators, HBM and optical communications have commercial deployments. Photonic computation has peer-reviewed hardware demonstrations, research installations and early commercial agreements, with software access improving. Analog in-memory and large neuromorphic systems have meaningful prototypes and research infrastructure; selected commercial products exist, but that does not establish a broad profitable application market. These are evidence-based stage judgments, not a claim that any technology will or will not win by 2031.

The best hedge for an application/AI developer is an independently useful systems skill plus one carefully selected experimental hardware ecosystem. A career should not depend on a single vendor’s TOPS/W headline or roadmap.

## 1. An evidence ladder for hardware claims

Different claims require different evidence:

1. Device/circuit demonstrated: a physical primitive works, possibly on a small array and under controlled conditions.
2. Integrated accelerator demonstrated: conversion, control and some memory are integrated; identify operations still handled externally.
3. Full application demonstrated: quality, latency and resource accounting cover the relevant model/workload, not only its favourable kernel.
4. Product available: an orderable or deployed system with supported software, documented restrictions and lifecycle terms.
5. Commercial operation: named deployment, repeat use or recognised revenue; a partnership, evaluation kit or signed future capacity agreement is weaker evidence.
6. Attractive economics: whole-system cost, utilisation, maintenance, yield/support and customer value support continued adoption.

A simulator is useful evidence about a model and software contract; it is not a measurement of fabricated hardware performance or energy. A fabrication/production announcement and a benchmark’s “available” classification can refer to different stages.

## 2. What is shipping, deployed, demonstrated or still promised

| Family | Primary dated evidence | What is established | What must not be inferred |
| --- | --- | --- | --- |
| CPU/GPU baseline and public comparison | [MLPerf Inference v6.1 announcement, 16 September 2026](https://mlcommons.org/2026/09/mlperf-inference-v6-1-results/) and [working-group analysis, 17 September](https://mlcommons.org/2026/09/chairs-mlperf-inference-v6-1/) | Standardised system results, with availability categories and workload/quality/latency rules. This round includes available and preview systems; the announcement explicitly labels Rubin/Vera Rubin NVL72 preview. | Fastest submitted result is not automatically lowest cost or best for a different batch, model, latency target or quality requirement. Participation is not a market-share census. |
| HBM and memory integration | [Samsung HBM4 announcement, 12 February 2026](https://news.samsungsemiconductor.com/global/samsung-ships-industry-first-commercial-hbm4-with-ultimate-performance-for-ai-computing/) reports mass production and customer shipments. | Vendor-reported commercial shipment of a memory component. | Shipment of HBM does not establish a particular full accelerator’s generally available status, memory utilisation, yield or software performance. |
| Memory pooling/chiplet standards | [CXL consortium’s 4.0 recap](https://computeexpresslink.org/blog/introducing-the-cxl-4-0-specification-webinar-qa-recap-4386/) records the November 2025 specification; [UCIe’s release list](https://www.uciexpress.org/press-releases) records 3.0 on 5 August 2025. | New standards and manageability/memory-fabric design space. | A published specification does not mean corresponding products are deployed. Keep protocol version, physical device, firmware, OS and application support separate. |
| Optical interconnect/CPO | [NVIDIA announcement, 31 May 2026](https://nvidianews.nvidia.com/news/vera-rubin-full-production-agentic-ai-factory) describes Spectrum-X Ethernet Photonics as in production. | A vendor reports production of optical networking alongside a platform ramp. | This is optical data movement, not proof that general neural-network arithmetic is performed optically. Its platform production language should not replace MLPerf’s separate preview/available classification. |
| Alternative digital accelerator | [Tenstorrent Galaxy Blackhole GA, 28 April 2026](https://tenstorrent.com/en/newsroom/tenstorrent-enables-ai-at-scale-with-industry-leading-performance). | Vendor reports general availability and deployment at scale, with open software integration. | Claims such as broad Hugging Face compatibility or leadership performance were not independently tested here. Supported operators, numerical quality and actual workload performance still need evaluation. |
| Wafer-scale digital compute | [Cerebras CS-4 architecture account, 25 August 2026](https://www.cerebras.ai/blog/ultrafast-frontier-inference-cerebras-deep-dive-at-hot-chips-2026) and [Q2 results, 12 August](https://cerebras.gcs-web.com/news-releases/news-release-details/cerebras-systems-fast-inference-cloud-business-nearly-quadruples) | The vendor has recognised commercial revenue and an operating inference business; it introduced a new rack architecture. | The newest announced system, future racks and contracted MW are not automatically all installed or available. SRAM-rich/wafer-scale digital design is not analog memory or photonic computation. |
| Photonic interposer | [Lightmatter Passage M1000 EVK](https://lightmatter.co/products/passage-m1000-evk/) says the kit is deployed in its validation datacentre. | Product/validation infrastructure and an optical interconnect development path. | An internal validation deployment does not establish mass customer deployment or a generally available optical arithmetic engine. |
| Photonic arithmetic | [PACE Nature paper, 9 April 2025](https://www.nature.com/articles/s41586-025-08786-6) and [Lightelligence PACE2 product page](https://www.lightelligence.ai/products/photon-computing/pace2) | A measured integrated accelerator paper; PACE2 is described as a released card with a 128×128 optical matrix and PCIe interface. | A request-information product page is not an independently verified shipment count, revenue result or general LLM benchmark. The PACE paper and PACE2 are different hardware generations. |
| Photonic co-processor deployment and accessible SDK | [Q.ANT LRZ deployment, 17 March 2026](https://qant.com/press-releases/higher-performance-less-energy-q-ant-deploys-second-generation-photonic-processors-at-supercomputing-center-lrz/), [IONOS agreement, 19 May](https://qant.com/news/q-ant-takes-photonic-ai-computing-commercial-as-ais-power-demand-surges/) and [SDK release, 23 September](https://qant.com/press-releases/q-ant-launches-world-first-open-source-sdk-for-photonic-computing/) | Vendor reports research-centre installations and a first commercial-customer agreement. Public C/Python software and a CPU simulation backend are available. | The September release still describes cloud hardware access in subsequent months. No claim of generally available IONOS hardware access was verified. Vendor cross-platform efficiency claims remain claims without the full comparison reproduced. |
| Analog/phase-change-memory inference | [IBM ALBERT hardware paper, 30 September 2025](https://www.nature.com/articles/s41467-025-63794-4) | Physical PCM inference chip running the relevant weight layers, with measured task accuracy and drift effects. | This is not a shipping general-purpose LLM replacement. Attention, activations and other work remain on a control computer; see the scope audit below. |
| Research neuromorphic systems | [Intel Hala Point announcement, 17 April 2024](https://newsroom.intel.com/artificial-intelligence/intel-builds-worlds-largest-neuromorphic-system-to-enable-more-sustainable-ai) and [Loihi 2 technical brief](https://www.intel.com/content/dam/www/central-libraries/us/en/documents/neuromorphic-computing-loihi-2-brief.pdf) | Sandia research deployment; a developer/research community and restricted hardware-access route. | Research deployment and open framework availability do not imply retail Loihi availability or a broad commercial replacement for dense models. |
| Commercial neuromorphic activity | [BrainChip H1 2026 report, 26 August 2026](https://investor.brainchip.com/wp-content/uploads/2026/09/2026-08-26-June-2026-half-yearly-report.pdf) | Recognised product, licence and development-services revenue; developer/evaluation products are described through its official channels. | Partnerships and new-product announcements are not large recurring production revenue. Revenues are small relative to research/operating expenditure; see economics below. |

## 3. Full-system audit: what efficiency headlines can hide

### Compare a complete contract

Use the same task and acceptance quality, not only nominal operation count. Record model/version, precision and sparsity, input/output lengths, batch/concurrency, latency deadline, throughput/goodput, warm-up, device count, host, memory, interconnect, software versions and availability class. A custom recurrent model with fewer parameters is a valid research approach; comparing it to another architecture requires checking equal task quality and total training/deployment cost.

For energy, define a boundary before counting: accelerator-only, board, host/system, or facility. Include relevant conversion, memory, control, interconnect, laser/thermal stabilisation and idle allocations without double-counting overlapping measurements. Facility overhead should be labelled separately. If only operation counts or simulator estimates exist, report them as proxies/estimates rather than measured joules.

For latency, distinguish kernel time from the critical path containing queueing, preprocessing, transfers, accelerator work, unsupported operations, output handling and possible recalibration. Overlapping stages cannot simply be summed as if sequential. For business economics, include hardware amortisation/rental, utilisation, energy, integration, support, retraining/calibration, lifecycle changes and failure recovery.

### Three concrete boundaries from research

**PACE:** the [2025 Nature paper](https://www.nature.com/articles/s41586-025-08786-6) describes a 64×64 photonic accelerator for a recurrent Ising solver. It reports approximately 4.21 TOPS/W excluding lasers and 2.38 including them. Its comparison uses a particular algorithm/workload against an NVIDIA A10, not a current general AI service. The paper also distinguishes advertised/possible cycle latency from the tested convergence setting and reports different iteration counts. Do not label the result a universal GPU replacement or full-datacentre efficiency result.

**IBM ALBERT:** the [2025 paper](https://www.nature.com/articles/s41467-025-63794-4) maps 7.1 million unique analog weights shared across 12 layers onto a chip. The study reports near-reference accuracy, hardware-aware fine-tuning benefits and recalibration mitigating drift. It explicitly implements attention, vector operations, pooler and classifier off-chip on a control computer. A successful full-model accuracy demonstration is not evidence that every operation or its entire energy/latency path is on the analog chip.

**Analog foundation models:** [IBM’s NeurIPS 2025 publication](https://research.ibm.com/publications/analog-foundation-models) addresses analog noise and quantisation through model adaptation. This is meaningful progress, and also evidence that deploying an off-the-shelf model unchanged is not a solved assumption. The [research code](https://github.com/IBM/analog-foundation-models) includes synthetic-data generation and distributed retraining; reproducing a paper’s entire training procedure is materially different from running a small simulator example.

### Digital baselines are moving too

The competitor is a well-tuned contemporary CPU/GPU/NPU implementation, including efficient batching, quantisation and memory placement—not a naive CPU loop or an old GPU implementation selected only because it loses. Conversely, an edge task with continuous sparse sensor input should not be forced into a large dense-batch benchmark that erases its use case. Match the real operating regime, then disclose where each design wins or loses.

Illustrative reasoning, not a measured result: accelerating 90% of elapsed work by 100× produces only about 9.17× whole-job speedup if the other 10% is unchanged and stages are sequential. Conversion or transfer becoming dominant is a predictable reason a device headline does not transfer to a product.

## 4. Software opportunity map: specific bottlenecks and prerequisites

### Memory/interconnect and conventional accelerators

- Memory-bound model phases → weight/KV movement and allocation → layout, tiling, precision and placement → utilisation under the real latency target.
- Chiplet/CXL/optical fabric → topology and interface contracts → firmware/driver and RAS/telemetry → failure/recovery and cross-version compatibility → application-level benefit.
- A mature entry path is an operator/kernel, workload profiler, simulator correlation or supportability problem. Foundry and packaging physics remain different specialties.

### Photonic interconnect versus photonic compute

- Interconnect: optical/electrical boundaries → laser and thermal control → link health, error correction and diagnostics → packaging/serviceability → network/application behaviour.
- Compute: supported primitive/precision → mapping and unsupported operators → calibration and drift → conversion/host bottlenecks → quality and whole-workload economics.
- Software-accessible work includes CPU simulator correctness, framework bridges, workload mapping, firmware/control and hardware-in-loop automation. Designing a PIC, obtaining a foundry PDK or validating fabricated devices usually needs specialised institutional/company access.

### Analog/in-memory computation

- Device model → write/programming variability and drift → ADC/DAC precision and clipping → layer mapping/tiling → hardware-aware training/recalibration → end-to-end quality/cost.
- The [IBM IMW 2026 paper](https://research.ibm.com/publications/analog-in-memory-computing-for-large-language-model-inference-opportunities-and-challenges) explicitly frames this as a heterogeneous-system problem, covering architecture and operations that fit AIMC.
- Algorithm/software contributions can test robust training, noise models, calibration, numerical validation and simulator/runtime interfaces. Materials/device fabrication and circuit characterisation need a substantially different laboratory skill path; the phrase “in-memory” does not remove those requirements.

### Neuromorphic/event-based computation

- Task with temporal/sparse input → encoding and state → model training/learning rule → mapping and numerical semantics → sensor/runtime/hardware integration → measured task outcome.
- [NeuroBench, published 11 February 2025](https://www.nature.com/articles/s41467-025-56739-4?error=cookies_not_supported), separates algorithm and system benchmarking. [NIR, published 16 September 2024](https://www.nature.com/articles/s41467-024-52259-9), provides an interoperability representation, rather than forcing every contribution to invent a new chip.
- Software opportunities include portable model representations, event preprocessing, reference semantics, benchmark metrics and hardware mapping. Low spike count is not measured low power; all encoding, host and communication work must be considered.

## 5. Vendor economics and technical career risk

Commercialisation should be assessed separately from technical merit. BrainChip’s [H1 2026 filing](https://investor.brainchip.com/wp-content/uploads/2026/09/2026-08-26-June-2026-half-yearly-report.pdf) reports **US$1,222,745 revenue** and **US$12,015,897 net loss** for the half-year. Revenue includes US$110,362 product sales, US$613,826 licences and US$498,557 development services. These are actual disclosed figures, not a conclusion about future failure or viability. They show why evaluation products and partnerships should not be mistaken for a large mature product market.

Cerebras’s [12 August 2026 results](https://cerebras.gcs-web.com/news-releases/news-release-details/cerebras-systems-fast-inference-cloud-business-nearly-quadruples) report US$180.1 million GAAP quarterly revenue, separately presenting US$209.9 million non-GAAP “core” revenue. Its advertised 600 MW under contract is not a measurement of currently operating capacity. The GAAP/non-GAAP distinction matters when assessing a vendor’s commercial claims. A large technical performance number is not itself evidence of profitability, customer diversification or a stable hiring budget.

For an employer/startup bet, investigate supported customer workloads, actual deployments and renewals, software maturity, hardware access, supply dependencies, integration burden and the role’s funded scope. Private vendors’ revenue/unit economics were not generally available in this pass. Funding raised, a valuation, a standard release and a tapeout are not interchangeable with recurring commercial demand. This is career/business assessment, not an investment recommendation.

## 6. Concrete teams, researchers, labs and professional channels

No person or organisation was contacted. Names identify relevant public work; they are not implied mentors, recruiters or available collaborators. Use official role, project or institutional channels after an authorised contribution or enquiry is prepared.

| Team/lab and relevant public work | Specific skill/contribution fit | Public professional route and access caveat |
| --- | --- | --- |
| MLCommons Inference community | Reproducible measurements, workload rules, quality/latency and availability metadata; benchmark-tooling contributions. | [Reference implementations](https://github.com/mlcommons/inference), [v6.1 submitted results](https://github.com/mlcommons/inference_results_v6.1) and their contribution guidance. Results can be inspected without owning a rack. |
| Tenstorrent accelerator/system software | Operator/kernel support, memory movement, firmware compatibility, simulation and validation. | [TT-Metal/TTNN](https://github.com/tenstorrent/tt-metal) lists community and contribution routes. Hardware is required for real device measurements; CPU reference tests remain useful initial work. |
| Q.ANT software team; Utz Bacher is identified as VP Software in the September SDK release | Photonic API/simulator, framework bridges, numerical/capability tests and workload examples. | [Native computing toolkit](https://github.com/Q-ANT-GmbH/qant_native_computing_toolkit), public issues/discussions and [examples](https://github.com/Q-ANT-GmbH/qant_native_computing_toolkit_examples). CPU backend is accessible; hardware availability remains a separate gate. |
| Lightmatter hardware-software teams | Photonic control, diagnostics, firmware and HIL rather than a generic chatbot integration. | [Firmware automation role](https://job-boards.greenhouse.io/lightmatter/jobs/5447431008?gh_jid=5447431008) and [laser-control software role](https://job-boards.greenhouse.io/lightmatter/jobs/5419848008?gh_jid=5419848008) show official hiring channels. Geography/lab access matters. |
| Optalysys, UK | Full-system simulation, frameworks, profiling/cost models and photonic control-plane interfaces. | [Official careers](https://optalysys.com/careers/) and its published recruitment channel. A UK-remote role is not worldwide remote. |
| IBM Analog AI; Abu Sebastian, Julian Büchel and Manuel Le Gallo appear in the cited research | Hardware-aware training, noise/calibration models, inference mapping and numerical validation. | [AIHWKit](https://github.com/IBM/aihwkit) provides public issue/contribution guidance and an official team contact. Paper/repository access is not automatic access to physical PCM devices. |
| Intel neuromorphic community/Lava; NeuroBench and NIR contributors | Portable event models, numerical semantics, system-aware metrics and CPU/neuromorphic interoperability. | [Lava](https://github.com/lava-nc/lava), [NeuroBench](https://github.com/NeuroBench/neurobench) and [NIR](https://github.com/neuromorphs/NIR). Intel brief describes research-community hardware access; some components are gated. |
| IISc NeuRonICS; Chetan Singh Thakur is represented in the lab’s publications | Brain-inspired algorithms, ASIC/FPGA, analog systems and event sensors; RAMAN/Aryabhat are named research platforms. | [Lab](https://labs.dese.iisc.ac.in/neuronics/) and [publications](https://labs.dese.iisc.ac.in/neuronics/publications/) provide opportunities/institutional routes. Actual openings, degrees, funding and device access must be checked separately. |
| IIT Madras RISE/SHAKTI | RISC-V software/OS/toolchain, SDK and verification can form an India-based open-computing route. | [Official getting-started page](https://shakti.org.in/getting_started.html) lists public forum, SDK and supported OS routes. Core licence and tool/dependency licences differ; no board acquired. |
| Manchester SpiNNaker facility; Andrew Rowley is listed as core facility lead | Event simulation, runtime, packet-routing and mapping; a real research machine rather than an invented future product. | [Official facility page](https://research.manchester.ac.uk/en/equipments/spinnaker-1million/) lists a shared facility contact. Access is an institutional/allocated-resource question, not assumed free cloud availability. |
| Bristol Centre for Supercomputing | Contemporary CPU/GPU baseline, research software and whole-system performance/energy work. | [Official system/account of user experience](https://www.bristol.ac.uk/research/centres/bristol-supercomputing/articles/2025/lifting-the-lid-on-isambard-ai.html) and institutional channels. Access eligibility/calls must be checked currently; old workshops are not current open allocations. |

### Hiring requirements: deliberately small, primary-source sample

- [Optalysys Simulation & Frameworks role, August 2026 PDF](https://optalysys.com/wp-content/uploads/2026/08/Software-Engineer-Simulation-Frameworks-job-spec.pdf): UK remote with travel; senior/principal; 10+ years C/C++ or Python, event simulation, SoC/memory architecture, tests/specifications and framework integration. This is a software path without a stated mandatory photonics PhD, but it is not an entry-level role.
- [Optalysys Silicon Photonics role, October 2026 PDF](https://optalysys.com/wp-content/uploads/2026/10/Senior-Silicon-Photonics-Engineer-WDM.pdf): onsite Leeds; MSc/PhD in a relevant subject, successful tapeouts, foundry PDK/layout/simulation, device variation and optical characterisation. This illustrates why device research is a different prerequisite path.
- [Tenstorrent CPU Core Verification, Bengaluru](https://job-boards.greenhouse.io/tenstorrent/jobs/5140149007): a direct Indian hardware-validation route, hybrid rather than generic worldwide remote work. The broader [performance-modelling architect role](https://job-boards.greenhouse.io/tenstorrent/jobs/5165938007?gh_src=Eclipse+job+board) is US-based and asks for 8+ years plus real architectural modelling; its export eligibility language must not be ignored.
- [Lightmatter firmware automation role](https://job-boards.greenhouse.io/lightmatter/jobs/5447431008?gh_jid=5447431008): Toronto, 8+ years embedded software, a previously built/adopted HIL framework, strong Python and cross-layer diagnostics. This is evidence that photonics needs serious software infrastructure, not evidence of India/UK remote eligibility.

The sample proves these work categories exist, not their national vacancy counts, relative pay, entry probability or 2031 headcount.

## 7. Papers, code, data and licence audit

Technical papers below are useful for their demonstrated scope and methods; they were not reproduced. Code/data licences are independent of paper access or model-weight licences. No dataset or model was downloaded.

| Resource | Checked status/licence | Use and limit |
| --- | --- | --- |
| [MLPerf inference code](https://github.com/mlcommons/inference) and [v6.1 results](https://github.com/mlcommons/inference_results_v6.1) | Code core Apache-2.0. Submissions/models/datasets can have separate terms. | A baseline contract and auditable result metadata; do not imply an unofficial run is an official submission. |
| [TT-Metal/TTNN](https://github.com/tenstorrent/tt-metal) | Apache-2.0 core; repository identifies separately licensed bundled libraries. | Hardware-specific kernel/operator work and support matrix. |
| [Tenstorrent firmware release history](https://github.com/tenstorrent/tt-firmware/releases) | Old repository is archived; follow current project links when implementing. | January/February 2026 notes say P150 support changed from 140 to 120 cores and applications depending on grid layout may need changes. Physical products have real software compatibility/lifecycle work. Vendor’s 1–2% typical impact was not reproduced. |
| [Q.ANT native toolkit](https://github.com/Q-ANT-GmbH/qant_native_computing_toolkit) | Apache-2.0 core; separate third-party licence file and hardware drivers. | C/Python API and CPU backend without Q.ANT drivers; CPU execution proves software semantics, not hardware efficiency. |
| [IBM AIHWKit](https://github.com/IBM/aihwkit) | MIT core. | Noise/device simulation and hardware-aware learning; simulator assumptions need sensitivity tests. |
| [Analog Foundation Models, NeurIPS 2025](https://research.ibm.com/publications/analog-foundation-models) and [code](https://github.com/IBM/analog-foundation-models) | Code MIT; model, data-generation inputs and pretrained-weight terms remain separate. | Adaptation under analog noise/precision. Published foundation-model retraining is not a free CPU-scale experiment. |
| [IBM ALBERT PCM paper, 30 September 2025](https://www.nature.com/articles/s41467-025-63794-4) | Peer-reviewed physical experiment; data/artefact terms need per-item review. | Read its off-chip computation, selected task samples and drift-compensation methods, not only abstract accuracy. |
| [PACE Nature paper, 9 April 2025](https://www.nature.com/articles/s41586-025-08786-6) | Peer-reviewed integrated accelerator experiment; source data are listed; other requests can be subject to IP/confidentiality. | Laser-inclusive energy, calibration, iteration-to-solution and the exact A10 comparison. Open access is not blanket permission to use proprietary hardware designs. |
| [NIR Nature Communications paper, 16 September 2024](https://www.nature.com/articles/s41467-024-52259-9) and [reference implementation](https://github.com/neuromorphs/NIR) | Reference implementation BSD-3-Clause. | Cross-platform primitives and numerical/temporal semantics. Model compatibility must be tested, not inferred from a format conversion succeeding. |
| [NeuroBench paper, 11 February 2025](https://www.nature.com/articles/s41467-025-56739-4?error=cookies_not_supported) and [harness](https://github.com/NeuroBench/neurobench) | Harness Apache-2.0; each task’s datasets need separate terms. | Algorithm/system comparison, quality and resource metrics; algorithm operation counts are not measured energy. |
| [Lava](https://github.com/lava-nc/lava) | High-level BSD-3; lower-level mapping/runtime components LGPL-2.1; some Loihi support may remain proprietary/gated. | CPU-first neuromorphic software development with explicit hardware-access limits. |
| [SHAKTI](https://shakti.org.in/getting_started.html) | Site describes processors under BSD-3; SDK/tools need individual licence checks. | India-based RISC-V learning/contribution. Open source does not make a physical board or fabrication run free. |

## 8. Proposed 30/90-day projects with measurable rejection criteria

Select one main project and one small comparison experiment. Use existing approved tools first; obtaining new software, model weights, data, hardware or rented resources must be separately authorised when implementation is requested. Metrics below are evaluation designs, not claimed achieved improvements.

### H1 — Hardware-claim auditor and whole-workload baseline

**First 30 days:** choose one task and create a machine-readable comparison contract: model/quality, precision, batch, latency, device count, host, memory, interconnect, availability and power boundary. Inspect a small set of public MLPerf submissions and one paper/vendor claim. Reproduce only a workload that fits existing approved hardware; otherwise produce a reproducibility audit with a clear “not run” state. Record preparation, compile/warm-up, preprocessing, device and output time separately.

**By 90 days:** compare two available execution paths or obtain authorised hardware access for the second. Use a held-out workload distribution, repeated runs, confidence/noise reporting and error checks. Produce a report and reusable metadata validator that rejects comparisons with mismatched quality/availability/boundaries.

**Reject/limit:** no end-to-end accuracy contract; unavailable software/data; unfair unoptimised baseline; absent host/laser/conversion energy; no actual power measurement. A valid outcome may be “claim cannot be compared,” not a forced ranking. Original contribution: better audit tooling, a benchmark ambiguity fix or a carefully documented negative result.

### H2 — A photonic software port with a CPU reference

**First 30 days:** after any needed installation approval, use Q.ANT’s CPU backend and a small self-generated approximation/classification task. Implement identical input/output tests in a normal reference. Compare quality, parameter count, supported operations, numerical range and training steps. Establish which example comparisons change model architecture rather than only hardware.

**By 90 days:** create out-of-range, precision, shape and state tests; document unsupported operations and host fallback. If authorised hardware becomes available, correlate the simulator with actual outputs/latency and full power boundary. Until then, retain a software-compatibility result and a hardware-validation plan.

**Reject/limit:** simulator speed used as hardware speed; smaller model claimed better without equal task quality; no account of host fallbacks, drivers or hardware access. Original contribution: an API conformance test, numerical corner case, reference workload or framework bridge with clear semantics.

### H3 — Analog noise/precision and adaptation break-even experiment

**First 30 days:** on an approved CPU/small model, compare an ordinary digital baseline, a low-precision digital baseline and a parameterised analog-noise simulation. Use owned/self-generated data. Sweep clipping, quantisation, programming error, drift and recalibration assumptions; track quality across seeds and distributions. Do not download/retrain a foundation model just to start.

**By 90 days:** implement one calibration or hardware-aware adaptation method and test a different distribution/noise setting. Record added training/calibration time, dataset preparation and inference overhead. If measured energy exists, calculate a break-even inference count from incremental adaptation energy divided by positive per-inference savings, with the scope/uncertainty stated. Without measured hardware energy, present sensitivity estimates rather than savings claims.

**Reject/limit:** improvement disappears against the low-precision digital baseline; adaptation cost is omitted; a favourable noise model is selected after seeing outcomes; simulator performance is presented as silicon performance. Original contribution: model-validation evidence, robust calibration, a failure taxonomy or an independently useful simulator test.

### H4 — Event-based task with a genuinely fair conventional baseline

**First 30 days:** use a self-generated temporal-event task or an already authorised benchmark dataset. Compare a simple event-driven conventional algorithm, a compact ANN and an SNN at the same task quality/deadline. Include encoding and all input events, not only useful spikes. Track accuracy/false alarms, detection latency, state memory and workload activity.

**By 90 days:** test temporal jitter, noise, burst density and distribution shift. Export/import through NIR where applicable and compare simulator semantics. With approved hardware access, measure the whole sensor/host/device path; otherwise report only algorithm/resource results. A benchmark contribution can add a missing metric or portability test.

**Reject/limit:** SNN only beats an oversized dense baseline; off-chip encoding/training cost disappears; operation/spike counts are called watts; model export silently changes time constants or numerical behaviour. Leadership evidence: explain the exact task regime in which event-driven computation earns its integration cost.

### H5 — Memory/interconnect sensitivity and simulator correlation

**First 30 days:** choose a workload with compute and movement phases. Build a transparent analytical/discrete-event model using generated traces: compute rate, memory bandwidth/capacity, transfer/queue latency, contention and unsupported work. Calibrate against an existing available machine and show error bars. No assumption that a specification’s peak bandwidth is sustained application bandwidth.

**By 90 days:** compare a layout/placement/partitioning change with a hardware-upgrade scenario. Validate on an unseen trace and, if authorised access exists, a second device. Identify where a CXL/optical/HBM change affects the critical path versus merely moving the bottleneck. Keep modelled and measured results separate.

**Reject/limit:** model cannot predict a held-out case; ignores occupancy/contention/queueing; improvement relies on unrealistically perfect overlap or utilisation. Original contribution: better trace reduction, model calibration or workload map that gives a hardware team an actionable decision.

### H6 — Photonic control/firmware validation without inventing device results

**First 30 days:** define a simulated control/telemetry interface with drift, sensor faults, link resets, missing samples and version changes. Build tests for state transitions, settling criteria, saturation, bounded recovery and diagnostics. Use an explicit plant/noise model and state that it is hypothetical unless validated against public measured data.

**By 90 days:** with authorised team/lab access, correlate the model against real hardware and convert fixtures into a repeatable HIL workflow. Track false alarms, missed failures, recovery time, test coverage and developer adoption. Without real hardware, deliver the software harness and quantified validation gap rather than a calibrated-device claim.

**Reject/limit:** no independently justified plant model; real behaviour cannot be reproduced; tests mirror implementation; hidden manual steps prevent reliable runs. Original contribution: a reusable fault-injection/diagnostic fixture or evidence that catches a real firmware regression. This maps to observed photonic software roles more directly than learning fabrication from scratch.

## 9. Skill transfer and leadership by 2031

The portable sequence is: numerical/performance literacy → workload and boundary discipline → one hardware ecosystem → reproducible contribution → ownership of a subsystem’s correctness and economics. For a developer, original work can be an operator implementation, numerical bug, compatibility test, simulator-correlation improvement, workload reduction, control/diagnostics tool or fair benchmark. It need not be a new semiconductor process.

Retain an independent transfer test after AI-assisted implementation: change shape, precision, input density, memory budget, grid size or fault timing, predict what should change and explain the observed difference. Use AI where it helps, while keeping executable/reference/model oracles strong enough to detect plausible but wrong code. No evidence here establishes that semiconductor software is immune to AI automation; engineering economics and validation requirements remain real constraints.

An appropriate leadership artefact is a reviewable technical decision that changes hardware/software design or deployment: the measured bottleneck, alternatives, numerical contract, uncertainty, cost consequence and rejection criteria. Respectful upstream reviews and useful maintenance establish credibility over time. None was submitted during this research.

## Remaining gaps and next targeted checks

- Verify Q.ANT’s actual current cloud access, pricing and supported hardware workloads; its September release still describes future access. Do not treat an API or press agreement as a live service test.
- Seek independent, same-quality whole-system comparisons for photonic/analog devices against contemporary digital implementations. The source set is rich in vendor and laboratory evidence, thinner on broad commercial fleet economics.
- Confirm PACE2 hardware shipment/revenue/support availability and avoid reusing PACE1 paper numbers as PACE2 facts. No device was accessed here.
- Obtain project-specific foundry/PDK and hardware-access restrictions only if pursuing device work. The role samples distinguish software, circuit/PIC and fabrication paths; they do not cover every route.
- Hardware/model/data licences and benchmark rules need rechecking at a chosen implementation version. Core repository licences do not automatically cover pretrained weights, proprietary extensions, drivers, devices or benchmark datasets.
- Public job descriptions are a small nonrepresentative sample. Country eligibility, sponsorship, export controls, headcount funding and actual entry/mid-level opportunities remain separate checks.
- One large Cerebras filing could not be opened because of its size; the smaller current earnings release was used instead. Some Nature direct pages had cookie/redirect errors; indexed primary text and accessible relevant paper sections were used, and no full reproduction is claimed.
