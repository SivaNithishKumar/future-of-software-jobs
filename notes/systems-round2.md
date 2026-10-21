# Mature computing specialties: systems depth, modern transitions and routes to contribution

Cutoff: 19 October 2026. Owner scope: compilers/performance, databases/storage, distributed/network systems, embedded/firmware, formal verification, accessibility, and legacy enterprise migration. This complements the earlier sector scan; it does not repeat finance, creative or space market research. No installations, outreach, private-system access, purchases or external writes occurred. Projects below are proposals, not completed implementations. No final mind map is included.

## What the evidence changes

An AI-heavy career landscape misses a large set of software problems whose requirements are imposed by hardware, concurrency, protocol semantics, compatibility, physical devices and human access. AI does not make those constraints disappear. Equally, these specialties are not protected refuges where automation has no effect: their tools and day-to-day work are changing, and AI infrastructure itself creates compiler, networking, storage and reliability work.

For an existing application/AI engineer, database performance, distributed reliability and migration verification are plausible adjacent extensions. Accessibility is a strong extension for someone who already owns frontend/product quality. Compilers, firmware and formal-methods research can be rewarding deeper pivots, but sampled employers often require substantial prior systems experience or research credentials. These are judgments about skill transfer, not estimates of hiring growth or automation resistance.

The likely useful combination is one difficult systems specialty plus enough product/domain ownership to choose valuable problems and prove results. A five-year strategy should not depend on either “all future work is prompting agents” or “low-level work is immune to AI.”

## 1. Compilers and performance engineering

### Shipping changes and economic drivers

