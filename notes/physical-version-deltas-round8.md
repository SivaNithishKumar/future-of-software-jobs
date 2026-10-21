# Three substantive paper-version deltas

Audit completed 20 October 2026, Asia/Kolkata (19 October UTC). This compares DeepFleet v1→v3, Prithvi-EO-2.0 v1→v3 and TerraMind v1→v5. The separate Prithvi orbital paper, arXiv:2512.01181v1, is not a revised version of the EO-model paper and acquires no new operating evidence from these revisions.

The result is mixed: **DeepFleet's inspected evaluation remains the same; Prithvi changes several adaptation experiments and corrects denominators; TerraMind adds useful diagnostics while retaining its central benchmark scores.** None supplies new evidence here of customer ROI, accessible job volume or autonomous scientific correctness. Earlier results remain version-specific historical findings.

## Comparison method and access

The six exact-version HTML documents were read in overlapping slices and checked for full line coverage: DeepFleet 547/574 lines; Prithvi 424/742; TerraMind 439/500. Citation-number/reflow normalization helped identify candidate differences; tables and relevant methods were then checked explicitly. This is document analysis, not model reproduction, statistical reanalysis or a byte-for-byte PDF comparison. No software, models, datasets, paid runs, hardware, private systems or outreach were involved. Round 6/7 catalogues and prior reports remain unchanged.

