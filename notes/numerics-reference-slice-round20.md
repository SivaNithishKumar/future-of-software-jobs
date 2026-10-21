# Numerical reference slice: bounded repair, round 20

20 October 2026. The separately versioned demonstration closes the two confirmed reuse gaps from the independent round16 review. It rejects changed oracle bytes rather than silently treating their parameters as supported, and it rejects invalid or incomplete time grids before numerical iteration. Forty-one own regression controls pass. All numerical values and mechanism results in the published fixed case replay exactly.

The original round15 demo, oracle, results, notes and content-addressed review snapshots remain unchanged. No shared research catalogue or preparation graph was edited. This is an author repair and author regression run, pending independent recheck; it does not adopt the original reviewer’s independence for the new implementation.

## Exact baseline-to-repaired behavior

On an isolated copy of the old source, a genuinely changed rate `k=0.25 s^-1` with consistent analytic formula labels still produced the original `exp(-2)` final reference and `2 ln(2)` event reference. The changed mathematical case would instead have final `exp(-1)=0.36787944117144233 mol` and event `4 ln(2)=2.772588722239781 s`. This reproduction is retained in `numerics-reference-slice-round20-baseline-reproduction.json`.

The repair deliberately chooses the reviewer’s **fixed-case fail-closed option**. `load_fixed_spec` accepts only the exact original oracle SHA256 `3c3f6a591b93ba9de728c571278bb95d369dcf95cc2162b3225c3d51ba7a68b9`. A different rate, different formula, different grid list, or even changed formatting requires a separately reviewed version; the script raises before it computes or creates a results file. It does not parse formula strings, pretend to bind arbitrary models, or claim the changed case has been numerically validated. The changed-rate fixture is an exposed same-author rejection test, authored after seeing the original answers. Its inherited original oracle labels do not independently establish its writing chronology or an unseen assessment.

The original negative step `euler_transfer(-0.2)` returned unchanged initial states labelled at 4 seconds; the original event scan accepted `h=0.3` and stopped at 0.9 seconds. The new `grid_count` rejects nonfinite/nonpositive or nonnumeric steps and intervals, requires a positive integer step count covering the declared interval within an absolute `1e-12 s` tolerance, and caps the teaching workload at 100,000 steps. Both helpers use this check. No endpoint segment is silently discarded. The five transfer grids and four event grids remain accepted.

The numerical recurrences, fixed reference values, strict endpoint-sign event policy, unit example and deliberately planted sequential-update error are unchanged. Direct helper rate/amount-scale arguments remain teaching controls, not a generalized parameter-validation or scientific-model interface. Grid validity alone does not guarantee stability, positivity or reference correctness for arbitrary helper arguments.

The new CLI requires an explicit output path and opens it exclusively. A repeated run cannot overwrite an existing results file, including the frozen baseline. This also addresses the review’s replay clarification in the new version; the old direct command still has its original behavior and must not be used in place on frozen evidence.

## What ran

`numerics-reference-slice-round20-tests.py` ran the new demo through its real CLI under the existing CPython runtime, then imported only this inspected own stdlib code for helper controls. Seven numerical/result sections equal the original results JSON exactly: analytic reference, transfer trajectories/errors/orders, sequential-error example, unit example, exact-trajectory event scan, fixed checks and proof limits. The code/results identifiers and new binding/domain provenance intentionally differ.

The 41 passing checks cover those seven equality comparisons, actual CLI code/oracle receipts, changed-rate CLI rejection with no output, formatting-only oracle rejection, 20 invalid-step/helper combinations, seven invalid-interval cases, all nine valid grids, refused results overwrite, stdlib-only imports, and preservation of all twenty original/snapshot files. Negative, zero, NaN, positive/negative infinity, boolean, string, noncovering, excessive-work and oversized steps are included. These finite controls exercise the two repaired mechanisms; they are not a general solver test suite.

A later replay must select a **new nonexistent** results path, for example an owned temporary filename:

```sh
python3 -B numerics-reference-slice-round20-demo.py --oracle numerics-reference-slice-round15-oracle.json --output /private/tmp/numerics-round20-replay-NEW.json
```

The test script similarly requires its two owned result paths to be absent. To rerun the full suite while preserving this evidence, copy the inspected task-owned script/demo/oracle/reference snapshots into an isolated review workspace or explicitly revise the reviewer-owned destination paths. Do not delete frozen results to make the test rerun.

## Source and proof boundary

The repair uses only saved local source/context and self-authored Python standard library code. It does not refresh the inherited SciPy/PyBaMM source observations, import or execute those packages, exercise native solver internal steps, or validate a scientific dataset. The original source/version/access limits remain in force. A fixed oracle hash binds a known teaching case to known answers; it is not independent scientific truth or parameter calibration.

Exact endpoint-zero behavior, duplicate/direction policy, tangencies, complete event detection, general equations, stiffness/DAEs, numerical-library equivalence, physical calibration, experimental/battery truth, device safety and scientific competence remain unestablished. The deliberately coarse exact-state event scan still misses two interior roots; that demonstrates the toy policy limitation and is not evidence of a native-solver defect. The original oracle-before-code chronology remains author-reported rather than independently timestamped.

Existing joins remain references only: `preparation-round8.module.numerics`, `preparation-round8.path.scientific-software`, `learning-round8.resource.scipy-optimize`, and `science-enrichment-round5.project.pybamm`. No preparation gate, learner timing, project execution, employment or commercial claim is upgraded by this repair. The mature release-matched solver, domain reviewer and physical reference gates still apply to any later scientific continuation.
