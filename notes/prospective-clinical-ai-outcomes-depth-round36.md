# CoMET PM-IMPACCT: prediction, deployment and patient outcome are different claims

This is a bounded research-methods audit, not medical advice or clinical authority. It examines one previously uncovered 2026 prospective deployment report, with an important access limit: the **2021 published protocol was directly readable; the 2026 results were available only through a substantial indexed primary-source extract**. The publisher redirected to an inaccessible authorisation page and direct/cached-find PMC reads showed a browser challenge. No challenge was solved, and full Table 2 effects/confidence intervals, registry history, amendments and correction status were not verified.

The [2026 results paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC12923516/), *A randomized controlled trial of artificial intelligence-based analytics for clinical deterioration*, appeared in Scientific Reports on 5 February 2026, DOI `10.1038/s41598-026-39051-z`. Its indexed report describes no statistically significant improvement in the primary outcome. That is a source-qualified finding, **not** verified equivalence, effect zero, safety, harm or absence of benefit from clinical AI generally. No exact treatment-effect estimate is invented here.

The [directly read protocol](https://pmc.ncbi.nlm.nih.gov/articles/PMC8285742/), Jessica Keim-Malpass and colleagues, *Predictive Monitoring–Impact in Acute Care Cardiology Trial (PM-IMPACCT): Protocol for a Randomized Controlled Trial*, was published 2 July 2021, DOI `10.2196/29631`. It links NCT04359641. The results report registration on 24 April 2020, before the reported January 2021 start, but the registry/history itself was not opened. Publication of the protocol after start does not by itself establish late registration; nor does a reported registration date verify every prespecified analysis.

## What was randomised and measured

This is a single-hospital, room/bed-cluster trial across three acute cardiac medical-surgical wards, not individual randomisation or a representative sample of health systems. The protocol covers 85 beds, with clusters rerandomised every two months. All admitted patients were eligible under its pragmatic design. Usual care included clinically ordered monitoring; the intervention added the CoMET risk display, charted scores, education and discussion. No particular clinical response was mandatory. Staff could see which beds had displays.

The indexed 2026 report describes 10,422 **visits**, rather than necessarily that many unique people, and repeated-admission correlation was modelled. It reports 5,242 display-on and 5,180 display-off visits in the January 2021–October 2022 period. The population was mostly older, male and White; some beds had been repurposed for transplant care. These are scope facts, not evidence of performance in every ward, country or subgroup.

The protocol's primary endpoint is hours free of defined deterioration within 21 days. It awards 504 hours to uncomplicated early discharge and zero to in-admission death; planned/nonemergent or allocation-changing transfers censor follow-up. Consequently the score is **protocol-defined outcome coding**, not literal continuous observation of 504 event-free hours after every early discharge. Clinical urgency and ambiguous event status required trained adjudication. A valid EHR resource or timestamp cannot supply that clinical judgement.

## Prespecification and censoring need careful reconciliation

| Directly read 2021 protocol | Indexed 2026 report | What can be concluded here |
|---|---|---|
| Fourteen clusters; approximately 20 months planned | Eleven clusters; period described as 22 months | Exact amendment/design reconciliation remains open; this is not an established error |
| Estimated 10,424 admissions, 80% power, anticipated 11% attrition | 10,422 visits and a lower-than-expected event rate discussed | Near-complete planned N does not independently establish actual power or exclude a clinically important effect |
| Poisson-link GEE proposed for the primary endpoint | Zero-inflated negative-binomial GEE reported | A model/SAP change to reconcile, not proof that either model was inappropriate |
| Transfer/room-allocation changes explicitly anticipated as censoring | Clinicians reportedly moved sicker patients towards display beds | Transfer was not unforeseen; anticipating its frequency does not remove informative censoring |

The protocol includes an interim spending plan and a DSMB. Its published power section does not let this audit reconstruct the assumed effect, correlation structure or actual post-pandemic precision. Full estimates, confidence intervals and sensitivity analyses remain needed before making stronger absence-of-benefit claims.

The indexed narrative reports 382 usual-care-to-display and 419 display-to-usual-care moves, while its abstract uses an 11% transfer statement. Those figures are **not merged into a new censoring percentage here**: directional moves, participants/visits, epoch switches and other censoring reasons may have different denominators, and full Table 2 was not accessible. The anticipated 11% attrition and the results' reported transfer fraction also should not be treated as the same quantity without checking their definitions.

There are two causal issues to preserve. Assignment to a display room is different from subsequent exposure or a clinician-directed transfer. Censoring after risk-directed movement can depend on a patient's evolving condition, so an “all randomised” analysis description does not guarantee complete follow-up or noninformative censoring. The authors suggest movement/censoring could bias towards a null finding; this audit cannot verify its direction or magnitude. An as-treated comparison or a post-hoc rising-risk subgroup does not automatically restore randomisation.

The report's at-risk subgroup was explicitly exploratory, not a successful prespecified primary endpoint. Its apparent movement/usefulness patterns can motivate implementation research without proving patient benefit. The result remains useful evidence about this display-and-education care pathway, with the above uncertainty; it is not a verdict on every early-warning system.

## Implementation, harms and work burden

This was more than a retrospective model score. The directly read protocol describes hospital interface-engine integration, display updates every 15 minutes, hourly EHR score flow, clinical champions, rounding support and more than 50 education sessions reaching over 120 clinicians at that stage. These provisions support a real deployment experiment and show why “AI model available” is not the whole intervention.

They do not establish that the intervention saved staff time. Response processes, costs, alerts and workforce burden were planned as additional analyses; the available results excerpt says further analyses would be reported separately. DSMB monitoring is not a completed proof of safety. Exact harms, subgroup effects, workload savings, resource costs and longer-term outcomes were not verified here. A null primary comparison should not become an unsupported statement that implementation was harmless, harmful or economically worthless.

The protocol also shows why prediction and causal utility differ. A score can discriminate risk while its display does not change outcomes in the tested workflow. Conversely, a workflow may change measurement, recognition, transfer or censoring. Observation, clinician order, chart entry, ingestion, score generation, display availability, action and outcome have distinct information times. This is a general validation guard; no future-data leakage or coding defect in CoMET was demonstrated by this pass. Its reported model/qSOFA comparison belongs to separate work and was not reproduced.

## A legitimate guard for the existing interoperability artifact

The only proposed software binding is an **unapplied reporting/information-time guard** on `health-r12.synthetic-reconciliation`, at `/project` in the frozen health-interoperability proposal. Its existing nonclinical snapshots, 24 development cases, eight withheld permutations and original hours remain unchanged. No clinical project, extra cases, patient data, model, clinical endpoint scorer or new budget is created.

Keep four statuses separate: structural/profile validity, source/identity/unit/state correctness, as-of information availability, and clinical-outcome verification. For the existing nonclinical Observation revisions, an older effective time must not make a later-issued/ingested revision appear known in an earlier as-of view. Preserve the effective, issued, ingested and view times, revision and unknown-availability reason. If selected, one existing revision/state case can express this within the original case contract, rather than add a separate trial simulator.

Compare the existing native parser/profile validator, applicable native custom constraints and ordinary explicit field-map/SQL projection on the same source versions and as-of view. Check configured native behaviour before alleging a missing capability. The independent expectation remains the existing nonclinical field/state/time table; no source case shown to its author becomes fresh validation automatically.

Do **not** infer clinical deterioration, emergent status, censoring, trial allocation or patient benefit from schema-valid FHIR. Do not introduce CoMET scores, alert thresholds, medical codes or actual trial populations. If the proposed guard requires clinical adjudication or patient data, stop that arm and retain generic reconciliation work. If the mature native path already handles it, reuse/document that behaviour or a real minimal regression. This could demonstrate software provenance discipline, not clinical competence or a paid role.

## Rights, people and access

The directly read protocol is CC BY 4.0 with its citation requirements. The indexed results header states CC BY-NC-ND 4.0; this report does not reproduce or adapt its figures/tables. The indexed data statement says data are not public and mentions reasonable-request replication. That is neither data access nor permission; no request was made. No code/weights/runtime grant was inspected, and a company affiliation alone establishes neither an open nor a proprietary software licence.

Public professional discovery is limited to the linked publications and the protocol's registry link. Named investigators include Jessica Keim-Malpass, Sarah Ratcliffe, J. Randall Moorman and Jamieson Bourque. The 2021 protocol names UVA and AMP3D; the 2026 indexed affiliations include UVA and Nihon Kohden Digital Health Solutions. Those clocks and identities are not silently merged into a current employer relationship. The protocol discloses company officer/shareholder roles for some authors; it also names research support. Neither establishes present recruiting, funded access, a degree waiver or permission to adjudicate patients.

Clinical investigators, adjudicating clinicians, biostatisticians and integration engineers have different responsibilities and credentials. Public methods can inform software work, but the trial's IRB waiver does not authorise a learner or agent to access records or conduct a clinical deployment.

## Access and preservation receipt

The three unique primary URLs were the inaccessible publisher, challenged results PMC page and readable protocol PMC page. A cached same-URL find did not bypass the challenge or recover the tables. The only 2026 result claims above are explicitly indexed-primary observations; no exact effect, safety estimate, full registry/history, correction search or raw-data replication is claimed. No fourth source, patient record, image, transcript, dataset, model, native run, clinical exercise, account, contact, UI or child agent was used. Prior reports, the proposal, tree and held source index were not modified.
