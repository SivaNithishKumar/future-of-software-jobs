# SWE-Lancer payout-unit audit, round 34

This pass resolves the task-generation and scoring units but leaves the final unique-issue/payment denominator open. It finds no duplicate-cash event or paper error. The safe description is a payout-weighted benchmark aggregate, with the underlying historical-payment claim attributed to the paper.

## Question and falsifiers, specified before retrieval

The saved prespecification distinguishes disjoint historical issues/payments, shared issues with reused task weights, and a shared-issue population whose headline might still count unique payments. Stable issue overlap would refute disjoint issues, but not independently paid events: one issue can have multiple payments. Conversely, a row-price sum cannot show whether a bounty appears once or in both task types. An actual verdict requires the task→issue→price→payment crosswalk and the aggregate's inclusion/de-duplication rule.

I read the prior reuse26 and root39 notes first. I then inspected the exact versioned paper and **three** small public upstream metadata/source-text endpoints. No task row, task attachment, dataset body, model, container, checkout, package or upstream runtime was fetched or executed. No shared root39 file was changed.

## What the paper establishes, and the contrary arithmetic

[SWE-Lancer v4, dated 29 May 2025](https://arxiv.org/html/2502.12115v4), §2.2, describes generating an implementation task from each validated issue and a management task when at least two proposals exist. That supports shared source-issue origin during generation, without exposing the final issue/price/payment join. Section 2 and Table 1 report these marginals:

| Reported population | Implementation tasks / weight | Management tasks / weight |
| --- | ---: | ---: |
| Full | 764 / $414,775 | 724 / $585,225 |
| Diamond | 237 / $236,300 | 265 / $264,500 |

The full category weights sum to $1 million. If **every** management row were a same-price subset of the reported implementation rows, its nonnegative weight sum could not exceed the implementation sum. It does. Diamond also violates the corresponding count condition. This disproves that simplistic complete-subset reading, not the paper. It leaves final filtering, population differences and price associations to reconcile with actual bindings.

The paper explicitly describes historically paid amounts rather than estimated value. Preserve that positive producer claim. A.12 adds composition statistics, not a unique-issue/payment crosswalk. This pass neither transaction-verifies that claim nor downgrades it to advertised prices merely because a current loader accepts `price`.

## Three upstream endpoints and their limits

1. The current [suite directory metadata](https://api.github.com/repos/openai/frontier-evals/contents/project/swelancer) exposes 17 entries. The 8,403,631-byte task CSV was listed only; its body was deliberately not fetched.
2. The immutable [nested source tree](https://api.github.com/repos/openai/frontier-evals/git/trees/6b48833d0c9ad046532c51559e8805cabf2d556e) identifies seven entries and the evaluator blob.
3. The immutable [evaluator source blob](https://api.github.com/repos/openai/frontier-evals/git/blobs/8dd5d6ec3ee272a99fd4b5e2304ef3f88b1a5ece) supplies 26,658 bytes for `project/swelancer/swelancer/eval.py`. Independent UTF-8 Git-blob hashing reproduces SHA1 `8dd5d6ec3ee272a99fd4b5e2304ef3f88b1a5ece`.

No repository commit or timestamp was fetched. The tree/blob identities pin content, but do not make this a paper-era harness. The earlier archive→preparedness→frontier-evals observations remain separately dated prior evidence. A listed nested licence filename is not an inspected grant for code, data, attachments, dependencies or runtime.

The connector returned the blob already decoded as source. An initial local JSON-decoding assumption failed; I inspected the stored successful response without retrying or using a fourth endpoint. Retained receipts identify decoded connector text, not raw HTTP bytes. The evaluator's full blob hash, unlike the metadata-response hashes, is independently reproduced.

## Current source behavior

The exact source receipt supports these bounded observations:

| Lines | Observed relation |
| --- | --- |
| 89–101 | Task carries `issue_id`, `price` and `variant` |
| 478–485 | Loader reads CSV rows, then filters split and variant |
| 499–545 | Attempts enumerate rows; row `question_id`, `price` and `variant` become task fields; `issue_id` aliases `question_id` |
| 245–256; 365–375 | Both graders assign earned weight as price times correctness, with price as available weight |
| 641–665 | Summary sums per-result earned values; failed/system-error results can contribute zero |

These inspected loader/grader/summary paths contain no issue or payment de-duplication. That is a statement about these paths, not every file or dataset column. `question_id` was not checked against a canonical GitHub issue, source bounty or payment event. The unseen CSV could resolve or alter the interpretation.

The current file also rejects `task_type='all'` and requires a specific variant (432–453). This is a real configuration safeguard, not cross-variant payment accounting. Its per-attempt loop also means task rows and result attempts are separate units. No attempt, retry-cost, pass@k or runtime behavior was evaluated, and current aggregation cannot be silently back-projected onto the historical experiments.

## Owned arithmetic, not SWE-Lancer observations

All three deliberately hypothetical fixtures have two $100-weight benchmark tasks and a $200 score if both succeed:

| Owned fixture | Unique issues | Hypothetical payment events | Hypothetical event sum |
| --- | ---: | ---: | ---: |
| Same issue, same bounty reused as two task weights | 1 | 1 | $100 |
| Distinct issues, distinct bounties | 2 | 2 | $200 |
| Same issue, two distinct paid events | 1 | 2 | $200 |

Their identical task/score totals cannot identify the underlying join. Shared issue identity alone also cannot identify one payment event. These fixtures do **not** show that SWE-Lancer reused a particular bounty or that anyone was paid twice. No model or payment event was performed by the arithmetic.

## Disposition and decisive missing evidence

Keep five units distinct: benchmark task/variant rows; payout-weighted scores; unique historical issues; unique payout transactions/work events; actual money transferred to an autonomous agent. Only the reported task marginals and inspected current score mapping are established here. The historical paid-price assertion remains paper-reported; the actual overlap and unique-payment total remain unverified.

A decisive follow-up artifact would be a version-matched, lawfully inspectable **metadata-only** crosswalk: task ID, variant, split, stable source issue key, price/currency/source, unique payment-event key and aggregate inclusion rule. Reconcile same-issue pairs, shared versus distinct events, any different prices, and the exact experiment population. No issue descriptions, attachments, full container or model run is necessary merely to ask that accounting question. This pass stops at its three-endpoint budget without acquiring that artifact.

Root39 can say that v4 reports 1,488 benchmark tasks with $1 million in task-associated historical-payout weights, while this bounded audit has not verified the unique issue/payment-event denominator. Reported model earnings are evaluation mappings, not observed cash transfers. No conclusion follows here about duplicate actual payments, 1,488 independent commissions, an available paid route, current jobs or future employment demand. No new career node, project budget, source acceptance or UI acceptance is proposed.

The structured report records the prespecified hypothesis outcomes, exact source/line pointers, unresolved relations and suggested wording. The separate check script verifies source bytes and the owned arithmetic only; its result is explicitly **not benchmark execution**. All original root39 declared output pins still match.
