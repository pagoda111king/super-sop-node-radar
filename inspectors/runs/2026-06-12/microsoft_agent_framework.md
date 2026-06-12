# Project Inspector Report · 2026-06-12

## Inspector

- id: `microsoft_agent_framework`
- name: Microsoft Agent Framework / Magentic-One Inspector
- priority: `P0`

## Inspector Node Chain

This inspector must pass context through the full chain before making recommendations:

```text
scope_lock -> memory_load -> source_radar -> architecture_reading -> change_diff -> evidence_normalize -> impact_modeling -> score_check -> sediment_proposal
```

## Understanding Contract

Logic focus: How Microsoft structures orchestrator-worker systems, typed state, middleware, telemetry, graph workflows, and replanning.

### Must Read Surfaces

- Agent Framework releases and docs
- middleware, state, workflow, telemetry docs
- Magentic-One architecture article
- examples of orchestrator-worker delegation

### Tracking Surfaces

- microsoft/agent-framework releases
- Microsoft Learn Agent Framework docs
- Microsoft Research Magentic-One updates

### Architecture Questions

- How is live plan state represented?
- How do workers receive tasks and return artifacts?
- Where do middleware, filters, telemetry, and safety gates sit?
- Which changes should affect Planning, Routing, Data Modeling, Observe/Trace, or Check?

### Sediment Targets

- orchestrator-worker pattern
- typed state pattern
- middleware rail improvement
- telemetry check pattern

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
| github | Microsoft Agent Framework | https://github.com/microsoft/agent-framework | github_metadata_checked |
| docs | Agent Framework Overview | https://learn.microsoft.com/en-us/agent-framework/overview/ | manual_review_needed |
| article | Magentic-One | https://www.microsoft.com/en-us/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks/ | manual_review_needed |

## GitHub Metadata Snapshot

| Repo | Stars | Forks | Pushed At | Latest Release | License | Archived |
|---|---:|---:|---|---|---|---|
| [`microsoft/agent-framework`](https://github.com/microsoft/agent-framework) | 11285 | 1886 | 2026-06-12T11:50:29Z | [dotnet-1.10.0](https://github.com/microsoft/agent-framework/releases/tag/dotnet-1.10.0) · 2026-06-10T17:50:17Z | MIT License | False |

## Watch Questions

- orchestrator-worker architecture
- state, middleware, filters, and telemetry
- multi-agent planning and replanning

## Node / Rail Relevance

- `planning`
- `routing`
- `data_modeling`
- `observe_trace`
- `check`

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