| Work | Historical source | Current source | Access and date distinction |
|---|---|---|---|
| DeepFleet | [v1, 12 August 2025](https://arxiv.org/html/2508.08574v1) | [v3, 13 April 2026](https://arxiv.org/html/2508.08574v3) | Exact PDFs also readable: [v1, 25 pages](https://arxiv.org/pdf/2508.08574v1), [v3, 27 pages](https://arxiv.org/pdf/2508.08574v3). |
| Prithvi-EO-2.0 | [v1, 3 December 2024](https://arxiv.org/html/2412.02732v1) | [v3, 6 March 2026](https://arxiv.org/html/2412.02732v3) | Exact PDF endpoints failed; exact-version HTML was available in full. |
| TerraMind | [v1, 15 April 2025](https://arxiv.org/html/2504.11171v1) | [v5, 17 June 2026](https://arxiv.org/html/2504.11171v5) | Same PDF access limitation; complete versioned HTML, including appendices, was read. |

## DeepFleet: evaluation survives; the rival story improves

The substantive body comparison finds the same state/action representation, deterministic rollout logic, architecture configurations and Table 2 results. Both evaluate 60-second forecasts against seven held-out floors over seven days. These are prediction endpoints rather than a measured production-throughput intervention. The unequal training sizes and model capacities still prevent a clean architecture-only causal comparison. The added pages are not evidence of a larger operating trial. See both versions' §§3–5, Table 2 and §9. [v1](https://arxiv.org/html/2508.08574v1), [v3](https://arxiv.org/html/2508.08574v3)

The consequential addition is §2: v3 gives stronger treatment to classical MAPF solvers, physical-model limitations and search guided by learned predictions/edge weights. This narrows any suggestion that a learned fleet foundation model replaces conventional coordination wholesale. No newly released training corpus/checkpoint was established in either document. [v3 §2](https://arxiv.org/html/2508.08574v3)

**Disposition:** retain the earlier typed-state/learned-prediction observation and the private-data replication barrier. Strengthen the baseline requirement: compare matched useful work and runtime with a mature search/scheduling method, including hybrids. Do not turn unchanged forecasting accuracy into proved congestion reduction, staffing demand or useful-hour economics. The old results can now be described as explicitly rechecked in v3, with the same endpoint boundary.

## Prithvi: preserve results by experiment, not by model name

Core pretraining persists: 4.2M training/46k validation samples, four timestamps, six HLS bands at 30 m, and 2014–2023 imagery. Final tile counts clarify exclusions. The inspected flood, wildfire, US-crop and Sen4Map rows retain their numbers. Added PASTIS and ten-run benchmark tables expand evaluation without proving operational transfer. [v1 §§2–4](https://arxiv.org/html/2412.02732v1), [v3 §§III–IV, Appendix A](https://arxiv.org/html/2412.02732v3)

| Experiment | v1 statement/result | v3 statement/result | Required interpretation |
|---|---|---|---|
| Burn severity | Small-image and validation descriptions conflict internally; 150 epochs, convolutional decoder; 300M mIoU 29.4. | 224-pixel inputs, held-out test, UPerNet/LoRA, 50 epochs; 300M mIoU 31.2 versus ResNet-50 U-Net 28.8. | Changed adaptation/assessment; not a measured improvement from a new base model. |
| Low-label landslides | 100 images; 600M mIoU 67.1. | 50 images; 600M mIoU 67.0. | Different data budget; do not compare these as the same assay. |
| Full landslides | Lovasz row labelled 600M despite prose saying 300M. | Row labelled 300M; numerical result retained. | Label correction, not a new gain. |
| Biomass | Test RMSE 54.51 versus baseline 27.49. | Best optical/12-frame/LoRA RMSE 33.40; baseline remains 27.49. | Better revised adaptation still loses; adding SAR did not improve this setup. |
| GPP | Caption says 975 towers; body says 37 sites/975 samples. | Caption corrected; XGBoost/ResNet comparisons added. | Leave-one-year-out is not unseen-site validation. |

Source locations: [v1 Tables 6–8,12–13](https://arxiv.org/html/2412.02732v1); [v3 Tables VI–VIII,XIII–XV; §§III-C2,IV-B,IV-D](https://arxiv.org/html/2412.02732v3).

**Disposition:** keep the general finding that released pretraining can support several tasks and that cheap/specialist baselines remain essential. Revise any universal-superiority wording. Every claim must identify the input window, decoder, loss, adaptation method, label budget and split. The biomass result is direct contrary evidence to a blanket advantage from either a foundation model or additional sensors. The GPP correction changes the apparent independent sampling scale dramatically; repeated observations at existing sites cannot support a claim about new sites.

The hyperparameter tool changes from forthcoming to a repository pointer; exact configurations, manifests and hashes still need matching. The checked 300M Hub revision cannot stand for every 600M experiment. Paper v3 does not mean Prithvi model version 3.

## TerraMind: useful new diagnostics, mostly stable central outcomes

Core dataset/modality and training descriptions remain consistent across revisions: TerraMesh and the named TerraMindv1 model family persist. The water-body zero-shot table retains 45.40/69.75 IoU for two variants; v5 fixes a variant attribution and the DeCUR comparison in surrounding prose. Main-table presentation changes should not be counted as new benchmark wins: task-specific U-Net/ViT comparisons were already in v1's appendix. The retained nine-task average mIoUs are 58.35/59.57 for base/large versus 57.58 U-Net; two unreproduced tasks remain excluded. [v1 §§5,12](https://arxiv.org/html/2504.11171v1), [v5 §§5,11](https://arxiv.org/html/2504.11171v5)

V5 adds quantitative generation diagnostics. For optical→DEM, reported RMSE is 745.5 m despite SSIM 0.942; image structure and physical accuracy are different endpoints. Geolocation analysis also describes nearest-seen-location behavior and urban/bare-land confusion. Tokenizer detail and a more explicit TiM formulation improve methodological inspection, without establishing a new base checkpoint. Both revisions retain inconsistent base-training duration statements in main text versus appendix; that resource denominator needs reconciliation. [v5 Table 3, §§4,9,11–12](https://arxiv.org/html/2504.11171v5)

**Disposition:** preserve the inference that generated modalities may aid a particular downstream task, while labelling them predictions throughout the pipeline. They are not substitute ground-truth measurements, uncertainty estimates or independent safety evidence. The revised text strengthens the case for physical-unit validation and independent labels. The small average advantage on the retained benchmark cannot be generalized to all tasks, particularly when protocol failures removed two tasks. The existing flood-project gate should distinguish binary water mapping from transient-flood delineation and test a cheap matched-input baseline.

## Artifact terms and implications that do not change

The article licenses remain unchanged: DeepFleet/TerraMind display arXiv's non-exclusive distribution license; Prithvi displays CC BY 4.0. These do not determine code, weights or data rights. TerraMind's abstract changes from a planned release to model/code links, while dataset-release language elsewhere remains prospective. Round 7 separately inspected pinned Apache-2.0 code/model surfaces; neither paper revision establishes an immutable mapping between every reported experiment and those artifacts.

No orbital, physical safety, intervention-cost or paid-work conclusion is upgraded by these comparisons. The independent orbital audit remains [arXiv:2512.01181v1](https://arxiv.org/html/2512.01181v1), with its own uploaded-data/runtime boundary. The career inference stays conditional: adaptation, data quality and evaluation are technically useful work; evidence of durable hiring scarcity or a defensible standalone product still needs paid workflow and cost denominators.

## Bounded follow-through

Use one declared experiment and its version-specific oracle before extending the project. For DeepFleet, a public synthetic scheduler comparison remains an educational analogue rather than a reproduction. For Prithvi, select one adaptation protocol and independently match input sizes, label budget and held-out groups. For TerraMind, compare real inputs with generated augmentation under a fixed downstream metric and report physical-unit errors separately from visual similarity. Stop if the result relies on unmatched versions, changed data budgets, unverified reference labels or inaccessible artifacts. No new installation, model/data retrieval or experiment is authorized or performed by this audit.

Record-linked proposals are in `physical-version-deltas-round8-updates.json`. They add current-version assessments and matching gates while preserving prior statements as historical; they do not modify the frozen catalogue or apply round 7 repairs.
