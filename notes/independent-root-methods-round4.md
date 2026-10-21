# Independent audit of root-methods-round2 — round 4

Checked 19 October 2026. Assignment: challenge the root interpretation of BIS Working Paper 1325, then verify only the necessary dates/definitions in its TCS/Infosys examples. This is independent validation, not an independent dataset replication or an additional labor-market survey. The Nationalbank paper was excluded because labor_market owns it.

## Verdict

The root's cautious interpretation is substantially sound. Its employment interval arithmetic is correct. Its warning about Table 2 stars is justified and can now be made precise: one inconsistency survives rounding. However, neither that reporting error nor the unusual estimator proves the whole study wrong. The final synthesis should retain the result as conditional firm-level evidence, distinguish the authors' causal claim from what this audit could establish, and avoid converting it into a forecast of individual careers.

Two refinements are needed: describe the residual global-shock concern more precisely given the fixed effects, and avoid assuming every displayed US-matched regression uses the same bootstrap standard-error procedure.

## Exact source and visual verification

Primary paper: [BIS official PDF](https://www.bis.org/publications/working-paper-1325-ai-adoption-productivity-and-employment-evidence-european-firms.pdf), January 2026; [official publication record](https://www.bis.org/publications/working-paper-1325-ai-adoption-productivity-and-employment-evidence-european-firms), 23 January 2026.

Relevant locations in this **36-page PDF**:

- Data: printed pp. 5–6 / PDF pp. 8–9.
- Matching/estimator: printed pp. 11–14 / PDF pp. 14–17; especially Equation (1) and notes 5/7/8.
- Bootstrap and note 9: printed p. 15 / PDF p. 18.
- Productivity Table 2: printed p. 16 / PDF p. 19.
- Employment Table 3 and its note: printed p. 17 / PDF p. 20.
- Alternative fixed effects and standard errors: printed pp. 30–31 / PDF pp. 33–34, Tables B.2/B.3.

The public PDF was retrieved into `/private/tmp/bis1325-independent-audit.pdf` for read-only inspection, extracted with existing `pdftotext`, and Tables 2/3 rendered with existing `pdftoppm`. Both complete table images were viewed; the stars, signs, standard errors and footnotes below are visible in the PDF, not just text-extraction artifacts. Temporary table images: `/private/tmp/bis1325-table-19.png` and `bis1325-table-20.png`. Retrieved PDF SHA-256: `449d93cf11c569885ffefd259521422f19b59721a3f06493ac5ccc4288a56512`.

The [EIB Working Paper 2026/02 PDF](https://www.eib.org/files/publications/20250383-130126-economics-working-paper-2026-02-en.pdf) contains the same main displayed values and methods. It is another official edition of the same research, **not an independent replication**. Its cover metadata is January 2026 and its internal manuscript date is 8 December 2025. No corrected/revised table was found in this bounded search; absence of a found revision is not proof none exists.

## 1. Data, treatment and estimator: what the root got right

Compact source facts: the paper pools 2019–2024 EIBIS observations matched to ORBIS. Adoption combines big-data analytics/AI and counts use in part or all of a business. Within sector/size strata it uses four matching covariates and five US neighbours; their majority label replaces actual adoption in Equation (1). It then estimates pooled OLS with controls/fixed effects. The controlled productivity/employment samples have 30,228/30,446 observations. [BIS, sections 3–4 and Tables 2–3](https://www.bis.org/publications/working-paper-1325-ai-adoption-productivity-and-employment-evidence-european-firms.pdf).

The root correctly calls these **observations**, rather than that many distinct firms or a panel adoption experiment. A stratified random survey is not random assignment of AI. Nor does this historical broad technology category isolate generative agents used in 2026.

The text calls its approach an IV/two-stage strategy. The displayed equation and majority-classification rule do not document conventional 2SLS: there is no shown regression of actual EU adoption on the proposed instrument followed by an identified fitted-adoption second stage, nor a reported first-stage scaling/relevance diagnostic for that construction. Root's phrase “not a conventional documented first-stage 2SLS design” is appropriately narrow. Do not replace it with “the authors secretly ran the wrong estimator”; code/data or an author derivation would be needed to settle implementation and estimand.

### Why the distinction matters: independent algebra

For a simple constant-effect model, after partialling out controls, let actual adoption be D, a proposed instrument Z, outcome Y = τD + u, and assume Cov(Z,u)=0. Regressing Y directly on Z gives:

`b_reduced_form = Cov(Z,Y) / Var(Z) = τ × Cov(Z,D) / Var(Z)`.

A treatment-effect IV estimate divides by the first-stage slope. A thresholded majority prediction is not automatically the same object as a properly calibrated fitted value. Without extra calibration/transport/structural conditions, direct regression on the proxy cannot simply be read as τ. This is a logical illustration, not a re-estimate of the paper or proof its coefficient has a known bias direction.

Similarly, matching observable distributions checks overlap/balance; it cannot establish the exclusion restriction or the absence of unobserved selection. A conditional-independence/transportability assumption needs to connect the constructed US label to EU potential outcomes, rather than follow merely from geography. This is an identification question, not evidence the observed association is fabricated.

## 2. The root's global-shock warning needs a narrower mechanism

Country-sector-wave effects already absorb additive shocks common to firms in the same cell, including ordinary shared sector/time shocks. It would overstate the criticism to imply these effects do nothing about global conditions. Table B.2 also varies the fixed-effect structure; root correctly acknowledges the robustness checks.

The remaining concern must instead be explicit: unobserved firm characteristics, or heterogeneous responses **within** those cells, may relate both to the matching label and to outcomes. Different macro institutions do not automatically make a US-adoption pattern independent of EU firm-level demand, technology-readiness or management effects. Alternative fixed effects can reduce a concern without proving exclusion.

Also unresolved from the written description: whether matching is restricted to the same wave; the exact propensity-score response model/overlap handling; repeated-firm treatment in resampling; timing of matching covariates relative to adoption; and whether survey weights enter every stage. These are replication questions. Contemporaneous matching variables could themselves reflect adoption, but this audit has not established their actual timing or the resulting bias.

## 3. Bootstrap: real uncertainty, not a blanket invalidity verdict

The described main procedure resamples US firms within strata 500 times, rematches and refits while EU observations stay fixed. That propagates variation in the transferred regressor. It does not, just by being called a bootstrap, demonstrate that all uncertainty relevant to a European-population causal estimand has been included. [BIS printed p. 15](https://www.bis.org/publications/working-paper-1325-ai-adoption-productivity-and-employment-evidence-european-firms.pdf).

**Independent reasoning:** a variance calculation must identify what is random and what is conditioned on. If rematching leaves a transferred regressor unchanged, a US-only bootstrap could return no variation even though repeated EU outcome samples would change an OLS estimate. That illustrates why source-sample uncertainty and EU outcome/sampling uncertainty are different components. It is not evidence this paper actually obtained zero standard errors. A conditional finite-EU/design-based target might justify different conditioning; the relevant derivation and implementation were not available here.

Nearest-neighbour matching also raises a separate technical issue. Abadie/Imbens show that ordinary bootstrap inference can fail for a particular class of fixed-neighbour matching treatment-effect estimators. That theorem is a reason to require justification, **not a proof that it applies unchanged to this paper's transferred-classifier-plus-OLS estimator**. [Primary methods paper](https://economics.mit.edu/sites/default/files/publications/ON%20THE%20FAILURE%20OF%20THE%20BOOTSTRAP%20FOR.pdf), [author/NBER record](https://www.nber.org/papers/t0325).

The root should therefore say “inferential target/procedure requires clarification,” rather than declare the standard errors invalid or the result refuted.

**Table-specific point:** Table 2's note identifies bootstrap errors for columns 3/4. Table 3's note instead says errors are clustered at country-sector-wave level. It may deliberately use a different procedure, or reflect incomplete table documentation; the code is needed. The displayed employment SE can be used for a labelled rough calculation without asserting it came from bootstrap draws.

## 4. Stars and confidence intervals: checked arithmetic

Using rounded printed values and a two-sided normal calculation:

| Location | Printed b / SE / stars | Calculated z / p | Assessment |
| --- | --- | --- | --- |
| Table 2 col. 4, US-matched productivity | 0.041 / 0.019 / *** | 2.1579 / 0.03094 | Does not match the printed 1% convention |
| Table 2 col. 2, actual productivity | 0.028 / 0.011 / *** | 2.5455 / 0.01091 | Rounding could put the unrounded statistic below 1%; not a definite error |
| Table 3 col. 4, US-matched employment | −0.012 / 0.010 / no stars | −1.2 / 0.23014 | Displayed nonsignificance is consistent |

For Table 2 col. 4, allowing each printed value to have ordinary three-decimal rounding gives z approximately 2.077–2.243 and p approximately 0.02488–0.03781. Rounding cannot rescue *** at 1%. Note 9 explicitly mentions normal-approximation significance. An unreported empirical-bootstrap p-value, a typographical error or stars carried from another SE calculation might explain the discrepancy; they cannot be selected as fact without additional evidence. Table B.3 prints the same turnover coefficient/sample with a different SE, illustrating why table-specific inference matters.

This is a **verified internal reporting inconsistency**, not proof of no productivity relationship: from the displayed values the positive estimate remains conventionally significant at 5%. It would be wrong for the final report to reproduce “p<0.01” without qualification.

Root's employment calculation checks out:

`−0.012 ± 1.96 × 0.010 = [−0.0316, +0.0076] log points`.

Exponentiating the endpoints gives roughly **−3.11% to +0.763%**. Root's rounded “about −3% to +1%” is fair. It is an analyst normal approximation from rounded SEs, not an author-reported bootstrap, equivalence or population-valid confidence interval. Failure to reject zero does not establish zero effects, and uncertainty about identification/inference is not captured by this arithmetic alone.

For context, the displayed productivity coefficient's analogous normal interval is [0.00376, 0.07824], or approximately +0.38% to +8.14%. Its exact exponentiated point is +4.19%; referring to about 4% is reasonable. Avoid presenting either endpoint set as more exact than the source and assumptions allow.

All calculations are saved in `root-methods-round4-calculations.json` and were independently executed with Python standard-library `math.erfc` / `expm1`. No source data or regression code was accessed; this is numerical checking, not replication.

## 5. TCS / Infosys: dates and definitions independently check

The root's dates/numbers are supported by the current official pages. TCS's release is dated **8 October 2026**, covers quarter ended **30 September 2026**, and prints revenue **US$7,642m**, workforce **598,056**, and **US$3.1bn annualised AI revenue**. The annualised figure is not US$3.1bn earned in that quarter or an independently standardised sector measure. [Official TCS release](https://www.tcs.com/who-we-are/newsroom/press-release/tcs-financial-results-q2-fy-2027).

One temporal refinement: proposed acquisitions and transition announcements should not be assumed already consolidated into the quarter's workforce. The release says the Porsche/MHP transaction remains subject to approvals. Root's general request to decompose headcount is sound; no causal headcount explanation has yet been established.

Infosys's current official investor page schedules Q2 FY27 results for **23 October 2026**, after this check. Its FAQ lists group employees **328,062 as of 30 June 2026**, with Q1 FY27 financial data. The investor page itself dates the Truist/Hyderabad collaboration item **19 October 2026**. The direct press-release endpoint failed in this pass; its official investor listing independently supports the narrow date/description. [Investor page](https://www.infosys.com/investors.html), [FAQ and result calendar](https://www.infosys.com/investors/shareholder-services/faqs.html).

No company announcements here identify an individual hiring probability, net job multiplier or causal effect of AI on employment. The root does not claim otherwise.

## Required final-synthesis changes

- Keep the broad technology period, pooled firm-level outcome and observational identification boundary visible; do not label it a generative-agent experiment.
- Attribute “causal” to the authors and describe our independent concerns separately. Report a positive conditional estimate and an employment estimate consistent with a range around zero, rather than treat the paper as proof either of guaranteed employment protection or of job destruction.
- Correct the significance description: the displayed main productivity b/SE imply roughly p=.031 under the paper's stated normal convention, despite ***. Do not imply every star is demonstrably erroneous.
- Do not call the employment interval a bootstrap interval or an equivalence finding. Root's rough arithmetic itself is not wrong.
- Narrow the shared-shock criticism to channels not absorbed by the stated fixed effects. Acknowledge robustness checks without treating them as proof of identification.
- Treat the bootstrap/estimator questions as unresolved methodology requiring derivation/code; the current evidence does not justify a sweeping rejection of the study.
- Preserve the India services/GCC/product/industrial/research segmentation. TCS/Infosys date and metric checks support contextual examples, not 2031 career forecasts.

The valid personal preparation implication remains modest: test useful delivery and independently retained understanding on real tasks, diversify evidence beyond one study, and do not infer the wage return of learning a particular tool from a firm-level adoption coefficient.
