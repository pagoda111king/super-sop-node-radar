# Automation

## Super SOP Reference Inspectors

- Automation ID: `super-sop-reference-inspectors`
- Kind: Codex cron automation
- Status: `ACTIVE`
- Workspace: `/Users/tanghuiwen/工作/SOP工厂/github/super-sop-node-radar`
- Schedule: every Monday and Thursday at 10:00 local time
- Cadence: roughly every 3-4 days

## Mission

Run the fixed reference inspector cycle for:

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

## Expected Output

Each cycle should produce a chief inspector proposal for user review.

The proposal should classify changes as:

- `no_action`
- `watch`
- `document_pattern`
- `update_node_design`
- `update_rail_design`
- `propose_new_compound_pattern`
- `propose_taxonomy_change`

## Safety

The automation must not directly change the Super SOP core taxonomy.

It can create reports and proposals, but user approval is required before changing:

- 6-layer model
- 14 core node classes
- cross-cutting rails
- compound patterns

