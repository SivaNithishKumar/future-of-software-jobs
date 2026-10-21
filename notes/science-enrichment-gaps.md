# Science enrichment: validation, gaps and launch decisions

Owner `/root/bio_science`; curation date 19 October 2026. Companion: `science-enrichment-round5.json`. This is a candidate enrichment layer for coordinator deduplication and independent review. It is not final-tree acceptance or evidence that the requested research period has elapsed.

## What was completed and checked

Read the frozen taxonomy, institution-directory schema/example records, all four authored science reports, `corrections.json` and the independent `actionability-review-round4.md`. No new internet retrieval was necessary for this curation. No source report, existing directory record or tree node was modified.

The candidate contains **154 evidence/directory/project records plus two separately proposed technical nodes**, with stable `science-enrichment-round5.*` IDs:

| Kind | Count |
|---|---:|
| Institutions | 29 |
| Teams | 8 |
| Researchers | 13 |
| Papers | 26 |
| Code | 21 |
| Datasets | 11 |
| Weight families | 2 |
| Public professional contacts | 20 |
| Claims | 18 |
| Proposed projects | 6 |

The saved file was reparsed after generation and prose repairs. Checks passed for unique IDs, **323 internal references**, **180 links to existing technical nodes**, primary-source URL syntax, referenced local note existence and required institution/paper field presence. There are 106 unique primary URLs across 203 source occurrences; syntax checks do not establish present availability. SHA-256 comparisons confirmed that all eight listed frozen input snapshots remained unchanged during the pass. Validation counts and hashes are retained inside the JSON.

The independent review corrections are carried into the projects: an Opentrons command log or `load_liquid` label is not a capacity/conservation oracle; a scientific importer needs a mature validator and independently specified counterexample; PTB-XL requires an explicit label task/mapping and missingness policy. Local latency is a service measurement, not clinical proof. The obsolete “BCI evidence is only single-participant” interpretation is replaced with distinct longitudinal N1, small multi-user preprint and cross-person EMG records.

## Gaps that prevent final acceptance

| Priority | Issue / affected records | Required reconciliation or boundary |
|---|---|---|
| Citation export | **20 of 26 paper records have null exact titles.** The descriptive labels, primary identifiers, dated methods and limits are retained. Full author lists and some exact date/version suffixes are also incomplete. | Retrieve publisher/arXiv metadata for these precise identifiers. Do not invent titles or treat descriptive labels as exact bibliography. The six supplied titles were not newly checked against publisher metadata in this pass either. |
| Before scientific claim | `paper.masai` | Obtain an accessible authorised full paper/statistical appendix and verify its design/noninferiority details. Existing notes conservatively preserve the reported noninferiority conclusion and the non-significant superiority comparison. They do not claim raw-data reanalysis. |
| Before current trial/approval statement | `inst.insilico`, `paper.rentosertib`, `claim.drug-stages` | Independently parse NCT07687459 and relevant regulator records. The phase III start remains sponsor-reported; no completed phase III outcome or current approval is inferred. Do not extrapolate to every AI-associated drug. |
| Before affected replication | `paper.matbench`, `project.materials` | Read correction DOI `10.1038/s42256-025-01117-4` and determine which artifacts/metrics change. This pass did not infer its contents from its existence. |
| Before foundation-model comparison | `paper.eegcompass`, `paper.eegarena`, `project.neuro` | Reconcile exact tasks, adaptation budgets, preprocessing, pretraining overlap and compute. They have different scopes and publication status; their summaries are not an established contradiction or a settled ranking. |
| Before artifact reuse | 11 code/data records explicitly flag unresolved or unretained terms; several other records still require selected-asset checks. | Pin each actual license, selected asset, version and hash. Code, paper, data and weights have separate rights. Do not convert a framework licence into blanket commercial permission. |
| Before physical/clinical conclusion | All projects and relevant paper records | No raw clinical, EEG, MD, DFT, assay or instrument experiment was rerun. No clinician/operator/domain reviewer, independent reproducer or accessibility participant has been secured. Public healthy-participant EEG does not establish clinical suitability. Numerical model consistency does not establish a material's real properties. |
| Before role recommendation | Employer records, especially Isomorphic, Toronto, Neuralink, CuspAI and Orbital | Recheck current acceptance, exact role requirements, work authorisation and location. The user’s degree, relocation plans, hardware and weekly hours remain unknown. No hiring probability, role-volume or salary estimate follows from this purposive sample. |
| Before funding recommendation | `claim.funding-access`, Toronto, FAIRmat and ARIA records | Keep award allocations, historical solicitation expectations, closed calls and current open funding separate. No programme amount is money available to an independent developer. No staffing effect or actual disbursement was measured. |
| Directory completeness | 12 institutions lack a separate normalised public-contact record. | Their sources may provide recruiting, documentation or paper channels. Missing named contacts remain missing; no personal address was guessed. Do not require contacting anyone to validate this research directory. |
| Schema vocabulary | FDA and ARIA use `institutionType: publicagency`, an explicit extension. | The supplied type list has no regulator/funding-agency category. Root should add an appropriate contextual-authority type or retain these as source authorities; classifying them as research laboratories would be inaccurate. |
| Global deduplication | Shared organisations and research groups may appear in other workers’ enrichment files. | Root owns canonical merges. Meta CTRL-labs and FAIR-Chem are separate team records under one institutional identity; no inference that their employment or data access is interchangeable. No shared index was edited. |

