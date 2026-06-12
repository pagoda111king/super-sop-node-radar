# Inspector Node Protocol

Project inspectors must understand project logic before making architecture recommendations.

This protocol defines the smallest sufficient node chain for an inspector.

## Why 9 Nodes

An inspector needs enough structure to avoid shallow scanning, but not so much structure that the review becomes ritual.

The minimum sufficient chain is:

```text
1. Scope Lock
2. Memory Load
3. Source Radar
4. Architecture Reading
5. Change Diff
6. Evidence Normalize
7. Impact Modeling
8. Score / Check
9. Sediment / Proposal
```

Fewer than 9 usually misses one of these:

- project purpose
- project internal logic
- meaningful change detection
- evidence quality
- node-system impact
- reusable sediment

More than 9 usually adds ceremony without improving judgment.

## The 9 Inspector Nodes

| # | Inspector Node | Super SOP Node Family | Purpose | Must Produce |
|---:|---|---|---|---|
| 1 | Scope Lock | Intake | Define project, source boundaries, inspection question, and risk of overclaiming. | project identity, sources, watch goal |
| 2 | Memory Load | Context / Memory | Load Super SOP memory, previous inspection, accepted decisions, rejected ideas, and current taxonomy. | memory snapshot |
| 3 | Source Radar | Radar | Scan configured repos, releases, docs, examples, issues, discussions, blogs, and forums. | source evidence list |
| 4 | Architecture Reading | Evidence Normalize + Data Modeling | Understand how the project actually works: runtime, state, APIs, tools, evals, security, extension points. | project logic map |
| 5 | Change Diff | Radar + Normalize | Compare current state against previous inspection and identify meaningful deltas. | change list |
| 6 | Evidence Normalize | Evidence Normalize | Convert raw findings into normalized evidence records with links, confidence, and claim scope. | evidence table |
| 7 | Impact Modeling | Data Modeling + Planning | Map evidence to Super SOP nodes, rails, or compound patterns. | impact map |
| 8 | Score / Check | Score + Check | Judge evidence strength, testability, usefulness, risk, and whether recommendation is allowed. | decision + confidence |
| 9 | Sediment / Proposal | Handoff + Sediment | Write inspector report, chief proposal, next tests, and reusable pattern notes. | report + next action |

## Required Context Passing

Each node must pass its output to the next node.

Do not jump from Source Radar directly to Recommendation.

The required path is:

```text
source -> project logic -> change -> evidence -> impact -> score/check -> proposal
```

## Project Logic Map

Every serious inspector report must explain the project's logic in this shape:

```yaml
project_purpose:
main_runtime_model:
core_abstractions:
state_and_memory_model:
tool_or_api_surface:
extension_points:
evaluation_or_testing_model:
permission_or_safety_model:
deployment_or_distribution_model:
examples_or_templates:
where_the_project_is_opinionated:
where_the_project_is_weak_or_unclear:
```

If this map is empty, the inspector does not understand the project yet.

## What To Inspect

For GitHub projects:

- README and docs entry
- latest releases and changelog
- source directories for runtime primitives
- examples and templates
- tests and benchmark folders
- issues, discussions, and roadmap when available
- package manifests and integration surfaces
- security, permission, sandbox, auth, or policy files
- tracing, logging, eval, and observability code

For docs-only or article sources:

- official docs
- examples
- diagrams
- API reference
- changelog or announcement posts
- product pages
- linked repos or demos

## Recommendation Gate

A recommendation cannot pass Check unless it answers:

```text
What changed?
Where is the evidence?
How does the project work?
Which node or rail is affected?
Is the pattern recurring across projects?
Can we test it?
What should we sediment?
What happens if we ignore it?
```

## Decision Levels

Use the fixed decision levels:

```text
no_action
watch
document_pattern
update_node_design
update_rail_design
propose_new_compound_pattern
propose_taxonomy_change
```

Taxonomy change is rare. It requires strong evidence across multiple projects or a major project update that is released, documented, testable, and clearly improves the system.

## Sediment Types

Good sediment is reusable.

Allowed sediment:

- architecture pattern note
- node design improvement
- rail design improvement
- test fixture idea
- adapter idea
- skill idea
- MCP connector note
- benchmark case
- rejection rationale

Never sediment vague admiration.

