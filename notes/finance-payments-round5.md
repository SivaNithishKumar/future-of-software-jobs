# Round 5: payment infrastructure, reconciliation, fraud and agentic transactions

Research checked 19 October 2026. Technical/funded-work pass beyond prior authentication-protocol notes. Read-only public evidence; no funds, accounts, trades, private banking data, installations, downloads of datasets/models, contact or applications. This is engineering/career research, not legal, accounting, investment or product-licensing advice for a real business.

## Finding

The strongest accessible direction is **reliable financial data and transaction software**, with statistics/ML where labels and decisions justify it. Actual work includes ledgers, reconciliation, settlement state, refunds/disputes, risk features, model monitoring, audit trails, migration and incident recovery. An AI engineer can enter through backend/platform/data/evaluation competence without becoming a quantitative trader or inventing a new payment network.

Agents add another proposer/interface to this infrastructure. They do not remove accounting, evidence, funds availability, chargeback or reconciliation obligations. Generic matching, dispute drafting and risk scoring already have established providers. A defensible skill is diagnosing the exact unreconciled amount, stale label or failed state transition; a new business additionally needs permitted data, distribution, recurring buyer pain and an advantage over incumbent tools.

## 1. A technical branch map with the actual work

### Ledger and balance semantics

Separate authorization, reservation, captured/posted funds, provider availability, payout initiation, bank receipt and reconciliation. These are related but different states/times. A successful API response is not a complete cash ledger, and a balanced internal journal can still contain the wrong account/recipient or omit an external transaction.

Use a mature transactional database or ledger engine. Represent money with explicit currency and the source's specified unit/precision; never assume every amount is a binary float or every currency has two decimal places. Separate immutable source events, interpreted business operations and accounting postings. Correct history through explicit reversal/adjustment relationships, rather than silently rewriting completed entries. The exact accounting policy belongs to the business/domain owner.

