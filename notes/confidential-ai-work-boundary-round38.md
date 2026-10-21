# Confidential AI: attestation, authority and readiness boundary — round38

Native CPU/GPU confidential computing can protect data in use from an untrusted infrastructure operator. Its verifier, reference-value and key-release controls are substantial existing infrastructure. A device quote alone still does not establish which AI artifact served a request,who authorized it,what an approved application logs or whether its output is correct. That chain must be evidenced layer by layer; it is not a permanent custom-integration or human-review moat.

## Census and bounded sources

The saved security baseline/protocol3, local-inference15/independent17, compute3 directory and source-index9074 came first. Root clarified its27 shorthand; there was no missing source/skill block. These notes already separate local/offline execution from privacy,workload identity from user/task authority,artifact signatures from semantics,and device specifications from whole-workload measurement. The index's attestation matches concern supply-chain provenance,with unrelatedteetone false positives. No previous CPU/GPUquote protocol audit was found in this bounded set;that is not proof of global absence.

Exactly **three** new primary text surfaces were read and stopped. Their structured metadata/locators are in [source receipts](<confidential-ai-work-boundary-round38-source-receipts.json>). No code,keys,quotes,models,data,traffic,accounts,hardware,containers or images were acquired or run. The two `/latest/`doc URLs are moving observations on20 October UTC,not immutable19 October snapshots or installed releases.

