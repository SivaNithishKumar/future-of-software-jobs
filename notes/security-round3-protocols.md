# Round 3: delegated authority across agent protocols and business commits

Bounded technical audit, checked 19 October 2026. This supplements the market/platform comparison in round 2; it does not repeat a general formal-methods overview. Source inspection only: no installations, running implementations, network scans, tenant access, outreach or exploit execution. The experiment below is a reproducible design specification, **not an implemented or executed harness**.

## Main result

An agent's authority crosses several different contracts: login, client identity, resource-token audience, workload identity, allowed action, task ownership, current business state and final commit. A correct contract at one layer does not automatically establish the next one. Established protocols already provide important protections and should be reused. Many residual problems are ordinary application/distributed-systems problems rather than grounds for a new agent-identity protocol.

Three particularly consequential counterexamples to oversimplified architectures:

1. **Token exchange need not attenuate privileges.** Current Keycloak standard exchange can add optional scopes unless a downscoping policy is configured. RFC 8693 actor history does not itself constitute a recursively enforced chain of task constraints.
2. **Proof of possession is not approval of an exact action.** DPoP binds a token to a key and HTTP request context, but does not generally sign the request body. A compromised legitimate client may still act with its own bound key.
3. **Cancellation acknowledgement is not stopped execution.** Current MCP Tasks explicitly permits cooperative cancellation without an eventual cancelled result. Neither token revocation nor a task cancellation request rolls back a committed business effect.

The personal competence opportunity is being able to identify, test and operate these seams. It does not establish a large new role count, wage premium or independent-product moat.

## Reference versions and implementation snapshot

