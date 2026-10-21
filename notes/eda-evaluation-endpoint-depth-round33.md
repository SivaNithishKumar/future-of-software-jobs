# AHRR: which endpoint improved, on which design cohort?

This pass extends the saved EDA work through one previously uncovered case, rather than repeating AuDoPEDA, PostEDA's scorer or the educational-PDK/manufacturing distinction. The case is Zijian Ding, Yang Zou, Yizhou Sun and Jason Cong, **“Can Agents Design Better Chips with a Higher Level Abstraction?”**, [arXiv 2609.21157v1, 17 September 2026](https://arxiv.org/html/2609.21157v1). Its header identifies an ICCAD 2026 invited paper and DOI `10.1145/3831252.3847810`; the November conference had not occurred at this audit. Only this version was read, not a later proceedings version or conference programme.

The positive finding is substantive: HLS and domain-specific compilers supply architecture knowledge that agents can use, and agents sometimes improve the resulting implementation. The endpoint is **simulated task cycles combined with a vendor-tool post-route clock estimate on a fixed FPGA target**, under correctness and resource checks. It is not measured board runtime, power, ASIC signoff or a fabricated-design result. The headline also uses a conditional task/model-pair denominator. [Paper §3–4](https://arxiv.org/html/2609.21157v1)

## What the experiment actually does

The study compares direct agent-written RTL, agent-written HLS C++, refinement of HLS-generated RTL, and refinement of domain-compiler-generated HLS. AHRR combines the second and third flows. Both specification-driven arms receive the same specification, correct unoptimised C++ reference, one public stimulus and interface contract. Tasks cover 11 named workloads, with an additional GEM1 interface variant; some use fixed-point or reduced dimensions to control simulation cost.

The target is AMD Alveo U55C, `xcu55c-fsvh2892-2L-e`, with Vitis 2025.2, **out of context and without a shell**. Reported validity requires the hidden testbench to pass, successful routing, and resource usage within 60% of each listed resource class. Correctness uses C and RTL simulation. The authors expand tests to 100% C++-reference branch coverage and also measure reference-RTL coverage. These are real disclosed controls, not just parser success; they are finite coverage, not formal equivalence or proof that every task specification/reference is correct.

Each stated experiment runs once. The agent can use up to five one-hour rounds, retaining its session and receiving previous evaluation results. RTL simulation, synthesis/PnR and total experiment time have stated limits. The next refinement stage starts from the best preceding HLS design. This is adaptive design search with a held-back testbench, not an untouched final transfer experiment. Hosted model pretraining overlap is not resolved by this setup. [Paper Tables 1–2 and §3–4.1](https://arxiv.org/html/2609.21157v1)

## The clock target is a scoring floor, not the old FIFO hard gate

The paper defines estimated execution time as:

`simulated cycles × max(target period − WNS, target period)`

The target is 3.33 ns. Thus a negative WNS can produce a slower effective period and remain a scored design under the stated validity predicate. Positive slack cannot produce a reported period faster than the target. This is a legitimate metric choice: it penalises missing the target while declining to credit additional frequency beyond the target. It is not an observed scoring defect.

The distinction prevents two incorrect readings. A post-route period improvement below the target can improve headroom or resources without improving this task-time score. Conversely, a lower cycle count can outweigh a slower effective clock under this metric. Neither inference should silently override a workload that requires a hard clock, fixed latency or throughput.

The existing `eda-hardware-round11.project.constrained-flow` has an illustrative **1-ns fixed target**, with setup/hold constraints required to pass. AHRR's soft scoring rule cannot be imported as permission to miss that constraint. The proposed extension below adds endpoint/clock-role reporting only. It introduces neither a new FPGA arm nor a substitute ASIC comparator.

## Cohort, success and cost are different denominators

Table 3 reports HLS's 2.31× geometric mean over 15 valid direct-RTL comparison pairs, while AHRR's 2.62× uses 13 pairs after two GEM1 cases were not evaluated in that refinement. These are task/model pairs, not 11 independent chips. A separate 1.17× post-HLS refinement mean uses 16 valid cases. Dividing the first two aggregate means as though they measured one same-cohort stage effect is unjustified; the different denominators are not themselves a contradiction.

The tiny arithmetic companion recomputes the rounded printed ratios: approximately 2.3128 for the 15 HLS ratios and 2.6151 for the 13 AHRR ratios, rounding to the reported values. A same-13-pair HLS mean differs from its 15-pair mean. These are arithmetic checks on a printed table, not recovered raw results or an independent native reproduction. Failed, excluded and unevaluated cells must remain in the report even when they cannot enter a finite speed ratio.

Likewise, equal limits for a stage do not automatically make combined-flow total cost equal. HLS construction supplies the seed for subsequent RTL refinement. Full cost must include both stages, failed/time-limited flows, model calls, setup and review. One run per case does not estimate stochastic repeatability or a seed-distribution confidence interval. Hardware host details, complete model costs, exact selection logic and resource-normalised total flow comparisons remain artifact-reconciliation gates. [Paper Table 3, §4.1–4.4](https://arxiv.org/html/2609.21157v1)

## Native tools are part of the positive result

The study does not merely compare against random RTL. AutoSA and StreamHLS provide strong compiler-generated starting designs for selected tasks. Agents improve some of them, while SHL1 shows no improvement and simulation approaches the timeout. That last result cannot distinguish “no useful optimisation exists” from “the evaluation loop leaves too little opportunity to find it.” Direct RTL also wins some small-kernel cases; the authors say prompt changes may affect either arm.

The case studies show architectural parallelism and local mapping/timing changes. More parallel hardware can use substantially more resources; speed is not a free improvement in every PPA dimension. FPGA LUT/DSP/BRAM counts are not standard-cell or die area, and no measured energy-per-workload result follows from them. The output should be read as a scoped compiler/agent design-flow result with declared constraints, not proof that an agent beats all skilled hardware designers or all classical design-space searches. [Paper §4.3–5.3](https://arxiv.org/html/2609.21157v1)

The manuscript mentions an industrial Jalapeño announcement but says no flow details are released and displays an unresolved citation marker. This pass did not verify that announcement. It is not a measured fabrication endpoint in the AHRR experiment; neither is it evidence against the industrial design. Funding and donated cluster/equipment access likewise do not establish an accessible opening or that this run occurred on a programmed card.

## Release evidence, rights and reproduction

The [official repository](https://github.com/ZijD/AHRR) describes per-round reports/ledgers, seed/submission digests, hidden-test definitions and mutation gates, distilled agent trajectories, and table/figure provenance. It advertises a metadata/table checking path that does not need FPGA tools. Those are useful reproducibility provisions. This pass did not execute those scripts, inspect each artifact, or verify their claim that every paper number regenerates.

The README also discloses that routed binary checkpoints, simulation workdirs and raw agent transcripts are not shipped. Flow execution requires Vitis 2025.2 and model credentials; the example commands would install software, so none was run. The paper is CC BY 4.0. The repository displays an MIT label and a LICENSE path, but the one allowed licence-file read returned a cache miss. Full source/task grant, immutable commit, third-party IP/compiler terms, vendor/device libraries, model/API terms and compatible environment remain unresolved. No commercial-use permission was inferred from the badge.

This is a fixed FPGA-device experiment, not an ASIC process/library cross-validation. It cannot establish cross-PDK generalisation from one vendor part. Device, tool and library entitlement are distinct from open paper/code metadata; no PDK, toolchain, bitstream, checkpoint, task package or model was downloaded.

The paper's four authors are affiliated with UCLA. The publication and [official repository issue route](https://github.com/ZijD/AHRR/issues) are public professional discovery channels; issue contents, submission rules, faculty availability and hiring/admission/work-rights routes were not audited. C++/HLS scheduling, HDL arithmetic/clock/interface semantics, simulation and timing/resource reports are real preparation needs. A repository-level report contribution does not establish specialist silicon competence, waive a degree/experience/onsite filter or create paid access.

## Narrow addition to the existing EDA artifact

The JSON proposes an **unapplied report-contract extension** to the existing `eda-hardware-round11.project.constrained-flow`, whose raw kind remains `contributionpath`. It preserves 40 hours in the first window, **120 TOTAL** by the later checkpoint, and the included eight-hour launch gate. These remain unmeasured planning caps, not personal availability. No additional hours, tool install, HLS/FPGA flow, board or fabrication work is allocated.

The proposed report records:

- Endpoint profile and actual stage: simulation, synthesis, post-route, board, signoff and fabrication stay separate.
- Whether a clock value is a hard requirement or a scoring floor; cycle source, time units and measured-versus-estimated status.
- Exact task/model/flow/variant/round/seed, paired-cohort membership, and planned/attempted/valid/excluded/unsupported counts with reasons.
- Stage and whole-flow costs, including failed attempts, alongside the unchanged accepted-transaction, latency, throughput, resource and clock contract.

The original sealed queue/transaction oracle and fixed constraints remain authoritative. Proposed metadata controls reject accepted results from a failed stage, mismatched comparison cohorts, a changed hard target or missing attempt accounting. Independently prepared fresh cases/reviewer and a native run do not exist here. The four own fictional fixtures demonstrate the described clock arithmetic and the difference between soft and hard targets only; they are not tests of AHRR's implementation.

Continue this addition only if it exposes a real reporting ambiguity after inspecting the chosen native flow. If native reporting already supplies the needed distinction, use it or document a genuinely reduced discrepancy. Rights/runtime/resource failure retains a source/report-schema result inside the existing cap. A competent default/compiler or negative result can justify maintenance work without rescuing an unnecessary custom agent layer. Accepted contribution, sustained ownership, signoff authority and employment remain separate later evidence.

## Scope receipt

Three primary endpoints were attempted: the pinned arXiv HTML, official repository root/README, and failed LICENSE blob. No fourth endpoint or assets were fetched. Only own small arithmetic ran. Web line metadata is not a raw primary-file hash or an immutable code pin. Earlier reports, both original/root38 EDA records, the taxonomy and held source index remain unmodified; no native EDA execution, private account, contact, UI or child agent was used.
