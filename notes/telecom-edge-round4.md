# Telecom, wireless and edge infrastructure: a developer's outlook through 2031

Cutoff: 19 October 2026. Scope: 5G Advanced, Open RAN, private industrial networks, edge inference, network automation and 6G readiness. This extends the earlier systems/compute work without repeating its compiler, database or hardware overview. No software/data installation or download, paid compute, network scanning, radio transmission, communications/configuration changes, private access, outreach or child agents occurred. Experiments below are proposals, not completed work.

## Finding and career implication

The actionable software opportunity is in **making existing networks programmable, observable, interoperable and useful to an application with a real service requirement**. That includes cloud-native network functions, test/assurance automation, network APIs, telemetry and controlled policy loops, private-network application integration and edge-placement decisions. It is different from inventing an air interface, designing RF equipment or installing industrial radios.

There is real deployment and spending, but the source set does not establish a general shortage of telecom developers or guaranteed growth in 2031 salaries. Open interfaces create integration/testing work and can lower some entry barriers; they do not remove operator procurement, interoperability, support or spectrum constraints. A sensible near-term path for an application/AI engineer is Linux/cloud/network fundamentals plus one specific telecom software boundary, while learning enough radio/core architecture to avoid false assumptions.

6G is a standards/research and early-product-development opportunity at this cutoff, rather than an already deployed mass market. By 2031, 4G/5G, fibre, Wi-Fi, private networks and early 6G are likely to coexist. That coexistence is a forecast from deployment and standardisation timelines, not a measured future market share.

## 1. Standards: completed features, studies and deployment are different states

