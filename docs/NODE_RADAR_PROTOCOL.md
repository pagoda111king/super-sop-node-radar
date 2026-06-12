# Node Radar Protocol

The radar turns ecosystem signals into node-ready evidence.

## Node Chain

```text
Intake -> Context -> Radar -> Evidence Normalize -> Data Modeling -> Score -> Check -> Sediment
```

## 1. Intake

Define the question:

```text
Which projects can power this node capability?
```

Example:

```text
Which projects can power the database capability family for Data Modeling nodes?
```

## 2. Context

Load:

- target node class
- existing registry entries
- expected use case
- constraints: local-first, enterprise, cloud, CLI, MCP, skill, library
- required license or deployment limits

## 3. Radar

Collect candidates from:

- GitHub search
- releases and tags
- official docs
- package registries
- MCP registries
- skill/plugin registries
- real projects using the tool
- benchmark reports

Radar signals are not proof. They only decide what deserves review.

## 4. Evidence Normalize

Normalize into a `project-entry.v1` record:

- repo identity
- license
- activity signal
- release signal
- topics
- node fit hypothesis
- risks
- next review tasks

## 5. Data Modeling

Map the project into one or more node capabilities:

```text
project -> node class -> capability family -> use case -> adapter shape
```

Example:

```text
duckdb/duckdb -> Data Modeling -> analytical_workspace -> local OLAP over files
```

## 6. Score

Score only after evidence exists.

Default dimensions:

- node fit
- maturity
- activity
- integration surface
- local testability
- enterprise fit
- risk
- maintenance burden

## 7. Check

Before approval, verify:

- source URLs are traceable
- claims are scoped
- install or minimal test is reproducible
- license is recorded
- failure modes are documented
- adapter recommendation is specific

## 8. Sediment

When a project proves useful, sediment one of:

- node adapter
- skill
- MCP connector note
- benchmark case
- template
- rule
- migration guide

## Review State Transitions

```text
candidate
  -> metadata_triaged
  -> docs_reviewed
  -> code_reviewed
  -> tested
  -> benchmarked
  -> approved
```

Any state can become:

```text
deprecated
```

## Non-Negotiable Rule

Do not approve from GitHub stars alone.
