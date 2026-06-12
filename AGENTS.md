# Agent Instructions

Use this repository as a living radar and registry for node capabilities.

## Operating Model

When adding or updating projects, use this chain:

```text
Intake -> Context -> Radar -> Evidence Normalize -> Data Modeling -> Score -> Check -> Sediment
```

## Rules

- Do not mark a project as `approved` from metadata alone.
- Every registry entry must include source URLs and a review state.
- Every node mapping must say which node class the project can support and why.
- Every score must explain tradeoffs, not only stars or popularity.
- If a tool requires credentials, network services, paid accounts, or local daemons, record that in risks.
- Prefer small, testable claims over broad claims.

## Review States

Use only:

```text
candidate
metadata_triaged
docs_reviewed
code_reviewed
tested
benchmarked
approved
deprecated
```

## Quality Gate

Before committing a registry update, run:

```bash
python3 scripts/validate_registry.py
```

For project-like changes, update the relevant report under `radar/reports/`.
