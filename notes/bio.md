# Bio, health, neuroscience, materials and scientific software: evidence as of 2026-10-19

## Main judgment (2031 inference)

For a broad ML/software/robotics engineer, the most defensible entry point is the engineering that makes models work with real experiments, instruments and clinical workflows: data provenance, orchestration, inference infrastructure, rigorous evaluation, instrument integration, observability and safe execution. Scientific model invention is a second, higher-specialisation route. Drug development and implant ventures have genuine progress, but their deployment timelines, capital requirements, credentials and geographical concentration make them weaker default career bets than transferable engineering skills. No evidence gathered supports a precise forecast of sector hiring volumes by 2031.

## Clinical AI: market presence is established, outcome claims need individual review

The FDA says it had authorised over 1,600 AI-enabled medical devices for US marketing by September 2026. These span imaging, retinal screening, sensor analysis and insulin delivery. That is regulatory authorisation for defined intended uses, not a measurement of adoption, doctor replacement or improved population health. The FDA list itself is noncomprehensive and periodically updated.

Source (regulator, current Sept 2026): https://www.fda.gov/medical-devices/digital-health-center-excellence/artificial-intelligence-enabled-medical-devices

MASAI is unusually strong prospective evidence. The January 2026 Lancet follow-up analysed approximately 106,000 women in a Swedish randomised screening trial. AI triaged scans to one or two radiologists and supplied detection support. Sensitivity was 80.5% versus 73.8%; specificity 98.5% in both arms; screen-reading workload was around 44% lower. The headline of 12% fewer interval cancers needs qualification: 82 versus 93, ratio 0.88 (95% CI 0.65–1.18; p=.41), establishing noninferiority within its prespecified margin rather than a statistically demonstrated reduction. The study does not establish mortality reduction, universal generalisation across countries/vendors, or autonomous diagnosis.

Primary paper: https://doi.org/10.1016/S0140-6736(25)02464-X
Primary trial index: https://pubmed.ncbi.nlm.nih.gov/41620232/
Investigator institution, read: https://www.lu.se/artikel/ai-stod-vid-brostcancerscreening-farre-missade-cancerfall
Public copy of original Lancet paper, search-indexed but too large for browser extraction: https://www.mdc-berlin.de/system/files/document/cjc%202026.02.04.pdf
The exact Table2 figures were crosschecked in an IHE presentation reproducing original table: https://connectathon.ihe-europe.net/sites/ihe-cat2014.org/files/IHE_EU_EXP_DAYS_2026_Jacob_J_Visser_AI_Tools_for_Radiology.pdf

The November/December 2025 UCLA ambient-scribe RCT randomised 238 outpatient physicians over two months. Nabla reduced measured time-in-note 9.5% versus control; DAX had no statistically significant reduction. Secondary scores suggested wellbeing benefits, and clinicians reported occasional significant inaccuracies. Crucially, Epic Signal omitted editing time inside the vendor platform, potentially overstating whole-workflow savings. The trial was English-only, single institution, registered after commencement, and did not prove downstream patient-safety or quality benefit.

Published primary RCT: https://pmc.ncbi.nlm.nih.gov/articles/PMC12768499/
Primary journal DOI: https://doi.org/10.1056/AIoa2501000
Underlying protocol: https://cdn.clinicaltrials.gov/large-docs/90/NCT06792890/Prot_SAP_000.pdf

## AI drug discovery: later clinical stages, still biological and clinical risk

Rentosertib's June 2025 Nature Medicine trial was a blinded randomised 12-week phase IIa trial in 71 Chinese patients with IPF. The primary endpoint was adverse-event incidence. High-dose arm n=18 showed mean FVC +98.4 mL versus -20.3 mL in placebo n=17, an encouraging preliminary signal. Sixteen of 71 discontinued treatment; participants were geographically homogeneous and 90.1% male. This is not a pivotal efficacy result and does not identify how much AI changed approval probability versus traditional discovery.

