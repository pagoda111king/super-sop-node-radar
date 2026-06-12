# 超级 SOP 节点雷达

Super SOP Node Radar 是超级 SOP 节点操作系统的持续雷达仓库。

它负责把 GitHub 项目、CLI、MCP、Skill、插件、SDK、数据库、软件产品等外部能力，持续扫描、归类、评分、测试，并映射到 6 层 14 类节点体系中。

核心公式：

```text
节点雷达 = 外部项目扫描 + 节点能力归类 + 证据记录 + 评分测试 + 检查门禁 + 沉淀复用
```

## 一句话说明

这个仓库不是“工具大全”，也不是“awesome list”。

它是一个可验证的节点能力注册表。

也就是说：

```text
每个项目能不能进入某类节点，不看热度，不看感觉，只看证据、理解、测试和适配价值。
```

## 为什么需要这个仓库

我们已经有了 Super SOP Node OS：

```text
6 层 + 14 类核心节点 + 4 条横向轨道
```

但下一步必须回答：

```text
现实世界里哪些项目、工具、框架、软件，真正能支撑每个节点？
```

比如数据库节点能力，不应该只说“数据库”三个字，而要拆成：

- 本地状态库
- 分析型工作区
- 向量记忆库
- 产品级后端
- schema adapter

然后再判断 SQLite、DuckDB、pgvector、Qdrant、Chroma、LanceDB、Supabase、Prisma 分别适合什么位置。

## 当前仓库做两件事

### 1. 节点能力注册表

持续收集外部项目，并把它们映射到节点能力。

目前首批重点是：

```text
Data Modeling -> database substrates
```

也就是数据建模节点里的数据库能力族。

### 2. 固定参考项目检察官系统

固定追踪一批足够重要的 Agent / AI / 工作流项目：

- OpenAI Codex / Agents SDK
- Anthropic Building Effective Agents / Claude Code patterns
- Google ADK / A2A
- Microsoft Agent Framework / Magentic-One
- LangGraph
- OpenClaw / ClawHub
- OpenMAIC
- Hermes Agent
- Feishu Aily
- Coze Studio / Coze Loop
- DeerFlow
- AgentScope

每 3-4 天运行一次检察官评审，判断这些项目有没有值得反哺到我们节点体系的重大更新。

## 数据库节点首批候选

| 项目 | 当前定位 | 状态 |
|---|---|---|
| SQLite | 本地状态库、artifact registry | metadata_triaged |
| DuckDB | 本地分析工作区 | metadata_triaged |
| pgvector | Postgres 内的向量记忆 | metadata_triaged |
| Qdrant | 专用向量检索服务 | metadata_triaged |
| Chroma | AI-native 检索实验 | metadata_triaged |
| LanceDB | 嵌入式多模态检索 | metadata_triaged |
| Supabase | 产品级 Postgres 后端 | metadata_triaged |
| Prisma | TypeScript/Node schema adapter | metadata_triaged |

注意：

```text
metadata_triaged 只代表完成元信息初审，不代表已推荐。
```

真正推荐之前必须经过文档审查、代码/架构理解、测试、评分、检查。

## 检察官 9 节点协议

每个参考项目检察官必须走这个 9 节点链：

```text
Scope Lock
-> Memory Load
-> Source Radar
-> Architecture Reading
-> Change Diff
-> Evidence Normalize
-> Impact Modeling
-> Score / Check
-> Sediment / Proposal
```

为什么是 9 个？

少于 9 个，容易跳过“项目到底怎么工作”的理解。

多于 9 个，容易变成形式主义。

## 检察官必须理解什么

每个检察官都要填项目逻辑图：

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

如果项目逻辑图没有完成：

```text
最高只能给 watch，不能建议修改节点体系。
```

## 总检察官规则

项目检察官负责：

- 看项目
- 查文档
- 查代码
- 查 release
- 查 issue/discussion
- 抽象架构变化
- 映射到我们的节点体系

总检察官负责：

- 汇总所有检察官报告
- 判断是否有必要更新节点设计
- 判断是否要更新横向轨道
- 判断是否要新增复合模式
- 极少数情况下提出 taxonomy change

但是：

```text
总检察官不能直接修改 6 层 14 节点核心体系，只能提出方案，等用户决定。
```

## 决策等级

| 等级 | 含义 |
|---|---|
| no_action | 没有动作 |
| watch | 继续观察 |
| document_pattern | 记录模式，不改体系 |
| update_node_design | 优化某个节点内部设计 |
| update_rail_design | 优化某条横向轨道 |
| propose_new_compound_pattern | 提议新增复合模式 |
| propose_taxonomy_change | 提议改核心分类，要求最高证据 |

## 自动化

已经创建 Codex 自动化：

```text
Automation ID: super-sop-reference-inspectors
Schedule: 每周一、周四 10:00
Cadence: 约每 3-4 天一次
```

它会定期跑固定参考项目检察官系统，并生成总检察官方案。

自动化说明在：

```text
docs/AUTOMATION.md
```

## 中文阅读顺序

建议按这个顺序看：

1. 本文件：中文总说明
2. `docs/NODE_RADAR_PROTOCOL.md`：节点雷达协议
3. `docs/DATABASE_NODE_PLAYBOOK.md`：数据库节点设计
4. `docs/REFERENCE_INSPECTOR_SYSTEM.md`：固定参考项目检察官系统
5. `docs/INSPECTOR_NODE_PROTOCOL.md`：检察官 9 节点协议
6. `inspectors/reference-projects.json`：固定追踪项目清单
7. `inspectors/understanding-contracts.json`：每个检察官要看什么、怎么想
8. `chief-inspector/reports/2026-06-12-reference-inspection.md`：总检察官基线报告

## 重要文件说明

| 文件 | 用途 |
|---|---|
| `README.md` | 英文总说明 |
| `README.zh-CN.md` | 中文总说明 |
| `AGENTS.md` | Codex 加载说明 |
| `CLAUDE.md` | Claude Code 加载说明 |
| `docs/NODE_RADAR_PROTOCOL.md` | 雷达扫描协议 |
| `docs/DATABASE_NODE_PLAYBOOK.md` | 数据库节点 playbook |
| `docs/REFERENCE_INSPECTOR_SYSTEM.md` | 检察官系统说明 |
| `docs/INSPECTOR_NODE_PROTOCOL.md` | 检察官 9 节点协议 |
| `docs/AUTOMATION.md` | 自动化说明 |
| `registry/projects/` | 项目注册表 |
| `registry/node-maps/` | 节点能力映射 |
| `inspectors/reference-projects.json` | 固定参考项目 |
| `inspectors/understanding-contracts.json` | 检察官理解契约 |
| `inspectors/runs/` | 每次项目检察官报告 |
| `chief-inspector/reports/` | 总检察官报告 |
| `scripts/validate_registry.py` | 注册表校验 |
| `scripts/validate_inspectors.py` | 检察官配置校验 |
| `scripts/run_reference_inspection.py` | 生成检察官报告 |

## 基本命令

校验注册表：

```bash
python3 scripts/validate_registry.py
```

校验检察官配置：

```bash
python3 scripts/validate_inspectors.py
```

生成一次参考项目检察官报告：

```bash
python3 scripts/run_reference_inspection.py
```

查看数据库节点摘要：

```bash
python3 scripts/summarize_node.py data-modeling.database
```

## 最重要原则

```text
不要把热度当证据。
不要把元信息当理解。
不要从扫描直接跳到建议。
必须先理解项目逻辑，再判断它是否值得改变我们的节点体系。
```

