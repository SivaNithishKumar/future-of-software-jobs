# FAIR-MAST minimum archive access, round 14

20 October 2026. **A tiny actual archive-metadata fixture is now verified.** Three complete Zarr v3 JSON objects for the documented shot 30421 summary group returned successfully, totaling 2442 retained body bytes. They identify plasma-current units **A**, time units **s**, matching shape **[767]** and dimension **time**, a CC-BY-SA 4 resource license, and ingestion provenance. This resolves the narrow metadata-access question; it does not accept numeric-data, runtime, scientific-oracle or project-launch gates.

## What changed from round 13

Read the round 13 readiness assessment/receipts, nuclear/fusion report and energy metadata repairs first. The earlier literal v2 objects—summary/ip/.zattrs, summary/ip/.zarray and summary/time/.zattrs—returned 404; one catalogue request timed out. Those historical observations remain frozen and are not service-wide conclusions. None of those URLs was repeated.

The [current pinned source](https://github.com/ukaea/fair-mast/tree/6c9573d43440941ea2dad3ff80cc194d4814e7b4), independently reconfirmed as checked HEAD, supplies a new layout hypothesis. Its [level2 notebook](https://github.com/ukaea/fair-mast/blob/6c9573d43440941ea2dad3ff80cc194d4814e7b4/docs/level2-data.ipynb) explicitly says stores currently carry mixed v2/v3 metadata and shows Zarr 3 FsspecStore/xarray access. The [quickstart](https://github.com/ukaea/fair-mast/blob/6c9573d43440941ea2dad3ff80cc194d4814e7b4/docs/quickstart.ipynb) supplies shot 30421, the storage prefix, summary group and ip variable. These notebooks were read as source JSON, not installed or executed.

## Five-probe result

Every probe requested only a metadata key, sent Range bytes 0–8191 and Accept-Encoding identity, used an 8-second network timeout, and retained at most 8 KiB. The helper allowed one extra byte to detect an ignored range/cap overflow; no successful response reached that cap. The first sandboxed attempt failed DNS; subsequent authorized read-only requests used the same bounded helper with network access. No signal chunks, array samples, browser downloads or waits occurred. Five invocations were counted, including the transport failure; no requests followed the cap.

| Probe | New metadata path under 30421.zarr | Result |
|---|---|---|
|1|zarr.json at root|Sandbox DNS failure, no HTTP response; layout hypothesis unresolved.|
|2|.zmetadata at root|HTTP 404; consolidated v2 root object not found at this URI.|
|3|summary/zarr.json|HTTP 206, complete 756-byte group metadata.|
|4|summary/ip/zarr.json|HTTP 206, complete 970-byte array metadata.|
|5|summary/time/zarr.json|HTTP 206, complete 716-byte coordinate metadata.|

The successful Content-Range values were 0–755/756, 0–969/970 and 0–715/716. Content-Length and retained byte counts match those complete ranges. Thus the SHA-256 values below cover each complete metadata object, not merely a prefix. They do not cover decoded values, signal chunks, the complete shot store or the archive.

| Saved raw object | Complete-body SHA-256 |
|---|---|
|summary.zarr.json|2f9611de287a4c00e1ee996b3c8be7ca2ccdb9be9372540dd52546629cabeaca|
|ip.zarr.json|4c21e35cc31c5db41540a73e09ed892180011c8679dc4d340c5b9cd6385cda97|
|time.zarr.json|5d23dafba38014d3797fb02af4673502ae97604038ba29129b047ddb764c91fc|

Exact request/response headers, elapsed durations, raw metadata text and hash scope are in `fair-mast-minimum-access-round14-receipts.json`. Byte-identical raw JSON is saved under `fair-mast-round14-metadata/`, with an attribution/manifest sidecar. HTTP headers/TLS overhead and unread error bodies are not included in the 2442-byte successful-body total.

## The actual minimal record

The [group metadata](https://s3.echo.stfc.ac.uk/mast/level2/shots/30421.zarr/summary/zarr.json) states Zarr format 3/group, name summary, license Creative Commons 4.0 BY-SA and license URL. It reports ingested_at **2026-09-24T17:10:53Z** and ingestion-code URL `https://github.com/ukaea/fair-mast-ingestion/tree/ed6ea4e2a81f2317ae474f7c5421071994220948`. This is source-reported provenance; that repository/commit's contents were not fetched or verified here. It is separate from the API/docs commit and paper-named 1.0 release.

The [ip metadata](https://s3.echo.stfc.ac.uk/mast/level2/shots/30421.zarr/summary/ip/zarr.json) describes float64, shape [767], dimension_names [time], units A, UDA name AMC_PLASMA CURRENT and IMAS path summary.global_quantities.ip. Its description defines total toroidal plasma current and a sign convention. The [time metadata](https://s3.echo.stfc.ac.uk/mast/level2/shots/30421.zarr/summary/time/zarr.json) is float64 with the same shape/dimension and units s. Both describe little-endian bytes plus zstd and NaN fill; no codec was run. Raw storage units A should not be replaced by a plotting display's kA label without an explicit conversion.

**Known identity boundary:** 30421 is the documented URI/selected shot identity. The ip attributes name a shot_id coordinate, but its scalar value was not fetched. No experimental timestamp, time extent, sample spacing, monotonicity, waveform amplitude, quality flag or calibration was established. The group says time can represent slices or interval ends when time_width exists; no time_width or numeric coordinate was fetched, so that choice remains unknown.

Last-Modified headers are 25 September 2026 and ETags are retained as opaque validators. Response headers were recorded through an allowlist; object-version headers were not captured. Neither those headers nor ingested_at is the experiment's shot time. No S3 version ID was captured or verified; URLs may change. The locally computed full-metadata hashes preserve what was actually observed, without creating an immutable waveform-version claim.

## Rights, fallback and gate proposal

Actual group attributes and the [official UKAEA service page](https://www.ukaea.org/service/fair-mast/) align on archive/catalogue CC-BY-SA 4 except where noted, separate from MIT software. The sidecar credits UKAEA/FAIR-MAST, source URLs, terms and unchanged raw bytes. No extra exception was present in these selected metadata objects. This does not independently clear every other signal, downstream publication use or private calibration source.

The proposed update is **metadata-readable; array-values/runtime/oracle/reviewer unaccepted**. `fair-mast-minimum-access-round14-proposals.json` carries seven exact guarded field proposals for `launch-fixture-round13.fairmast`, including old values, presence, record/absolute pointers and original-file hash. Nothing is applied to frozen inputs and no launch gate is accepted. The source-test fallback remains separately described instead of being relabeled experimental truth.

A viable immediate fallback/learning slice is to parse these three tiny metadata files with an already approved JSON tool or paper trace, confirm schema/units/dimension agreement, preserve unknown clocks/calibration, and specify independent constant/ramp/sinusoid conversion cases. It needs no archive container/database stack and no fusion equipment. A later numerical adapter still needs a separately authorized bounded array/time slice, compatible Zarr/xarray environment and independently specified transform/reference. This pass deliberately stops before those steps. It establishes no plasma interpretation, archive-wide availability, performance gain, vacancy or paid demand.

Validation checked complete-range/body/hash agreement, JSON parsing/schema, matching shapes/dimensions, units and all proposal preconditions. No upstream code, source notebook, array decoder or benchmark executed. The five reviewed existing local input files remain byte-identical across report/proposal creation.
