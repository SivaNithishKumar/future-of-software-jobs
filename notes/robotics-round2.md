# Robotics round 2: attempt to disprove the career opportunity

Audited on 19 October 2026. This pass tests whether deployed robots imply attractive, accessible software work. It supplements `robotics.md` rather than repeating its release survey. Figures are company/operator disclosures unless identified as audited filings or independently derived arithmetic. No packages, models, datasets or software were installed; no private systems were accessed; no outreach occurred.

## Finding

There is paid engineering work around physical automation, but robot deployment is a poor standalone indicator of accessible jobs or a profitable software business. The stronger opportunity is a specific operational bottleneck with a buyer, usable data, integration access and a measurable improvement over existing automation. A generic robot dashboard, a model API wrapper or a learned policy demo faces established substitutes. Some of the work created by robot adoption is local maintenance, commissioning, field operations and customer support; it does not all become remote software engineering.

## Audited economics and labor denominators

### Mature warehouse automation: real revenue, real support burden

Symbotic's FY2025 10-K reports $98.452 million operation-services revenue against $105.304 million cost: a **derived gross margin of -6.96%**. It explains this category includes training, managed/on-site services and spare parts, with costs primarily labor and parts. Some site contracts were loss-making. Walmart accounted for approximately 85% of total revenue. These facts show commercial automation without proving a diversified SaaS-like market. [FY2025 10-K, definitions on printed p.50, financials p.51, service explanation p.53, concentration p.19](https://ir.symbotic.com/static-files/8d44e050-9519-4347-aa51-fc51e49c4a87)

