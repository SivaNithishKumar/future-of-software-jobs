# Practical PQC migration and crypto-agility engineering

Owner: sectors_business. Round 10, checked **20 October 2026** against the research cutoff of **19 October 2026**. Read first: `security.md` S15, the existing PQC claim/project in `security-finance-interfaces-enrichment-round7.json`, and the crypto inventory/migration taxonomy. This extends those records; it does not repeat the standards announcement or migration-date survey.

No cryptographic software/binary was downloaded, installed or executed. No existing machine's key stores, network endpoints, customer estate or credentials were inspected. No production configuration, external account, shared catalogue or public discussion was changed. All experiments below are proposed.

## Finding

PQC migration is already a classical-software integration problem. The useful work is to identify **where cryptography actually protects an asset**, determine which implementation and peer negotiate it, preserve authentication and availability during a supported transition, and verify the result. Native platforms increasingly supply the algorithms and protocol support. A custom wrapper or “quantum readiness” dashboard must outperform those defaults on a concrete integration or evidence gap.

The strongest low-cost proof is a small, offline **inventory-to-negotiation-to-rollback acceptance ledger**. It can demonstrate compatibility and operational measurement. It cannot prove a cryptographic primitive secure, predict a quantum computer's arrival, certify an enterprise migration or establish a universal statutory deadline.

## Three core artifact families and their precise versions

### P1 — OpenSSL's native implementation, configuration and a real migration fault

OpenSSL **3.5.0, 8 April 2025**, introduced native ML-KEM/ML-DSA/SLH-DSA and default hybrid key shares. The branch release notes record **3.5.9, 29 September 2026**. An older downloads-page snapshot returned 3.5.8, so use the dated release notes rather than treating that cached table as the latest patch. Neither the installed local version nor a 3.5.9 source commit was verified. OpenSSL's code is Apache-2.0. [3.5 release notes](https://openssl-library.org/news/openssl-3.5-notes/), [project code/terms](https://github.com/openssl/openssl/)

