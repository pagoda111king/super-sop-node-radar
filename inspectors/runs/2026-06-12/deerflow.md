# Project Inspector Report · 2026-06-12

## Inspector

- id: `deerflow`
- name: DeerFlow Inspector
- priority: `P1`

## Inspector Node Chain

This inspector must pass context through the full chain before making recommendations:

```text
scope_lock -> memory_load -> source_radar -> architecture_reading -> change_diff -> evidence_normalize -> impact_modeling -> score_check -> sediment_proposal
```

## Understanding Contract

Logic focus: How DeerFlow handles long-horizon agent tasks, subagents, memory, sandboxes, filesystem operations, skills, tools, and gateways.

### Must Read Surfaces

- DeerFlow releases
- subagent and memory code/docs
- sandbox and filesystem handling
- tool, skill, and gateway examples

### Tracking Surfaces

- bytedance/deer-flow releases
- architecture docs or examples
- long-horizon task implementations

### Architecture Questions

- How is long-horizon task state represented?
- How are subagents delegated and monitored?
- How are sandbox, filesystem, and gateway risks controlled?
- Which changes should affect Context, Routing, Action, Check, or Sediment?

### Sediment Targets

- long-horizon run rule
- subagent delegation pattern
- sandbox action gate
- filesystem rollback note

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
| github | DeerFlow | https://github.com/bytedance/deer-flow | github_metadata_checked |

## GitHub Metadata Snapshot

| Repo | Stars | Forks | Pushed At | Latest Release | License | Archived |
|---|---:|---:|---|---|---|---|
| [`bytedance/deer-flow`](https://github.com/bytedance/deer-flow) | 71039 | 9623 | 2026-06-12T09:16:02Z | - | MIT License | False |

## Watch Questions

- long-horizon agent architecture
- subagents, memory, sandboxes, filesystem, gateways
- skills and tool execution patterns

## Node / Rail Relevance

- `context_memory`
- `routing`
- `action`
- `check`
- `sediment`

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
