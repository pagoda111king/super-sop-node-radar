# Project Inspector Report · 2026-06-12

## Inspector

- id: `hermes_agent`
- name: Hermes Agent Inspector
- priority: `P1`

## Inspector Node Chain

This inspector must pass context through the full chain before making recommendations:

```text
scope_lock -> memory_load -> source_radar -> architecture_reading -> change_diff -> evidence_normalize -> impact_modeling -> score_check -> sediment_proposal
```

## Understanding Contract

Logic focus: How Hermes Agent maintains persistent agent identity, memory, searchable history, messaging gateways, and automated skill creation.

### Must Read Surfaces

- Hermes Agent releases
- memory and history docs
- messaging gateway docs
- skill creation or automation docs

### Tracking Surfaces

- NousResearch/hermes-agent releases
- Hermes docs
- memory and gateway examples

### Architecture Questions

- How is long-term memory stored and searched?
- How does the agent continue across channels?
- How are repeated patterns turned into skills?
- Which changes should affect Context, Handoff, or Sediment?

### Sediment Targets

- persistent memory rule
- cross-channel handoff pattern
- skill creation trigger
- searchable history note

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
| github | Hermes Agent | https://github.com/NousResearch/hermes-agent | github_metadata_checked |
| docs | Hermes Agent Docs | https://hermes-agent.nousresearch.com/docs/ | manual_review_needed |

## GitHub Metadata Snapshot

| Repo | Stars | Forks | Pushed At | Latest Release | License | Archived |
|---|---:|---:|---|---|---|---|
| [`NousResearch/hermes-agent`](https://github.com/NousResearch/hermes-agent) | 191602 | 33330 | 2026-06-12T10:27:52Z | [v2026.6.5](https://github.com/NousResearch/hermes-agent/releases/tag/v2026.6.5) · 2026-06-06T00:55:58Z | MIT License | False |

## Watch Questions

- persistent agent memory
- searchable conversation history
- messaging gateways
- automated skill creation

## Node / Rail Relevance

- `context_memory`
- `handoff`
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
