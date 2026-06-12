# Classification Model

The registry classifies projects by node usefulness, not by software category alone.

## Core Question

For each project, ask:

```text
What node job can this project reliably perform?
```

## 14 Core Node Classes

| Node | Typical External Capabilities |
|---|---|
| Intake | forms, issue templates, chat capture, voice capture |
| Context / Memory | memory stores, session stores, pruning, retrieval |
| Radar | search APIs, crawlers, repository scanners, market scanners |
| Evidence Normalize | parsers, extractors, ETL, cleaning, schema mapping |
| Data Modeling | databases, vector stores, knowledge bases, tables, artifacts |
| Planning | planners, task DAGs, workflow engines |
| Routing | routers, orchestrators, subagent dispatch, A2A |
| Learning | tutors, quiz engines, simulation tools, whiteboards |
| Action | CLIs, browser automation, filesystem tools, deploy tools |
| Test | test runners, browser QA, benchmark harnesses, eval datasets |
| Score | graders, eval frameworks, metric systems, ranking engines |
| Check | guardrails, policy engines, security scanners, review gates |
| Handoff | docs, tickets, PRs, IM, email, task systems |
| Sediment | skills, templates, rules, playbooks, memory updates |

## Cross-Cutting Rails

Some projects should not be forced into one node.

Use rails when the project supports many nodes:

| Rail | Examples |
|---|---|
| Observe / Trace | tracing, logs, telemetry, cost tracking |
| Policy / Permission | auth, sandbox, approval, secrets |
| Artifact Registry | object stores, schema registries, package registries |
| Human / Team | review workflows, assignments, escalation, approvals |

## Compound Patterns

Some capabilities are combinations:

| Compound | Composed From |
|---|---|
| Deploy / Publish | Action + Check + Handoff |
| Monitor / Ops | Observe + Test + Score + Check + Sediment |

## Fit Levels

Use fit levels to avoid overclaiming.

| Fit | Meaning |
|---|---|
| `primary` | The project directly performs this node job. |
| `supporting` | The project supports the node but is not enough alone. |
| `adapter` | The project connects this node to another system. |
| `infrastructure` | The project provides substrate under many nodes. |
| `reference` | Useful design reference, not a direct runtime dependency. |

## Database Example

Database projects are not one generic bucket.

They split into several node roles:

| Role | Node Use |
|---|---|
| local state store | checkpoints, small artifacts, local runs |
| analytical workspace | temporary analysis over files and tables |
| product database | multi-user app state and permissions |
| vector memory | semantic retrieval and long-term memory |
| schema adapter | typed application access to databases |