Primary RCT: https://www.nature.com/articles/s41591-025-03743-2
Same paper, useful search-indexed detailed tables: https://pmc.ncbi.nlm.nih.gov/articles/PMC12353801/

Insilico reported first patient dosing in phase III on September 10,2026: 320 participants planned across 47 Chinese centres,52 weeks; FVC decline primary outcome. Its own announcement explicitly states that rentosertib remains investigational and has not been approved by any regulator. The PI's favourable-case timeline was 3–4 years to approval. Phase III status is sponsor-reported here; the trial registry was found but could not be independently parsed with available tools. Do not claim all AI-discovered drugs are unapproved: attribution is ambiguous and exhaustive global regulator audit was not done.

Company primary announcement: https://insilico.com/news/isn1009261-insilico-medicine-doses-first-patient-genesis-ipf-3
Registry identity, not independently parsed: https://clinicaltrials.gov/study/NCT07687459

## Molecular models: usable discovery tools, not digital organism or patient simulators

AlphaFold 3 (May 2024) predicts complexes involving proteins, nucleic acids, small molecules and ions. A structure model is one component of biological efficacy, toxicity, delivery and manufacturability. BindCraft (Nature, Aug 2025) provides stronger experimental evidence than a purely in-silico benchmark: automated open-source designs tested on 12 protein targets, reported 10–100% binder hit rates across targets, average 46.3%. Examples include 13/53 PD1 designs binding and 7/9 PDL1 designs. These are selected research targets and binding assays, with some patient-derived serum experiments, not treated-patient outcomes. Authors explicitly flag immunogenicity and delivery concerns. Avoid reproducing headline success rates as universal.

AF3 primary: https://www.nature.com/articles/s41586-024-07487-w
BindCraft primary: https://www.nature.com/articles/s41586-025-09429-6

AlphaGenome (Nature, Jan 28,2026) processes 1 MbDNA and predicts molecular tracks, matching/exceeding external models on 25/26 variant-effect evaluations in the paper. These are particular molecular prediction benchmarks, not clinical diagnoses. Developer documentation states that personal-genome prediction has not been benchmarked, human/mouse species scope, distal regulatory/tissue-specific limits, and a single sequence input that is not inherently diploid-aware.

AlphaGenome primary: https://www.nature.com/articles/s41586-025-10014-0
Developer limitations: https://google-deepmind-alphagenome.readthedocs-hosted.com/faqs.html

Google's Sept 8,2026 AlphaGenome Atlas precomputes approximately 9 billion single-nucleotide changes in a 1 PBcatalog, available through a no-code portal. Company-reported rare-disease/UKBiobank examples are research assistance, not clinical approval. This also erodes the value of building a thin interface around one model; cohort curation, provenance, validation and integration remain engineering opportunities.

Primary launch: https://blog.google/innovation-and-ai/models-and-research/google-deepmind/alphagenome-atlas/

## Automated science and materials: the strongest transfer from robotics/software

A March 6,2026 npj Computational Materials paper actually operated an X-ray nanoprobe and polymer-film robotic platform with AI agents, Python functions, EPICS/PyEpics, code checks and human guidance. Hardware tests used narrow tasks and small repeated evaluations (four per task), not broad autonomous lab validation. More complex tasks degraded without feedback; model-dependent code and visual failures persisted. Calibration, manual loading and expert procedural teaching remained. The architecture constrained action spaces and kept low level instrument control deterministic and validated. Useful work exists at exactly those interfaces.

Primary experiment: https://www.nature.com/articles/s41524-026-02005-0

The Jan 19,2026 Nature A-Lab correction is an important reproducibility counterweight: novelty originally meant new to its prediction platform, not necessarily new to science; reanalysis confirmed 36/40 reported successes, four inconclusive, and one training-data compound was removed. Automation capability survives, but design count and synthesis count should not be called commercially useful discoveries without verification, novelty and property testing.

Primary correction: https://www.nature.com/articles/s41586-025-09992-y

## BCI: impressive assistive trials; broad consumer forecast not established

