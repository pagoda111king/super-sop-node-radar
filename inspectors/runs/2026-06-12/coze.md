# Project Inspector Report · 2026-06-12

## Inspector

- id: `coze`
- name: Coze Studio / Coze Loop Inspector
- priority: `P1`

## Inspector Node Chain

This inspector must pass context through the full chain before making recommendations:

```text
scope_lock -> memory_load -> source_radar -> architecture_reading -> change_diff -> evidence_normalize -> impact_modeling -> score_check -> sediment_proposal
```

## Understanding Contract

Logic focus: How Coze Studio and Coze Loop represent visual workflow nodes, DAG execution, node metadata, resources, prompt debugging, eval sets, experiments, and traces.

### Must Read Surfaces

- Coze Studio releases and workflow docs
- Coze Loop releases and eval/trace docs
- node metadata and input/output map implementations
- workflow examples and resources

### Tracking Surfaces

- coze-dev/coze-studio releases
- coze-dev/coze-loop releases
- workflow, prompt, eval, and trace examples

### Architecture Questions

- How are visual nodes typed and executed?
- How are resources, variables, prompts, databases, and knowledge bases attached?
- How do eval sets, experiments, and traces inform improvements?
- Which changes should affect Data Modeling, Planning, Routing, Test, Score, or Observe/Trace?

### Sediment Targets

- executable node spec
- resource mapping pattern
- eval set pattern
- trace-to-improvement loop

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
| github | Coze Studio | https://github.com/coze-dev/coze-studio | github_metadata_checked |
| github | Coze Loop | https://github.com/coze-dev/coze-loop | github_metadata_checked |

## GitHub Metadata Snapshot

| Repo | Stars | Forks | Pushed At | Latest Release | License | Archived |
|---|---:|---:|---|---|---|---|
| [`coze-dev/coze-studio`](https://github.com/coze-dev/coze-studio) | 20976 | 3044 | 2026-04-20T09:20:44Z | [v0.5.1](https://github.com/coze-dev/coze-studio/releases/tag/v0.5.1) · 2026-02-05T06:04:16Z | Apache License 2.0 | False |
| [`coze-dev/coze-loop`](https://github.com/coze-dev/coze-loop) | 5515 | 764 | 2026-06-12T11:13:50Z | [v1.5.1](https://github.com/coze-dev/coze-loop/releases/tag/v1.5.1) · 2026-01-20T12:35:01Z | Apache License 2.0 | False |

## Watch Questions

- visual workflow nodes
- DAG execution
- node metadata and input/output maps
- prompt debugging, eval sets, experiments, traces

## Node / Rail Relevance

- `data_modeling`
- `planning`
- `routing`
- `test`
- `score`
- `observe_trace`

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