The current counterweight is important: Q3 FY2026 reported $720.838 million revenue and $32.895 million GAAP operating income. Operation-services revenue/cost improved to $37.121/$32.835 million, **derived 11.55% gross margin**. Software maintenance/support was $12.765 million revenue against $3.486 million cost: **72.69% gross margin, but only 1.77% of total revenue**. Nine-month revenue grew 24.49% while R&D expense fell 8.54%. These are accounting categories, not a measure of software headcount, so neither universal unprofitability nor proportional engineering hiring follows. [Q3 FY2026 release, 4 August 2026](https://ir.symbotic.com/news-releases/news-release-details/symbotic-reports-third-quarter-fiscal-year-2026-results)

Its May 2026 operating release reports 22,000 mobile robots, over 200 million miles and 2.23 billion inbound/outbound cases processed during 2025. **Do not divide annual revenue or total system costs by that fleet count to invent per-robot economics:** the stock/time basis, system components, deployment revenue and service coverage do not match. Useful missing denominators are accepted cases per scheduled system-hour, exception labor, downtime and customer total cost. [Operating milestone release, 12 May 2026](https://www.symbotic.com/news/symbotic-announces-2025-milestones-processing-over-2-billion-cases-as-demand-for-physical-ai-accelerates/)

### Industrial robot suppliers: adoption can coexist with layoffs

Teradyne's FY2025 10-K reports a $99.4 million Robotics loss before income taxes and equity in affiliate earnings, versus $77.6 million in 2024. It reports Robotics restructuring affecting approximately 400 employees and reduced Robotics engineering/development spending. The latest Q2 FY2026 release reports $100 million Robotics revenue, showing a recovery rather than a one-direction collapse. **Career inference:** secular robot growth does not remove supplier cyclicality or guarantee growth in every engineering team. [FY2025 10-K, printed p.30 and p.69](https://investors.teradyne.com/sec-filings/all-sec-filings/content/0001193125-26-059002/0001193125-26-059002.pdf), [Q2 FY2026 release, 28 July 2026](https://investors.teradyne.com/news-events/press-releases/detail/445/teradyne-reports-second-quarter-2026-results)

Amazon says its Shreveport generation of fulfillment center requires **30% more employees in reliability, maintenance and engineering roles**. This is an operator statement about a combined role category at a particular center type; it supplies neither net jobs across all roles nor the software-engineer fraction. It therefore supports local technical work while leaving the total employment effect unresolved. [Amazon, 30 June 2025](https://www.aboutamazon.com/news/operations/amazon-million-robots-ai-foundation-model)

### AV operations: the important denominator is deliberately unavailable

Waymo's 17 February 2026 response to a senator reports about 70 remote-assistance agents on duty globally, roughly half in the Philippines, alongside 400,000 weekly trips and over four million autonomous miles. It says these agents advise rather than directly steer, and represent a small portion of total fleet-support staff. It withholds granular invocation rates and related operational information as confidential. **Derived capacity measure:** 70 × 168 hours / 400,000 trips is 1.764 minutes of staffed RA capacity per trip. This is not handling time, intervention frequency or total human labor per trip. [Original company responses, Waymo section PDF pp.30–38](https://www.markey.senate.gov/imo/media/doc/company_responses_to_rao_letter.pdf)

The senator's investigation reports that none of the seven respondent companies disclosed intervention frequency. Its interpretation of the resulting risks is a policy argument, distinct from the companies' factual answers. **Decisive gap:** without engaged minutes, staffing costs, depot/charging/cleaning/recovery labor and matched completed-trip denominators, public data cannot establish total robotaxi human-labor cost or an audited autonomous profitability ratio. [Investigation report, 31 March 2026](https://www.markey.senate.gov/imo/media/doc/remote_assistance_investigation_report.pdf)

### Agriculture: resource savings may be the value, not removing the driver

A Deere government-sales list-price document dated 5 February 2026 lists a **$30,000 See & Spray Premium 120-foot option** for Hagie STS16, requiring specified boom and plumbing configurations. This is an option's published list price, not a full machine price, dealer transaction price or lifecycle cost. A proper adoption calculation needs compatible equipment, field eligibility, seasonal acres, chemicals saved, subscription terms, maintenance and agronomic outcomes. The paid unit of value can be input savings per eligible acre even while a human remains in the cab. [Primary configuration price book, PDF page index 36 / model section printed p.12](https://www.deere.com/assets/pdfs/region-4/industries/government-and-military-sales/contracts/price-pages/agricultural/SPRAYERS_LESS_PUKs_05FEB2026.pdf)

**Rival explanations to test:** high herbicide prices can improve payback without better AI; large farms amortize hardware over more acres; early adopters may have easier field conditions or unusually high labor/input costs. A broad fleet-level savings percentage cannot be transferred to an Indian smallholding or a different crop without local denominators. These are economic hypotheses, not observed results from this price document.

### Mining: evidence for bounded autonomy predates the foundation-model wave

Rio Tinto's operator page says its autonomous trucks use predefined GPS routes, a supervisory system and central controller. It reports an **estimated 700 additional operating hours and 15% lower costs in 2018** relative to conventional trucks. The age and scope matter: this is historical operator-reported evidence, not a 2026 matched study or proof that adding a VLA caused the savings. It demonstrates a mature structured-operations alternative to general-purpose embodied AI. [Rio Tinto automation description](https://www.riotinto.com/en/mn/about/innovation/automation)

Missing for a current normalized comparison: haul distance, grade, payload, loading queues, empty return time, availability, maintenance allocation, remote-control labor, site communications/civil works and capital charge. A tonne moved is a useful denominator only with comparable routes and material handling conditions. Mine access and operational trust are much larger barriers to an individual developer than an API subscription.

## A cost model that does not hide the remaining people

This is an accounting framework, not a claim that these values have been observed:

`cost per accepted task = (annualized capital OR lease + integration + energy + repair/spares + software/cloud + ALL supervision, remote assistance and onsite labor + downtime/rework losses) / accepted tasks`

`equivalent useful hours = accepted tasks / matched human or existing-machine baseline accepted tasks per hour`

Only compare useful hours after matching task complexity, quality, payload and conditions. Robot clock-hours and human-equivalent output hours differ when task rates differ. Do not add both a capital charge and the lease that already recovers it; do not count a supervisor as free because they sit outside the robot's bill of materials.

**Illustrative sensitivity, entirely assumed inputs:** annual fixed cost $81,000; 4,000 scheduled hours; availability 85%; eligible-work utilization 70%; accepted-output ratio 90%; robot instantaneous accepted-task rate equal to the human baseline; remaining labor 0.125 human-hour per useful hour at $30/hour. This produces 2,142 equivalent useful hours and **$41.57 per equivalent useful hour**, versus $24.00 with perfect availability/utilization/yield. This calculation is about denominator discipline, not an estimate for any named robot.

Public filings above support the importance of labor/service costs but do **not** supply every input necessary to fill this formula. A business whose proposal depends on assuming all those inputs away has not established its case.

## Existing substitutes weaken the generic-platform thesis

Equinor already publishes **Flotilla**, an operator interface for multiple robots/facilities, implemented in React, ASP.NET and MQTT, with an EPL-2.0 license. The repository describes development/staging/production deployments. That is self-reported repository documentation, not an independent uptime audit. [Operator-owned source](https://github.com/equinor/flotilla)

Its **Armada** integration suite describes realistic mission/error testing with a mocked robot, local OIDC authentication, generated MQTT test credentials and public service images. The README says no private tenant secrets are required for its integration-test lane. This is a promising reproducibility starting point; it was inspected, not run here. [Integration-test source](https://github.com/equinor/armada)

A vendor's Northern Lights deployment account reports pre-mapping, an ANYbotics field engineer, integration with Flotilla and hosting within Equinor's cloud tenant. The first Flotilla autonomous mission without local supervision took place within two weeks. There is no published full cost or maintained intervention rate in this account. It illustrates integration and cybersecurity work beyond robot motion, while remaining vendor-published evidence. [Deployment account, 23 June 2025](https://www.anybotics.com/news/equinor-deploys-anymal-at-northern-lights-ccs-facility/)

Traditional application engineering also competes. Universal Robots documents programmable palletizing applications built around fixed product patterns, payload/reach and existing production lines. Its payback claims are promotional, so they should not be treated as a universal price benchmark. The relevant lesson is that a customer may need a simple repeatable cell, not a humanoid or open-ended language reasoning. [Existing application category](https://www.universal-robots.com/industries/logistics/robotic-palletizing/)

**Potential defensibility:** permissioned operational failure data with known labels and distribution; validated integration into an expensive workflow; deployment/recovery expertise; hardware-aware reliability; and customer trust. **Weak defensibility by itself:** a shared JSON schema, another fleet map, a prompt, a public benchmark fine-tune or a hosted-model wrapper. These judgments must be tested against actual alternatives and customer needs.

## Role boundaries and geography filters

This is a field-specific constraint check, not a representative vacancy survey; the labor research track owns broad job-market sampling.

| Track | What must be demonstrated | Accessibility limit |
| --- | --- | --- |
| Platform/runtime/integration | Reliable APIs, middleware, telemetry, timing, failure containment and deployment tooling | Backend skills transfer, but robotic timing/hardware faults must be learned; field access matters |
| Data/evaluation/research engineering | Versioned data, leakage-free splits, training/inference pipelines, calibrated failure detection | Requires statistics/ML and access to model internals/rollouts; a hosted API may hide needed signals |
| Controls/perception | Geometry, calibration, estimation, dynamics, planning and actual hardware behavior | A software portfolio alone is insufficient without math and physical-system practice |
| Frontier research | Original methods, careful experiments, publications or equivalent research record | A different evidence standard from application engineering; some jobs explicitly require doctoral training |
| Field/customer operations | Commissioning, networking, repair, operator training and onsite diagnosis | Creates work but often entails travel and physical/site requirements rather than remote coding |

The ANYbotics Field Deployment Technician vacancy is **United States-based**, advertises remote hiring but up to **80% travel**, with mechanics/electronics/mechatronics or equivalent experience. "Remote" here means a home base between deployments, not a globally remote software role. [Primary vacancy](https://jobs.lever.co/anybotics/21610dea-72a2-4771-8fb9-0d9c00b7b3dd)

A current Deterrence Defense robotics-software posting requires ROS 2 experience shipped on hardware, C++/Python, transforms, planning and onsite commissioning in Austin. It explicitly requires U.S.-person status or eligibility for required authorization. This is a restriction stated by this employer, not a claim that all U.S. robotics roles have the same requirement. [Primary vacancy](https://job-boards.greenhouse.io/deterrencedefenseinc/jobs/4453709009)

Caterpillar's Chennai Autonomy Engineer posting describes robotics software, validation, debugging and safety documentation and requires an accredited relevant degree. **Its listed application period ended 4 October 2026**: it is recent evidence of India-based work, not an opening confirmed available today. [Dated primary posting](https://careers.caterpillar.com/it/lavori/r0000395301/autonomy-engineer/)

No immigration eligibility, sponsorship or the user's citizenship was inferred. Filter any eventual target by actual work location, work authorization, seniority, on-site/travel expectations and access to hardware before treating it as actionable.

## Reproducible papers and materials for the next experiment

Each row distinguishes the scientific paper from code, data and model permissions. No reproduction was executed.

| Material and exact paper version | Practical value and replication requirements | Code/data/license audit |
| --- | --- | --- |
| **SAFE**, Gu et al.; NeurIPS 2025 camera-ready, [arXiv:2506.09937v2](https://arxiv.org/abs/2506.09937v2), revised 30 Oct 2025; DOI `10.48550/arXiv.2506.09937` | Train a small MLP/LSTM on VLA latent features to detect failed rollouts; requires white-box policy features, successful/failed rollouts and held-out calibration/tasks. Paper explicitly leaves cross-embodiment and sim-to-real transfer unresolved. | [Official implementation](https://github.com/vla-safe/SAFE) links adapted policy forks, simulation rollouts and lab-rollout files. No top-level LICENSE was visible in the inspected listing, so reuse permission remains unverified. Benchmark/model dependencies have separate terms. |
| **DROID**, Khazatsky et al.; [arXiv:2403.12945v2](https://arxiv.org/abs/2403.12945v2), revised 22 Apr 2025; DOI `10.48550/arXiv.2403.12945` | In-the-wild demonstrations; useful for data adapters, calibration/quality audits and co-training. Full training is a substantial compute/storage project. The project later supplied improved calibration for a subset, making data revision part of reproducibility. | [Project](https://droid-dataset.github.io/), [policy learning](https://github.com/droid-dataset/droid_policy_learning). README offers a 2GB/100-trajectory sample versus a 1.7TB full processed dataset. Paper states dataset CC BY 4.0; code-platform, policy-learning and checkpoint licenses require separate checks. |
| **SmolVLA**, Shukor et al.; [arXiv:2506.01844v1](https://arxiv.org/abs/2506.01844v1), 2 Jun 2025; DOI `10.48550/arXiv.2506.01844` | Small VLA and asynchronous inference as an affordable learning baseline. Requires a compatible action/state/camera schema; useful action prediction on data does not establish closed-loop task success. | [Model card](https://huggingface.co/lerobot/smolvla_base) declares Apache-2.0 and base-model fine-tuning as intended use; [LeRobot code](https://github.com/huggingface/lerobot). Pin the checkpoint and framework revision before running; source code, assets and dataset terms remain separate. Broader HF ecosystem is owned by the software/AI research track. |

SAFE's published runtime example uses a 2.3-million-parameter LSTM adding 0.73 ms to a policy taking 149 ms; that is a useful feasibility result, not an assurance of the same overhead on another runtime. The paper uses latent-feature access, not a black-box confidence endpoint. A commercial API removing internals changes the available design. [Peer-reviewed methods and limitations](https://proceedings.neurips.cc/paper_files/paper/2025/file/392d0d05e2f514063e6ce6f8b370834c-Paper-Conference.pdf)

## Institution, group and public professional-channel directory

These are research leads, not endorsements, implied personal connections or sent messages. Channels were located on official institutional/group pages. An application page can be more appropriate than direct email; follow the institution's stated route if outreach is later authorized.

| Group / public professional contact | Why relevant to the technical branch | Public channel and barrier |
| --- | --- | --- |
| **IIIT Hyderabad Robotics Research Center; K. Madhava Krishna** | Robot vision, autonomous flight, mobile robotics and vision/language for robotics; a relevant India-based research node | [Institutional faculty page](https://www.iiit.ac.in/faculty/k-madhava-krishna/) lists `mkrishna@iiit.ac.in`; [research program](https://robotics.iiit.ac.in/research/). Research admission/project availability must be verified; this is not a job offer. |
| **TiHAN, IIT Hyderabad; project director Rajalakshmi P** | Autonomous ground/aerial vehicles and testbed work; useful for real sensor/navigation validation and local ecosystem access | [Team](https://tihan.iith.ac.in/team.html); [official contact](https://tihan.iith.ac.in/contact.html) lists `office.tihan@iith.ac.in`. Testbed access and collaboration terms are not public guarantees. |
| **CMU AirLab; Sebastian Scherer, Wenshan Wang** | Field autonomy, visual odometry and difficult-environment navigation; connects portable perception interests to real mobility requirements | [Lab](https://theairlab.org/); [professional contact page](https://theairlab.org/contact/) lists `basti@andrew.cmu.edu` and `wenshanw@andrew.cmu.edu`. [Joining instructions](https://theairlab.org/openings/) route graduate applicants through institute admissions; research staff require a relevant skill record. |
| **ETH Zurich Robotic Systems Lab; Marco Hutter / lab administration** | Legged robots, control and physical-system research; useful for learning the control and hardware boundary behind embodied models | [Lab and official administrative contact](https://rsl.ethz.ch/); [public code organization](https://github.com/leggedrobotics/). Start with published projects and institutional application routes; hardware/Swiss location/admission access is separate. |
| **University of Toronto Robot Vision & Learning; Florian Shkurti, SAFE coauthor Qiao Gu** | Risk estimation, policy evaluation, safe learning and perception/control; directly relevant to the proposed failure-detection experiment | [Faculty profile](https://www.cs.toronto.edu/~florian/) lists `florian@cs.toronto.edu` and 2026–27 recruitment instructions. [SAFE project](https://vla-safe.github.io/) supplies paper/code links. Current degrees/research requirements apply; no availability was presumed. |
| **UT Austin Robot Perception and Learning; Yuke Zhu, RoboCasa-associated authors** | Generalist robot autonomy, benchmark design, perception/action loops and open research software | [Lab](https://ut-austin-rpl.github.io/); [people](https://ut-austin-rpl.github.io/people/) lists `yukez@cs.utexas.edu`; [opportunities](https://ut-austin-rpl.github.io/opportunities/) says prospective graduate students should use admissions and need not contact the PI. Visiting-researcher route is generally six months or longer. |

Company/operator professional channels that connect directly to this pass:

| Organization | Appropriate public research channel | Concrete reason to follow |
| --- | --- | --- |
| **Equinor robotics / Flotilla maintainers** | [Public Flotilla repository](https://github.com/equinor/flotilla) issues and contributor instructions; no issue/PR was opened | Operator-defined integration, industrial tenancy/security, real mission abstractions and existing substitutes for a new platform |
| **ANYbotics field engineering** | [Primary field-engineering vacancy channel](https://jobs.lever.co/anybotics/33498bd9-d81b-415c-bad9-50c936269faf); no application submitted | Deployment requirements, travel and the operational boundary between robot supplier and customer |
| **Symbotic** | [Public investor filings](https://ir.symbotic.com/) and [careers](https://www.symbotic.com/careers/); no inquiries or applications | Distinguish systems sale, software maintenance and labor-heavy operations; follow paid demand by function rather than robot count |

## Revised 30/90-day projects with stronger falsification

### Project 1: operational failure-cost audit, not another fleet dashboard

**30 days, after approval of any needed installs:** inspect a pinned Flotilla/Armada release and reproduce an existing mission/error path. Add a local-only benchmark ledger that records mission acceptance, retries, operator-equivalent handling minutes, stale events, failed recovery and work completed. Use a mocked robot and permission-free test credentials. Start with standard components and demonstrate the new metric on a reproducible injected failure; a simulation-only path must be labeled as such.

**90 days:** compare three bounded policies for the same failed mission: stop-and-escalate; fixed deterministic retry; and model-assisted diagnosis/recovery. Freeze 100 scenario/seed cases covering normal work, sensor staleness, a blocked route, low battery and lost connectivity. Measure accepted missions/hour, false recovery, intervention minutes, recovery latency and total computing/service cost. A model must improve accepted work or reduce intervention cost after its overhead, with a task-stratified uncertainty interval; it cannot win by suppressing escalation or silently dropping failures.

**Kill criteria:** existing upstream telemetry already answers the buyer's question; the useful signal cannot be collected without proprietary access; improvements vanish against deterministic recovery; or a customer cannot act differently on the metric. This project is evidence for platform/integration ability even if it disproves a standalone product.

### Project 2: reproduce a failure detector and test the feature-access assumption

**30 days:** reproduce a small SAFE configuration from published rollouts if terms/access permit, keeping training, threshold calibration and held-out tasks separate. Record exact policy fork/checkpoint, feature layer and preprocessing; compare the learned detector with a simple action-consistency or embedding-distance baseline. Do not substitute a model's prose confidence for measured calibration.

**90 days:** examine a genuinely different task family or visual perturbation, reporting false alarms per rollout, missed failures, warning lead time and cost of interruption as well as ROC-AUC. Test what survives when latent access is removed and only observations/actions remain. This explicitly distinguishes a white-box research route from a black-box commercial API product.

**Kill criteria:** no permitted access to the required features/rollouts; the gain depends on leaked future data or the policy's own success declaration; calibrated thresholds fail under modest changes; or an inexpensive consistency check matches the detector. No claim of physical safety or cross-embodiment generality follows from these experiments.

### Project 3: buyer-denominator worksheet before hardware purchase

**30 days:** choose one bounded physical task and create a fully auditable comparison of manual work, a conventional fixed/programmable solution and a learned/adaptive robot. Use public price/contract evidence only for the exact configurations it supports. Leave unobserved values blank; show sensitivity and break-even surfaces instead of filling gaps with market averages.

**90 days, only with authorized operator access:** collect at least several weeks of matched task/shift logs, including exceptions, staffing, setup and failed attempts. Define the minimum useful improvement before observing outcomes. The output is a buyer decision memo with rejection cases, not a sales demo.

**Kill criteria:** savings exist only at implausible utilization, baseline selection favors the new system, required access is unavailable, regulatory/procurement costs overwhelm the small opportunity, or a simpler fixture/software change yields the same benefit.

## Decisive unresolved evidence

- **Intervention economics:** public companies frequently disclose total operation or fleet activity, not matched operator time per accepted output. Waymo explicitly withheld key rates in the public response. Do not turn missing data into either proof of full autonomy or proof of hidden one-to-one teleoperation.
- **Net employment:** no audited mapping from robot installations to additional software positions was found. Supplier layoffs, expanding field support and growing robot fleets can all occur together.
- **Customer economics:** vendor gross margin is different from customer return; a profitable supplier can sell an unsuitable installation, and an early supplier can lose money while a particular customer benefits.
- **Geography:** remote, hybrid and on-site labels require actual country and travel checks. Research-lab admissions, employment rights and commercial field access are distinct constraints.
- **Procurement access gap:** search surfaced UKAEA preliminary-market-engagement notice `057997-2026` for Spot-based contamination sampling, but both [official notice](https://www.find-tender.service.gov.uk/Notice/057997-2026) and its PDF failed to load. The intermediary's budget/date information was not promoted to verified contract or awarded-revenue evidence.
- **Artifacts/licenses:** a public paper, accessible weights, an open code repository and commercial reuse permission are different facts. SAFE's visible code listing lacked a top-level license; DROID has distinct data/platform/learning components. No assets were downloaded to bypass access or terms gaps.

## Forecast adjustment

By 2031, physical automation is a plausible specialty for a systems-oriented developer, but **integration and reliability are a conditional opportunity, not a guaranteed job refuge**. The best near-term entry is a narrow role or project where existing backend/testing skills meet operational data and physical validation. Direct controls and frontier research demand additional evidence. The entrepreneurial path should survive a conventional-automation comparison, paid-support costs and realistic utilization before consuming hardware capital.
