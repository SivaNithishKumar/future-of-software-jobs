# Future of software jobs → 2031

What will developer work look like in five years, and how should a developer prepare? This repo holds the results of a **multi-day, multi-agent research run** on that question. Eight parallel research agents in OpenAI Codex worked through scheduled passes from 19 to 21 October 2026. They followed claims back to papers, filings, datasets and job postings, then repeatedly tried to disprove their own conclusions. Claude then condensed the work into a plain-language mind map.

**[Open the interactive mind map →](https://sivanithishkumar.github.io/future-of-software-jobs/)** (or open `index.html` locally)

> These are evidence-backed findings and hypotheses to test, **not** a jobs forecast. No source predicts 2031 job counts. The research also flags where its own evidence is weak.

## The short answer

- **Aim to own outcomes, not just write code.** Understand a real system, use AI and ready-made tools well, measure failures and cost, and maintain what others depend on. The research treats this as a bet to test with small experiments, not a safe niche.
- **Entry-level hiring looks weaker in AI-exposed jobs.** In US payroll data, 22–25-year-olds in those jobs are about 19% below their peers, mostly because of less hiring. Nobody has shown that AI caused it, and no study shows mass developer job loss.
- **AI agents do long coding tasks well when the answer is easy to check.** Work like ports, migrations and clearly specified code automates first. Building and auditing those checks looks more durable than producing the code.
- **Real productivity evidence conflicts.** One study found experienced developers 19% slower with AI tools, another found 26% more pull requests, and a 2026 follow-up was inconclusive.
- **AI is now an industrial supply chain**: chips, HBM memory, fabs, packaging, networks and power. Announced capacity isn't built capacity. The developer work there (serving and memory software, compilers, open EDA, grid data) is real but narrow.
- **Robotics is real but narrow.** About 5 million factory robots are in use, versus about 7,000 humanoids sold in 2025. The accessible software work is operations, evaluation, replay and inspection. Hardware access and location are real barriers.
- **Neither research nor custom integration is automatically safe.** Cloud vendors already bundle evals, agents and incident tooling. AI research-engineering results are strong.
- **Start small.** Run one 30-day experiment against a strong existing tool. Stop if the existing tool wins or you can't check the right answer independently.

## What's inside

| Path | What it is |
|---|---|
| [`index.html`](index.html) | Interactive mind map: 6 branches, ~340 nodes, each linked to notes and sources |
| [`notes/`](notes) | 258 research notes in markdown: findings, evidence audits, counter-arguments, 2031 scenarios, field deep-dives |
| [`INDEX.json`](INDEX.json) | Every note's path, field, title and one-paragraph summary. Start here to navigate |
| [`data/mindmap.json`](data/mindmap.json) | The mind map as plain JSON |
| [`data/sources.json`](data/sources.json) | All **2,375 source URLs**, each tagged with the notes that cite it |
| [`data/claims.json`](data/claims.json) | Main claims, each with counter-evidence and what would prove it wrong |
| [`data/codex-final-tree.json`](data/codex-final-tree.json) | Codex's full final tree (1,022 entries, project plans, directories, cross-links). A readable outline is in [`codex-final-tree-outline.md`](data/codex-final-tree-outline.md) |
| [`data/codex-living-updates.json`](data/codex-living-updates.json) | Dated branches added in later research rounds |
| [`sources/`](sources) | The few source documents whose licences allow redistribution (see [`sources/LICENSES.md`](sources/LICENSES.md)). Everything else is linked, not copied |

### Notes by field

| Field | Notes | Good first reads |
|---|---|---|
| Strategy, preparation & critiques | 70 | `interim-findings-report-2026-10-20.md`, `adversarial-2031-scenarios-round9.md`, `adversarial-baseline.md`, `preparation-pathways-round8.md` |
| Science, health, security & sectors | 55 | `security.md`, `bio.md`, `finance-payments-round5.md`, `quantum-round3.md` |
| AI hardware, energy & geopolitics | 48 | `supply-chain/sc02-memory.md`, `supply-chain/sc07-geopolitics-dependencies.md`, `compute-hardware-round3.md`, `energy.md` |
| Software & AI engineering | 30 | `software.md`, `agent-capability-horizons-round6.md`, `ai-evaluation-source-audit-round10.md` |
| Jobs & hiring evidence | 28 | `labor.md`, `labor-round3-methods.md`, `india-services-gcc-round4.md`, `uk-ai-workforce-methods-round13.md` |
| Robotics & physical systems | 27 | `robotics.md`, `robotics-round3-generalization.md`, `field-robotics-round4.md` |

## Use it with your own AI agent

The repo is set up so an agent can learn the research and answer questions from it, with citations:

- **Clone it** and open it in Claude Code, Codex, Cursor or similar. The agent reads [`AGENTS.md`](AGENTS.md) for how to navigate.
- **Point any web-capable agent** at [`llms.txt`](llms.txt). It's a short index, and the agent fetches only the files it needs.
- **Use it as an MCP server** through [GitMCP](https://gitmcp.io): add `https://gitmcp.io/SivaNithishKumar/future-of-software-jobs` to Claude Desktop, Cursor or another MCP client.

Example questions: *"What's the evidence on entry-level developer hiring, and what argues against it?"* · *"Where can a software developer contribute in the AI memory/HBM supply chain?"* · *"Give me the 30-day experiments and their stop conditions."*

## How the research was done (and its limits)

- Announcements were treated as leads. Claims were followed to primary papers, filings, trial registrations, datasets and actual job requirements.
- Each claim is labelled by evidence type: observed result, causal study, correlation, forecast, survey, vendor claim, or the researchers' own inference.
- Independent "skeptic" passes tried to break each main conclusion. Several early recommendations were weakened or dropped as a result.
- **Limits:** the proposed experiments were planned, not run. Job postings are examples of requirements, not demand counts. The research doesn't certify current export law or anyone's eligibility for a role. It was written for one developer's breadth (software, AI/ML, robotics), so weigh it against your own situation.
- About 1.8GB of build snapshots and self-check files were left out. Only the research itself is here.

Research by OpenAI Codex (multi-agent), condensed and published with Claude Code.