The March 31,2025 Nature Neuroscience streaming brain-to-voice system decoded in 80 msincrements in one severely paralysed/anarthric clinical-trial participant; this is a meaningful assistive result, with limited participant-level generalisability. UCLH's Jan 29,2026 update confirms seven GB-PRIMEpatients received Neuralink implants in late 2025, explicitly to evaluate safety/functionality. Neither source establishes broadly available enhancement implants for healthy consumers by 2031. Real engineering areas include neural-signal pipelines, realtime inference, calibration, assistive interfaces and device reliability; access and specialist collaboration constrain entry.

Primary BCI paper: https://www.nature.com/articles/s41593-025-01905-6
Clinical institution: https://www.uclh.nhs.uk/news/seven-gb-prime-patients-now-participating-neuralink-trial
Company updates additionally say21participants and Oct1,2026pretraining on50,000hours; treat as vendor claims not peer-reviewed generalisation: https://neuralink.com/updates/

## Concrete current hiring evidence and limits

Opened Isomorphic Labs current job board and clicked active postings Oct 19,2026. Main board listed 29 roles. Staff Software Engineer (Inference Platform) asks productionML, Kubernetes / GCP / GPU/reliability with no PhD requirement listed. ML Research Engineer accepts advanced degree OR equivalent practical experience, asks 4+ years and end to end ML; biological domain knowledge is nice-to-have. Research Scientist saysPhD-or-equivalent in prose but application asks aboutPhD and warns lack may reject. All three explicitly require 3 days/week inLondon office. This is evidence of transferable engineering work, not aggregate hiring growth or global remote availability. Search-indexed Benchling vacancies looked active, but opened careers render showed no openings; do not cite them as verified current.

Main current board: https://job-boards.greenhouse.io/isomorphiclabs
Staff inference engineering: https://job-boards.greenhouse.io/isomorphiclabs/jobs/5837899004
Research engineering: https://job-boards.greenhouse.io/isomorphiclabs/jobs/5578430004
Research scientist: https://job-boards.greenhouse.io/isomorphiclabs/jobs/5224363004

## Three defensible inferences, option value, and falsifiers

1. Model abundance increases the relative value of measured ground truth and experimental throughput. Prefer lab orchestration, telemetry, calibrated sensing, lineage, negative-result capture, active learning and validation systems. This transfers to manufacturing, energy and robotics. Falsifier: prospective blinded evidence that virtual assays reliably replace broad physical validation and that necessary data/interfaces become cheap commodities.
2. Commercial value depends on whole-workflow outcomes. MASAI and ambient scribes show task savings, adoption and clinically relevant outcomes can move differently. Prefer engineering that measures total cycle time, rework, failure, model drift and downstream outcome, together with integration. Falsifier: multicentre autonomous systems repeatedly deliver better patient outcomes and lower full cost, with broad authorised deployments and little integration/oversight burden.
3. Choose the layer before choosing the field. Scientific research leadership, clinical decisions and devices have high credentials or physical/geography barriers; inference/reliability/data/software roles preserve cross sector options. Nocode Atlas and open BindCraft reduce scarcity of merely accessing a model. Falsifier: platform vendors absorb the integration/evaluation layer while specialist employers show sustained hiring primarily of narrow credentialed scientists. Monitor current job mix and customer procurement, not model-news volume.

Recommended portable evidence of ability: one reproducible instrument/robot workflow with deterministic constrained commands, simulated fault recovery and a complete experiment ledger; one ML evaluation showing leakage-aware splits, calibrated uncertainty and external validation; one production inference service with measured GPUcost/latency/reliability. Work with domain scientists. These show transferable capability without pretending to validate a medical treatment or control hazardous equipment.

## Method and evidence audit

This is the first-pass specialist research completed on 19 October 2026, not a report of 24 hours already spent researching. Root is arranging a later research pass. This file preserves the evidence and reproducible questions for that pass.

