# Guide for AI agents

This repo is a research corpus on **the future of developer and software jobs through ~2031**: labor-market evidence, AI capability, the AI hardware supply chain, robotics, other sectors, and preparation strategies. Use it to answer questions with citations.

## How to navigate

1. **Get the overview first.** Read `README.md` ("The short answer"), then `data/mindmap.json`. It has 6 branches, each with `headlines`, `summary` and nested nodes. Every node has `kind`, `confidence`, `sources` (URLs) and `notes` (paths relative to `notes/`).
2. **Find the right notes.** Read `INDEX.json`. Each entry has `path`, `field`, `title` and a `summary`. Filter by field: `labor-hiring`, `software-ai`, `supply-chain-energy`, `robotics-physical`, `science-health-security-sectors`, `strategy-methods`.
3. **Read only the notes you need.** Notes are dense. Most open with the finding, followed by evidence, limits and counter-evidence. Files named `*-roundNN.md` are later deep-dives, and a higher round can refine an earlier note on the same topic.
4. **Check claims and their counter-evidence** in `data/claims.json`. Every claim lists its evidence type, counter-evidence and what would falsify it.
5. **Trace sources** through `data/sources.json`: URL → notes that cite it. Openly licensed copies of a few documents are in `sources/`.
6. **For depth beyond the mind map**, `data/codex-final-tree.json` holds the full 1,022-entry tree, with project plans that include 30/90-day steps, hours and stop conditions, plus an organisation/lab directory. `data/codex-final-tree-outline.md` is the readable version. Node arrays are `[_, id, parentId, label, type, family, _, _, refs]`, and the `cards` hold details.

## How to answer

- Cite the note path, and the source URL where there is one. Don't present a hypothesis as a finding.
- Keep the evidence labels: a correlation is not a causal effect, a vendor claim is not a deployment, and a job posting is not a demand count.
- Surface counter-evidence alongside a claim. The corpus deliberately argues against its own conclusions.
- The planned experiments were **not run**. Present them as proposals.
- Facts are as of 19–21 October 2026. Flag anything time-sensitive, such as export controls, vacancies or model capability.
- "The reader" in the notes is the developer the research was written for: broad interests across software, AI/ML and robotics, with no verified CV.
