# Numerical ODE and event reference slice, round 15

20 October 2026. **The missing ODE/event preparation slice is now concrete and runnable with the existing Python standard library.** The demonstration uses independently derived closed-form references, checks finite-grid error and units, and exposes three plausible failures. SciPy, PyBaMM and upstream notebooks were read but never imported or executed. This is a finite synthetic numerical exercise, not a production solver, physical calibration or assessment of the user's scientific competence.

## Exact place in the preparation map

The staged `preparation-round8.module.numerics` correctly retains task-specific mathematics and measurement semantics. Its `selectedMethodResourceGate` says the existing `learning-round8.resource.scipy-optimize` does not cover ODE/DAE/event correctness. This slice supplies the missing ODE/event reading and reference exercise for `preparation-round8.path.scientific-software` and the optional methods branch of `preparation-round8.path.research-credential`. It can precede `science-enrichment-round5.project.pybamm`; it does not complete that project.

The JSON companion proposes two new resource IDs, without changing shared catalogues:

- `numerics-round15.resource.scipy-ivp-events`
- `numerics-round15.resource.pybamm-ode-events`

Their exact existing technical anchors are `darkside2031.foundations.math.dynamics` and `darkside2031.bio-science.materials.infrastructure`. Basic derivatives, exponentials/logarithms, units and initial-value algebra are relevant here. Probability calibration and a complete ML curriculum are not prerequisites for this deterministic exercise.

## Official resource slices and compatibility

