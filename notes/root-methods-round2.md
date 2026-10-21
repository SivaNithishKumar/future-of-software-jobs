# Root methods and regional evidence audit

19 October 2026. This pass addresses distinct unresolved questions, rather than repeating the sector scans. Findings remain inputs to the final synthesis.

## BIS 1325 is conditional evidence about earlier firm technology adoption

[Official full paper, 23 January 2026](https://www.bis.org/publications/working-paper-1325-ai-adoption-productivity-and-employment-evidence-european-firms.pdf), sections3–5 and Tables2–3. Pooled2019–2024 EIBIS/ORBIS data; survey category combines big-data analytics and AI. The controlled matched-regressor productivity specification has30,228 observations. The US-matched adoption variable is a majority vote among five nearest neighbours, followed by pooled OLS with controls/fixed effects and US-resampling bootstrap. Authors call the strategy IV and invoke conditional independence; it should not be casually described as a randomized adoption experiment or a conventional documented first-stage2SLS design.

Table3's controlled employment estimate is−0.012 withSE0.010,30,446 observations. Failure to reject zero does not establish an exactly zero effect. A rough normal approximation spans−0.032to+0.008 log points, approximately−3%to+1%; that is an analyst calculation, not a reported equivalence interval. Global shared shocks remain a concern even with observable balance and alternative fixed effects. The study does not identify effects of2026agents or2031career returns. Table2's printed significance stars merit checking against coefficients/SE before reproducing a precise p-value.

**Implication, our inference:** keep this as a competing conditional firm-level result. It cannot settle a claim about junior developers, job creation in India, or the wage return from learning a particular tool. Newer adoption-linked and task-level studies may legitimately disagree because the treatment, population and time window differ.

## India services firms are a comparator, not one homogeneous labor market

[TCS Q2FY27 primary release,8October2026](https://www.tcs.com/who-we-are/newsroom/press-release/tcs-financial-results-q2-fy-2027) reports quarter revenue$7.642bn, workforce598,056 and annualized AI revenue$3.1bn. The latter is an annualized company-defined measure, not a completed-year independently comparable AI market statistic. Announced transitions of client capability centers and acquisitions also complicate inference from headcount. Revenue, staff stocks, gross recruitment, employee mix and productivity per accepted outcome remain different quantities.

[Infosys investor page checked19October](https://www.infosys.com/investors.html) schedules Q2FY27 results for23October, still in the future. Use [its current FAQ](https://www.infosys.com/investors/shareholder-services/faqs.html) only for the dated June30 employee figure328,062 and Q1FY27 financial data. Do not accidentally substitute October2025 Q2FY26 for current results.

[Infosys/Truist announcement,19October2026](https://www.infosys.com/newsroom/press-releases/2026/collaboration-build-global-capability-center-india.html) describes an AI-first Hyderabad capability center collaboration. This is issuer-reported collaboration evidence. It does not disclose a general developer hiring probability, employment multiplier or a quantified accessible vacancy pool.

**Implication, our inference:** compare product companies, services, industrial suppliers, GCCs and research organizations as distinct routes. A company can expand AI revenue while reorganizing roles or concentrating responsibility. Avoid concluding either inevitable services collapse or protected growth from a few aggregate observations.

## Training returns require independent transfer checks

The coding-skillsRCT audit in software.md and labor-round3-methods.md concerns52 programmers learning an unfamiliar library, not a representative population of junior developers. Immediate quiz outcomes cannot establish long-term skill atrophy. Reported percentage summaries and raw-score denominators differ; use the narrow supported result and effect statistics rather than reconciling incompatible rounding into a false precise percentage. Self-selected interaction styles do not establish the causal benefit of a particular prompting strategy.

**Preparation consequence, our inference:** a project should test whether the learner can explain an unfamiliar failure, modify the design, and solve a held-out problem without model assistance. This is a proposed learning gate, not proof that unaided work is always economically preferable. A credible career experiment measures both useful delivered work and independently retained understanding.

## Closed checks and remaining gaps

Closed: BIS full source located; data period/adoption definition/regressor construction and employment denominator inspected. Closed: current TCS release and future Infosys reporting date checked. Closed: government and trade acronyms must be resolved before interpreting search hits; initial RBI results about general credit cards/Gulf states were irrelevant and discarded.

Open: independent assessment of BIS inference and printed-star consistency; current full NASSCOM2026 methodology and employer coverage; revenue/headcount decomposition that controls acquisitions and role mix; credible causal evidence for attainable skill returns. These remain distinct from the Nationalbank employment paper owned by labor_market and the technical learning mechanisms owned by software_ai.
