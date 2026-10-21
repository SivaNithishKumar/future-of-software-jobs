# Creative media, games and production software through 2031

Cutoff: 19 October 2026. This contribution moves beyond the initial GDC/Roblox macro statistics into production engineering, controllability, editing, temporal/identity correctness, asset provenance, audio, rendering/streaming and interactive worlds. Research/design only: no media was generated, rendered, transformed, downloaded, uploaded or published; no software was installed, paid runs made, private projects accessed, people contacted or child agents created. Proposed projects below are unexecuted designs.

## Finding and career implication

Generative models are becoming useful parts of creative workflows. The more defensible developer opportunity is **turning generated and authored assets into a controllable, editable, reviewable production**, with known timing, identity, rights, versions and costs. This includes pipeline/tools engineering, technical art, evaluation/QA, editorial interchange, audio/localisation tooling, rendering infrastructure and interactive-system engineering.

This is not evidence that traditional production work is immune to automation or that every creator-tool startup will find buyers. It suggests a practical combination: software/system competence plus understanding of artists’ workflows and a measurable production bottleneck. A portfolio proving reliable revision and integration is different from a collection of attractive generated clips.

For an AI/application engineer, ordinary tools/pipeline and quality-engineering routes can be more directly accessible than training a frontier media model. Original graphics/vision research remains a different, potentially valuable path with deeper mathematical/research requirements. The source set does not justify a 2031 salary or vacancy-count forecast.

## 1. Capabilities are moving toward control, but vendor claims need production tests

