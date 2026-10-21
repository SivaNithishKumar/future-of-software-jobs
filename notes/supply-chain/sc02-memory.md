# SC02 — Memory supply and the software work around it

Memory is a useful systems specialism, but a career bet on a permanent shortage is poorly supported. The strongest practical route is learning to identify a workload’s actual capacity, bandwidth, latency and correctness constraint, then testing the native solution before adding custom work. Supplier capacity expansion and software efficiency can both relieve a bottleneck; either can also move it elsewhere. Neither establishes a2031 vacancy count or a durable human moat.

This report answers two separately prespecified questions. A audits memory types and qualified supply. B examines substitution, relief and software work at the application boundary. Three queries and six deliberately selected official surfaces were used; the budget is closed. A low-yield Micron landing page counts among the six. Same-document windows are not independent sources. No code, data, models, SDKs, devices, accounts or native workloads were acquired or run.

## A. “Memory” is several different constraints

The table is an engineering orientation, not a set of current per-part latency measurements. No SRAM or GDDR SKU datasheet was audited in this bounded pass.

| Type | Role in a system | What a substitution claim must preserve |
| --- | --- | --- |
| SRAM | Volatile on-chip caches and scratchpads; locality and short access latency, with limited die-area capacity. | More externalGB does not supply the same locality. Cache misses and reuse matter, not just total memory. |
| DDR DRAM | Volatile, refreshed host working memory; channels, controller, NUMA and access pattern determine useful delivery. | Capacity, memory-controller support, bandwidth and latency. A qualified server module is not an HBM package. |
| HBM | Stacked DRAM with a very wide interface close to the accelerator. | Stack capacity, interface, package integration, thermal limits and customer qualification. It is not a generic DIMM upgrade. |
| GDDR | Graphics-oriented DRAM with a different board/controller/interface design and high per-pin rates. | The accelerator/board must support it. A nominalGB comparison does not make it drop-in HBM. |
| LPDDR | Low-power DRAM family used in mobile/client systems and newer server-module designs. | Power, controller, module and platform support; SOCAMM is not proof that every server can substitute it. |
| NAND | Nonvolatile storage, often behind SSD controllers and firmware managing block access and endurance. | Persistence, transfer/queueing latency, sustained access pattern and endurance. It can be a capacity tier without being a DRAM-speed tier. |

“DRAM versus HBM” therefore usually means conventional DRAM products versus a particular stacked DRAM architecture. NAND flash is a different technology. SRAM-rich architectures may avoid some external traffic, but that is a system redesign, not free replacement of external memory capacity.

## What2026 evidence actually establishes

