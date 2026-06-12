# Project Inspector Report · 2026-06-12

## Inspector

- id: `anthropic_effective_agents`
- name: Anthropic Effective Agents / Claude Code Inspector
- priority: `P0`

## Inspector Node Chain

This inspector must pass context through the full chain before making recommendations:

```text
scope_lock -> memory_load -> source_radar -> architecture_reading -> change_diff -> evidence_normalize -> impact_modeling -> score_check -> sediment_proposal
```

## Understanding Contract

Logic focus: How Anthropic frames agent workflows, subagents, hooks, evaluator-optimizer loops, and practical evals.

### Must Read Surfaces

- Building Effective Agents article
- agent evals article
- Claude Code hook docs
- workflow and subagent examples when available

### Tracking Surfaces

- Anthropic engineering and research posts
- Claude Code docs
- hook/event lifecycle docs

### Architecture Questions

- Which workflow pattern is being recommended?
- Where do hooks intercept the node run?
- How are evaluators designed and calibrated?
- Which changes should affect Planning, Routing, Test, Score, Check, or Sediment nodes?

### Sediment Targets

- workflow pattern note
- hook gate pattern
- evaluator design pattern
- score/check improvement

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
| article | Building Effective Agents | https://www.anthropic.com/research/building-effective-agents | manual_review_needed |
| article | Demystifying Evals for AI Agents | https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents | manual_review_needed |
| docs | Claude Code Hooks | https://code.claude.com/docs/en/agent-sdk/hooks | manual_review_needed |

## GitHub Metadata Snapshot

| Repo | Stars | Forks | Pushed At | Latest Release | License | Archived |
|---|---:|---:|---|---|---|---|

## Watch Questions

- workflow patterns
- subagents and hooks
- evaluator-optimizer changes
- agent evaluation practice

## Node / Rail Relevance

- `planning`
- `routing`
- `test`
- `score`
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
