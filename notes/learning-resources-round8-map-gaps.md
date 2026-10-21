# Official learning resources: bounded preparation map

Checked 20 October 2026, Asia/Kolkata. Companion: `learning-resources-round8.json`. This is a resource catalog with **18 official resources**, not a popularity ranking, a personal readiness assessment or a second curriculum. `bio_science` owns the prerequisite/pathway DAG; stable IDs use `learning-round8.resource.<slug>`.

The selection starts with existing research notes, then verifies primary course/book/documentation pages for useful sections, access, prerequisites and terms. No course, package, data bundle, lab, enrollment, purchase, cloud GPU or physical system was executed or acquired. Every suggested diagnostic remains proposed.

## Shared resources

Each range is an assumed **focused slice**, not time to finish the resource. Use a fresh diagnostic to skip material already demonstrated or expose a prerequisite gap.

| Stable slug | Exact useful material | Assumed slice | Concrete check |
|---|---|---:|---|
| `missing-semester` | [2020 debugging/profiling](https://missing.csail.mit.edu/2020/debugging-profiling/) and [Git](https://missing.csail.mit.edu/2020/version-control/) exercises | 4–6h | Explain and repair a new parser/service failure through the same real path. |
| `ostep` | [OSTEP](https://pages.cs.wisc.edu/~remzi/OSTEP/) Ch26/28/30/32 concurrency; Ch39/42 persistence, choosing one mechanism | 4–8h | Predict a lost update or crash/recovery interleaving against an independently written invariant. |
| `postgres` | PostgreSQL18 [13.2 isolation](https://www.postgresql.org/docs/18/transaction-iso.html), [14.1 EXPLAIN](https://www.postgresql.org/docs/18/using-explain.html) | 6–10h | Correct historical as-of query plus a two-session snapshot explanation. Match eventual runtime version. |
| `mit-18-06` | [18.06SC](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/pages/syllabus/) linear systems, projections/least squares, then selected SVD | 6–12h | Hand-check a new small calibration problem, rank and residual. Full course is roughly150h in the official syllabus. |
| `mit-18-05` | [18.05 calendar](https://ocw.mit.edu/courses/18-05-introduction-to-probability-and-statistics-spring-2022/pages/calendar/): Class3; Class22/23, Studio9; Class24, Studio10 | 6–10h | Known-process interval simulation and a dependence-aware resampling comparison. |
| `islp` | [Author book/resources](https://www.statlearning.com/resources-python): basic regression, Chapter5 resampling lab and optional regularization | 6–12h | Mean/persistence versus one simple model on a reserved new group/time period. |
| `sklearn-evaluation` | [Grouped/time splits](https://scikit-learn.org/stable/modules/cross_validation.html) and [probability calibration](https://scikit-learn.org/stable/modules/calibration.html) | 4–8h | Detect leaked group IDs and examine probability quality. Lower Brier loss alone does not establish better calibration. |
| `boyd-convex` | [Boyd/Vandenberghe](https://web.stanford.edu/~boyd/cvxbook/): Ch2–5, selected exercises; AppendixC as needed | 6–12h | Formulate and hand-check a tiny constrained allocation/storage problem before invoking a solver. |
| `scipy-optimize` | [Official tutorial](https://docs.scipy.org/doc/scipy/tutorial/optimize.html): objective/Jacobian examples, constraints, least squares and LP | 4–8h | Catch a deliberately wrong derivative; check known optimum/residuals instead of trusting a success flag. |

These are complementary references, not nine mandatory preliminaries. For example, PostgreSQL and Elexon can serve a data/replay path without first taking the full optimization or robotics sequence.

## Conditional depth resources

| Stable slug | Useful section/exercise | Assumed slice | Gate or boundary |
|---|---|---:|---|
| `mit-65840` | [MIT6.5840](https://pdos.csail.mit.edu/6.5840/): one fault-tolerance reading and [MapReduce Lab1](https://pdos.csail.mit.edu/6.5840/labs/lab-mr.html) handout | 6–12h | Graduate systems prerequisites and substantial programming. Read/reason first; official lab needs approved toolchain. Course prohibits public lab-solution publication. |
| `cs336` | [StanfordCS336](https://cs336.stanford.edu/): tokenization, resource accounting and evaluation; one reduced CPU diagnostic | 6–12h | Strong Python/PyTorch, systems, math and ML expected. Full assignments involve GPUs; no paid compute assumed. Course's assignment AI/implementation policies are recorded. |
| `modern-robotics` | [Author preprint/resource page](https://hades.mech.northwestern.edu/index.php/Modern_Robotics): Ch3 transforms, Ch4 forward kinematics, then Ch6; public practice exercises | 6–12h | Physics, linear algebra, calculus/basic ODEs and programming. Paper/Python transforms need no robot; simulation/physical safety remain separate. |
| `ros2-jazzy` | Official [Jazzy tutorial source](https://raw.githubusercontent.com/ros2/ros2_documentation/jazzy/source/Tutorials.rst): beginner nodes/topics/actions/replay and Python client interfaces | 4–8h | Rendered docs blocked by Anubis; source indexes/licence readable. Read/stdlib mock is accessible; actual ROS setup and compatibility remain untested. |
| `pypsa` | [Rolling-horizon example](https://docs.pypsa.org/stable/examples/rolling-horizon/): initialization, perfect foresight and horizon/overlap comparison | 6–10h | Toy has constant import cost, no export and no forecast errors. Match release/solver and check terminal energy; no profit or real-dispatch claim. |
| `elexon` | [Insights API Patterns](https://developer.data.elexon.co.uk/): publication-time dataset endpoints versus latest/derived feeds | 4–8h | Synthetic revision replay first; source terms/attribution and market meaning still matter. Public data is not a dispatch permission or production SLA. |
| `wntr` | [Getting Started](https://usepa.github.io/WNTR/getting_started.html): model I/O, hydraulic simulation and results | 4–8h | Explicit EPANET/Python prerequisite. Without approved runtime, inspect a synthetic network/units contract; that is not solver replication. |
| `neuralhydrology` | [Introduction](https://neuralhydrology.readthedocs.io/en/latest/tutorials/introduction.html): configuration, data prerequisites and train/evaluate state | 4–8h | Running notebook requires CAMELS-US and installed package. Audit synthetic basin/time rows and train-only scaling first. Data rights and large-training resources are separate. |
| `openmc` | [Developer tests](https://docs.openmc.org/en/stable/devguide/tests.html): prerequisites, failure causes, generated inputs and reference handling | 4–8h | Full tests require executable/module, cross-sections, some ENDF/NJOY and numerical settings. A synthetic numerical-manifest comparator needs no reactor/HPC access; it proves a narrower skill. |

## One illustrative 30–50h starting module

The JSON gives one composition example for a developer who has the selected prerequisites. It does **not** prescribe the user's schedule or replace the preparation DAG:

| Component | Focused hours assumed |
|---|---:|
| New debugging problem, using Missing Semester selectively | 4–6 |
| State/interleaving/failure trace, using OSTEP selectively | 4–6 |
| SQL/as-of provenance, using PostgreSQL selectively | 6–10 |
| Dependence/uncertainty, using selected18.05 material | 6–10 |
| Fresh synthetic data-feed diagnostic and withheld cases | 8–12 |
| Evidence memo and unaided explanation | 2–6 |
| **Total** | **30–50** |

The diagnostic specifies expected results **before** implementing a parser/replay: event/publication/revision times, duplicate or stale records, late arrivals and dependent observations. Reserve another source/schema family and a later publication period. Demonstrate correct state and explicitly explain one failure. If the same person authors the data and oracle, label it a single-author learning exercise; an independent reviewer has not been secured.

An existing approved Python/SQL stack is enough for the reduced exercise. A paper or SQLite fallback can demonstrate logic; it does not establish PostgreSQL isolation, ROS/DDS integration or a scientific model's behaviour. Nothing here authorizes dependency installation, a real account or an external submission.

## Access, terms and remaining gaps

- **Public reading differs from open licensing.** Missing Semester links CC-BY-NC-SA4.0; MIT OCW uses CC-BY-NC-SA4.0 with exceptions; ROS documentation source licence is CC-BY4.0. These do not automatically license linked software, datasets or model weights. No material was copied into a training corpus.
- **Books can be free to read while retaining copyright.** OSTEP offers free chapter PDFs and requests linking rather than instructor redistribution. Boyd's publisher permits the author-hosted book; full exercise solutions are instructor-request only. ISLP's author slides reserve rights with nonprofit educational permission. Modern Robotics offers a free preprint and public practice solutions while full book solutions remain instructor-only. Paid print books, combined PDFs, Coursera/MATLAB and optional cloud GPUs are unnecessary for the reduced reading/checks; no purchases or enrollments occurred.
- **Prerequisites were separated from inference.** MIT18.05 lists18.02. MIT18.06SC calls18.02 a formal prerequisite but explicitly says calculus is unnecessary for learning its subject. The Boyd text assumes advanced calculus/linear algebra. WNTR explicitly expects EPANET/Python. API/reference docs do not provide a formal curriculum, so their practical coding/domain requirements are labelled curator inference.
- **Version/runtime access remains conditional.** PostgreSQL18, SciPy1.18.0, scikit-learn1.9.1, Jazzy and NeuralHydrology1.13.0 are documentation observations, not installed-machine facts. Earlier round7 has selected energy/scientific code pins. PyPSA's current MIT and historical GPLv3 versions must remain separate. All package/data downloads require later approval.
- **Access limitations remain visible.** ROS rendered docs failed; official source indexes were read, with subordinate step-by-step/runtime behaviour not fully audited. StanfordEE364A's separate information URL was inaccessible; the Boyd book/preface and author materials were readable. No private learning platform, solutions portal or academic grading system was accessed.
- **No measured training return.** Four-to-twelve-hour slices and the30–50h composition are planning assumptions. They establish neither full-course completion nor transferable skill until tested on a fresh task. A certificate, notebook score or passed teaching suite does not establish a job qualification, operating authority, paid workflow value or a 2031 employment forecast.

Validation checks resource-ID uniqueness, existing technical references, source URLs, all proposed diagnostic states,4–12h slice bounds and the exact30–50h sum. The catalog deliberately supplies no invented prerequisite-route IDs; the pathway owner can join by the stable resource IDs.