- Discovery used the installed agent-reach skill routing guidance and built-in web search. Root had already checked available backends; no social account sessions were accessed. Reading focused on peer-reviewed primary papers, investigator institutions, the FDA, developer documentation and directly opened employer job postings. Press releases are explicitly labelled sponsor/company reports.
- Bibliographic dates were read from source pages or the paper, not the search engine's relative-age field. No statement above depends on a forecast market-size article.
- Some Nature full-text opens intermittently failed while search-indexed article text was available. PubMed/PMC direct opens sometimes returned browser checks; detailed trial text was retrieved from the search index. Lancet returned 403. The MASAI primary paper was identified on an academic host, but full extraction failed because its 13 MB size exceeded browser limits; exact Table 2 statistics were crosschecked against the reproduced original table in IHE's 2026 radiology presentation and the investigator's institution report. For final report, quote the noninferiority conclusion conservatively, link the primary DOI, and avoid implying full supplementary-data reanalysis.
- No individual-level trial data, raw molecular assay data, clinical outcomes, or instrument trajectories were independently reanalysed. Reported experimental success is the authors' result; the A-Lab correction itself is peer-reviewed post-publication reanalysis.
- NCT07687459 was located, but clinicaltrials.gov public HTML/API did not expose usable contents in this session. Phase III details therefore retain sponsor-report status; no unpublished Phase III efficacy is claimed.
- Live job board inspection changed the evidence: Isomorphic Labs' root board showed 29 positions with working links, whereas some search results showed 30 or older role titles. Benchling's search snippets suggested openings but its opened page did not list them. Avoid inferring current vacancy availability from snippets. Three Iso job pages were opened and requirement sections read; no application, contact or account action occurred.
- No software, package, plugin, skill, model weights or dataset was installed/downloaded. No private mailbox, research data, employer data or clinical records were accessed. The only writes were local research notes.

### Gaps for the next research pass

1. Verify phase III registry fields, recruitment status, registered endpoints, planned completion and protocol changes against an accessible registry snapshot. Check whether any regulator has approved the named drug since the latest sponsor statement; do not generalise to every AI-assisted molecule.
2. Locate the publisher-authorised MASAI paper and statistical appendix; verify randomisation units, noninferiority margin, missing follow-up, preplanned subgroup analyses and confidence intervals. Look for independent prospective studies on another vendor and screening system; the same trial's multiple papers are not independent replications.
3. Review external replication and target-selection rules for BindCraft, with particular attention to prospective difficult targets, binding measurement formats/avidity, expression, immunogenicity and in vivo functionality. Separate selected-target hit rate from unbiased prospective success.
4. For AlphaGenome Atlas, examine preprint methods, release licences and independent studies of per-individual accuracy, distal effects, causal variant ranking and ancestry/cell-type distribution shift. Do not describe a molecular score as a diagnosis.
5. For scientific-agent papers, collect full evaluation task counts, number of trials, human intervention frequency, consumable/time cost, failed runs and shared raw traces. Compare actual protocols against deterministic automation baselines. A successful agent demo is not evidence it improves cost per validated experiment.
6. For BCI, read trial registrations and any peer-reviewed multisubject, longitudinal, home-use results. Look for calibration burden, uptime, signal stability, adverse events, lost channels, withdrawal and independence measures; separate cursor/speech demonstration from durable clinical benefit.
7. Expand employer sample to 10–20 direct postings across UK/EU/US/India, scientific software vendors, clinical infrastructure and lab robotics; record geography, visa/remote constraints, degree wording, seniority and requested practical evidence. One frontier employer is not representative demand evidence. No salary or hiring-volume estimate was validated in this pass.

## Reachable roles and degree/geography barriers

