# Domain institutions, public research access and contribution routes — round 2

Checked 19 October 2026. This is a bounded institutions/access pass covering payments; education; legal/public administration; media/games; geospatial/space; XR; quantum; and nuclear/fusion software. It leaves `taxonomy-draft.json` unchanged. Existing specialist workers own AI/ML, robotics, bio, security, mature computing and energy technical assessment.

The useful discovery is not a list of famous laboratories. Several organisations expose a real technical boundary a developer can study or improve: Stripe's payment events; CMU's learner transactions; LegalBench's task definitions; OpenTimelineIO's editorial interchange; openEO's geospatial process graphs; Monado's XR runtime; TKET's compilation passes; OpenMC's reviewed numerical software; UKAEA's research-data and systems-code interfaces. Access to source is distinct from access to paid work, datasets, hardware, a lab or an institution's employees.

## Evidence and contact conventions

“Opened” means the official page/repository was retrieved directly during this pass. “Indexed primary” means the primary page was available in search text, with limits noted. “Proposed” means a learning/contribution experiment that has not been executed. No downloads, installs, account creation, applications, messages, pull requests, purchases, datasets or physical operations occurred. Contact entries are official professional channels only. A directory listing neither promises access nor implies a person welcomes unsolicited requests.

Source-page publication dates are recorded where visible; a crawler's relative date is not used as the publication date. Project main branches and vacancies drift. Recheck the relevant tag, contribution policy, licence and vacancy before later action. Public code is not evidence of production deployment or software-job growth.

## Finance/payments

### DI-F01 — Stripe: payment integration and regional reliability

