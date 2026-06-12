---
name: super-sop-node-radar
description: Continuously discover, classify, score, and sediment GitHub projects, CLIs, MCP servers, skills, plugins, apps, and software as reusable Super SOP node capabilities.
version: 0.1.0
metadata:
  openclaw:
    homepage: https://github.com/pagoda111king/super-sop-node-radar
    requires:
      bins:
        - python3
---

# Super SOP Node Radar

Use this skill when the user wants to scan GitHub or the ecosystem for projects that can power specific Super SOP node classes.

## Thesis

In the node era, software capabilities become node capabilities:

```text
GitHub projects, CLIs, MCP servers, skills, plugins, apps, SDKs, and databases
-> node candidates
-> reviewed node capabilities
-> adapters / skills / templates / rules
```

## Default Chain

```text
Intake -> Context -> Radar -> Evidence Normalize -> Data Modeling -> Score -> Check -> Sediment
```

## Do Not Overclaim

Do not mark a project as approved from popularity or metadata alone.

Use review states:

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

## Registry Workflow

1. Identify the target node class or capability family.
2. Scan candidate projects.
3. Create or update `registry/projects/*.json`.
4. Map projects in `registry/node-maps/*.json`.
5. Record findings in `radar/reports/`.
6. Run `python3 scripts/validate_registry.py`.

## Reference Loading

Read only what is needed:

- `references/node-radar-protocol.md` for the scan/review flow.
- `references/classification-model.md` for node classification.
- `references/database-node-playbook.md` for database capability design.

## Fixed Reference Inspectors

When the user asks to monitor major reference projects, read `inspectors/reference-projects.json` and use:

```bash
python3 scripts/validate_inspectors.py
python3 scripts/run_reference_inspection.py
```

The chief inspector can propose node, rail, or compound-pattern improvements, but cannot directly modify the core taxonomy without user approval.
