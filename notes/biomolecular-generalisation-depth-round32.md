# Boltz-2 affinity: exactly which generalisation and prospective outcome?

This bounded primary-methods pass closes a gap in the saved molecular notes: they covered AlphaFold 3, BindCraft, AlphaGenome and atomistic materials, but not an affinity model's assay/split/generalisation contract. The question is whether Boltz-2's reported results establish new-target, new-chemistry or prospective experimental affinity prediction. They establish meaningful scoped computational results; those stronger claims need separate evidence.

The inspected paper is Saro Passaro, Gabriele Corso, Jeremy Wohlwend and colleagues, **“Boltz-2: Towards Accurate and Efficient Binding Affinity Prediction,” version 1, posted 18 June 2025**, DOI [10.1101/2025.06.14.659707](https://doi.org/10.1101/2025.06.14.659707). The readable [author-preprint mirror](https://pmc.ncbi.nlm.nih.gov/articles/PMC12262699/) explicitly identifies v1 and its preprint status. The DOI's June 14 identifier is not its posting date. No claim is made that v1 is the latest paper or that no later journal publication exists.

## Positive evidence and its units

The main text reports:

| Evaluation | Reported observation | Exact proof boundary |
|---|---|---|
| FEP+ / OpenFE | 876 measurements; training excludes proteins at least 90% sequence-identical to benchmark proteins; four-target subset mean Pearson 0.66 | Retrospective affinity ranking under that exclusion; not remote-family/scaffold/time holdout |
| CASP16 | 140 protein–ligand pairs, two targets | Boltz-2 was evaluated retrospectively; the original competition's blind status is not a prospective Boltz-2 entry |
| Internal Recursion assays | Eight blinded assays; three exceed Pearson 0.55, five have limited performance | A useful harder-setting countercase within the authors' own paper; public replication material not established |
| TYK2 prospective selection | Candidates checked with one repeat of Boltz-ABFE, without experimental measurements | Prospective computational selection and physics rescoring; not a wet-lab hit-rate trial |

These are author-reported results, not independent reruns. See [paper §5.3–5.4](https://pmc.ncbi.nlm.nih.gov/articles/PMC12262699/). The paper compares serious ML, docking and physics baselines; it does not merely compare against a weak random method. Its four-target subset was selected for common comparator availability.

## What generalises, and what remains unresolved

The protein-identity exclusion is a real positive control. It should not be erased by a generic “all benchmarks leak” criticism. A 90% threshold nevertheless defines a particular similarity rule; it cannot alone establish transfer to a remote protein family, a changed pocket state or a new chemical scaffold. Nor does the structural PDB cutoff of 1 June 2023 establish an availability-time cutoff for every affinity label, distilled feature or later model choice. These are different data paths.

The authors explicitly analyse compound similarity in Appendix D.2.1 and discuss generated-compound novelty elsewhere. That appendix was not opened within this pass's endpoint limit. Exact scaffold/similarity bins, overlap results, input preparation, repeated-measurement handling, censor rules and label availability dates therefore remain **unresolved**, not absent. No accusation of demonstrated contamination follows. A future overlap report would need the actual paper-matched training/test manifest and compound/protein identifiers; a benchmark title or target name is not enough.

The meaningful statistical units also differ. A protein–ligand pair can have multiple assay measurements. Within-series analogue ranking is not the same task as ranking compounds across unrelated assays or predicting success on a new target. Compound-count-weighted aggregate performance can give a large assay more influence than a small one; it does not estimate the fraction of unseen targets that work. The read main text describes bootstrap variability, but does not resolve the resampling unit for this audit. An assay/target-grouped report would answer a different uncertainty question from resampling individual compound rows.

## Affinity numbers, labels and calibration

The paper trains with heterogeneous Ki, Kd and concentration-response quantities, normalised into log micromolar units, and emphasises intra-assay differences. It describes the value head as ranking-oriented and only approximately IC50-like. The [official README](https://github.com/jwohlwend/boltz) gives distinct binary-binder and affinity-value outputs, intended for different settings. These are not interchangeable endpoints.

Unit normalisation cannot turn Kd into IC50 or remove substrate, assay and condition effects. Within-assay comparisons can still be valuable precisely because some shared offsets cancel. Conversely, an average-precision/enrichment gain or Pearson correlation does not by itself establish calibrated probabilities, useful absolute prediction intervals, or a correct cross-assay physical constant. The appropriate evaluation depends on the intended decision and the assay's base rate, measurement range and uncertainty.

The binary training mix includes synthetic shuffled-binder negatives with similarity safeguards. That is a disclosed attempt to reduce shortcut/false-negative problems, not a collection of experimentally established nonbinders for every possible target. A reported binder probability needs independent deployment-like calibration evidence before being treated as a literal chance in a changed screen.

The tiny metadata companion runs four **fictional, exposed, same-author** unit examples only. For example, 100 nM normalises to −1 in log10 micromolar units for either a Kd or IC50 record; the quantity and assay remain different. A “less than” measurement remains a bound, and a probability has no concentration-unit conversion. These checks exercise arithmetic and an authored metadata policy; they test neither Boltz code nor real assay truth.

## “Prospective” and the physical comparator

The TYK2 result adds a distinct physics-based reference after candidate selection, which is stronger than reporting the generator's reward alone. It still uses computational rescoring. The paper itself chooses a well-performing target and warns the outcome may be optimistic. A favourable selected target and a single simulation repeat cannot estimate broad experimental hit rate or general new-target performance. Shared pose/preparation errors between learned structure input and a simulation workflow also need scrutiny before calling the reference fully independent. This is a limitation on inference, not evidence that the candidates lack value.

The headline computational-speed comparison is likewise a reported benchmark result, not a measured local saving including every cost. A replication must reconcile hardware, molecule/target sets, structures, protonation/cofactors, MSA/preparation, caching, unsuccessful runs, supported cases and wall-clock/operator costs. A cheap ligand-only or nearest-neighbour control could test shortcut dependence if lawful matched artifacts become available. It should complement the actual strong baselines, not imply the paper omitted physics comparisons.

## Rights, released methods and reachable contribution

The article states CC BY 4.0. The official repository expressly states MIT for code and weights; this is stronger than reading a badge, but this pass did not read the full licence file at an immutable commit or inspect a checkpoint's bytes/terms. Data-source grants, compiled assay manifests, proprietary internal assays and dependency/MSA-service terms remain separate. No asset download or commercial permission was exercised.

At inspection the unpinned README still labels updated Boltz-2 evaluation/training material as forthcoming and says the default model selection tracks latest. That is a concrete documentation/reproduction gate, **not proof no relevant scripts, predictions or newer release exist elsewhere**. The paper is pinned to v1; the repository commit, matched checkpoint, prediction artifacts and full evaluation environment remain unpinned. No reproducibility defect, code bug, speed result or calibration result was independently demonstrated.

The paper identifies MIT CSAIL/Jameel Clinic, Valence Labs/Recursion and ETH Zurich. Saro Passaro, Gabriele Corso and Jeremy Wohlwend are named public research contacts through the publication and [official repository](https://github.com/jwohlwend/boltz); its issue route is public discovery. No issue bodies, contribution policy, recruitment channel or contact availability were audited. Affiliations and an open repository are not funded admission, an engineering vacancy or a degree/work-rights waiver.

A useful software contribution could concern exact assay/quantity/censor provenance, split/report correctness or a reproduced native evaluator regression, once lawful paper-matched artifacts and independent expectations exist. Qualified chemistry/assay review is still needed for scientific interpretation; producing a parser/report does not supply medicinal-chemistry expertise, lab access or a scientist credential. No broad claim about clinical value or future job volume follows.

## Existing-artifact decision: preserve the gap

There is **no valid direct canonical project join established here**. The existing scientific-data gateway is an ORD reaction-schema/validator project; the materials project uses DFT hull/energy/force references. An affinity assay evaluator has different native schemas, labels, splits and scientific oracles. The scientific-oracle diagnostic shares a proof-level principle, but its authored volume/force/identifiability tasks are not silently replaced by affinity prediction.

Accordingly this pass adds no project, course, hours, budget or claim of biological competence. The existing gateway/materials hours remain unchanged and unallocated. This report and four fictional metadata cases are reference material only. If a future chosen artifact legitimately accepts an assay/split-report extension, its compatible schema, native baseline, independently specified counterexamples, rights and paper-matched artifacts must first be explicit.

Continue only after those source/version/oracle gates can support the intended claim; otherwise retain the metadata/methods result. Stop a novelty claim if the native evaluator already supplies the report or a supposed defect disappears under correct versions. Stop an accuracy or prospective-experiment claim when the reference or access is missing, without declaring the model or entire field useless. Accepted contribution, sustained software ownership and paid research access remain separate later evidence.

## Retrieval and preservation limits

Three primary endpoint URLs were directly attempted: the official repository, bioRxiv v1 full text (403), and the readable PMC v1 mirror. Jina DNS failed, so the purpose-built web reader was used; title search discovered the mirror. No fourth primary endpoint, supplementary PDF, model, data, compound asset, install, account, native run, lab/patient action, outreach, UI or child agent was used. Web line receipts are not raw-source byte hashes or an immutable repository pin. The held source index remains SHA `9074b4fb616b9f200cca5b6dcd8efcbd37321761f87e8e623ee359ce01fa13fe`; saved reports and the tree remain unchanged.