| Route | Actual work | Evidence of reachability | Main barrier | Portable skill value |
|---|---|---|---|---|
| ML/inference platform engineering | Model serving, schedulers, GPU utilisation, scaling and reliability | Iso Staff Inference posting asks production AI / ML, Kubernetes / GCP / GPU and software experience; no PhD listed | Staff-level production track record, London 3 days/week | High across AI products and sectors |
| Research engineering | Implement models, build data/training/evaluation infrastructure, benchmark and optimise | Iso ML Research Engineer accepts Master's / PhD OR equivalent practical experience;4+ years; biology a nice-to-have | Strong actual model lifecycle and architecture experience; London hybrid | High across scientific and general ML |
| Lab automation/software | Integrate instrument APIs, state/lineage, run orchestration, quality checks and recovery |2026 instrument study demonstrates existing Python/EPICS/vendor interfaces; Opentrons/PyLabRobot offer mature control APIs | Physical equipment access, calibration, domain operators; location often matters | High across robotics/manufacturing/experimental systems |
| Clinical workflow/evaluation engineering | EHR integration, traceable notes, error review, drift/failure monitoring and total workflow measurement | scribe RCT shows real deployment plus measurement/integration gaps | Institutional data/access, procurement, standards, clinical collaborators | High in enterprise/regulatory workflows |
| Research scientist / medicinal or clinical leadership | Invent new methods, define mechanisms/targets, clinical responsibility | Iso scientist form warns no PhD may be rejected; clinical and drug scientist roles are separately staffed | Relevant doctorate/equivalent research record or profession-specific credentials, depending on role | Scientific depth valuable, entry slower and more specialised |

This is a role-selection comparison, not a personalised eligibility determination. A job title's future existence is easier to infer than its 2031 headcount. Access to UK / US physical teams is a practical condition, not a detail to postpone.

## 30-day experiment: an auditable simulated lab runner

Purpose: test interest and demonstrate the robotics/software interface before committing to specialised science training. Use an established protocol simulator instead of building a custom robot framework. The current Opentrons Python API explicitly supports robot-free simulation, returns structured run logs and distinguishes simulation from physical execution. PyLabRobot similarly exposes backend-agnostic frontends and testing backends.

Primary docs read 19 October 2026:

- https://docs.opentrons.com/python-api/tutorial/
- https://docs.opentrons.com/python-api/reference/execute-simulate/
- https://docs.opentrons.com/python-api/reference/protocols/
- https://docs.pylabrobot.org/stable/api/pylabrobot.liquid_handling.html

Scope: simulated liquid-handling protocol execution with a typed command boundary, explicit resource reservations, an immutable experiment ledger and deterministic replay. Start with published vendor tutorial protocols and labware definitions; record licences/versions. Any LLM proposes structured operations; the controller validates and schedules them. No actual hazardous substances, live instruments or patient-facing decisions are needed. Dependency installation would require separate user approval before implementation.

Suggested schedule: days 1–7 read the control API, trace one reference protocol, define input / output and failure states; days 8–18 implement simulation, ledger and recovery; days 19–25 run seeded failure cases and compare with a deterministic reference; days 26–30 write a short engineering case study and record a reproducible demo.

Chosen portfolio acceptance gates, not industry safety standards:

1. 20 valid reference / parameter-variation protocols compile to simulator-accepted actions; all generated commands belong to an explicit allowlist. At least 20 deliberately invalid fixtures are rejected with reasons, including resource conflicts, impossible volume/state and invalid labware.
2. 100 seeded runs exercise at least five fault types: timeout before execution, ambiguous timeout after execution, duplicate response, controller restart and unavailable resource. Zero ambiguous outcomes are silently marked successful. Every ambiguous action is reconciled or explicitly stopped for review; no automatic replay of a possibly completed action.
3. 100% of run ledger entries contain protocol version, input hash, simulator version, action ID, pre/post state, outcome and error/recovery event where relevant. Replay reproduces planned action sequence and final logical state for every completed fixture; timestamp differences are excluded.
4. Compare deterministic reference, unconstrained model proposal and constrained model proposal on the same fixed 20 tasks. Report completion rate, invalid-action rate, human-review frequency, tokens/cost, walltime and simulator commands; failures remain visible. Target zero accepted invalid commands. Successful simulation makes no claim about pipetting accuracy or hardware safety.
5. One-command local reproduction after an explicitly approved setup; an independent engineer can reproduce all fixed fixtures from the repository instructions. No public publication/push is presumed authorised by this research request.