[Python 3.15.0 shipped on 9 October 2026](https://www.python.org/downloads/release/python-3150/). Its release notes describe an improved experimental JIT, a profiling package/statistical profiler, stable-ABI work for free-threaded builds, and default installation of free-threading support in official macOS binaries. Installing support by default does **not** mean every Python program now runs free-threaded. The reported JIT speedups are benchmark geometric means, not a promise for a particular service.

[LLVM 23.1 release notes](https://releases.llvm.org/23.1.0/docs/ReleaseNotes.html) document continued backend, optimisation, profiling and BOLT work. The [release announcement](https://discourse.llvm.org/t/llvm-23-1-0-released/91654) is dated 26 August 2026; the LLVM download index contained a conflicting date, so the release announcement is the chronology source used here.

A concrete non-model example is Cloudflare’s [18 September 2026 account of reclaiming over 100 TB of RAM](https://blog.cloudflare.com/saving-100-tb-of-ram-with-math/). It describes changing consistent-hashing representation and sizing, with a staged migration to protect cache behaviour. This is a company engineering report, not an independent financial audit. It nevertheless demonstrates the kind of resource problem for which deeper algorithm and layout work can be valuable.

### Meaningful subbranches

- Runtime performance: allocation and object layout → cache locality and memory bandwidth → garbage collection, threading and FFI/ABI compatibility → latency under real concurrency.
- Compiler engineering: IR and dataflow analysis → legal transformations and optimisation profitability → register allocation/scheduling/code generation → target-specific validation.
- Measurement: representative workload → profiling and hypothesis → controlled baseline → uncertainty and correctness checks → cost/latency consequence.
- Hardware/software co-design: CPU/GPU/accelerator limits → compiler/runtime changes → observability and debugging → usable application interfaces.

### What AI may automate, and the depth that remains

Candidate transformations, benchmark scaffolding, assembly explanations and regression-test drafts are plausible AI-assisted tasks. They must be measured rather than assumed to save time. Choosing the right workload, recognising undefined behaviour, explaining a cache/branch/NUMA effect, respecting floating-point semantics and demonstrating an improvement outside a microbenchmark require an independently checkable model of the machine and program. These are task-analysis hypotheses, not quantified automation estimates.

### Career and contribution route

Employers sampled below connect compilers directly to graphics, AI and HPC; this field complements frontier AI rather than competing with it. Useful first contributions are reduced compiler bugs, regression tests, performance counterexamples, profiling improvements and small justified optimisation patches. A new compiler or GPU purchase is not needed to begin reading, reducing examples and measuring a CPU workload on existing approved tools.

## 2. Databases and storage

### Current transition

[PostgreSQL 18, released 25 September 2025](https://www.postgresql.org/about/news/postgresql-18-released-3142/), introduced asynchronous I/O for operations including sequential/bitmap scans and vacuum, selectable through worker/io_uring/synchronous methods. Its “up to 3×” storage-read result is explicitly workload-dependent. More knobs create a need for workload understanding rather than a universal tuning recipe.

[PostgreSQL 19 was RC1 on 15 October 2026](https://www.postgresql.org/about/news/postgresql-19-rc-1-released-3409/). It should not be described as generally available at this cutoff. Release maturity and application migration readiness are separate facts.

### Meaningful subbranches

- Query execution: data distribution/cardinality → plan choice → indexes and physical layout → execution operators/vectorisation → memory spills and tail latency.
- Transaction correctness: isolation level → anomalies and invariants → locks/MVCC → retries/idempotency → recovery and externally visible outcomes.
- Storage: page/LSM/column layouts → caching/compression → write amplification and compaction → durability/WAL → repair, backup and restore.
- Operational transitions: schema/data compatibility → upgrade/backfill strategy → replication lag → rollback → proof that applications still observe the intended data.

### AI and depth

AI can propose SQL, indexes, schema mappings and incident hypotheses. A syntactically valid query is not evidence of correct results, and a faster benchmark query may merely shift cost into writes, storage or another tenant. Expertise includes data semantics, query-plan reading, realistic skew, recovery and the economic trade-off between a simpler single-node design and distribution.

### Companies, labs and contribution

MongoDB’s UK query-engine role explicitly seeks C++ and systems experience. [CWI’s Database Architectures group](https://www.cwi.nl/en/research/database-architectures/) works on column stores, compression, vectorised execution and in-process analytics, and identifies related companies including DuckDB Labs. [CMU’s BusTub](https://github.com/CMU-DB/bustub) is an MIT-licensed educational DBMS, explicitly unsuitable for production. Use it for internals learning, not as a production dependency or as permission to publish course-assignment solutions.

A strong initial contribution is a reproducible query-plan or recovery defect with generated data, an explanation of the relevant invariant, and a narrowly scoped test. Learning SQL usage alone is not the same specialism as building query engines; both can be valuable, with different entry barriers.

## 3. Distributed systems and network software

### Current transitions

[Kubernetes in-place container resource resize became GA in 1.35 on 19 December 2025](https://kubernetes.io/blog/2025/12/19/kubernetes-v1-35-in-place-pod-resize-ga/); [pod-level resource resize became beta in 1.36 on 30 April 2026](https://kubernetes.io/blog/2026/04/30/kubernetes-v1-36-inplace-pod-level-resources-beta/). The posts identify limits, runtime interactions and residual coordination issues. A feature being GA does not make resource management or application resizing automatic.

Cloudflare’s [12 May 2026 QUIC congestion-control incident analysis](https://blog.cloudflare.com/quic-death-spiral-fix/) shows how a subtle interpretation of application idleness could pin a congestion window and severely reduce throughput. This illustrates why protocol implementation, scheduling and measurement remain important alongside memory safety and higher-level code generation.

### Meaningful subbranches

- Correctness under failure: state and invariants → retries/duplicates → failover/partitions → consistency versus availability → recovery and reconciliation.
- Performance under contention: queueing and backpressure → admission control → fairness and tail latency → capacity limits → graceful degradation.
- Protocol engineering: wire format/state machine → timers and loss/reordering → interoperability → congestion control → observability.
- Platform operation: scheduling/resource budgets → rollout and version skew → failure domains → incident response → durable prevention rather than one-off repair.

### AI and depth

AI may generate manifests, reproduce familiar incidents or summarise telemetry. The core challenge is deciding which evidence discriminates between competing explanations and validating behaviour under failures that normal integration tests miss. Better code production can increase the amount of infrastructure needing this work, but this source set does not establish a net increase in headcount.

### Contribution route

Canonical’s sampled role is explicitly about validating resilient distributed systems rather than merely writing deployment YAML. Useful contributions include fault-injection harnesses, minimized protocol regressions, cross-version compatibility tests and actionable operational documentation. Test only owned/local environments; there is no reason to probe public services for a career portfolio.

## 4. Embedded and firmware

### Current transition

[Zephyr 4.4 release notes](https://docs.zephyrproject.org/latest/releases/release-notes-4.4.html), with the [release index recording 14 April 2026](https://docs.zephyrproject.org/latest/releases/index.html), describe SDK/toolchain changes, C17, additional architecture support, pressure-based frequency scaling, footprint reports and cycle-accurate benchmark infrastructure. Some components are explicitly experimental. Its emulator support makes an initial software-only experiment possible; this does not validate hardware timing or power consumption.

[Cambridge/SRI’s CHERI programme](https://www.cl.cam.ac.uk/research/security/ctsrd/cheri/) is a useful cross-boundary example: ISA changes, compilers, OS adaptations, formal models and porting all interact. Its QEMU models are described as ISA-level rather than microarchitecturally realistic. Do not infer measured silicon performance from an emulator.

### Meaningful subbranches

- Hardware boundary: memory maps/registers → interrupt/DMA behaviour → drivers and buses → board bring-up → electrical/physical validation.
- Real-time behaviour: scheduler and priorities → deadlines/jitter → bounded memory → worst-case failure paths → watchdog/recovery.
- Product lifecycle: boot/update process → version and compatibility policy → field diagnostics → manufacturing/test → long-lived support.
- Efficiency: code/data footprint → allocation and buffers → sleep/wake and frequency policy → measured energy → physical deployment constraints.

### AI, access and depth

Generated drivers, HAL glue, test cases and register explanations may help. Datasheets, timing, hardware errata, power behaviour and fault recovery still need reliable validation. India has a directly observed Arm firmware vacancy; Cambridge has a directly observed firmware release/defect leadership role. These examples do not mean hardware roles are universally remote or open without lab access.

An appropriate first contribution can improve a simulator-based regression, driver test or footprint report. Board purchases and specialised probes belong only after a specific need and approval; no hardware was acquired here.

## 5. Formal verification and specification

### Current transition, with a crucial boundary

[AWS announced generally available Automated Reasoning checks on 6 August 2025](https://aws.amazon.com/about-aws/whats-new/2025/08/automated-reasoning-checks-amazon-bedrock-guardrails/). This is a concrete product combining formal methods and generative AI. Do not convert its “up to 99%” vendor wording into a universal correctness guarantee.

[AWS’s testing documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/test-automated-reasoning-policy.html) separates natural-language-to-logic translation from checking against policy rules. Incorrect translations, missing variables and incorrectly encoded rules remain possible. A proof is conditional on what was specified and on the implementation/model relationship.

### Meaningful subbranches

- Specification: stakeholder intention → precise state/transition model → safety and liveness properties → assumptions and exclusions → review against real requirements.
- Model checking: finite abstraction → reachable states → counterexamples → model repair → understanding state-space and bound limits.
- Program verification: contracts/invariants → proof obligations → solver/proof assistant → trusted assumptions/axioms → relation to executing code.
- AI assurance: generated code/claims → formal or executable oracle → proof/checking results → translation and scope tests → residual uncertainty.

### Career and contribution

The sampled AWS engineering role asks for production software/architecture experience and lists formal-methods interest as preferred; its research scientist route asks for a PhD or equivalent research experience. These are distinct entry paths. London programming-language work also includes verification without a mandatory OCaml background. Strong original contributions can be a previously unmodelled failure, a reusable verified component, a smaller counterexample or better specification/tool feedback—not only a new theorem prover.

## 6. Accessibility engineering

### Technical and commercial evidence

[W3C published WCAG-EM 2.0 as a Group Note on 23 July 2026](https://www.w3.org/TR/2026/NOTE-wcag-em-2-20260723/). It is an evaluation methodology, not a new legal declaration that every product conforms. [W3C’s introductory guidance](https://www.w3.org/WAI/fundamentals/accessibility-intro/) says knowledgeable human evaluation remains necessary; a tool alone cannot determine full accessibility.

The British Council’s [6 February 2026 accessibility-audit tender](https://www.find-tender.service.gov.uk/Notice/010916-2026/PDF) lists an estimated **£207,720 including VAT**, an initial two-year remote rate-card engagement and possible extensions. This is a concrete procurement estimate, not verified money spent or a verified award. The primary PDF was available in the search index; direct opening returned 403. The supplier scope includes testing, audits, reporting and assurance, not only running a scanner.

### Meaningful subbranches

- Platform semantics: native elements → accessible names/roles/states → focus and keyboard interaction → dynamic updates → assistive-technology behaviour.
- Evaluation: representative journeys/states → automated checks → manual review and assistive-tech tests → disabled-user involvement → scoped claims and remediation evidence.
- Product lifecycle: component/design-system contracts → regressions in CI → documentation and content → audit readiness → recurring quality ownership.
- Inclusion beyond pass/fail: task usability → cognitive/information load → multiple input/output methods → real-context constraints → feedback and iteration.

### AI and depth

AI can suggest alt text, inspect markup and draft fixes; whether text is equivalent, focus behaviour is usable or the task can actually be completed is not established by plausible output. There is active research on agentic audits, so assuming this field will remain manual is equally unsupported. Deque’s India role and public tools demonstrate both services and automation. The strongest position is technical remediation plus evidence of user outcomes, not selling automatic certification.

## 7. Legacy enterprise migration and compatibility

### Current transitions and budget constraints

[SAP’s 7 October 2026 clarification](https://news.sap.com/2026/10/beyond-2030-sap-business-suite-7-sap-netweaver-customers-third-party-databases-java/) reiterates Business Suite 7 mainstream maintenance through 2027 and optional extended maintenance through 2030, with third-party database/Java support arrangements also relevant after 2030. Product-specific terms matter; this is not proof that every customer will migrate on schedule.

[Microsoft’s support policy, updated 13 October 2026](https://dotnet.microsoft.com/en-us/platform/support/policy/dotnet-core), lists .NET 8/9 support ending 10 November 2026 and .NET 10 LTS ending 14 November 2028. The economic driver is compatibility/support lifecycle as well as new features.

The UK’s [21 January 2025 State of Digital Government review](https://www.gov.uk/government/publications/state-of-digital-government-review/state-of-digital-government-review) reports over £26 billion annual digital expenditure and cases where 70–85% of technology budgets went on upkeep. These are overall/reported organisational figures, not an available migration market. The review also says legacy-remediation budgets are often reallocated: high need is not the same as funded demand.

### Meaningful subbranches

- Discovery: executable behaviours and hidden dependencies → business semantics → data lineage/contracts → integration map → decommission criteria.
- Transformation: typed AST/model-based refactoring → API/runtime compatibility → incremental replacement → interfaces/adapters → parallel running and cutover.
- Verification: characterisation tests → differential execution → data/reconciliation invariants → performance and failure behaviour → rollback and recoverability.
- Organisational delivery: application owner and budget → sequencing/dependencies → training and operating model → benefits measurement → sustained capability after consultants leave.

### AI and depth

Code translation, discovery summaries, test drafts and repetitive rewrites are plausible automation targets. A compiling rewrite does not establish preserved rounding, timezones, identity, transaction boundaries, authorization, reports or integration semantics. Conversely, it is unreasonable to assume migration needs the same amount of manual translation forever. AWS’s sampled Indian architect role explicitly combines GenAI tooling with discovery, validation, risk mitigation and modernisation delivery.

An original contribution can be an open refactoring recipe with regression coverage, a difficult compatibility fixture or an evaluation showing where automated migration fails. A domain-specific professional pathway is often more valuable than acquiring random ERP credentials without access to real projects.

## Employer requirement sample: evidence of roles, not a vacancy census

Observed on 19 October 2026 from public employer pages or their indexed text. This is a purposive sample, skewed toward specialist/senior employers; it cannot support national hiring-volume, salary or trend estimates. An accessible job page does not prove the requisition remains funded or that an applicant has work authorisation. Several dynamic pages expose better text through the search index than direct opening.

| Team and public job page | Requirements actually described | Location/access implication |
| --- | --- | --- |
| [NVIDIA Senior Compiler Optimisation Engineer, LLVM — JR2014377](https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite/job/India-Bengaluru/Compiler-Optimization-Engineer---LLVM_JR2014377) | 8+ years in compiler design; C/C++, LLVM/GCC, program analysis, processor architecture, register allocation/scheduling. | Bengaluru/Pune listed. Shows an Indian compiler pathway, not an entry-level opening or proof that a short course meets the bar. |
| [MongoDB Senior Software Engineer, Query Execution](https://www.mongodb.com/careers/jobs/8281679) | 5+ years systems programming; C++; execution algorithms, query performance/robustness, testing and diagnostics. | London/remote within UK. Direct page was largely script-rendered; requirements were visible in indexed primary text. UK remote does not mean worldwide remote. |
| [Canonical Distributed Systems Software Engineer, Python/Go](https://canonical.com/careers/6768925) | Python/Go, Linux architecture, networking, CI, testing resilience/performance and deploying/debugging distributed systems; 2–4 weeks annual travel. | Body says globally remote while a location header is regional. Country eligibility should be confirmed through the employer before relying on it. |
| [Arm Staff Software Engineer, Release & Defect Lead — 2026-17354](https://careers.arm.com/job/cambridge/staff-software-engineer-release-and-defect-lead/33099/97895593504) | Production firmware, SoC integration, post-silicon validation, release/defect leadership, board/lab capacity planning; TF-A/UEFI/OpenBMC among useful experience. | Cambridge; dated 23 September 2026. The page discusses possible sponsorship; it is not a guarantee of sponsorship or hiring. |
| [Arm Embedded/Senior Embedded Software Engineer — 2025-16450](https://careers.arm.com/job/bengaluru/software-engineer-senior-software-engineer/33099/89611383968) | Low-level firmware development/test/debug across models, boards and shipping products. | Bengaluru. Different employer views displayed different Sep/Oct 2026 posting dates, so no precise date-age inference is made. |
| [Deque Accessibility Consultant](https://www.deque.com/careers/accessibility-consultant-2/) and [current careers directory](https://www.deque.com/company/careers/) | Minimum five years professional testing; WCAG 2.1/2.2; screen-reader testing, HTML/CSS/ARIA, DOM understanding and remediation advice. | Directory lists Hyderabad, India. An accessibility scan alone is far short of the described requirements. |
| [AWS Sr. SDE, Automated Reasoning Group — 10475668](https://www.amazon.jobs/en/jobs/10475668/sr-software-development-engineer-automated-reasoning-group) | 5+ years software, architecture/reliability/scaling and mentoring; formal-methods experience or interest preferred. | New York. Useful evidence of an engineering route without a stated PhD requirement; not a directly accessible India/UK role. |
| [AWS Applied Scientist, Automated Reasoning — 10522626](https://www.amazon.jobs/en/jobs/10522626/applied-scientist-automated-reasoning) | PhD or equivalent research; logic/formal verification/SAT/SMT/proof/model checking/program analysis; original research. | Santa Clara. Research route has a different evidence bar and geography from application engineering. |
| [Jane Street Programming Language Engineer](https://www.janestreet.com/join-jane-street/position/7700474002/) | Deep PL/compiler/runtime/type-system/DSL experience; strong programming and collaboration; no prior OCaml or functional-programming experience required. | London. The role includes tooling/verification and GPU/accelerator support; no claim about applicant admission likelihood. |
| [AWS Sr. Migration Modernisation Architect — 10464493](https://amazon.jobs/en/jobs/10464493/sr-migration-modernization-architect-professional-services) | 10+ years customer-facing complex-project experience, cloud/application/data integrations, CI/CD, risk/discovery, validation and post-migration optimisation; mentions GenAI tooling. | Indian locations listed, with body referencing Delhi/NCR. Exact location should be clarified with the official application channel. |

## Labs, teams and official professional channels

No outreach was sent. These are relevant public channels for future, authorised engagement. Public maintainer channels are preferable to hunting personal contact details. Read community rules and bring a concrete reproducer, technical question or research fit; a channel is not an offer of mentorship or employment.

| Organisation/team | Why relevant and first useful artefact | Official channel |
| --- | --- | --- |
| LLVM/MLIR community; relevant employer teams include sampled NVIDIA and Jane Street groups | Compiler/tooling depth. Begin with a reduced bug, benchmark or regression test explaining semantics and baseline. | [LLVM getting involved](https://llvm.org/docs/GettingInvolved.html) lists discussion, meetings and contribution routes. |
| PostgreSQL community | Database correctness/performance, release testing and upgrades. Bring generated data, exact version, plan, timings and expected result. | [Official mailing-list directory](https://www.postgresql.org/list/), including development and performance lists. |
| CWI Database Architectures; CMU Database Group | CWI bridges research and data-system products; CMU provides an internals-learning system. Reproduce one operator/storage result and explain why it transfers. | [CWI group](https://www.cwi.nl/en/research/database-architectures/) for institutional collaboration/careers; [BusTub repository](https://github.com/CMU-DB/bustub) for project guidance. |
| Cloudflare network/performance teams; Canonical distributed-systems team | Measured reliability/efficiency and open protocols. A local protocol regression or failure-injection result is useful. | [quiche repository](https://github.com/cloudflare/quiche) contribution/issue channels; Canonical’s official job page for employment. |
| Zephyr Project; Arm firmware groups | RTOS, driver, footprint and validation depth. Start with a simulator regression or reproducible driver/benchmark issue. | [Zephyr repository](https://github.com/zephyrproject-rtos/zephyr) contributing guidance and public issue channels; Arm official job pages. |
| Cambridge CHERI Research Centre / SRI collaboration | Hardware-software-semantics co-design: compilers, OS, models and verification. Begin with a bounded port/compatibility or model question. | [CHERI programme](https://www.cl.cam.ac.uk/research/security/ctsrd/cheri/) and [official CHERI mailing-list guidance](https://www.cl.cam.ac.uk/research/security/ctsrd/cheri/cheri-lists.html). |
| AWS Automated Reasoning; TLA+ Foundation; Dafny community | Production formal methods and AI verification. Bring a failing model/counterexample, proof-obligation improvement or soundness-boundary explanation. | [TLA+ tools](https://github.com/tlaplus/tlaplus) and [Dafny](https://github.com/dafny-lang/dafny) contribution/community links; AWS official roles for hiring. |
| Deque; University of Washington CREATE | Accessibility tooling plus disability-centred research. Bring reproducible interaction evidence and a scoped remediation/evaluation result. | [axe-core](https://github.com/dequelabs/axe-core) issues/contribution guidance; [CREATE](https://create.uw.edu/) lists institutional contact, mailing lists and community channels. |
| OpenRewrite community; sampled AWS modernisation team | Repeatable AST-based transformation, compatibility and migration delivery. A narrowly scoped recipe with behaviour-preservation fixtures is a concrete contribution. | [OpenRewrite repository](https://github.com/openrewrite/rewrite) contributing guide and public issues; employer pages for career enquiries. |

## Papers and technical reading mapped to a purpose

Foundational work is labelled by its actual date, rather than presented as recent news. Conference/paper landing pages, abstracts and relevant documentation were checked; no claim of reproducing these results is made.

| Reading | What to extract and challenge |
| --- | --- |
| [MLIR: Scaling Compiler Infrastructure for Domain Specific Computation, CGO 2021](https://research.google/pubs/mlir-scaling-compiler-infrastructure-for-domain-specific-computation/) | Why multiple IR abstraction levels and reusable infrastructure matter; implement/review one lowering and state which semantics it preserves. Connect to current LLVM work instead of assuming the paper’s original performance claims describe 2026. |
| [DuckDB: An Embeddable Analytical Database, SIGMOD 2019](https://duckdb.org/library/duckdb-sigmod-demo/) | In-process analytics and vectorised execution. Re-evaluate a current workload before preferring distributed processing. Historical demo paper, not a current exhaustive benchmark. |
| [FoundationDB: A Distributed Unbundled Transactional Key Value Store, SIGMOD 2021](https://www.foundationdb.org/files/fdb-paper.pdf) | Separation of transaction/storage roles, failure handling and deterministic simulation; distinguish a model/checker’s coverage from arbitrary real-world execution. |
| [CHERI: Hardware-Enabled C/C++ Memory Protection at Scale, IEEE Security & Privacy, July/August 2024 PDF](https://www.cl.cam.ac.uk/research/security/ctsrd/pdfs/20240419-ieeesp-cheri-memory-safety.pdf) | Architectural capability bounds, compatibility and software/hardware co-design. The current project page labels its article link August 2025, but the linked PDF says July/August 2024; the PDF date is used here. Do not reuse early performance results as current production measurements. |
| [How Amazon Web Services Uses Formal Methods, CACM 2015](https://www.amazon.science/publications/how-amazon-web-services-uses-formal-methods) | Understand specifications/counterexamples in distributed services. Compare historical method lessons with the separate 2025–2026 product evidence above. |
| [Agentic Web Accessibility Auditing, arXiv v2, 10 September 2026](https://arxiv.org/abs/2609.09379v2) | Current preprint, not established consensus. Criterion-specific agent framework; ancillary metrics, prompts and research records are listed. Inspect false positives, ground truth and evaluated scope before treating audit automation as solved. Code/data reuse licences need per-artifact review. |
| [Model-Driven Legacy System Modernization at Scale, ReCode 2026](https://arxiv.org/abs/2602.04341v1) | Experience report using an intermediate model; authors report that standard patterns automate more easily than bespoke layout composites. Distinguish one industrial case from general success rates. Page lists an accepted workshop publication and DOI. |

## Open tools, data and licence boundaries for proposed projects

None was installed. Prefer already available approved tools for initial work; request approval before any needed download/install. Licences below describe the checked core repository, not every dependency, extension, model, paper or dataset. Code licences do not transfer rights to private customer data.

| Tool/resource | Checked licence/status | Suitable use and limitation |
| --- | --- | --- |
| LLVM | [Official release index](https://releases.llvm.org/index.html) describes Apache-2.0 with LLVM exception for modern releases. | Compiler/profile experiments; avoid version/date confusion from index metadata. |
| BusTub | [MIT; explicitly educational](https://github.com/CMU-DB/bustub). | Learn storage/query internals; not production and not a reason to post assignment solutions. |
| quiche | [BSD-2-Clause](https://github.com/cloudflare/quiche). | Local QUIC/HTTP3 experimentation. Application still provides I/O/event-loop integration; protocol library alone is not a service. |
| Zephyr | [Apache-2.0 core repository](https://github.com/zephyrproject-rtos/zephyr). | Simulator-based firmware, drivers and tests; hardware effects still require hardware validation. |
| TLA+ TLC/toolbox | [MIT](https://github.com/tlaplus/tlaplus). | Model checking. Bounded state exploration is not automatically a proof of an unbounded implementation. |
| Dafny | [MIT core, with identified third-party material](https://github.com/dafny-lang/dafny). | Contracts/invariants and verified program exercises. Review assumptions and subcomponent licences. |
| axe-core | [MPL-2.0](https://github.com/dequelabs/axe-core). | Automated checks as part of broader evaluation, with manual/assistive-tech coverage. |
| OpenRewrite | [Apache-2.0](https://github.com/openrewrite/rewrite). | AST-based transformation recipes; verify the licences of separately selected recipes/platform services. |
| Project test data | Prefer self-generated deterministic records, owned source and purpose-built interaction fixtures. | Record generator seed, schema, skew, faults and rights. Synthetic-data success does not establish customer distribution or production scale. Public datasets require their own licence and suitability checks. |

## Proposed 30/90-day projects with baselines and transfer tests

Choose one main track, not seven simultaneous builds. These plans are educational and research designs, not promises of mastery or admission to senior jobs in 90 days. Use approvals before software/hardware acquisition, publication, contribution submission, user studies or private-data access. Performance targets must be set after measuring baseline noise and business/error costs; no arbitrary speedup is presented as a market benchmark.

### P1 — Explainable performance improvement, then a compiler/runtime contribution

**Days 1–30:** select an owned/publicly licensed parser, serializer or data-processing kernel with a realistic service wrapper. Generate inputs with small/large/skewed cases. Record correctness, CPU time, throughput, allocation/RSS and p50/p95/p99 over repeated randomised runs. Profile before editing. Compare an algorithm/layout change against compiler-flag/runtime changes and the unmodified baseline. Existing system profiling facilities may be enough; no new tool is required merely to produce a plan.

**Days 31–90:** validate on an unseen input distribution and, if an existing authorised second environment is available, another architecture/runtime. Submit nothing externally until authorised. Prepare a reduced bug, regression test or narrowly justified improvement for the appropriate project. Report confidence intervals/noise, build flags, saturation and correctness; include regressions and negative results.

**Transfer test:** explain why the improvement should or should not survive a change in data shape, concurrency or CPU. Diagnose a deliberately changed bottleneck without copying the original solution. Leadership evidence is a defensible trade-off memo and reproducible artefact, not a spectacular isolated number.

### P2 — Query/storage diagnosis with recovery evidence

**Days 1–30:** use an available approved database and self-generated data with explicit skew, nulls, time boundaries and updates. Define three query shapes. Capture plans, exact result checks, cold/warm behaviour, read/write throughput, tail latency and disk/memory footprint. Compare one index/layout/query change with the untouched baseline; do not silently change durability settings.

**Days 31–90:** add concurrency and controlled process termination in a disposable environment; test restart/restore and invariant preservation. Evaluate the chosen change on a later/unseen workload and document when it loses. An internals alternative is a small educational storage/execution component with reference results, not deploying a new database.

**Transfer test:** explain a slow query with a changed distribution and show why an index speeds reads but may harm writes or storage. Contribution path: a minimized planner/recovery repro, regression test or documentation improvement. Prove the workload belongs to the claimed OLTP/analytic use case.

### P3 — Distributed failure and protocol lab

**Days 1–30:** build around an existing available queue/service or a small owned fixture: two workers, retries, durable state and an explicit side effect. Enumerate duplicate, crash-before/after-commit, delay and reorder cases. Compare naive retry with the intended idempotency/outbox strategy. Record successful operations, duplicate effects, loss, recovery time, queue age and resource cost.

**Days 31–90:** add bounded faults/partitions and a local protocol or scheduler regression. Compare fixed workload and offered-load curves; distinguish throughput from goodput and overload collapse. Link a state model to failure tests. A local QUIC case is optional if its tools already exist or their installation is approved.

**Transfer test:** change the failure timing or add a second consumer and predict the invariant before running. State liveness assumptions: no system can promise completion during an indefinitely unavailable dependency without additional assumptions. Contribution path: reproducible failure trace and robust regression.

### P4 — Firmware with constrained resources, first simulated then measured

**Days 1–30:** inspect a bounded RTOS/sensor-buffer task using approved existing simulation tools, or design the test fixtures pending installation approval. Model interrupts/message arrivals, overflow, reset and corrupted input. Track RAM/ROM, queue high-water mark, deadline misses and recoverability. Compare a simple baseline with one buffering/scheduling change.

**Days 31–90:** obtain separately approved hardware/lab access only if the task needs it. Validate real timing, energy and I/O; explicitly report which emulator conclusions failed to transfer. Produce a driver/simulator regression, footprint improvement or release validation contribution.

**Transfer test:** handle changed sampling rate and memory budget, and explain why simulator cycle counts are not board power measurements. Leadership path: release readiness, failure triage and cross-layer coordination, matching the observed Arm release role rather than only a blinking-LED demo.

### P5 — A specification that first finds a bug

**Days 1–30:** specify a small two-worker task/lease or retry protocol. Write safety and liveness claims in plain language first, then a bounded state model. Confirm a deliberately incorrect design produces the intended counterexample. Repair it and record explored bounds, assumptions and remaining exclusions. An alternative is a Dafny component with executable reference tests and explicit pre/postconditions.

**Days 31–90:** connect model scenarios to implementation fault tests or verify a reusable component. Change one assumption—lease expiry, clock behaviour or message duplication—and determine whether the proof/model still applies. Measure model/proof runtime and maintenance cost, not just “green” status. Compare AI-assisted modelling with independently reviewed specifications.

**Transfer test:** identify a specification that trivially passes by omitting the real requirement, or an axiom that makes a proof meaningless. Original-contribution route: a missing failure mode, more usable invariant library, smaller counterexample or actionable tooling feedback. Distinguish research-scientist and product-engineering pathways.

### P6 — Accessible interaction, beyond scanner completion

**Days 1–30:** build/evaluate an owned fixture containing a modal, validation form, dynamic list, table and keyboard interaction. Define representative tasks and states. Establish automatic findings plus manual keyboard and available assistive-technology baselines. Repair native semantics, focus, naming and error communication; keep a trace from issue to WCAG criterion and task impact.

**Days 31–90:** with separately authorised participation, involve a qualified accessibility practitioner and/or disabled users in task evaluation. Do not simulate a person’s disability and call that user evidence. Add component regressions and compare automated/agentic/manual findings, false positives and missed task blockers. Measure task completion/errors and rework, with a scoped conformance statement rather than blanket certification.

**Transfer test:** handle a changed dynamic state or input method and explain the accessible tree rather than only the DOM. Contribution route: a well-evidenced axe rule/report, accessible component pattern, evaluation fixture or research replication. Leadership means a repeatable design-system and delivery practice.

### P7 — Migration with a behavioural oracle and reversible cutover

**Days 1–30:** select owned/publicly licensed source and an outdated dependency/runtime or interface. Freeze behaviour via characterisation tests and generated edge-case data. Inventory APIs, schema, dates, identifiers, ordering and error behaviour. Compare a manual upgrade/refactor with a deterministic recipe or AI-assisted draft while recording review and repair effort.

**Days 31–90:** implement a narrowly scoped transformation, differential-run old/new behaviour and exercise restart/rollback on disposable state. Record unexplained differences, regression escape, cutover duration, data invariants, performance and total person-hours. If using OpenRewrite, write recipe tests for both transformed and deliberately unchanged cases. Business-semantic differences must be reviewed, not normalised away until tests agree.

**Transfer test:** migrate an unseen variant and identify when a superficially identical API has different semantics. Original-contribution route: a tested open recipe, compatibility fixture, migration failure taxonomy or reproducible evaluation. Leadership means sequencing risk, obtaining domain decisions and preserving service continuity.

## A fair AI comparison and evidence of independent expertise

For any chosen project, measure the whole job: understand requirements, implement, verify, diagnose failures and maintain a later change. Compare AI-assisted work with a clear baseline; count prompts, review, debugging, retries and tool cost. Keep an unseen transfer case so a rehearsed benchmark cannot masquerade as competence. If AI wins, retain the win; if it makes a critical error, explain the violated invariant and improve the oracle. The goal is neither to prove AI useless nor to call a generated artefact expertise.

Evidence of leadership can grow through a sequence: reproducible result → useful contribution and respectful review → ownership of a difficult subsystem or standard → mentoring others through diagnosis → a track record of deployment/operational outcomes. Public reputation should follow useful work. No publication, PR or message was sent during this research.

## Remaining gaps for the next assigned research pass

1. Job sampling is deliberately small and senior-skewed. A separate deduplicated employer-page cohort should include entry/mid-level, hiring dates, country eligibility and actual advertised pay where available. Do not combine it with other workers’ samples without deduplication.
2. The accessibility tender is indexed primary evidence of an estimated procurement budget; the award/current spend remains unchecked. Direct access returned 403. Other fields lack project-level budgets in this contribution.
3. Technical releases establish what shipped, not adoption, return on investment or future vacancies. Upgrade/compatibility rollout evidence would improve the ranking.
4. India/UK lab access, postgraduate routes, scholarships and employer sponsorship require specific official opportunity checks. A public lab or mailing list is not a promise of an open position.
5. Several papers are foundational, and recent audit/modernisation studies need deeper methods and artefact examination before quantitative claims are reused. No experiment was reproduced.
6. Tools/licences were checked at repository level; specific dependencies, datasets and contribution policies need rechecking when an implementation target is selected.
7. The highest-value next decision is which specialty fits both sustained interest and an accessible real problem. No source here justifies a universal pivot, guaranteed salary, guaranteed remote role or five-year automation-proof label.