Google’s [13 January 2026 Veo API update](https://blog.google/innovation-and-ai/technology/developers-tools/veo-3-1-gemini-api/) describes stronger reference-conditioned identity/background preservation and additional creative controls. Runway’s [21 May 2026 Aleph 2.0/Edit Studio release](https://runway.com/news/introducing-aleph-2-and-edit-studio) explicitly targets localised video edits while preserving input footage. These are concrete product directions. They are not independent demonstrations that arbitrary footage can be revised without introducing temporal, identity or unaffected-region errors.

[Adobe’s 15 April 2026 production update](https://blog.adobe.com/en/publish/2026/04/15/adobe-extends-leadership-video-unleashing-new-ai-powered-creation-firefly-reinventing-color-editors-in-premiere) combines generation with editing, colour and collaborative review. Its different features have separate beta/general-availability states. A release announcement should not be flattened into “all production functionality is finished.”

The emerging requirement is a contract for a revision: **what may change, what must remain, when the change applies, what source assets/performances it uses, and how someone can revise it again**. Prompts, reference images and camera controls help satisfy parts of that contract; explicit masks, tracks, scene descriptions, timings and review remain useful.

## 2. A technical branch map with independent correctness questions

### Image, video and identity control

- Reference conditioning: character/object/style references → measurable identity attributes → lighting/pose/scale variation → repeated shots → continuity across a sequence.
- Motion and layout: spatial blocking/trajectory → camera and object motion → occlusion/disocclusion → persistence and interaction → artist revision.
- Local editing: instruction and mask/time range → intended change → unchanged-region preservation → temporal/audio continuity → further editability.
- Quality separation: aesthetic preference → instruction adherence → factual/textual accuracy → structural/temporal correctness → production acceptance.

An output can look excellent while changing the wrong object, altering a logo, moving a camera incorrectly or changing identity after occlusion. Conversely, pixel differences outside a mask can result from valid colour/codec changes; the oracle must reflect the editing contract rather than demanding impossible byte identity.

Recent research makes the control gap concrete. [LooseControlVideo, June 2026 / ECCV 2026](https://arxiv.org/abs/2606.19495) studies spatial blocking with sparse 3D boxes. [Motion and Disocclusion Control, 2026](https://anranqi.github.io/jackinbox/) separately studies what moves and what newly appears; the authors identify difficulty jointly controlling the appearance and dynamics of newly revealed objects. Its page marks code as coming soon, so a paper/project page is not automatically an available implementation.

### Audio, speech, localisation and sync

- Meaning: source text/dialogue → pronunciation and named entities → language/translation fidelity → performance/prosody → human approval.
- Timing: words/phonemes/cues → alignment with picture → pauses/overlap → subtitle duration/readability → localisation revisions.
- Signal delivery: sample rates/channels/loudness → stems and mix → clipping/noise → codec/container metadata → actual playback.
- Rights: model/code/weights → source recordings and performer permission → intended replica/use scope → distribution terms and attribution.

A pleasing voice is not proof of correct words, meaning, timing or permission. ASR/WER, alignment and loudness checks are useful but incomplete: automatic transcription can miss a repeated error, translated dialogue can preserve words but lose meaning, and voice similarity does not prove a valid performance licence.

### Editorial, assets and production pipelines

- Editorial state: shots/clips and rational timebases → tracks/transitions → source-media links → versions/review notes → reproducible revision.
- Asset state: identity and dependency graph → textures/rigs/materials/colour transforms → approved versions → interchange → archive/reuse.
- Production operations: jobs/dependencies → storage/transfers/cache → render/encode/retry → QC/review → release/delivery.
- Collaboration: artist intent → tool behaviour → feedback/approval → audit/version history → repeatable workflow improvement.

[OpenTimelineIO](https://github.com/AcademySoftwareFoundation/OpenTimelineIO) represents editorial cut information and references external media; it is not a media container. [OpenUSD](https://github.com/PixarAnimationStudios/OpenUSD) represents time-sampled scene description for interchange. These are useful explicit structures around which generated and authored media can be organised. Neither automatically supplies a complete editor, renderer or studio asset-management system.

### Interactive games and world models

- Game correctness: authoritative state → rules, interaction and collision → action/replay → saving/loading and persistence → networking/multi-agent behaviour.
- Generated world behaviour: action conditioning → visual response → identity/object persistence → long-horizon consistency → task success and recoverability.
- Production integration: editable assets/state → level/tool workflows → debug/repro → performance/latency budget → distribution and ongoing operation.

Google’s [5 August 2025 Genie 3 research account](https://deepmind.google/blog/genie-3-a-new-frontier-for-world-models/) reports interactive 720p/24fps environments lasting minutes, while explicitly listing constrained actions, multi-agent challenges and limited duration. This is a dated research demonstration, not a claim about the newest 2026 model/account access. Visually plausible navigation is not proof of saved-state correctness, stable game rules, multiplayer synchronisation or a complete game-production toolchain.

Mature engines expose authored state, assets and APIs that make many invariants testable. They are not automatically bit-identical across platforms or stochastic render/physics configurations. The appropriate comparison controls version, seed, timestep and numerical assumptions, and asks which properties are actually guaranteed.

## 3. Evaluation: aesthetics cannot substitute for temporal and edit correctness

[VBench 2.0, March 2025](https://arxiv.org/abs/2503.21755) expands video evaluation toward intrinsic faithfulness; its [implementation](https://github.com/Vchitect/VBench) provides usable evaluation components. [OmniEdit-Bench, August/September 2026](https://arxiv.org/abs/2608.05049v2) explicitly argues that visually strong unchanged footage can inflate editing scores despite an incorrect edit, and separates spatial, temporal, audio and reference-driven instructions. These are research frameworks, not certificates of production readiness.

A practical evaluation should define separate pass/fail or scored dimensions:

| Dimension | Independent reference/oracle | Material limitation |
| --- | --- | --- |
| Edit fidelity | Written task plus annotated object/time/mask and expected operation | A language-model judge can share the generator’s mistakes; validate against human-labelled or executable cases. |
| Preservation | Source/reference frames, masks and declared permitted transformations | Compression and valid lighting/motion effects can make strict pixel equality inappropriate. |
| Temporal structure | Track/camera/object annotations; source IDs; known events and time ranges | Optical-flow consistency depends on flow quality and cannot alone establish correct scene physics. |
| Identity/continuity | Permitted character/object reference attributes and reviewed cross-shot matches | A single embedding similarity can overlook costume, topology, accessories or semantic identity errors. |
| Text/audio | Exact transcript/cues/names plus permitted source recordings and listening review | WER or automated alignment does not prove translation, acting quality or consent. |
| Interactive behaviour | Explicit game state, rules and action trace; invariant/state-transition tests | Visual similarity cannot prove hidden state or causal/game-rule correctness. |
| Aesthetic acceptance | Blind human review with declared rubric and reviewer agreement | Subjective preference is context-dependent and distinct from functional correctness. |
| Delivery | Timebase/frame count, channels, encoding metadata, subtitles and playback | A successfully encoded file can still have wrong content, timing or poor viewer experience. |

Keep success denominators visible: all attempts, all selected clips, accepted clips/seconds, manual fixes, review time and failures. A curated demo does not reveal acceptance rate. Use held-out scenes, occlusions, motion directions, durations, names/languages and revision requests, rather than evaluating only the prompts used during tuning.

## 4. Actual production evidence and economics

### Finished production use is real, but its denominator matters

In its [17 July 2025 earnings call](https://s22.q4cdn.com/959853165/files/doc_financials/2025/q2/Netflix-Inc-_Earnings-Call_Transcript.pdf), Netflix describes its Eyeline team using AI-powered VFX on a building-collapse sequence in *The Eternaut* and claims the sequence was completed ten times faster than a traditional workflow. This is a company executive’s sequence-level report; it does not disclose the complete attempt/review cost, a controlled counterfactual, a whole-series productivity gain or an employment effect.

Adobe’s [4 September 2026 account of its own Times Square campaign](https://blog.adobe.com/en/publish/2026/09/04/times-square-takeover-how-adobe-brought-firefly-world-biggest-stages) reports hundreds of assets, millions of rendered frames and substantial production data, with Frame.io handling feedback/approvals. This is vendor/customer-zero evidence of finished campaign production and coordination, not an independent general ROI study or proof that review and post-production disappeared.

Runway and Lionsgate’s [11 June 2026 expanded partnership](https://runway.com/news/company-news/runway-and-lionsgate-expand-partnership) includes equity and plans for co-developed IP. A partnership and planned slate are commercial signals, not proof every planned title shipped profitably. Runway’s [20 August 2026 enterprise account](https://runway.com/news/company-news%2Fthe-next-phase-of-enterprise-video-generation) reports rapid growth and high net retention; these are private-company claims without an audited production-cost denominator supplied here.

### Price per generated second is not cost per finished minute

The [Runway developer pricing page](https://docs.dev.runwayml.com/guides/pricing/), checked at this cutoff, lists credits at US$0.01, Aleph2 at 28 credits/second with a 56-credit minimum, and Gen4.5 at 12 credits/second. These are provider/API-specific posted prices, not subscription entitlements or observed costs from a run.

Illustrative calculation only: at US$0.28 per generated second, a hypothetical 25% acceptance rate would mean US$67.20 in model charges per accepted minute. The acceptance rate is an assumption, not a measured benchmark. Review, fixes, editing, audio, upscaling, rendering, storage and delivery still add cost.

[Cloudflare Stream’s current pricing](https://developers.cloudflare.com/stream/pricing/) separately counts stored and delivered minutes: US$5/month per 1,000 minutes of capacity and US$1 per 1,000 delivered minutes. Delivered usage includes viewer multiplicity and some preloading/buffering. This is one service’s pricing, not a universal media cost. Interactive remote-rendered sessions have a different resource/concurrency model from replaying an encoded video; [Unreal Pixel Streaming](https://dev.epicgames.com/documentation/en-us/unreal-engine/pixel-streaming-in-unreal-engine) uses streamed runtime output rather than turning a game into a static downloadable video.

The useful business metric is total cost and time **to accepted, editable, delivered output that the customer values**, including all attempts and ongoing support. No audited cross-studio average for that metric was established in this pass. Original content economics also depend on audience/distribution; lower production cost does not guarantee attention or monetisation.

## 5. Rights, provenance and software licences are separate layers

[Adobe’s August 2026 Content Credentials guidance](https://helpx.adobe.com/firefly/web/get-started/learn-the-basics/content-credentials-overview.html) describes tamper-evident creation/edit metadata. The [C2PA technical specification](https://c2pa.org/specifications/specifications/1.0/specs/C2PA_Specification.html) makes the boundary explicit: validation concerns signed assertions and their binding/integrity, not a general determination that the scene or assertion is true. This citation is an older specification version used for the principle, not a claim that version 1.0 is the latest implementation target.

Provenance is useful for asset history, attribution and review. It does not independently grant copyright, performer permission or model-training rights. Missing credentials are not proof an asset is fake; valid credentials are not proof the depicted event occurred.

The [2025 SAG-AFTRA Interactive Media Agreement](https://www.sagaftra.org/contracts-industry-resources/interactive/2025-interactive-media-video-game-agreement) illustrates that consent/disclosure and use conditions for digital replicas can be production-contract requirements. This is a contract-specific example, not a statement of every Indian/UK performer’s legal terms.

A particularly useful model example is [F5-TTS](https://github.com/swivid/f5-tts): the repository distinguishes MIT code from CC-BY-NC pretrained models. An open code repository therefore does not establish commercial rights to every checkpoint, dataset, voice or generated use.

| Resource | Checked licence/status | Practical limit |
| --- | --- | --- |
| [OpenTimelineIO](https://github.com/AcademySoftwareFoundation/OpenTimelineIO) | Apache-2.0 core; adapters/plugins and dependencies need separate version checks. | Editorial data is not the media itself; format conversion can lose unsupported semantics. |
| [OpenUSD](https://github.com/PixarAnimationStudios/OpenUSD) | Repository supplies a specific OpenUSD licence, which should be read at the selected version. | Do not infer asset/content rights or universal renderer compatibility from source availability. |
| [Blender Studio tools](https://studio.blender.org/tools/overview/introduction) | Documentation says GPLv2-or-later for studio tools. | Tool code, Blender itself, output assets and individual dependencies have separate terms. |
| [Godot](https://godotengine.org/license/) | MIT engine with third-party notices; created game content is separately licensed. | MIT engine access does not grant rights to a downloaded asset pack or generated IP. |
| [Unreal licensing update](https://www.unrealengine.com/blog/we-are-updating-unreal-engine-twinmotion-and-realitycapture-pricing-in-late-april?lang=en-US) | Commercial/source-available product terms; use category, revenue/seat/royalty conditions and current amendments matter. | Not a permissive open-source engine. No personalised fee conclusion is made here. |
| [FFmpeg](https://ffmpeg.org/legal.html) | LGPL baseline, with build options/components that change obligations; external codec issues can be separate. | Record the actual binary/build/licence rather than labelling every FFmpeg build identically. |
| [VBench](https://github.com/Vchitect/VBench) | Apache-2.0 core. | Evaluator models, datasets and published video examples require separate checks; a metric is not a production guarantee. |
| [C2PA Rust SDK](https://github.com/contentauth/c2pa-rs) | MIT/Apache-2.0 core, separately licensed dependencies. | Local test signing is not production trust-list membership or a rights-clearance service. |
| [F5-TTS](https://github.com/swivid/f5-tts) | MIT code; CC-BY-NC pretrained models, as stated by the repository. | Model/recording/performer rights remain separate. No clone or audio generation was performed. |
| [Spring open movie](https://studio.blender.org/projects/spring/pages/about/) | CC-BY-4.0 for the film/published project data, with stated logo/trademark and third-party exclusions. | A useful permitted-fixture candidate with attribution; it has no dialogue, so is not a speech-fidelity benchmark. Nothing was downloaded. |

## 6. Ordinary jobs, research routes and public professional channels

The following are actual role descriptions or institutional/project routes, not a vacancy census, guaranteed access or salary projection. No person/company was contacted.

### India and UK role evidence

[DNEG’s Pipeline Assistant Technical Director description](https://jobs.jobvite.com/double-negative-visual-effects/job/ojV1zfwy) lists Bengaluru/Mumbai/Chennai and describes artist support, render-farm/disk/file-transfer monitoring, release feedback and Python tools. It describes progression toward pipeline specialism/supervision or R&D. Its body also contains a London-studio sentence, so exact location should be confirmed through the official channel rather than silently assuming the template is consistent.

[Ubisoft Pune’s Junior R&D Engineer, GenAI/ML](https://jobs.smartrecruiters.com/Ubisoft2/744000150941499-junior-r-d-engineer-gen-ai-ml-) supports tools, test/automation frameworks, prototypes, debugging and integration under senior guidance. This is a concrete ordinary software entry path; it does not require a portfolio consisting only of generated art. Its [R&D C++ role](https://jobs.smartrecruiters.com/ubisoft2/744000155725659) separately describes deeper automation/engine integration and experience requirements. The [technical architect role](https://jobs.smartrecruiters.com/Ubisoft2/744000155903584-technical-architect) shows a longer-term production-services leadership path; it asks for substantial experience, not a 90-day certificate.

For the UK, [ScreenSkills’ pipeline TD profile](https://www.screenskills.com/job-profiles/browse/visual-effects-vfx/technical/pipeline-technical-director-td/) describes Python/C++, DCC/pipeline knowledge, communication with artists and an assistant-TD route; it explicitly says pipeline TD is not entry-level. [Framestore’s London page](https://framestore.recruitee.com/london-studio) provides studio/career information but showed no featured open positions when checked. Do not count an expression of interest, talent community or old listing as a funded current vacancy.

### Teams, labs and contribution paths

| Organisation/researcher | Relevant branch and useful first contribution | Public professional channel |
| --- | --- | --- |
| Academy Software Foundation / OpenTimelineIO | Editorial interchange, round-trip/cut semantics, media-link validation and production tooling. | [Official OTIO repository](https://github.com/AcademySoftwareFoundation/OpenTimelineIO) contribution guidance and public issues. |
| Pixar/OpenUSD community | Asset/scene identity, dependencies, time-sampled interchange and compatibility tests. | [Official repository](https://github.com/PixarAnimationStudios/OpenUSD) and its contribution guidance. |
| Blender Studio and development community | Open production tools, artist workflow, dependency/render operations and reproducible bug reports. | [Studio tools](https://studio.blender.org/tools/), [design principles](https://studio.blender.org/tools/pipeline-overview/design-principles) and project contribution channels. Production access/assets can have separate subscription/licence conditions. |
| Google DeepMind Veo/Genie, Runway, Adobe production teams | Controlled generation/editing, temporal evaluation, application integration and production constraints. | Official research/product/API pages cited above; no assumption that proprietary model weights or a research role are openly available. |
| VBench researchers; Ziqi Huang is named by the repository as a contact | Evaluation implementations, failure cases and metric-to-human agreement. | [VBench public repository](https://github.com/Vchitect/VBench) issues/contribution route. |
| UCL geometry/creative-AI group; Niloy J. Mitra; Adobe collaborators Shariq Farooq Bhat and Kalyan Sunkavalli | Spatial blocking, motion/disocclusion, 3D/animation and directorial interfaces. | [Institutional publications](https://geometry.cs.ucl.ac.uk/publications.php), [LooseControlVideo paper](https://arxiv.org/abs/2606.19495), [Motion/Disocclusion project](https://anranqi.github.io/jackinbox/). Accepted/listed papers are not automatic code releases or job offers. |
| University of Bath CAMERA; Neill Campbell and Darren Cosker appear in its project record | Motion capture, human/character behaviour and creative-industry research. | [Official research-project/output record](https://researchportal.bath.ac.uk/en/projects/centre-for-the-analysis-of-motion-entertainment-research-and-appl-3/publications/?type=%2Fdk%2Fatira%2Fpure%2Fresearchoutput%2Fresearchoutputtypes%2Fcontributiontojournal%2Farticle). Current funded posts/equipment access need separate checking. |
| IIIT Hyderabad CVIT; Vineet Gandhi | Computational cinematography, multimedia, tracking and editing/vision research. | [Official institutional profile](https://www.iiit.ac.in/faculty/vineet-gandhi/) and linked publication routes. A separate CVIT faculty-list URL returned unrelated gambling content and was excluded as a reliable source. |
| IIT Bombay; Avinash Sharma | 3D human/garment/face/hand modelling and graphics/AR/VR. | [Department’s 10 September 2026 faculty announcement](https://www.cse.iitb.ac.in/news). This checks his current institutional move rather than relying on older IIIT-H/IIT-Jodhpur affiliation. |
| DNEG, Ubisoft production services and other studio tools teams | Artist-facing tools, testing, asset processing, pipeline integration and support. | Official role pages above. A good artefact solves a real workflow problem and explains adoption/support, not only an impressive model demo. |
| Content Authenticity Initiative/C2PA implementers | Asset manifests, signing/validation and provenance-preserving pipeline tests. | [c2pa-rs](https://github.com/contentauth/c2pa-rs) issues, contribution guidance and specification links; no outreach sent. |

## 7. Primary papers/artefacts to examine, with limits

- [VBench 2.0, 2025](https://arxiv.org/abs/2503.21755): ask whether benchmark gains correspond to the actual revision/continuity failure that matters to a creator. Core code is available; dependencies/data terms differ.
- [OmniEdit-Bench, v2 September 2026](https://arxiv.org/abs/2608.05049v2): examine task coverage and whether metrics reward doing the requested edit rather than preserving attractive input. Metadata/abstract were checked; no benchmark was run.
- [LooseControlVideo, June 2026](https://arxiv.org/abs/2606.19495): investigate sparse 3D blocking versus dense control, trajectory/occlusion errors and authoring effort. Do not infer full artist editability from generated output quality.
- [Motion and Disocclusion Control, 2026](https://anranqi.github.io/jackinbox/): a useful design-space decomposition with synthetic/captured scenes. Code was marked coming soon at this check; benchmark-reproduction access is therefore incomplete.
- [Building Pretraining Data for World Models, September 2026](https://arxiv.org/abs/2609.03557): authors separate trajectory/state generation from offline rendering and discuss pipeline failures. This is a recent preprint, not proof every real-time engine replay is numerically deterministic.
- [F5-TTS, 2024](https://arxiv.org/abs/2410.06885): connect speech fluency/fidelity claims to the actual text, timing, pronunciation and licensing requirements. Model training and performance were not reproduced here.
- [Blender Studio production-pipeline documentation](https://studio.blender.org/tools/): a maintained, production-used reference for workflow design, rather than assuming a bespoke all-in-one agent should replace every mature component.

## 8. Proposed 30/90-day software projects, with baselines and kill criteria

Choose one main track. These are research designs only. No video/audio/image generation or rendering happened. Use existing approved software and owned/permitted fixtures; obtain any needed software/model/data/resource approval when implementation is requested. Do not redistribute third-party demos or assume an academic dataset permits commercial training.

### C1 — Editorial/asset integrity and revision tool

**First 30 days:** define an asset manifest and a small editorial timeline from existing owned/permitted clips. Represent source identity, hash/version, timebase, in/out, audio channels, subtitles and attribution. Compare a manual spreadsheet/file-naming workflow with a metadata validator and, if already available, an OTIO round trip. No new rendered video is necessary for the initial structural tests.

**By 90 days:** handle missing assets, mixed rates, overlapping cues, relinks, alternate cuts and a later revision. Measure invalid references, timing drift, lost semantics, time to resolve an artist request and reproducibility of the chosen outputs. Keep generated and authored sources traceable through the same structure.

**Kill/limit:** round trips silently lose critical effects/timings; users cannot make ordinary revisions; automation saves no total time once correction is counted. Original contribution: a format/adapter edge-case test, media-link validator or production-ready revision workflow.

### C2 — Local video-edit correctness benchmark

**First 30 days:** specify a permitted fixture set with exact requested edits, time/mask/object annotations and unchanged regions. Use existing public/owned outputs where licences allow, or prepare the benchmark without running models. Compare a mature manual/compositing workflow, a simple baseline and candidate model results only when legitimately available. Separate aesthetic preference from pass/fail requirements.

**By 90 days:** add occlusion, camera movement, repeated character/object identity, scene text, longer clips and a second revision. Blind reviewers to method. Record instruction success, preservation, temporal failures, reviewer agreement, attempts, manual repair minutes and total cost per accepted second.

**Kill/limit:** the metric rewards a no-op; a changed logo/name slips through; flow/embedding/LLM scores contradict labelled ground truth; a curated subset hides retries. Original contribution: an independent oracle, actionable failure set or stronger evaluation of an existing editor.

### C3 — Audio/subtitle/delivery QA without voice generation

**First 30 days:** use explicitly permitted existing audio and transcripts/cues, or define owned recording fixtures for later. Validate channels/sample rates, duration, cue overlaps, named words, silence/clipping and expected timeline alignment. Compare manual QA against automated checks with seeded known faults. No cloned voice or new audio generation is needed.

**By 90 days:** test a different language/accent, noisy material, timing revision and variable-rate picture. Measure missed/false findings, timing error, word/name error, reviewer time and actual playback correctness. Use listening/linguistic review where metrics cannot settle meaning/performance.

**Kill/limit:** ASR is treated as unquestionable ground truth; “nice voice” masks wrong dialogue; language meaning or performer terms are ignored; error correction costs more than the saved review. Original contribution: a precise AV/caption regression suite or editor-integrated diagnostic tool.

### C4 — Provenance-preserving asset catalogue

**First 30 days:** build a local catalogue of permitted fixtures recording asset/source, licence/attribution, tool/model version, transformations, approval and dependency relationships. If SDKs are already available, use local test manifests/signing only. Test missing, mismatched and modified metadata; a provenance-free item should remain “unknown,” not automatically “fake.”

**By 90 days:** test relinking, legitimate transcoding/editing, redaction, broken dependencies and export/import through a chosen production tool. Measure provenance loss, false assurance, attribution completeness and investigation time. Keep technical signature validity, content assertions and rights clearance as separate fields.

**Kill/limit:** valid signatures are marketed as truth/ownership; a tool strips the chain without detection; rights metadata is copied forward without a source; production trust is implied from a self-signed test. Original contribution: preservation/conformance tests, a useful adaptor or a clearer provenance failure model.

### C5 — Interactive-state and world-model evaluation harness

**First 30 days:** define a tiny headless game/state task with explicit actions, inventory/object state, collisions/constraints, save/load and an authoritative reference implementation. No rendering is required to test state semantics. For any permitted published model-output fixture, annotate only observable actions/outcomes; do not infer hidden state or production performance from a demo.

**By 90 days:** add replay, return-after-occlusion, repeated interactions, alternate action ordering and multi-agent conflicts. Compare a mature authored-state baseline with legitimate world-model outputs only if access/permissions/resources are authorised. Measure task success, invariants violated, persistence, latency, recovery and reproducibility independently of visual appeal.

**Kill/limit:** a visually plausible response is scored as a correct rule transition; no ground truth exists for the claimed capability; hidden game state is inferred from a frame; cost/latency makes the actual interactive task unusable. Original contribution: a causal/persistence benchmark, trace schema or engine-to-evaluation bridge.

### C6 — Production job/streaming reliability and cost audit

**First 30 days:** model a small batch of media jobs using existing permitted files/metadata and a mature tool’s documented states. Compare naive retry with idempotent task/dependency handling in a local simulator; no render jobs or paid endpoints are necessary for the research phase. Account for all attempted, accepted and delivered units separately.

**By 90 days:** with later authorised local resources, validate failure recovery, missing assets, version changes, job cancellation and viewer/playback conditions. Measure duplicate/lost work, operator minutes, turnaround, resource utilisation, delivery errors and total cost. Distinguish simulator evidence from actual renderer/streaming throughput.

**Kill/limit:** only successful jobs count; retries create untracked charges; simulation is claimed as production capacity; viewers cannot play the delivered result correctly. Original contribution: job-state diagnostics, cache/provenance integration, delivery-QC tests or a cost ledger that makes production decisions clearer.

## 9. Expertise and leadership evidence by 2031

The durable skill stack is programming/systems plus time, colour/audio, geometry/animation or interaction semantics, followed by production workflow knowledge. Learn one artist-facing application/engine deeply enough to understand the actual revision loop. Use mature interchange and production frameworks before inventing a complete replacement. AI-assisted code can accelerate implementation, but an unseen timebase, clip, character, language or action sequence should test whether the engineer understands the system independently.

Leadership comes from getting a useful tool or standard adopted, maintaining it through show/game revisions, mentoring others and producing evidence that it saves total time without breaking quality/rights/delivery requirements. Valuable original work includes an adapter fix, temporal bug, reproducible benchmark, improved oracle, accessibility/localisation test or robust production integration. No publication, contribution or outreach was performed here.

## Remaining gaps and source-quality notes

- No media model/editor was run and no video was generated/rendered. Product controls and performance are reported from primary documentation/papers, not independently verified outputs.
- Acceptance rates, retries, repair effort and complete studio unit economics are usually absent from public case studies. The proposed projects explicitly collect these denominators.
- Model-code, checkpoint, dataset, asset, performer and distribution rights need separate checks for any selected implementation. Contract examples do not establish universal law.
- Live job pages can be templates, stale vacancies or expressions of interest. The DNEG location mismatch and Framestore absence of featured jobs are retained rather than converted to confident vacancy claims.
- One CVIT faculty-list URL returned unrelated gambling content and was excluded; the official IIIT Hyderabad institutional profile was used. Current affiliation matters: IIT Bombay’s September 2026 announcement was used for Avinash Sharma.
- Several recent research artefacts are preprints or have incomplete code access. No replication, full-paper review of every method, dataset-rights audit or user study was completed.
- Prices and API availability can change. Listed prices are public checks at this cutoff and hypothetical calculations, not purchased usage or an account entitlement check.
