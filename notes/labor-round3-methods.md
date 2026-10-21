# Labor methods audit: adoption, exposure, equilibrium and returns to learning

Checked against primary sources on 19 October 2026. This is a distinct follow-up to `labor.md` and `labor-round2.md`; no new job sample was collected. BIS WP1325 is deliberately outside this pass because the root researcher owns its instrumental-variable audit.

## Result

The new Danish working paper is now available in full and **does not establish that AI caused an 11% loss of jobs**. It documents a conditional, trend-relative employment divergence among adopting firms, explicitly labels its estimates descriptive rather than causal, and has meaningful sensitivity and measurement limits. The earlier Danish null studies answer different questions and cannot be discarded, but their nulls also do not prove that every employer, cohort or future model is unaffected.

Similarly, an AI wage premium, a certificate-associated job gain, a successful assisted task and durable independent expertise are different outcomes. A good 2031 learning path needs tests of **retention, transfer, production judgment and market access**, rather than a chain of assumed implications between these measures.

## Primary source recovery and provenance

Nationalbank's public HTML exposed a PDF link omitted by the text reader. The web PDF fetch timed out; a public read-only download succeeded using existing Python and Poppler. No package was installed. Complete relevant methods pages, footnotes, tables and figure captions were inspected; Figure 7 was also rendered visually.

