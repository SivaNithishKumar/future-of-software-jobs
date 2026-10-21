# Operational weather decisions: issue-time evidence before another model

Checked **20 October 2026** after reading the climate-water, geospatial and independent hydrology notes and source index. Those reports already cover basin models, reanalysis leakage and operator decisions. The uncovered question is narrower: **can a developer reconstruct a forecast that was actually available before a decision, verify the matching outcome and show value after delivery/data costs?** This pass audits three operational/data artifacts and proposes a tiny model-free replay. The [structured attachment](weather-decision-option-round13.json) records versions, rights, source pins, proposed nodes, contacts and unresolved gates.

AI forecasting has a concrete operational milestone here. The opportunity for a software engineer is also concrete: forecast/observation adapters, metadata and issue-time lineage, uncertainty verification, model-change handling and decision integration. These functions do not imply rising job counts, profitable products or automatic access to a meteorological research post.

## 1. AIFS v2 is operational; the comparison contract still matters

[ECMWF's current dataset page](https://www.ecmwf.int/en/forecasts/datasets/aifs-machine-learning-data) identifies AIFS Single and ENS **v2**, implemented on **12 May 2026**. The [ENS model card](https://huggingface.co/ecmwf/aifs-ens-2.0) describes a 51-member, 15-day, six-hourly forecast, run four times daily. This is deployed forecast production, not merely a research leaderboard.

The particularly useful methodological source is [*Adapting the AIFS for 50r1*, 12 May 2026, DOI 10.21957/3c84860825](https://www.ecmwf.int/en/about/media-centre/aifs-blog/2026/adapting-aifs-50r1). Changing the physics-based initial analysis changed AIFS behaviour and the verification comparison. The article distinguishes v2-from-50r1 versus v1-from-49r1 from a comparison using the same analysis cycle. Improvements under one comparison do not isolate a neural architecture effect, and degradation against a changed analysis need not mean the same degradation against observations. Preserve the strong physics-based IFS reference and the matched-input comparison.

The [selected ENS scorecard](https://sites.ecmwf.int/aifs/scorecards/AIFS-ENS-v2%20vs%20AIFS-ENS-v1.html) displays dates **28 January–10 March 2026**, leads 24–240 hours and analysis/observation reference options. That evaluation predates v2 deployment. It can support model assessment without implying that a customer could receive operational v2 output on those January issue dates. No scorecard values, missing-case population or model run were independently reproduced here.

A release identifier does not settle every reproducibility detail. The model card separates **CC BY 4.0 weights** from **Apache-2.0 example scripts** and says the prototype 50r1 analysis data used for fine-tuning are unavailable to users. Running released weights and reconstructing training are different access problems. Some card/history text also mixes Single/ENS wording; an older ENS-v1 date conflicts with the July-2025 operational announcement. The current v2 date agrees across the inspected surfaces. No training reconstruction or silent repair of the older chronology is claimed.

Global skill and proper-score training do not establish calibrated local probabilities for every lead, season or extreme. A sensible comparison specifies variable, reference, grid/station mapping, model/analysis version, issue date, lead, ensemble and observation exclusions. CRPS, event Brier score, reliability, sharpness and tail behaviour answer different questions. Ensemble members and adjacent weather days are dependent; their number is not the number of independent verification events.

## 2. Public historical access exists, with important layout and lineage limits

The [ECMWF real-time portal](https://www.ecmwf.int/en/forecasts/datasets/open-data) retains the latest **12 runs**, about two–three days. Historical AIFS through MARS requires registration. That is an important default-access boundary, but **it is not evidence that all historical AIFS access is gated**.

The counterexample is [dynamical.org's AIFS ENS archive](https://dynamical.org/catalog/ecmwf-aifs-ens-forecast/), documented from **2 July 2025**. It preserves `init_time`, `lead_time` and `ensemble_member` and states CC BY 4.0 plus ECMWF terms. Its temperature field is Celsius, requiring an explicit conversion for the Fahrenheit station/MOS comparison below. Its [STAC collection](https://stac.dynamical.org/ecmwf-aifs-ens-forecast/collection.json) identifies dataset version `0.1.0`; that encoding/data-product version is not AIFS model version 0.1. A transformed historical archive can preserve a model run without proving original public availability, first receipt or every later correction.

Its layout also challenges an apparently tiny experiment: one spatial chunk includes all 61 leads and 51 members over 32×32 grid points, listed as **12.2 MiB uncompressed**, inside much larger shards. Selecting one point/lead does not necessarily read only those values. Compression, HTTP range access, shard indexing and caching determine actual traffic; none was measured. The provider's [August update](https://dynamical.org/updates/2026-08-31/) extended the old `data.dynamical.org` endpoint only through 30 September. Use current STAC discovery and an immutable snapshot when available, rather than an old notebook URL. The validation report was inaccessible in this pass.

This preserves both sides of the evidence: an open historical alternative exists, and a reproducible operational replay still needs provider transformations, missingness, model vintage, snapshot and receipt lineage. ERA5/reanalysis, retrospective model evaluation, historical operational runs and records of what a particular consumer received are distinct objects. A source timestamp called “initialisation” cannot stand in for all of them.

### Account for the whole running/data path

| Boundary | Costs/evidence to retain |
|---|---|
| Produce a global forecast | Observation ingestion/assimilation, initial states, interpolation, model members/horizon, memory, warm-up and output encoding |
| Consume public output | Network bytes, range/chunk behaviour, decompression, cache/storage/egress, retries and delivery lag |
| Make a dependable local product | Postprocessing, calibration/reference data, observation QC, monitoring, version migration, missing-feed fallback and human review |
| Change a real decision | Physical response model, constraints, action/miss costs, delayed/lost opportunities and operating evidence |

No all-in dollars, joules or local inference requirement was measured. Training hardware is not a per-forecast inference benchmark. Consuming an externally produced forecast avoids running the model locally; it does not make its upstream computation or the user's integration effort free.

## 3. A strong tiny baseline: archived station MOS and observations

[IEM's MOS archive](https://mesonet.agron.iastate.edu/mos/) provides an established NWS point-forecast product, including GFS/MAV, without requiring a new global model. Its [public CGI documentation](https://mesonet.agron.iastate.edu/cgi-bin/request/mos.py?help) supports station/model/time-range GET requests. The [IEM disclaimer](https://mesonet.agron.iastate.edu/disclaimer.php) explicitly places website materials in the public domain for lawful use. Preserve original NWS/IEM attribution and the service's reliability limitations; do not relabel that statement as a particular CC0 licence.

The current service source was read at **`akrherz/iem` commit `3ec0e2a26d998a95c244dfb88823c93bf260f7dc`**. It queries by `runtime`, returns `ftime`, includes both ends of the requested runtime interval and drops entirely null columns. Client keys, half-open windows, de-duplication and optional-column handling therefore matter. The source pin does not freeze the database. [MOS request path L91–121](https://github.com/akrherz/iem/blob/3ec0e2a26d998a95c244dfb88823c93bf260f7dc/pylib/iemweb/request/mos.py#L91-L121)

The accessible first task uses **KAMW/Ames**, 00 UTC GFS MOS, one 24-hour-valid `TMP` value per run, paired with **AMW in IA_ASOS**. [Station metadata](https://mesonet.agron.iastate.edu/sites/site.php?station=AMW&network=IA_ASOS) establish the site and archive context. The [historical official GFS bulletin format](https://www.weather.gov/media/mdl/mdltpb05-03.pdf) describes whole-degree Fahrenheit `TMP` and `999` missing; [observation documentation](https://mesonet.agron.iastate.edu/request/download.phtml) describes `tmpf`, valid timestamps and missing/QC ambiguity. Actual current payload/schema/sentinel behaviour must be checked before scoring. Payload retrieval attempts failed through the web tool; that does not prove the public service is unavailable or requires authentication.

A probability/precipitation extension needs a stronger target oracle. The observation service's selected fields include `p01i`, not a ready-made `p06i`; hourly reset periods vary and frozen-precipitation handling is incompletely known. Summing arbitrary reports into six hours is not automatically a valid MOS-P06 label. The first project deliberately avoids disguising that unresolved measurement problem. [ASOS fields L64–92](https://github.com/akrherz/iem/blob/3ec0e2a26d998a95c244dfb88823c93bf260f7dc/pylib/iemweb/request/asos.py#L64-L92), [provider variable caveats](https://mesonet.agron.iastate.edu/request/download.phtml)

## A no-new-model/no-hardware 30/90-day experiment

Choose one narrow archive-and-decision proof. Assume **25–40 focused hours initially**, then **50–90 additional hours**; these are planning assumptions. No forecast payload, model, package or archive chunk was downloaded here. The attachment contains precise query templates and proposed caps: seven pilot runs, 256 KiB per response, 25 MiB total forecast/observation traffic, bounded retries and at least one second between requests. Real response sizes/access remain launch gates.

**First 30 days:** define the UTC/station/unit/missing contracts and use at most seven runs from the declared **January–March 2025** window. Keep model-reference runtime, publication metadata if available, actual receipt/retrieval, decision time, forecast valid time and verification time separately. Retain raw bodies, query, hash, headers, schema and revisions. A later retrieval of a historical run does not prove it arrived before the historical decision.

Use a chosen verification rule: nearest valid nonmissing station-temperature report within ±10 minutes of the forecast instant, ties earlier; record the time offset and abstain on absent/ambiguous reports. This defines a near-time screen-temperature task, not exact physical truth at an instant or a canopy/road-surface temperature. An independent setter should prepare fresh unit, time, revision, duplicate and missing-code cases and expected outcomes before implementation. Known self-authored fixtures remain exposed design checks.

**Days 31–90:** extend within caps, compare the existing MOS product with persistence using the latest observation actually available at decision time and with always/never-protect policies. An optional calendar baseline uses only earlier records. Historical cases without release/receipt proof must remain **assumed-availability replay**. A later authorised prospective capture could record first receipt before outcomes; no recorder or recurring task was started by this report. Use a declared runtime+6-hour decision cut, and include late/missing forecasts with a fixed fallback instead of deleting them.

Report MAE/RMSE/bias, threshold confusion counts, missing/late/abstention coverage and hypothetical action cost. A 32°F screen-temperature threshold is an educational action rule, not crop or transport advice. Use time/event-block uncertainty and disclose sparse tails. A confidence interval for mean forecast error is not predictive-probability calibration. Fit no new forecasting model or recalibration model.

An optional **AIFS public-mirror read-size/provenance pilot** can inspect at most one–two initialisations within the remaining cap, only if approved existing codecs and bounded range reads are available. Such a tiny slice cannot establish ensemble calibration. Broader AIFS/MOS comparisons require a matched later period, weather-model version, grid/station treatment, data budget and independent event oracle. Do not silently expand downloads or replace original receipt history with archive backfill.

The acceptance gates are concrete:

- All critical invalid fixtures—future inputs, later revisions backfilled into an earlier decision, wrong units/station/valid time, `999` as temperature, missing as zero—are rejected or explicitly unknown.
- Every scored pair has unique keys, lineage, verification offset and an availability proof label. Source data, client parsing and outcome correctness use separate checks.
- All intended decision opportunities are counted, including delivery failures. A positive gain is optional; a well-supported negative result is useful.
- A probability task starts only after a probability/interval/observation oracle is independently verified. Reliability/Brier/CRPS and event counts are then reported for their proper targets; a handful of examples cannot certify extremes.
- No real customer cost, physical response or authorised operating decision means the result remains hypothetical sensitivity analysis.

A tiny self-authored calculation illustrates the last point. With true temperatures 31/33°F, forecast A gives 31.9/32.1, forecast B 32.1/33. B has lower RMSE (about .778 versus .9), yet under a 32°F action threshold, protection cost 1 and unprotected event loss 10, A costs 1 and B costs 10. Those invented values show a metric/decision distinction; they are not a weather result or monetary return.

## Where decision value and access become domain-specific

For energy, weather must map to actual power/plant availability, curtailment and settlement-time information. For agriculture, screen temperature or rainfall must map to soil/canopy conditions, crop response, management and feasible intervention. For transport, route exposure, lead time and the action window matter. A good station score cannot supply those layers. A 15-day forecast also does not establish seasonal skill: seasonal anomalies, start month, model drift, matched multi-year reforecasts and independent years need a separate protocol.

| Official team/role evidence | Reachable contribution and real barrier |
|---|---|
| [ECMWF/AIFS](https://www.ecmwf.int/en/forecasts/datasets/aifs-machine-learning-data), [Anemoi inference](https://github.com/ecmwf/anemoi-inference), [jobs](https://www.ecmwf.int/en/about/jobs) | Data/model adapters, verification and reproducibility; Reading/Bologna/Bonn. No specific current engineering vacancy, nationality or visa eligibility verified. Research-model work adds domain/mathematical depth. |
| [Met Office Foundation Scientific Software Engineer 1488](https://careers.metoffice.gov.uk/join-us/search-our-jobs/Urban-scale-Prediction-Foundation-Scientific-Software-Engineer-1488) | Code, ML interest, QA, requirements and communication; listed essentials do not require a PhD. One vacancy at two grades, deadline 1 November. UK work eligibility plus role-specific residency requirements remain substantial gates. |
| [IITM Pune AI/ML/DL centre](https://tropmet.res.in/313-news_details) | India Earth-system problems/capacity-building; official professional channel Dr Suryachandra Rao, `surya@tropmet.res.in`. No advertised role/funding eligibility established. |
| [NISE April-2026 notice](https://nise.res.in/uploads/pages/17764051665697-advt-for-senior-project-scientist-dated-17-04-2026.pdf) | A concrete solar-probabilistic/DSM function: relevant BTech+8 years or MTech/MS+4; Indian citizenship and age conditions. Historical short-contract notice, not presented as open; a small project does not replace that experience. |
| [IEM](https://mesonet.agron.iastate.edu/mos/), [dynamical.org](https://dynamical.org/catalog/ecmwf-aifs-ens-forecast/) | Public archive/schema/validation contributors; official team/issue channels are recorded in the attachment. Public contribution does not establish a paid opening. |

For the Met Office example specifically, security eligibility requires three of the last five years resident in the UK, including the two immediately preceding application; the rule is not generalized to all weather employers. Public channels include `careers@metoffice.gov.uk`, IEM's official footer contact, `feedback@dynamical.org` in the AWS registry and project issue forums. No outreach, application or account access occurred. Third-party Meteomatics software-job copies were excluded; its inspected official page did not establish an engineering vacancy.

The transferable route is software/data/verification first, with meteorology and statistics learned around one actual forecast/decision contract. Original contributions can be a meaningful issue-time regression, observation/forecast join, missingness validation or a reproducible failure in a mature adapter. Standardized providers and AI-assisted tooling may automate much of this work; no source establishes permanent scarcity or 2031 hiring growth. Domain access and operating evidence may matter more than another model demo.

## Validation and remaining uncertainty

The attachment distinguishes observed sources, proposed experiments and future hypotheses, with 22 source records, three artifacts, seven directory records and five proposed taxonomy nodes. Exact IEM source/licence files were read; its database and forecast payloads remain unverified. The mirror's data/schema version and layout were read, but its validation report, immutable snapshot/current asset resolution and actual range-read traffic remain gates. No source/index/tree was changed, model/forecast bulk downloaded, account/gate accepted, package installed or upstream code run. Only the tiny illustrative arithmetic was executed.