Unresolved rights are especially relevant for Opentrons tutorial/labware assets, the PTB-XL example code, home-use BCI reproduction artifacts, FALCON dataset-specific terms, LSL components, selected FAIR-Chem code, WBM/MPtrj versions, MatterGen public data and phonon utilities. The JSON gives their precise source URLs rather than assigning an invented licence.

Other rights boundaries are already established at a useful level: ORD data/metadata are CC BY-SA 4.0 while specified code/scripts have Apache terms; emg2qwerty/emg2pose actual licence files are CC BY-NC-SA 4.0; current UMA weights have a custom gated FAIR Chemistry licence; MACE checkpoints have family-specific MIT/ASL terms. All require an exact selected version before implementation.

## Proposed depth additions, kept outside the frozen tree

1. **Atomistic numerical/reference validity**, attached under existing `darkside2031.bio-science.materials.evaluation`: force-energy consistency, units/reference corrections, symmetry/extensivity, energy drift and time-step convergence. Existing composition-split/baseline leaves do not express these numerical failure modes precisely.
2. **Mechanistic battery numerical software**, attached under existing `darkside2031.bio-science.materials.infrastructure`: PyBaMM solvers/events, parameter identifiability and electrochemical models. This differs from atomistic material generation and the energy worker’s grid-dispatch/nuclear work.

Accessibility and non-invasive sensing do **not** need a new parallel top-level branch. Their records link existing neuro signal/runtime nodes to existing `darkside2031.interfaces.multimodal.accessibility` nodes. Root may decide the proposed materials depth also fits as richer annotations; neither proposal has been inserted into the tree.

## Launch decisions for a later implementation task

These are alternatives, not six concurrent commitments. Hours are explicit planning assumptions and have not been calibrated to the user’s availability. A 30-day calendar window is not a promise of effort or completion.

| Project | Assumed effort | First decisive gate | Independent oracle | What a successful result could establish |
|---|---|---|---|---|
| Lab runner | 30–50 hours in a month | Exact approved simulator/assets and one reference protocol | Independent capacity/conservation ledger plus an overfilled label the simulator accepts | Resource/state, traceability and ambiguous-action handling in simulation |
| Scientific data gateway | 30–50 hours initially; 40–80 additional hours | Mature ORD validator, exact subset rights and independently expected counterexample | Established schema path plus source-to-output trace and independently specified unit/conflict cases | Data/control engineering; chemistry claims require a domain reviewer |
| PTB-XL evaluation | 80–140 hours over 90 days | Exact diagnostic-superclass task, baseline recipe and permitted local runtime | Dataset labels with documented mapping; patient split and independent scorer fixture | Retrospective ML evaluation and bounded service measurement |
| EEG calibration/uncertainty | 30–50 hours initially; 50–90 additional hours | Labelled offline runs, loader/version, standard baseline | Producer labels, mature MOABB evaluator and independent split/metric controls | Subject/session evaluation and causal replay engineering |
| Materials evaluation/numerics | 30–50 hours initially; 50–90 additional hours | DFT-reference/prediction identity, correction contents, selected artifact rights | Published DFT labels; independent metric traces; finite-difference consistency for the numerical slice | Screening evaluation or numerical/runtime engineering, depending on the tested layer |
| PyBaMM fallback | 40–80 hours after choosing it | One real solver/event/parameter defect with independent expected behaviour | Analytical/simplified constraint and tolerance convergence | A bounded numerical-software contribution |

Before any launch: secure explicit approval for applicable installations/downloads, choose one route and freeze a small resource/time budget. Reproduce an existing result before extending it. Stop or redirect when rights, the oracle or essential review is unavailable. No participant recruitment, hardware operation, cloud spending, application, publication or outreach is authorised by these proposals.

For all routes, distinguish learning the mechanism, passing a specified regression suite, improving a real workflow, meeting an employer’s requirements and earning repeat customer revenue. Each has a different oracle. Zero failures in a small purposive suite is not a safety certificate or a population reliability estimate.

## Acceptance still pending

The curation is structurally usable and preserves the strongest corrections, uncertainty and practical gates. It still needs coordinator deduplication, citation/artifact reconciliation and independent substantive review. It does not settle personal career fit or forecast 2031 employment.
