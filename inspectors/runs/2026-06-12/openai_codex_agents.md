# Project Inspector Report · 2026-06-12

## Inspector

- id: `openai_codex_agents`
- name: OpenAI Codex / Agents SDK Inspector
- priority: `P0`

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
| [`openai/codex`](https://github.com/openai/codex) | 90640 | 13355 | 2026-06-12T11:58:29Z | [rust-v0.139.0](https://github.com/openai/codex/releases/tag/rust-v0.139.0) · 2026-06-09T20:13:29Z | Apache License 2.0 | False |
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

Automated metadata snapshot complete. Deep code, docs, forum, issue, and release-note review should be added by the scheduled inspector run before recommending node changes.

## Recommendation

Decision: `watch`

Reason: metadata checked; no deep impact judgment recorded yet.

Next test: inspect recent releases/docs/issues and map any substantial change to node/rail impact.
