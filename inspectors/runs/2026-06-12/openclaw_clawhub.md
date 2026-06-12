# Project Inspector Report · 2026-06-12

## Inspector

- id: `openclaw_clawhub`
- name: OpenClaw / ClawHub Inspector
- priority: `P0`

## Inspector Node Chain

This inspector must pass context through the full chain before making recommendations:

```text
scope_lock -> memory_load -> source_radar -> architecture_reading -> change_diff -> evidence_normalize -> impact_modeling -> score_check -> sediment_proposal
```

## Understanding Contract

Logic focus: How OpenClaw and ClawHub package skills/plugins, gate tools, publish versions, moderate packages, and distribute agent capabilities.

### Must Read Surfaces

- OpenClaw releases and docs
- ClawHub releases and skill format docs
- plugin and skill examples
- moderation, install, and update flows

### Tracking Surfaces

- openclaw/openclaw releases
- openclaw/clawhub releases
- OpenClaw docs
- ClawHub docs

### Architecture Questions

- What is the current skill/plugin contract?
- How are package trust, moderation, install, and versioning handled?
- How are tools and permissions gated?
- Which changes should affect Context, Action, Check, Handoff, Sediment, or Policy/Permission?

### Sediment Targets

- skill format update
- package trust rule
- publish/handoff pattern
- policy permission gate

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
| github | OpenClaw | https://github.com/openclaw/openclaw | github_metadata_checked |
| github | ClawHub | https://github.com/openclaw/clawhub | github_metadata_checked |
| docs | OpenClaw Skills | https://docs.openclaw.ai/tools/skills | manual_review_needed |
| docs | ClawHub Skill Format | https://docs.openclaw.ai/clawhub/skill-format | manual_review_needed |

## GitHub Metadata Snapshot

| Repo | Stars | Forks | Pushed At | Latest Release | License | Archived |
|---|---:|---:|---|---|---|---|
| [`openclaw/openclaw`](https://github.com/openclaw/openclaw) | 378334 | 79124 | 2026-06-12T12:24:06Z | [v2026.6.6](https://github.com/openclaw/openclaw/releases/tag/v2026.6.6) · 2026-06-12T11:04:42Z | Other | False |
| [`openclaw/clawhub`](https://github.com/openclaw/clawhub) | 8930 | 1393 | 2026-06-12T09:35:49Z | [v0.21.0](https://github.com/openclaw/clawhub/releases/tag/v0.21.0) · 2026-06-12T01:02:36Z | MIT License | False |

## Watch Questions

- skill format changes
- plugin packaging
- registry trust, moderation, and versioning
- tool permissions and installation flows

## Node / Rail Relevance

- `context_memory`
- `action`
- `check`
- `handoff`
- `sediment`
- `policy_permission`

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
