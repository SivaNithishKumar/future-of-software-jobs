# Eight targeted learning slices for newly deepened paths

Checked 20 October 2026. Companion: [structured slices](<targeted-learning-slices-round16.json>). These extend the [existing resource map](<learning-resources-round8.json>) and [preparation DAG](<preparation-dependencies-round8.json>); they do not replace either or create a second curriculum. No shared catalog was edited.

Choose a slice only when a fresh diagnostic exposes that specific gap on one selected route. Each 4–8h range is an assumed focused reading/design allowance, not time to complete the resource. The eight are alternatives or small gap fillers, never eight additive courses or a guaranteed 30-day schedule. Existing competence can justify skipping them.

All exercises and transfer checks below are proposed. Public worked examples, supplied solutions and the guide's own exercises are study material. No unfamiliar task, independent setter, answer key or test secrecy has been established. A later separate setter must prepare and audit a new case; if the learner authors or sees its key, call it practice. Normal assisted study and a later agreed unaided prediction/explanation check are different activities.

## 1. Formal contracts: intended property versus proved annotation

**Assumed slice: 6–8h.** [Primary resource](https://dafny.org/v4.11.0/OnlineTutorial/guide) — Dafny 4.11.0 guide; examples use Dafny 4 syntax; [Supporting contract/rights](https://raw.githubusercontent.com/dafny-lang/dafny/v4.11.0/LICENSE.txt) — v4.11.0 MIT licence.

Read only: Methods, Pre- and Postconditions and Assertions; Loop Invariants. Use the Abs/counter/Fibonacci material only as worked study; completing the full guide is not required. Practical prerequisites (curator inference): Imperative code, loops, integer/array reasoning and basic Boolean logic. No research degree is a prerequisite for this reading slice.

Study output: Annotate one small method on paper, state what the contract omits, and predict an invariant failure before consulting the guide's worked reasoning. Do not run Dafny now. Fresh transfer design: Have a later setter provide a tiny bounded receipt/retry state machine unrelated to Abs/Fibonacci, with a missing frame condition or weak invariant. Ask for a counterexample, corrected specification and an explanation of what a proof would not establish about persistence or the real service. Audit the key with independent traces/reference reasoning; no proof success is claimed without a later approved run.

Rights/access: Tagged Dafny licence is MIT and explicitly includes associated documentation files; preserve notices. Solver/tool dependencies retain separate terms. Read without login; no enrollment or purchase. Later gates: Dafny/prover/toolchain execution only in a later approved environment; no install is assumed. No hardware needed for reading/paper reasoning. No degree/enrollment gate to read. A formal-methods research role can have separate research/credential requirements; ordinary data migration does not thereby require them. A specification proof is conditional and does not grant production or safety sign-off.

Existing module links: `preparation-round8.module.implementation`, `preparation-round8.module.oracles`. Adds an exact formal-contract tutorial missing from the18-resource map; does not replace the existing OSTEP/runtime or independent-oracle modules.

## 2. BIM: IDS applicability, requirement and validation scope

**Assumed slice: 4–6h.** [Primary resource](https://docs.ifcopenshell.org/ifctester.html) — Live docs labelled 0.9.0post1; not an executable release pin; [Supporting contract/rights](https://docs.ifcopenshell.org/autoapi/ifcopenshell/validate/index.html) — Live validation API; [Supporting contract/rights](https://github.com/IfcOpenShell/IfcOpenShell) — Mixed repository terms, carried forward from round9 rights audit.

Read only: IfcTester: Examples and CLI manual. Validation API: parse/type/cardinality checks and express_rules option. Ignore the geometry-engine/entire IFC specification for this first slice. Practical prerequisites (curator inference): Read simple Python/JSON/XML and distinguish schema, identifier and requirement. No architecture licence is needed to inspect an authored data contract.

Study output: Trace applicability versus requirement for one IDS example and label which claims a successful check cannot make. Treat complete example code as exposed study, not an assessment. Fresh transfer design: A later setter supplies a different tiny synthetic entity/property table plus two model revisions: one changes identity or units, another changes only representation. Predict requirement applicability, pass/fail/unknown and the precise difference claim. Use a separately authored table; do not treat tool agreement as physical design truth.

Rights/access: Round9 verified core/IfcTester LGPL-3.0-or-later, Bonsai GPL-3.0-or-later and mixed-component exceptions. IDS specification CC-BY-ND 4.0; official certification fixtures CC-BY 4.0. Public reading is not a blanket licence for all linked models. Read without login; no enrollment or purchase. Later gates: IfcOpenShell/IfcTester and geometry dependencies require later approval and exact version/config pin. No cleanroom, construction site or new device needed for the reading/data-contract exercise. No IFC/model download now. The exact public CC-BY fixture in round9 needs a commit/byte pin and attribution before any later approved use. Architectural/structural/safety judgement is a different gate; this data exercise does not establish engineering sign-off.

Existing module links: `preparation-round8.module.implementation`, `preparation-round8.module.data-meaning`, `preparation-round8.module.oracles`. Adds exact IDS/validation reading to the generic scientific-data/oracle modules; no second BIM curriculum.

## 3. PQC migration: supported groups versus offered shares and actual negotiation

**Assumed slice: 4–6h.** [Primary resource](https://docs.openssl.org/3.5/man3/SSL_CTX_set1_curves/) — OpenSSL 3.5 API/document branch; report10 records patched 3.5.9; [Supporting contract/rights](https://www.rfc-editor.org/rfc/rfc10024.html) — RFC 10024, August 2026; [Supporting contract/rights](https://github.com/openssl/openssl/) — OpenSSL 3.5 code Apache-2.0, carried forward from round10 audit.

Read only: Group-list/tuple handling, predicted key shares, client versus server preference and selection pseudo-code; RFC10024 hybrid group definitions/key-share validation boundaries only. Do not take the entire TLS/RFC corpus. Practical prerequisites (curator inference): Basic TLS1.3 client/server negotiation and configuration reading; distinguish key agreement, certificate authentication and trust store. No cryptographic primitive research is required to begin.

Study output: Make a paper inventory of algorithm presence, supported list, sent share, negotiated group and resumed/full mode. Identify evidence missing from a version string. Worked API examples are study cases. Fresh transfer design: A later setter varies peer support, sent shares and preference/tuple structure in a synthetic transcript table, with an omitted observation and a resumed session. Predict what is determined, when retry/fallback is permitted by the declared policy, and what stays unknown. Key must be independently checked against the native selection contract; no session or security claim is measured here.

Rights/access: OpenSSL current code Apache-2.0. RFC document/code components governed by IETF Trust/BCP78 terms; not an MIT package. No third-party software or keys acquired. Read without login; no enrollment or purchase. Later gates: No TLS/server/client run now. Later loopback reproduction needs approved patched native library/runtime and explicit policy. No HSM or quantum hardware needed for the reading slice. No degree/enrollment requirement for reading or ordinary migration integration. Primitive design, specialized research and regulated approval are separate. No production config change, universal deadline, security guarantee or cryptographic implementation.

Existing module links: `preparation-round8.module.data-meaning`, `preparation-round8.module.authority`, `preparation-round8.module.production`. Deepens exact native negotiation semantics missing from broad security/crypto headlines; does not repeat the NIST/NCSC standards timeline.

## 4. FHIR: validator configuration versus meaning-preserving records

**Assumed slice: 4–6h.** [Primary resource](https://hapifhir.io/hapi-fhir/docs/validation/instance_validator.html) — Live HAPI docs; exact runnable dependency pin remains a gate; [Supporting contract/rights](https://hl7.org/fhir/R4/resource-definitions.html) — FHIR R4 4.0.1 Meta.versionId/lastUpdated; [Supporting contract/rights](https://hl7.org/fhir/R4/observation-definitions.html) — FHIR R4 4.0.1 effective[x]; [Supporting contract/rights](https://hl7.org/fhir/R4/license.html) — CC0 plus trademark/third-party exclusions.

Read only: HAPI: FHIR Conformance Concepts, FHIR Instance Validator and Running the Validator; raw-string versus parsed-object discussion. R4: Meta.versionId/lastUpdated and Observation.effective[x] only. Practical prerequisites (curator inference): Read JSON/Java examples, identifiers, typed times and simple local-unit arithmetic. No medical degree is needed for the nonclinical schema exercise.

Study output: Annotate which configured profile/terminology checks ran and which are missing. Separate source update time from observation time. Existing complete validator snippets are study, not unseen testing. Fresh transfer design: A later setter provides two synthetic source namespaces sharing a local ID, an opaque version, a unit change and a partial date. Predict a neutral staging state and which failures a configured native validator can or cannot settle. Independent field/state table is the oracle; no actual clinical codes or patient records.

Rights/access: FHIR R4 specification CC0 with trademark and third-party terminology limits; HAPI Apache-2.0 as carried forward from round12. CC0 does not grant SNOMED/LOINC or patient-data rights. Read without login; no enrollment or purchase. Later gates: No HAPI/server or validator execution now; later approved Java/package/terminology pin required. Existing laptop sufficient for paper/JSON reasoning. No patient records, terminology gate acceptance or vocabulary download. Nonclinical owned fixtures only. Domain/clinical semantic review and authorized workflow data are separate from software schema skill; no treatment or clinical-validity claim.

Existing module links: `preparation-round8.module.implementation`, `preparation-round8.module.data-meaning`, `preparation-round8.module.oracles`. Fills exact validator/time/state reading absent from the general data-meaning catalog; no full health-informatics course.

## 5. CDC: exported snapshot, slot replay and target-ready state

**Assumed slice: 4–6h.** [Primary resource](https://www.postgresql.org/docs/18/logicaldecoding-explanation.html) — PostgreSQL 18; [Supporting contract/rights](https://www.postgresql.org/docs/18/logical-replication-architecture.html) — PostgreSQL 18; [Supporting contract/rights](https://www.postgresql.org/docs/18/logical-replication-restrictions.html) — PostgreSQL 18.

Read only: 47.2.2 Replication Slots;47.2.5 Exported Snapshots;29.9.1 Initial Snapshot; restrictions on DDL/sequence/TRUNCATE only. The existing 13.2 isolation/14.1 EXPLAIN slice remains unchanged. Practical prerequisites (curator inference): Basic table/key/transaction concepts and sequence/retry reasoning. SQL can help when the workflow uses a database; formal-methods or research-degree mastery is not a prerequisite.

Study output: Draw a source committed cut, copied rows, retained log and consumer progress. State what becomes visible and what must remain unknown when a log range is absent. Fresh transfer design: A later setter changes a two-table snapshot/stream schedule with a deleted key, duplicate delivery and a source restart. Predict exact target state at a declared ready barrier and demonstrate one bad arrival-order merge. Key comes from an independent committed-state ledger, not the candidate replay function. Synthetic log numbers do not become universal connector IDs.

Rights/access: PostgreSQL License covers software/documentation with notice conditions, carried forward from round13 primary audit. Managed service terms or connector licences are separate. Read without login; no enrollment or purchase. Later gates: Reading/design only. Real PostgreSQL/connector crash replay,lock behavior and WAL retention require later approved disposable runtime; no containers now. No new hardware. Owned synthetic rows only; no private work schema/logs. Ordinary integration depth comes from transaction/recovery reasoning and real experience, not an inferred director's research degree.

Existing module links: `preparation-round8.module.data-meaning`, `preparation-round8.module.runtime`, `preparation-round8.module.oracles`. An extension of the existing PostgreSQL resource, adding an uncovered handoff/recovery contract rather than a second SQL course.

## 6. Supply-chain evidence: verified identity, subject and expected authority

**Assumed slice: 4–6h.** [Primary resource](https://slsa.dev/spec/v1.2/verifying-artifacts) — SLSA 1.2; [Supporting contract/rights](https://raw.githubusercontent.com/in-toto/attestation/main/spec/v1/statement.md) — Statement/v1; live source revision not pinned; [Supporting contract/rights](https://cli.github.com/manual/gh_attestation_verify) — Live native verifier manual; runtime version unverified.

Read only: SLSA Step 1 Check SLSA Build level and Step 2 Check expectations; in-toto subject/predicateType; native verifier Understanding Verification and Additional Policy Enforcement. Skip signing setup and full standards implementation. Practical prerequisites (curator inference): Basic hashes, JSON, source revision and CI/workflow concepts. Understand authentication versus authorization before applying evidence policy.

Study output: Annotate a worked statement: which fields bind bytes, source or signer, which are producer-controlled claims, and which expectations come from the consumer. No signing keys or actual bundles needed. Fresh transfer design: A later setter swaps an artifact under an unchanged filename and varies reusable-workflow identity, approved source and a missing trust input. Predict separate native-verification NOT_RUN/unknown status and conditional policy verdicts. Key must not accept an unsigned producer's mockVerified flag as trust. Do not claim a forged-signature test from unsigned fixtures.

Rights/access: SLSA Community Specification License 1.0; in-toto attestation Apache-2.0. GitHub service permissions/terms and CLI binary version separate; no account used. Read without login; no enrollment or purchase. Later gates: No verifier execution,keys,CI,release or registry action. Later verification uses approved existing artifact/bundle/trust material and tools only. No HSM/new hardware for reading. No admission requirement for these public docs; cryptography/security research credentials remain role-specific. No compliance,secure-code,complete-inventory or release authorization claim.

Existing module links: `preparation-round8.module.authority`, `preparation-round8.module.data-meaning`, `preparation-round8.module.oracles`. Adds exact source-to-artifact policy reading missing from generic identity/provenance modules; native generation/verifiers remain the baseline.

## 7. Accessibility: keyboard, modal focus and error-state coverage

**Assumed slice: 4–6h.** [Primary resource](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/) — Live APG guidance; [Supporting contract/rights](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/examples/dialog/) — Illustrative example; Read This First; [Supporting contract/rights](https://playwright.dev/docs/accessibility-testing) — Live guide; round15 proposes Playwright 1.64.1/axe 4.14.0; [Supporting contract/rights](https://playwright.dev/docs/aria-snapshots) — Live semantic-state contract.

Read only: APG modal Keyboard Interaction and Roles/States/Properties; example Read This First. Playwright state-specific scans/tags/exclusions and aria snapshot matching. Read complete example code as exposed study only. Practical prerequisites (curator inference): Native HTML labels/buttons/forms, DOM events and elementary state transitions. No new device or disability simulation.

Study output: Write a paper keyboard/focus/error table for the already designed task editor. Compare native control behavior with what a role attribute alone supplies; no UI is authored now. Fresh transfer design: A later setter supplies a different inline-edit/discard flow in which the invoker can disappear and an asynchronous error arrives after another edit. Predict reachable keyboard path,focus target/allowed set,error relationship and exact task state. Separate DOM intent from actual AT announcement. Independent test material is not yet created or sealed.

Rights/access: APG repository W3C Software and Document License; Playwright Apache 2.0 and axe MPL 2.0 at round15 tags. Browser/wrapper terms separate; no examples copied or tools installed. Read without login; no enrollment or purchase. Later gates: No UI/browser/scan/AT run. Later approved implementation and exact browser/runtime/axe wrapper pins needed. No new hardware. Existing configured AT may support a later approved check; downloading/enabling new assets is separate. A public-doc slice needs no degree; actual roles may require professional testing,AT skills or credentials. AT/specialist/disabled-user review requires separate authorized participation; scan success never certifies usability or WCAG conformance.

Existing module links: `preparation-round8.module.implementation`, `preparation-round8.module.data-meaning`, `preparation-round8.module.oracles`. Narrows prior multimodal/voice plans to a conventional multi-state web contract; not a second accessibility survey.

## 8. GPU performance: time the accepted workload and its transfers

**Assumed slice: 4–6h.** [Primary resource](https://docs.nvidia.com/cuda/archive/13.0.0/cuda-c-best-practices-guide/index.html) — CUDA 13.0.0 archive deliberately selected, not a latest-version claim.

Read only: 9.1 Timing, especially CPU timers versus GPU events;9.2.2 Effective Bandwidth Calculation;10.1 Data Transfer Between Host and Device, including overlap/pinned-memory context only. Do not read the entire CUDA guide. Practical prerequisites (curator inference): Arrays,byte arithmetic,time units and basic CPU/device/asynchronous execution. C/CUDA implementation depth is conditional,not a prerequisite for every application role.

Study output: Annotate an explicitly hypothetical trace: preparation,warm-up,transfers,kernels and output. State which time/byte boundary a bandwidth or speedup number uses. The guide's solved arithmetic is study material. Fresh transfer design: A later setter creates a new two-path trace with transfer overlap,changed batch and equal output-quality requirement. Predict which comparisons are supportable and where synchronization/timing changes the denominator. Use independent interval/byte accounting,with units; a synthetic trace cannot establish measured GPU speed,energy or bottlenecks.

Rights/access: Official public NVIDIA documentation under its Notices; no open redistribution licence verified and no general IP licence is granted by the document. Link rather than reproduce it. SDK/sample-code/dependency terms are separate. Read without login; no enrollment or purchase. Later gates: No CUDA/compiler/benchmark execution or package download. Actual measurement needs later approved compatible driver/toolchain. No GPU purchase or rental. Paper/trace analysis is accessible now; hardware timing/power claims require real authorized hardware. No degree/enrollment needed to read; specialized kernel/architecture research roles have separate prerequisites. No silicon performance or training/inference savings claimed from arithmetic.

Existing module links: `preparation-round8.module.runtime`, `preparation-round8.module.measurement`, `preparation-round8.module.native-specialism`. Adds exact transfer/timing sections to the hardware-claim/native-specialism branch; CS336 remains a separate deeper option,not a prerequisite to this paper exercise.

## What this preparation establishes

The two new tutorial/reference additions are a versioned Dafny contract/invariant guide and the deliberately selected CUDA 13.0 archive. Other entries select exact missing sections from the new BIM/PQC/FHIR/CDC/supply-chain/accessibility reports. CDC explicitly extends `learning-round8.resource.postgres` beyond its existing isolation/EXPLAIN slice. GPU timing is adjacent to `learning-round8.resource.cs336`, without making the full course a prerequisite.

Each entry links actual existing module IDs. Proposed project/technical branches are labelled queued and identify their owning report; their inclusion in the root catalog is not assumed. Formal and GPU text-only project links do not receive invented catalog IDs.

Resource availability, mechanism understanding, an actual native implementation, representative workflow validity, role eligibility and sustained ownership are separate evidence levels. No learner competence, hidden-test validity, credential, production permission, independent user review or employment outcome has been demonstrated. Ordinary migration or API integration does not acquire a research-degree requirement merely because a specialized research/leadership advert elsewhere has one.

Checks performed here concern authoring/bookkeeping: eight unique slice IDs, 4–8h bounds, links to the 17 read DAG module IDs and 23 official resource pointers; JSON serialization was checked. No course/tool exercise, benchmark, proof, GPU operation, browser/AT interaction, software/data download, enrollment, outreach or external mutation was performed. All live-document/runtime pin gaps remain visible in the structured companion.

