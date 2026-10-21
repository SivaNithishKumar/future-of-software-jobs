# One measured building-control deployment: effect, native automation and work boundaries

This closes part of the field-outcome gap: an open MPC toolchain actually controlled office HVAC and produced a reported energy benefit. It does **not** close the route to accessible paid developer work. The evidence is one historical site, a particular baseline and transition season, with substantial implementation effort and automatic fallback already doing useful work.

The selected paper is **David Blum, Zhe Wang, Chris Weyandt, Donghun Kim, Michael Wetter, Tianzhen Hong and Mary Ann Piette**, *Field demonstration and implementation analysis of model predictive control in an office HVAC system*, **Applied Energy 318 (2022), 119104**, DOI `10.1016/j.apenergy.2022.119104`. This is MPCPy/ALC, a comparable open supervisory-control study—not evidence that VOLTTRON was deployed at this site. A similarly titled Kim paper was not merged into it.

## What actually operated

| Unit | Reported scope |
|---|---|
| Asset | LBNL Building 59, Berkeley; two office floors, 6,038 m²—not the whole NERSC computing centre |
| Equipment | Four rooftop units, 50 underfloor terminals, 16 added core-temperature sensors |
| Period |18 October–15 December 2020; 31 MPC-on and 27 off days, approximately alternating weeks with maintenance exceptions |
| Context | Mild transition season; significantly lower COVID-period occupancy |
| Result | Estimated 40% HVAC-energy reduction, mostly fan savings on mild days |
| Effort | Estimated 239 person-days: 70 preparation, 79 model/integration, 30 controller software and 60 deployment |

These are related days/equipment within one building, not independent sites. The paper's [archived full text](https://escholarship.org/content/qt89d820hb/qt89d820hb_noSplash_c061629d521f5c1ff05be15fbb57ff8b.pdf?t=rf7zyh) supplies the methods; the [lab record](https://eta-publications.lbl.gov/publications/field-demonstration-and) matches its authors, DOI, volume and article number.

## What 40% means

The estimate comes from integrating fitted daily-energy/outdoor-temperature curves for the two control modes. Energy combines electrical-panel measurements with reheat heat flow divided by an assumed heat-pump COP 2.0. It is not 40% whole-building energy, peak demand, carbon or tariff saving. Comfort is a zone-averaged temperature-deviation measure; some individual-zone temperature extremes differ. Those measurement choices and scope are retained in the JSON's exact source locators. [Study, Section 5, Eqs 24–25](https://escholarship.org/content/qt89d820hb/qt89d820hb_noSplash_c061629d521f5c1ff05be15fbb57ff8b.pdf?t=rf7zyh)

This is stronger than a controller simulation or unadjusted anecdote: real physical measurements, existing-control periods and temperature adjustment support a meaningful site-specific positive. It remains a nonrandom switchback-style comparison. Week order, occupancy, equipment state and maintenance can differ; temperature adjustment does not settle all those counterfactuals. No confidence interval or all-attempt statistical recalculation was verified here.

The relevant alternative is important. Existing sequences had few schedules/resets and had to protect 24-hour IT-room cooling with limited core feedback. The result does not establish superiority over a well-configured modern native sequence given equal sensing and information. The added observations, operator constraints and baseline headroom are part of the intervention's context, not a reason to dismiss its actual benefit. Annual, hot-climate or other-building transfer remains a separate question.

## Native automation and failure handling

MPCPy generated core optimisation problems. Ordinary database/services and existing BMS privilege checks, range/ramp checks, operator override and watchdog fallback handled part of reliable operation. Communication, server, weather-feed, account and equipment incidents were reported; the appendix also identifies failed parameter estimates and a server-building power shutdown. The record is not a complete event/repair-time denominator, so no availability rate follows. [Study, Sections 4, 6 and Appendix](https://escholarship.org/content/qt89d820hb/qt89d820hb_noSplash_c061629d521f5c1ff05be15fbb57ff8b.pdf?t=rf7zyh)

Preserve one timing uncertainty: the integration description says a 20-minute watchdog window, while incident narratives describe 10-minute fallback. No configuration history was recovered to reconcile them. This is not a paper-error finding or an instruction to operate a building. Likewise, soft comfort penalties and feasible optimisation do not prove every comfort bound or safety requirement was met.

This native positive cuts against a generic custom controller/platform proposal. The field implementation already used automatic formulation, reusable infrastructure and automatic reversion. Authors also identify further equipment-fault response that could be automated. Historical integration effort does not reserve a permanent human role; improved native tools may remove a proposed custom residual.

## Real work, incomplete economics

The person-day table is retrospective project estimation, not payroll or controlled productivity measurement. It excludes developing MPCPy itself and includes management only for key coordination meetings. Reuse and experience can change the next site's burden. Do not convert 239 person-days into FTE vacancies, an implementation quote or an income forecast. The study acknowledges DOE-supported research and facility/data access; that is a real funded research setting, not an open individual contract or India-eligible employer route.

What the case concretely demonstrates is the need, at this site, time and tool version, for source/API interpretation, forecast-vintage storage, service recovery, BMS integration and commissioning. Its storage design separates forecast creation time from forecast-valid time, which enabled as-issued replay. That is relevant software evidence. It does not establish how much of that work remains unmet today, who would accept a new contribution, what a complete commercial project costs or whether anyone is hiring for it.

An admissible opportunity needs the next links: a current owner-specific residual beyond competent native controls, an independent expected outcome, accepted maintained value and a funded eligible responsibility. If native controls meet the same legitimate outcome at lower complete burden, extra custom work should stop. If permission, representative data, physical reference or an accepting receiver is missing, source-only understanding can remain useful while stronger operating claims stay blocked.

No 30/90 exercise, keys or hours are added here. The existing energy-vintage project's market-publication/as-of contract is not a building-control project simply because both use timestamps. No state/control/workflow cap is transferred. Actual credentials, onsite access, geography and UK/India work rights remain unassessed.

## Access, version and replication limits

Three distinct primary surfaces were attempted: lab metadata, publisher route and the exact public archive PDF. The publisher returned a reader-reported 403. Direct archive open failed, but the **same exact PDF URL's indexed reader** returned 22 pages / 1,951 lines and the selected methods/results/appendix. That is a different reader/cache access outcome, not a fourth source or binary download. Two tightly targeted metadata queries located identity and the authorised archive fallback; no unrelated paper/profile was opened.

The archive header matches the journal-layout identity and declares article CC BY 4.0. Publisher byte identity was not checked. MPCPy's short paper commit `ecb9833` is not a complete current runtime lock. The paper points to an open before/during/after dataset, whose actual release, licence and completeness were not inspected. Article rights do not grant code, device data, building access or actuation authority. No code, data, model, accounts, controls or native solver ran. Existing round 58, source-index and project records remain unchanged.

This is one historical field-methods audit, pending different review and root disposition—not final career/source-currentness/rights/UI acceptance.
