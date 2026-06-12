# Project Inspector Report · 2026-06-12

## Inspector

- id: `openai_codex_agents`
- name: OpenAI Codex / Agents SDK Inspector
- priority: `P0`

## Inspector Node Chain

This inspector must pass context through the full chain before making recommendations:

```text
scope_lock -> memory_load -> source_radar -> architecture_reading -> change_diff -> evidence_normalize -> impact_modeling -> score_check -> sediment_proposal
```

## Understanding Contract

Logic focus: How Codex and the Agents SDK turn tools, handoffs, guardrails, sessions, tracing, skills, project instructions, and sandboxed coding into a reliable agent runtime.

### Must Read Surfaces

- Codex release notes and repo changes
- Agents SDK release notes and examples
- AGENTS.md guidance
- Codex Skills guidance
- tool, handoff, guardrail, tracing, and session docs

### Tracking Surfaces

- openai/codex releases and major source changes
- openai/openai-agents-python releases and examples
- official Codex docs
- official Agents SDK docs

### Architecture Questions

- How are project instructions loaded and scoped?
- How are tools, handoffs, sessions, and guardrails represented?
- How are sandbox, permissions, review, and rollback handled?
- Which changes should affect Context, Action, Check, Score, Handoff, or Sediment nodes?

### Sediment Targets

- project instruction pattern
- skill packaging pattern
- tool and handoff gate
- trace/eval improvement

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
| github | OpenAI Codex | https://github.com/openai/codex | github_metadata_checked |
| github | OpenAI Agents SDK Python | https://github.com/openai/openai-agents-python | github_metadata_checked |
| docs | OpenAI Agents Guide | https://developers.openai.com/api/docs/guides/agents | manual_review_needed |
| docs | Codex AGENTS.md | https://developers.openai.com/codex/guides/agents-md | manual_review_needed |
| docs | Codex Skills | https://developers.openai.com/codex/skills | manual_review_needed |

## GitHub Metadata Snapshot

| Repo | Stars | Forks | Pushed At | Latest Release | License | Archived |
|---|---:|---:|---|---|---|---|
| [`openai/codex`](https://github.com/openai/codex) | 90641 | 13355 | 2026-06-12T11:58:29Z | [rust-v0.139.0](https://github.com/openai/codex/releases/tag/rust-v0.139.0) · 2026-06-09T20:13:29Z | Apache License 2.0 | False |
| [`openai/openai-agents-python`](https://github.com/openai/openai-agents-python) | 27104 | 4185 | 2026-06-11T04:10:37Z | [v0.17.5](https://github.com/openai/openai-agents-python/releases/tag/v0.17.5) · 2026-06-11T04:11:51Z | MIT License | False |

## Watch Questions

- tool calling and handoff changes
- skills and project instruction changes
- sandbox, worktree, permission, and review changes
- guardrails, tracing, evals, and sessions

## Node / Rail Relevance

- `context_memory`
- `routing`
- `action`
- `score`
- `check`
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