The current [SciPy solve_ivp reference](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.solve_ivp.html) identifies version 1.18.0. Read the initial-value/shape contract; method selection; `t_eval`, `dense_output` and `max_step`; event function/direction/termination; tolerances; and returned state/status/event fields. It distinguishes non-stiff from stiff methods. Output times do not bound internal steps, and sign-change detection may miss multiple crossings within a step. `atol + rtol*abs(y)` controls local error estimates; it is not a global physical-accuracy certificate. The [linked source tag](https://github.com/scipy/scipy/blob/v1.18.0/scipy/integrate/_ivp/ivp.py) resolves to commit `54ef5423f2e4376230ec3bfda6912a07a50958e3`; its BSD-3-Clause license text was read. No upstream solver code was copied.

The [PyBaMM ODE/event notebook](https://docs.pybamm.org/en/latest/source/examples/notebooks/solvers/ode-solver.html) provides an analytical oscillator comparison and a termination-event example. Its returned version is **26.10.1.1.dev8+g70a562632**, with an explicit warning that development notebooks may not match the stable release. The initial stable URL returned 404. The current example instantiates IDAKLUSolver, despite introductory text mentioning a SciPy solver. Therefore choose release-matched docs/tests before any execution; do not copy the notebook's install cell or assume a supported local environment. A versioned deprecation-source search result was only indexed, and its direct reader failed; it is retained as an access caveat rather than a verified installed API.

## Independent reference before numerical implementation

The oracle JSON was written before the demonstration code. “Independent” here means a mathematical solution derived from the equations rather than the numerical recurrence. The same author specified both, so no independent human review or learner-unseen test is claimed.

For two amounts A and B:

`dA/dt = -k*A; dB/dt = +k*A`

Use A(0)=1 mol, B(0)=0 mol, k=0.5 s⁻¹ and final time 4 s. Integration gives A(t)=exp(-t/2) mol and B(t)=1-exp(-t/2) mol; hence A+B=1 mol. The first downward crossing of A=0.5 mol is at **2 ln(2)=1.3862943611 s**. A(4)=exp(-2)=**0.1353352832 mol**. The derivative units are mol/s and k*t is dimensionless.

The teaching implementation applies fixed-step forward Euler using the same old-state flux for both amounts. It records the first event using bracket interpolation but continues to the common 4 s horizon. This avoids comparing final states taken at different physical times.

| Step h, s | Absolute A(4) error, mol | First-event time error, s |
|---:|---:|---:|
| 0.4 | 0.02796110 | 0.13941936 |
| 0.2 | 0.01375863 | 0.06797078 |
| 0.1 | 0.00682313 | 0.03431310 |
| 0.05 | 0.00339748 | 0.01725286 |
| 0.025 | 0.00169522 | 0.00866777 |

The measured state-error order approaches 1 on these grids. Maximum conservation error is below 9×10⁻¹⁶ mol and the tested states are nonnegative. These observations fit the deliberately simple method and problem; they are not a convergence theorem for arbitrary equations.

## Failure cases that a plot can conceal

**Wrong update order:** advancing B using the already-updated A yields smooth, nonnegative amounts but loses **0.0878423345 mol** by 4 s at h=0.2 s. The declared conservation check rejects it. A solver's success flag or plausible plot would not supply that invariant.

**Missed events with exact states:** to isolate event policy from integration error, evaluate the exact trajectory

`q(t)=0.5 mol + (1 mol/s²)*(t-0.5 s)²; r(t)=1 mol-q(t).`

The threshold q=0.54 mol has roots **0.3 s and 0.7 s**. On the single step 0→1 s, the event function is positive at both endpoints, so a sign-change-only scan finds zero events even though the endpoint states and conservation are exact. Smaller endpoint grids detect both: h=0.25 gives times 0.34/0.66 s; h=0.125 gives 0.31/0.69 s; h=0.0625 gives approximately 0.301429/0.698571 s. This does not show a SciPy failure—it demonstrates why the documented event-resolution limitation matters. Tangencies, discontinuities, stiffness and general event completeness remain outside the test.

**Wrong rate units:** interpreting numeric 0.5 as per-minute instead of the declared per-second rate preserves conservation while producing A(4)≈0.967189 mol, an error of 0.831854 mol against the declared model. An invariant alone cannot detect all model/units errors. Separately, a mol→mmol→mol representation check agrees within 4.2×10⁻¹⁷ mol. Absolute tolerances must scale with state units; relative tolerance is dimensionless.

## Mature baseline and bounded continuation

The native comparator is a release-pinned mature solver, not an expansion of this teaching Euler loop. Once an approved compatible runtime exists, specify two separate SciPy arms: a common-horizon trajectory run to 4 s, and a terminal downward-event run checked against 2 ln(2) and A=0.5. For the quadratic event case, specify `max_step` deliberately rather than assuming dense output or `t_eval` guarantees detection. Record method, component-wise tolerances, actual evaluation/step information, status and event outputs. None of these native runs occurred here.

The targeted resource slice is **6–10 focused hours assumed**: 1.5–2.5 on the exact contract/units, 1.5–2.5 deriving references, 2–3 inspecting/running the own demonstration, and 1–2 explaining failures and a fresh independently specified variant. This is a menu slice, not a completed course or measured learner time.

A **30-day continuation** can use 12–20 assumed focused hours: the 6–10-hour slice plus 6–10 for one version/runtime/native-baseline contract and a fresh variant. Within that second block, stop setup after a proposed 4–6-hour subcap if no approved runtime or valid oracle is available; preserve the mathematical/stdlib result.

A conditional **90-day continuation** inherits the existing PyBaMM project's **40–80 additional post-launch hours**: 8–16 on release-matched docs/tests and one question, 12–24 reproducing a genuine failure or unmet reference case, 12–24 on one justified adapter/event/regression change, and 8–16 on another condition and reproducible report. These phases total 52–100 hours only if both are deliberately selected. Do not stack all DAG courses or alternative projects. Calendar availability, starting depth, suitable releases and domain review remain unknown.

Stop the custom improvement when the mature framework already satisfies the contract. Stop a scientific claim without an appropriate equation/reference, data or qualified reviewer. ODE success does not establish DAE consistency, stiff battery-model coverage, parameter identifiability, calibrated chemistry or device safety. A useful software result can remain when a new-science or venture claim is unsupported.

## What was actually run

The own demonstration ran once under existing **CPython 3.11.15**, importing only pathlib, hashlib, json, math, platform and sys. It checked five transfer grids, four exact-trajectory event grids, the planted mass-loss update, and unit cases. Results retain code/oracle hashes, units, all rows and negative controls. No package/runtime catalogue, private work, battery data, hardware, upstream code or learner was tested. Re-run only the own file with:

`python3 "numerics-reference-slice-round15-demo.py"`

The code and results are local teaching artifacts. Any fresh learning assessment needs unseen questions and an audited scorer; any actual PyBaMM contribution needs its separate release/runtime/maintainer gates. No shared preparation, taxonomy or scientific project record was changed.

