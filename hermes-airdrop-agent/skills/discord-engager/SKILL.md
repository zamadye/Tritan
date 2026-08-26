---
name: discord-engager
description: "Monitor project Discord communities for announcements and campaign changes, and draft replies for the operator to review."
version: 1.0.0
author: Hermes Airdrop Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Airdrop, Discord, Community, Monitoring]
    related_skills: [portfolio-tracker, daily-executor]
---

# Discord Engager

Watch project communities for the things that actually change a campaign —
deadline moves, rule changes, snapshot dates, new quest seasons — and draft
replies for a human to send.

## What this skill does and does not do

**Does:** read channels, summarise, detect changes that affect your campaigns,
draft text.

**Does not:** mass-post, auto-reply, or generate engagement at scale. Automated
bulk posting violates Discord's Terms of Service and is a fast way to lose the
accounts a campaign depends on. Every outbound message is drafted here and sent
by the operator. If a project genuinely requires community participation, that
participation should be yours.

## Routine

1. Open the project's Discord in the browser session that is already logged in.
2. Read, newest first: `#announcements`, `#rules`, any `#airdrop` / `#points`
   channel, and recent moderator posts.
3. Compare against what the campaign record currently says:

```bash
haa campaign show <slug>
```

4. Log anything that changed the plan:

```bash
haa campaign log <slug> discord_scan ok \
  --detail "snapshot moved to 2026-09-15; quest season 3 opens Monday"
```

5. Draft (do not send) any reply the operator may want to make.

## What is worth flagging

- Snapshot or deadline dates — **the highest-value signal there is**
- Changes to point multipliers, quest requirements, or eligibility rules
- New seasons or campaigns opening
- Sybil/anti-cheat policy announcements — read these carefully and take them
  at face value
- Security incidents, exploits, or paused contracts
- Team departures or funding news that changes the analyzer's Team rating

## What is not worth flagging

- Price talk, hype, "wen token"
- Rumours with no source
- Anything you would have to speculate to interpret

## Rules

- **Never post automatically.** Draft only.
- Never claim to be someone else, and never misrepresent that a message is
  from a human when an agent wrote it — the operator decides what to send and
  owns it.
- Never share wallet addresses, transaction hashes, or personal details in a
  public channel to "prove" activity.
- Do not use the community channel to ask how to evade a rule.
- If a project's rules forbid the kind of activity being run here, surface that
  plainly to the operator rather than working around it.
