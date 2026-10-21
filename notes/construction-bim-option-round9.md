# Construction option: IFC interoperability, validation and operational handover

Owner: sectors_business. Round 9; public-source research checked **20 October 2026**. This is a bounded addition to the construction software branch, not a market forecast or a selected primary specialty. Publications are dated below; live documentation snapshots are identified separately. No tools were installed, model collections downloaded, cloud accounts used, people contacted or shared catalogues changed. Proposed attachments are in the separate JSON file for root review.

## Why this belongs in the developer tree

There is a concrete software path between an exported building model and a trustworthy operational decision: parse the declared schema, preserve units and coordinate frames, identify the same assets across revisions, check the required information, explain changes, and join model elements to an asset register or event stream. These are data engineering, geometry, versioning and workflow problems. A visually convincing model does not establish any of them.

The attractive entry experiment is **a small, explainable validation-and-diff pipeline with independent fixtures**. The commercial hypothesis is narrower: reduce rejected handovers or time spent reconciling asset changes. Existing open tools already perform substantial parts of this work. A new generic IFC viewer, unchecked JSON converter or LLM description of a model would be a weak starting point.

## Standards and validation boundaries

**Version and exchange contract.** buildingSMART lists **IFC 4.3 ADD2, version 4.3.2.0**, as official and associated with **ISO 16739-1:2024**; IFC 4.4 and IFC 5 remain development work. Earlier IFC4 and IFC2x3 releases remain relevant. IFC implementation is version- and model-view-specific: “supports IFC” does not establish support for every entity, geometry representation or exchange view. Freeze schema identifier, addendum, view, exporter/version and selected purpose. [Official specification database](https://technical.buildingsmart.org/standards/ifc/ifc-schema-specifications/), [standards server](https://standards.buildingsmart.org/)

**Different checks answer different questions.** buildingSMART's Validation Service describes four layers: STEP syntax; schema/formal constraints; normative rules; and non-normative industry practices. It supports IFC2X3, IFC4 and IFC4X3_ADD2, requires an account for its hosted service, and does not provide geometric visualization/coordination. No hosted file upload was attempted. [Validation Service scope](https://dev.validate.buildingsmart.org/)

**IDS checks the information contract.** IDS 1.0 was approved on **1 June 2024**; pre-1.0 versions were beta. It expresses expected entities, properties, classifications, materials and values. Auditing an IDS file and checking an IFC model against it are separate operations. A syntactically valid requirement can still select the wrong objects or omit the requirement that matters. [buildingSMART IDS explanation](https://www.buildingsmart.org/standards/bsi-standards/information-delivery-specification-ids/page/4/), [official specification repository](https://github.com/buildingSMART/IDS)

**Software correctness is not design or physical truth.** An IFC object may carry an allowed `FireRating` string while the underlying design, installation, certificate or current condition is wrong. Correct geometry can describe an obsolete design. A complete maintenance field can refer to the wrong real asset. Standards conformity should therefore produce a report about its declared scope; it cannot by itself constitute structural, fire, clinical or construction acceptance. Qualified domain review and project-specific evidence remain separate gates. This is a scope inference from what the validators check, not advice on how to approve a building.

## Technical problem branches

| Branch | Precise failure | Strong baseline / proof target |
|---|---|---|
| Schema/version/view | Renamed attributes, unsupported entities, wrong header, required exchange content lost by an exporter | Native parser/schema checks plus a pinned exchange contract; unsupported must be distinct from invalid |
| Units and coordinates | Millimetres treated as metres; local coordinates confused with map coordinates; missing vertical datum; transforms applied twice | Normalize explicit units and composed placements; independent synthetic dimension/transform oracles |
| Identity and federation | GUID regenerated, reused or duplicated; one physical asset appears in multiple discipline models | File-scoped identity plus authoritative asset ID and provenance; ambiguous correspondence stays unresolved |
| Information semantics | Instance versus type property; missing versus empty; value stored under a custom property name; classification version changes | Declared IDS plus explicit applicability counts, inheritance and mapping tests |
| Geometry | Extrusion versus tessellation; opening subtraction; inconsistent tolerances; conversion failure hidden as an empty object | Native geometry processor and separately defined physical-equivalence checks; preserve failures |
| Change provenance | A noisy text diff appears significant; meaningful property or containment change is omitted | Native IfcDiff configured for the required relationships; immutable input/report hashes and reasoned change categories |
| Operational integration | BIM element joined to the wrong CMMS/equipment/sensor ID; old observations treated as current; asset replacement overwrites history | Versioned mapping, event/ingestion times, quality flags, replay/idempotency and explicit source authority |

### Coordinates and units need explicit treatment

The IFC specification distinguishes a projected map CRS from the local engineering coordinate system. `IfcProjectedCRS.MapUnit` can define map-axis length units; when omitted, project units supply the default. A vertical datum may need identification as well. [IFC4.3 ProjectedCRS definition](https://standards.buildingsmart.org/IFC/RELEASE/IFC4_3/HTML/lexical/IfcProjectedCRS.htm)

IfcOpenShell's geometry documentation distinguishes local vertices from the element transformation matrix and gives an explicit project-units-to-SI conversion example. It supports meshes/BReps and recommends an iterator for bulk processing, with kernel/settings affecting capability. [Geometry processing documentation, snapshot labelled 0.9.0post1](https://docs.ifcopenshell.org/ifcopenshell-python/geometry_processing.html)

**Proposed proof:** synthetic boxes with analytically known dimensions, placement and volume, including an equivalent millimetre encoding and a translated/rotated version. Keep coordinate reference, units and tolerance in the manifest. A bounding-box match alone cannot prove shape equality: different solids can share bounds. Actual surveyed placement and installation tolerances are outside this software-only exercise.

### Identity and diff semantics are already partly solved

IfcDiff assumes an element's `GlobalId` remains consistent between versions. It reports added/deleted/changed elements, supports cross-schema comparisons, and defaults to attributes plus geometry; property, type, container, aggregate and classification relationships can be selected. Its geometry comparison intentionally examines the underlying IFC definition: extrusion versus mesh is a change even if the resolved boundary is the same. Tolerance comes from the new model's precision. [IfcDiff documented contract](https://docs.ifcopenshell.org/ifcdiff.html)

**Implication:** do not call that behavior a defect when the desired product is “representation changed.” If an operator instead needs “physical geometry changed,” define and test a separate equivalence contract. GUID churn can make one revision look like widespread deletion/recreation; silently guessing correspondence can be worse than reporting an unresolved match. Asset replacement should not inherit old sensor/maintenance history merely because a model ID stayed constant.

### Operational handover has a mature extraction baseline

IfcFM already extracts IFC asset/facility information into spreadsheet and machine-readable forms, including COBie-related presets. A hand-built CSV exporter is not an original contribution by itself. [IfcFM scope and supported mappings](https://docs.ifcopenshell.org/ifcfm.html)

Bentley's Synchronization API already supplies connectors that transform geometry, properties and relationships into iModels, detect incremental differences, produce changesets and retain synchronization history/diagnostics. This is stronger than a one-time conversion baseline, although hosted access and commercial terms are separate from the code. [iTwin synchronization overview](https://developer.bentley.com/apis/synchronization/overview/)

**Possible remaining contribution:** a reproducible mismatch or loss report on a clearly specified mapping, or an acceptance ledger that makes otherwise hidden unit, identity, applicability and stale-event failures visible. Compare against the native tool first. Do not assume a new standalone platform is necessary.

## Two research sources: what they demonstrate and what they do not

**An Inspection of IFC Models from Practice — Noardo, Arroyo Ohori, Krijnen and Stoter, 3 March 2021, Applied Sciences, DOI 10.3390/app11052232.** The study inspects **57 practitioner models**, some related within federated projects, with subsets outside the authors' full semantic expertise. It finds substantial variability in modelling, semantics and georeferencing. The sample is historical and selected, not a current estimate of exporter failure rates. The useful lesson is to test actual use-specific information rather than assume schema richness means a deliverable contains it. The article is CC-BY 4.0; this does not automatically grant rights to every underlying practitioner model. [Institutional final-paper copy](https://repository.tudelft.nl/file/File_53bc6e1a-b2ee-4d06-bd70-b9d911484fe0?preview=1)

**Data Integration for Space-Aware Digital Twins of Hospital Operations — Moretti et al., 2025, Automation in Construction 176, 106276, DOI 10.1016/j.autcon.2025.106276.** The Addenbrooke's Hospital case links an IFC4 model to navigation and discrete-event simulation, testing lift failure and changed functional layouts. It is an initial step toward an operational twin: the paper limits implementation to BIM/navigation/process modules, leaving other proposed integrations outside scope. Its appendix includes case-specific door naming, simplified geometric extraction and unit assumptions. These are transfer conditions to audit, not evidence of a universal hospital integration. The research was funded by Cambridge University Hospitals NHS Foundation Trust; no causal paid-production ROI is established here. [Paper and scope](https://discovery.ucl.ac.uk/id/eprint/10208682/1/Moretti_1-s2.0-S0926580525003164-main.pdf), [metadata and CC-BY 4.0 statement](https://discovery.ucl.ac.uk/id/eprint/10208682/)

The hospital demo's public code is MIT and names Yin-Chi Chan and Nicola Moretti as contributors. Code accessibility is useful for reading the interfaces, but the original facility data, clinical systems and real-time integrations must not be assumed available or covered by the same permissions. [BIM-DES demonstration repository](https://github.com/yinchi/histopath-bim-des)

## Tools, code and rights for the experiment

| Artifact | Verified scope / terms | Use and boundary |
|---|---|---|
| [IfcOpenShell ecosystem](https://github.com/IfcOpenShell/IfcOpenShell) | Core Python/library tools, IfcTester and IfcFM are LGPL-3.0-or-later; Bonsai is GPL-3.0-or-later; some components note exceptions | Reuse parser/geometry/IDS/diff/FM machinery. Check exact package/dependency terms before redistribution; the repository has mixed licences |
| [Validation API](https://docs.ifcopenshell.org/autoapi/ifcopenshell/validate/index.html) | Attribute/type/cardinality checks and an `express_rules` option; documentation distinguishes parse-stage errors | Preserve parser logs and actual checks run; one success flag must not imply every validation layer ran. Some prose about WHERE-rule coverage is internally awkward, so verify the pinned implementation before claiming exhaustive rule coverage |
| [IfcTester](https://docs.ifcopenshell.org/ifctester.html) | Authors/reads IDS, checks models, exports JSON/HTML/BCF and other reports | Native requirement-checking baseline, not a new feature to build |
| [That Open web-ifc](https://github.com/ThatOpen/engine_web-ifc) | MPL-2.0; C++/WebAssembly IFC reader/writer | Optional second implementation for differential checks; agreement between tools is not an independent ground truth |
| [iTwin.js](https://github.com/iTwin/itwinjs-core) | MIT library; infrastructure data/visualization/integration | Platform/contribution baseline. Open library terms do not make cloud services, connectors or data free |
| [Official certification fixtures](https://github.com/buildingSMART/Certification-datasets) | Repository licence CC-BY 4.0 | Small public-model fixture source with attribution and change notices. The old Sample-Test-Files URL now redirects here; older community collections are separate |
| [Fixture licence](https://github.com/buildingSMART/Certification-datasets/blob/main/LICENSE) | CC-BY 4.0 explicitly stated | Retain source attribution; record modifications and selected file/version |
| [IDS specification licence](https://github.com/buildingSMART/IDS/blob/development/LICENSE) | CC-BY-ND 4.0 | Keep standard/XSD unmodified; distinguish the standard from separately authored instance requirements. Do not label the specification MIT |

**One exact candidate fixture:** [IFC4 Simple-Scene Building-Hvac.ifc](https://github.com/buildingSMART/Certification-datasets/blob/main/IFC%204.0.2.1%20%28IFC%204%20ADD2%20TC1%29/Simple-Scene/Building-Hvac.ifc). The inspected file page reports **109 KB**, `FILE_SCHEMA(('IFC4'))`, and an exporter header dated **23 June 2026**. The file was not downloaded or executed. Before launch, pin its actual commit and byte hash plus the adjacent licence; those are not invented here. Pair it with independently authored tiny synthetic controls, rather than downloading a building-model collection. No hospital model or patient data is needed.

Live IfcOpenShell documentation was labelled **0.9.0post1** when checked. This is a documentation snapshot, not a verified release/commit pin or a claim that every described feature existed in an earlier package. Install nothing in this research pass. A later approved run must pin the compatible library, kernel, schema and configuration actually used.

## Equipment-light 30/90-day option

This is a conditional option within the existing preparation policy: **30–50 focused hours for a first probe**, and **another 90–150 only if worthwhile**. “30/90 days” is a planning window, not an entitlement to additional hours alongside every other specialty. A CPU laptop and tiny fixtures are plausible for the first probe; actual RAM/runtime availability has not been assessed. No GPU, cleanroom, survey scanner, paid CAD authoring licence or live building connection is required for the software exercise. New dependency downloads still require explicit approval.

### First window: explain a model's acceptance and change report

1. **Contract and rights, 6–10 h.** Select the one public fixture and at most two tiny owned controls. Freeze schema/view, exporter metadata, source/commit/hash, licence, units, placement convention, tolerances, expected asset count and chosen information requirements. The synthetic contract might require a stable asset tag, manufacturer/model fields and spatial containment for selected maintainable equipment. These are demonstration requirements, not an owner's real AIR or a construction standard.
2. **Baseline, 8–12 h.** After any necessary software approval, run the parser/validation logs, native IfcTester, correctly configured IfcDiff and a minimal IfcFM extraction. Record every unsupported representation, exception and empty selection. If no approved runtime is available, stop at a source/fixture specification; do not report runtime validation.
3. **Independent mutation oracle, 10–18 h.** Create a bounded set of 24–40 known mutations and non-changes. Define expected outcomes before comparing reports. Native checker results are the baseline, not their own truth label. Keep untouched controls and a few combined mutations out of development.
4. **Reproducible acceptance package, 6–10 h.** Produce a small machine-readable report with input/config hashes, applicability counts, rule evidence, normalized asset table, semantic/representation changes and unresolved correspondences. Human-readable explanations should point to actual entities and rules, not make broad engineering assertions.

**Required failure and non-change cases:**

- Wrong schema header, truncated STEP, missing required attribute and duplicate identity; distinguish parse failure from an unsupported feature.
- Missing, blank and wrongly typed properties; required value on a type instead of an occurrence; a classification from the wrong version.
- No matching objects for an intended mandatory requirement; never let an empty selection masquerade as a useful pass.
- A 1,000× unit mistake versus equivalent metre/millimetre geometry; nested placement, 90-degree rotation and map/local-frame mismatch.
- Stable GUID plus changed asset tag; regenerated GUID with otherwise unchanged asset; duplicated objects across files; explicit ambiguity.
- Extrusion-to-mesh equivalence versus a genuine dimensional change; changed opening; geometry-conversion exception; different shapes sharing a bounding box.
- Property-only and containment-only changes with geometry unchanged; reordered serialization as a non-change under the semantic contract.

Use analytically known synthetic dimensions and transformations for geometry truth. For the public fixture, inspect only a small declared subset manually; a plausible viewer rendering does not establish every quantity. An engineering-domain oracle is not available for real building adequacy, so keep that endpoint out of the proof.

**Metrics:** detected/undetected planted changes by category, false positives on equivalent encodings, applicability coverage, unsupported/error counts, unit/coordinate errors, stable report reproduction and reviewer minutes to explain a result. Report raw counts and stratified failures; these purposive cases do not estimate field-wide accuracy or p95 reliability. Prefer a smaller explained result over an unexamined “all valid” dashboard.

### Conditional second window: operational identity and stale data

Choose **one** extension: validated asset handover or a synthetic event join. For the latter, create a tiny public/owned asset register and replayed observations with model GUID, external asset ID, model version, event time, ingestion time, unit and quality flag. Include out-of-order/duplicate events, a replaced sensor, a model revision deleting an asset and an ambiguous mapping. Preserve history and require explicit resolution of identity conflicts. This is a simulator/replay exercise, not a live building twin.

Use roughly 25–40 h to define the schema/versioned joins and an independent expected-state oracle; 40–65 h for implementation and adverse-case comparison with the mature extraction/synchronization baseline; 25–45 h for holdouts, measurement and documentation, fitting within the approved extension. Demonstrate idempotent replay, reversible mappings, invalidation after revision and a clear stale-data state. An SQLite table plus deterministic event replay is an adequate baseline; a graph database or agent is not automatically necessary.

An original contribution could be a minimal reproducible interoperability failure, a precise unit/identity regression test, a documented lost-field mapping or improved diagnosis of unsupported geometry. Upstream publication/submission is a later external action requiring authorization. No contribution is claimed until actually reproduced and accepted.

**Kill/redirect gates:** permissions or redistribution rights unresolved; source model has no declared purpose; only the library under test defines expected truth; parser errors disappear; geometry assumptions do not fit the selected model; native tools already meet the contract; zero-applicability passes conceal missing assets; or a commercial claim needs customer models, engineering review or CMMS access that is unavailable. A software demo must not be presented as engineering sign-off or validated paid demand.

## Teams, companies, labs and professional routes

| Route | Work that makes it relevant | Entry proof and limits |
|---|---|---|
| **IfcOpenShell / Bonsai community** — [contribution documentation](https://docs.ifcopenshell.org/introduction/how_to_contribute.html), repository issues | Parser, geometry, IDS and FM tools; documentation, bugs and tests are explicit contribution modes | A small licensed fixture and expected-versus-actual reproduction. No construction qualification inferred from an accepted software test |
| **buildingSMART International** — [IDS repository](https://github.com/buildingSMART/IDS), [validation source/service route](https://dev.validate.buildingsmart.org/) | Exchange standards, implementation/certification fixtures and conformance rules | Requirement ambiguities or interoperability evidence with exact versions. Hosted validation requires an account; none used. Standards participation and certification are not interchangeable |
| **Bentley Infrastructure Cloud / iTwin** — [official senior cloud-ETL role, dated 1 September 2026](https://jobs.bentley.com/job/Vilnius-Senior-Software-Engineer-%28Cloud-ETL-%26-Data%29/1415133700/), [iTwin.js contributor route](https://github.com/iTwin/itwinjs-core) | Role describes engineering-format ingestion, schema versioning, deterministic execution, transactional consistency, idempotency and observability; asks for 7+ years and C#/.NET/Azure experience | Concrete software-team evidence in **Lithuania**, not an India/UK remote-work promise. Demonstrate an ingestion/diff failure contract before attempting the full cloud stack |
| **Autodesk AEC Data / interoperability** — [UK architect, requisition 26WD94957](https://autodesk.wd1.myworkdayjobs.com/en-US/Ext/job/Software-Architect_26WD94957-1), [Pune senior principal, 25WD93301](https://autodesk.wd1.myworkdayjobs.com/fr-CA/Ext/job/Principal-Engineer--AWS--C---React--Vite-Tauri-_25WD93301-1) | Official indexed descriptions connect schema/API/cloud architecture and connectors to BIM/IFC/CAD; the Pune role mentions C#/.NET, SDKs and design-data interoperability | Senior samples, not entry-level predictions. Search-index text was readable but direct live Workday bodies were empty; **availability and exact current conditions remain unconfirmed**. Use official recruiting pages, no application sent |
| **UCL Bartlett School of Sustainable Construction** — [Mahendrini Ariyachandra's official profile](https://profiles.ucl.ac.uk/98899-mahendrini-ariyachandra/about) | Public profile identifies BIM/digital-twin teaching/research and information interoperability, IoT and infrastructure | A precise interoperable-asset proof relates better than a generic 3D demo. Profile supplies the public professional route; funding, supervision availability and admission eligibility were not checked |
| **IIT Madras BTCM / TLC2, Aritra Pal / DICE** — [official research-opportunities page](https://tlc2.iitm.ac.in/open-position/), [group contact route](https://tlc2.iitm.ac.in/organizational-and-policy-research/) | Lists C'TWIN vision+BIM integration and 5D BIM-from-specification topics under MS/PhD, with basic programming and multidisciplinary collaboration requirements | A verified India research route, **not a salaried software vacancy or demonstrated deployed twin**. Degree/admission/funding/site-data conditions need checking before commitment; no enquiry sent |
| **Cambridge/UCL BIM-DES authors** — [public demonstration repository](https://github.com/yinchi/histopath-bim-des), paper authorship above | Model-to-navigation/process interfaces and explicit operational requirements | Reproduce a tiny synthetic transfer case; code issues are a relevant professional channel. Hospital data access, clinical evaluation and production integration are separate prerequisites |

No private contacts are collected. Public profile, issue/contribution, lab and official recruiting pages are sufficient routes for this directory. The existence of an indexed role or a research topic is not evidence that anyone will reply, hire, fund or purchase the proposed work.

## Opportunity economics and the 2031 interpretation

Potential users include an information manager rejecting repeated handover defects, a BIM coordinator reconciling revisions, an asset owner importing maintainable equipment, or a platform team maintaining connectors. Those are **hypothesized users**, not validated customers. A paid problem requires a particular recurring rejection, owner of the budget, permission to process representative files, baseline review time and an agreed acceptance contract.

This branch competes with free validators, mature IFC tooling, commercial coordination products, platform connectors and existing engineering consultancies. Project-specific property mappings and procurement can consume the apparent margin. Account-dependent APIs, proprietary source-model access and on-site truth may constrain a solo developer more than compute. The first credible commercial gate would be repeatable reduction in reconciliation/rejection effort at matched acceptance quality; no price, sales cycle, local salary or market-size estimate was verified here.

AI may help draft mappings, explain rules or produce tests. Unchecked generation cannot be the oracle for schema compliance, coordinates, physical equivalence or asset identity. A defensible 2031 path combines software reliability and data/geometry depth with one asset workflow and a domain partner. Specialized engineering design, surveying and physical asset acceptance require different expertise and evidence from an IFC software test.

## Residual gaps and attachment status

The structured proposals add a bounded child under `darkside2031.industry-commerce.agriculture-construction.construction`; they are **not applied** to the taxonomy or institution/source catalogues. Root should deduplicate Autodesk, Bentley, UCL and IIT records already present elsewhere.

Remaining gaps: actual buyer economics; a real owner's information requirements; current role availability/eligibility; exact tool/fixture commit pins; per-package redistribution details; representative multi-exporter models; independent domain review; operational data access and source authority. No source bytes or model hashes were retained in this research-only pass. The two papers are evidence of failure mechanisms and a bounded integration case, not a current market-demand measurement.

