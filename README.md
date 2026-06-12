# Super SOP Node Radar

Everything as Nodes Registry for the Node Era.

This repository is the continuously updated radar for Super SOP Node OS.

The core idea:

```text
apps, plugins, CLIs, MCP servers, skills, SDKs, databases, and GitHub projects
are not just tools. They are reusable node capabilities.
```

Super SOP Node OS defines the operating system:

```text
6 layers + 14 core node classes + 4 cross-cutting rails
```

This repository answers the next question:

```text
Which real projects can reliably power each node?
```

## Why This Exists

The agent ecosystem is moving through several stages:

1. Chat era: one-off model conversations.
2. Agent era: tools, memory, planning, handoffs, evals.
3. OpenClaw / Hermes era: skills, plugins, always-on agents, registries.
4. Node era: every useful capability becomes a composable, testable, reusable node.

In the node era, a GitHub project is often doing one node job:

- database state
- retrieval
- orchestration
- evaluation
- tracing
- browser control
- document generation
- workflow routing
- skill packaging
- enterprise handoff

But a project should not be accepted just because it is popular. Each candidate must pass radar, normalization, scoring, testing, and review.

## Repository Contract

This repo is not a "best tools" list.

It is a verifiable registry with review stages:

| Stage | Meaning |
|---|---|
| `candidate` | Discovered by Radar. Metadata only. Not recommended yet. |
| `metadata_triaged` | Basic GitHub metadata checked and mapped to possible nodes. |
| `docs_reviewed` | README/docs inspected and fit risks documented. |
| `code_reviewed` | Important implementation areas inspected. |
| `tested` | Minimal local or CI test run completed. |
| `benchmarked` | Reproducible task benchmark exists. |
| `approved` | Stable recommendation for a node use case. |
| `deprecated` | No longer recommended. |

## Current Seed Focus

The first focus area is the database capability family inside the Data Modeling node:

```text
Data Modeling -> database substrates -> state, analytics, vectors, product DBs, ORM/schema adapters
```

Initial candidates include SQLite, DuckDB, pgvector, Qdrant, Chroma, LanceDB, Supabase, and Prisma.

These are not all approved. Most are seed candidates or metadata-triaged records.

## Directory

```text
.
├── AGENTS.md
├── CLAUDE.md
├── README.md
├── docs/
│   ├── CLASSIFICATION_MODEL.md
│   ├── DATABASE_NODE_PLAYBOOK.md
│   ├── NODE_RADAR_PROTOCOL.md
│   ├── OPERATING_CADENCE.md
│   └── SCORING_RUBRIC.md
├── registry/
│   ├── node-classes.json
│   ├── node-maps/
│   │   └── data-modeling.database.json
│   └── projects/
├── radar/
│   ├── queues/
│   │   └── database-candidates.json
│   └── reports/
│       └── 2026-06-12-database-node-seed.md
├── schemas/
│   ├── node-capability.v1.json
│   └── project-entry.v1.json
└── scripts/
    ├── summarize_node.py
    └── validate_registry.py
```

## Basic Use

Validate the registry:

```bash
python3 scripts/validate_registry.py
```

Summarize one node map:

```bash
python3 scripts/summarize_node.py data-modeling.database
```

Current note: the first public version uses local validation scripts. GitHub Actions can be added after the repository token has workflow permission.

## Relationship To Super SOP Node OS

Super SOP Node OS is the method and execution protocol:

- https://github.com/pagoda111king/super-sop-node-os

Super SOP Node Radar is the living evidence base:

- discover projects
- classify node fit
- record evidence
- score stability
- test real performance
- sediment approved adapters and skills

## Fixed Reference Inspectors

Some projects are not ordinary candidates. They are major reference systems that should be watched continuously because their updates can influence the node architecture itself.

The fixed inspector set is in:

```text
inspectors/reference-projects.json
```

It currently tracks:

```text
OpenAI Codex / Agents SDK, Anthropic, Google ADK / A2A,
Microsoft Agent Framework / Magentic-One, LangGraph,
OpenClaw / ClawHub, OpenMAIC, Hermes Agent, Feishu Aily,
Coze, DeerFlow, AgentScope
```

Generate a metadata-first inspection snapshot:

```bash
python3 scripts/validate_inspectors.py
python3 scripts/run_reference_inspection.py
```

Project inspector reports are written to:

```text
inspectors/runs/YYYY-MM-DD/
```

The chief inspector proposal is written to:

```text
chief-inspector/reports/YYYY-MM-DD-reference-inspection.md
```

The chief inspector cannot directly change the 14-node taxonomy. It only proposes optimizations for user review.

## Main Rule

Do not promote a project from candidate to approved without evidence.

Popularity is a radar signal, not a proof.