[1: NVIDIA VM trust model](https://docs.nvidia.com/enterprise-reference-architectures/deploying-proprietary-models-confidential-compute-self-hosted-vms/latest/trust-and-threat-model.html),updated 4 June 2026,assigns approved guest/model policy to the provider,callers/outputs/logs to the enterprise owner,and key-release/reference policy to its authority. It excludes malicious guest code, vulnerable inference software, payload logging, compromised assurance administrators, side channels/physical attack and DoS. Those exclusions matter to the end user's claim;they do not erase the protection against ordinary privileged infrastructure memory access.

[2: NVIDIA CoCo attestation](https://docs.nvidia.com/datacenter/cloud-native/confidential-containers/latest/attestation.html) describes Kata/Trustee composite CPU/GPU evidence,reference values and policy-based release. **Kata Agent API policy and KBS release policy are distinct.** Its quickstart explicitly has **no TEE, no real hardware evidence and no secret release to a workload**:sample fake evidence is denied,and that denial is the expected connectivity result. The document names Trustee v0.21.0 but warns its compose recipe pulls mutable latest images;its supplied commit/digest alternatives were not fetched. A tagged recipe or reachable backend is not a production attestation deployment.

[3: NVIDIA GPU Confidential Computing Demystified,2507.02770v1,3 July 2025](https://arxiv.org/html/2507.02770v1) is an IBM Research/Ohio State primary study using instrumentation and component experiments,with some opaque mechanisms explicitly speculative. Its single-H100 CVM configurations and **4,394 CPU–GSP transfers (453 reads/3,941 writes)** during one lifecycle do not measure LLM inference throughput or a user-population privacy rate. It reports metadata/timing visibility and preserves signature checks that turn some tampering into out-of-scope DoS. No universal plaintext/model extraction or current-fleet failure is inferred.

## The cross-layer contract

| Layer | Native protection/control | What still needs its own evidence |
|---|---|---|
| CPU/GPU state | Isolation,secure boot,signed device/firmware/configuration evidence | Actual supported mode/build,trust anchors,reference values and accepted TCB state |
| Workload and release | Composite guest evidence,Kata Agent policy,Trustee default-deny/key release | Exact guest/bootstrap,allowed API surface,resource policy and freshness/collateral chain |
| AI artifact | An enforced measured loader/artifact-release policy can bind an approved model | Actual weight digest,version/signer/lineage and load-time enforcement;GPU firmware identity alone is insufficient |
| Client/request | Standard authenticated endpoint and application permissions can be integrated | Evidence-to-endpoint binding,current caller/tenant/purpose and business-action authorization |
| Output/application | Measured code can enforce ordinary logging,retention,egress and task rules | Whether this trusted code/model obeys those rules and produces permitted,correct outputs |

This is not a claim attestation can never bind an application or model. A properly measured/enforced workload and release policy may do so. The selected material does not supply a real model-digest/loaded-instance/channel receipt. A “Model Certificate” in a **GPU device** certificate chain must not be mistaken for evidence of an ML model's weights or training lineage. Nor does an approved,correctly measured program become bug-free or privacy-preserving merely because it runs inside the protected boundary.

The paper describes certificate revocation checks and reference-integrity-manifest comparison before GPU readiness. Secure boot/signatures alone are not a proof that a component has no vulnerability or has not been revoked. Exact nonce/channel binding,freshness/cache windows,minimum accepted TCB/update/rollback policy and elapsed revocation behavior were not recovered or measured. Their absence from these selected pages is not proof native implementations lack them. No live service or currentfix/CVE status was checked.

Threat models also remain source-specific. The reference architecture broadly excludes physical attack;the paper permits infrastructure/PCIe access while excluding advanced GPU-package probing. Its2025single-GPU/TrustedIO statements do not describe all2026 Hopper/Blackwell configurations. Counterevidence must respect those differences rather than declaring every implementation compromised.

## Measurement, access and a missing serious route

The paper's host had eight H100s installed but passed only **one** to each studied64 GB guest. Two guest/driver/CUDA configurations are specified;they are study settings,not current minimum recommendations or patch status. Transfer-size/timing observations concern one component/lifecycle,not full training/serving latency,cold start,attestation cost,heap,energy or an all-attempt overhead percentage. These three sources do not establish those production denominators.

Native verification and release automation should be the baseline. A custom verifier/crypto/secret broker must not be invented just to create portfolio complexity. A residual may be a precise artifact-policy binding,reference/patch rollout mismatch or an operational evidence join,but actual owner need,funded responsibility and incremental value remain unmeasured. Tools can automate this work too.

No exact existing **serious TEE project/cap** was established. The authority/local-inference/compute notes provide related reasoning,not transferable TEE hardware proof or hours. This branch is therefore **discovery-only/missing a serious launch contract**,with no new canonical ID,hours,exercise,keys or learner assessment.

A CPU-only source audit can record which party vouches for device,guest,model,resource,caller and output,with source/asserted/unknown/unrun states. It cannot create a valid signed quote. Even a later approved fake-evidence/backend demo would establish only its local connectivity/denial contract. Before any real TEE activation,a selected budget must count prerequisite study,host/firmware/guest/driver setup,verifier/collateral operations,model loading,validation/review,patch/revocation handling,recovery and reporting—not just inference. No such estimate is allocated here.

Actual continuation would need supported confidential CPU/GPU,modes/firmware/passthrough privileges,authentic evidence and policy/reference pins,model/software/data rights,endpoint binding,independent useful-allowed and invalid/stale/revoked cases,and complete cost/resource/support ceilings. Current tasks authorize none of the install/account/compute/traffic steps. Stop or remain source-only when those gates are missing;stop a redundant custom layer when native policy already meets the legitimate contract. Expected denial in a sample setup is not evidence that useful real requests also succeed.

## Teams, rights and proof limits

The paper authors are Zhongshu Gu, Enriquillo Valdez, Salman Ahmed, Julian James Stephen, Michael Le, Hani Jamjoom, Shixuan Zhao and Zhiqiang Lin,with **paper-time** IBM Research/Ohio State affiliations. The [paper](https://arxiv.org/html/2507.02770v1) and official NVIDIA docs are public professional discovery routes,not person contact endpoints or current employment/funding checks. The docs reference [Trustee](https://github.com/confidential-containers/trustee),and the paper references [nvTrust](https://github.com/NVIDIA/nvtrust);those repositories/contribution/AI-use policies were not opened. No email or address is retained here; no contact, grant application or submission occurred.

Article CC BY4.0 does not grant code,model, data,firmware or device use. Documented release/commit/digest names are not fetched artifact identity or verified dependency licences. The research platform's privileged Linux/VM/driver/protocol work differs from a laptop source audit. No current role,graduate-degree requirement or waiver,India/UK access,workrights,grant eligibility or free GPU entitlement is established by a paper affiliation or project URL.

All six local input hashes,including held source-index9074,remain exact;no index or shared artifact was edited. Source architecture claims,observed component results,explicit speculation and this report's missing-route judgments remain separate. No universal privacy,legal/compliance certification,security/physical proof,paid role count,wage premium,human moat or final UI/conclusion acceptance follows.