[Samsung’s12February release](https://news.samsungsemiconductor.com/global/samsung-ships-industry-first-commercial-hbm4-with-ultimate-performance-for-ai-computing/) reports commercial HBM4 shipments, not just a future launch. It specifies2048I/Os,11.7Gbps consistent pin speed, capability up to13Gbps, maximum3.3TB/s per stack and24–36GB with12 layers. The16-layer48GB option is future-facing. “Stable yield” is a vendor statement without a numerical yield distribution or independently verified shipment count. Peak component bandwidth is not an application result.

[SK hynix’s29July Q2 report](https://news.skhynix.com/en/q2-2026-business-results/?trk=article-ssr-frontend-pulse_little-text-block) distinguishes HBM4 mass shipments from HBM4E samples. It reports around10 long-term customer agreements, while second-half ramping, an early2027 cleanroom and later packaging/NAND investments remain plans. “Largest share of production” and a planned share of domestic capacity have different denominators. Contract text, deliveries and numerical qualified yields were not recovered.

[Micron’s fiscal-Q3 filing](https://www.sec.gov/Archives/edgar/data/723125/000072312526000015/mu-20260528.htm), for the period ended28May, explicitly states that HBM consumes more wafers and cleanroom space per bit than conventional DRAM at the same node; it supplies no universal conversion multiplier. It also names the reverse case: weaker HBM demand and a mix shift can increase conventional DRAM supply. Qualification and ramp risks, take-or-pay terms and planned factory clocks make supply more specific than a capex headline. Its first Idaho wafer output in mid2027, Singapore HBM packaging in1H2027, new NAND cleanroom in2H2028 and NewYork supply in2030+ are projections. Gujarat assembly/test commercial shipments are a separate operating milestone, not a wafer fab or job-access proof. Fiscal-Q3 DRAM revenue rose67% quarter-on-quarter while bit shipments rose only in the low single digits; revenue growth cannot be read as equivalent bit capacity.

[Micron’s30September fiscal-Q4 release](https://www.sec.gov/Archives/edgar/data/723125/000072312526000018/a2026q4ex991-pressrelease.htm), for the period ended3September, distinguishes512GB DDR5 samples, completed8800MT/s RDIMM qualifications, LPDDR shipments and SSD shipments for KV-cache applications. The last item is useful positive evidence of an actual storage-tier product path; it does not establish a customer’s inference speed, accepted output or savings. The direct quarterly landing page omitted its result tables, so mixed-quarter indexed snippets were not treated as one coherent Q4 report.

A “sold out” statement, were one supplied, would still need a product, period and contract/allocation definition. It would not prove that every form of DRAM, every buyer or every workload lacks memory. This pass makes no future price, market-share,2031 shortage or investment forecast.

## Units and the qualified-output boundary

Wafers, good dies, bits, GB, die layers, stacks and customer-qualified accelerator memory are not interchangeable. Useful output depends on process yield, binning, stacking/assembly/test yield, package capacity and qualification. A simple multiplication can illustrate the stages, but correlated defects and shared bottlenecks prevent treating independent-yield assumptions as measured fact. SC04 owns interposer, substrate, bonding and OSAT depth; this report only crosslinks those dependencies.

A dimensional check helps read the HBM claim:2048pins×11.7Gb/s÷8 gives2.9952 decimalTB/s; using13Gb/s gives3.328TB/s, consistent with the rounded maximum3.3 figure. This is theoretical interface arithmetic, not sustained bandwidth. It is also distinct from capacity inGB and from the binaryGiB used by runtime controls. There is no justified per-SKU nanosecond latency estimate in the selected evidence.

## B. What developers can change—and what native tools already do

Start by identifying the actual problem. Failure to fit is a capacity problem; stalled execution may be bandwidth, access latency, synchronization, compute, queueing or transfers. More memory can prevent an out-of-memory error while making no improvement to the critical path. Larger batches can improve hardware throughput while worsening a user’s deadline.

The current [vLLM engine-argument documentation](https://docs.vllm.ai/en/latest/configuration/engine_args/) already provides explicit KV allocation, cache dtypes, prefix caching, CPU-offload backends and admission/headroom controls. Its units matter: KV cache bytes are perGPU; weight-offloadGiB are perGPU; the KV-offload buffer is summed across tensor-parallel ranks. Weight offload explicitly depends on a fast CPU–GPU interconnect. This is a substantial native baseline, not an absent feature waiting for a wrapper. The floating `latest` page is not an immutable installed build, a guarantee that every combination composes or a benchmark.

Several distinct changes should be compared separately:

- **Reuse, locality and allocation:** reduce avoidable residency or repeated work without changing the intended answer. Gains depend on real prefix reuse and arrival distribution. Cache identity, isolation, eviction and invalidation remain correctness obligations.
- **Quantization/compression:** lower nominal weight or KV bytes, but include metadata, packing, conversion and kernel support. Weight precision and KV precision affect different objects. Required quality must be tested with the same checkpoint, tokenizer, prompt and decoding contract when isolating the policy.
- **Context eviction/truncation:** changes retained information. It may be a good product choice, but it is not evidence of equal-information compression.
- **Host/SSD tiering:** provides capacity at transfer, scheduling, NUMA and storage costs. Include warm and cold reads, misses, write/eviction traffic, failures and endurance assumptions. Native offload may suffice; a faster local interconnect may change the answer.
- **A smaller or different model:** can meet the real task more cheaply. It is a valid product comparator, while a different model is not an isolated memory-policy experiment.

For ordinary full-attention MHA/GQA, a transparent nominal KV ledger is `2 × layers × KV_heads × head_dimension × total_retained_tokens × bytes_per_element`. A self-authored case with32 layers,8 KV heads,128 dimensions,8192 tokens across16 sequences and2-byte elements gives16GiB;1-byte elements give8GiB before overhead. This formula is not a general model of MLA, sliding-window or recurrent-state architectures, and naive division by tensor-parallel size may be wrong when state is replicated. No tensor was allocated or model run here.

Resident parameter count times stored bytes is likewise only a weights lower bound. Scales/zero-points, padding, allocator reservations, activations, workspaces, communication buffers and duplicate copies matter. Mixture-of-experts active parameters do not automatically equal resident weights. For performance, bytes divided by effective bandwidth is a lower bound on transfer time, not a prediction of overlapped execution, latency or tail goodput.

## One existing route, not another parallel project

Existing H5 memory/interconnect sensitivity, local15 cache/quantization compatibility and serving145 already cover this problem. No additional project or personal time allocation is needed. The exact chosen anchor is `ai-ml-round5.project.serving`, source `ai-ml-enrichment-round5.json#/records/145`; its32–48FIRST/96–144TOTAL hours and included4–6-hour gate remain conditional planning assumptions. Other routes are alternatives, not extra allowances to stack.

The **pending first-stage attachment** is a memory/quality/arrival manifest inside that selected old task: separate weights, KV, workspaces, reserved versus resident allocations and per-rank units. Use an already approved runtime and permitted fixture only if available; otherwise finish a source-contract report and leave memory, speed and quality unmeasured.

The **pending continuation** is one supported native configuration versus one policy change under matched checkpoint/tokenizer, acceptance, lengths, arrivals, cache state and hardware. Keep held-out, pressure and failure regimes. The original independent quality oracle and all-offered-request ledger remain necessary. Independently reconcile the dimensional ledger with native counters and their measurement boundaries; a runtime counter is not total system memory or semantic correctness.

Report peak allocated/reserved/resident memory per device and host, OOM/eviction/recomputation/copy traffic, all offered requests, accepted in-deadline output, TTFT, token/tail latency and cold/warm/cache-miss behavior. Cost includes host, GPU, network/storage, setup and review only when measured on a consistent basis. A memory reduction with lost evidence, lower quality or more failed deadlines is a trade-off, not a free saving.

Stop extra custom work if the native configuration meets the same contract more simply. Stop a performance claim if the gain vanishes after restoring failures, equal context/quality or full costs. New hardware, software, models, selected-asset rights or an unavailable independent oracle are access gates; they do not justify silently buying resources or calling the learner weak. No new resource, fixture, exercise, device arm, keys or hours is authorized by this proposal.

## Reachable software layers and real entry barriers

An application/AI developer can start with memory accounting, configuration regressions, profiling interpretation, cache identity and cancellation/recovery. Runtime/allocator work adds C++ resource lifetimes, concurrency, NUMA and parallelism; backend kernels add numerical and hardware-specific depth. Silicon design, memory-controller validation, test/yield engineering and device characterization are separate routes with proprietary data, lab equipment and role-specific qualifications. No generic ML demo proves those competencies.

The held local15 report includes a dated ArmCambridge runtime role accepting C++ evidence from work, internships, academic projects or open source, and a contrasting indexed AppleMunich role asking for a bachelor’s degree plus10 years. These are prior sampled observations, not fresh vacancies or universal degree rules. No current Micron/Samsung/SK software vacancy, personal sponsorship, country eligibility or paid receiving path was verified here. An assembly facility in India does not establish remote access to its process data or a suitable engineering opening.

Public routes are the cited supplier publication channels and vLLM’s repository/community linked from its documentation, plus the held MLX/ggml contribution routes. Samsung’s February release identifies SangJoonHwang as Memory Development head at that date; no current profile or mentor availability is inferred. Existing local15 identifies MLX software authors and public contribution rules. A supported minimal regression, numerical/kernel test or memory-accounting correction may become a contribution only after actual reproduction and maintainer review. No contact, issue, application or submission occurred.

The credible2031 preparation claim is conditional: systems skills can remain useful across tight and abundant supply because applications still trade capacity, movement, quality and latency. Native automation may absorb most custom work, and there may be few personally accessible roles. This source pass establishes neither the market size nor the return from a course, project or career pivot.
