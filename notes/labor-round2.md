# Reachable developer pathways: ordinary employer requirements and adoption-linked evidence

Checked 19 October 2026 using the client date in Asia/Kolkata. This pass reads public sources only. It complements `labor.md`; it does not replace its methods audit or make a personal qualification assessment.

## Main finding

The practical choice is not simply “stay a developer” versus “become an AI researcher.” Current employer requirements show several overlapping routes: conventional product backend; enterprise data/platform engineering; automated quality/reliability; applied AI built on those foundations; and substantially more specialized perception/control research. Ordinary engineering work inside an industrial company can be closer to an existing software skill set than that company's domain-research roles. These are observations from selected postings, not estimates of market size or a claim that any role is reachable for the reader without further evidence.

An immediate career screen should ask **where can the person legally and practically work, which hard credentials apply, which production responsibilities they can already demonstrate, and what switching costs remain**. The answer cannot be inferred from “AI engineer” or from interest in a field. Exact experience, education, geography preferences, runway and current independent proficiency remain unknown.

## Declared small sampling frame

The machine-readable companion is [job-requirements.json](job-requirements.json). It contains **15 visible employer role pages from 11 employers**, deliberately selected for variation across India, UK and country-restricted remote work. Employer types include software products/banking, technology services, industrial software centers and suppliers, plus one frontier-lab comparator. Role families cover backend, data, DevOps, testing, graduate engineering, applied AI, evaluation and robotics/control.

Selection used official employer sites or their linked ATS pages, readable English requirements, and an available Apply/Interested channel. The pass favored bounded/intermediate requirements where found, included specialized barriers for comparison, and counted no more than two roles per employer. This is a **purposive requirement audit**: it is not statistically representative, geographically exhaustive, a count of funded vacancies, or a source of hiring odds. Large-employer, English-language and search-index selection bias are substantial. SMEs, informal hiring, non-English recruiting, public-sector hiring and many services employers are undercovered.

Only **four records have an explicit employer publication date**, and only **four disclose salary**. The remaining fields are missing, not zero. A crawler timestamp is not a posting date. A visible application page does not establish active headcount, a new vacancy, a completed hire or continued availability tomorrow. Evergreen roles are marked. Employer categories and role-family tags are analyst classifications, not official occupational statistics.

Two Bosch pages clearly name an Indian legal entity but the readable role text does not expose a job city or work mode. Those fields remain unverified; the existence of an India software center must not be silently converted into Bengaluru onsite or India-wide remote eligibility.

## The requirement matrix

Each linked role is also its official public recruiting channel. No application, message, personal-contact collection or outreach occurred. Team/organization context comes from the role's own description, rather than inferred current employees or scraped personal profiles. Salary ranges below are those of these specific roles and are not comparable measures of total compensation.

