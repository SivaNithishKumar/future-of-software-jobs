# Database query rewriting: useful speedups, narrower correctness and cost evidence

The newly audited result is GenRewrite’s exact [*Query Rewriting via Large Language Models*, arXiv2403.09060v1](https://arxiv.org/pdf/2403.09060v1),14March2024. It is an older unreviewed-in-this-census preprint,not a latest2026method or finalpublication claim. The PDF still has placeholder venue/DOI/artifact fields,so those do not identify a released repository or accepted journal version. The fixed question preceded new calls.

The positive result is meaningful: an LLM-driven rewrite/correction/hint scaffold reports gains on selected TPC-DS queries beyond its zero-shot and traditional-rewriter baselines. It works above a native database optimizer,which still plans and executes the transformed SQL. It does not replace the whole database or establish speedups for every query. Exact counts/configurations and unresolved source joins are in the companion JSON.

## What was actually optimized

The selected evaluation uses one generated benchmark database and its query workload,with repeated rounds feeding newly useful natural-language rules and latency results into later hints. That is a legitimate recurring-workload optimization design. It is not an independently held-out query-family/schema/data/engine transfer experiment. A public benchmark may also occur in model training;this pass neither establishes absence of exposure nor alleges contamination. The workload’s role in adaptation must simply stay visible.

The semantic-repair loop asks the LLM to reason about counterexamples. Syntax repair instead uses nativeEXPLAIN feedback. Final equivalence checking is separately described as an external SlabCity tester followed by manual inspection. Those checks are real safeguards,but the selected v1 does not supply an independently audited universal equivalence certificate here. A correct-looking explanation or an executable plan is not enough.

The required semantic boundary includes duplicates/bag behavior,NULL/three-valued logic,types/collations,numeric and time rules,ordering/LIMIT,volatile operations and relied-on schema constraints. These are **uninspected obligations**,not demonstrated implementation failures. The original query is the rewrite target;preserving it does not independently establish that the original expresses the business requirement. No database,query corpus,tester or model was run.

## Denominators and the native baseline

The source explicitly assigns fallback speedup1when a method fails to find an equivalent rewrite. It would be wrong to say all failures are dropped. Conversely,the selected speedup plot covers queries where at least one method has a large gain;it is not the whole-workload distribution. Error rates,successful-query counts,attempts and repeated-round cumulative coverage must not be merged as interchangeable denominators.

The paper contains reporting joins left unresolved here:the abstract’s22large-speedup queries versus21in the main text/table,and a narrative increment that differs from the cumulative correction table. Both source statements are retained without inventing a corrected count,trace or ranking. They do not by themselves erase the measured positive or demonstrate an executable defect.

Three-run average latency is not a tail-latency or concurrent service guarantee. The authors describe restarting the database and clearing its cache,but the exactOS/page/disk state and commands were not inspected. Timeouts,rejected/unknown attempts,complete retry budgets and all human/validation costs were not fully recovered. Different correction work across an equal number of rounds is not automatically equal compute or review effort.

The [official PostgreSQL14EXPLAIN documentation](https://www.postgresql.org/docs/14/using-explain.html) is a strong native control. Plans,actual rows/loops,buffers and timing already support systematic diagnosis. Estimated planner cost uses relative units,not milliseconds or complete client-response cost. EXPLAINANALYZE actually executes and adds instrumentation overhead;its planning and execution fields exclude other work such as parsing/rewriting or delivery. Native optimization and ordinary statistics/index/query fixes must remain credible competitors,not intentionally weak baselines.

## The cost and preparation boundary

A recurring query can amortize rewrite work only while semantic validity and useful execution savings persist. The complete decision includes LLM calls,database validation and candidate runs,human review,deployment,revalidation as data/constraints change,regressions and operating support. A faster selected query and a historical per-round API bill do not establish a buyer’s return or how often the rewrite remains reusable. No new price,modern-engine comparison or job effect is inferred.

This pass closes at **two** primary bodies:the exact preprint and official native documentation. No third route was manufactured from the artifact placeholder. Exact released code,licences,model/APIrevision,tester semantics,data terms and a reproducible configuration remain unestablished. This is a source-methods audit,not replication or proof ofthe reader’s database skill.

There is no exact existing project activation. Data117does include join correctness,latency and cost,but its contract is multi-tenant ingestion/retrieval/recovery. It does not supply this rewrite benchmark,query split,approved database or checker. Evaluation146’s oracle principle is relevant reading,not permission to add a newSQLarm or borrow its hours. Original data117personal effort staysNULL;newproject,arm,exercise,keys and added hours remainnone.

A competent native/ordinary path can reject extra custom optimization for a predeclared legitimate need. That negative investment decision would not mean database work has no future. Useful remaining work is conditional on a real semantic/performance gap,permitted environment and independent acceptance;no enduring humanmoat,productionROI,credentialwaiver or2031developer forecast follows from this one benchmark. Earlier gate51/progression50and source57hold remain untouched. Different review and root retention are pending.