| Source | Version verified | Local evidence copy | Integrity |
|---|---|---|---|
| [Bonin, Darougheh and Kuchler, WP223](https://www.nationalbanken.dk/media/m2rn4owp/ai-adoption-and-firm-size-employment-effects-in-monthly-administrative-data.pdf) | 16 September 2026; 70 PDF pages | `sources/labor-wp223.pdf` | 5,411,451 bytes; SHA256 `6b2bc33fc7a96402362164f19bb2944673d81b04c7f4a961451eb20a1c249b84` |
| [Humlum and Vestergaard, revised paper](https://www.rfberlin.com/wp-content/uploads/2026/03/26078.pdf) | 13 March 2026; RFBerlin DP078/26; 132 PDF pages | `sources/labor-humlum-vestergaard-2026.pdf` | 5,352,945 bytes; SHA256 `6e6bc747de2764ce47e51594e9a33ba794c48510e27155b13d3dd79eff3347d0` |

These working papers are provisional research, not a settled occupational forecast. Page numbers below are printed page numbers; Humlum's online appendix restarts pagination.

## What WP223 actually measures

**Verified methods card (pp. 4, 8–10, 17–21, 28–31, 39, 45):** IT survey of private nonfinancial enterprises with at least 10 employees, linked to monthly wage-payment registers. Table 1's 2024 matched sample: **4,139 firms / 749,111 average monthly workers**; its universe: **25,608 / 2,346,654**. These are not the Figure 7 treated-cohort counts. Treatment is reported AI use in 2023 but not 2022; controls report neither, though about 24% later adopt. The outcome is log FTE employment residualized on firm-specific **2021–22 trends** and seasonality, then compared within **196 three-digit industry × month** cells with size effects, survey weights and firm-clustered errors. End-sample divergence is approximately −11.3 log points; 95% bands are plotted, without exact endpoint values. Under-100-FTE firms dominate; their endpoint attenuates from about −16 to −9 log points with entropy balancing. Earlier trend fitting holds out 2022; a later cohort also declines. Recruitment is inferred from tenure stocks. Table 5's averaged-post small-firm coefficient is −0.051 (SE0.024); size interactions are +0.044 (SE0.035) or +0.064 (SE0.035). Authors explicitly disclaim causal identification.

The [institution's accompanying analysis](https://www.nationalbanken.dk/en/news-and-knowledge/publications-and-speeches/analysis/2026/artificial-intelligence-and-the-labour-market-the-transition-has-begun) explains that an employment shortfall from a projected trend can coexist with actual headcount growth. That distinction should survive every chart and mind-map summary.

### Independent audit: what strengthens the result, and what remains vulnerable

The following are analytical implications of the design, not additional author claims.

**The counterfactual is the main load-bearing assumption.** A firm-specific trend estimated during recovery from a large shock is not guaranteed to remain its no-AI path for several subsequent years. Industry-month effects absorb a shared sector shock; they do not absorb a demand slowdown, capital constraint, management change or restructuring plan that differs between adopting and non-adopting firms within that sector. A richer panel can make this comparison more precise without making adoption random.

**Pretrend diagnostics require separation from pretrend construction.** Residuals should look relatively flat over the window used to fit them. The more informative check is an untreated held-out period and sensitivity to the estimation window, not only a plot of fitted pre-period residuals. The reported held-out exercise is useful evidence. It does not prove that a later, adoption-correlated business strategy would be absent without AI. An event study of planned adoption, actual usage intensity and contemporaneous restructuring would help distinguish these possibilities.

**The timing is annual, while the outcome is monthly.** The data can show a monthly outcome path, but an annual first-use report does not provide the exact month of economically consequential adoption. Treating January as an event anchor is not evidence that all firms started then. Anticipation, shallow initial use and later integration can blur the apparent onset. The historic survey questionnaire and reference-period coding should be audited before making a month-precise causal chronology.

**“AI” is broader than a randomly assigned coding assistant.** A self-reported enterprise AI indicator can capture a family of tools and an organizational strategy. A strong text/code component does not isolate the effect of one chatbot or model. Changes in question wording or interpretation can create apparent adoption. The 2021 measure is not directly comparable to later waves; an exact historic-question reconciliation remains open.

**A control that later adopts is not automatically a conservative experiment.** If all subsequent treatments had the same direction and timing, contamination could attenuate a contrast. With heterogeneous effects, endogenous adoption and correlated plans, the direction of bias needs assumptions. A useful robustness package would show never-adopter controls, not-yet-treated comparisons with defensible timing, cohort-specific estimates and an explicit discussion of what changing the control population does to external validity.

**Tenure stocks support a recruitment hypothesis but do not identify hires and layoffs separately.** Fewer recent-tenure workers can result from fewer entrants, more departures of recent hires, altered retention or aging across tenure thresholds. Direct flow accounting is the closer oracle. The absence of a reduction in a long-tenure stock is not proof that nobody was dismissed. A careful summary is “consistent with reduced recruitment,” unless directly observed flows establish a stronger claim.

**Heterogeneity needs its own uncertainty assessment.** A significant coefficient in one subgroup and an insignificant one in another does not by itself establish a significant difference. The formal interaction and alternative weighting matter. Do not compare a late-month endpoint with an average-post-period coefficient as if they were the same estimand. The small-firm threshold is also a classification choice; sensitivity to nearby thresholds would strengthen a general size-channel claim.

**The accounting exercise is not a general-equilibrium experiment.** Reweighting observed micro contrasts can reveal why a sector exposure gradient overstates an adoption-specific component. It does not identify every spillover to competitors, prices, new entrants, consumers, suppliers or labor supply. A small aggregate signal might reflect a small affected group or measurement noise; it need not prove an offsetting job-creation mechanism. Conversely, a sizable relative firm effect does not imply the same percentage loss economy-wide.

### Paper-specific issues to retain in the evidence ledger

- The headline matched-sample count is not an interchangeable denominator for the baseline event-study cohort. Table 5 reports firm-month observations, not unique treated and control firms. Exact Figure 7 cohort counts were not located and should be requested from replication materials before a full replication claim.
- Table 1's firm counts imply approximately **16.2%** of its displayed universe, while nearby prose uses a “10% sample” shorthand. Use the counts and state the relevant denominator; do not repeat an unexplained percentage.
- Exact endpoint confidence limits were not digitized from the chart. The visual inspection establishes a negative band, not defensible three-decimal numerical endpoints. Computed normal intervals from Table 5 would refer to its averaged-post estimand, not the headline endpoint.
- The paper's quantile bootstrap explicitly conditions on first-stage pretrends estimated once. A replication should examine unconditional uncertainty by re-estimating generated trend components, where appropriate for the inferential target.
- Occupational reallocation can precede recorded adoption, leaving anticipation versus selection unresolved. This limits a clean “adoption caused reallocation” chronology.

## The earlier Danish null: a different treatment and selected population

**Verified methods card (main pp. 8–9, 18–23, 30–32; appendix B.1–B.2):** Humlum/Vestergaard survey **11 exposed occupations** and link outcomes through **December 2024**. The 2024 round invited 115,000 workers; **25,241 completed**, **24,796 linked** (21.6% of invitees). Workplaces were sampled within occupations; large-workplace sampling was adjusted. Main workplace treatment is **encouragement**, with enterprise tools/training variants; individual treatment is reported use. Controls may use tools without encouragement. Event time is ChatGPT's **November 2022** launch, not observed firm adoption month. Models use worker/workplace effects, occupation × time controls, predetermined characteristics and workplace-occupation clustered errors; pooled estimates add adopter trends. They report precise average earnings/hours nulls, generally excluding effects above **2%**; workplace early-career-share changes exclude about **0.33 percentage points**. Occupation-specific intervals are wider. The sampling frame requires employment in a target occupation at sampling; register links follow departures and coworkers as well. Exact adoption months are unavailable. Respondents differ from invitees in some characteristics despite response-quality checks.

### Independent interpretation

This is not a randomized encouragement experiment: employers choose their policies and workers report them. Its causal reading needs comparable untreated trajectories after controls, credible measurement and limited unmodeled spillovers. Worker fixed effects remove stable ability differences; they do not remove every changing opportunity or unobserved motivation. Survey-response incentives were randomized, but employer AI policy was not.

A comparison of encouragement at already-exposed workplaces can be small even if first adoption at a different set of firms matters. At the same time, that explanation should not be used to dismiss a precise null whenever it is inconvenient. A decisive comparison would harmonize firm versus workplace identifiers, industry and size, sampling eligibility, outcome definitions, treatment state and calendar window on the same data.

Its equilibrium model helps interpret the “missing intercept” but does not independently observe a no-AI economy. The model imposes structure on production, demand, labor prices and sorting. Agreement between several measured margins supports a bounded conclusion within those assumptions; it cannot rule out all shared macro effects or future changes. Occupational moves into higher-paying work can also cause greater AI use, rather than the reverse. They are not experimental returns to taking a course.

## Cross-study estimands: do not combine these into a vote count

| Primary evidence / version | Comparison and window | What the result can establish | What it cannot establish |
|---|---|---|---|
| WP223, Denmark, Sep2026 | Newly reporting enterprise AI users versus earlier non-users; monthly detrended FTE, through Sep2025 | Conditional firm/size employment patterns after recorded adoption | Randomized GenAI effect, direct layoff count, economy-wide loss |
| Humlum/Vestergaard, Denmark, Mar2026 | Use/encouragement groups around Nov2022; linked workers/workplaces through Dec2024 | Bound on particular differential average outcomes under identification assumptions | Every occupation/cohort unaffected; global or 2031 null |
| [Stanford Canaries, Aug2026](https://digitaleconomy.stanford.edu/app/uploads/2026/08/Canaries_August2026.pdf) | US ADP age × exposure headcount through Jun2026 | Large-sample descriptive divergence, especially young/exposed workers | Observed firm AI treatment or an identified causal 19% loss |
| [Yale Budget Lab, May2026 methods](https://budgetlab.yale.edu/research/what-we-do-and-dont-know-about-how-ai-affecting-labor-market), [Oct2026 tracker](https://budgetlab.yale.edu/research/tracking-impact-ai-labor-market) | US CPS exposed occupations versus synthetic comparisons; broad outcomes | Broad-group changes against a fitted comparison and their uncertainty | Highly powered early-graduate subgroups or effects hidden by opposing responses |
| [ECB SAFE, Mar2026](https://www.ecb.europa.eu/press/blog/date/2026/html/ecb.blog20260304~d9e34fc95f.en.html) | Euro-area firm use/investment and current hiring; 2025 survey cross-section | Conditional associations, including varying reasons for adoption | Adoption-caused job creation; identities or skills of actual hires |
| [Firm Data on AI, Mar2026 revision](https://www.nber.org/papers/w34836?utmCampaign=ApolloAcademy&utmMedium=AATraffic&utmSource=ApolloAcademy) | Executive-reported own-firm histories and three-year expectations in four countries | What sampled executives report and expect | Verified administrative treatment effects or reliable point forecasts |

An exposure score says which tasks may be affected; it does not specify adoption, substitution, complementarity or a whole job's feasibility of automation. A firm-level comparison can miss common shocks. A national comparison can miss narrow cohorts. A null can mean a small effect within a confidence interval, a weak treatment, mixed signs, poor timing or inadequate power. A non-null can reflect selection or a wrong counterfactual. Each interpretation needs evidence, not a preferred narrative.

## What would establish returns to learning?

The necessary chain has several separately testable links:

**training access → actual participation → acquired competence → retained/transferable competence → credible visibility → interviews or work access → sustained output/earnings net of cost.**

Randomizing one link does not identify all the others. A study of certificate sharing among graduates identifies a signaling intervention, not the return to enrolling. A study of assisted task performance does not identify unassisted skill. Higher salaries among AI adopters can reflect who adopts, where they work or what jobs remain. A job outcome can improve while earnings do not, and a move into a preferred sector can coexist with lower overall employment during transition.

### Direct learning experiment: coding assistance can impair immediate acquisition

[Shen/Tamkin, full primary paper](https://arxiv.org/html/2601.20245v1) analyzes **52 participants, 26 per arm**, learning unfamiliar Python Trio tasks under a 35-minute task limit, followed by an unassisted quiz. Four pilots preceded the preregistered main study; 53 completed and one met a preregistered exclusion. The immediate quiz difference favored no-AI (**d=0.738, p=.01**); average completion time did not differ significantly. Most were not necessarily junior programmers: they were new to Trio. The published table contains experience-count/percentage inconsistencies. The paper's “4.15 points on 27” and “17%” wording is also arithmetically inconsistent, while the [research blog](https://www.anthropic.com/research/AI-assistance-coding-skills) rounds scores to 50% versus 67%. Avoid a precise percentage headline; certainly do not call this 17% relative decline. Learning-style clusters are exploratory/self-selected, not randomized teaching treatments. Neither delayed retention nor long-term job competence was measured.

### Positive counterexample: a deliberately designed tutor can improve learning

[Kestin et al., Scientific Reports, May2025](https://www.nature.com/articles/s41598-025-97652-6) uses a crossover study in Harvard introductory physics: **194 eligible completers from 233 enrolled**, with each student experiencing structured AI tutoring and active class teaching for different lessons. Post-tests favored the tutor condition. Its package includes instructor-designed scaffolding, question-specific prompts, prepared answers and recorded material, rather than unrestricted answer generation. Completion-based inclusion, two lessons, one institution and immediate outcomes limit extrapolation. This is positive evidence for a particular learning design, not proof that generic chatbots, coding agents, delayed transfer or labor-market earnings improve.

### Actual training allocation: skill gains do not imply every employment metric rises

[World Bank WP9721, June2021](https://documents1.worldbank.org/curated/en/670761624977598623/pdf/Coding-Bootcamps-for-Female-Digital-Employment-Evidence-from-an-RCT-in-Argentina-and-Colombia.pdf) randomizes scholarship offers among **803 eligible women** in Argentina/Colombia: 402 offered, 401 controls. Follow-up reinterviewed **724**, with differential response (**93.3% versus 87.0%**), for which bounds are investigated. Adjusted intention-to-treat estimates include **+1.119/10 skill-test points** and **+6.7 percentage points** coding employment (SE3.1pp), against 24% control coding employment. But overall employment is **−7.2pp** (SE2.9pp) in a population already highly employed; treatment can alter participation and transition choices. Outcomes refer to only **2–5 months after completion**, measured retrospectively during COVID. A high-motivation selected female applicant population in 2019–20 is not a forecast for an employed Indian AI engineer in 2026. The scholarship/course package cannot isolate pure knowledge from signaling, peers or support.

### Credential visibility: useful evidence for signaling, not the training itself

[Athey/Palikot, v2 revised 5Nov2025](https://arxiv.org/abs/2405.00247) randomizes encouragement/friction reduction for sharing credentials among **800,000+ certificate earners**; employment is observed for about **40,000**. The revised abstract reports **+1.0pp / 6% relative** new employment and **+1.2pp / 9% relative** credential-related jobs. Earlier 2024 material said 8% for the latter; keep versions separate. Learners had already earned certificates before intervention. Thus this is evidence that visibility can help selected graduates, especially those with weaker conventional credentials. It does not randomize training, establish a course's skill value, or justify buying a credential. Instrumental-variable interpretation of sharing additionally needs exclusion and compliance assumptions; reminders could affect other job-search behavior.

## Equilibrium and displacement: private success is not net job creation

As a matter of economic accounting, lower labor required per unit of output can be offset by greater output, new products and tasks, or shifted between firms. Profits, prices, hours, wages and employment are distinct adjustment margins. A company can expand because it captures competitors' customers without expanding economy-wide jobs. A worker can win an interview because a signal improves ranking without creating another vacancy. None of these mechanisms determines the sign without elasticities, timing and market institutions.

There is direct experimental reason to take this distinction seriously. [Crépon et al., published QJE2013](https://www.nber.org/papers/w18597) randomized job-placement programme saturation across **235 French local labor markets**, then randomized individuals within them. Direct short-run placement gains came partly at other eligible workers' expense, with little net benefit. This is old job-search assistance evidence, not an AI or coding-training result. Its methodological lesson is the value of measuring untreated people and varying treatment saturation, rather than assuming an individual gain scales linearly to everyone.

For AI employment, a stronger equilibrium audit would observe entrants/exits, output/prices, workers moving between adopters and non-adopters, hours and wages, and demand spillovers. For training, it would measure untreated competitors and employer hiring as well as participants. The absence of a clear aggregate signal cannot, by itself, identify either offsetting creation or no damage.

## Implications for learning and entry gates

These are proposed decision rules, not experimentally validated intervals or promises of mastery.

1. **Separate delivery mode from learning mode.** Use tools to deliver where appropriate, but deliberately schedule exercises where the target skill must be demonstrated without answer generation. The test is whether the learner can explain, diagnose and repair, not whether a polished artifact exists.
2. **Measure retention after a delay and transfer to an unfamiliar task.** For a new concurrency library, later debug a fresh race/cancellation failure in unseen code; for evaluation, repair a misleading metric or leakage problem in another dataset; for robotics, explain a failure under changed timing/calibration. Testing after a week and again later is a practical proposal, not a proven optimal schedule.
3. **Test both tool-free judgment and assisted operating skill.** Memorizing every API is unnecessary; inability to recognize a forbidden action, wrong invariant or bad experiment is consequential. A test can permit normal reference documentation while withholding a generative solution, then separately measure safe tool use.
4. **Get independent review.** Predetermine an oracle and a rubric; do not let the same assistant generate the solution, define success and grade the result without audit. Include intentionally incorrect solutions and novel failure cases to test supervision.
5. **Treat a portfolio as evidence plus a signal.** Make permitted results inspectable and reproducible, record assistance and limitations, and explain outcomes. Visibility may help; it does not compensate for an inability to defend the work. Private employer code needs permission before public use.
6. **Require market access evidence before expensive specialization.** Confirm hard location/credential filters and actual adjacent roles, then compare study cost, foregone earnings and fit. No paper here identifies the return to a robotics degree, a cloud certification or an ML course for this user.
7. **Escalate the gate as responsibility grows.** Move from bounded unseen exercises to authorized production operation, novel problem diagnosis, reviewed system decisions and other engineers adopting the work. Leadership evidence is sustained contribution and judgment, not elapsed years or tool count.

## Explicit unresolved items and falsification targets

- **Resolved:** WP223 full-paper access, main matched denominator, trend/control definitions, weighting/clustering, key sensitivity and tenure-channel interpretation; revised Humlum treatment/sample/uncertainty.
- **Unresolved:** exact WP223 baseline adopter/control firm counts; historical verbatim adoption-question wording and wave/reference-date reconciliation; exact numerical Figure7 endpoint intervals; executable replication/material access and full first-stage uncertainty propagation. No claim of replication is made.
- A same-data, same-window comparison of encouragement versus first adoption, with harmonized firm/workplace definitions and outcomes, would be more decisive than comparing headlines.
- Stronger evidence for training returns would randomize training access or credible eligibility near a cutoff, independently measure delayed transfer, retain nonparticipants in analysis, address attrition, track administrative earnings and report total costs. A factorial design separating instruction, credential and employer access would clarify mechanisms.
- The actionable hypothesis is that retained foundations plus verified systems and useful visibility improve options. It should be revised if independent tests show no competence transfer, if relevant demand/access fails, or if the incremental investment has unacceptable opportunity cost. There is no evidence-based fixed timetable to “master everything by 2031.”