| Reference | Version/status inspected | Consequence for this audit |
|---|---|---|
| [MCP versioning](https://modelcontextprotocol.io/docs/2026-07-28/learn/versioning) | Current **2026-07-28**; older 2025-11-25 is historical | Current protocol negotiation is per request with protocol metadata; server/discover replaces assumptions about a compulsory old initialization handshake. Do not analyze all current implementations as permanently stateful MCP sessions. |
| [MCP authorization](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization) | 2026-07-28 transport authorization profile | Profile references a selected subset of OAuth-related standards, including an OAuth 2.1 draft. This is not evidence that OAuth 2.1 is a finalized RFC. HTTP authorization remains optional for implementations, with requirements when supported. |
| [MCP security practices](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices) | 2026-07-28 documentation | Discovery, client registration, consent, token and execution boundaries require implementation controls. DCR is deprecated in current MCP in favor of Client ID Metadata Documents, while compatibility remains. |
| [MCP Tasks extension](https://modelcontextprotocol.github.io/ext-tasks/specification/2026-07-28/tasks.html) | 2026-07-28 extension | Tasks moved out of experimental core. Each task request requires authentication/authorization. Cancellation is cooperative, not a rollback guarantee. |
| [OAuth Security BCP, RFC 9700](https://www.rfc-editor.org/info/rfc9700/) | January 2025 BCP | Current security recommendations help prevent known OAuth attacks; they do not define a refund's business invariant. |
| [OIDC Core](https://openid.net/specs/openid-connect-core-1_0.html) | Core 1.0 incorporating errata set 2 | ID Token identifies an authentication result for the relying party. API authority requires the appropriate access-token contract and application checks. |
| [RFC 8693](https://www.rfc-editor.org/info/rfc8693/) | Token Exchange, January 2020 | Token service protocol can express delegation/impersonation; deployment policy determines allowed exchanges and resulting authority. |
| [RFC 9396](https://www.rfc-editor.org/rfc/rfc9396.html) | Rich Authorization Requests, May 2023 | Fine-grained authorization_details already exists; do not invent a new standard merely because a scope string is too coarse. Type-specific meaning still needs agreed enforcement. |
| [RFC 7009](https://www.rfc-editor.org/rfc/rfc7009.html) / [RFC 7662](https://www.rfc-editor.org/rfc/rfc7662.html) | Revocation, August 2013 / introspection, October 2015 | Revocation propagation, cascading policy and introspection-cache staleness require explicit operational design. |
| [RFC 9449](https://www.rfc-editor.org/rfc/rfc9449.html) | DPoP, September 2023 | Sender constraint/replay protection does not itself confer intent or general HTTP payload integrity. |
| [SPIFFE concepts](https://spiffe.io/docs/latest/spiffe-about/spiffe-concepts/) / [JWT-SVID](https://spiffe.io/docs/latest/spiffe-specs/jwt-svid/) | Live specifications inspected, 19 October 2026 | Workload identity, trust domains, audiences and expiry; no automatic human/task/business authorization. |
| [Official MCP TypeScript SDK release](https://github.com/modelcontextprotocol/typescript-sdk/releases/tag/v2.3.1) | v2.3.1, 5 October 2026; tag commit fcef852f6cdafea07f36cf6fae69b37c8adf85be | Inspected release metadata, pinned license, auth guide and package metadata through public GitHub API; not built or tested. Minimum engines Node >=20 is package compatibility, not a recommendation to use an end-of-support runtime. |
| [Keycloak](https://github.com/keycloak/keycloak/releases/tag/26.8.1) | 26.8.1, 13 October 2026; tag commit 24ed1dadf3f246a555adb6d3d4a99e9b3003fb3b | Documentation is live, so exact release behavior must still be checked in a later approved experiment. Standard V2 and legacy V1 differ materially. |
| [SPIRE](https://github.com/spiffe/spire/releases/tag/v1.15.4) | 1.15.4, 15 October 2026 | Release metadata inspected, not installed. Not needed for the minimum experiment below. |

### A useful SDK-level boundary

The pinned [TypeScript SDK authorization guide](https://github.com/modelcontextprotocol/typescript-sdk/blob/v2.3.1/docs/serving/authorization.md) requires the application to supply verifyAccessToken. expectedResource adds audience comparison against AuthInfo.resource; without it that helper performs no such comparison. The guide also identifies an older Express adapter (2.0.1) that does not forward the option. A verifier might independently enforce audience, so an omitted helper option is not automatically an exploitable application. Test the complete verifier/adapter combination. This is why protocol compliance cannot be inferred from installing an official SDK or checking one package's version.

## Authority path and property boundaries

The following is an analytical map, not a claim that every product uses this exact architecture:

Human/operator → authenticated host → orchestrator workload → MCP/API resource → downstream service → business-state transaction → external effect.

For autonomous background jobs, an operator/service principal may be the authority source; there need not be a human actively approving every call. The distinction is whether the configured authority is valid and bounded for the job, not whether the principal is human.

| Layer | What a correct implementation establishes | What remains outside that property |
|---|---|---|
| OIDC login | Issuer/subject authentication for the intended relying party, with required validation | Whether the user may access tenant T, whether an API should accept the ID Token, or whether a current business action is approved |
| OAuth client/consent | Authorized client/resource/scope flow under the issuer's policy, correct browser-request binding | A readable consent screen does not bind every future argument or delegate's action to the user's precise intent |
| Audience-bound access token | Intended recipient/resource and granted claims under the issuer's signature/token format | A valid payments token can still contain authority broader than the intended refund; application must validate token type, issuer, audience and actual resource access |
| Token exchange | New token according to the authorization server's exchange policy | Automatic monotonic downscoping, instantaneous descendant revocation, or universally interpreted nested delegation restrictions |
| DPoP / mTLS / workload identity | Possession of a bound credential/key or attested workload identity under a trust domain | A legitimate workload's correctness, a transaction payload's intent, or resistance to untrusted code running inside the authorized client |
| Native/ordinary policy decision | Permit/deny under supplied principals, attributes and policies | Accuracy/freshness of supplied attributes, mediation of alternate paths, atomic relation between check and later commit |
| Task handle / trace / cancellation | Defined task status/access/control messages and recorded evidence | Business cancellation, reversal, compensation, cross-tool ACID or physical stop |
| Transaction commit | Application-enforced state transition under chosen database/external-service semantics | Correct organizational policy or safe effects outside that transaction boundary |

“Establishes” is conditional on the protocol's attacker model, configuration, implementation correctness and trusted infrastructure. The table does not claim an unconditional cryptographic guarantee for a whole deployed agent.

## Precise threat models and counterexamples

### T1 — Wrong-resource token or discovery mix-up

Attacker has a token legitimately issued for server A or influences discovery metadata; server B mistakenly accepts it, or the client sends a code/token to an unintended endpoint. The relevant controls are trusted issuer metadata, resource indicators, audience validation, response-issuer binding, URL/redirect rules and SSRF defenses. An attacker need not break a model or signature. A compliant resource rejects the wrong audience even when issuer/signature/expiry are otherwise valid. Application tenancy is a separate check: the correct server may host multiple tenants.

**Test:** same valid token against intended and unintended test endpoints; wrong issuer; absent audience; metadata/callback mismatch in an isolated harness. Do not probe public servers.

### T2 — Confused deputy and inherited upstream consent

An MCP proxy uses one upstream OAuth client for many downstream clients. If prior browser consent is treated as consent for every new downstream client/redirect, a malicious client may exploit the proxy's authority. Bind consent and callback state to the actual downstream client, resource owner, exact registered redirect and upstream context. Keep authoritative routing state server-side or integrity-protected. The protection is an authorization flow property; it is not a model prompt.

**Counterexample to over-building:** a correctly implemented mature OAuth proxy with explicit per-client consent may already solve this fully. A new “agent passport” is not inherently better.

### T3 — Exchanged token gains authority or loses context

The model/client already has some granted authority and requests a downstream token. The [current Keycloak guide](https://www.keycloak.org/securing-apps/token-exchange) says standard V2 scope can request optional scopes; by default exchange may obtain scopes/audiences absent from the subject token. The downscope-assertion-grant-enforcer can restrict this. audience filters, rather than creates, available audience entries. Delegation support is preview and differs from ordinary standard exchange; do not enable preview casually to make a demo fit a diagram.

RFC 8693 section 4.1 says nested act entries record prior actors, while access-control consumers consider top-level claims and the current actor; prior nested actors are informational. A signed actor history is not proof that each hop was narrower, nor that a business constraint propagated. The issuer/exchange/application profile must define and enforce those properties.

**Test:** optional-scope exchange with/without the downscoping policy; compare effective claims and allowed business operations, not only token text. A successful exchange is not itself an attack if the issuer intentionally grants that authority.

### T4 — Revoked request continues in a queue

Attacker or faulty agent retains a valid short-lived token or queued job after the user/operator revokes access. Offline JWT verification may not learn revocation until expiry or a separate deny signal. RFC 7009 acknowledges propagation delay and deployment-dependent related-token revocation. RFC 7662 explicitly warns that cached active introspection can become stale. Keycloak's table distinguishes access-token and refresh-token revocation chains.

Define the contract: revoke future minting, reject new resource calls, stop queued work before commit, or compensate already completed work. These are different operations. Rechecking a task-grant epoch at the business commit can reduce queued-work exposure but introduces dependency/availability costs. A network partition requires a deliberate fail-open/fail-closed decision appropriate to the operation.

### T5 — Bound key signs an unintended request

Attacker steals only a bearer token versus controls code inside the legitimate client. DPoP helps against the former. RFC 9449 section 11.4 discusses untrusted code in the client context; section 11.7 says general body/header integrity is outside its protection. TLS remains essential. An exact approval must be compared with authoritative typed business arguments; do not treat a DPoP proof as an exact refund authorization.

**Counterexample to favored capability design:** a custom signed JSON approval introduces canonicalization/key/replay/storage complexity. An ordinary server-stored approval record with a stable operation ID and transactional validation may be simpler and equally effective within one application.

### T6 — Correct identity, wrong tenant or job

Two callers reach one server or task queue. Server indexes cached credentials/state by tool/session/task ID rather than authenticated issuer/subject plus authorized tenant/job context. Correctly authenticating both callers does not prevent context collision. Current MCP core need not have a stateful session, but application jobs still do. Tasks extension requires permission checks per task request and removes tasks/list; opaque IDs must not become a substitute for the declared access model.

**Test:** valid user A token plus B's resource/task ID; replay across tenant; same subject string from a second issuer; different actor under one user. Inspect business state and data returned, not a successful HTTP handshake alone.

### T7 — Each request is allowed, combined commits exceed authority

Two concurrent requests each see remaining budget 100 and each request 80. Per-call tokens/policies can allow both while committed total becomes 160. Scope/audience checks have worked correctly; the aggregate invariant was never atomically enforced. A serializable transaction or appropriate row-lock/conditional-update design at the authoritative ledger can solve this. [PostgreSQL 18 isolation documentation](https://www.postgresql.org/docs/18/transaction-iso.html) describes anomalies and serialization retries; it does not promise atomicity across unrelated external services.

**Counterexample:** application transaction checks can protect this invariant even with an ordinary scoped service account. The capability token is not the mechanism enforcing the shared budget. Conversely, consuming a one-use grant before a failed external payment can prevent legitimate retries; operation idempotency and recovery must be designed together.

### T8 — Cancel acknowledged, effect still commits

Current Tasks section Task Cancellation explicitly permits eventual-consistency/cooperative semantics: acknowledgement is required, actual stopping is not. A task can complete before cancellation takes effect. Therefore the UI/API must distinguish cancel requested, execution stopped before commit, committed, and compensation required. For a physical system, an independent stop/safety path needs its own engineering evidence; an MCP acknowledgement is not that path.

## Primary empirical and formal evidence

### A current ecosystem measurement with important limits

[A First Measurement Study on Authentication Security in Real-World Remote MCP Servers](https://arxiv.org/html/2605.22333v1), Huijun Zhou, Xiaohan Zhang, Haozhe Zhang, Haoyang Zhang, Mi Zhang and Min Yang; Fudan/Central South affiliations; arXiv:2605.22333v1, 21 May 2026; [DOI](https://doi.org/10.48550/arXiv.2605.22333). Paper license: arXiv non-exclusive distribution.

Reports 7,973 live indexed servers, 40.55% without authentication, and 325 flaws across 119 testable OAuth servers; nine CVEs after disclosure. Public tools without authentication are not automatically vulnerable. The 119 testable OAuth deployments are selected, not every remote server; discovery favors public indexed infrastructure. Much analysis concerns DCR-era deployments before July hardening. No public turnkey code/raw measurement release was established by this inspection. Do not reproduce its active probing on third-party assets under this research's read-only scope.

### An implementation flaw rather than a broken OAuth proof

[JFrog CVE-2025-6514 advisory](https://research.jfrog.com/vulnerabilities/mcp-remote-command-injection-rce-jfsa-2025-001290844/) describes command injection through an untrusted authorization endpoint URL in mcp-remote versions 0.0.5–0.1.15. This is a primary researcher disclosure of unsafe client URL handling, not evidence that OAuth audience binding is mathematically broken. Do not execute historical vulnerable packages; a harmless synthetic URL-handling regression test can check the relevant boundary. The advisory's existence does not mean current versions remain vulnerable.

### Protocol proof scope

[Fett, Küsters and Schmitz, OAuth formal analysis](https://arxiv.org/abs/1601.01229) models authorization/authentication/session integrity in a detailed web model, discovers attacks and proves a fixed form under explicit measures/assumptions. [Their OIDC analysis](https://arxiv.org/abs/1704.08539) similarly formalizes protocol properties and implementation guidelines. These are strong evidence that exact bindings and attacker models matter. They do not prove that a contemporary SDK, an arbitrary issuer configuration, or a multistep business transaction is correct. Paper/code licenses and complete runnable proof-artifact setup were not newly verified in this bounded pass; do not imply turnkey replication.

The [FAPI 2.0 Security Profile](https://openid.net/specs/fapi-security-profile-2_0.html) is a mature high-value API profile; its [final approval](https://openid.net/fapi-2-security-profile-attacker-model-final-specifications-approved/) was announced 19 February 2025. It is a relevant existing comparator to inventing a new security profile, with an explicit attacker model. Applicability and issuer support still need checking for a chosen application.

## Fair architecture comparison

| Architecture | Reasonable strength | Residual weakness or cost | What would make it the right answer |
|---|---|---|---|
| Native gateway/IAM policy + application transaction | Mature discovery, token verification, identity lifecycle and deterministic enforcement; cloud support | Identity mapping, attributes, bypass control, business commit/recovery still configured by application | Existing platform fits the workflow and passes realistic tests with low operating burden |
| Ordinary scoped service account/workload identity + application transaction | Simple autonomous principal; short-lived credentials, mTLS/attestation and ordinary least privilege can be strong | Human request attribution may require additional trusted context; many jobs may share one blast radius | Background authority is truly organizational/service-owned, task context is explicit, and transaction invariants hold |
| Per-user delegated OAuth exchange | Preserves appropriate user context and can target downstream resources | Exchange/consent/revocation semantics vary; preview delegation features may add fragility | User-specific authority is necessary and issuer/client/resource interoperability is verified |
| Bounded task grant atop mature identity | Explicit job/recipient/resource/budget/expiry/revocation contract, narrow execution permission | Extra state, spec authoring, availability, retries and approval friction; a signed token alone does not enforce budget | It prevents a demonstrated residual failure with acceptable utility and less complexity than alternatives |

These can be combined. “Service account” is not synonymous with a permanent superuser key. “Capability” is not synonymous with safe or novel. The application transaction remains common infrastructure for all conditions.

## Publicly reproducible experiment design, no installation or execution

### Question

Which protection comes from transport identity/delegation, which from the application's state machine, and does a bounded task grant add value beyond well-configured ordinary/native controls?

### Proposed minimal stack

- Official MCP TypeScript client/server **2.3.1** at pinned commit above, with compatible adapters and current 2026-07-28 protocol. Node must be an already approved supported runtime. Do not rely on the package's minimum version as a security-support guarantee.
- Keycloak **26.8.1**, standard token exchange V2; explicit issuer/audience/client/optional-scope configuration. No preview delegation required for the minimum experiment. If exact act-chain semantics require preview support, record it as a separate optional condition rather than silently changing baseline.
- Existing supported PostgreSQL, with exact minor version recorded at approved execution time. One local fake business ledger; official [PostgreSQL License](https://www.postgresql.org/about/licence/).
- Existing test runner and official JWT/OIDC verification components. No custom OAuth server, JWT crypto, DPoP implementation or policy language. Optional native-cloud replication is a later separately authorized phase, not a dependency.
- Two local synthetic MCP tool servers: invoices/read and payments/commit. They share a ledger in phase 1 so the experiment can isolate authority versus database transaction guarantees. This is deliberately not proof of a real distributed transaction across external payment providers.

The complete planned fixture can be public: two synthetic tenants, users A/B, service worker W, two tool audiences, invoices with version/currency/amount/recipient and approved aggregate budget. No real credentials, personal data, money or messages.

### Three baseline conditions

**B0:** well-scoped workload/service account and the same business rules/transaction semantics as other conditions. Do not intentionally give it administrator credentials.

**B1:** per-user OAuth access/exchanged tokens with correct issuer/audience and SDK verifier configuration. Same business ledger rules. Run optional-scope/downscoping configurations as explicit subconditions.

**B2:** B1 plus server-stored task grant binding authenticated owner/allowed actor, tenant, invoice version, recipient, integer minor-unit currency amount, aggregate limit, expiry, grant epoch and stable operation ID. Grant approval comes from trusted user/operator context; the model cannot authorize itself. Revalidate and atomically consume/update the grant with the simulated commit. No novel signing format is necessary.

An optional **Bnative** maps the same fixtures/invariants to an approved native policy service. Without executing it, native equivalence remains untested; don't fabricate a cloud result from local conditions.

### Deterministic schedules and expected observations

| Case | Schedule | Oracle |
|---|---|---|
| Audience | Send a correctly signed A-resource token to B; repeat with expectedResource configured/unconfigured and with verifier audience validation | Which exact layer rejects; no B data/effects on rejected paths |
| Exchange | Request an optional downstream scope using standard V2, then apply downscoping policy and repeat | Issued claims and actual allowed endpoint operations; distinguish intentional policy from escalation |
| Owner/tenant | Authenticate A and request B's invoice/task; same sub from another issuer | No returned B content or committed B effect |
| Approval staleness | Approve invoice version 1, alter recipient/version to 2, then commit | Stale version rejected or explicitly reapproved; record whether B0's normal state check already suffices |
| Concurrent budget | Two requests for 80 against remaining budget 100, synchronized after reads | Total committed <=100; record transaction isolation/retries rather than attributing result to OAuth |
| Duplicate outcome | Commit succeeds, response dropped, same operation retried | One committed effect and stable/recoverable result; grant not lost before a failed effect |
| Revocation | Queue action, revoke at t1, delay execution to t2 | Measure whether execution rechecks authority and actual last accepted/committed time; do not infer from revoke HTTP200 |
| Introspection cache | Warm active cache, revoke token, repeat before/after cache TTL | Measured stale-acceptance window, availability and lookup cost |
| Cancel | Queue work with controlled pause; cancel/ack; allow worker to resume | Cancel requested versus stopped/committed are separately observable; app stop barrier tested independently |
| Client compromise | Replay token without key versus run untrusted action in the authorized client context | DPoP key-possession protection differentiated from authorized-client misuse; no general payload-integrity claim |

The DPoP condition should use an already approved conformant library/issuer feature; if unavailable, keep it as a specification test case, not a hand-rolled implementation. For all cases retain event times, token metadata without secrets, actual issuer/resource/policy configuration and committed ledger diffs. Provider/model behavior can be replayed deterministically: no LLM calls are needed to demonstrate these contracts.

### Metrics and kill criteria

- Separate authentication failures, protocol-policy rejections, application-policy rejections, transaction conflicts, committed unauthorized effects, benign successes and unrecoverable legitimate operations.
- For each schedule, at least 100 deterministic repetitions with randomized order/delays and explicit seed. These are engineering checks, not an independent real-world risk sample.
- Measure revocation and cancellation **at the resource/commit**, not only at issuer/queue acknowledgement. Report p50/p95/max window and the configured TTL/cache/queue conditions.
- Report p95 added latency, external lookups, state writes, lines of custom adapter, setup/review time, retry rate, false rejection and recovery effort. No measured numbers exist yet.
- Seed a known missing audience check, tenant check and non-atomic budget check. The suite must detect all three through the intended real code path before a green result is trusted.
- **Kill the bounded grant layer** if B0/B1 plus the ordinary application ledger already satisfy every required invariant with lower operational complexity, or its benefit disappears after correct native/issuer setup.
- **Reject a narrow-token claim** if effective issued scope/action is broader than the task, even when JWT syntax/verification is valid. The broader scope may be legitimate issuer policy; the task architecture then needs a narrower configured contract.
- **Reject an immediate-stop claim** if any work commits after the specified stop barrier; distinguish a failure of the application barrier from protocol-compliant cooperative cancellation.
- **Reject a whole-system guarantee** based solely on a protocol proof, passing helper unit test, a valid actor chain or a finite zero-effect test suite.

### Original contribution paths

1. A versioned conformance matrix that explicitly separates issuer/client/resource/helper/adapter responsibilities; include a regression for optional expectedResource and package-version propagation.
2. A small task-lifecycle corpus joining revocation, cancellation, queued execution and committed effects. Current high-level agent benchmarks often do not expose this authority timeline.
3. A fair comparison showing when ordinary workload identity plus a transaction is sufficient; negative results and removed layers are valuable.
4. Behavioral policy review cases for optional-scope exchange and stale business state, with a programmatic effect oracle and complete reproducibility manifests. Do not publish a vulnerability exploit before following the project's security process.

These are proposed contributions, not claims that the questions have never been studied. Search the relevant issue trackers/papers before claiming novelty.

## Code, licenses and public research channels

Public GitHub metadata was inspected via the installed Agent-Reach gh route with read-only network escalation. No repositories were cloned.

- **MCP TypeScript SDK:** [repo](https://github.com/modelcontextprotocol/typescript-sdk), pinned v2.3.1 license inspected. It is in an **MIT-to-Apache-2.0 transition**: new code/spec contributions Apache-2.0, prior unconsented contributions MIT, non-spec docs CC BY 4.0. GitHub metadata says NOASSERTION. Do not blanket-label all code MIT or Apache. [Issues](https://github.com/modelcontextprotocol/typescript-sdk/issues), SECURITY.md and CONTRIBUTING.md are public routes; use security reporting for vulnerabilities.
- **MCP Tasks extension:** [repo](https://github.com/modelcontextprotocol/ext-tasks), metadata Apache-2.0. Extension spec/issue discussions are the relevant technical channel; no issue/comment sent.
- **Keycloak:** [repo](https://github.com/keycloak/keycloak), Apache-2.0 verified metadata; official token-exchange guide above. Public issues/contribution docs and project community are routes. Protocol fidelity must be tied to the tested feature/version; legacy, standard and preview modes are different.
- **SPIRE:** [repo](https://github.com/spiffe/spire), Apache-2.0 verified metadata. [SPIFFE specifications](https://spiffe.io/docs/latest/spiffe-specs/) and repository contribution/community links are public routes. Workload attestation expertise is distinct from user/task authorization.
- **IETF OAuth WG:** [official WG page](https://datatracker.ietf.org/wg/oauth/about/) links public mailing-list archive and Zulip. RFC authors include Brian Campbell, John Bradley, Michael Jones, Torsten Lodderstedt and Daniel Fett across relevant documents. Institutional/public WG channels are more appropriate than treating authors' addresses as personal access.
- **Protocol security research:** [University of Stuttgart Institute of Information Security](https://www.sec.uni-stuttgart.de/), Ralf Küsters and coauthor network; original OAuth/OIDC papers above. Relevant for exact web attacker models and binding failures. No hiring/admission status inferred.
- **Remote MCP authentication measurement:** Fudan/Central South paper authors above; paper's public institutional author information is the professional starting point. A complete public detector/measurement artifact was not established, so do not imply access or permission to rescan the measured services.
- **JFrog Security Research:** primary advisory above and designated vendor security/contact routes. Historical client command-injection research is relevant to the discovery→local-execution seam; it does not authorize running the disclosed PoC.

## Career interpretation and remaining uncertainty

This work rewards protocol reading, version/configuration literacy, identity modeling, state-machine/transaction engineering and evidence-based failure diagnosis. The most transferable result is knowing which layer owns each invariant. Original research or leadership requires a clear contribution and real operational ownership, not merely implementing a fashionable token format.

No public experiment was implemented/run, no current deployed vendor was attacked, and no universal independent conformance result was obtained. Live Keycloak documentation may evolve beyond the pinned release; verify exact supported behavior before a later test. Native-platform integration, third-party effects and real user utility need separate approved experiments. Technical gaps remain evidence for engineering work; they remain insufficient evidence for headcount, salaries or a new company.
