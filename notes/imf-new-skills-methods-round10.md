# IMF SDN 2026/001: new-skill measurement, wages and employment identification

Checked 20 October 2026, extending the [earlier partial reconciliation](<root-imf-partial-reconciliation-round10.md>) and [root evidence notes](<root-evidence.md>). The previously resolved scaling arithmetic is unchanged and is not new work here.

**Access improved:** the [official 49-page PDF](https://www.imf.org/-/media/files/publications/sdn/2026/english/sdnea2026001.pdf) became readable in the web PDF tool. Relevant main text and Annexes I–IV were inspected. Direct public-network retrieval and publisher HTML still returned 403; a local PDF byte copy/hash and visual graph inspection were not obtained. This is a substantive methods-text audit, not a regression replication or a completed graph/pretrend audit.

The responsible conclusion is narrower than a training recommendation: the note documents changing skill language in online demand, conditional advertised-pay differences and regional employment/wage patterns under substantial identification assumptions. Its different designs should remain separate. It does not estimate the reader's return to a course, predict Indian developer job counts or observe five years of post-ChatGPT employment effects.

## Source identity and version

The document is *Bridging Skill Gaps for the Future: New Jobs Creation in the AI Age*, by Florence Jaumotte, Jaden Kim, David Koll, Elmer Z. Li, Longji Li, Giovanni Melina, Alina Song and Marina M. Tavares, SDN 2026/001. The PDF cover says January 2026. The [IMF publication URL](https://www.imf.org/en/publications/staff-discussion-notes/issues/2026/01/09/bridging-skill-gaps-for-the-future-new-jobs-creation-in-the-ai-age-572136) and series listing use 9 January, while the [publisher record](https://www.elibrary.imf.org/view/journals/006/2026/001/article-A001-en.xml) gives 14 January. Book DOI: `10.5089/9798229028196.006`; article DOI adds `.A001`. These date surfaces were already identified and remain distinct.

Page references below are printed PDF pages, which match the page number of the complete 49-page document. “Verified” means the inspected text supports the documentary statement; it does not imply causal identification or independent data verification.

## Measurement and sample map

| Component | Verified definition/window | Consequence |
|---|---|---|
| New-skill dictionary | US 2010–24; sparse 2010–11 presence, normalized annual mentions/CDF; minimum 100 US postings | Retrospective relative emergence, not a literal invention date or 1% of all vacancies |
| Descriptive postings | June 2025 Lightcast release; different country windows | Formal online demand, not complete employment or task use |
| Posted-pay comparison | US/UK 2020–24, complete required fields; 54.3m/5.6m postings | Selected advertisements, not worker earnings |
| US regional outcomes | ACS/Lightcast 2013–23; commuting-zone long differences | Regional levels/composition, not observed hiring/separation flows |
| German outcomes | 2019–23 differences; administrative 2% sample, 96 regions; June 30 employment | Different endpoint and population from US survey outcomes |
| AI event study | Reuses US regional outcome data; changing/recurrent skill-demand intensity | Historical differential adjustment, not a post-2026 forecast |
| Extended country indices | US skill patterns projected using employment/graduation structure | Modelled comparability assumptions, including for India |

Exact country windows in Annex I are US 2010–25, UK 2012–24, Germany 2018–24, and Denmark/Brazil/South Africa 2021–24; 2025 descriptive coverage is January–June where specified. The introduction's broader references to coverage beginning 2020 should not replace those analysis-specific windows. Annex III's wage subset and Annex II's outcomes have separate windows.

## 1. “New” has a particular retrospective denominator

The main definition on p. 8 classifies a skill as new when its early-period presence is below a 1% threshold relative to its 2010–24 US appearance distribution. Footnote 3 matters: annual posting-volume differences are accounted for using the share listing each skill within each year to construct a cumulative appearance distribution. Skills need at least 100 US postings. It would be incorrect to describe this as “used in 1% of all jobs,” or implement it as a simple raw-mention threshold while ignoring the normalization.

**Independent audit implications:** the measure captures the growth of demand language relative to a historical benchmark. A pre-existing capability can qualify if its mentions grow sufficiently. A new product name, a new label for established work, taxonomy changes and genuine new tasks need not be the same phenomenon. The cutoff uses information from later years; it is not an index that a 2013 observer could necessarily have constructed then. That need not invalidate a retrospective description, but it matters for predictive or causal interpretation.

The exact code/formula translating normalized annual shares into the cumulative threshold was not located. A replication should freeze taxonomy IDs, aliases, annual denominators, cutoff horizon and the 100-ad filter. Sensitivity to alternative cutoff dates and definitions would test whether later growth mechanically selects the treatment set. The country-specific “pure new” check in Annex I uses absence in 2021 followed by emergence from 2022; its similar occupational distribution supports a descriptive pattern, not automatically the wage or employment identification.

AI labels are a further layer. Footnote 7 says **ChatGPT 4.1-nano** classifies identified new skills into developer, user or non-AI categories, excluding general software skills with weak AI links. This differs from the **4o-mini** field-of-study inference used in the supply index. The two model uses should not be merged. Exact prompts, model snapshot, label-validation error and a reusable classification manifest were not established in this pass.

## 2. Posting coverage and weights do not recreate all vacancies

Annex I.5 describes scraping more than 220,000 sites and a two-step deduplication process, including comparison with the preceding 60 days. Occupations, industries, skills and locations are vendor-inferred. Remote status is not consistently identified. The note acknowledges formal/urban/high-skill coverage bias and employer internal labor markets.

Brazil and South Africa are reweighted using ILO two-digit occupational employment shares; their occupation coding vintages also differ. Employment weights and vacancy weights answer different questions. Reweighting can address a compositional margin while leaving within-occupation coverage, missing informal work, firm selection and posting intensity unresolved. A unique advertisement is not necessarily a unique funded vacancy or a hire; 60-day deduplication does not itself establish the absence of recurring or strategically written ads.

**Replication requirements:** occupation crosswalk versions, coverage changes, geographic assignment rules, denominator construction and missing-cell handling. Remote recruitment can separate the employer's advertised location from the worker's residence. The paper acknowledges that issue and argues that IV/controls mitigate it; mitigation is not proof that the geographic assignment error is harmless or absent.

## 3. The advertised-pay premium is conditional selection, not a training experiment

Annex III uses postings with nonmissing wage, skill, industry, occupation, geography, pay-period and year information. Wage ranges become midpoints and pay frequencies are converted to hourly units. Intended comparisons are within detailed occupation×industry×local-geography×year cells, with pay-period×year and total-skill-count effects; errors cluster by occupation. Main text and Figure 5 support county/local-authority geography, while Annex III's notation once says “country.” That wording discrepancy should be reconciled from code rather than silently selecting the weaker or stronger specification.

These controls are meaningful. They make a broad occupational-composition explanation less sufficient. They do not randomize skill acquisition, hold every employer/seniority/experience requirement constant or observe what workers subsequently earn. At fixed total skill count, the coefficient compares a different mix of requested skills; it is not the effect of taking a course and adding a skill to an individual's CV.

Posted-pay availability itself changes with disclosure behavior and pay-transparency rules, acknowledged in footnote 9. Local-year effects can absorb common local changes without eliminating selection within the cell. A stronger audit would report the wage-reporting fraction and exclusions by year/region/skill/seniority, analyze narrow versus wide ranges, assess firm-level dependence and verify hourly conversion assumptions. The retained sample sizes are counts of ads, not unique workers or offer acceptances. No causal pay return for an Indian engineer follows from the conditional premium.

## 4. Regional long differences: a distinct shift-share IV design

Annex II.1 combines baseline occupational employment shares with skill-demand changes. US outcomes change over 2013–23, using 2000 occupational shares; instruments draw on 2013 skill-demand levels in California and the UK. Germany uses 2019–23 outcomes, baseline 2011–14 shares, and US skill measures from earlier years. The printed formulas and surrounding description require careful implementation: some components are levels rather than changes, and exact first-stage construction should be documented.

US ACS outcomes are geographically aggregated using PUMA/CZ and county/CZ crosswalks. Controls cover initial labor-market, industry, education and demographic conditions, with state and demographic effects; US uncertainty clusters at CZ level. The note claims high first-stage F statistics and supportive Hansen J tests, but exact reported values were not located in the methods text inspected. Do not state that no diagnostics were run. Conversely, instrument relevance and a nonrejection test do not prove exclusion.

**Independent identification audit:** frontier occupational skill demand may predict later local outcomes through persistent occupational/sectoral trends, global demand, organizational change or worker migration as well as skill diffusion. Predetermined shares remove one source of simultaneity, not every omitted exposure. An industry or technology shock may affect regions differently according to those same shares. Useful checks include alternative base years, exclusion of frontier regions where relevant, contribution/weight diagnostics, first-stage sensitivity and preperiod outcomes. None was independently re-estimated here.

German daily wages are censored/imputed, and part-time wages are multiplied by two; cells require at least five observations. Those are consequential measurement assumptions, not actual hours observed. The US text describes hourly wages from annual income/hours/weeks; exact ACS variable names, income exclusions, survey weights and sample filters still need the implementation. Differences between the two countries are not a randomized comparison of institutions or training policies.

Policy interactions also deserve their own interpretation: baseline union, retraining or other regional conditions are moderators, not randomized interventions. A positive interaction cannot identify the return to signing up for a course, nor prove that changing a policy alone would reproduce the estimate.

## 5. AI event study: modern estimator, remaining assignment assumptions

Annex II.2 describes de Chaisemartin/D'Haultfoeuille methods for staggered, recurrent and nonbinary treatment, comparing relevant treated groups with not-yet/never-treated units. That is preferable to assuming a conventional two-way-fixed-effects event study automatically handles heterogeneous timing. Figure 9 reports 95% bands around dynamic log-employment estimates.

However, the package/version, exact treatment series, entry threshold, recurrent-wave rules, cohort/event-time weights, sample counts, control support, clustering and exact normalization were not sufficiently specified to reproduce the analysis from this note alone. The methods say county-level analysis and later define the index as a commuting zone. It is unsafe to collapse that inconsistency into a precise geographic claim without the underlying implementation. The simplified regression is not the executable estimator.

The identifying problem remains: job-posting skill demand can change in response to expected restructuring or demand conditions. Employers and workers can anticipate changes before a measured first posting. Not-yet-treated areas can already be affected through competition, mobility, services demand or remote work. An appropriate estimator handles certain weighting/timing biases; it does not create random adoption or eliminate interference.

A complete check would inspect the leads, uncertainty and power; report a joint pretrend test where appropriate; vary anticipation windows; show event-time support; and assess sensitivity to alternative definitions/controls. The graph itself was not visually inspected in this environment, so this audit claims neither that parallel trends hold nor that a particular lead rejects them. The caption's 95% bands are not numerical endpoint intervals extracted here.

**The clock is decisive:** Annex II says the event study uses the US 2013–23 outcome data. A five-year response with that endpoint must draw on earlier entry cohorts; it cannot mean five years after ChatGPT's November 2022 release. Descriptive AI-user postings through 2025 and historical regional outcomes are different evidence. This materially limits direct transport to stronger 2026 agents or 2031.

## 6. Exposure, complementarity and India require separate bridges

The note's high-exposure/low-complementarity groups inherit occupation-based measures from earlier IMF work. They are not individually observed substitution decisions. Figure 8 also uses a different AI-use proxy: industry adoption from the 2019 ABS module, weighted into local areas using their industry composition. That should not be confused with Figure 9's changing AI-skill posting demand. The group mapping and its uncertainty were not re-created here.

Likewise, the youth-risk discussion combines age/occupational composition with other studies; it is not a direct age-specific course-return experiment. The note cites an older Stanford/ADP vintage. Current Stanford evidence is already reconciled in the existing labor reports; the SDN should not be treated as payroll evidence through 2026.

India is absent from the six-country core posting/outcome exercises. It appears in the extended country-index exercise using UNESCO graduate information. Annex IV projects US occupational skill requirements and US graduate skill-by-field patterns onto other countries; the extension has broader field mappings and different tertiary-level coverage. This is a modelled comparison, not directly observed Indian AI vacancies, actual graduate competence or a domestic causal employment estimate. Inferred profile skills, graduation flows, employment stocks and normalized readiness are separate quantities.

The broader macro task/wage regressions use O*NET emerging tasks and country-year data rather than the same Lightcast treatment. They supply another conditional association; they cannot be merged with the posting premium or regional estimate as multiple estimates of one personal return. Numerical macro-table extraction/typography was not adjudicated visually and is not used for a precision claim here.

## Strongest responsible use in the developer-futures research

Use the note as evidence that occupational labels conceal changing combinations of requested skills, that requested-skill wage associations differ by setting, and that diffusion can coexist with uneven regional adjustment. Retain the assumptions beside every employment or pay number. Do not infer that a specific tool, course, credential or profession supplies a measured individual wage gain, or that projected national skill imbalance creates an attainable vacancy.

For the reader's preparation, the defensible implication is a question: **which actual work requirement can be demonstrated independently and used within an attainable role or workflow?** Existing preparation and selection gates already answer how to test that. A small synthetic implementation can illustrate the effect of a dictionary cutoff or wage-reporting selection, but would demonstrate measurement mechanics rather than replicate this paper or forecast employment. No new project, private-data request, enrollment or application is authorized by this audit.

Evidence that would strengthen causal use includes a reproducible dictionary/label manifest, frozen historical definitions, exact event-study settings, supported leads and cohorts, credible treatment assignment, sensitivity to common industry shocks and spillovers, and more direct adoption/worker outcomes. Evidence that would weaken it includes strong results disappearing under those checks. Neither absence of implementation details nor a plausible rival explanation by itself proves the substantive result false.

## Completion and remaining access limits

The source/claim manifest is [imf-new-skills-methods-round10.json](<imf-new-skills-methods-round10.json>). It separates documentary definitions, conditional findings, independent inferences and open replication gates. Full primary **text** access is recovered; code/data replication, exact graph/pretrend verification, some notation and classification details remain open. Lightcast and restricted administrative microdata were not accessed. Public PDF byte retrieval stayed 403, so no local source-file hash is invented. No third-party account was used in place of the methods.
