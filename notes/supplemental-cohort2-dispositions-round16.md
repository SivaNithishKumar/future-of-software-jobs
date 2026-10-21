# Supplemental cohort 2: structural adaptation and remaining gates

Status: draft, unapplied, unmounted, and not substantively accepted. This is a local data-preparation result, not a new source review or a readiness decision. The validated core builder, cohort 1 pack, cohort 1 display projection, and its compactor remain unchanged.

## Stable handoff

| Owned output | SHA-256 | Bytes including newline |
|---|---|---:|
| supplemental-cohort2-adapter-round16.py | ae3e71bd2a0a3ee3d642467a8091c5929c3e114b646be97de174153aa1f7fd3d | 30,208 |
| supplemental-cohort2-pack-round16.json | cb981e8781c65c5dd6cdb4cd313b62e94bf47aeabb646b22e9e675e2b2a87a34 | 1,118,336 |
| supplemental-cohort2-validation-round16.json | 21c7cfba7de05f004e4bd473c137c83804b4e13bab36f3953b38d447836fdf17 | 2,209 |

The pack records its inventory time as 2026-10-19T20:18:07.814574+00:00. Included stable packets cover industrial inspection, state estimation, weather decisions, battery health, health interoperability, and data migration. Migration's JSON, report, and arithmetic receipt were present and included. No dedicated stable GPU/kernel option JSON matched this bounded local inventory. That exclusion says nothing about broader corpus coverage or labour demand, and later files are not silently added to this snapshot.

The source manifest carries exact file hashes for 27 inputs. Every adapted occurrence has its source file/hash, JSON pointer, canonical record hash, original ID field or explicit absent ID, and state-field pointers. Complete authored structured packets are embedded alongside adapted views, so uncommon or currently unmapped fields remain available without reinterpretation.

## Conservation and local validation

| Item | Retained |
|---|---:|
| Occurrences | 312 |
| Inspection / state estimation / weather | 58 / 112 / 43 |
| Battery health / interoperability / migration | 15 / 44 / 40 |
| Occurrences with no authored ID | 49 |
| Proposed technical nodes, all unmounted | 27 |
| Full project occurrences | 8 |
| Typed reference occurrences | 651 |
| State-field values and hashes | 1,382 |
| Existing-identity reuse descriptors | 5 |
| Existing-record update proposal groups | 3 |
| Separate fixture/validation receipt files | 5 |
| Retained public-source text receipts | 56 |

These are heterogeneous records and receipts, not counts of employers, vacancies, independent experiments, or scientific results. Opaque supp16.occ handles identify source occurrences; they do not manufacture semantic IDs. Two nonunique authored source IDs are retained as groups: anomalib appears in 13 saved file receipts and opencv in two. They function as source/repository grouping tokens, not unique file or employer identities. No last-writer selection or alias merge is accepted.

All 27 source file hashes, 312 record pointers/hashes, 1,382 state values/hashes, 651 reference source pointers and their occurrence targets, and six complete structured packets passed local consistency checks. The proposed hierarchy resolves and is acyclic. Four adapter self-tests passed: strict array pointer handling with object-key contrast, opaque provenance identity, hierarchy-cycle rejection, and lossless shared-dictionary roundtrip. The separate supplemental-cohort2-integrity-round16.json records the replay and protected-input hashes.

The 56 already saved code-text bodies remain addressed by exact companion file/hash/pointer. Each local UTF-8 body SHA-256 and recorded Git blob SHA-1 calculation matches. This proves consistency of the retained bytes with their recorded blob, not a fresh remote read, paper-environment match, execution, or correctness. Source bodies are not re-downloaded or executed.

## Reference and identity dispositions

The 651 references comprise 73 exact existing technical-node joins, five existing preparation/resource/selection joins, 207 within-cohort occurrence joins, four existing core occurrence-group joins, one canonical navigation proposal, four within-cohort proposed-node joins, 52 saved-file/proof-slice receipts, 304 carried URLs, and one explicitly unresolved resource selector. Carried URLs are not freshly verified. All links remain inactive.