Career interpretation: passing demonstrates integration, state management, fault recovery and experimental provenance. Failure is useful if it reveals that the interface work is unappealing or simulated successes do not translate to practical laboratory requirements. A domain operator's protocol review, if later arranged by the user, is more informative than adding another agent framework.

## 90-day experiment: leakage-aware ML evaluation plus serving

Purpose: demonstrate credible scientific ML without claiming to discover a treatment. Choose one workload; avoid starting three weak projects. An accessible signal task is PTB-XL v1.0.3, whose primary dataset page verifies open access under CC BY 4.0,21,799 ten-second ECGs from 18,869 patients, recommended patient-respecting splits and documented duplicate corrections. These are historical 1989–1996 recordings, a useful generalisation caveat. Use its 100 Hz data for a bounded baseline. Downloading data/model weights or installing dependencies is a later implementation step requiring the applicable approval, not something done in this research pass.

Primary dataset and access/split notes: https://physionet.org/content/ptb-xl/1.0.3/

Weeks 1–2: define the exact label task and preregister split / metrics locally. Weeks 3–5: reproduce one simple baseline and an established model. Weeks 6–8: evaluate calibration, noise, subgroups and label/split sensitivity; separate development analysis from a frozen final test. Weeks 9–12: serve the frozen model with input validation, observability and benchmarked throughput, then package an honest model card and failure report.

Chosen engineering/evaluation acceptance gates:

1. Zero patient ID overlap between train/validation/test; zero exact waveform hash overlap across partitions. Use official folds 1–8 train,9 validation,10 test and preserve a manifest with dataset version and file hashes. Do not use age values over 89 as ordinary numbers: dataset privacy handling encodes these specially. Demonstrate a deliberately leaked random record split as a separate diagnostic only; never report its result as the valid baseline.
2. Report classwise and macro AUROC / AUPRC, calibration/Brier score and thresholds selected only on validation data. Include patient-level bootstrap95% CIs and age / sex / noise subgroup results when samples support them. Report sample counts and avoid claims from small groups. Do not set an arbitrary leaderboard score as a pass gate; reproducibility and transparent comparison are the goal.
3. Reproduce a published / open baseline within an agreed tolerance, for example 0.02 macro AUROC, only after matching its dataset version, labels, preprocessing and split. If those do not match, document why and establish a local baseline rather than labelling a mismatch as replication.
4. Rerun with three training seeds and record spread; freeze test set access until final model selection. Show sensitivity to one controlled signal shift, such as added noise or lead masking, and report confidence/error behaviour. A site held out test is not independently external validation; reserve that term for a separately sourced, appropriately harmonised dataset.
5. Serve the 100 Hz ten-second input locally. On declared hardware, load test 1,000 fixed requests and target zero silent schema acceptance errors,100% run traceability and p95 latency below 1 second at concurrency 1. Report cold start, memory, energy/compute proxy,latency distribution and full preprocessing time. This is a chosen portfolio performance gate, not a clinical latency requirement.
6. Save 5–10 representative failure cases, trace inputs through preprocessing/model/output and explain what additional evidence would resolve them. A successful model benchmark is a software/research demonstration, not clinical validation.

Optional alternate 90-day track for stronger materials interest: reproduce an established Matbench task with composition-aware leakage checks, then add active learning and simulation orchestration. Matbench primary material identifies open tasks/reference implementation: https://arxiv.org/abs/2005.00707 . The current Matbench Discovery site returned403 in this session, so it was not inspected and no specific leaderboard claim is made. Choose this alternative only after confirming current datasets / licences and baseline instructions.

## Decision after 90 days

Assess the evidence of ability against actual employer requirements: production ML platform role needs robust serving and infrastructure; research engineering needs actual model implementation/evaluation; lab automation needs a real operator / instrument collaboration beyond simulation; research scientist path needs research depth and often credentials. Keep whichever project produces the clearest independently reproducible evidence. Continue toward specialised biology only if both the scientific questions and the practical constraints remain attractive. No guarantee of hiring, visa availability, remote access or pay is implied.
