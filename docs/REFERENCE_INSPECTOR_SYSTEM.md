# Reference Inspector System

This system monitors fixed reference projects and asks whether their updates should improve Super SOP Node OS.

## Purpose

The reference projects are large enough and influential enough that their updates may reveal:

- new agent architecture patterns
- better node design
- better cross-cutting rails
- better evaluation methods
- better workflow/runtime packaging
- better enterprise interoperability
- better learning or memory loops

The goal is not to copy them. The goal is to inspect their strongest updates and decide whether they should change our node system.

## Fixed Reference Set

The fixed sources are configured in:

```text
inspectors/reference-projects.json
```

Current source families:

- OpenAI Codex / Agents SDK
- Anthropic Building Effective Agents / Claude Code patterns
- Google ADK / A2A
- Microsoft Agent Framework / Magentic-One
- LangGraph
- OpenClaw / ClawHub
- OpenMAIC
- Hermes Agent
- Feishu Aily
- Coze Studio / Coze Loop
- DeerFlow
- AgentScope

## Inspector Roles

Each project inspector acts like a specialist reviewer.

It knows:

- the fixed project sources
- what to watch for
- which Super SOP nodes and rails the project may affect
- the current Super SOP memory:

```text
6 layers + 14 core nodes + 4 rails + 2 compound patterns
```

Each inspector must output:

- important updates
- evidence links
- possible node/rail impact
- confidence level
- suggested next action
- whether the change is local, structural, or potentially taxonomy-changing

## Chief Inspector

The chief inspector reads all project inspector outputs.

It decides whether updates deserve:

| Decision | Meaning |
|---|---|
| `no_action` | No meaningful impact. |
| `watch` | Interesting but not mature enough. |
| `document_pattern` | Add a pattern note, but do not alter nodes. |
| `update_node_design` | Improve one node's internal protocol. |
| `update_rail_design` | Improve a cross-cutting rail. |
| `propose_new_compound_pattern` | Add a reusable combination of nodes/rails. |
| `propose_taxonomy_change` | Consider changing 6-layer/14-node taxonomy. Requires high evidence. |

## Cadence

Run every Monday and Thursday.

This produces a 3-4 day rhythm:

```text
Monday -> Thursday -> Monday
```

This fits the target of one proposal every 3-5 days.

## Evidence Standard

An update is worth surfacing only if it is at least one of:

- released
- documented
- merged in code
- repeatedly discussed in official channels
- visible in examples/templates
- tied to a real product/runtime behavior

Do not escalate:

- vague marketing copy
- isolated commits with unclear impact
- popularity movement alone
- speculation without source links

## Impact Standard

Every proposed change must answer:

```text
What does this improve in our system?
Which node or rail changes?
Is it testable?
Is it reusable?
Does it simplify or complicate the taxonomy?
What happens if we ignore it?
```

## Output

Each cycle should produce a chief inspector proposal:

```text
chief-inspector/reports/YYYY-MM-DD-reference-inspection.md
```

The user decides whether to accept any proposed optimization.

## Safety Rule

Inspectors cannot directly modify the core node taxonomy.

They can only propose:

- node protocol improvements
- rail improvements
- compound pattern additions
- test tasks
- documentation updates
- taxonomy change proposals

