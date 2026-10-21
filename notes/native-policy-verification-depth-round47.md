# Native policy verification: what a learned policy generator can actually certify

AutoCedar supplies a substantive counterexample to treating policy generation or checking as an untouched human specialty. Its model proposes policies while native Cedar/SymCC/SMT machinery checks a fixed, approved target. The newly audited v1 claim is **boundary satisfaction**, not a general guarantee of correct organizational intent or deployed effects. Native validation is already strong and has explicit input assumptions; neither source justifies a new human moat or job forecast.

## Fixed question and two-source method

The census found Cedar’s formal/native advantage and AutoCedar’s221-task headline in security2/directory and metadata8, but no full target/quantifier/admission/attempt audit. Formal11 concerns other verification benchmarks. The question was fixed before reads in prespec `eacf9923…`. Exactly two new primary surfaces were read: [AutoCedar2607.03656v1](https://arxiv.org/html/2607.03656v1),4July2026, and [official Cedar validation methods](https://docs.cedarpolicy.com/policies/validation.html). Same-source windows only followed. No extra classic-Cedar paper, repo, code, solver, model/API, benchmark/corpora, accounts or installation was accessed or executed. The source budget is closed.

## The actual formal target

A schema defines request universe RΣ. The plan supplies floors F, ceilings C and liveness slices G. The paper’s theorem states:

**union(F) ⊆ Allow(P) ⊆ intersection(C), and Allow(P) intersects every approved G.**

This is stronger than passing a finite request suite: symbolic comparison ranges over the supported Cedar fragment. It is also narrower than many convenient summaries. Unless lower and upper bounds coincide, it need not select one unique golden-policy equivalent. A liveness slice requires **at least one** permitted request in that class; it is not eventual application completion or a promise that every legitimate user works. Universal required permission belongs in an appropriate floor. Rate-limit-style atoms contribute only compiled finite obligations, not atomic runtime rate limiting. See v1§III-B,definition1/theorem1/proposition1,lines177–215.

Target construction may repair schemas and properties before admission/freeze. During subsequent search the proposer cannot change the approved plan; typed feedback preserves whether a failure means excess permission,tightening; missing permission,loosening; or an empty slice,expansion. This is a useful enforced separation of generation and authority. It is not guaranteed termination: a compatible target may lack a concise implementation, and the model can exhaust its20-iteration budget or repeat failures.

Conditional soundness assumes the approved plan captures organizational intent and the supported verifier/compiler/solver model is faithful. Mechanical validation of an artifact and a reviewer accepting its plain-English rendering are distinct. Source-span/atom/clause associations help audit, but the paper explicitly says the trace is **not proof of clause provenance**. This pass did not inspect backend proofs, implementation/refinement, timeout/unknown handling or the formal-to-runtime mapping.

## Native controls are serious competitors

Cedar’s official page describes schema/type/optional-attribute checks, a Lean validation-soundness result and differential testing against Rust. This is meaningful automated assurance; it is not a claim that the entire Rust/application stack was formally proved here. Validation is a **separate API**, not automatically performed for each authorization request. Request/entity data must satisfy the schema contract, and schema changes can require policy revalidation.

The page names exceptions: integer overflow, missing entities (including references), and malformed extension strings in non-strict mode. Native request/schema parsing utilities exist, but they do not establish every referenced entity’s existence. Errored policies are ignored; a validation pass is not universal error-free evaluation or an automatic global-deny policy for every runtime diagnostic. A true attribute value,authenticated caller/tenant,complete mediation,current version and atomic business effect are separate application contracts—not evidence that native platforms lack solutions.

## Positive results and their units

The paper reports both tested proposers converging221/221 on authored CedarBench:79mutations of official domains plus142hand-authored tasks. These are not221 companies or deployed permission incidents. The fixed100-task ablation is an especially useful contrary case: **raw native-verifier feedback already achieves94/100**, versus100/100 with the full signal layer. That native-feedback arm **still includes the LLM proposer**; deterministic verification alone is not being credited with writing94policies. TableIII costs are total for that slice, while TableII reports per-scenario averages; API-model cost is not full review/setup/solver/operating cost.

Direct baseline Pass@3 means validation in at least one of three generations. Category1 invents its schema and receives validation-only comparison; Category2 shares AutoCedar’s schema/target. Property-check denominators include only validation-passing candidates, while full-scenario rates retain221. Invalid cases are N/A, not measured semantic failures. Two external GPT policies received authors’ claimed trivial syntax/casing repairs; that claim was not independently code-checked.

Across three extracted requirements-corpus scenarios, reported semantic requests match76/76,68/68 and38/38. They were constructed from decisions determined by the source prose under the AutoCedar schema, not independently audited production policies or ambiguous-input coverage. The14-participant/98-response randomized A/B artifact study favours AutoCedar82/98; repeated probe answers are not98 independent people, correctness certificates or a live intent-review study. OptionalHITL feedback was sparse. AutoCedar repeated-runN,seeds,error bars,raw reset/attempt lineage and unseen requirements-family exposure were not recovered. Those gaps limit robustness/transfer, not the conditional formal statement.

## The unsecured bridge

A missing tenant restriction in an approved target can leave all modeled checks passing while the intended business rule is absent. That is an exposed conceptual assumption failure, not a demonstrated checker bypass or an actual exploit. Likewise, a policy can pass type validation while a runtime entity is missing; the native docs explicitly retain that exception. Neither a policy-set proof nor a rate-limit-style current-context check establishes atomic cross-request commit,fulfilment or a real permitted effect.

The useful transferable skill is to identify which layer owns vocabulary,intent,typing,symbolic permission,request facts and committed outcomes. Native tools and agents can automate these layers; this paper’s review assumption does not reserve a permanent human seat. No paid authoring-hours reduction,customer preference,current role,training return or venture moat is measured.

## Existing artifact and access boundary

Only authority141’s **existing evidence/report** can carry this source distinction: which approved boundary was checked,request/entity provenance,version/fragment/check status and actual effect scope. It retains35–55FIRST +70–120conditionalADDITIONAL hours,with4–6included launch gate and unknown personal availability. No new exercise,key,course,role or nativeCedararm is added. Its ordinary scoped/native/delegated and ledger oracles remain unchanged. Missing approved runtime/rights/independent intent/effect oracle keeps the work source-only; a competent native solution stops redundant custom work.

The paper is arXiv non-exclusive,not a code/data grant. Prior metadata8 pins the AutoCedar repo at0201565abf5993e258764d3f0ef83a59d3b4962e,8September2026,with inspected Apache2.0rootLICENSE/NOTICE; that is carried metadata,not a fresh repo inspection,paper-matched release or all-artifact clearance. Exact CedarCLI/SymCC/cvc5/Python/provider/corpora versions,rights and resources still require a later approved preflight. Current native engine build is unpinned. No packages,models,keys,raw human responses or code ran.

Stevens paper authors and Cedar/AWSdocumentation are relevant public research/technical routes; publication-time affiliation is not current employment,maintainer permission or an invitation. No personal contacts or jobs were searched. Original notes/catalogue/statuses/index remain frozen; source-author overlap is explicit. Different methods review,source-world/implementation acceptance and final retention remain pending.
