# Source evaluation audit: delayed fraud labels and legal evidence spans

Bounded code-to-claim review, 20 October 2026. Earlier finance, security and public/legal notes were read first. This pass inspects public source text at the previously recorded immutable revisions. It does not clone repositories, install dependencies, retrieve datasets/models, run upstream code, probe services or give financial/legal advice. Only the small self-authored arithmetic fixtures described below were executed. Earlier notes and shared catalogs remain unchanged.

## Findings

The earlier claims largely survive, with narrower execution contracts. The Fraud Detection Handbook implements chronological windows, a fixed feedback-delay convention, train-only scaling and useful review-capacity metrics. Its card precision is **not transaction precision or causal fraud savings**: it is a daily, capacity-normalized, simulated card-discovery measure with explicit removal assumptions. A project must encode actual label-observation and action times instead of treating seven days as universal.

LegalBench-RAG measures overlap with annotated character spans. The core scorer can double-count overlapping returned spans and produce recall above one; its response model does not enforce their disjointness or bounds. The inspected baseline normally avoids overlap by constructing disjoint chunks, so this is an interface/scorer assumption requiring tests—not evidence that published baseline results are inflated. Default sampling also reduces the searchable corpus using selected gold documents. Exact span matching remains useful, but does not establish legal entailment, applicability, freshness, permissions or correct critical fields.

## Pins, files and reading boundary

