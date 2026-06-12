# Project Inspector Report · 2026-06-12

## Inspector

- id: `agentscope`
- name: AgentScope Inspector
- priority: `P1`

## Inspector Node Chain

This inspector must pass context through the full chain before making recommendations:

```text
scope_lock -> memory_load -> source_radar -> architecture_reading -> change_diff -> evidence_normalize -> impact_modeling -> score_check -> sediment_proposal
```

## Understanding Contract

Logic focus: How AgentScope handles event streams, permissions, workspace sandboxing, multi-session services, middleware, tracing, evaluation, memory, handoffs, and agent teams.

### Must Read Surfaces

- AgentScope releases and docs
- event stream and frontend docs
- permission/workspace/sandbox docs
- middleware, tracing, eval, memory, and team examples

### Tracking Surfaces

- agentscope-ai/agentscope releases
- AgentScope docs
- service, event, permission, and team examples

### Architecture Questions

- How are events streamed to humans or frontends?
- How are permissions and workspaces enforced?
- How are multi-session services and agent teams represented?
- Which changes should affect Routing, Action, Observe/Trace, Policy/Permission, or Human/Team?

### Sediment Targets

- event stream rail pattern
- workspace permission rule
- agent team routing pattern
- human-in-loop surface note

### Required Logic Map

- `project_purpose`
- `main_runtime_model`
- `core_abstractions`
- `state_and_memory_model`
- `tool_or_api_surface`
- `extension_points`
- `evaluation_or_testing_model`
- `permission_or_safety_model`
- `deployment_or_distribution_model`
- `examples_or_templates`
- `where_the_project_is_opinionated`
- `where_the_project_is_weak_or_unclear`

Current completion status: `incomplete_metadata_only`

## Sources Checked

| Type | Source | URL | Automated Status |
|---|---|---|---|
| github | AgentScope | https://github.com/agentscope-ai/agentscope | github_metadata_checked |
| docs | AgentScope Docs | https://doc.agentscope.io/ | manual_review_needed |

## GitHub Metadata Snapshot

| Repo | Stars | Forks | Pushed At | Latest Release | License | Archived |
|---|---:|---:|---|---|---|---|
| [`agentscope-ai/agentscope`](https://github.com/agentscope-ai/agentscope) | 26733 | 2993 | 2026-06-12T09:03:16Z | [v2.0.1](https://github.com/agentscope-ai/agentscope/releases/tag/v2.0.1) · 2026-06-05T12:13:50Z | Apache License 2.0 | False |

## Watch Questions

- event streams
- permissions and workspace sandbox
- multi-session services
- middleware, tracing, evaluation, agent teams

## Node / Rail Relevance

- `routing`
- `action`
- `observe_trace`
- `policy_permission`
- `human_team`

## Inspector Interpretation

Automated metadata snapshot complete. This report is not sufficient for node-system recommendations until the understanding contract is filled through docs, code, examples, tests/evals, issues/discussions, and release-note review.

## Understanding Gate

The inspector should not recommend node or taxonomy changes until it can answer:

1. What is this project's real runtime or product logic?
2. Which architecture primitive changed or improved?
3. Which Super SOP node, rail, or compound pattern is affected?
4. What evidence proves the change is real?
5. What test or benchmark would falsify the recommendation?
6. What should be sedimented if the recommendation is accepted?

## Recommendation

Decision: `watch`

Reason: metadata checked; no deep impact judgment recorded yet.

Next test: inspect recent releases/docs/issues and map any substantial change to node/rail impact.
