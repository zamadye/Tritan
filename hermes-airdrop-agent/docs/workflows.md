# Workflows

How a task actually travels from your Telegram message to a completed action,
and what each agent does while it holds the work.

Everything here maps onto real Hermes mechanisms — verified against
`website/docs/user-guide/features/kanban.md`, `multi-profile-gateways.md`, and
the `kanban` / `delegation` toolsets in `toolsets.py`. Nothing is invented.

---

## The one-paragraph version

You message one Telegram bot. The **orchestrator** reads it, works out what the
project actually wants, and files the work onto a **kanban board** as tasks
assigned to specific profiles. Hermes' **dispatcher** (running inside the
gateway, ticking every 60s) picks up each task when its parents are done and
spawns the assigned profile. The **lead** turns a project into ordered steps;
the **workers** execute one verified step at a time. Anything that needs you
comes back to the same Telegram thread.

---

## The transport: two real mechanisms

| Mechanism | What it is | When it is used |
|---|---|---|
| **`delegation`** (`delegate_task`) | Spawns a subagent with isolated context, in-process | Small, quick subtasks — "read this page and tell me what it asks for" |
| **`kanban`** | A durable task board: rows with an assignee, status, parents, and structured handoffs | Anything that outlives one turn, needs sequencing, or might need a human |

Kanban is the backbone. `delegate_task` is for the small stuff.

Task statuses, verbatim from the Hermes docs:

```
triage → todo → ready → running → blocked → review → done → archived
```

- `blocked` with `kind=dependency` waits in `todo` and **auto-resumes** when the
  parent finishes.
- `blocked` with `kind=needs_input`, `capability`, or `transient` **surfaces to
  a human** — that is how a CAPTCHA, a signature, or a missing extension
  install reaches you.

---

## End to end

```
  You (Telegram)
      │  "🔈 MemeBitcoin Airdrop  ➖ Register ... ➖ Connect Twitter ..."
      ▼
 ┌─────────────────────────────────────────────────────────────┐
 │ worker-orchestrator            (layer 1, one Telegram bot)  │
 │  1. parse: project, URL, referral code, task list           │
 │  2. haa campaign list — do we already know this project?    │
 │  3. new?  → file a screening task, assign worker-analyzer   │
 │  4. known? → file the work, assign worker-lead              │
 │  5. reply to you: what it understood, what it is doing      │
 └─────────────────────────────────────────────────────────────┘
      │ kanban_create(assignee=..., parents=..., skills=...)
      ▼
 ┌─────────────────────────────────────────────────────────────┐
 │ worker-analyzer              (layer 3, screening)           │
 │  scores Team / Product / Narrative / Timing → verdict       │
 │  SKIP → kanban_complete(summary=…) and the thread ends      │
 │  PRIORITIZE / CONSIDER → parent task unblocks               │
 └─────────────────────────────────────────────────────────────┘
      │
      ▼
 ┌─────────────────────────────────────────────────────────────┐
 │ worker-lead                  (layer 2, one per project)     │
 │  reads the project's OWN task list in the browser           │
 │  writes it into haa as ordered actions + dependencies       │
 │  files one kanban task per dApp, assigned to a worker       │
 └─────────────────────────────────────────────────────────────┘
      │ kanban_create × N  (grouped per dApp)
      ▼
 ┌─────────────────────────────────────────────────────────────┐
 │ workers                     (layer 3)                       │
 │  quests   onboarding sequences                              │
 │  daily    recurring check-ins                               │
 │  discord  community scan                                    │
 │  monitor  verification + reporting                          │
 └─────────────────────────────────────────────────────────────┘
      │ kanban_complete(summary=…, metadata=…)
      ▼
  auto_subscribe_on_create → the orchestrator is notified → replies to you
```

---

## Each agent's workflow

### worker-orchestrator — the front door

**Trigger:** a Telegram message, or a cron tick at 08:30.

```
1. PREFLIGHT      haa browser check        → stop if Chrome is down
2. PARSE          extract project, URL, referral code, task list
3. LOOK UP        haa campaign list
4. BRANCH
     unknown  → kanban_create(screening, assignee=worker-analyzer)
                then wait for the verdict
     known    → check the stored verdict
                  SKIP  → tell the operator, stop
                  else  → kanban_create(plan, assignee=worker-lead)
5. REPLY          what it understood, what it filed, what needs you
6. ON COMPLETION  relay the worker's summary back to the thread
```

**Never:** touches a dApp itself, signs anything, or files work for a project
nobody has screened.

### worker-analyzer — the gate

**Trigger:** a kanban task assigned to it.

```
1. kanban_show                      read the task and its context
2. open the product and USE it      browser, not docs
3. read 20+ founder posts
4. haa analyze --project … --save-to
5. kanban_complete(summary=verdict, metadata={score, decision})
```