| Artifact | Recorded inspection pin | Source/rights boundary |
|---|---|---|
| [Fraud Detection Handbook](https://github.com/Fraud-Detection-Handbook/fraud-detection-handbook/tree/81cf7d1714bb7b2f5b496407d9055d91dc68dc25) | `81cf7d1714bb7b2f5b496407d9055d91dc68dc25`, commit date 8 September 2022 | Previously inspected README distinguishes notebook code GPL-3.0 from prose/pictures CC-BY-SA-4.0. Selected data/runtime rights and compatibility remain separate. |
| [LegalBench-RAG](https://github.com/zeroentropy-ai/legalbenchrag/tree/431bc8f2488a81569ab7259fa633dcc50ab77f9a) | `431bc8f2488a81569ab7259fa633dcc50ab77f9a`, commit date 30 May 2025 | Previously inspected code LICENSE MIT. [README lines 38–48](https://github.com/zeroentropy-ai/legalbenchrag/blob/431bc8f2488a81569ab7259fa633dcc50ab77f9a/README.md#L38-L48) separately requires upstream dataset usage policies and says LLM-assisted regeneration is not byte-identical to the distributed benchmark. |

These are checked source snapshots, not established paper-matched releases or tested environments. Source text was obtained through read-only GitHub contents/tree APIs and decoded for inspection. A public immutable raw source has the form `https://raw.githubusercontent.com/<owner>/<repo>/<commit>/<path>`; the line-linked public blob URLs below identify the precise files actually read. No dataset download link or notebook fetch/clone command was executed.

Handbook files inspected: `Chapter_References/shared_functions.py`; relevant code cells and physical JSON lines of `Chapter_3_GettingStarted/BaselineFeatureTransformation.ipynb` and `Chapter_5_ModelValidationAndSelection/ValidationStrategies.ipynb`. LegalBench-RAG files: `benchmark.py`, `benchmark_types.py`, `run_benchmark.py`, `methods/baseline.py`, `methods/retrieval_strategies.py`, `generate/generate_contractnli.py`, `generate/utils.py`, and relevant README lines. Other dataset generators and the released corpus/results were not fully audited.

## 1. Fraud: what information exists at the decision time?

### F1 — The split is chronological, with a particular feedback policy

[`get_train_test_set`, shared_functions.py lines 133–188](https://github.com/Fraud-Detection-Handbook/fraud-detection-handbook/blob/81cf7d1714bb7b2f5b496407d9055d91dc68dc25/Chapter_References/shared_functions.py#L133-L188) selects training transactions by a half-open datetime interval. Test days follow training plus a configurable delay. It initializes a set of known fraudulent customers from training labels, then adds newly known customers each test day and removes their test transactions.

The exact day arithmetic matters. For training days 0–6, seven delay days and testing from day 14, the day-14 update considers day 6 again; day 15 adds day 7. The selected update day is `test_day − delay − 1`, with prior discoveries accumulated. This is compatible with a conservative daily decision convention where the preceding full day has matured after the delay. It is not automatically an off-by-one bug, nor a universal definition of when real disputes become known.

The helper has no per-event `label_observed_at`, subsequent label revision or investigation-result time. Its `TX_FRAUD` reads are legitimate only under the assumed availability/removal convention. If one transaction's label arrives later than the fixed delay, the simulated removal set can know something the operator does not. Conversely, real earlier feedback could be ignored. [`get_train_delay_test_set`, lines 195–255](https://github.com/Fraud-Detection-Handbook/fraud-detection-handbook/blob/81cf7d1714bb7b2f5b496407d9055d91dc68dc25/Chapter_References/shared_functions.py#L195-L255) exposes a separate delay dataframe, but does not create a variable observation-time model.

This is **not a blanket customer holdout**. A legitimate known customer's earlier available history can remain useful. The target is future transactions under the specified compromise-removal policy. Predicting new customers, new merchants or new episodes is a different distribution. The prior semantic review's population correction is confirmed by the source, rather than replaced by “always isolate every entity.”

The datetime/day-counter join also assumes a coherent calendar anchor. Training begins using `TX_DATETIME`, while test days are anchored to the minimum training `TX_TIME_DAYS`. The examples use midnight dates and regular daily data. A new sparse or partial-day input should explicitly test that anchor and empty-window behavior before assuming it preserves the desired gap.

### F2 — Whole-history feature construction is not automatically leakage

The spending feature code sorts each customer's transactions and computes backward rolling amount/count windows, explicitly including the current transaction. See notebook **code cell 18**, physical JSON [lines 645–672](https://github.com/Fraud-Detection-Handbook/fraud-detection-handbook/blob/81cf7d1714bb7b2f5b496407d9055d91dc68dc25/Chapter_3_GettingStarted/BaselineFeatureTransformation.ipynb#L645-L672). Including the current amount is not label leakage if that amount is available when scoring. A new deployment still needs a timestamp/arrival-order rule for simultaneous or late transactions.

Terminal-risk features subtract a recent delay window from a longer delay-plus-history window: notebook **code cell 26**, physical JSON [lines 1540–1568](https://github.com/Fraud-Detection-Handbook/fraud-detection-handbook/blob/81cf7d1714bb7b2f5b496407d9055d91dc68dc25/Chapter_3_GettingStarted/BaselineFeatureTransformation.ipynb#L1540-L1568). Under the intended time-based rolling semantics this selects historical labels outside the most recent delay interval. It implements a fixed-age availability proxy; it does not check when each label was actually observed or revised. Actual rolling-boundary behavior belongs in a later version-pinned test, not an unexamined pandas-default assumption.

Thus precomputing backward features over a full ordered file can be causal under the stated clock; calling every whole-file transform leakage would be incorrect. The test is whether each value depends only on data and labels available at the scoring time. A late revision or delayed arrival can break that property even if the transaction's original event date is old.

The inspected scaling paths are appropriately narrower than a global-fit caricature. [`scaleData`, lines 114–120](https://github.com/Fraud-Detection-Handbook/fraud-detection-handbook/blob/81cf7d1714bb7b2f5b496407d9055d91dc68dc25/Chapter_References/shared_functions.py#L114-L120) fits on training rows; [`prequential_grid_search`, lines 788–803](https://github.com/Fraud-Detection-Handbook/fraud-detection-handbook/blob/81cf7d1714bb7b2f5b496407d9055d91dc68dc25/Chapter_References/shared_functions.py#L788-L803) places scaling inside the cross-validation pipeline. Passing full `X,y` to that configured search is not evidence the scaler trains on every test row. No scaler leakage was established in these paths.

### F3 — Card precision has a capacity denominator and simulated feedback

[`card_precision_top_k_day`, lines 352–365](https://github.com/Fraud-Detection-Handbook/fraud-detection-handbook/blob/81cf7d1714bb7b2f5b496407d9055d91dc68dc25/Chapter_References/shared_functions.py#L352-L365) groups transactions by customer, uses maximum prediction and maximum fraud label, takes up to `k` customers and divides detected fraudulent customers by **k**, even when fewer than k customers are available. A high-scoring genuine transaction on a customer with another fraudulent transaction can count toward discovering a compromised customer. That is a card-discovery endpoint, not a claim that the ranked transaction itself was fraudulent.

[`card_precision_top_k`, lines 376–411](https://github.com/Fraud-Detection-Handbook/fraud-detection-handbook/blob/81cf7d1714bb7b2f5b496407d9055d91dc68dc25/Chapter_References/shared_functions.py#L376-L411) iterates days present in the dataframe, removes previously detected true-positive customers and averages the daily scores. It does not average over absent calendar days. Immediate correct identification/removal of selected compromised customers is a simulated investigation policy. It is not a measured investigation delay, realized intervention or avoided loss. Review of false positives and the consequences of blocking them are not monetized by this metric.

The transaction-level ROC AUC and average precision in [`performance_assessment`, lines 442–460](https://github.com/Fraud-Detection-Handbook/fraud-detection-handbook/blob/81cf7d1714bb7b2f5b496407d9055d91dc68dc25/Chapter_References/shared_functions.py#L442-L460) use the supplied transaction rows. They therefore have a different unit and, after the split/removal policy, a potentially different population from all originally arriving transactions. Neither their score nor CP@k is an estimate of causal financial savings.

### F4 — Prequential validation has index and selection contracts

[`prequentialSplit`, lines 265–292](https://github.com/Fraud-Detection-Handbook/fraud-detection-handbook/blob/81cf7d1714bb7b2f5b496407d9055d91dc68dc25/Chapter_References/shared_functions.py#L265-L292) moves the training start backward by assessment-block increments and returns dataframe indices as CV positions. [`card_precision_top_k_custom`, lines 421–432](https://github.com/Fraud-Detection-Handbook/fraud-detection-handbook/blob/81cf7d1714bb7b2f5b496407d9055d91dc68dc25/Chapter_References/shared_functions.py#L421-L432) also uses target indices with `transactions_df.iloc`. This requires consistent positional identity. The book's [`read_from_files`, lines 74–90](https://github.com/Fraud-Detection-Handbook/fraud-detection-handbook/blob/81cf7d1714bb7b2f5b496407d9055d91dc68dc25/Chapter_References/shared_functions.py#L74-L90) sorts and resets the index, which supports that convention. A filtered/reindexed external dataframe needs an explicit row-ID/position invariant; preserving arbitrary index labels can select wrong rows or fail.

The grid search reports mean and standard deviation of fold scores, not a calibrated population confidence interval. Later folds can legitimately use history that was future to earlier folds; independence of their errors does not follow. [`get_summary_performances`, lines 608–646](https://github.com/Fraud-Detection-Handbook/fraud-detection-handbook/blob/81cf7d1714bb7b2f5b496407d9055d91dc68dc25/Chapter_References/shared_functions.py#L608-L646) separately reports validation-selected parameters and an explicitly test-optimal comparison. The latter is an educational oracle comparison, not a deployable parameter-selection procedure. A new experiment must not select its claimed winner from that test-optimal row.

Reproducibility also needs more than pinning the notebook: the validation notebook's physical [line 59](https://github.com/Fraud-Detection-Handbook/fraud-detection-handbook/blob/81cf7d1714bb7b2f5b496407d9055d91dc68dc25/Chapter_5_ModelValidationAndSelection/ValidationStrategies.ipynb#L59) fetches `shared_functions.py` from `main`. The feature notebook contains similar convenience fetching and data-clone commands. None was executed here. A later approved reproduction should use an explicit local/source/data/dependency manifest instead of assuming a pinned notebook pins everything it fetches.

## 2. LegalBench-RAG: what does a span score certify?

### L1 — The oracle is source-coordinate overlap

[`QAResult.precision/recall`, run_benchmark.py lines 16–54](https://github.com/zeroentropy-ai/legalbenchrag/blob/431bc8f2488a81569ab7259fa633dcc50ab77f9a/legalbenchrag/run_benchmark.py#L16-L54) computes pairwise same-file interval intersections. Precision divides overlap mass by returned span lengths; recall divides overlap mass by gold span lengths. It uses half-open geometry, consistent with Python slicing. There is no answer-generation or legal-entailment judgment in these functions.

[`Snippet.answer`, benchmark_types.py lines 24–32](https://github.com/zeroentropy-ai/legalbenchrag/blob/431bc8f2488a81569ab7259fa633dcc50ab77f9a/legalbenchrag/benchmark_types.py#L24-L32) opens the corpus text and slices a Python string. Coordinates are decoded-string code-point positions, not necessarily UTF-8 bytes, tokenizer tokens or user-perceived graphemes. Corpus hashes are necessary but insufficient without the decoding, newline and normalization contract used to create offsets. OCR or reformatting must either preserve that coordinate space or carry a verified mapping.

`QAGroundTruth` validates disjointness within a file; the snippet type itself does not enforce nonnegative, ordered or in-bounds ranges or compare the range with current document length. The ground-truth validator uses `previous_end >= next_start`, so even touching half-open spans are rejected unless merged. These are source facts about the schema, not evidence that the released gold annotations contain invalid ranges.

The types have query, file path, span and tags, but no first-class document revision, effective/publication time, jurisdiction, caller permission or amendment-state contract. Those can be supplied by an application, but this scorer does not establish them. A correct passage in a wrong-version source can be perfectly overlapped and still be wrong evidence for the application's decision.

### L2 — Overlap/duplicate responses violate an implicit core assumption

The [`QueryResponse` validator, lines 79–85](https://github.com/zeroentropy-ai/legalbenchrag/blob/431bc8f2488a81569ab7259fa633dcc50ab77f9a/legalbenchrag/benchmark_types.py#L79-L85) has its snippet-disjointness call commented out. The core scorer sums each retrieved/gold intersection independently, rather than unioning covered characters. With gold `[0,10)` and two identical retrieved `[0,10)` spans, its equations yield precision 1 and recall 2. This follows statically from the code; upstream classes were not executed here.

This should not be described as observed inflation of the default results. The inspected [baseline chunk construction, lines 86–134](https://github.com/zeroentropy-ai/legalbenchrag/blob/431bc8f2488a81569ab7259fa633dcc50ab77f9a/legalbenchrag/methods/baseline.py#L86-L134) uses zero chunk overlap, asserts complete concatenation and assigns successive non-overlapping spans. The ordinary returned chunks therefore satisfy a stronger invariant than the general response API enforces. A custom retriever, duplicate rerank index or overlapping-window adapter must establish that invariant itself. No actual provider response, released result file or corpus was checked for such violations.

A project can either reject invalid/overlapping returns or define unique-coverage recall and a stated precision/context-cost treatment. It must not silently clip recall above one, because clipping hides the failed contract. If duplicate material consumes context, report that wasted volume separately even when coverage is computed on unions.

### L3 — Default sampling and weighting define a smaller retrieval problem

[`benchmark.py`, lines 13–27 and 35–82](https://github.com/zeroentropy-ai/legalbenchrag/blob/431bc8f2488a81569ab7259fa633dcc50ab77f9a/legalbenchrag/benchmark.py#L13-L82) assigns each of four component benchmarks weight 0.25, caps each at 194 queries and defaults `SORT_BY_DOCUMENT=True`. Tests are ordered using a deterministic pseudorandom value seeded by the first gold snippet's file path, grouping same-document queries. The searchable corpus then contains documents used by the selected tests, rather than the larger document set identified before truncation. The source explicitly comments on the reduced search-space limitation.

This is a cost-saving evaluation configuration, not a random sample establishing full-corpus performance. With document sorting disabled, the code still builds from documents referenced by the loaded benchmark tests; it does not infer every distractor in a deployment. The actual available corpus/query counts cannot be recovered without the selected data snapshot, which was not downloaded.

[`BenchmarkResult`, lines 63–101](https://github.com/zeroentropy-ai/legalbenchrag/blob/431bc8f2488a81569ab7259fa633dcc50ab77f9a/legalbenchrag/run_benchmark.py#L63-L101) forms normalized weighted averages of **per-query** scores. In the main driver, each retained query receives its component's weight divided by retained query count. It is not a global micro-average over all gold characters or an estimate of a real service's query mix. Per-component and per-document summaries should accompany a transplanted score; correlated queries from one contract are not independent evidence about many contracts.

### L4 — A retrieval fixture is not an untouched learning or temporal split

The inspected [ContractNLI generator, lines 51–58](https://github.com/zeroentropy-ai/legalbenchrag/blob/431bc8f2488a81569ab7259fa633dcc50ab77f9a/legalbenchrag/generate/generate_contractnli.py#L51-L58) combines its upstream training and test documents for the adapted retrieval dataset. [Lines 95–113](https://github.com/zeroentropy-ai/legalbenchrag/blob/431bc8f2488a81569ab7259fa633dcc50ab77f9a/legalbenchrag/generate/generate_contractnli.py#L95-L113) use annotated spans, merge close spans and skip empty-span cases. That is not automatically leakage for evaluating a fixed retriever; it does mean upstream train/test labels do not supply an untouched split for someone who then tunes on the adapted benchmark. Document/source-family holdouts and separate no-evidence cases must be specified for the new question.

There is also a narrow regeneration concern. The ContractNLI title call at [lines 128–135](https://github.com/zeroentropy-ai/legalbenchrag/blob/431bc8f2488a81569ab7259fa633dcc50ab77f9a/legalbenchrag/generate/generate_contractnli.py#L128-L135) passes a pathname as its `text` argument. The [title helper, utils.py lines 75–98](https://github.com/zeroentropy-ai/legalbenchrag/blob/431bc8f2488a81569ab7259fa633dcc50ab77f9a/legalbenchrag/generate/utils.py#L75-L98) inserts that argument directly into the model's content prompt; it does not load that path. Generated titles are subsequently embedded in questions and some titles cause filtering. This inspected path should be checked before trusting a regenerated fixture's intended query. It does **not** establish that the distributed benchmark was produced with this exact snapshot or contains wrong titles; neither was tested.

The deterministic interval scorer assumes its gold evidence is appropriate and sufficiently complete. Correctly slicing an annotation does not independently verify the annotation's legal meaning, exceptions or applicability. The new procurement exercise should retain separately authored field/state truth rather than use retrieval overlap as its only evidence oracle.

### L5 — Resource and failure denominators need explicit handling

The baseline field named `token_limit` truncates/subtracts Python character counts, not tokenizer counts: [`baseline.py`, lines 232–249](https://github.com/zeroentropy-ai/legalbenchrag/blob/431bc8f2488a81569ab7259fa633dcc50ab77f9a/legalbenchrag/methods/baseline.py#L232-L249). The inspected [strategy list, lines 23–34](https://github.com/zeroentropy-ai/legalbenchrag/blob/431bc8f2488a81569ab7259fa633dcc50ab77f9a/legalbenchrag/methods/retrieval_strategies.py#L23-L34) sets that field to `None`, so this is not evidence that the default displayed runs used a mislabeled active cap. If a project enables it, call it a character budget or implement an explicit tokenizer/mapping contract; do not report exact token cost from the name.

[`run_benchmark`, lines 117–138](https://github.com/zeroentropy-ai/legalbenchrag/blob/431bc8f2488a81569ab7259fa633dcc50ab77f9a/legalbenchrag/run_benchmark.py#L117-L138) ingests the supplied corpus, issues queries with `asyncio.gather` and returns scored results. There is no per-query exception-result contract in this function; an exception can abort the run rather than become a counted failed case. A later local harness needs an all-attempt ledger, explicit failure/timeout status and actual processing/review costs. An empty gold or empty returned total yields zero in the core score, so correct abstention on no-evidence cases needs its own endpoint.

## 3. Tiny fixtures actually executed

Only self-authored Python built-in set, string and arithmetic operations were run. No upstream function/class, pandas, sklearn, pydantic, embedding API, notebook or provider was executed. These checks demonstrate mathematical contract differences; they are **not package reproductions, empirical fraud tests or legal benchmark results**.

| Fixture | Observed local arithmetic result | Why it matters |
|---|---|---|
| One ten-character gold interval; same interval returned twice | Pairwise-mass equations: precision 1, recall 2. Set-union coverage: precision 1, recall 1. | Core overlap scoring needs a disjointness/unique-coverage contract. |
| One true-positive card, three available reviewed cards, capacity five | Capacity-normalized 0.2; among-reviewed precision 1/3. | Different denominators answer different questions. |
| Fraud event day 7; decision day 15; assumed delay seven; actual label observed day 18 | Fixed daily convention treats it as known; actual observation clock does not. | A fixed-delay exercise cannot silently stand in for variable real feedback. |
| Owned text `Aé🙂Z` | Four Python code points, eight UTF-8 bytes; `[1:3]` gives `é🙂`. | Offsets need a coordinate convention, not just the word “characters.” |
| Owned ten-character string with range `[-5,5)` | Geometric claimed length ten; Python slice is empty. | Negative/out-of-range coordinates should be rejected before scoring. |

## 4. Narrower acceptance rules for the proposed projects

These are proposed repairs to execution/interpretation, not edits to frozen catalogs. Existing hour caps and resource approvals remain conditional; no new implementation was started.

### Fraud project: `security-finance-interfaces-round7.project.fraud`

**First 30-day slice:** declare event time, data arrival, feature availability, label observation/revision, review decision and evaluation time. Select the intended known-customer/new-entity population and whether known/detected cards disappear. Establish one causal feature/label fixture before comparing models. Validate row-ID/position correspondence, midnight/day-counter assumptions and train-only transforms. Seed an old transaction with a newly arriving label and a future label concealed behind an old event date; neither may become a scoring-time feature early.

Report transaction AP/ROC, card-discovery CP@k, actual reviewed count, capacity, zero-traffic-day treatment and removed/censored populations separately. If discovery/blocking is simulated, name its delay and false-positive treatment. A fixed review-capacity comparison is useful; its numerator is not money saved. Use validation-selected parameters only for the claimed final test; a test-optimal educational row stays labeled an oracle comparison.

**90-day extension:** add one variable-label-delay or drift condition and a separate novel-entity shift condition only if they answer the chosen deployment question. Freeze a final period before selecting the winner, and report failed/indeterminate cases and grouped/time uncertainty. Actual bank labels, counterfactual blocked outcomes and cost weights remain unavailable unless separately authorized. Until then the acceptable result is time-aware predictive evaluation and software competence.

### Public-document project: `energy-public-round6.project.public-doc`

**First 30-day slice:** retain the fictional notice-family baseline. Freeze document revision, publication/effective/retrieval times, decoded text representation and offset convention. Reject missing files, negative/reversed/out-of-bounds spans and malformed source/version identity before metrics. Deliberately test duplicate/overlapping returned ranges. Choose a stated unique-coverage metric and track redundant context/actual tokens separately. Critical amounts, currency/VAT basis, dates, status and amendment precedence have exact field/state gates independent of aggregate character overlap.

Use a full declared candidate corpus with distractors, not a corpus selected from the test's gold documents. If a reduced corpus is needed for cost, record the exact selection and limit the claim to it. Keep document/notice families together when holding out, and report per-family/component results rather than treating every related query as independent. Include explicit no-evidence and inaccessible/stale-source cases with their own abstention/authorization expectations.

**90-day extension:** test one later amendment/version or new source family with actual state-transition truth, correction/deletion/reindex behavior and the synthetic permission matrix. Retain all query failures and total review/correction time. Span recovery is one layer; it does not establish claim entailment, rule application or real legal-case suitability. Without a domain reviewer, retain a single-author synthetic extraction/state exercise. A perfect retrieval score cannot override a critical wrong field or unauthorized disclosure.

## Remaining uncertainty and next question

Static inspection establishes the named code contracts and potential edge cases; it does not show their frequency in real transactions or released benchmark outputs. Installed library versions, dataframe behavior on actual data, all four legal-data generators, exact distributed corpus bytes/offsets, actual reranker responses and paper-to-code matching remain unchecked. No claim is made that the supplied releases exhibit the constructed counterexamples.

**Next unresolved question:** do the permitted, versioned LegalBench-RAG corpus/result manifests satisfy span bounds/disjointness and record the full sampling/corpus configuration used for the compared results? Resolving that would distinguish a latent extension-interface defect from an issue that actually changes a published evaluation. No gated/released data were downloaded to answer it in this pass.
