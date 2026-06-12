# Database Node Playbook

Database capability belongs mainly to the Data Modeling node, but it touches Context, Action, Test, Score, Check, Handoff, and Sediment.

## Database Is A Capability Family

Do not define a single generic "database node" too early.

Use this model:

```text
Data Modeling node
  -> database substrates
    -> local state
    -> analytical workspace
    -> vector memory
    -> product backend
    -> schema adapter
```

## Capability Types

| Capability | Best For | Common Risks |
|---|---|---|
| local state store | local node runs, small artifacts, checkpoints | migration discipline, concurrency limits |
| analytical workspace | CSV/Parquet/JSON analysis, temporary modeling | memory usage, query correctness |
| vector memory | semantic retrieval, RAG, memory search | retrieval quality, drift, embedding coupling |
| product backend | real app database, auth, realtime, team access | permissions, hosted service dependency |
| schema adapter | typed DB access, migrations, query ergonomics | abstraction lock-in, generated client drift |

## First Seed Candidates

| Project | Initial Hypothesis |
|---|---|
| SQLite | local state store and durable local artifact index |
| DuckDB | local analytical workspace for Radar/Normalize/Data Modeling |
| pgvector | vector memory inside Postgres-backed systems |
| Qdrant | dedicated vector memory and retrieval service |
| Chroma | AI-native retrieval and memory experiments |
| LanceDB | embedded multimodal retrieval library |
| Supabase | product backend with Postgres, auth, realtime, storage |
| Prisma | schema adapter and typed application DB access |

## What Must Be Tested

Each database candidate needs a real task benchmark:

- create schema
- insert node artifacts
- query by node class
- retrieve evidence by source
- run migration or schema change
- export or backup
- measure setup complexity
- document failure modes

## Approval Criteria

A database project can be approved only for a specific role.

Good:

```text
DuckDB is approved for local analytical workspace over CSV/Parquet artifacts.
```

Too broad:

```text
DuckDB is the best database node.
```

## Adapter Sediment

When a candidate passes tests, sediment:

- schema template
- minimal setup script
- adapter notes
- test fixture
- rollback guide
- node map entry