**Technical relevance/status:** Stripe's official webhook documentation specifies duplicate delivery, retries and out-of-order events, so the developer problem is financial state reconciliation under unreliable delivery. The Python SDK is public. A directly opened Bangalore Staff Core Infrastructure role describes traffic replay, synthetic checks, failover drills and service dependency validation. It requires 12+ years and a BS/MS or equivalent field; the page's general office policy is at least 50% in-office, with possible stricter team rules. This is one current senior requirement example, not an accessible-entry or demand estimate. [Webhook semantics](https://docs.stripe.com/webhooks), [SDK](https://github.com/stripe/stripe-python), [staff role](https://stripe.com/careers/listing/staff-engineer-core-infrastructure/8070949).

**Entry/contribution/contact:** study the documented API contract and build a local fake financial workflow first. The SDK links developer Discord. GitHub renders “Only collaborators can create PRs”, but the directly opened contribution policy explicitly welcomes external PRs, requires a CLA and usually an associated issue, and warns that generated-code changes may require its private generator. These surfaces conflict; do not infer a settled access restriction from the banner alone. Official careers/emerging-talent routes exist, without implying the reader fits them. [Contribution policy](https://github.com/stripe/stripe-python/blob/master/CONTRIBUTING.md), [early careers](https://stripe.com/careers/emerging-talent).

**Proposed proof:** 30 days: local event consumer with duplicate/out-of-order fixtures and ledger invariants. 90 days: regional-failure/reconciliation harness with a simple baseline, matched workload, accepted outcomes, zero duplicated committed effects in the tested suite, recovery time and review burden. No real funds or live account needed for the initial proof. Payment-state knowledge and distributed systems transfer beyond Stripe; staff-level leadership additionally needs sustained production ownership.

### DI-F02 — BIS Innovation Hub / Nexus Global Payments: interoperability and settlement research

**Technical relevance/status:** BIS's 29 January 2026 FuSSE report explores microservice settlement and cryptographic agility. BIS explicitly calls it an experimental proof of concept, not production components, a compliance assertion or an implementation/performance benchmark. Nexus's operator documentation concerns payment operators, banks, PSPs and FX providers. Its API journey says users use their existing PSP; there is no direct consumer Nexus app. [FuSSE primary report](https://www.bis.org/publications/project-fusse-exploring-flexible-scalable-and-secure-settlement-engines), [Nexus guides](https://nexusglobalpayments.org/nexus-technical-guides/), [API journey](https://docs.nexusglobalpayments.org/payment-setup/steps-1-2-country-currency-and-amount).

**Access/barriers/contact:** Nexus Global Payments is the implementation organisation; BIS is a research origin rather than its owner. A still-rendered job page has an already-passed 31 August 2026 application deadline and discusses targeted late-2027 go-live. That page cannot establish a current vacancy or live network. Entry is more plausibly through a participating payment operator or technology supplier than joining the network as an individual developer. [Handover](https://nexusglobalpayments.org/project-nexus-partners-incorporate-nexus-global-payments-to-run-the-cross-border-payment-scheme-search-for-technical-operator-commenced/), [dated job/context page](https://nexusglobalpayments.org/jobs/business-development-executive/), [official enquiry form](https://nexusglobalpayments.org/contact-us/).

**Proposed proof:** 30 days: model ISO-20022-style message lifecycle and a fake PSP–FX–settlement flow from public specifications; document what the model omits. 90 days: schema/version migration, timeout/duplicate failure, audit and reconciliation tests with resource accounting. Seek no live connection during this research. This would demonstrate relevant engineering, not eligibility to operate payment infrastructure. Missing: full implementation status, contributor policy and actual junior/intermediate technical supplier vacancies.

## Education and learning science

### DI-E01 — Carnegie Mellon DataShop / LearnLab / HCII

**Technical relevance/status:** CMU's official DataShop page exposes longitudinal student/software transaction data and learning-curve analysis, with contributions from LearnLab, ASSISTments and the Open Learning Initiative. The page's totals are a historical website snapshot, not newly measured 2026 coverage. Public datasets require an account; private datasets require provider permission. The main DataShop help URL returned 403 during direct retrieval. [Official DataShop description](https://www.cmu.edu/datalab/tools/datashop.html), [primary API specification](https://pslcdatashop.web.cmu.edu/api/DataShop%20Public%20API-v0.41.pdf).

**People/papers/contact:** CMU's institutional page identifies John C. Stamper as an HCII associate professor and DataShop technical director and links his newer website; confirm current detail before approaching. Stamper et al.'s *PSLC DataShop: A Data Analysis Service for the Learning Science Community* is an identifiable 2010 methods starting point, not current evidence of tutor effectiveness. Use the official DataLab contact page/group channel. [Institutional profile](https://www.cs.cmu.edu/~jstamper/), [methods paper](https://pact.cs.cmu.edu/pubs/Stamper%2C%20J.%2C%20Koedinger%2C%20K.R.%2C%20Baker%2C%20R.%2C%20Skogshol%2C%20A.%2C%20Leber%2C%20B.%2C%20Rankin%2C%20J.%2C%20Demi%2C%20S.%202010.pdf), [DataLab](https://www.cmu.edu/datalab/about-datalab/index.html).

**Proposed proof:** 30 days: on an authorised public dataset, reproduce a simple learning curve with learner/time-aware splits and uncertainty; distinguish skill labels from ground truth. 90 days: compare a simple knowledge-tracing baseline and a more complex model, test new learners/time periods and explain whether the output changes an instructor decision. Retrospective prediction alone is not proof of improved learning. Academic employment/PhD routes require their actual educational and funding criteria; public data access does not confer a lab place.

## Legal, administrative and public-service systems

### DI-L01 — UK i.AI / GDS: Lex and public-service engineering

**Technical relevance/status:** the official i.AI organisation identifies its GDS/DSIT remit and public projects. Lex's directly opened README says the service is experimental and unsuitable as a production dependency. Its case-law component is temporarily disabled pending a National Archives licence. Thus an attractive legal-AI demo can fail at dependency stability and data rights before model quality. Lex exposes Python/FastAPI/MCP, parsing/indexing, infrastructure and operations material. [Organisation](https://github.com/i-dot-ai), [Lex](https://github.com/i-dot-ai/lex).

**Entry/contact/barriers:** use the organisation's published enquiry channel and Lex's contribution guide/issue tracker; no outreach occurred. The organisation advertises UK city bases, but a generic hiring banner does not establish a particular live role, nationality eligibility or sponsorship. Local setup lists Python, Docker and Azure credentials; those are later execution prerequisites and may carry cost. [Contribution guide](https://github.com/i-dot-ai/lex/blob/main/CONTRIBUTING.md), [official organisation route](https://github.com/i-dot-ai).

**Proposed proof:** 30 days: a small public-legislation change/citation corpus with versioned provenance and withheld queries; do not promise unavailable case-law access. 90 days: compare lexical/hybrid/model-assisted retrieval on citation correctness, applicable-date handling, unsupported claims, permission failures and reviewer time. A narrowly reproducible parser/evaluation/operations fix is a plausible contribution; a production legal-advice service is a different scope.

### DI-L02 — Stanford RegLab / Hazy Research: legal reasoning and public-sector evaluation

**Technical relevance/status:** RegLab describes an interdisciplinary public-agency research/engineering programme; Daniel E. Ho's official profile identifies him as director. LegalBench is an open legal-reasoning task effort with a public task-contribution process. Each underlying dataset retains its own licence; “repository public” does not imply blanket commercial rights. [RegLab](https://reglab.stanford.edu/about/), [Ho profile](https://reglab.stanford.edu/team-members/daniel-ho/), [LegalBench code/data links](https://github.com/HazyResearch/legalbench), [contribution instructions](https://hazyresearch.stanford.edu/legalbench/contribute/).

**Paper/contact/barriers:** Guha et al., *LegalBench: A Collaboratively Built Benchmark for Measuring Legal Reasoning in Large Language Models* (2023), is a primary starting point. Its selected English tasks are not an oracle for current UK/Indian legal advice. RegLab's directly opened “Work With Us” page lists research/data routes and says complete submissions use its general-interest form plus formal postings; it cannot respond to direct inquiries. A visible page does not establish the reader's eligibility, work authorisation or final vacancy status. [Paper](https://arxiv.org/abs/2308.11462), [official submission route](https://reglab.stanford.edu/work-with-us/), [contact](https://reglab.stanford.edu/contact/).

**Proposed proof:** 30 days: reproduce three licensed task types and audit ambiguous labels, outdated law and prompt sensitivity. 90 days: with an authorised domain expert, construct a fresh local-jurisdiction task and distinguish legal outcome, citation grounding and safe abstention. Contributing a well-justified task/reproduction is more attainable than assuming research employment. Benchmark scores alone do not demonstrate legal competence or agency adoption.

## Media, games and production infrastructure

### DI-M01 — Academy Software Foundation / OpenTimelineIO

**Technical relevance/status:** OTIO is an ASWF project for editorial interchange. Its governance explicitly separates contributor, committer and technical steering roles. Contributors may submit documentation/code subject to CLA/DCO and review; sustained useful contributions are a route to nomination rather than an automatic promotion. The official public discussion list is a professional entry channel. [Governance](https://github.com/AcademySoftwareFoundation/OpenTimelineIO/blob/main/GOVERNANCE.md), [ASWF participation](https://www.aswf.io/get-involved/).

**Proposed proof:** 30 days: round-trip a small owned editorial timeline between two supported formats and produce a precise mismatch report for timing, gaps, transitions, metadata and media references. 90 days: improve a bounded adapter/test fixture, compare with a baseline and preserve all unsupported constructs explicitly. A real editor should reproduce the workflow. Contribution acceptance is not guaranteed, and authoring a new adapter no one uses is weaker proof than fixing a maintained interchange failure.

**Barriers/contact:** public code/docs/list access is geographically broad; paid studio work still depends on employer eligibility and pipeline experience. No particular current job or hiring count was established. Follow project review policies and protect employer-owned media/IP. [Project](https://github.com/AcademySoftwareFoundation/OpenTimelineIO), [public list](https://lists.aswf.io/g/otio-discussion).

### DI-M02 — Blender Foundation / Blender Institute / module teams

**Technical relevance/status:** Blender's official developer material exposes module ownership, architecture, task review and a contributor path from bugs/docs/tests to deeper responsibility. Its organisation page identifies Thomas Dinges as an involvement contact and lists development coordinators, but direct open of that page returned 402; names are indexed-primary evidence, not independently confirmed employment records. Prefer the official module directory over cold-contacting a prominent executive. [Organisation](https://developer.blender.org/docs/handbook/organization/), [modules](https://developer.blender.org/docs/handbook/organization/modules/), [contact](https://developer.blender.org/docs/handbook/new_developers/contact/).

**Proposed proof:** 30 days: reproduce one compositor/rendering/asset-pipeline failure with a minimal owned test scene and a meaningful regression oracle. 90 days: resolve a maintained module issue or deliver an accepted, editable production workflow, documenting runtime, correctness and user benefit. Substantive design needs early module alignment; a code submission requires the current contributor agreement and review. [Contribution rules](https://developer.blender.org/docs/handbook/contributing/).

**Barriers:** C/C++ and numerical/graphics depth differ from Python automation/add-on entry; technical-art and testing routes are adjacent alternatives. Remote contribution is not a salaried role. No named-owner response, employment opening or contribution acceptance is assumed.

## Geospatial, Earth observation and space

### DI-G01 — openEO / Copernicus Data Space / University of Münster and client teams

**Technical relevance/status:** the official openEO contact page distinguishes specification/steering questions from provider support and client bugs. It lists Edzer Pebesma at the University of Münster as the institutional contact location, plus Python/R/JS/web-editor issue routes and community calls. This is an actual public software collaboration surface. [Official route](https://openeo.org/contact.html), [Python client issues](https://github.com/Open-EO/openeo-python-client/issues).

**Proposed proof:** 30 days: one small reproducible Sentinel-derived process graph with fixed region/time/collection and explicit cloud/missing-data behaviour; estimate compute/storage before a paid job. 90 days: reproduce on a second backend where supported and a later season/location, test schema/process compatibility and compare output against independent labels. Distinguish a client bug from a service-specific failure; the central specification contact explicitly asks that provider issues use provider support.

**Barriers/contact:** public imagery does not ensure unlimited free processing, labels or commercially usable outputs. Account terms, backend quotas, cloud cost and data licences need explicit checks before execution. Public spec contribution is broader than ESA employee eligibility. [CDSE support](https://helpcenter.dataspace.copernicus.eu/), [openEO developer docs](https://openeo.org/documentation/1.0/developers/).

### DI-G02 — ESA Φ-lab: research-to-application collaboration

**Technical relevance/status:** ESA's official Φ-lab page lists scientific/industrial visiting researchers, co-funded PhDs, research fellowships, internships and graduate routes. It places the lab at ESRIN, Frascati. Its team page identifies Nicolas Longépé as a core-team member; a team listing is not an open collaboration commitment. [About](https://philab.esa.int/about/), [collaboration routes](https://philab.esa.int/jobs-and-collaborations/), [researcher profile](https://philab.esa.int/team/nicolas-longepe/).

**Proposed proof:** 30 days: select one lab research/use-case paper and reproduce a small public-data baseline with spatial/temporal leakage checks. 90 days: prepare an auditable case study addressing one operator decision, with uncertainty, transfer limits and the existing operational alternative. A technically specific contribution/case-study proposal is stronger preparation than a generic “interested in AI for space” message. No proposal is sent here.

**Barriers/contact:** graduate routes target master's graduates; postdoctoral routes imply advanced research training; visits require a suitable proposal and usually institutional/industry context. Staff/trainee nationality and funding eligibility must be checked in the exact call—this pass does not establish that an Indian applicant is eligible. The page's official lab contact route is the appropriate professional directory entry. Upstream satellite hardware/defence work has separate constraints.

## XR, wearables and interaction research

### DI-X01 — Monado / Collabora / Khronos OpenXR community

**Technical relevance/status:** Monado's directly opened developer site describes an open XR runtime, source/contribution links and public discussion channels. Platform/hardware support is uneven: most native hardware drivers are Linux-focused; Windows direct mode has vendor-API constraints. Thus OpenXR standardisation does not make every headset interchangeable. [Runtime and channels](https://monado.freedesktop.org/), [code](https://gitlab.freedesktop.org/monado/monado), [development docs](https://monado.freedesktop.org/developing-with-monado.html).

**Proposed proof:** 30 days: trace a minimal OpenXR application's lifecycle and coordinate spaces; make a reproducible simulated/headless test before buying hardware. 90 days: a bounded runtime, tracking, frame-timing or conformance issue, with predicted latency/error behaviour and a regression case. Use already available or separately approved tools/hardware. No installation or hardware test occurred in this pass.

**Barriers/contact:** graphics APIs, C/C++, transforms, device timing and platform restrictions matter. Public Matrix/IRC/Discord and the contribution file give a community path; they are not a job offer. Validate supported hardware rather than assume a developer's existing computer/headset works. Consumer XR adoption and paid roles remain separate research questions.

### DI-X02 — UCL VECG / Immersive Virtual Environments Laboratory

**Technical relevance/status:** UCL's official current group page connects real-time graphics, geometry, sensors/tracking and human evaluation, with Anthony Steed listed as group head. This illustrates an alternative to pure device APIs: build a technically sound interface and test whether people perform a task better. His own site has newer research posts but a recruitment paragraph referring to 2022/23; that paragraph cannot establish a 2026 opening. [Group](https://www.ucl.ac.uk/engineering/computer-science/research/research-groups-and-centres/virtual-environments-and-computer-graphics-group), [official researcher page](https://wp.cs.ucl.ac.uk/anthonysteed/), [lab team](https://vr.cs.ucl.ac.uk/about/people/).

**Proposed proof:** 30 days: reproduce a small public interaction/networked-VR example and specify latency/interaction hypotheses. 90 days: compare one task against a phone/desktop baseline with a predeclared protocol, errors, time, discomfort/interruptions and accessibility outcomes. Hardware and user-study access/ethics are later gates, not assumptions.

**Barriers/contact:** study and research positions require exact admission/funding/role checks; lab hardware is not automatically public. Use the group's official professional contact directory and advertised positions. An academic contact is a source of relevant work, not a route around admission or work-authorisation requirements.

## Quantum software

### DI-Q01 — Quantinuum / TKET compiler team

**Technical relevance/status:** Quantinuum's public TKET repository exposes C++ compiler source, Python bindings and docs; the compiler guide covers routing and pass composition. Sivarajah, Dilkes, Cowtan, Simmons, Edgington and Duncan's 2020 *t|ket〉* paper is a historical architecture/benchmark starting point, not evidence that current hardware delivers economically useful advantage. Named authors here are paper authors; their present employers and availability were not verified. [Code](https://github.com/Quantinuum/tket), [compiler guide](https://docs.quantinuum.com/tket/user-guide/manual/manual_compiler.html), [paper](https://arxiv.org/abs/2003.10611).

**Proposed proof:** 30 days: understand a tiny set of circuit transforms and reproduce semantic equivalence with a classical simulator. 90 days: compare routing/passes across fixed circuits and device-connectivity assumptions, reporting compile time, depth, two-qubit operations and correctness. Keep sampling/resource costs explicit; better compilation is not proof of quantum application advantage.

**Barriers/contact:** compiler engineering is a narrower entry than inventing quantum algorithms, but it still needs quantum information, complex linear algebra and numerical/software depth. Follow the official repository's issue/support path and current contribution policy; this pass did not verify an open external-contributor policy or a particular live vacancy. Paid device access is unnecessary for the first classical correctness experiment.

### DI-Q02 — IBM Quantum / Qiskit open-source teams

**Technical relevance/status:** IBM's official open-source docs and Qiskit's contribution guide provide maintained code, review and issue-label routes. Documentation has a subtle restriction: unsolicited new pages or large changes are not accepted; a content request must be approved first. Code/API documentation and general guides use different repositories. [Official community](https://quantum.cloud.ibm.com/docs/en/guides/open-source), [SDK contribution guide](https://github.com/Qiskit/qiskit/blob/main/CONTRIBUTING.md), [documentation policy](https://github.com/Qiskit/documentation).

**Proposed proof:** 30 days: reproduce a small existing issue or tutorial/circuit inconsistency and explain the mathematics. 90 days: one bounded SDK/test or approved documentation contribution, with a reproducible failing case, correct fix and no overstated application claims. This is a credible contribution ladder; completing tutorials is not proof of research competence or hiring probability.

**Barriers/contact:** public code and Slack/community participation are broad, while employment, cloud hardware quotas, contributor agreements and employer IP permissions have separate conditions. Use the official contributor/community routes; no messages or agreements were submitted. Formal research roles may still need graduate training and publications. Do not confuse this path with the separate post-quantum cryptographic migration branch.

## Nuclear/fusion software: institutions and access only

### DI-N01 — OpenMC community: numerical scientific software

**Technical relevance/status:** latest stable OpenMC governance directly lists Paul Romano as project lead and Patrick Shriwise, Adam Nelson, Jonathan Shimwell and John Tramm on its technical committee. All contributions use independently reviewed PRs; first-time-contributor issues, public mailing list and Slack are explicit entry surfaces. Romano et al.'s 2015 OpenMC paper provides a historical particle-transport/software starting point. This is an open research code, not a personal reactor-design certification. [Stable governance](https://docs.openmc.org/en/stable/devguide/contributing.html), [primary paper](https://www.sciencedirect.com/science/article/pii/S030645491400379X).

**Proposed proof:** 30 days: understand and reproduce one documented, non-sensitive numerical example or an I/O/testing issue; report uncertainty and reproducibility rather than a reactor claim. 90 days: a bounded regression, documentation, parallel-performance or data-validation improvement with domain review. Distinguish stochastic sampling error from a correctness regression.

**Barriers/contact:** neutron-transport methods require scientific grounding beyond generic Python; code/tooling work may be more attainable than physics-model invention. Hardware, national-lab employment and sensitive data have separate access/export/credential rules not settled here. Use the official developer list, issue labels and workflow; the governance page is the public professional directory, not permission to contact individuals or access institutional systems.

### DI-N02 — UKAEA: PROCESS and Fusion Data Service teams

**Technical relevance/status:** PROCESS is public UKAEA systems/optimisation software, with release/version and numerical-platform caveats. The Fusion Data Service is particularly close to conventional backend work: metadata, provenance, access control and storage interfaces. Its directly opened README explicitly states **pre-production; no deployments yet** and provisional API/model before 0.1.0. It is a contribution/learning route, not observed production demand. [PROCESS](https://github.com/ukaea/PROCESS), [numerical-platform caveat](https://ukaea.github.io/PROCESS/installation/installation/), [FDS](https://github.com/ukaea/fds/).

**Proposed proof:** choose one lane. 30 days: trace a released PROCESS example with residual/sensitivity accounting, or a synthetic FDS metadata/provenance/access scenario. 90 days: improve a small reviewed numerical regression or migration/authorisation test with reproducible cases. Do not silently substitute public “main” results for an official release. No real fusion experiment or scientific discovery claim follows from running a software example.

**Barriers/contact:** PROCESS physics changes need experienced modellers; FDS backend work still needs research-data semantics and domain review. UKAEA careers lists UK locations and separate recruitment/early-career channels; exact role qualification, UK residence, vetting, sponsorship and onsite requirements remain unverified. PROCESS offers a formal contact form and code discussions; FDS asks for an issue before substantial work and private reporting for security problems. [Official careers contact](https://careers.ukaea.uk/contact-us/), [PROCESS professional channel](https://www.ukaea.org/service/process/).

## What this pass disproved or narrowed

1. **Open source is not automatic contributor access:** Qiskit docs require prior approval for new content; Blender/OTIO require agreements and review. Stripe's rendered PR banner initially suggested a restriction, but its opened policy welcomes contributions subject to CLA/issues/private-generator constraints. Keep that discrepancy unresolved instead of converting UI wording into a false blanket ban. A realistic path starts with a reproducible problem and the actual policy.
2. **A public project is not production evidence:** Lex warns against production dependency and disables licensed case law; UKAEA FDS has no deployments; BIS FuSSE explicitly disclaims a production reference. Keep those statuses visible beside the institution name.
3. **A famous lab is not an accessible employer:** ESA training nationality/funding, CMU/Stanford/UCL academic admissions, UKAEA vetting/geography and staff-level Stripe experience must be checked separately. Public paper/code access can still be valuable preparation.
4. **Search freshness is not role freshness:** Nexus's job deadline has passed; a UCL personal-page recruitment paragraph is old despite newer posts elsewhere; CMU's website totals are historical. Do not count them as 2026 opportunities.
5. **Directory names are not endorsement or willingness to engage:** named researchers establish relevance to specific work. Actual current teams, available supervision, lab openings and response likelihood require later evidence.

## Strongest remaining gaps / next distinct questions

- India-specific accessible institutional routes remain thin outside payment operators and selected software roles. Investigate official NCERT/DIKSHA/Bhashini, IIT learning-science/XR/geospatial, IN-SPACe/ISRO supplier/open-data and Indian quantum-programme calls. Verify current eligibility and contribution policies rather than list institutions from reputation.
- For each route, sample actual junior/intermediate engineering requirements and closed/filled status where disclosed. This pass cannot measure demand, salaries or likelihood of entry.
- Read LegalBench task-licence and law-date details, and Lex's disabled-case-law/licence update. Legal data access is a concrete product risk; don't wave it away with generic RAG advice.
- Read current Stripe SDK contribution restrictions, TKET contribution policy, Qiskit content rules and agreement/IP terms before proposing a specific contribution. No agreements were accepted here.
- Add paper-level methods audits for the selected technical learning path, rather than extrapolate historical architecture papers to present benchmarks. Cite old papers as foundations.
- Validate public-data/service account terms, quotas, hardware availability and computation budget before a runnable 30-day plan. No accounts, datasets or paid compute were used for this institutions pass.
- For nuclear/fusion, the energy worker owns technology economics/safety/readiness; this pass only establishes public institutional/code access and its limits.

## Directory schema handoff

`domain-institutions-round2.json` supplies typed `institution`, `team`, `researcher`, `paper`, `code`, `data`, `contact` and `contributionpath` entities linked to stable technical-node IDs. It records relevance, evidence status and primary URLs. Keep technical topics nested in the main taxonomy and attach these as a resource/contribution branch; do not replace the technical hierarchy with a name catalogue. Directory entries are draft and no contact has been made.
