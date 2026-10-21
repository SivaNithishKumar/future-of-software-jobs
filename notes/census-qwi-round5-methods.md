# Census QWI audit: early-career hiring, employment and the limits of a ChatGPT event study

Primary paper and supporting Census definitions checked 19 October 2026. This is a distinct full-method pass on Lee C. Tucker, CES26-27. It does not resample vacancies, audit BLSWP591 or NBER35271, install software, use restricted records or contact anyone.

## Narrow conclusion

The paper supplies a valuable **independent administrative-data check on weakness in young-worker employment and sustained hiring in highly AI-exposed industries**, outside the selected ADP payroll sample. It improves mechanism analysis by observing relevant employment flows and establishments' growth or contraction.

It does **not identify a causal 12% loss of jobs from actual AI use**, count unemployed graduates, observe individual occupations or establish a 2031 forecast. Its stronger controls expose important pre-ChatGPT trends. Its counterfactual is an accounting exercise conditional on assumed flows, and its “backfill” evidence uses an association rather than linked vacancies. These qualifications belong beside the headline, not in a distant disclaimer.

## Exact source and version

- [Official Census working-paper page](https://www.census.gov/library/working-papers/2026/adrm/CES-WP-26-27.html): **April2026**, CES26-27; page last revised **7May2026**. The page does not establish that the PDF itself was substantively revised that day.
- [Official primary PDF](https://www2.census.gov/library/working-papers/2026/adrm/ces/CES-WP-26-27.pdf): **43pages**, cover dated April2026; PDF creation/modification metadata **27April2026**. Retained as `sources/labor-census-ces26-27.pdf`, **2,886,584bytes**, SHA256 `bc4c7e6da652f79fd796aecc008ff1219138eff9c4a1cf44d3411160eec039c6`.
- Methods, footnotes, equations, findings and appendices were read. Figures6,7 and12 were rendered and inspected to verify plotted windows, definitions and pretrends. These are a methods audit, not an econometric replication. Printed page numbers are used below; PDF page number is one greater.
- The working-paper series states that findings are the author's and have not undergone the review accorded official Census publications. Administrative data provenance should not be confused with official endorsement of a causal interpretation.

## What is observed, and what is assigned

| Component | Verified definition | Consequence for interpretation |
|---|---|---|
| Employment source | Public Quarterly Workforce Indicators, tabulated from matched employer–employee/UI wage records; paper analyzes private-sector employment | Much broader administrative coverage than one payroll provider, but not every form of US work or an individual population census |
| Age | **22–24** for the main group; comparisons include **25–54** and **55+** | An age bin is not a first-job cohort, graduate cohort, tenure category or credential measure |
| Unit | Detailed **6-digit NAICS2022 industry × state × quarter** tabulations | Actual individual occupations, employer AI adoption and job requirements are not observed |
| Assigned exposure | GPT4-beta task exposure, crosswalked through **2015–19ACS PUMS** occupational composition and Census industry/occupation mappings | Predetermined composition helps avoid some post-treatment reclassification, but assigns industry averages and loses within-industry differences |
| Quintiles | Industry-state means weighted by **all-age 2022employment** | Top quintile represents20% of all-age employment, not20% of young workers; the reference young-worker share is15.9% |
| Stock | Beginning-of-quarter employment inferred from positive quarterly earnings across a boundary | A dated stock proxy, not all people with any earnings during that quarter |
| Hiring flow | **End-of-quarter hires**: hires during the quarter remaining employed at the next boundary | Not every fleeting hire, not necessarily a first-ever job, and not the general all-accessions series |
| Separation flow | **Beginning-of-quarter separations**: separations from people employed at the prior boundary | Does not distinguish voluntary departures, layoffs or other separation reasons |
| Earnings | Four-quarter change in log average monthly earnings of stable/full-quarter workers | A selected-stayer group average; not a wage offer, lifetime earnings or an individual fixed-worker wage treatment effect |

Supporting primary [LEHD/QWI documentation](https://lehd.ces.census.gov/data/lehd-snapshot-doc/latest/sections/employer_level/qwi.html) explains job-history-based construction, imputation/successor-predecessor adjustments and public variable mappings. The paper's footnotes9/13 specify end-boundary hires and beginning-boundary separations. The public schema calls the former **HirAEnd**; the paper prints **HireAEnd** in one footnote, a naming discrepancy a replication should resolve explicitly.

The general [QWI measure guide](https://lehd.ces.census.gov/doc/QWI_101.pdf) describes broad UI-based coverage. “Near-universe” does not remove excluded work, disclosure protection, revisions or classification issues. A person with multiple employer-job relationships is not automatically a unique employed individual when aggregating job measures.

### Coverage and sample details that remain insufficiently documented

The PDF does not provide a clear manifest of included states, a baseline cell count, unique state/industry counts, a balanced-panel rule, or an exact public-data release identifier. It also does not clearly state baseline zero/log-zero handling, suppression-status filters, or whether missing cells are dropped, interpolated or reaggregated. These are **documentation gaps identified in the materials inspected**, not proof the implementation is incorrect.

Figures display a long preperiod beginning around2007 and end in2025. “All available” time periods are used in the monetary-policy exercise, but the exact state-specific starting quarters were not recovered from the paper. Do not invent a uniform national sample window from axis labels. Current public QWI releases can revise the full history, so a present-day download need not reproduce this April2026 snapshot exactly.

## Exposure aggregation: useful validation, substantial information loss

The paper's Table1 quantifies the principal cost of its crosswalk: weighted exposure variance falls from **0.0447 at occupation level to0.0148 at industry-state level**, with an intraclass correlation of about **0.331**. Roughly two-thirds of the individual occupational variation is lost in that aggregation. Further mapping to fine NAICS categories adds less information because ACS industries often resolve only approximately to4-digit NAICS.

The industry exposure measure predicts a meaningful fraction of later BTOS subsector adoption variation, and alternative exposure measures are compared in AppendixTableA1. This supports exposure's relevance. It does not observe treatment for the same individual employer whose hiring changes. Aggregate adoption validation cannot establish that every high-exposure firm uses AI, why it uses it or what jobs it automates. BTOS question wording also changed in late2025; its later association with exposure is not a direct measure of uptake at ChatGPT's release.

**Independent audit implication:** precision at the6-digit industry-state outcome level should not be mistaken for equally fine exposure measurement. Workers doing very different tasks receive the same average assignment. Measurement error may weaken effects, but it can also correlate with sector composition or education; its bias is not guaranteed to be simple attenuation.

## Baseline regression and correct clocks

Equation1 regresses an age-specific log outcome on **industry-state fixed effects, quarter fixed effects and period × top-quintile indicators**. Errors are **two-way clustered by detailed industry and state**. The baseline absorbs stable cell differences and shocks common to the age group. It does not directly absorb every time-varying industry-specific or state-specific shock. Its discussion and figure captions do not make main-regression weighting as explicit as the2022employment weighting used in exposure construction and within-sector Table2; a replicator should not silently assume those are identical.

Stocks and flows use deliberately different reference quarters: **2022Q4** for beginning-boundary employment/separations and **2022Q3** for end-boundary hires/earnings. Thus their reference dates are approximately **1October2022** and **30September2022**, before ChatGPT's30November release. Main employment ends at **2025Q2 beginning**, approximately **1April2025**; corresponding latest flows are **2025Q1**, ending31March. This is not an employment observation on30June2025 or a study through2026.

The reference stock is **6.55m young-worker employment relationships**, with **1.04m in the top exposure quintile**. The raw top-quintile decline is **15.2%**, approximately159,000 relationships. Regression adjustment plus a four-quarter comparison produces the paper's preferred approximately **12.4%** relative decline; the latest single-quarter log coefficient is different. These observed/adjusted quantities are not interchangeable with an AI-caused job-loss count.

### Why the four-quarter result matters

The author explicitly identifies residual exposure-specific seasonality. The preferred comparison averages the latest four quarterly estimates against the four-quarter reference window, rather than treating the last point as a seasonally invariant endpoint. For example, Figure6 prints a latest coefficient of−0.134 and latest-four-quarter comparison of−0.124. Log coefficients are approximate percentages; exact exponential transformation differs slightly. Report “roughly12% relative” unless the precise estimand and transformation are supplied.

The figures show uncertainty bands, but numerical endpoint intervals and their level are not clearly specified in the inspected captions. No exact confidence interval is reconstructed here. Table2 states its robust-error significance thresholds; the main event studies state their clustering. A pooled four-quarter contrast also requires its own covariance-aware uncertainty calculation, rather than averaging individual bands.

## Hiring-rate recovery is not hiring recovery

The persistent fall in **hire counts** coexists with recovery of the **hiring rate**. The rate uses average beginning/end-quarter employment as denominator. If both hires and the employment base contract proportionately, the rate can return to its former value without any catch-up in the number of starts.

Illustration only:100hires /1,000jobs =10%;88hires /880jobs =10%. This is not the paper's actual data. It shows why a normal-looking rate does not establish restoration of the original opportunity pool.

Figure7's four-quarter hire-count comparison is about−12.7log points, while separations also decline. Fewer separations partly offset fewer hires. These are boundary-linked flows, not evidence that layoffs surged. Establishment moves across states can also be coded as hires and separations, as the paper notes. This makes vacancy starts, labor-force entries, job-to-job transitions and demographic entry important distinct outcomes for career interpretation.

## The flow counterfactual is accounting, not causal identification

The paper decomposes stock changes into hires minus separations plus workers aging into/out of the bin and miscellaneous adjustments. Its residual composition term includes age transitions, NAICS changes and imputations. The author argues it is dominated by net aging, based partly on all-age checks, but it is not directly observed educational deferral.

The counterfactual uses pre-reference/calendar-matched flow patterns and assumes a stable relative compositional adjustment. Under those assumptions, maintaining counterfactual hires would offset the full observed employment decline, while counterfactual higher separations would worsen it. This establishes that reduced hiring is a central accounting margin. It does **not establish that AI caused100% of the decline**.

Delayed graduation or longer education can appear immediately as a foregone hire, with later offsets in age composition. Therefore a “hires” channel does not, on its own, distinguish employer demand from worker supply. Nor can a descriptive accounting decomposition reveal the counterfactual lifetime careers of people absent from the22–24bin. A lower narrow-age stock may have different implications from fewer jobs over an entire career.

## The strongest internal disconfirmation: earlier triple-difference trends

Equation3 relates younger-worker outcomes to older-worker outcomes, allowing the relationship to vary by time and exposure. It is a **scale/slope comparison**, not simply the baseline12% coefficient with an older control subtracted. It relaxes the assumption that industries share every aggregate demand shock, but requires the younger/older relationship to evolve comparably absent AI.

The paper's Figure12 and discussion acknowledge that relative employment, overall hires and separations in high-exposure industries began weakening around **COVID**, before ChatGPT. Overall hire results in this specification do not show an obvious release-date discontinuity. Earlier growth of remote work and educational attainment is correlated with exposure; neither is directly controlled at the employer level. These are substantial rival explanations, not minor qualifications.

**Independent audit implications:** older workers can themselves be affected by AI, making this a relative-age estimand rather than the total employment effect. An age-specific financing or mentoring shock can also violate the scale assumption. Conditioning on contemporaneous older outcomes may absorb an AI channel common to ages. Conversely, finding a young-relative effect does not distinguish supply from demand. Both the baseline and this alternative should be reported rather than choosing the preferred result after inspection.

## Job gains and “backfill”: useful but indirect mechanism evidence

The author finds more release-aligned changes in young-worker job gains/losses at growing/shrinking establishments and in relationships between young replacement hires and older separations. This adds information beyond a single age-stock plot.

But QWI tabulations do not link a particular young hire to a particular vacancy left by an older worker. **True backfills are a subset of replacement hires**, and the paper cautions that this relationship is a proxy. Correlated cell-level flows can arise from several patterns of turnover and labor demand. It is too strong to say the data directly observe firms replacing older workers with AI rather than hiring juniors. Separation reasons remain unidentified, and a declined job-loss count can reflect fewer jobs exposed to loss.

A stronger mechanism test would link employers, vacancies/job positions, worker spells, actual tasks and adoption dates, including older separations that were never refilled and positions filled by another age group. The current evidence motivates that test; it does not substitute for it.

## Monetary policy: a bounded rival-explanation test

The author fits industry-specific local projections to **unexpected monetary-policy shocks**, using pre-COVID QWI observations through **2016Q4**, then applies historical responses to later shocks. The surprise-shock series ends in **2023Q4**; later shocks are set to zero. The model suggests a relative employment contribution of about3.1log points by2025Q2, around one-quarter of the preferred12.4comparison, but does not reproduce the observed relative hire pattern well.

This weakens one particular explanation based on measured policy surprises. It does not demonstrate that **all interest-rate/financing effects are small**, or that the remaining three-quarters is AI. The author explicitly notes that anticipated policy effects are omitted. Historical transmission can change after COVID; venture financing, client demand and uncertainty may operate differently from the fitted shock. Impulse-response outcomes are estimated separately and need not satisfy the stock-flow identity.

There is also a reproducibility question: the method text specifies projection horizons1–8, while the historical-decomposition equation sums12lags. This could be a documentation error rather than an implementation error, but code or clarification is needed before exact replication. No combined decomposition of AI, remote work, education and financing is identified by subtracting separate headline estimates.

## Robustness: what was actually done

- Within-sector exposure associations are examined, so the headline is not solely a count from one technology sector. There are exceptions: Finance/Insurance and Educational Services do not uniformly follow the overall negative within-sector pattern. Sector-specific estimates are not forecasts of safe careers.
- Appendix analyses split by firm size/age using **4-digit** groups to reduce small-cell suppression. Patterns are broadly similar, with some stronger declines in medium/large firms. These are different definitions/populations from the Danish small-firm result and do not create a clean replication conflict.
- Alternative exposure/crosswalk measures are compared for **prediction of aggregate adoption**. That is not the same as showing every employment finding robust to all those alternatives.
- Quarter fixed effects, four-quarter comparisons, age-scale comparisons and a policy-shock exercise address particular confounds. They do not jointly randomize adoption or eliminate every changing sector/age-specific influence.
- Two-way clustering is more informative than cell-level independent errors. A replication should still assess coarser clustering where exposure is effectively assigned at an ACS industry level, disclose cluster counts and examine sensitivity to broad sectors/common shocks. This is an audit question, not a claim that the reported errors are necessarily wrong.

## Comparison with existing tracks

| Study | What differs from Tucker/QWI | Valid synthesis |
|---|---|---|
| Stanford/ADP, revisedAug2026 | Selected balanced firms, occupation exposure, ages22–25, monthly data throughJun2026; headline19% kept-pace shortfall | Similar descriptive weakness across another data source improves external confidence in the pattern; different age, grouping, window and adjustment mean the numbers are not direct replications or additive losses |
| Yale CPS/SDID | Occupation-based broad groups, survey sampling and fitted synthetic comparison; narrower-cohort power limits | Broad nulls can coexist with narrow hiring problems. They also caution against assuming aggregate AI displacement from selected subgroups |
| Humlum/Vestergaard, DenmarkMar2026 | Reported users/employer encouragement in11occupations, outcomes throughDec2024, linked workers/workplaces | A null for differential adoption/encouragement effects does not rule out shared anticipation; neither does an exposure event study override the null's treatment-specific bounds |
| NationalbankWP223, Sep2026 | First-reported firm AI adoption, firm-specific trend residuals, monthly FTE throughSep2025; recruitment mainly inferred from tenure stocks | QWI observes boundary flows more directly, but lacks actual firm adoption. WP223 adds adoption timing while retaining selection/counterfactual problems. Neither identifies the other's exact estimand |

The relevant primary references and fuller audits are in `labor.md` and `labor-round3-methods.md`. These studies are not votes on a single common treatment. A harmonized same-country, same-window, same-age/outcome analysis with firm adoption would be a stronger comparison.

## Causal language and alternative stories

The author describes timing as consistent with an AI role but explicitly cautions against attributing the entire decline to AI and against long-run inference. His conclusion proposes **uncertainty-induced hiring delay** and **anticipated future adoption** as possible mechanisms, partly because measured early business uptake seems too small for an immediate direct-production explanation. These mechanisms are hypotheses, not observed firm decisions.

Other plausible stories include differential unwinding of pandemic hiring, age-specific remote-work/mentoring effects, financing or demand shocks within broad sectors, and delayed labor-force entry. A calendar coincidence and aggregate adoption correlation cannot distinguish them fully. Effects might also coexist. None should be declared the explanation without tests that measure its own timing and affected population.

## Reproducibility and what would change the conclusion

**Available:** public primary PDF, public QWI tabulations, ACS PUMS, exposure papers/crosswalks and named monetary-shock source. The paper explicitly states it uses no confidential data. The local PDF hash preserves the version inspected.

**Not found in the inspected paper/page and targeted code searches:** a linked replication package, exact data-release manifest, sample/cell counts and complete filter/weight/log-zero decisions. This is not a claim that no code exists anywhere. No full data download or regression replication was performed. Public QWI histories are recalculated quarterly; reproducing results requires archived input vintages, not only a current API request.

A replication should first reconcile the boundary variable names and dates, disclosure flags, zero cells, weighting, exposure mappings, panel balance and cluster level; reproduce Figures3/6/7/12 before extending them; distinguish point endpoints from four-quarter contrasts; and audit the local-projection horizon discrepancy. It should report what changes under newer data vintages, alternative reference dates, exposure measures, sector exclusions, seasonal controls and placebo release dates.

The stronger **AI-causal** interpretation would weaken materially if the same discontinuities appear under credible pre-release placebos, disappear with robust exposure/seasonality/sample choices, or align more closely with measured financing/remote-work/education events. It would strengthen if linked actual adoption or credible expectation shocks predict the changes within otherwise comparable firms, with no prior shifts and a demonstrated task/recruitment channel. Broad exposure effects among firms that never adopt could support anticipation but would also require ruling out non-AI common causes.

The **descriptive hiring-bottleneck** conclusion would weaken if corrected/revised public data or a transparent replication remove it. It would strengthen with persistent absolute starts, graduate-entry and promotion evidence across datasets, including restoration or continued absence of catch-up. A recovered hiring rate alone cannot decide that question.

## Career relevance, without a five-year point prediction

This evidence makes an entry/apprenticeship bottleneck worth taking seriously. It does not establish the user's age, current seniority, employment risk, country's outcome or return to a specific course. A practical response is to develop and independently verify retained fundamentals, debugging and system ownership while building inspectable work and access to feedback/real responsibilities. Track actual entry opportunities and skill transfer, rather than assuming either that more certificates guarantee a role or that developer careers have disappeared.

No job family is shown to be AI-proof. Choosing a branch should still depend on personal fit, hard geography/credential filters, credible local demand and the incremental cost to acquire demonstrable competence. These are decision gates supported by the evidence's limits, not a claim that one small portfolio or a fixed number of months ensures employment by2031.
