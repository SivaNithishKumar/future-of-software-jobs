# Recursive taxonomy draft: handoff and gaps

`taxonomy-draft.json` is a **draft scaffold**, not the final mind map or a field ranking. It contains 773 stable-ID nodes across 16 top-level branches, reaches seven levels including the root, and has 42 validated cross-links plus 65 references into the saved research notes. Every node and cross-link is marked draft. The source evidence and proposed action plans have not been independently reverified during taxonomy construction.

The branches are foundations; software/data/agents; ML/compute; robotics; security; bio/science; energy/climate/water; finance; industry/commerce; administration/legal/public services; education; media/games; geospatial/space; interfaces/wearables; quantum; and personal preparation/career scenarios. Robotics separates sensing/geometry, localisation, tracking/fusion, planning/control, learned policies, runtime/middleware, fleets, safety and bounded applications. Other fields likewise branch through distinct technical problems and selected projects instead of repeating a generic checklist.

Interpret `claimType` carefully: `knowledge-taxonomy` organises concepts; `proposed-experiment` is work not yet run; `future-hypothesis` is an uncertain thesis; `open-question` is unresolved; `role-map` identifies a family without predicting vacancies. The single `reported-primary-guidance` leaf records NCSC's indicative PQC timetable with its scope caveat. Source refs are pointers to note sections, not blanket validation of everything in a subtree.

## Needed before final synthesis

- Adversarially test the preferred integration/evaluation/security thesis against platform bundling, cheaper autonomous systems, buyer access, procurement and support economics. The tree exposes the countercases but does not settle them.
- Strengthen ML training/research, semiconductor/EDA, embedded/real-time electronics, telecom/networking and hardware-access routes. Breadth here is mostly a knowledge scaffold, not a verified hiring or market analysis.
- Strengthen operator/buyer evidence for manufacturing SMEs, agriculture, construction, EV/charging and water operations. Do not present these partial branches as equally evidenced with robotics platform or financial-reconciliation examples.
- Add current role samples with seniority, degree, location, onsite/field work, eligibility and actual accessible entry. Neither the taxonomy nor selected existing postings establish representative India/UK/global demand or salary levels.
- Replace broad note refs with claim-level source IDs from `claim-register.json` / `source-index.json` where appropriate during synthesis. Keep stable node IDs when enriching the tree; cross-links target those IDs.
- Verify source dates, primary methods, corrected/withdrawn announcements and actual current vacancy availability during later research passes. A branch's technical vocabulary is more stable than its market inference.
- Do not infer the reader's seniority, mathematical level, credentials, hardware access, available hours, relocation eligibility or founder preference. Personalise the eventual choices through verified ability and constraints.
- The final visual must progressively disclose this breadth; displaying 773 nodes at once would be unreadable. Default to the trunk and expandable subbranches, preserve keyboard/source access, and make uncertainty visible.

## Validation performed

Python standard-library generation and JSON parse passed. Assertions checked required node fields, unique node IDs, `status=draft`, every cross-link endpoint, every used evidence-reference key and existence of referenced research-note files. Projects and metrics are proposed only; no project tests, source experiments, installations, purchases, external mutations or physical operations were performed.