| Layer | Primary evidence and date | What it supports | What it does not support |
| --- | --- | --- | --- |
| 5G Advanced releases | [3GPP release portal](https://portal.3gpp.org/Releases.aspx) lists Release 18 frozen on 21 June 2024 and Release 19 frozen on 12 December 2025. Its [June 2025 technical newsletter](https://www.3gpp.org/images/newsletters/3GPP_Highlights_Issue_10_WEB.pdf) describes Rel-19/20 evolution. | Stable specifications are available as engineering/study anchors. | A release freeze is not proof every optional feature is implemented in a device, core, radio or commercial network. |
| Release 20 | [3GPP portal](https://portal.3gpp.org/Releases.aspx) shows it open with a June 2027 end milestone; [RAN#113 reports, September 2026](https://www.3gpp.org/news-events/3gpp-news/ran113-reports) describe 5G Advanced work alongside 6G studies. | Ongoing work, with current 5G evolution and future 6G research separate. | A study item is not a normative deployable 6G specification. |
| First normative 6G release | [3GPP's Release 21 timeline announcement](https://www.3gpp.org/news-events/3gpp-news/rel21-timeline), June 2026; 3GPP's indexed home-page text confirms a December 2028 functional-freeze target. | A scheduled specification process, with Rel-21 combining 5G evolution and initial 6G work. | Target dates are not product availability, spectrum assignment or widespread 2030 deployment. Direct opening of the announcement returned 403 in this pass; see access limits below. |
| IMT-2030 evaluation | [ITU-R IMT-2030 page](https://www.itu.int/en/ITU-R/study-groups/rsg5/rwp5d/imt-2030/Pages/default.aspx), February/June 2026 updates | Draft technical performance requirements and evaluation guidelines; candidate radio proposals invited February 2027–February 2029. ITU explicitly says requirements are not guaranteed real-world performance. | The drafts were pending parent-group approval in December 2026 at this cutoff. Headline performance capabilities must not become application SLAs. |
| Edge application environment | [ETSI MEC group](https://www.etsi.org/technical-groups/mec/?id=1700) and [MEC 002 V4.2.1, May 2026](https://www.etsi.org/deliver/etsi_gs/MEC/001_099/002/04.02.01_60/gs_MEC002v040201p.pdf) | APIs, application requirements and multiple edge placements. ETSI explicitly includes fixed and WLAN access, not only mobile networks. | Edge computing does not require a new cellular generation, nor does proximity alone guarantee useful end-to-end latency. |

Potential 5G Advanced topics include reduced-capability devices, network energy management, positioning, slicing, AI/ML support and additional communication scenarios. Study the relevant normative feature and implementation support, rather than learning a marketing list as if all features arrive together. Vodafone's [current network programme description](https://www.vodafone.com/news/newsroom/technology/vodafone-advances-future-ready-radio-access-network) itself conditions new feature introduction on market demand and vendor support.

## 2. Real operator progress, money and counterevidence

### Open RAN: readiness is not the same as complete multi-vendor deployment

AT&T's [3 March 2026 update](https://about.att.com/blogs/2026/att-advances-open-ran-readiness.html) says more than half its radio swap programme was completed and more than half its traffic ran on **open-capable hardware**. In the same update, Cloud RAN was live in two cities, a commercial call using Ericsson basebands and 1Finity radios had been completed, and a third-party rApp was operating in its production network. These are distinct maturity facts. Do not rewrite “open-capable” as “all traffic already running on a fully interchangeable multi-vendor Open RAN.”

AT&T's [innovation disclosure](https://sustainability.att.com/priority-topics/innovation-technology) describes about **US$14 billion over five years** for its Ericsson-led programme and a late-2026 open-capable traffic target. This is an operator investment commitment with a deployment programme, not software-vendor revenue available to small teams or a count of developer vacancies.

Vodafone's [programme description](https://www.vodafone.com/news/newsroom/technology/vodafone-advances-future-ready-radio-access-network) mixes existing sites, future country/site plans, current strategic vendors and planned automation. Its large numbers should be kept as plans where described as plans. This contribution does not infer current UK site counts from older announcements or a new nationwide rollout from a trial.

### Private 5G: a completed industrial deployment has substantial operations work

Three Group Solutions [reported on 13 January 2026](https://groupsolutions.three.com/insights/three-group-solutions-completes-private-5g-network) completion of private 5G across Felixstowe, Harwich International and London Thamesport. Its account describes parallel 4G/5G operation during migration, staged movement of assets, dual cores, overlapping coverage and diverse links. This is a named operator deployment; performance and business benefits remain operator-reported rather than independently reproduced here.

The important software implication is the operating problem: device onboarding, application integration, telemetry, reliable migration and fault handling. The case does not show that every factory should replace Wi-Fi or that an application developer can deploy the full radio/core/industrial system alone.

### Assurance has concrete programme budgets, with eligibility requirements

The UK's [SNPN 5G Assured Integration competition](https://apply-for-innovation-funding.service.gov.uk/competition/2400/overview/cbbc48e2-d78e-42cd-b570-330f702ba82f) specified grant requests of **£2–4 million**, 18-month projects starting August 2026, UK work/exploitation requirements and an accountable systems integrator for multi-vendor design and assurance. This is evidence of a funded programme structure and purchasing priorities, not a current open grant invitation or confirmed spend/award to a particular applicant.

Digital Catapult's [1 April 2026 SONIC end-of-programme account](https://www.digicatapult.org.uk/publications/post/sonic-labs-end-of-programme-impact-report-2026/) reports 82 product tests, seven interoperability cohorts and 27 vendors. The report is programme-produced and includes self-reported commercial outcomes. It supports the practical importance of integration/validation, but the completed programme should not be presented as a current unlimited free-lab offer.

### Product lifecycle is real counterevidence

Microsoft's [archived Azure Private 5G Core documentation](https://learn.microsoft.com/en-us/previous-versions/azure/private-5g-core/private-5g-core-overview) documents a 30 September 2025 retirement date and partner migration options. This shows that a large cloud vendor's original product can be withdrawn. It is not evidence that all private networks fail, that the service's exact shutdown was tested here, or that a different supplier cannot deliver a viable solution.

## 3. A useful technical map for software engineers

### Open RAN and cloud-native network functions

- Disaggregation: radio unit, distributed unit and centralised unit → functional splits/interfaces → compute and transport requirements → interoperable configuration → service-level operation.
- Network software platform: VNF/CNF lifecycle → placement, configuration, scaling and upgrade → resource isolation/acceleration constraints → observability and recovery → application/network quality.
- Control and automation: telemetry schema and timestamp quality → policy scope and timescale → decision/actuation → conflicting policies and rollback → measured network outcome.
- Assurance: reproducible component versions → conformance and interoperability tests → load/fault scenarios → coverage gaps → evidence supporting deployment decisions.

An rApp/xApp is a software product with a contract, deployment boundary and control timescale. It is not a generic LLM agent allowed to change anything in a live network. Fast radio scheduling, management policy and application-placement loops solve different problems. A model with good offline prediction accuracy may be too slow, unstable or unable to actuate the relevant parameter.

### Private industrial networks

- Requirement: mobility, uplink traffic, coverage, deterministic task deadline or isolation → compare an existing LAN/Wi-Fi/LTE design → select a justified cellular/edge configuration.
- Application path: device/sensor and identity → radio and core → user-plane/edge placement → application processing → decision/actuator and human intervention.
- Operations: SIM/eSIM and device lifecycle → policy and network identity → industrial integrations → staged migration → faults, maintenance and long-lived support.
- Delivery: buyer and budget → system integrator → radio/site/spectrum specialists → software owner → measurable operational outcome.

The natural small-team wedge is a component or measurable workflow inside an existing operator/integrator/customer relationship. Owning a complete private mobile network introduces RF planning, physical installation, support, spectrum and procurement dependencies.

### Edge inference and network APIs

- Placement: device vs on-premise edge vs operator edge vs regional cloud → transport/queueing and compute → quality/deadline under load → recovery/disconnected operation → cost and energy.
- API integration: network context/capability → authenticated access and policy → consistent application behaviour when information is stale/unavailable → value over a normal application implementation.
- Scaling: avoid one-off edge deployments without fleet management → version/model rollout → resource contention and overload → diagnostics → recurring operating economics.

The opportunity is an end-to-end application improvement. Sending a model to a nearby server can lose if transfer, queueing or orchestration dominates. Fixed/WLAN edge alternatives may satisfy the same need with simpler integration.

### 6G research and early engineering

- Research hypotheses: new sensing/communication integration, radio/architecture/AI concepts → channel and traffic assumptions → comparative simulation → measured prototype → standard contribution and deployability.
- Software-accessible pieces: evaluation environments, workload/channel models, test automation, protocol prototypes, reproducibility and standards-to-test mapping.
- Specialist pieces: RF/channel measurement, antenna/beamforming and physical-layer algorithm design → EE/signal-processing depth and calibrated equipment → spectrum/testbed access → field validation.

A software engineer can contribute to research infrastructure without claiming to be an RF specialist. A research proposal or preprint should not be mistaken for a standard decision or a deployment forecast.

## 4. End-to-end latency, reliability, energy and spectrum assumptions

**Latency:** define the application's start/end events and clock synchronisation. Include sensing/encoding, radio scheduling/retransmission, transport/backhaul, core/user-plane, edge queues/compute, output and actuation. Report percentiles and deadline misses under offered load and mobility, not only unloaded average ping or a radio-interface target. Overlapping stages require critical-path accounting. A network-only claim and an application SLA are different measurements.

**Reliability:** define packet/service/decision success, time window, traffic load and failure domains. Dual cores and coverage do not remove common power, backhaul, software/configuration or security dependencies. Small tests with zero observed errors cannot establish ultra-rare failure probabilities; temporal correlation and adequate exposure matter. Measure recovery and degraded operation as well as steady state.

**Energy:** decide whether the boundary is UE, radio, compute, transport or facility. Count idle capacity, cooling and inference/control overhead where relevant. Radio sleep can affect coverage, capacity and wake-up delay; an optimiser must show the QoS trade-off. Less data traffic, fewer model operations or a favourable simulator proxy is not a measured full-system energy reduction.

**Spectrum and deployment:** [Ofcom's shared-access guidance, updated 1 May 2026](https://www.ofcom.org.uk/spectrum/frequencies/shared-access), describes specific licence types, bands and geographic/power conditions. India's [DoT authorisation portal](https://www.eservices.dot.gov.in/authorisation-portal) and [CNPN FAQs](https://eservices.dot.gov.in/faqs?page=1) distinguish captive authorisation from separate wireless spectrum assignment. These are access gates, not permission to transmit from an SDR or scan neighbouring networks. This research proposes local simulation/offline analysis only.

## 5. Software/data ecosystem: current changes and licence limits

| Resource | What was checked | Contribution/experiment value and limit |
| --- | --- | --- |
| [OCUDU 26.04 transition announcement](https://www.srsran.com/press_releases/srsran_becomes_ocudu/) and [project](https://gitlab.com/ocudu) | SRS says srsRAN Project is now OCUDU, with neutral Linux Foundation governance and a BSD 3-Clause Open MPI licence. Historical srsRAN AGPL repository/forum/docs are archived/historical. | A substantive 2026 change to starting instructions and licensing. Pin the actual new repository/release and dependencies; do not use archived instructions as current deployment guidance. |
| [free5GC](https://github.com/free5gc/free5gc) | Core repository identifies Apache-2.0 and an official support forum; repository description references 3GPP R17. | Core/session/configuration/telemetry learning and test contributions. Implemented features are not blanket Rel-18/19 or carrier-grade certification. |
| [UERANSIM](https://github.com/aligungr/UERANSIM) | It explicitly says physical NR is partial and simulated over UDP. Live page identifies AGPL-3.0/commercial terms, but also contains a 2027 copyright line. | Useful UE/gNB/core testing candidate, **not a validated RF/PHY simulator**. The future-dated line prevents treating the live README as a clean cutoff-version licence audit; pin and check a pre-cutoff release before implementation. Attempts to inspect v3.2.6 files through the web tool failed. |
| [5G-LENA](https://cttc-lena.gitlab.io/5g-lena-website/) and [version documentation](https://cttc-lena.gitlab.io/nr/html/) | CTTC describes GPLv2 and end-to-end NR simulation. Documentation lists NR-v5.1 with ns-3.48, released 6 August 2026. | Explicit models and supported feature/version combinations for comparative simulation. Simulated compliance/performance is not field certification or measured industrial reliability. |
| [OpenAirInterface licensing](https://openairinterface.org/oai-public-license-v1-1/) and [CSSL transition](https://openairinterface.org/cssl-the-oai-move-to-a-generic-license/) | OAI PL1.1 separates research/study patent permissions and FRAND negotiation for other purposes; OAI describes evolving this model into CSSL for Duranta. | Do not call all OAI components/version combinations permissive Apache software or imply copyright access resolves essential-patent/commercial terms. Inspect the exact target repository/version and contribution agreements. |
| [ETSI MEC Forge group](https://labs.etsi.org/rep/mec) | Public APIs and developer/test work are linked by ETSI's MEC group. | Standards/API conformance and application integration. Review each repository's terms; no blanket licence inferred from ETSI branding. |
| [OpenRAN Gym datasets](https://openrangym.com/datasets) and [ColO-RAN dataset repository](https://github.com/wineslab/colosseum-oran-coloran-dataset) | Dataset describes 7 base stations, 42 static users, a Rome emulation scenario and three traffic classes; repository displays GPL-3.0. | A public experimental dataset, not a nationwide operator/industrial trace. Verify data/associated provenance terms. Train/test separation by conditions matters; randomly splitting adjacent rows risks leakage. |

The source ecosystem is accessible enough for a first software experiment, but combining a virtual core, simulated UE and generated traffic does not reproduce the full radio, interference, mobility or operational environment.

## 6. Labs, companies, researchers and public channels

No contact was initiated. Public institutional/project channels are listed as future routes; they do not imply free equipment, available supervision, an open grant or a vacancy.

| Organisation/path | Relevant technical work | Official channel and access reality |
| --- | --- | --- |
| 3GPP and ITU-R | Standards status, traceable requirements and evaluation models; conformance-to-test mapping. | [3GPP portal](https://portal.3gpp.org/Releases.aspx), [ITU IMT-2030](https://www.itu.int/en/ITU-R/study-groups/rsg5/rwp5d/imt-2030/Pages/default.aspx). Read public specs first; formal participation has organisational procedures. |
| ETSI MEC | Edge application/API requirements and interoperability. | [MEC group](https://www.etsi.org/technical-groups/mec/?id=1700) links developer, Forge, sandbox and participation routes. Sandbox/API learning is not an operator deployment. |
| SRS/OCUDU; OAI | CU/DU/core/protocol implementation, simulation and integration. | [OCUDU transition/project](https://www.srsran.com/press_releases/srsran_becomes_ocudu/), [OAI](https://openairinterface.org/oai-license-model/). Use current project contribution channels, not the closed historical srsRAN forum. |
| Northeastern WiNES/Open6G/OpenRAN Gym; Michele Polese, Leonardo Bonati, Salvatore D'Oro, Stefano Basagni and Tommaso Melodia author the cited dataset/paper | Data-driven RAN control, experimental reproducibility and emulation/testbeds. | [Dataset/project](https://openrangym.com/datasets/colosseum-coloran-dataset) links institutional and repository routes. Public data can be studied locally; access to Colosseum is a separate matter. |
| CTTC OpenSim/5G-LENA | End-to-end NR models, schedulers and reproducible simulation. | [Official site](https://cttc-lena.gitlab.io/5g-lena-website/) and [repository](https://gitlab.com/cttc-lena/nr). A reduced scenario or model-validation contribution is a credible entry. |
| University of Surrey 5G/6G Innovation Centre; Rahim Tafazolli's [official research profile](https://openresearch.surrey.ac.uk/esploro/profile/rahim_tafazolli/output/publication.journalArticle?institution=44SUR_INST) | Wireless architecture and academic/industrial research spanning 5G/6G. | [Centre](https://www.surrey.ac.uk/institute-communication-systems/5g-6g-innovation-centre) lists institutional membership/contact/study routes. Research degrees and funded posts require separate current checks. |
| University of Bristol Smart Internet Lab | Communications/network research and research infrastructure, relevant to software/testbed and EE paths. | [Official group](https://www.bristol.ac.uk/research/groups/smart/). No inference of open equipment access or a current hiring round from a project page. |
| Indian indigenous 5G testbed partners: IIT Madras, IIT Bombay, IIT Kanpur, IIT Delhi, IIT Hyderabad, IISc, CEWiT and SAMEER | Core/RAN implementations, system simulation, protocol and radio testbed work. | [Official testbed contacts](https://5gtestbed.in/contacts.jsp) and [CEWiT/testbed access contacts](https://user.cewit.org.in/5gtb/linkfiles/new/ContactDetail.html). Access, current charges and licensing need confirmation; older free-access programmes are not assumed current. |
| Digital Catapult assurance/advanced-connectivity teams | Interoperability, test evidence, private-network assurance and integrator collaboration. | [SONIC 2026 report](https://www.digicatapult.org.uk/publications/post/sonic-labs-end-of-programme-impact-report-2026/) links institutional contacts and newer programme material. SONIC's original programme has ended. |
| Operators/integrators: AT&T, Vodafone, Three; vendors/platform teams such as Ericsson and Canonical | Production network evolution, CNF lifecycle, automation, assurance, industrial integration. | Official deployment/job pages below; private operational data and live-policy access are not publicly available by default. |

### Role samples and distinct prerequisites

[Ericsson's Bangalore Senior Software Engineer role, job 789745](https://jobs.ericsson.com/careers/job/563121777121454?domain=ericsson.com&triggerGoButton=false), describes cloud-native infrastructure powering its 5G portfolio, lifecycle ownership, CI qualification, containers/Kubernetes and Python/Robot automation. This is a directly observed India software-product path. It does not establish a requirement for an RF research PhD or indicate national hiring volume.

[Canonical's Telco Cloud Field Engineer](https://canonical.com/careers/3748266/telco-cloud-field-engineer-remote) describes VNF/CNF/NFV/MEC architectures, OpenStack/Kubernetes/SDN, customer delivery, defect investigation and infrastructure automation. The location is Americas/EMEA remote; that does **not** establish India eligibility. Field/customer delivery includes integration and communication responsibilities beyond writing code.

The EE/RF/onsite path instead needs the relevant signal-processing, channel/propagation, antenna/PHY, calibrated equipment, site/spectrum and measurement expertise. Some people bridge both paths, but a working virtual core or Kubernetes certificate is not evidence of those physical competencies. No salary or workforce forecast follows from two deliberately selected job descriptions.

## 7. Papers worth reading with a falsifiable question

- [ColO-RAN: Developing Machine Learning-based xApps for Open RAN Closed-loop Control, 2022](https://arxiv.org/abs/2112.09559): connect telemetry, action space and testbed results. Ask which conclusions depend on static users, traffic model, supported schedulers and measurement period; the linked dataset makes a bounded replication possible.
- [OpenRAN Gym: AI/ML Development, Data Collection, and Testing for O-RAN on PAWR Platforms, 2022](https://arxiv.org/abs/2207.12362): understand the data→controller→emulator/testbed pipeline. Ask whether a locally replayed trace can validate a new policy or only its predictor; policy evaluation needs an environment/counterfactual model.
- [An open-source implementation and validation of NR Configured Grant for URLLC in 5G-LENA, June 2026](https://arxiv.org/abs/2606.18763): a concrete scheduling/model-validation research candidate. Only metadata/abstract were checked in this pass; inspect artefacts, assumptions and methods before reusing quantitative results.
- [6G as It Is Actually Being Built: Insights from Early 3GPP Standardization, October 2026](https://arxiv.org/abs/2610.05694): a current synthesis that explicitly distinguishes approved, draft, individual proposal and vendor demonstration. Treat it as the authors' synthesis, not a substitute for a 3GPP decision record. No quantitative claims from it are adopted here.

## 8. Proposed 30/90-day experiments: local software first

Choose one main project. Use existing approved tools or prepare fixtures/specifications pending installation approval. No RF transmissions, device/network configuration changes, live scanning or paid resources are necessary for the initial designs. No experiment below has been run.

### T1 — Edge-placement latency and reliability decision

**Days 1–30:** choose one synthetic application task with explicit input size, compute requirement, deadline and quality. Compare device-local, LAN/WLAN edge and regional-cloud placements under generated delay/loss/queue traces. Separate measured local compute from modelled network stages. Baselines include the current/simple placement and a deterministic threshold policy; no “5G is faster” assumption.

**Days 31–90:** add burst loads, backhaul loss, cold starts, stale context and disconnected operation. Validate the model with an authorised public trace or testbed if available; otherwise retain simulation scope. Measure deadline-miss rate, useful completed tasks, tail latency, data transfer, resource cost and confidence/coverage. Do not claim rare-event SLA assurance from a short run.

**Kill/limit:** benefit disappears against LAN/Wi-Fi/fibre or local processing; queue/transfer cost dominates; required operator API is unavailable; model cannot predict a held-out condition. Original contribution: a reproducible placement evaluator, API fallback test or useful negative result.

### T2 — RAN controller baseline with drift and action limits

**Days 1–30:** inspect ColO-RAN metadata and, after any necessary download approval, a bounded subset. Reproduce a simple telemetry summary/forecast with persistence and fixed/rule-based baselines. Split by time/configuration/base-station condition rather than random adjacent rows. Record exactly what the dataset can and cannot observe.

**Days 31–90:** use an approved simulator/environment for an actual controller comparison. Match action/measurement timescales, incorporate stale telemetry, drift and conflicting objectives, and compare fixed/RR/PF or appropriate deterministic policies before adding ML. Track deadline misses, throughput/fairness, controller overhead, stability and recovery, not only prediction error/reward.

**Kill/limit:** offline prediction is presented as policy improvement; policy requires unavailable knobs; simulation assumptions make the answer trivial; improvement disappears under changed traffic/mobility or a stronger rule baseline. Original contribution: a leakage-resistant evaluation, drift test, latency-aware controller or model mismatch correction.

### T3 — Virtual core/UE lifecycle and failure lab

**Days 1–30:** specify a disposable, entirely local core/UE environment with synthetic test identities. Pin compatible versions and licences before implementation. Verify registration, session creation, data path and clean release; map PLMN/DNN/slice parameters and user-plane placement to actual observed state.

**Days 31–90:** inject controlled local process failure, delayed/repeated messages, restart and configuration mismatch. Check session cleanup, address/tunnel state, recovery time, diagnostics and resource growth. Produce an executable regression/reproducer and clear issue-to-protocol trace. Use UERANSIM only within its partial-radio model; its UDP link does not validate real NR/PHY behaviour.

**Kill/limit:** privileges/routing isolation are unavailable; no supported version pair or clean licence audit; normal application traffic is affected; results are described as RF coverage, handover or industrial reliability evidence. Original contribution: protocol/session regression, reproducible deployment issue or better diagnostics.

### T4 — Offline network automation with a controlled policy boundary

**Days 1–30:** define a synthetic inventory/configuration/telemetry model and allowed actions. Build schema checks, invariant checks and a dry-run diff; compare a deterministic rule implementation with an AI-assisted proposal/review path. Count requirements understood, wrong proposals, review effort and repair time.

**Days 31–90:** replay stale/conflicting observations and failed/partial action outcomes in a simulator. Add idempotency, action budgets, rollback and evidence links. Measure dangerous/invalid proposal rate, time to a verified plan, recovery and maintenance on an unseen schema/version change. No real changes or autonomous network control are part of this research.

**Kill/limit:** a convincing generated plan cannot be checked; telemetry cannot distinguish causes; loop oscillates; extra model/control cost exceeds a reliable rule baseline. Original contribution: policy-test fixture, typed action adapter, conformance test or useful closed-loop failure example.

### T5 — Reproducible NR scheduling/assurance experiment

**Days 1–30:** select one supported 5G-LENA version/scenario and write a hypothesis about a scheduler/traffic combination. Establish seeds, load, channel/mobility assumptions, baselines and result checks. Keep initial work CPU-scale and compare to a reference/example before extending the model.

**Days 31–90:** test a held-out load, channel, mobility or failure condition. Report latency distribution, useful throughput, fairness, retransmissions and modelled energy only if the model justifies it. Seek an original contribution through a model-validation test, scheduler corner case, reproducibility fix or standards-to-simulation discrepancy.

**Kill/limit:** conclusions depend on one favourable seed or unrealistically fixed channel; offered load/quality differs across baselines; numerical results are called field measurements; a simulated packet target is promoted to an application SLA.

## 9. Expertise and leadership outcome by 2031

The portable foundation is networking/Linux and distributed software, then core/RAN architecture, then rigorous measurement and one concrete boundary such as CNF lifecycle, E2 telemetry/control, MEC APIs or private-network application assurance. Research-oriented 6G work adds deeper mathematics/radio modelling and testbed collaboration. A complete air-interface pivot is optional; transferable software work exists around current networks.

Leadership evidence should be a subsystem or evaluation that others use: a versioned interoperability matrix, a minimized protocol failure, an honest SLA model, a policy with quantified limits, or an integration that improves an actual operator/customer outcome. Handle an unseen traffic/schema/fault change after AI-assisted development to demonstrate independent understanding. A standards paper, certificate, generated xApp or green simulator run alone does not prove deployment competence.

## Remaining gaps and access limits

- No current operator hiring census, salary analysis or customer interviews were performed. The role sample is narrow and location-sensitive.
- Operator benefits are operator-reported. Independent cost/energy/reliability results and private-network renewals/operating economics would strengthen commercial conclusions.
- A Teesport award notice was discovered but could not be opened/verified, so no award amount is used. Programme funding and AT&T commitments are labelled as such rather than spent software budgets.
- Some 3GPP pages returned 403; the release portal/indexed primary text and ITU material were usable. Detailed timeline claims should be rechecked against accessible decision records before a final high-precision timeline graphic.
- A DoT CNPN search initially returned a preproduction portal. The main authorisation portal/FAQs were subsequently found; use those, not the preproduction page, for source context. No deployment-specific legal conclusion is offered.
- Live code repositories can contain changes or timestamps after the cutoff. UERANSIM's future copyright line was explicitly flagged; any implementation must pin an audited pre-cutoff version. No code/data was downloaded or executed.
- Current testbed access, fees, spectrum/device permissions, grant eligibility and open academic positions require separate verification before engagement. The source list does not authorise outreach, scanning, RF use or operational changes.
