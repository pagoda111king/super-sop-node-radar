# Radar Report · Database Node Seed · 2026-06-12

## Question

Which real projects should be tracked first for the database capability family inside the Data Modeling node?

## Current Answer

Create a database capability family instead of a single generic database node.

```text
Data Modeling -> database substrates
```

Initial capability types:

- local state store
- analytical workspace
- vector memory
- product backend
- schema adapter

## Seed Candidates

| Project | Candidate Role | Review State |
|---|---|---|
| SQLite | local state store | metadata_triaged |
| DuckDB | analytical workspace | metadata_triaged |
| pgvector | vector memory inside Postgres | metadata_triaged |
| Qdrant | dedicated vector memory service | metadata_triaged |
| Chroma | AI-native vector memory/search | metadata_triaged |
| LanceDB | embedded multimodal retrieval | metadata_triaged |
| Supabase | product backend | metadata_triaged |
| Prisma | schema adapter | metadata_triaged |

## Important Distinction

Database projects do not all do the same node job.

SQLite and DuckDB are especially important for local-first agent work:

- SQLite: state, checkpoints, artifact registry, small relational stores.
- DuckDB: analytical workspace over evidence files and tabular artifacts.

Vector projects are important for memory and retrieval:

- pgvector: vector search inside Postgres.
- Qdrant: dedicated vector retrieval service.
- Chroma: AI-native search infrastructure.
- LanceDB: embedded multimodal retrieval.

Platform and adapter projects are different:

- Supabase: product-grade backend.
- Prisma: typed schema adapter for application code.

## Why Not Approve Yet

This report is a seed radar, not a final recommendation.

Approval requires:

- docs review
- install path review
- minimal task benchmark
- failure-mode notes
- adapter guidance

## Next Tests

P0:

- SQLite artifact registry test.
- DuckDB evidence analysis test.

P1:

- pgvector/Qdrant/Chroma concept memory retrieval comparison.
- Supabase team-facing artifact backend review.

P2:

- LanceDB multimodal retrieval test.
- Prisma typed schema adapter test.

## Sediment Candidate

If P0 tests pass, create:

- `adapters/sqlite-artifact-registry`
- `adapters/duckdb-evidence-workspace`
- database node benchmark fixture