[TigerBeetle's two-phase transfer documentation](https://docs.tigerbeetle.com/coding/two-phase-transfers/) provides a concrete mature comparator: pending funds are reserved, then posted, voided or expired; resolution uses new immutable transfers, and a pending transfer resolves at most once under its defined semantics. Its internal ledger guarantees do not make an unrelated bank/provider effect atomic. Linked internal postings and external settlement require a separate integration/recovery contract.

**Roles/skills:** payments backend, ledger/platform engineering, data integrity, database/state-machine design, tests, observability and recovery. Domain fluency matters more than a new agent framework.

### Reconciliation and close

Reconcile at least three views: commercial orders/invoices, provider transaction/balance records, and bank/cash statements. The natural unit can be one-to-one, a settlement batch, a partial payment, a refund/dispute in another reporting period, fees/reserves or an FX conversion. Matching equal amounts and nearby dates is a baseline, not a universally valid proof.

Mature methods include exact stable IDs, typed normalization, deterministic amount/currency/time constraints, joins, bounded one-to-many matching, graph/assignment optimization and exception queues. Statistical similarity can rank ambiguous candidates; a model explanation should cite source rows and declared transformations. An unmatched amount must remain unmatched/suspense until evidence resolves it. An agent must not invent a fee or write off a difference merely to make totals agree.

[Stripe's current payout report](https://docs.stripe.com/reports/payout-reconciliation) directly illustrates the boundary: automatic payout batches have an itemized reconciliation path; manual/instant payout behavior differs. Report grouping uses estimated arrival, not necessarily actual bank posting time, and report availability can lag. Crucially, report columns explicitly specify **major currency units**, while API objects have their own amount contracts. Normalize from the actual field contract, not a global multiply/divide-by-100 rule.

**Roles/skills:** finance data/backend, integrations, financial operations tooling, exception/recovery workflows, schema/version migration and audit/reporting. A finance degree is not universally a software prerequisite; production-domain review is still needed for real reporting decisions.

### Settlement and interoperability

Payment messaging, clearing and settlement are distinct. A schema-valid pacs.008-style payment, pacs.002-style status or camt.053-style statement does not by itself establish every downstream bank state. Participant implementation guides, status definitions, message versions, cutoffs, duplicate/retry semantics and reconciliation rules matter.

The [Bank of England ISO 20022 handbook](https://www.bankofengland.co.uk/payment-and-settlement/rtgs-renewal-programme/iso-20022-handbook) documents structured data and payment/non-payment migration, including camt.053 statements and upcoming November 2026 address-format handling. Some historical sections still use future tense for Spring 2025. The [30 April 2025 go-live release](https://www.bankofengland.co.uk/news/2025/april/renewed-rtgs-service) confirms RT2 actually went live on 28 April 2025; do not treat it as an unlaunched future system. This is operator implementation context, not an applicability conclusion for a particular product.

**Roles/skills:** integration/protocol engineers, test automation, data migration, participant/vendor readiness and operational resilience. Public specifications permit learning; they do not grant access to a settlement network or participant test environment.

### Disputes, refunds and evidence

A chargeback is not a perfect fraud label. Reasons include unauthorized payment, duplication, non-receipt, canceled subscription and other commercial disagreements. A won/lost dispute is affected by evidence/process, not only underlying malicious intent. [Stripe's reason-code documentation](https://docs.stripe.com/disputes/categories) explicitly describes these categories and recognizes that an unrecognized charge can be a mistaken customer claim as well as genuine fraud.

Evidence assembly is a useful bounded model task: retrieve relevant existing records, map to reason-specific fields, show provenance and highlight missing/contradictory evidence. It must not fabricate delivery logs, alter original records or autonomously decide the truth of a dispute. Track evidence date, submission state, deadline source and final outcome separately. No real evidence submission is part of this research.

### Risk and fraud decision systems

Rules, logistic/linear models and boosted trees are serious baselines; graph or sequence models help only if entity links/history are available and causally valid. Features may include behavior/velocity, account/device relationships and transaction context, but availability, latency, privacy and permitted use constrain them. The engineering problem includes streaming aggregates, online/offline parity, label maturity, versioned decisions and investigation feedback.

Measure precision/recall at a practical review capacity, calibration, delayed outcomes, segment stability, monetary exposure under explicit cost assumptions, and customer/operational friction. A high ROC-AUC can coexist with an overwhelming alert queue. Loss prevented is not simply flagged transaction amount, because recovery, margin, false declines, review time and missed legitimate business differ.

## 2. Label timing, drift and causal evaluation

The [Fraud Detection Handbook's validation chapter](https://fraud-detection-handbook.github.io/fraud-detection-handbook/Chapter_5_ModelValidationAndSelection/ValidationStrategies.html) uses chronological train/delay/test blocks and prequential validation. Recent transactions lack mature labels; stale training can miss drift. Its illustrated one-week delay is an experimental choice, not a universal fraud-label delay.

The historical primary paper [Dal Pozzolo, Boracchi, Caelen, Alippi and Bontempi](https://dalpozz.github.io/static/pdf/TNNLS_2017.pdf), *Credit Card Fraud Detection: A Realistic Modeling and a Novel Learning Strategy*, DOI [10.1109/TNNLS.2017.2736643](https://doi.org/10.1109/TNNLS.2017.2736643), addresses class imbalance, concept drift and verification latency in an industrial data stream. Its private real-world data and old operating context are not a turnkey current reproduction or a 2026 effect estimate.

[Stripe's dispute measurement docs](https://docs.stripe.com/disputes/measuring) distinguish dispute activity by dispute date from cohort dispute rate by charge date. Recent charge cohorts can change as later disputes arrive. A model evaluation must preserve transaction time, decision time, feature availability, label-observation time and final/revised disposition. Do not leak a later dispute, resolution note or post-decision aggregate into a real-time feature.

**Selection/counterfactual problem:** labels from accepted transactions do not automatically reveal what would have happened to declined attempts. Analyst-reviewed cases are also a selected sample. A new policy changes the future data it sees, so a retrospective classifier comparison is not a causal estimate of prevented loss or increased approval revenue. Off-policy methods need credible logged propensities/support and assumptions; they cannot recover unobserved outcomes by assertion. A controlled real-world test requires a separately authorized institutional design. The offline project below claims no causal business lift.

**Distinct targets:** account-opening fraud, unauthorized card use, authorized scam payments, merchant abuse, AML investigation and credit default have different labels and operating decisions. Do not train on a synthetic account-opening benchmark and advertise a universal real-time transaction/AML detector.

## 3. Funded/operator evidence, with the right denominator

### RTGS: an implemented, funded engineering program

The [National Audit Office's December 2025 audit summary](https://www.nao.org.uk/press-releases/bank-of-england-successfully-navigates-complex-modernisation-of-uks-critical-payment-system/) reports a **£431 million** renewal delivered over nine years, with Accenture as main delivery partner, more than 450 program staff at peak, four major replans and around 18 months delay. It describes testing, interdependencies, assurance and continuing enhancement needs. This is substantially stronger evidence of paid infrastructure work than payment transaction volume. The staff count covers the program's roles, not 450 software vacancies; the cost is not a new startup's available budget or a 2031 employment forecast.

### Accounting automation is already an established business

[BlackLine's 10 February 2026 FY2025 release](https://investors.blackline.com/news-releases/news-release-details/blackline-announces-fourth-quarter-and-full-year-2025-financial) reports **$700.4 million GAAP revenue**, 4,394 customers and 105% dollar-based net revenue retention, alongside embedded AI and an acquisition. The release labels results preliminary pending final filing, so this note does not call them independently audited final figures. Revenue is company-wide, not a clean reconciliation-product segment. It demonstrates existing finance-software spend and incumbent distribution; it does not establish an unserved horizontal AI-reconciliation market.

### Native provider functionality is the competitive baseline

Stripe already offers payout/balance reports, risk scores/rules and dispute evidence tooling. Its [June 2026 Radar expansion account](https://stripe.com/blog/expanding-stripe-radar-to-protect-more-of-your-business) describes account-level risk and an evidence library/automated packet assembly. These are product claims, not independent effectiveness or ROI measurements. A new tool must demonstrate a recurring problem beyond what the provider/ERP/finance suite already does—often multi-provider meaning, missing source quality or a special workflow, rather than a nicer explanation of one standard payout.

**Inference:** integration/data-quality/risk engineering is plausible funded work; role counts and a scarce-wage premium remain unmeasured. A software startup still needs rights to representative data and a clear paid decision, not only a large payments ecosystem.

## 4. Agentic commercial transactions: emerging surface, existing obligations

Current [AP2 specification](https://ap2-protocol.org/ap2/specification/) is **v0.2**, with linked Checkout/Payment Mandates and Receipts, human-present and autonomous flows. It requires role validation/processing in deterministic code. Product/catalog/commerce orchestration and determining the user's intended task are outside its complete scope. A valid mandate/evidence chain does not prove fulfillment, inventory accuracy, bookkeeping correctness or that an ambiguous catalog description matched the intended goods.

[Visa Trusted Agent Protocol](https://developer.visa.com/docs/trusted-agent-protocol/trusted-agent-protocol-specifications) addresses merchant recognition of approved commerce agents over existing infrastructure. Agent providers are described as onboarded/certified by payment schemes; public merchant-facing documentation is not a promise that an independent developer can immediately become an approved provider or process live transactions. Product terms are separate from source-code licenses.

The August 2026 primary preprint [*Beyond the Mandate*, arXiv:2608.23858v1](https://arxiv.org/html/2608.23858v1) distinguishes signed artifacts from manipulated pre-signing context. It used an author-built testbed because a complete public AP2 deployment was unavailable. Threat scores and demonstrations are not measured attack prevalence in deployed commerce. This supports testing the **whole commercial lifecycle**, not assuming cryptography alone solves transaction meaning.

**Concrete work:** checkout/version integration, item/price/tax/fee consistency, duplicate purchase suppression, partial fulfillment/refunds, dispute evidence, merchant observability and reconciling mandate/receipt/order/payment/provider/bank views. The new interface may create integration work while native commerce/payment platforms capture most product revenue. This is a forecast to test, not an adoption statistic.

## 5. Papers, code, data and replication requirements

| Resource | Exact study/value | Artifact rights and attainable slice |
|---|---|---|
| [TigerBeetle](https://github.com/tigerbeetle/tigerbeetle), [two-phase docs](https://docs.tigerbeetle.com/coding/two-phase-transfers/) | Mature ledger semantics for reserve/post/void/expiry, immutable effects and balance constraints. Public latest release metadata inspected: 0.17.9, 6 July 2026. | Core repo **Apache-2.0**, verified via public API. Study a local synthetic transfer lifecycle after approved setup; not proof of external settlement finality. A normal transactional database remains a valid simpler comparator. |
| [BAF / Turning the Tables](https://arxiv.org/html/2211.13358v1), NeurIPS 2022, DOI [10.48550/arXiv.2211.13358](https://doi.org/10.48550/arXiv.2211.13358) | Sérgio Jesus, José Pombal, Duarte Alves, André Cruz, Pedro Saleiro, Rita Ribeiro, João Gama, Pedro Bizarro. Synthetic bank-account-opening data with temporal/bias variants. Distinct from payment-ledger or card-transaction data. | [Official repo](https://github.com/feedzai/bank-account-fraud) metadata **NOASSERTION**; LICENSE starts with a commercial-use contact note before Apache text. Do not blanket-label the whole artifact permissive Apache. Public [Kaggle card](https://www.kaggle.com/datasets/sgpjesus/bank-account-fraud-dataset-neurips-2022) returned no readable license text in this pass; dataset terms remain a verification gate. No data downloaded. |
| [Fraud Detection Handbook](https://fraud-detection-handbook.github.io/fraud-detection-handbook/), [repository](https://github.com/Fraud-Detection-Handbook/fraud-detection-handbook) | ULB Machine Learning Group / Worldline collaboration. Useful CPU-scale simulator, feature, review-capacity and delayed-label/prequential baselines. | Inspected README/LICENSE: notebook/code **GPL v3.0**, prose/pictures **CC BY-SA 4.0**. Do not call all artifacts MIT/Apache. Concepts can guide an independently written exercise; copying/distributing code has its own terms. Data artifacts need separate checks. Historical notebooks can require dependency adaptation. |
| [BIS Project Aurora](https://www.bis.org/publications/project-aurora-power-data-technology-and-collaboration-combat-money-laundering-across-institutions-and-borders), 31 May 2023 report | Synthetic cross-border transaction patterns, siloed versus collaborative ML/network analysis and privacy-enhancing methods. | Demonstration on synthetic data, not deployment detection rates. Public report does not establish a fully open licensed dataset/code package or institutional access. Good source for a mechanism/hypothesis; do not claim a real AML model reproduction from the report alone. |
| [AP2 v0.2](https://ap2-protocol.org/ap2/specification/), [official repo](https://github.com/google-agentic-commerce/AP2) | Checkout/payment evidence and deterministic role checks; code samples/demos rather than a complete bank/merchant ecosystem. | Repo **Apache-2.0** verified metadata; README sample setup expects Python >=3.11 and provider credentials for some examples. No sample was run. Protocol and vendor product terms differ; mock commerce is the safe initial slice. |
| [Beyond the Mandate](https://arxiv.org/html/2608.23858v1), 24 August 2026, DOI [10.48550/arXiv.2608.23858](https://doi.org/10.48550/arXiv.2608.23858) | Avital Aviv, Parth A. Gandh, Ron Bitton, Asaf Shabtai; Ben-Gurion/Intuit affiliations. Lifecycle/context analysis on a controlled AP2 testbed. | Paper arXiv non-exclusive license. Public testbed/scanner code/license completeness was not independently verified here. An offline state/evidence test is feasible; no turnkey production-system replication claimed. |

**BAF methodological caveat:** source study uses temporal month splitting and acknowledges selective labels; it also embeds generator/feature-selection choices. A proposed benchmark is still synthetic, and does not restore outcomes of pre-screened rejected applicants. Don't make precise operational-profit claims from it. This pass did not run its substantial model-search notebooks or regenerate the underlying private-data GAN.

## 6. Companies, teams, researchers and public professional channels

| Branch | Institutions/teams and professional channel | Access/evidence limit |
|---|---|---|
| Ledger, resilience and integration | TigerBeetle [public repo/issues/contribution files](https://github.com/tigerbeetle/tigerbeetle); bank/payment-provider platform teams; Accenture RTGS delivery context in NAO report | Open code contributions are possible routes, not guaranteed employment. Production critical infrastructure needs trusted access and extensive operations evidence. |
| Payment/data reconciliation | Wise [official engineering/careers route](https://wise.jobs/jobs); Stripe [careers](https://stripe.com/jobs) and developer documentation; BlackLine investor/company channels | Existing recurring software spend is established; live customer exports and operating policy are not public. Do not contact finance operators or use employer/customer data without authorization. |
| Fraud and fair ML | [Feedzai Research](https://research.feedzai.com/) and [BAF issues](https://github.com/feedzai/bank-account-fraud/issues); authors listed above; ULB/Worldline handbook [public repository/issues](https://github.com/Fraud-Detection-Handbook/fraud-detection-handbook) | Research participation is distinct from a current job. [Feedzai careers](https://careers.feedzai.com/all-jobs/) currently exposes several technical roles in Portugal/Brazil/US; a generic UK office does not establish UK/India ML availability. |
| Settlement and interoperability | Bank of England [RTGS renewal/operator pages](https://www.bankofengland.co.uk/payment-and-settlement/rtgs-renewal-programme); BIS Innovation Hub [Aurora project page](https://www.bis.org/publications/project-aurora-power-data-technology-and-collaboration-combat-money-laundering-across-institutions-and-borders) | Public operator engagement/contact routes can be followed later if requested. No settlement-account/testbed eligibility inferred; “open research” is not open network membership. |
| Agentic commerce | AP2 [official repo/issues](https://github.com/google-agentic-commerce/AP2), Visa developer documentation, Ben-Gurion/Intuit paper author network | Use designated project/security channels. No outreach, certification, developer account, keys or merchant onboarding was requested or performed. |
| India payment engineering | [Razorpay careers](https://razorpay.com/careers/), Wise Hyderabad role below; Adyen Bengaluru [official office/careers](https://adyen-careers.com/locations/bengaluru) | Razorpay career messaging is positioning, not a verified specific opening. Adyen search snippets listed backend roles, but direct office render showed **0 openings**; current specific availability unresolved. |

Names are public paper/professional identifiers, not private contacts or implied advisers. Company careers/developer issues and institutional channels are the routes; no person was messaged.

## 7. Reachable role evidence for India/UK, with filters retained

### India: a genuine backend/ML-integration route, at seniority

Directly opened [Wise Senior Software Engineer, Backend, Hyderabad](https://wise.jobs/job/senior-software-engineer-backend-in-hyderabad-jid-4122), with Apply visible on 19 October 2026. Describes Global KYC/Onboarding, risk/mitigation integrations, ML/AI where useful, safe fallbacks and observability. Requires **6+ years Java/Spring, asynchronous messaging and scalable microservices**, plus database/architecture/cross-team ownership. Advertised range **INR 4.9–7.8 million annual** is this role's range, not a sector median or a promised offer. No PhD is listed; it is still a senior engineering bar, and a Python-only demo does not satisfy it. Work authorization/sponsorship was not established.

### UK: domain entry may accept transferable systems skill

Directly opened [Zopa Senior C# Software Engineer, London, Cards Engineering](https://jobs.lever.co/zopa/d29493d5-149d-4353-a199-1733b9818026). It values production ownership, TDD, distributed-system judgment, mentoring and Kafka/Kubernetes/Postgres-style infrastructure, and describes support for JVM/Kotlin cross-training. Banking experience is a plus rather than a universal prerequisite. **London office 2–3 days/week**; limited working-abroad provisions do not mean global remote employment. Visa eligibility, pay and hiring probability not established.

The particularly relevant [Wise Spend Settlements & Reconciliation backend ad](https://wise.jobs/job/backend-engineer-spend-settlements-and-reconciliation-in-london-jid-125) explicitly says **expired**. Its Java/Spring/messaging/database and operational consistency requirements are useful historical capability evidence, not an available action today.

**Career inference:** the nearest first route is backend/data/reliability or risk-platform engineering, then deeper domain/model decision responsibility. Pure fraud research, quantitative credit modeling and financial/scientific leadership have different statistics/domain/research requirements. Software roles do not universally require a finance doctorate, and the sample does not establish a junior hiring boom, a 2031 salary forecast or automatic portfolio substitution for experience.

## 8. Safe offline 30-day project: a settlement and reconciliation evidence harness

Proposed, not implemented. Planning assumption: 35–55 focused hours, an existing approved SQL/Python or JVM runtime and synthetic records. No payment-provider account, API keys or real money is needed. Any missing software/data download remains a later approval decision. Prefer an existing transactional database or approved ledger library; do not build a new production ledger engine.

**Domain boundary:** one fake merchant, provider clearing account, bank account and fee/refund/dispute categories; one currency initially. Two synthetic views are generated from a hidden source-of-truth fixture: provider events/batches and bank statement rows. The matcher sees only the allowed observable fields. Keep the generator's true match IDs out of matcher features. Ordinary deterministic extraction is the baseline.

### Week 1: define the accounting/state oracle

- Every modeled journal balances signed debits/credits **within its currency/ledger**, using integer minor units or exact decimal with explicit currency precision. Do not sum unrelated currencies numerically.
- Opening position plus posted movements equals closing position; pending/reserved and available amounts are separate. A reservation is not posted revenue or bank cash.
- Same committed business operation cannot post twice; source-event deduplication alone is insufficient if two distinct events describe the same effect.
- Unknown settlement or unmatched external movement remains explicit. A perfectly balanced internal journal does not permit the reconciliation report to assert a bank receipt absent statement evidence.
- Define fake-domain refund/capture rules and reversal references explicitly; do not present them as universal payment-network rules.

### Weeks 2–3: realistic exceptions and mature baselines

Create 100–300 auditable synthetic cases across exact matches, missing reference, shared amount/date, aggregated net payout, fee/refund/dispute in a later period, delayed bank posting, duplicate/out-of-order event, partial refund, failed payout and conflicting source revision. Include at least ten genuinely ambiguous cases with a required abstention.

Compare: (A) exact stable-ID SQL join; (B) deterministic constrained batch matching with declared tolerance/window; (C) optional statistical/model candidate ranking or explanation **without direct ledger writes**. Don't use a model if rules already solve the selected task. An explanation must reference actual source rows and expose alternatives/unknowns. No invented balancing entry is accepted.

Inject crash before commit, commit-success/response-loss, repeated event, report not yet available and stale/revised data. Record business event time, provider availability, expected/actual bank time, source publication/retrieval and reconciliation decision time. Decision-time replay must not see later bank/chargeback evidence.

### Week 4: acceptance and report

- Zero double-posting or accounting-invariant violations in the finite suite; seed and then detect a deliberately broken duplicate-effect check and a currency-unit conversion bug.
- Report match precision and coverage **by case family**, amount-weighted erroneous match exposure, unresolved amount/age, and appropriately abstained ambiguous cases. Do not optimize raw match rate by accepting guesses.
- Replay/recovery preserves postings and source provenance; no ambiguous timeout is silently successful. Preserve before/after state and the first failed assumption.
- Measure runtime, database writes, p95 latency for the local workload, review steps/time (measured or explicitly assumed), and optional model call cost. No real-money savings claim from synthetic cases.
- A second engineer can independently reproduce one ordinary, one ambiguous and one fault/recovery case after approved setup. Compare conclusions to the hidden oracle, not the implementation's own success flag.

**Kill criteria:** the mature SQL/provider report already solves everything; candidate ranking reduces review clicks while increasing costly false matches; source identifiers/vintages cannot be reconstructed; the only “value” is a generated narrative; or each new case requires inventing a different unsupported accounting rule. Keep the exercise as systems competence even when it disproves a product thesis.

## 9. Ninety-day extension: choose financial data integrity OR delayed-label risk

Do not combine a ledger rewrite, an AML detector and an autonomous buyer into one project. Estimated additional 70–130 hours, conditional on existing resources; no compute spend assumed approved.

### Option A — stronger reconciliation/recovery evidence

Add a second provider schema and month boundary; keep the same accounting oracle. Introduce a held-out case generator/version so test data does not share every template with development. Add bounded one-to-many batches, ambiguous matches, schema/unit changes and a second currency only if the per-currency/FX accounting specification is reviewed. A synthetic FX rate is an assumption, not a tradable price.

Test import/reprocessing, restore, backlog aging and operator correction after late revisions. Compare mature deterministic matching/assignment with optional model assistance at matched false-match exposure and total review effort. Evaluate the model on adversarial source text and missing evidence; a persuasive explanation must not override the ledger/row oracle. One public schema/SDK documentation bug or narrow regression may be prepared locally; external submission requires its own authorization.

**Stronger claims require:** an authorized domain owner and representative, permitted source data. Neither is secured by this research. Until then claim integration/evaluation/recovery evidence, not real close-time savings, compliant financial statements or commercial readiness.

### Option B — delayed-label risk experiment

Use an approved, rights-checked synthetic fraud simulator or selected public benchmark; BAF terms remain unresolved in this pass, so it is not a default cleared input. CPU-scale rules/logistic model and boosted-tree baseline are sufficient; full GAN regeneration or a large language model is unnecessary.

Preserve temporal blocks, feature availability and label-observation delay. Threshold/calibration only uses development data; freeze final test. Group related entities/episodes appropriately and make drift explicit. Compare stable rules, simple statistical baseline, adaptive/retrained model and a deliberately leaked random-split diagnostic kept separate from valid results.

Metrics: average precision, precision/recall at fixed review capacity or a chosen false-positive budget, calibration/Brier score, age/segment denominators where valid, compute/latency, label-delay sensitivity and an explicit synthetic cost surface. Cost weights are assumptions unless supplied by an authorized business. Report performance for mature labels and the unobserved/censored portion separately.

**Kill criteria:** gain disappears when delayed labels or causal features are enforced; performance relies on synthetic-generator shortcuts; model is no better than a simple rule at the operating point; subgroup conclusions have insufficient support; or claimed business lift requires outcomes the offline data cannot reveal. A benchmark improvement does not establish that blocking real payments prevents the same loss.

### Optional agent-commerce slice, after either foundation

Use fake cart/order/mandate/receipt/provider/statement records to test total-price changes, partial fulfillment, retry and refund/reconciliation consistency. Let an agent propose a cart or draft an evidence summary; deterministic code applies the same accepted business rules. Compare with a fixed workflow at matched correctness and review effort. Do not process a sandbox/live payment or claim scheme approval. The question is whether language flexibility adds measurable value after the existing ledger and matching infrastructure works.

## 10. What this changes in the 2031 career forecast

**High-confidence transferable preparation:** transaction/state correctness, money/unit models, SQL/data pipelines, streaming features, causal information-time reasoning, reliable APIs, traceability, fault recovery and evaluation with costly false positives.

**Medium-confidence specialization:** financial data/reconciliation, risk-platform and payment reliability engineers using both deterministic systems and ML. Native tools will automate parts of each job. Leadership comes from owning correctness, operational exceptions and stakeholder trade-offs, not merely producing an agent demo.

**Unproven:** new occupation counts, future wages, independent-developer access to bank labels, broad autonomous-commerce profitability, or a universal fraud/AML model. Public budgets and incumbent revenue support existing paid work; they do not establish which startup captures future value. The practical test is a narrow failure/decision whose improvement survives a competent native/non-AI baseline and representative permitted data.