**CVE-2026-2673** affected 3.5 before 3.5.6 and 3.6 before 3.6.2: `DEFAULT` could lose server group-tuple structure, preventing selection of a mutually supported hybrid group in some configurations. The native group documentation also warns that a larger ClientHello can expose broken firewall/TCP-segmentation assumptions, and distinguishes supported groups, offered shares, preferences and HelloRetryRequest. [Advisory record](https://openssl-library.org/news/vulnerabilities/#CVE-2026-2673), [3.5 group API/configuration contract](https://docs.openssl.org/3.5/man3/SSL_CTX_set1_curves/)

**Implication:** merely loading a PQ-capable library or listing an algorithm is not evidence that a connection used it. A policy/configuration regression can erase the intended negotiation without an algorithm failure. Do not reproduce this by deploying an old vulnerable binary; use the documented fault to design a regression expectation for an approved, patched implementation. Vendor backports and provider boundaries also matter, so a bare version string is not a complete vulnerability/compliance assessment.

### P2 — The TLS hybrid wire contract is now an RFC

**RFC 10024, August 2026**, is Standards Track; the earlier ECDHE-MLKEM draft is historical. It defines X25519MLKEM768, SecP256r1MLKEM768 and SecP384r1MLKEM1024. For X25519MLKEM768, the client share is **1,216 bytes** and server share **1,120 bytes**; these are key-share payloads, **not whole TLS-handshake sizes**. The RFC specifies input validation and abort behavior. It concerns hybrid **key agreement**, not a complete migration of certificate signatures, trust roots or every application protocol. [Final RFC](https://www.rfc-editor.org/rfc/rfc10024.html), [draft-to-RFC history](https://datatracker.ietf.org/doc/draft-ietf-tls-ecdhe-mlkem/history/)

**Implication:** test the final group identity/code point and the peer's actual support, not a similar legacy Kyber experiment name. A classical-certificate TLS session with hybrid key agreement has a different claim from a fully migrated PKI. Do not invent a new combiner, encoding or protocol extension for a migration portfolio. The RFC's IETF Trust/BCP 78 terms govern the document and its code components; it is not an MIT software package.

### P3 — Crypto agility is an operational architecture, not algorithm selection alone

NIST **CSWP 39 update 1, published 29 June 2026**, supersedes the December 2025 final. The PDF retains the original date in its running header; CSRC metadata identifies the update. Its asset-centric inventory includes code, libraries, applications, firmware, protocols and services. It connects policies, supply chains, updates and monitoring, and discusses constraints in hardware, secure boot and resource capacity. Larger keys/signatures/ciphertexts challenge existing protocol and storage assumptions; multiple algorithms also consume resources together. This is guidance, not a benchmark establishing a deployment's overhead or legal deadline. [Updated publication metadata](https://csrc.nist.gov/pubs/cswp/39/upd1/considerations-for-achieving-crypto-agility/final), [update-1 document, §§4–6](https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.39-upd1.pdf)

**Implication:** an editable cipher list is insufficient if the trust anchor, firmware verifier, certificate store, HSM or external peer cannot change. Prioritization needs a data-protection purpose and lifetime, an accountable owner, a supported change path and evidence after the change. No numerical constrained-device performance is inferred from this guidance.

## Inventory: what a developer must actually discover

The following is a proposed minimal evidence schema, not a claim that regex scanning provides an enterprise inventory:

| Dimension | Required evidence | Typical false conclusion to avoid |
|---|---|---|
| Protected asset/use | Data flow or signed object, confidentiality/authentication/integrity purpose, lifetime, owner | Every occurrence of “RSA” represents live vulnerable cryptography |
| Implementation | Application/build, library actually linked/loaded, provider, platform, policy and vendor patch evidence | An SBOM dependency or installed CLI proves runtime use |
| Protocol | TLS/SSH/IPsec/etc. version, negotiated group, authentication signature, full/resumed mode and peer | A TLS cipher-suite name identifies the key-exchange group and certificate algorithm |
| Keys/certificates | Algorithm/format, chain/trust-store role, expiry/rotation, key location and owner | A PQ KEM capability migrates the CA, code-signing or firmware trust chain |
| Dependencies | Both endpoints, proxies/terminators, SDK/runtime, hardware/firmware, outsourced service | Updating the client library migrates every hop |
| Change path | Native vendor support, compatibility matrix, maintenance owner, release/config provenance, rollback policy | A successful happy-path handshake is safe rollout evidence |
| Observation quality | Static candidate versus observed use; unknown/unreachable/unsupported states | Missing evidence means no cryptography or successful migration |

Do not collect secret key material for an inventory. On a permitted synthetic code/configuration bank, mark documentation strings, unused dependencies and dynamically selected libraries separately. A runtime observation applies to its exercised path and time, not every dormant feature. A cryptographic bill of materials can be a useful interchange artifact, but it still needs evidence linking a component to an asset and an observed use.

## TLS, PKI, updates and constrained systems

**Separate four outcomes:** implementation advertises support; peers share support; a specific handshake negotiates the intended group; the application accepts a correctly authenticated result under its policy. Record all four. Unknown algorithm/provider, hostname/chain failure, incompatible peer and policy failure are distinct diagnoses.

**Authentication remains independent.** Keep trust-chain/hostname verification enabled in the local test. Inventory certificate issuer/signature, application verification API, trust-store update and key custody independently of KEM negotiation. Algorithm availability in `libcrypto` does not prove support in TLS, X.509 encoding, a public CA, HSM or application binding. An offline test CA says nothing about those production systems.

**Full handshakes and resumption are different samples.** OpenSSL's group API documentation notes that PSK-only resumption can return a group from a previous connection. Therefore, tag resumption explicitly rather than counting a previously negotiated group as a fresh hybrid exchange. This is an additional instrumentation requirement from the same native API contract above.

**Rollback is a tested policy transition.** Retain a known-supported configuration and immutable dependency/configuration records. Decide whether a classical peer is allowed for this synthetic service. In an opportunistic policy, classical negotiation may be an expected compatibility result; in a hybrid-required policy it is a rejected outcome, even if TLS itself succeeds. Reverting a setting must not silently disable authentication, erase evidence or roll a patched library back to a vulnerable version. No production policy is selected by this report.

**Resource limits are whole-system limits.** The larger shares imply bytes and buffer pressure; they do not determine latency, RAM, energy or battery life. Certificate chains, signature choices, record fragmentation, retries, concurrency, CPU instructions, code size and the application's own work affect results. A desktop loopback benchmark cannot certify Cortex-M RAM/flash, an HSM, a boot ROM or a constrained network path. A local chunked transport can expose a parser/buffer assumption; it does not reproduce a firewall or actual path MTU. Device-specific claims need approved hardware/runtime and measurement later.

## Platform bundling is a serious opposing explanation

The default-provider baseline should come first. The OQS provider's current documentation explicitly defers standardized algorithms already supplied natively by OpenSSL 3.5+, describing its own role as experimental rather than duplicating maintained native implementations. It also distinguishes library support from TLS support and key formats. [OQS provider native-overlap and scope](https://github.com/open-quantum-safe/oqs-provider)

liboqs offers research/prototype integrations and warns against relying on the library to protect sensitive production data. Its top-level licence is MIT, with differently licensed bundled components. [OQS limitations and rights](https://openquantumsafe.org/liboqs/api/doxygen/index.html)

These are useful learning/contribution communities, not a reason to add an experimental provider when an approved native implementation already meets the exact contract. Similarly, a vendor update may solve the commodity part of migration. A custom product needs a residual problem—such as an unowned cross-platform dependency, unsupported appliance, weak inventory evidence or difficult trust-store transition—and a buyer who values resolving it. No such customer or paid margin was verified in this pass.

## Safe synthetic/offline 30/90-day experiment

This deepens `security-finance-interfaces-round7.project.pqc`; it does not start another flagship. Preserve that record's **25–40 focused-hour probe** and **additional 50–90 hours conditional extension**. The first **4–6 hours** must establish one permitted fixture, native baseline and independent oracle; otherwise narrow to static evidence or redirect. Calendar windows are planning labels. No installation, binary/software download, upstream execution or paid run is authorized by this research.

### First window: inventory and one local compatibility boundary

**Scope:** a tiny owned configuration/source bank and, only if an approved compatible runtime is already available, one in-memory/socket-pair or loopback client/server pair. No private estate scan, external endpoint, customer certificate/key, real tenant credential, privileged packet interception or system trust-store edit is needed.

Use roughly 4–6 h for the manifest/oracle, 6–10 h for inventory cases, 9–15 h for the bounded negotiation matrix, and 6–9 h for reporting, choosing totals within the 25–40 h cap. If runtime support is absent, deliver the inventory/transition test design and clearly mark negotiation unrun. Do not install an obsolete library to create a comparison.

**Version manifest:** record actual binary/library build and vendor patch provenance, linked provider, CPU/OS/runtime, TLS configuration, certificate algorithm/chain fingerprint, peer capability and policy, full/resumed mode, experiment seed/order and resource ceilings. The documentary reference is the OpenSSL 3.5 LTS family, including the known 3.5.9 release; a future executable must be independently pinned/approved and reviewed for then-current support/advisories.

**Independent oracle:** a hand-authored expected inventory for 12–20 purposive fixtures; an explicit policy table of peer capability versus acceptable outcome; and a fixed application message whose integrity/identity requirements remain constant. Do not derive the expected negotiated group from the same success string being tested. Instrument native group and certificate verification status separately. Test-only ephemeral credentials, if needed in a later authorized run, stay isolated and never appear in reports or logs; no real keys are inspected.

| Case | Expected acceptance contract |
|---|---|
| Classical-only peer, opportunistic policy | Correctly authenticated classical result, explicitly labelled; no false PQ claim |
| Classical-only peer, hybrid-required policy | Clear policy rejection; no silent fallback |
| Mutual supported hybrid group | Exact expected group plus ordinary authentication/application success |
| Mutual support but alternate initial share | Correct retry/negotiation state, recorded separately from an immediate handshake |
| Unknown/disabled provider or algorithm | Unsupported/configuration error is visible, not silently counted as success |
| Wrong hostname, untrusted/expired test certificate | Authentication failure remains a failure in every algorithm mode |
| Small chunk/buffer ceiling or truncated synthetic exchange | Bounded timeout/failure with retained denominator; no unbounded retry |
| Full versus resumed connection | Separate outcomes; no invented fresh exchange from cached metadata |
| Configuration rollback | Returns to its declared compatible policy with authentication and evidence intact |

Compare classical, native-default hybrid-capable and explicitly hybrid-required configurations at the **same application workload and authentication settings**. Run only finite, isolated tests with synthetic inputs. Do not implement new primitives, combiners or downgrade logic. An already patched native configuration is the main baseline; an experimental external provider is not required.

**Metrics:** inventory precision/recall on the declared fixture bank; unknown/candidate/observed counts; accepted application exchanges per planned attempt; negotiated group and authentication outcome; retries/timeouts; handshake bytes; active CPU/wall time and peak memory where actually measurable; human diagnosis/configuration minutes. Exclude warmup from a timing summary only if predeclared and still logged. Separate handshakes from application transfer and resumption. Report medians/ranges and raw counts, not population p95 or “enterprise readiness.”

### Conditional extension: update/rollback and one resource boundary

Use 10–20 h to define a slightly larger unseen fixture bank and expected transition states; 25–45 h for matched runs and one change, such as certificate-format acceptance or buffer/fragmentation handling; 15–25 h for analysis, rollback evidence and reproducibility. Stay within 50–90 h. Keep the mature native configuration as a comparator. If there is no supported second peer implementation already approved, call this a single-library configuration matrix, not cross-vendor interoperability.

A valuable negative result is that a native supported upgrade/configuration handles the task with less custom code and diagnostic effort. A valuable positive contribution is a small reproducible policy/format mismatch with exact versions and an independent expected outcome. Neither result establishes primitive security or hardware suitability. Upstream submission or public disclosure is a later authorized step; no confidential vulnerability details or production traffic are used here.

**Cost accounting:** distinguish measured CPU/bytes/memory and human setup/diagnosis from assumed labour valuation. Record existing-runtime costs as unavailable or amortization assumptions rather than zero. A local experiment can compare resource overhead; it cannot price customer outages, procurement, certification or inaccessible appliance replacements. Preserve unsuccessful attempts and unknown charges.

**Kill/redirect:** the installed approved runtime lacks support; native updates solve the entire problem; no independent inventory or authentication oracle exists; required real keys/HSM/appliance access is unavailable; the test disables certificate verification; policy failures disappear as “fallback success”; platform/device performance is extrapolated from a laptop; or a finite test is marketed as cryptographic certification. Do not broaden into a private network inventory to manufacture a use case.

## Prerequisite depth and professional routes

For migration engineering: understand TLS 1.3 handshake versus record protection, certificate paths and trust stores, key custody/rotation, providers and linking, binary formats, failures/timeouts, configuration release discipline and basic performance measurement. C/Python or an application-language TLS binding plus OS/network debugging are useful. Primitive implementation, constant-time assembly, cryptanalysis and physical side-channel evaluation are **deeper routes**, not skills demonstrated by this migration project.

| Official/community route | Why it fits | Constraints and proof |
|---|---|---|
| [OpenSSL contributor guide](https://openssl-library.org/community/getting-started/) | Maintained native TLS/crypto implementation and regression tests | Reproduce a configuration/negotiation issue with a minimal permitted fixture. Apache-2.0 code; exact future build pin required; no submission made |
| [NCCoE Migration to PQC community/project](https://www.nccoe.nist.gov/applied-cryptography/migration-to-pqc) | Discovery and interoperability workstreams, public findings and professional community route | NIST guidance/prototypes are not product approval; draft practice-guide volumes remain distinct from the updated crypto-agility white paper. No sign-up/contact performed |
| [IETF TLS group and RFC source discussion](https://datatracker.ietf.org/wg/tls/about/) | Protocol review, compatibility and final-versus-draft status | Bring precise wire/negotiation evidence; no new custom protocol claim. Public technical channel, not a hiring guarantee |
| [Open Quantum Safe team](https://openquantumsafe.org/team/) | Research integrations and contributors; linked to PQCA/Linux Foundation | Experimental scope and mixed component rights; native platform alternative must be assessed first |
| [PQShield Director of Software Engineering role](https://pqshield.com/careers/apply/4989532101/?gh_jid=4989532101) | Official role joins crypto libraries, protocols, secure implementation and product delivery | Remote only in listed European countries including UK; explicitly excludes applicants elsewhere. Requires 10+ years development and 5+ leadership; not an entry role or India-remote promise. Availability needs recheck |
| [QNu Labs employer-posted cryptography-engineer sample](https://in.linkedin.com/jobs/view/cryptography-engineer-%E2%80%94-post-quantum-secure-implementation-at-qnu-labs-4468587097) | Bengaluru in-person early-career example emphasizing C/Python, math, negative tests, reproducible benchmarks and constrained targets | Page says **no longer accepting applications**. It requires demonstrated primitive/protocol implementation and is deeper than this migration exercise; company deployment/certification marketing was not independently audited |
| [University of Bristol Cryptography research profile](https://www.bristol.ac.uk/research/impact/stories/cracking-online-security-in-a-post-quantum-world/) | Official profile links Chloe Martindale and the group to PQC, machine-checked crypto and software/hardware security | Research/admissions/funding not audited; use as a professional research route, not an arrival-date forecast or job offer |

No private contact details are collected. Recruiting, contributor and official lab/community pages are sufficient professional routes. Remote geography, right to work, defence/security restrictions and degree/funding eligibility must be checked for an actual application. An India-based developer can perform the public software proof; that does not establish eligibility for a UK-restricted role or access to an HSM/regulated estate.

## 2031 implication and remaining uncertainty

The plausible developer opportunity is **ownership of compatibility and migration evidence inside a platform, PKI/security or vendor-integration team**. Native bundling may eliminate a broad standalone “PQC switch” product while increasing demand for people who can resolve legacy interfaces and operational constraints. The relative size and paid accessibility of that residual work were not measured here.

The proposal adds depth under the existing inventory and migration nodes, reusing the existing project and NIST reference. It is not applied to shared files. Important remaining gaps are actual customer priority and willingness to pay, complete runtime/peer inventory, exact executable/provider pins, approved hardware measurements, real PKI/HSM support and independent security review. A working synthetic handshake demonstrates its finite contract only; it is not evidence that the entire system is quantum secure.

