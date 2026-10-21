# Security research, employer and contribution directory

Verified 19 October 2026. Directory only: no outreach, applications, issue creation, subscriptions, code checkout, installation, paid calls or tenant access. Public professional channels are supplied instead of private contact information. A listed organization is not a recommendation to buy from it, a claim of a suitable vacancy, or a promise of access to its staff.

This extends security.md and security-round2.md. Institutions, affiliations and product surfaces can change; paper affiliation describes publication context, while a current professional profile should determine present employment. In particular ETH's current lab page lists Edoardo Debenedetti under alumni after his July 2026 thesis defense; do not label him a current ETH student based on old papers.

## Institution/team/author map by technical branch

| Branch | Institution/team and why it matters | Public professional route | Entry route and barriers |
|---|---|---|---|
| Adversarial evaluation, task oracles | [ETH Secure and Private AI Lab](https://spylab.ai/), led by Florian Tramèr; AgentDojo authors include Edoardo Debenedetti, Jie Zhang, Mislav Balunović, Luca Beurer-Kellner and Marc Fischer. Learn experimental design and security/utility distinctions. | Lab-linked researcher profiles; [AgentDojo issues](https://github.com/ethz-spylab/agentdojo/issues). [Results contribution instructions](https://agentdojo.spylab.ai/results/) explicitly invite a fork/PR with an implemented attack/defense/model and results. No PR was opened. | A reproducible task-suite or evaluator bug fix is a concrete contribution. Academic research routes require credible research fit and role-specific admission/hiring criteria; code contribution does not imply lab admission. Lab results page explicitly warns it is not a fair cross-model leaderboard. |
| Capability/data-flow containment | Google Research/Google DeepMind/ETH authors of [CaMeL](https://arxiv.org/abs/2503.18813v2), including Edoardo Debenedetti and coauthors. Relevant for separating untrusted parsing from privileged planning. | [Official code issues](https://github.com/google-research/camel-prompt-injection/issues); paper author list; [DeepMind careers](https://deepmind.google/careers/). | Reproduce one bounded task and a documented limitation; contribution route is research-artifact discussion, not production support. Research scientist and research engineer paths differ. API access, changing provider models and strong systems/security skills are practical barriers. |
| Verifiable authorization | [Amazon Science automated reasoning](https://www.amazon.science/research-areas/automated-reasoning), AWS Cedar/AgentCore teams. Cedar paper authors include Joseph W. Cutler, Kesha Hietala, Michael Hicks, Emina Torlak and colleagues. | [Cedar issues](https://github.com/cedar-policy/cedar/issues); [Cedar docs](https://docs.cedarpolicy.com/); [Amazon Science careers](https://www.amazon.science/careers). | A small policy-validation, test or diagnostic improvement is a better entry artifact than a new interpreter. Rust/systems and authorization semantics are useful; formal-methods research roles may require substantially deeper PL/verification background than product integration roles. The careers portal has internships/postdocs/full-time routes; eligibility is position-specific. |
| Independent agent red teaming | [Gray Swan](https://www.grayswan.ai/careers), competition paper authors Mateusz Dziemian, Maxwell Lin, Xiaohan Fu, Micha Nowak, Nick Winter, Andy Zou, Matt Fredrikson and Zico Kolter with lab/government collaborators. | [Public evaluation-harness issues](https://github.com/GraySwanAI/ipi_arena_os/issues); official careers/contact links; public Arena link from careers page. Participation terms and scope must be read before any attack attempt. | Build a reproducible evaluation-quality contribution or analyze a disclosed benchmark limitation. A public competition is not authorization to attack real services. Full attack datasets are restricted and paid evaluation can multiply API calls. Official careers page mentions flexible arrangements/visa sponsorship, but no specific role/India eligibility is assumed here. |
| Agent identity/standards/implementation | [NIST NCCoE Software and AI Agent Identity and Authorization project](https://www.nccoe.nist.gov/projects/software-and-ai-agent-identity-and-authorization), alongside NIST CAISI standards/evaluation work. | Project's public Contact Us/rolling-feedback route and [resource hub](https://pages.nist.gov/nccoe-ai-identity/); [NIST careers](https://www.nist.gov/careers). | Public technical feedback is a standards participation route, distinct from employment. Current hub reports more than 600 responses and iterative implementation-oriented work toward an SP-1800 practice guide. Feedback is not a customer commitment; government employment/internship citizenship and eligibility constraints must be checked per program. Do not reuse the expired April concept-paper comment deadline as the only route. |
| Effective permissions, identity attack paths | [Compass Security research](https://blog.compass-security.com/2026/06/entra-agent-id-from-a-security-perspective/), Christian Feuchter; [EntraFalcon](https://github.com/CompassSecurity/EntraFalcon). Relevant for mapping inheritance/ownership to actual authority. | Public research byline/profile and [EntraFalcon issues](https://github.com/CompassSecurity/EntraFalcon/issues); [official jobs page](https://www.compass-security.com/de/firma/jobs). | Begin with offline synthetic report/model tests; running the tool requires explicitly authorized tenant read access. Entra/Graph/PowerShell and ordinary IAM security are more important than an AI-specific label. Source careers route is multilingual; exact vacancy, language, location and employment eligibility remain unverified. |
| Platform-role security, machine identities | [Silverfort research disclosure](https://www.silverfort.com/blog/agent-id-administrator-scope-overreach-service-principal-takeover-in-entra-id/), Noa Ariel. Relevant for testing the actual reach of newly introduced administrative roles. | Article's public professional byline and [official careers](https://www.silverfort.com/careers/). | Reproduce a disclosed mechanism only in an approved test environment; the cited role bug was fixed in April 2026 and must not be described as currently exploitable. Identity-security engineering/research requires controlled environments, responsible disclosure and cloud/IAM depth. No role-specific eligibility was inferred. |
| Native policy assistants, agent platform/IAM engineering | Microsoft Entra and [Microsoft Research](https://www.microsoft.com/en-us/research/careers/open-positions/); CA-agent RCT authors James Bono, Beibei Cheng and Joaquin Lozano. Relevant to native tools that automate policy administration. | [Microsoft India careers](https://careers.microsoft.com/v2/global/en/locations/india.html), research careers, official product documentation/feedback links. | Directory page currently exposes security-research work requiring demonstrated security/telemetry/scripting experience; senior agentic-systems research has research-track requirements. This is a route to inspect, not a role-count or guarantee that an AI engineer is qualified. No application was made. |
| Intent-to-policy synthesis | [Stevens Institute of Technology, William Eiers](https://www.stevens.edu/profile/weiers); AutoCedar authors Adarsh Vatsa, Sachi Shome, Yingming Zhou and William Eiers. Relevant for reviewed behavior specifications and verifier-guided policy synthesis. | Official faculty profile and [paper-linked repository](https://github.com/neselab/cedar-synthesis-engine); use official academic contact channel linked by profile if outreach is later authorized. | Small replication/counterexample with explicit intent boundaries is useful evidence. Academic collaboration/admission is separate from repository activity. Solver/PL expertise and reviewable requirements are barriers. Code license and exact environment have not yet been checked for this repository; do not redistribute or execute it based on a paper's availability. |

## Paper and artifact registry

ArXiv DOIs identify the paper lineage; use the listed version for precise claims. Paper, code and dataset licenses are different. A paper's CC license does not automatically license its benchmark data or software. No original experiment was reproduced in this research; “available” and “verified metadata” mean read-only inspection.

### P1 — AgentDojo

- Paper: [arXiv:2406.13352v3](https://arxiv.org/abs/2406.13352v3), 24 November 2024; [DOI](https://doi.org/10.48550/arXiv.2406.13352). NeurIPS 2024 Datasets and Benchmarks; current arXiv note mentions a Llama implementation bug fix and travel-suite update.
- Paper license: arXiv non-exclusive distribution license, inspected through its license link. Code: [ethz-spylab/agentdojo](https://github.com/ethz-spylab/agentdojo), **MIT**, public GitHub metadata verified.
- Data: bundled task suites/security cases; [public result traces](https://agentdojo.spylab.ai/results/). Check individual artifact terms before reuse.
- Replication requirements: Python/package environment, provider credentials/model access; optional detector dependencies; API under development. Current models may differ from historical version IDs. A tiny chosen suite/case is appropriate for a first approved smoke run; a full model matrix is not a free laptop experiment.
- Best contribution: add an independently justified task oracle or test a defense with benign utility and attack outcomes both reported.

### P2 — CaMeL

- Paper: [arXiv:2503.18813v2](https://arxiv.org/abs/2503.18813v2), 24 June 2025; [DOI](https://doi.org/10.48550/arXiv.2503.18813). **Paper CC BY 4.0**.
- Code: [google-research/camel-prompt-injection](https://github.com/google-research/camel-prompt-injection), **Apache-2.0**, verified metadata.
- Replication requirements: README expects uv plus provider API credentials, and warns that uv run installs dependencies. Thus do not run it under the current no-install boundary. AgentDojo environments, exact model/provider versions and policy settings affect results.
- Important version correction: v2 abstract reports **77% utility versus 84% undefended** under its evaluated setup; older v1/search snippets reported 67%. Do not mix versions or interpret utility as unconditional security.
- Best contribution: reproduce one documented policy/context limitation and quantify the utility cost; do not copy its interpreter into production without reviewing the larger trusted base.

### P3 — Cedar

- Paper: [arXiv:2403.04651v2](https://arxiv.org/abs/2403.04651v2), 8 March 2024; [DOI](https://doi.org/10.48550/arXiv.2403.04651). **Paper CC BY 4.0**.
- Code: [cedar-policy/cedar](https://github.com/cedar-policy/cedar), **Apache-2.0**, verified metadata. [Authorization docs](https://docs.cedarpolicy.com/auth/authorization.html), [security scope](https://docs.cedarpolicy.com/other/security.html).
- Replication requirements: Rust development toolchain for engine work; formal-model/proof work adds Lean/tool versions and deeper expertise. SDK/policy-only experiments have a lower barrier if an approved runtime already exists. No toolchain was installed or compilation run here.
- Best contribution: a minimal policy counterexample, validation diagnostic, test or documentation improvement. Preserve semantics rather than writing a new policy engine.

### P4 — Concealment-aware injection competition

- Paper: [arXiv:2603.15714v1](https://arxiv.org/abs/2603.15714v1), 16 March 2026; [DOI](https://doi.org/10.48550/arXiv.2603.15714). **Paper CC BY 4.0**.
- Code: canonical [GraySwanAI/ipi_arena_os](https://github.com/GraySwanAI/ipi_arena_os), **MIT**, verified metadata; old grayswansecurity URL redirects to this owner.
- Data: [paper-linked public partial dataset](https://huggingface.co/datasets/sureheremarv/ipi_arena_attacks). The full model-specific attack corpus is not public; partial release cannot reproduce all claims. Its dataset license was not separately checked here.
- Replication requirements: target and judge API access; README tool simulation can require an extra model call per tool interaction. Computer-use mode adds browser/Playwright setup. Previews can avoid API calls after an approved environment exists. No package or browser installation occurred.
- Best contribution: inspect scoring/denominator consistency and add non-sensitive deterministic checks; do not infer full-corpus comparability from a partial release.

### P5 — Native identity-agent RCT

- Paper: [arXiv:2511.13865v1](https://arxiv.org/html/2511.13865v1), 17 November 2025; [DOI](https://doi.org/10.48550/arXiv.2511.13865). **Paper CC BY 4.0**.
- Authors: James Bono, Beibei Cheng and Joaquin Lozano, Microsoft affiliation in paper.
- Code/data: no complete public participant-level raw dataset or turnkey tenant replica was established by this inspection. Appendices describe grading and time comparisons. Do not claim a turnkey independent reproduction.
- Replication requirements: approved Entra test environment and product eligibility, synthetic users/policies, qualified participants, pre-specified grading, consent/data handling and a study budget. This is higher effort than a one-user product demo.
- Best extension: a small within-engineer native-vs-manual task comparison is exploratory; it cannot replicate the causal population result.

### P6 — Independent Progent extension

- Paper: [arXiv:2606.26479v1](https://arxiv.org/html/2606.26479v1), 25 June 2026; [DOI](https://doi.org/10.48550/arXiv.2606.26479). LaunchSafe Research authors; paper identifies preliminary/non-peer-reviewed status.
- Paper license: CC BY 4.0 in HTML metadata. Code/raw-log public release completeness and its license were not verified here; paper describes scripts and retained logs.
- Replication requirements in reported setup: AgentDojo, vLLM, Progent, Qwen2.5-7B and **one H200**, three repeats on a small task subsample. This is not an ordinary-laptop replication. A smaller local model run would be a new setting requiring fresh utility checks.
- Best extension: authorized-tool-only/adaptive attacks, stronger agents, broader tasks, and disclosed errors. Do not report the paper's aggregate effect as your measurement.

### P7 — AutoCedar

- Paper: [arXiv:2607.03656v1](https://arxiv.org/html/2607.03656v1), 4 July 2026; [DOI](https://doi.org/10.48550/arXiv.2607.03656). **Paper arXiv non-exclusive license**.
- Artifact: [neselab/cedar-synthesis-engine](https://github.com/neselab/cedar-synthesis-engine), linked by paper. Code license/environment not inspected; explicit gap.
- Data: paper introduces 221-task CedarBench and three requirements-corpus case studies. Benchmark authors and framework authors overlap; independent held-out review matters.
- Replication requirements: policy-generation model, Cedar checker/symbolic compiler/solver tooling and reviewed intent boundaries. Exact setup/spend needs preflight before any approved replication.
- Best extension: test incorrect or incomplete approved intent, and count human-review/repair hours as well as convergence. Formal claims remain relative to the approved target.

### P8 — APort payment authorization

- Paper: [arXiv:2609.22076v1](https://arxiv.org/html/2609.22076v1), 18 September 2026; [DOI](https://doi.org/10.48550/arXiv.2609.22076). Vendor author Uchi Uchibeke, APort Technologies.
- Paper: CC BY 4.0 in HTML metadata. Data: [vault-benchmark-v1](https://huggingface.co/datasets/aporthq/vault-benchmark-v1), paper says CC BY 4.0; dataset card/license not independently inspected here.
- Replication: paper says released outcome rows/analysis can reproduce principal counts, but harness, judge prompts and keys are withheld; several measures require private infrastructure. Full replay therefore differs from reanalyzing public rows. Parquet analysis needs an appropriate reader; do not install one without approval.
- Best extension: independently audit denominators and matched cases first. A request is not an executed transfer, and an allowed transfer is not proof of legitimate task intent.

## Verified public code snapshots

Metadata and commit IDs were read through the installed Agent-Reach GitHub CLI route, using public GitHub APIs. Initial sandbox network access failed; read-only network escalation succeeded. No source repository was cloned or downloaded. All five repositories reported not archived. A main-branch commit is a reproducibility reference, not a validated release or a compatibility guarantee with the paper.

| Repository | Code license | Main commit inspected |
|---|---|---|
| [AgentDojo](https://github.com/ethz-spylab/agentdojo/tree/089ed468cf3ed0322acc66b0211f26d9d90dbf60) | MIT | 089ed468cf3ed0322acc66b0211f26d9d90dbf60 |
| [CaMeL](https://github.com/google-research/camel-prompt-injection/tree/f083b6b396399d3b3c7f2ddaf613a5945eaf32d8) | Apache-2.0 | f083b6b396399d3b3c7f2ddaf613a5945eaf32d8 |
| [Cedar](https://github.com/cedar-policy/cedar/tree/bf15eb3718a291834c403f104aa56d064a72504e) | Apache-2.0 | bf15eb3718a291834c403f104aa56d064a72504e |
| [IPI Arena](https://github.com/GraySwanAI/ipi_arena_os/tree/5e2e285910d581c97767195f1d113ef323f9ab07) | MIT | 5e2e285910d581c97767195f1d113ef323f9ab07 |
| [EntraFalcon](https://github.com/CompassSecurity/EntraFalcon/tree/7c6e584379669ee646e4f481266797d91adb9e67) | MIT | 7c6e584379669ee646e4f481266797d91adb9e67 |

EntraFalcon's README advertises PowerShell 5.1/7 and different authentication modes; an authorized Graph/optionally ARM connection is still required. The claim that one mode needs no additional modules/consent must not be generalized to every mode, nor treated as permission to enumerate a real tenant.

## Practical relationship-building without premature outreach

Build a precise, locally reproducible artifact against one public project: a bug, an improved oracle, a measurement correction or a documented negative result. Read contribution/security policy first. Keep questions tied to evidence and use the project's designated channel. For a security vulnerability, use the responsible disclosure channel rather than a public exploit issue.

A person being a paper author, maintainer or public speaker does not make them an adviser or a hiring sponsor. No email/DM/application/comment has been sent. If outreach is later requested, review the concrete message and recipient against the user's authorization; do not silently convert this directory into contact activity.

## Remaining verification gaps

Specific vacancy fit, compensation, location/visa eligibility, acceptance of unsolicited academic inquiries, dataset licenses marked unverified, code licenses marked unverified, whole-experiment cost, and exact dependency compatibility remain unchecked. These are concrete gaps for the next stage rather than reasons to imply all listed paths are equally accessible.