The five reuse descriptors point to existing NIST navigation and the Oxford DRS/Maurice Fallon/Hilti paper/data records. They preserve source-time unit, person, artefact, role, and contact scopes; they do not inherit parent facts or legal-employer equivalence. The three Hilti-related metadata update groups retain their authored dictionary fieldUpdates and original targets, but have no new raw-before-overlay application guards here. They remain separate and unapplied.

Nine proposed nodes lack authored kind or claim class. The interoperability and migration root nodes use source kind option and claim type evidence-and-inference, outside the current core enums. Both literal values are retained as schema conflicts. Two authored dataset records are not silently coerced into the core data grouping. Battery has no exact authored tree/preparation join or proposed node; no ID is inferred from its title. Inspection, state estimation, interoperability, and migration also lack exact authored preparation joins, while their prose prerequisites remain intact.

The weather snapshotAndAssetHref field is an instruction to resolve an actual STAC asset and immutable Icechunk snapshot before approved access. It is preserved as a declared-unresolved-resource-selector with selectedAsset null, not interpreted as a resolved URL or semantic ID.

## Proof, access, and role boundaries

Fixtures and arithmetic retain independent slice types and file receipts. They do not replace full project launch, dataset permission, oracle, representative workload, runtime, physical-validation, or employer-entry gates. Weather's in-packet arithmetic is also distinct from its project. Battery's six synthetic cases and metadata validation establish neither real-data rights nor trained accuracy/BMS-control validity. Health's synthetic FHIR/OMOP plan establishes neither patient-data access nor clinical correctness, hospital reliability, regulatory compliance, or paid demand. Migration's arithmetic uses an authored abstract envelope rather than captured connector behaviour; it supplies no database/WAL/Kafka/cloud crash or performance execution evidence. The eight full project records retain their authored 30/90-day content and limits independently of those slices.

The pack carries authored rights, versions, contacts, contribution limits, role requirements, and role currency without a new hiring check. In particular, the Met Office advert remains one vacancy at two levels with its stated deadline and eligibility filters; NISE remains historical with extension/current intake unknown. Eatron's no-open-position state, Breathe's sales/talent-community surface, Maxwell's indexed-only rows, generic institutional channels, and archived BatteryML contribution limits do not become live engineering vacancies or active maintainer invitations. Direct, indexed, closed, historical, generic-channel, and unknown states remain distinguishable in the full authored packets.

## Display estimate and acceptance gates

The existing held lossless shared-dictionary codec roundtrips a 164,368-byte estimate containing all six principal structured packets, complete fixture data, project-readiness contexts, proposed nodes, and schema gaps. It is an estimate, not a final supplemental display file. It excludes final projection wrappers/navigation, UI, and the retained code-body texts, whose exact local receipts are available separately. No hidden runtime fetch is proposed.

Core plus held cohort 1 display data is 811,890 bytes. Adding this estimate gives 976,258 bytes before final wrappers, UI, or separately reviewed context addenda. This does not establish the final 1 MB gate. Compression must not conceal decisive caveats or convert missing context into acceptance.

The pack exposes 26 schema/link/disposition gaps. Final integration requires explicit decisions on node meanings/parents and schema compatibility, preparation mappings where justified, current resource selection, guarded treatment of the three existing-record updates, identity scopes, authored-role currency, proof/context sufficiency, and final display size. No unsupported claim was accepted to make the structure look complete.

The adapter can be replayed into an existing reviewer-owned output directory using python3 supplemental-cohort2-adapter-round16.py --output-root /absolute/owned/directory; --self-test runs its four local tests. A replay records a new inventory timestamp, so compare source/occurrence invariants rather than expecting byte identity with this snapshot. It imports only two pinned, self-authored standard-library helpers. This task performed no retrieval, installation, external mutation, third-party execution, or source-input writes.
