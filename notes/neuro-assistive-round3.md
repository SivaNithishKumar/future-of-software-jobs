# Neurotechnology, assistive input and biosignal software

Bounded specialist pass completed 19 October 2026. Owner: `/root/bio_science`. This pass covers participant/session generalisation, drift, latency, usable interfaces and accessible software work. It does not repeat the LIMS, procurement or automated-chemistry work in round two. No data/model downloads, installations, accounts, applications, outreach, patient contact or live equipment were used.

## Main finding and corrected maturity assessment

**The field is beyond isolated short demonstrations, but evidence scales differently across modalities.** Implanted speech interfaces now have substantial home-use evidence in one individual and emerging multi-participant transfer results. Wrist EMG has stronger demonstrations of generic cross-person input models. EEG supports open research and many benchmarks, with substantial task, session and population dependence. Accessible engineering work includes inference, acquisition, timing, data quality, calibration, user correction and operating-system integration; the evidence does not establish a large remote neurotechnology job market by 2031.

The first-pass phrase that high-performance speech BCIs are demonstrated only in individual participants would now be incomplete. Distinguish **longitudinal usability in one participant**, **multi-user decoding in a small preprint cohort**, and **cross-person EMG studies**.

## 1. Implanted interfaces: duration, population and calibration are separate axes

### Long-term independent home use is real, with important system support