| ID | Official role / employer type | Concrete requirements and work | Access and freshness |
|---|---|---|---|
| J01 | [Accenture Custom Software Engineer](https://www.accenture.com/in-en/careers/jobdetails?id=ATCI-5351608-S1950118_en), services | Python, APIs, deployment, GenAI integration, experiments; 15 years full-time education | Bengaluru office location; attendance policy/pay/date unstated. Header says 2–5 years, minimum field 3, additional text 6; do not resolve this contradiction by assumption. |
| J02 | [Bosch Sr.Data Engineering](https://jobs.smartrecruiters.com/boschgroup/744000152321998), industrial software center | 6–8 relevant years; Python/PySpark, SQL, Azure Databricks/ADF, ETL, CI/CD, OpenShift/Helm, monitoring; qualifications list BE/MCA/MTech | India legal entity; actual location/work mode unverified. No pay/date. |
| J03 | [Bosch AI/ML enhanced control research](https://jobs.smartrecruiters.com/BoschGroup/744000154399049-research-engineer-ai-ml-enhanced-control-engineering), industrial research | 3+ experience; MS/MTech/PhD with selective institute wording; Lyapunov, optimal/adaptive/robust control, ODEs, ML, Python, MATLAB/Simulink | Location/work mode unverified; no pay/date. C/C++ preferred, not its core mathematical prerequisite. |
| J04 | [Hitachi Energy DevOps IDC](https://careers.hitachi.com/r-d-engineer-devops-idc/job/R0142094), industrial supplier | Engineering bachelor; 5–10 years; CI/CD, Azure DevOps/Git/Jenkins, operating systems, scripting, installation/deployment automation | Bengaluru onsite; posted **16 Oct 2026**. Pay/sponsorship unstated. |
| J05 | [Hitachi Energy Test Automation IDC](https://careers.hitachi.com/test-automation-engineer-idc/job/R0142411), industrial supplier | Relevant bachelor; 5–8 automation years; Playwright JS/TS, API automation, test design, SQL/Postgres, delivery tooling | Bengaluru onsite; posted **8 Oct 2026**. Pay/sponsorship unstated. |
| J06 | [Monzo Backend Engineer III](https://job-boards.greenhouse.io/monzo/jobs/6635595), banking product | Product backend, typed languages, distributed/resilient systems, customer judgment; company explicitly supports learning its stack rather than requiring prior knowledge of each listed technology | UK remote/ad hoc London; relocation and sponsorship possible. **£85k–£110k base**. Evergreen, no date. No-degree employer policy separately verified in its [staff engineering posting](https://job-boards.greenhouse.io/monzo/jobs/6636147). |
| J07 | [Cognizant Data Engineer](https://careers.cognizant.com/global-en/jobs/00069319943/data-engineer/), services | 4+ years ADF; SQL optimization, Azure data services, quality/error handling, CI/CD, end-to-end delivery and mentoring | London hybrid 2–3 days; **no sponsorship**. Posted **22 Sep 2026**. Degree/pay unstated. |
| J08 | [Capgemini AI Data Engineer](https://careers.capgemini.com/job/London-AI-Data-Engineer/1387989133/), services | Production data engineering, Python/SQL, distributed processing, data modeling and cloud; explicitly does not require all AI-specific experience already | UK multi-city hybrid; posting states SC/DV eligibility and a five-year continuous UK residence filter for SC. Posted **18 Oct 2026**. Numeric years/degree/pay unstated. These are this employer's filters, not general legal advice. |
| J09 | [NatWest Graduate Engineering](https://jobs.natwestgroup.com/jobs/18280482-graduate-trainee-engineering), banking | 2:1 STEM degree completed/in progress, communication, data/statistics, curiosity and learning; 12-month programme | Bristol hybrid; **£42k starting salary**. Date not exposed. Graduate eligibility/sponsorship must be checked in [official early-talent support](https://jobs.natwestgroup.com/pages/early-talent-application-support). Metadata says Experienced despite graduate content; flag retained. |
| J10 | [NatWest Boxed SDET](https://jobs.natwestgroup.com/jobs/18352728-sdet-front-end), banking product | ReactNative/frontend and backend automation, BDD, continuous deployment, performance/security testing, distributed microservices | London mostly remote; **£75,520–£113,280** salary range. Numeric years/degree/sponsorship/date unstated. Decorative team-stack logos are not coded as required skills. |
| J11 | [GitLab Intermediate Backend, India](https://job-boards.greenhouse.io/gitlab/jobs/8775507002), software product | Production backend fundamentals, APIs/jobs, migrations/indexes, tests, performance, feature ownership, validating AI-generated code, async communication | Bangalore label and India location question; role says remote-first. Numeric years/degree/pay/date unstated. Form asks for open-source project/contribution links. |
| J12 | [GitLab Python Agent Foundations](https://job-boards.greenhouse.io/gitlab/jobs/8704363002), software product | Intermediate; production Python, APIs, async/data models, LLM framework or AI backend/harness, evaluations, on-call | Remote Canada/Poland/UK; **India is not in this role's eligibility list**. Numeric years/degree/pay/date unstated. |
| J13 | [Atlassian Responsible AI MLE](https://www.atlassian.com/company/careers/details/27643), software product | Senior, 7+ production-ML years and relevant bachelor/master; safety models, adversarial evaluations, precision/recall, low-latency serving, audit controls | Remote **within India**. Pay/date unstated. This is a depth reference, not a general entry-level bar. |
| J14 | [Aeva Senior Perception](https://jobs.lever.co/aeva/142f731c-7de5-4978-8d64-33e1132f5570), autonomy supplier | 3+ real-time perception years plus MS/PhD; C++/Linux, geometry, tracking, Kalman/Bayesian estimation, fusion, optimized tested production code | Bangalore onsite; no pay/date. ROS2 is preferred, not a substitute for the required perception knowledge. |
| J15 | [Anthropic London FDE](https://job-boards.greenhouse.io/anthropic/jobs/5423029008), frontier comparator | Production agents/evaluations, Python, enterprise workflows and customer discovery; degree or equivalent | **£225k–£255k**, hybrid and 25–50% travel; sponsorship possible. Body says 4+ years, form asks 8+. Date unstated. Exceptional comparator, not ordinary pay or an assessed near-term fit. |

## Freshness failures retained rather than hidden

Three candidate results looked relevant in search but were not counted in the visible-role sample. [Siemens Healthineers P-100654](https://careers.siemens-healthineers.com/fr/fr/job/P-100654/PLEASE-ADD-LOCALISED-TITLE) was indexed as an 8 October C#/C++ scanner-software job, but the live page says filled. [Accenture ATCI-5500614](https://www.accenture.com/in-en/careers/jobdetails?id=ATCI-5500614-S2005727_en) redirected to general search. [Walmart R-2458592](https://careers.walmart.com/us/en/jobs/R-2458592) returned job-not-found. These observations do not tell us whether a hire occurred, whether a role was withdrawn or whether a site changed its identifiers.

The Monzo staff backend role was visible but excluded from the count to prefer Engineer III and avoid another senior-product anecdote. Its explicit engineering no-degree policy is a separate supporting source. Requirement contradictions at Accenture, NatWest and Anthropic also show that job text needs interpretation and verification; it is not a clean measurement instrument.

## Competing pathways and their opportunity costs

### 1. Preserve backend/data competence and add domain ownership

**Conditional fit:** strongest if existing work already demonstrates production services, databases and debugging. J02/J04/J06/J07/J10/J11 show durable engineering tasks in ordinary organizations. Their existence does not establish a growth rate or relative number of openings.

**Learn/build/test:** build a bounded operational service plus an incremental data pipeline: transactions, idempotency, schema evolution, retries, authentication, deletion and provenance. Inject duplicates, out-of-order updates, outages and permission failures; show correct recovery and measured service objectives. Write one design trade-off and one incident report. These are more transferable than memorizing every vendor logo.

**Entry route:** pursue a product/backend, data/platform or quality responsibility that matches demonstrated skills and geography; an industrial supplier's software team can provide domain exposure without first becoming a control theorist. A contribution to an existing maintained project is another inspectable route.

**Opportunity cost:** vendor-specific enterprise demand can reward Azure/ADF/OpenShift depth but narrow portability if fundamentals remain weak. Conventional work is still exposed to AI-assisted implementation; the advantage being developed is reliable independent ownership. More cloud certifications are not a substitute for diagnosing a failed pipeline. A listed certification should be verified for current availability before paying for it; the Cognizant page still names DP-203, which this pass has not independently validated.

### 2. Add applied AI to an existing engineering base

**Conditional fit:** attractive if the user enjoys model behavior and real workflows and can demonstrate software fundamentals. J01/J08/J12 show this route beyond frontier employers; J08 explicitly treats AI-specific details as learnable on top of production-data competence.

**Learn/build/test:** put a model into the operational service with a genuine deterministic/manual baseline. Measure task completion, consequential errors, manual intervention, cost, latency and recovery on held-out cases. Separate a model that proposes an action from the component authorized to execute it. Show why retrieval, fine-tuning, a deterministic rule or no AI was chosen.

**Entry route:** an existing backend/data role with scoped AI delivery, an intermediate agent-platform role where eligible, or a services engagement with a clearly defined outcome. Public applications remain future actions; no contacts were made.

**Opportunity cost:** concentrating only on frameworks and model-release demos can leave weak statistics, systems and customer reasoning. Customer-facing FDE work may require discovery, ambiguity, travel and selling the value of a solution; it is not interchangeable with uninterrupted research time. Frontier compensation should not anchor expected returns from learning these skills.

### 3. Move from quality/reliability into evaluation/security deliberately

**Conditional fit:** J05/J10 demonstrate a conventional testing path; J13 demonstrates a more specialized AI safety path. Their shared testing vocabulary does not make the responsibilities identical.

**Learn/build/test:** start with API/contract/performance/security tests and failure analysis, then add experimental design, sampling/leakage, grader calibration, adversarial inputs, authorization and model-drift analysis. Construct cases where a plausible model answer creates a forbidden effect; directly assert the effect did not occur. Independent human assessment and infrastructure-failure accounting are needed for credible model comparisons.

**Entry route:** improve a release gate, evaluation suite or production incident workflow in an existing team. Publish or contribute reproducible synthetic failures and fixes only where doing so is authorized. A senior Responsible AI role can be a later destination, not the required first job.

**Opportunity cost:** a pure checklist of prompt attacks ages quickly. Strong statistical and security foundations take sustained study; a passing suite is not proof of universal safety. Conventional UI automation alone does not demonstrate model-risk, ML or authorization expertise. Safety leadership requires both technical evidence and product/accountability decisions.

### 4. Separate robotics integration from perception/control research

**Conditional fit:** domain interest and willingness to work with real hardware, mathematical prerequisites, location and access matter. J03/J14 have clear mathematical/graduate-degree filters; ordinary DevOps/testing work at an industrial supplier offers a different entry surface.

**Learn/build/test:** assess C++/Linux, geometry, estimation and control separately. Build replayable simulation tests with sensor timing/dropouts and environmental variation; benchmark localization, interventions and completion against simple baselines. For a deeper perception route, demonstrate estimation/fusion/tracking rather than only ROS packaging. Physical deployment requires supervised access, calibration and operating-envelope evidence; a simulation cannot establish field reliability.

**Entry route:** software integration, tooling, data/replay, testing or deployment can be less discontinuous than a research reset. Where a target research role has a hard graduate-degree filter, independently verify it across several employers and weigh formal study against a directly relevant engineering route. Do not infer all robotics requires a PhD or that a short course replaces one.

**Opportunity cost:** physical access, onsite requirements, slower validation, hardware costs and deeper math can displace time spent building on an existing commercial advantage. Specialized research may also impose credential/institution filters. Neither physical-world work nor research titles provide immunity from automation or business cycles.

### Leadership test shared by all routes

Evidence of leadership by 2031 should mean that multiple systems or teams benefit from the person's decisions: reliable delivery, sound automation boundaries, adoption by others, mentoring, useful technical writing and durable incident learning. It should not mean merely using many tools, listing five years elapsed or accumulating project count. No exact timetable is justified without the person's baseline, available time, constraints and independent feedback.

## Beyond vacancies: adoption-linked evidence and genuine disagreement

### A newer Danish result changes the balance of the evidence

Danmarks Nationalbank WP223, **16 September 2026**, reports that firms adopting AI in 2023 had **11% lower employment growth relative to non-adopters by late 2025**, concentrated in smaller firms and reduced recruitment. This is **not an 11% count of workers fired**. Its accompanying institutional analysis says both groups' employment grew and interprets the gap relative to projected pretrends. [Working-paper landing page](https://www.nationalbanken.dk/en/news-and-knowledge/publications-and-speeches/working-paper/2026/ai-adoption-and-firm-size-employment-effects-in-monthly-administrative-data)

The analysis describes comparisons within narrow industry/size groups and deviations from each firm's pre-adoption trend. Adoption is nonrandom, so identification still depends on counterfactual trends and absence of differential concurrent shocks. **The full working-paper PDF, sample size, exact confidence-interval endpoints and sensitivity specifications were not recovered in this bounded pass**; the result is primary institutional reporting, not a completed independent methods audit. [Institutional analysis](https://www.nationalbanken.dk/en/news-and-knowledge/publications-and-speeches/analysis/2026/artificial-intelligence-and-the-labour-market-the-transition-has-begun)

This should sit alongside the earlier Humlum/Vestergaard null through December 2024 and the US Stanford exposure-by-age signal, not be omitted to preserve a simple narrative. Country, sample, adoption definition, period, employer size, outcome and counterfactual differ. A real unresolved disagreement may remain after accounting for these differences.

### Europe-wide cross-sectional evidence points in another direction

ECB economists' **4 March 2026** SAFE analysis uses a cross-section of about **5,300 euro-area firms** (headline rounded to 5,000, corrected from an initial 3,500), with investment information in Q2 and use in Q4 2025. Overall use has no significant hiring difference; intensive use and investment have positive associations with additional hiring, while cost-cutting use has negative associations. Its reported approximately **4%** hiring advantage concerns the marginal probability of workforce increase, **not 4% more workers**. Controls include firm size/age, turnover, profitability, investment, outlook, sector and country. [ECB primary analysis](https://www.ecb.europa.eu/press/blog/date/2026/html/ecb.blog20260304~d9e34fc95f.en.html)

Cross-sectional selection into AI use and profitable growth remains an alternative explanation; a survey cannot reveal what occupations were actually hired. This cannot invalidate a Danish adoption-cohort event study through a different period, nor does the Danish study prove Europe-wide job destruction. Treat differing results as a reason to audit estimands and data, rather than select the preferred sign.

### Executive expectations are another measurement category

**Firm Data on AI**, NBER WP34836, revised **March 2026**, surveys nearly **6,000 executives across US/UK/Germany/Australia**. Current revised reporting says **69%** use AI; **nine in ten** report no own-firm employment/productivity effect over the preceding three years. Executives expect employment −0.7% in the next three years; employees expect +0.5%. These are reported experiences and expectations, not administrative outcomes or causal estimates. Earlier February material said over 80% no effect; do not merge versions. [NBER primary record](https://www.nber.org/papers/w34836?utmCampaign=ApolloAcademy&utmMedium=AATraffic&utmSource=ApolloAcademy)

Firm adoption rates such as 69% or 20% cannot be compared without question wording, sampling and weighting. The Federal Reserve's **3 April 2026** methods note explains why US estimates span **18% of firms**, **41% of individuals using GenAI for work**, and **78% employment-weighted firms using AI**. These denominators describe different things; none means 78% of work automated. [Federal Reserve measurement audit](https://www.federalreserve.gov/econres/notes/feds-notes/monitoring-ai-adoption-in-the-u-s-economy-20260403.html)

## Practical use and remaining limits

Use the JSON as an eligibility and learning-evidence map, not a recommendation to apply to all 15 roles. First eliminate hard location/credential mismatches, explicitly separate absent requirements from no requirements, and select a small number of role families that fit demonstrated responsibilities and preferences. Compare the incremental effort to become credible in each branch; no exact years-to-mastery are inferred.

The most valuable next labor-market evidence would be India-specific longitudinal hiring with actual employer adoption, consistent job-requisition snapshots over time, and interviews or disclosed hiring outcomes that separate evergreen ads from funded starts. Such contact or private-data collection would require separate user authorization. This pass supports concrete skill-path hypotheses and identifies evidence that could disprove them; it cannot choose a statistically optimal career or forecast the number of jobs available to one person in 2031.
