# METR capability export: public source-route check, round 16

20 October 2026. **A source-family lead was found, but neither exact website export was retrieved or linked conclusively to repository bytes.** The raw-export gap remains open. Five new public GitHub retrievals were used and the route stopped at its cap. No browser, downloadMedia, YAML web-reader retry, installation, upstream execution, private repository search or login/account inspection occurred.

This deliberately revisits the same publisher through a different transport and artifact-identity question. The frozen round 7 checkpoint had identified two official website links; the round 12 reader rejected their application/x-yaml content type. Those failures were not repeated or reinterpreted as evidence of missing/invalid publisher data.

## Exact request ledger

| Request | Public scope | Result and limit |
|---|---|---|
| 1 | METR repository metadata, query `website is:public`, limit 5 | Empty result. A keyword/index result does not prove that no public website source exists. |
| 2 | Known public `METR/eval-analysis-public` file search for both exact export filenames, limit 8 | Empty result. This combined/default-branch query does not prove either file or generator is absent. |
| 3 | METR repository metadata, query `is:public`, limit 100 | Returned 67 repositories, all explicitly public. No obvious website-source name appeared in this returned page. No private repository was searched or opened. This is not an exhaustive provenance proof. |
| 4 | `METR/eval-analysis-public`, main, README.md | Returned the analysis/report layout and descriptions of run data and outputs. |
| 5 | Same public repository, main, `reports/time-horizon-1-1/dvc.yaml`, lines 1–260 | Returned a bounded pipeline prefix containing a benchmark-result generation stage. |

The [README](https://github.com/METR/eval-analysis-public/blob/main/README.md) was read in earlier research; this new connector receipt was obtained specifically to trace source-to-website identity. It describes both TH1.0 and TH1.1 report directories, source JSONL and logistic/bootstrap outputs. Its run-field descriptions remain a schema description for that repository artifact, **not a verified schema for the two website YAML files**. No code or DVC pipeline was run.

## Useful source lead, with the missing bridge explicit

The returned [TH1.1 DVC prefix](https://github.com/METR/eval-analysis-public/blob/main/reports/time-horizon-1-1/dvc.yaml) declares a `generate_benchmark_results` stage. It invokes `horizon.generate_benchmark_results` and writes:

`reports/time-horizon-1-1/metrics/benchmark_results.yaml`

Declared inputs include the headline logistic-fit CSV, raw runs JSONL, headline bootstrap CSV and model release dates. The stage passes unresolved benchmark-name, long-task-version and SWAA-version parameters. It also declares stitching selected GPT-2/davinci_002/gpt_3_5_turbo_instruct results from the TH1.0 benchmark file. This is **configuration/source evidence**, not a reconstructed run, resolved parameter value, model result or assurance that all exported entries share one suite configuration.

The generated candidate's name differs from the [official benchmark export](https://metr.org/assets/benchmark_results_1_1.yaml). The publication/rename/copy/deployment step was not observed. No repository commit, website deployment commit or byte comparison linked them. The actual candidate metric file was not fetched. Consequently, a plausible generating relationship is not canonical equivalence.

No exact source artifact or publisher mapping for [task_results_1_1.yaml](https://metr.org/assets/task_results_1_1.yaml) was established in this pass. Only the first 260 DVC lines were read; absence from that prefix is not absence from the complete repository or pipeline.

## Size, hash and schema scopes

| Inspected source text | Returned size | Exact identity boundary |
|---|---:|---|
| README.md | 4,254 UTF-8 bytes; 140 lines | Recomputed Git blob SHA-1 matches connector-reported `62265ad316203e3cbf8ab6cc2510dfaba45ecb6f`. |
| DVC lines 1–260 | 11,323 UTF-8 bytes | Connector reports whole-file blob `ac0a054e302015f272c0d4e9b4982bc68c6299d3`; returned-prefix Git hash does not match, as expected for a slice. |

The README returned-text SHA-256 is `4f5d2eb62e339e2804448364c8ef2364f8e5fc229aa78c073a36e0d572621a99`; the DVC prefix SHA-256 is `d4ef137f2d58f25a87e4d6236846d6bec1c20104c7764268565d96cb948a5280`. These hash UTF-8 re-encodings of connector-returned source text. They are not HTTP-transfer checksums, full-repository commits or website-export hashes. Both reads requested moving main; file content identities are retained separately.

The observed YAML source has params/vars/stages and unresolved substitutions/anchors. It was inspected as text, not parsed with an installed YAML package. It is a pipeline definition, not a result schema. The receipts retain a modest generator-stage excerpt and exact line scope. No source code is installed or executed. The README points to LICENSE; reuse/redistribution terms were not separately audited inside this five-request cap.

For **both canonical exports**, raw-byte size, checksum, schema, row/task/model counts, null/exclusion rules, complete configuration and fit uncertainty remain **null/unverified**. No task/run records were retrieved. No p50/p80 refit, p95/p99 horizon, model ranking, acceptance fraction, cost distribution or new jobs inference was calculated.

## Stop disposition and useful remaining work

The five-request source route is complete at a method-specific negative boundary: public source inspection succeeded, but website export identity and raw data did not. The prior browser/download and MIME-reader failures remain distinct. None establishes that the origin denies access or that its data are invalid.

The companion `capability-export-source-route-round16-receipts.json` records requests, explicit public scope, source blob/text-hash scopes, observed generator configuration and canonical-target nulls. Earlier research files remain unchanged.

A distinct useful question is whether a declared result mixes suite versions, weighting schemes, human-time measurement types or exclusion rules before it can support a capability comparison. That can be audited as a methods contract; it should not be replaced with a guessed export, a new percentile from a chart, or another unbounded download attempt.

