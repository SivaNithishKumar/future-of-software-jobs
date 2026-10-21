# SC05 — networks, storage and useful AI throughput

The physical chain has real vendor-reported shipping components. Faster links or SSDs nevertheless do not guarantee more useful AI work. A credible software path starts with the actual workload, topology, data path and correctness; bandwidth growth does not establish scarce jobs.

## A. The chain and its units

[GB300 NVL72](https://www.nvidia.com/en-us/data-center/gb300-nvl72/) combines 72 GPUs and 36 Grace CPUs. Its 130 TB/s NVLink figure is rack aggregate; 800 Gb/s networking is per GPU through ConnectX 8, using InfiniBand or Ethernet. The page marks the product available, but its 50x output headline is projected with different precision/runtime configurations.

An Ethernet switch ASIC is another unit. [Broadcom’s 12 March 2026 release](https://investors.broadcom.com/news-releases/news-release-details/broadcom-now-shipping-worlds-first-1024-tbps-switch-production) reports 102.4 Tbps Tomahawk 6 production-volume shipments and native congestion/load-balancing features. Aggregate chip capacity is not per-job throughput or an observed million-XPU deployment.

Copper/SerDes or fibre/transceiver modules complete the path. [Marvell](https://www.marvell.com/company/newsroom/marvell-1-6t-optical-dsp-ai-data-center-connectivity.html) separates mass-volume Ara from newer sampling variants. Lane counts, retiming, reach and compatibility remain attached to specific parts. Optical communication is not optical neural computation.

CPUs still run OS, control and whichever preprocessing/serialization the pipeline leaves there. PCIe is local device IO. Held CXL standard publication does not prove deployed host/device/OS support in this rack or automatic substitution for NVLink. HBM, fabs, packaging and facility power remain sibling topics.

NAND SSDs hold persistent datasets, weights/checkpoints and caches. The [Micron 9650 brief](https://www.micron.com/content/dam/micron/global/public/products/storage/ssds/data-center/9650/9650-nvme-ssd-product-brief.pdf) directly read is Rev B 02/2026, not an older indexed revision. Its advertised 28 GB/s is sequential. Peak random read IOPS uses QD 512; typical latency uses 4 KB/QD1 and is a median. Those cannot be advertised as simultaneous peak-and-tail performance. Efficiency tables, other power rows, NAND IO and whole SSD rates also use different boundaries.

## B. Diagnose the workload, then test the native alternative

| Workload | Necessary comparison |
|---|---|
| Training | Accepted step time at same precision/model, collective/rank imbalance, compute overlap and contention. |
| Prefill | Offered-load TTFT, prompt length, batching and stage transfer; simpler placement may win. |
| Decode | Per-token tails, KV/weight traffic and parallelism, with equal output quality. |
| Checkpoint/restart | Complete restorable state, serialization/IO/commit, foreground stall and failures; cached writes are not durability. |
| Retrieval | Cache/CPU index/random IO, retrieval quality and end-to-end tails, not drive IOPS alone. |

[NCCL’s method](https://github.com/NVIDIA/nccl-tests/blob/master/doc/PERFORMANCE.md) distinguishes algorithm from collective/rank-normalized bus bandwidth. That is not a literal wire trace or job score. Its selected master page is floating; a native comparison needs an immutable build and compatible runtime.

[GPUDirect Storage](https://docs.nvidia.com/gpudirect-storage/overview-guide/index.html) can avoid CPU bounce buffers, while unsupported/configured cases may fall back through CPU memory. Filesystem, alignment, version, PCIe topology and concurrency matter. It does not create application concurrency; its coarse-streaming design is not a universal fine-random-retrieval speedup. Native capabilities can remove a proposed custom layer.

Held DistServe evidence is a real older serving/SLO comparison with losing regimes, not a current 2026 training-cluster benchmark. No matched cluster trace, full energy/cost or paid receiver was obtained here.

## One pending option, not a new allocation

The unactivated measurement-contract proposal has NEW unmeasured estimates of 20–35 FIRST focused hours and 35–65 conditional ADDITIONAL, with a 3-hour setup stop inside FIRST. It borrows no old cap; day 30/day 90 are checkpoints, not availability or completion promises.

Choose one collective OR storage contract. Preserve units, grain, direction, ranks or QD/cache/block size in a small source/fictional fixture. Compare mature documented methods with independently fixed reference expectations; unknown context stays unknown. Public answers are exposed regression/learning material, not unseen skill proof.

A later native phase needs a permitted setup/log, exact versions/rights and independent truth. Choose NCCL-tests OR fio/GDS, not an entire cluster. Without access, retain source-only proof. Reject extra custom work if native/manual methods already meet the same receiver need or the gain disappears at equal quality, durability and failure accounting.

Deeper work needs task-specific C/C++, Linux/concurrency, CUDA, PCIe/RDMA and measurement statistics. Optical/device tasks add equipment/specialist knowledge. Public docs and vendor product groups are references, not hiring or submission permission. Held UK role examples are adjacent; current NIC/SSD degree, location and India eligibility remain unverified.

Four queries/six new primary bodies are closed. No hardware/network action, assets, installation, account/API, contact, purchase, native benchmark or shared index/UI mutation occurred. Contribution, retained skill, production ownership and pay require separate evidence.
