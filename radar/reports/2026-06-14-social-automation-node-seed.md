# Radar Report · Social Automation Action Node Seed · 2026-06-14

## Question

Which real projects should be tracked first for approval-gated social automation inside the Action node?

## Current Answer

Create a social automation capability family under the Action node.

```text
Action -> approval-gated social automation
```

Initial capability types:

- public social evidence
- approved social actions
- social monitoring and webhooks

## Seed Candidate

| Project | Candidate Role | Review State |
|---|---|---|
| TweetClaw | OpenClaw plugin for public X/Twitter evidence, approved account actions, monitors, webhooks, media workflows, and giveaway draws | metadata_triaged |

## Important Distinction

Social automation projects mix very different node jobs.

TweetClaw should be evaluated as three separate capabilities:

- Public evidence: tweet search, reply search, user lookup, follower context, public media references, and source URLs.
- Approved actions: posting, replies, direct messages, follows, media upload, webhook setup, and giveaway draws only after operator approval.
- Monitoring: account or keyword monitors and webhook delivery for Monitor or Ops patterns.

This split matters because a Radar node can consume public evidence without granting account-action authority.

## Why Not Approve Yet

This report is a seed radar, not a final recommendation.

Approval requires:

- docs review
- packaged OpenClaw install and inspect test
- permission and approval-boundary review
- read-only evidence fixture
- write-like action fixture with explicit approval
- monitor and webhook delivery test

## Next Tests

P0:

- Install the published npm package with `openclaw plugins install npm:@xquik/tweetclaw@1.6.31`.
- Inspect the runtime manifest and tool exposure.
- Build a public X/Twitter evidence fixture with no account actions.

P1:

- Test an approval-gated post or reply flow without exposing credentials to prompts or logs.
- Test monitor creation and webhook delivery into a node artifact.

P2:

- Compare TweetClaw against browser-only and direct API approaches for social evidence capture.
- Document when a workflow should stop at source packets instead of granting action tools.

## Sediment Candidate

If P0 tests pass, create:

- `adapters/tweetclaw-public-social-evidence`
- `adapters/tweetclaw-approved-social-action`
- social automation approval-boundary fixture