A June 2026 Nature Medicine study reports over 3,800 hours of home use over approximately 19 months in one man with ALS, sustaining communication and employment. Care partners still performed roughly 20 minutes of setup; the research system used wired connections and multiple computers. Speech decoding recalibrated in the background. The 99.2% word accuracy applies to prompted copy tasks; personal-use utterances had separate self-ratings, with 53.3% immediately fully correct, 12.9% corrected and 26.1% mostly correct. These word- and utterance-level metrics are not directly comparable. Stable performance required both algorithms and useful correction/control software. Raw personal-use neural data and transcripts remain private; figure/statistics reproduction data are public. [Final paper, 15 June 2026](https://doi.org/10.1038/s41591-026-04414-6), [analysis repository](https://github.com/Neuroprosthetics-Lab/NatMed_independent_personal_use)

### Cross-person transfer has improved, but is not calibration-free deployment

The July 2026 **preprint** *A generalizable speech neuroprosthesis* pools six BrainGate2 participants and compares closed-loop performance in three. Shared decoding still uses participant-specific input projections. Its few-shot first-day simulations concern two participants: approximately 17–23 minutes of attempted-speech calibration produced around 10–11% WER, with additional calibration improving performance. Those are retrospective offline adaptation experiments across recorded sessions, not prospective zero-shot installation in a new patient. The held-out-user scaling analysis excludes the lowest-SNR participant. This is substantive progress with a small, selected cohort. [Version 1 preprint](https://www.biorxiv.org/content/10.64898/2026.07.23.739430v1.full)

A separate BrainGate feasibility safety report accumulated 12,203 participant-days from 14 adults implanted during 2004–2021. It reports 68 device-related adverse events, including six serious events, and none causing death, explantation or permanent inability to continue participation. This supports qualified long-term feasibility, not a zero-risk implant or evidence of universal decoder durability. [Neurology primary report](https://doi.org/10.1212/WNL.0000000000201707)

### What counts as generalisation

| Axis | Evidence needed | Frequent misleading substitute |
|---|---|---|
| Across people | A person absent from decoder pretraining; explicit adaptation budget | New trials from a person already represented in training |
| Across sessions | A separately acquired later session, with normalisation and calibration disclosed | Random overlapping windows from the same recording |
| Across months | Prospective use, downtime, recalibration, signal-quality and software-change logs | A high accuracy number from one selected day |
| Across conditions | Different etiologies, residual movement and signal-quality regimes | One high-SNR cohort or exclusion of difficult cases without qualification |
| Usable daily life | Independent setup/use, correction burden, fatigue, false activations and user preference | Prompted copy-task word accuracy alone |

An 80-ms decoding update is not an 80-ms complete user interaction. Acquisition context, filtering, network transport, model look-ahead, debounce/dwell, speech endpointing and display/audio rendering all contribute. Offline prediction using future samples must not be advertised as causal streaming latency.

## 2. Non-invasive EMG: the strongest counterexample to universal personalisation claims

Meta's July 2025 Nature paper trained generic wrist-EMG models using thousands of participants and tested unseen people. Reported closed-loop performance includes handwriting at 20.9 words/minute and gesture/cursor tasks. This is stronger cross-person evidence than small bespoke implant studies, but collection was controlled, users received coaching, and the tasks involved particular motor behaviours. The authors identify disabled populations and wider conditions as further work. Personalisation can improve weaker users, yet adaptation to one person can worsen performance on another. Early stopping in one exploratory analysis used test data and is explicitly labelled validation evidence. The study supports generic neuromotor input, not universal applicability to people without usable muscle output. [Final paper, 23 July 2025](https://doi.org/10.1038/s41586-025-09255-w)

The public emg2qwerty benchmark is a different scale/task: 108 participants and 1,135 sessions, with substantial user and band-placement shift. Its baseline unpersonalised new-user CER exceeds 50%; typing on a physical keyboard, English and touch-typing skill limit deployment inference. A later, larger generic model's success does not mean this smaller public benchmark is solved. [NeurIPS 2024 paper / arXiv v1](https://arxiv.org/html/2410.20081v1)

Both emg2qwerty and emg2pose repositories have non-commercial share-alike licence text. The qwerty README says CC BY-NC, while its actual LICENSE says CC BY-NC-SA 4.0: use the licence file and resolve ambiguity before reuse. qwerty was archived/read-only on 1 August 2026, so it is a research resource, not an assumed active upstream contribution channel. [qwerty repository](https://github.com/facebookresearch/emg2qwerty), [qwerty licence](https://raw.githubusercontent.com/facebookresearch/emg2qwerty/main/LICENSE), [pose repository](https://github.com/facebookresearch/emg2pose), [pose licence](https://raw.githubusercontent.com/facebookresearch/emg2pose/main/LICENSE)

## 3. EEG foundations: a serious rival to bespoke features, with unsettled comparisons

It would be a mistake to build a career plan around hand-crafted signal features being permanently indispensable. Large pretrained encoders could absorb feature engineering, alignment and much calibration. Equally, current evidence does not show that any pretrained encoder makes task-specific evaluation unnecessary.

EEG-FM-Compass, revised August 2026 and published in National Science Review, evaluates 12 open models across 13 datasets. It finds specialist models remain competitive in many settings, frozen linear probes are often insufficient, and more parameters do not reliably improve transfer. [arXiv v3 and journal reference](https://arxiv.org/abs/2601.17883v3), [journal DOI](https://doi.org/10.1093/nsr/nwag466)

The newer September 2026 EEG-Arena **preprint** evaluates a much broader model/task collection and reports foundation-model advantages over strong supervised baselines on most evaluated tasks, alongside benefits from more pretraining data and channel flexibility. These findings challenge a blanket claim that simpler models always suffice. Different tasks, adaptation budgets and protocols could explain differing results; review pretraining overlap, preprocessing and compute before comparing summaries. [Preprint, 26 September 2026](https://arxiv.org/abs/2609.32743)

The practical skill with better option value is **reliable experimental comparison of pretrained and specialist systems under real constraints**, together with streaming and product engineering. Falsifier: genuinely independent person/session/device evaluations show a cheap generic model consistently meeting latency, calibration and usability requirements with little specialist work. Even that would shift work toward integration/product ownership rather than prove all neurosoftware work disappears.

## 4. Public data, code, licences and replication conditions

| Resource | Appropriate test | Version / licence evidence | What is required; what it cannot prove |
|---|---|---|---|
| OpenBMI / Lee2019 MI | Subject and day/session generalisation | [Paper DOI 10.1093/gigascience/giz002](https://doi.org/10.1093/gigascience/giz002); [data DOI 10.5524/100542](https://doi.org/10.5524/100542); current [MOABB dataset record](https://moabb.neurotechx.com/docs/generated/moabb.datasets.Lee2019_MI.html) records 54 people, two sessions and CC0 | Public retrospective healthy-participant data; no headset required. Pin channels, units, sample rate and session IDs. Use labelled offline runs: the loader warns that certain online runs lack labels. Does not validate assistive use in paralysis. |
| emg2qwerty | Cross-user and band-placement/session shift, personalisation budget | [arXiv:2410.20081v1](https://arxiv.org/abs/2410.20081v1); public HDF5 data/checkpoints via repository; actual licence CC BY-NC-SA 4.0 | No wristband needed for offline work. Full generic training is not a tiny-compute baseline; use a bounded subset or released checkpoint after approval. Physical-keyboard recordings do not establish keyboard-free control. |
| emg2pose | Person/session/stage generalisation of hand pose | [arXiv:2412.02725v1](https://arxiv.org/abs/2412.02725v1); 193 participants, 370 hours; CC BY-NC-SA 4.0 repository licence | Motion-capture ground truth is already recorded. Training a comparable dataset would require specialised hardware. Offline pose errors are not daily-life task success. |
| FALCON | Decoder stability on later recording days with small recalibration budgets | [NeurIPS 2024 paper](https://proceedings.neurips.cc/paper_files/paper/2024/file/8c2e6bb15be1894b8fb4e0f9bcad1739-Paper-Datasets_and_Benchmarks_Track.pdf); [MIT-licensed code](https://github.com/snel-repo/falcon-challenge); DANDI datasets | Human, monkey and songbird tasks must be kept distinct. Held-out sessions and private evaluation data are part of the design. Verify each dataset's licence/version separately; code MIT is not a blanket data licence. Challenge submission is an external action, not presumed authorised. |
| BrainFlow | Acquisition and replay-system engineering | [Current project](https://brainflow.org/); [licence](https://raw.githubusercontent.com/brainflow-dev/brainflow/master/LICENSE) has MIT terms plus a SimpleBLE component notice | Synthetic/playback boards avoid buying hardware initially. Native multi-device support already exists; do not rebuild a generic driver layer without a demonstrated gap. Real device timing needs equipment validation. |
| Lab Streaming Layer | Timestamped multimodal acquisition and synchronisation | [2025 paper DOI 10.1162/IMAG.a.136](https://doi.org/10.1162/IMAG.a.136); [project](https://labstreaminglayer.org/) | Mature acquisition/synchronisation framework. Per-component licences must be checked. Its existence weakens claims that every lab needs a custom transport protocol. |

MOABB itself uses BSD-3-Clause and provides standard cross-session/subject evaluation machinery. Its code licence does not override the licences of the datasets it loads. [Current code and contributor information](https://github.com/NeuroTechX/moabb)

## 5. Employers, laboratories and public professional channels

This is a directory, not outreach or a promise of openings. Names/channels come from official pages or paper correspondence. Credentials, work authorisation and geography need a separate eligibility check.

| Organisation / named people | Official channel and relevance | Entry path / limits |
|---|---|---|
| UC Davis Neuroprosthetics Lab: Sergey Stavisky, David Brandman, Nicholas Card | [Institutional lab page](https://health.ucdavis.edu/neurological-surgery/research/labs/neuroprosthetics); final paper correspondence includes `nscard@health.ucdavis.edu`, `sstavisky@health.ucdavis.edu`, `dmbrandman@health.ucdavis.edu` | Real-time decoding, interface/correction software and experimental systems. Clinical studies require institutional access and specialist collaboration. A search-indexed July 2026 junior-specialist posting returned 410 when opened; it is not counted as a confirmed live vacancy. |
| Meta Reality Labs / CTRL-labs: Patrick Kaifosh, Thomas Reardon; emg2qwerty corresponding author Viswanath Sivakumar | [Nature paper](https://doi.org/10.1038/s41586-025-09255-w); published 2024 correspondence `viswanath@meta.com`, current employment/contact validity not independently reconfirmed | Representation learning, on-device inference and HCI. Public dataset research is accessible; the large private training corpus is not. No current Meta vacancy was verified. |
| Systems Neural Engineering Lab / FALCON: Chethan Pandarinath | [Project contact](https://snel-repo.github.io/falcon/) lists `chethan@gatech.edu` for general inquiries; [code](https://github.com/snel-repo/falcon-challenge) | Session robustness, few-shot decoding and reproducibility. Public benchmarks enable work without new participants; clinical deployment remains a separate setting. |
| NeuroTechX / MOABB: Sylvain Chevallier, Bruno Aristimunha, Pierre Guetschel and other maintainers | [Current repository team/contact sections](https://github.com/NeuroTechX/moabb); preferred public channel is repository issues | Reproducible splits, loaders, documentation and evaluation. Explicitly welcomes programming, UX, sustainability and project-management contributions. Current issue ownership must be checked before proposing work; no contribution was submitted. |
| BrainFlow: Andrey Parfenov | [Official project and public professional channel](https://brainflow.org/), `andrey@brainflow.org`; project GitHub/Slack | Cross-language interfaces, device emulators, tests and acquisition. Public synthetic/playback support provides a cheap initial path. Component notices and real-hardware requirements remain relevant. |
| Neuralink: BCI Applications engineering team | [Directly opened official vacancy](https://job-boards.greenhouse.io/neuralink/jobs/6596365003) | Advertises junior-to-senior software work with no neuroscience background required; emphasises CS fundamentals, native/full-stack applications and user outcomes. Explicitly onsite five days/week in Austin or South San Francisco with demanding work expectations. It is evidence that broad software entry exists, not global remote availability. |
| OpenBCI | [Official careers page](https://openbci.com/careers); [project forum](https://openbci.com/forum/) | Official indexed careers material lists software/hardware roles in Brooklyn onsite, but direct page rendering was limited and detailed live requirements were not verified. Treat as a directory lead rather than confirmed eligibility. |
| NV Access / NVDA: Michael Curran, James Teh, contributor community | [Official organisation](https://www.nvaccess.org/), [active code and contribution channels](https://github.com/nvaccess/nvda) | Mature assistive software contribution without implant or neural-data collection. Windows API, Python/C++, screen-reader compatibility and testing are relevant. Modified GPL v2-or-later licence; Windows environment needed for realistic validation. No paid opening was verified. |
| ARIA: Jacques Carolan, programme director | [Precision Neurotechnologies programme](https://aria.org.uk/opportunity-spaces/scalable-neural-interfaces/precision-neurotechnologies) | Official £69m programme with 19 funded teams, including non-invasive and adoption work. This is a programme allocation, not an individual grant open to any developer or a software hiring count. |

## 6. Accessibility software as an alternative route

The product need is often dependable communication/computer access. Eye tracking, face/head control, switches, speech recognition and screen readers can serve parts of that need without neural recording. Which signal is appropriate depends on a person's abilities and context; an engineering prototype cannot determine clinical suitability.

Google's Project Gameface provides camera-based cursor/gesture source for Windows/Android under Apache 2.0, but its official repository has been archived since September 2025. NVDA is actively maintained. These examples distinguish reusable software and contribution opportunities from an assumed supported consumer product or paid job. [Gameface official repository](https://github.com/google/project-gameface), [NVDA current project](https://github.com/nvaccess/nvda)

A broadly useful engineering contribution might concern error recovery, accessible setup, interaction testing or reliable OS integration. A face-control demo on its developer is not proof of usability across disabilities. Improving an existing assistive application with its users is more defensible than declaring a novel neural interface from a webcam classifier.

## 7. A 30/90-day project without patients, implants or new sensing hardware

**Research question:** how much labelled personal calibration is actually needed for robust next-session decoding, and can an uncertainty policy reduce errors without merely refusing almost everything? This is an existing research area; the particular implementation is not presumed novel.

Use OpenBMI motor-imagery data through standard MNE/MOABB tools. Start with a declared small development subset, using only labelled offline data. New installs/downloads require the applicable user approval before implementation. No paid API or model training service is needed for CPU baselines.

### Days 1–30: reproduce the evaluation correctly

1. Freeze data versions, licences, hashes, subject/session/run IDs, units and EEG-only channel selection. Audit actual sample rates and event timing against the producer paper and loader. Exclude EMG/other auxiliary channels from the main EEG predictor.
2. Establish two mature CPU baselines, such as CSP+LDA and a covariance/tangent-space model, plus majority and label-permutation controls. Use training-only fitting for filters/statistics/feature selection and validation-only hyperparameters. Do not turn overlapping windows into independent examples.
3. Run distinct protocols: within-person session-1 to session-2; and subject-held-out evaluation on the development subset. Identify which transforms/calibration are permitted in each. No target labels or aggregate test statistics leak into model selection.
4. Report balanced accuracy/AUROC, Brier/calibration measures, per-subject spread and participant-bootstrap intervals. A demonstration with ten people is a development exercise, not a broad population result.
5. Deliver a reproducible report and data/split manifest, with a deliberate leaky-split comparison labelled as a negative methodological example. Acceptance is correctness, full traceability and reproducibility—not an invented accuracy threshold.

### Days 31–90: test adaptation, confidence and streaming constraints

- Prespecify a final subject split, for example 30 train / 12 validation / 12 held-out test people across the 54-person dataset. Retain all available sessions of a person in that person's group. Freeze hyperparameters before test access.
- Evaluate zero personal labels versus budgets of 10, 25 and 50 labelled trials from target session 1; test session 2 separately. Train-only population models, personalised-only models and adapted models are separate comparisons. Label counts are not automatically equivalent to real daily calibration minutes.
- Compare one eligible pretrained EEG model only after checking its weight/data licences and pretraining overlap. If the held-out people/data appeared in pretraining or provenance is unknown, do not call it independent subject generalisation. Include a matched scratch model where feasible.
- Evaluate selective error versus coverage at prespecified coverage levels (for example 50%, 70%, 90%), with calibration fitted only on validation people. The proposed method succeeds only if it improves a declared error/calibration/compute trade-off over simple baselines on held-out people; negative results remain useful.
- Replay signals with a standard playback/streaming stack. Separate context length, filter look-ahead/group delay, buffering, inference and output latency. Offline cue-locked motor imagery does not establish continuous no-intent false-activation performance; use emulated dropouts only to test software behaviour.
- Measure declared-hardware throughput, p50/p95 delay and memory. Inject missing channels, short gaps and amplitude changes as controlled stress tests; report them separately from natural session shift. No silent output/action should be accepted when the stream is explicitly missing or invalid. This is a software test gate, not a patient-safety claim.

**Possible upstream contribution:** a confirmed split/loader/unit defect with a minimal regression fixture, or a well-documented evaluation of calibration/coverage under session shift that complements existing MOABB machinery. Read existing issues, papers and tests first. Any publication, PR or contact would be a later authorised action.

## 8. What would change the career conclusion?

- Stronger generic models may remove much bespoke feature engineering. Evidence would be consistent gains on genuinely unseen people, sessions and devices under equal calibration/compute budgets, with deployable latency and transparent pretraining.
- Small numbers of well-funded labs may produce excellent science without many accessible jobs. Watch actual engineering roles, repeat hiring, location and funding duration—not article or implant counts.
- Native platforms can absorb acquisition/evaluation work. BrainFlow, LSL and MOABB already solve substantial parts of it. A new framework needs a concrete unmet requirement, not the existence of a hard field.
- Assistive input may be better served by simpler modalities for many users. Compare full task completion, fatigue, correction and setup with the relevant existing interface before claiming the neural modality's superiority.
- Public healthy-participant success may fail in the intended clinical population. Existing public data allow methodological work, not a shortcut around clinical collaboration and evaluation.

## Methods and remaining limits

Read the coordinator's accepted source/claim index before the new scan. New primary evidence includes the 2026 home-use paper, July multi-user speech preprint, Meta's cross-person EMG work, public benchmark methods/licences, current official software vacancy, ARIA programme and maintained open software. This file should be deduplicated into the root index by the coordinator.

No raw data were analysed and no decoder was run. Nature and bioRxiv sometimes blocked direct rendering; their indexed full methods were used, and publication/preprint status is preserved. GigaDB's JavaScript page did not render; dataset description/licence was corroborated through the maintained MOABB record and producer DOI. The BRAIN budget FAQ still discussed FY2025 while awaiting FY2026; it was not used as a current appropriation figure. Some recruitment search snippets were stale or failed direct verification and are labelled accordingly.

No claim is made that all implanted BCIs lack marketing authorisation: the named speech studies are investigational research, and broad BCI terminology includes very different device classes. No claim is made that EEG/EMG can read arbitrary private thoughts, diagnose a person, or substitute for individual accessibility assessment. This is an engineering career and research map, not medical advice.