**Output:** `PRIORITIZE` / `CONSIDER` / `SKIP` with a score and a reason.
A `SKIP` ends the thread — that is a successful outcome, not a failure.

### worker-lead — one project, end to end

**Trigger:** a kanban task assigned to it, after screening passes.

```
1. kanban_show
2. READ THE SITE'S OWN TASK LIST — quote it verbatim
     (the announcement is often already stale)
3. DECOMPOSE into haa actions
     haa campaign add-action <slug> "name@once" \
         --tier … --network … --group <dapp> --depends-on …
     outcome names only — never a selector or a click path
4. MODEL THE GATES
     prerequisites outside the campaign (faucet conditions, balances)
     become actions too, so the planner can refuse the rest
5. LONG-HORIZON COMMITMENTS
     haa positions add … --until <date>     (LP 30 days, badge expiry)
     haa positions streak …                 (30-day streaks)
6. FILE ONE KANBAN TASK PER GROUP
     kanban_create(title, assignee=worker-quests|worker-daily, parents=[…])
7. kanban_complete(summary=the plan, metadata={actions: N, groups: […]})
```

**Never:** writes a selector, an XPath, or a click sequence into a campaign
record. If it feels the urge to specify *how*, the *what* is not stated clearly
enough.

### worker-quests / worker-daily — the hands

**Trigger:** a kanban task assigned to them.

```
1. kanban_show                       what am I being asked to do
2. haa browser check                 is Chrome reachable
3. haa plan / haa campaign show      what is runnable, what is blocked
4. FOR EACH RUNNABLE ACTION
     browser_snapshot  → find the elements (never a stored selector)
     browser_vision    → when the tree is ambiguous
     act
     re-snapshot, VERIFY against the site's own feedback
     screenshot
     haa campaign log <slug> <action> ok|failed|halted
     kanban_heartbeat               during anything long
5. STOP CONDITIONS → kanban_block(kind=…)
     CAPTCHA / MFA / signature   → needs_input   (surfaces to you)
     needs an extension installed → capability    (surfaces to you)
     waiting on a parent action   → dependency    (auto-resumes)
     site down, rate limited      → transient     (surfaces to you)
6. kanban_complete(summary=…, metadata={done: […], evidence: […]})
```

**Never:** logs `ok` without verification. That single rule is what keeps the
whole ledger trustworthy.

### worker-discord — the ears

**Trigger:** cron, Monday 11:00.

```
1. haa campaign list
2. read #announcements, #rules, #airdrop/#points — newest first
3. haa campaign show <slug>   compare against what we recorded
4. haa campaign log <slug> discord_scan ok --detail "<what changed>"
5. DRAFT replies. Never post.
```

### worker-monitor — the conscience

**Trigger:** cron, 13:00 daily and 20:00 Sunday.

```
1. haa plan + haa evidence tail
2. haa evidence verify          re-hash every proof; lead with any mismatch
3. haa positions list           what is expiring, what streak is at risk
4. haa report --days 7
5. flag: zero streaks on active campaigns, failure_rate > 0.3,
         verdict SKIP still active, past-due positions
```

---

## What reaches you, and when

| Situation | How it arrives |
|---|---|
| Screening verdict | Telegram reply from the orchestrator |
| A step needs a signature | `kanban_block(kind=needs_input)` → Telegram |
| An extension must be installed | `kanban_block(kind=capability)` → Telegram |
| A CAPTCHA or MFA prompt | `kanban_block(kind=needs_input)` → Telegram |
| Spend above `HAA_MAX_SPEND_USD` | `kanban_block(kind=needs_input)` → Telegram |
| A position about to expire | `haa positions list` → daily report |
| A streak about to break | `haa positions list` → daily report |
| A week summary | cron, Sunday 20:00 |

Everything else runs without bothering you.

---

## Running it

Each profile is its own gateway service. You only need the orchestrator's
Telegram bot — the rest are spawned by the dispatcher.

```bash
hermes --profile worker-orchestrator gateway install
hermes --profile worker-orchestrator gateway start
```

The dispatcher runs **inside** that gateway (`kanban.dispatch_in_gateway: true`,
the default) and ticks every 60 seconds, spawning whichever profile a ready
task is assigned to. You do not start the workers yourself.

To watch the board:

```bash
hermes kanban list
hermes kanban show <task-id>
```

---

## Cost shape

Hermes' own kanban docs call this the *"frontier orchestrator, inexpensive
workers"* pattern, which is exactly the split here:

| Profile | Model | Why |
|---|---|---|
| orchestrator | strong | it decides what everyone else does |
| lead | strong | it interprets an unfamiliar UI into a plan |
| analyzer | strong | one decision gates weeks of work |
| quests | mid | follows a plan the lead already made |
| daily | cheap | the same verified loop, every day |
| discord / monitor | cheap | read and report |
