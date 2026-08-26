# Hermes Airdrop Agent

A ready-to-run control plane for [Hermes Agent](https://github.com/NousResearch/hermes-agent)
that screens airdrop opportunities, schedules the daily work, drives a **visible
GUI browser**, and keeps a hash-stamped audit trail of what actually happened.

```bash
./install.sh --dry-run   # see every step first — changes nothing
./install.sh             # install for real
nano .env                # add one API key
haa doctor               # verify
```

**599 tests.** Anything this README claims is enforced by a test that runs the
real code — not a description of it.

---

## Why there is a Python layer under an LLM agent

Hermes drives the browser and calls the model. This package is the boring,
auditable part: scoring, scheduling, storage, evidence, guardrails. Nothing in
`src/` talks to an LLM.

That split is deliberate. A decision that gates weeks of attention, or a claim
that a check-in happened, has to be reproducible from disk without asking a
model what it thinks it did.

| Module | Does |
|---|---|
| `analyzer.py` | The 4-dimension project filter, deterministic |
| `scheduler.py` | Real cron parser + next-run |
| `campaign.py` | Campaign and progress store (atomic JSON writes) |
| `executor.py` | "What is due today" |
| `browser_check.py` | GUI + persistence audit for every worker |
| `hermes_schema.py` | Validates YAML against Hermes' **real** schema |
| `guardrails.py` | Hard stops: keys, CAPTCHA, MFA, approvals, spend limits |
| `wallets.py` | Wallet tier registry — addresses only |
| `evidence.py` | Append-only, hash-stamped ledger |
| `notify.py` | Telegram alerts, secrets redacted |
| `cli.py` | `haa` |

---

## The browser is the product

Airdrop work is essentially all GUI — connect wallet, click claim, approve,
sign, read a quest board. There is no CLI for any of it. Three things have to
be true, and each fails independently:

### 1. Every worker has browser tools

All six configs — main plus `analyzer`, `daily`, `quests`, `discord`,
`monitor` — include `browser` in `toolsets`.

Including **`worker-monitor`**. A monitor that cannot open the page can report
the symptom ("campaign X stalled") but never the cause. Hermes drops a missing
toolset *without erroring*, so this is asserted by tests rather than trusted.

### 2. The browser is actually visible

Camofox always runs on an Xvfb virtual display, but at **1×1 resolution** unless
the VNC plugin is on. Without `ENABLE_VNC=1` it is not merely headless — it is
unwatchable, and nobody can take over for the CAPTCHA the agent halts on.

So `docker-compose.yml` enables the GUI **by default** and puts headless behind
an opt-in profile — the reverse of the usual arrangement.

> ⚠️ **Hermes' `browser.headed` does not make Camofox visible.** It only affects
> Hermes' *local Chromium* fallback. `ENABLE_VNC=1` is what turns the GUI on.
> We set `headed: true` anyway so the fallback path is visible, and the config
> comment says so.

```
docker compose up -d
open http://localhost:6080/vnc.html    # watch, and take over when it halts
```

Set `VNC_PASSWORD`. That port drives a browser logged into your accounts.

### 3. The session persists

Camofox keys its cookie store by `userId`, so persistence needs *both*
`managed_persistence: true` **and** a stable `user_id`. Each worker pins its own
(`haa-worker-daily`, `haa-worker-quests`, …) — one identity per **role**, so
their logins don't collide.

Camofox's default timeouts will drop a session mid-run: 30 min session, 5 min
browser idle, 5 min tab. Compose raises these to 6 h / 1 h / 1 h, and Hermes'
`browser.inactivity_timeout` to 900 s.

### Verify it

```bash
haa browser check            # config audit + live probes
haa browser check --offline  # config audit only
```

```
browser readiness
  main                 browser · camofox · persistent · user_id=haa-worker-main · visible-fallback
  worker-analyzer      browser · camofox · persistent · user_id=haa-worker-analyzer · visible-fallback
  worker-daily         browser · camofox · persistent · user_id=haa-worker-daily · visible-fallback
  worker-discord       browser · camofox · persistent · user_id=haa-worker-discord · visible-fallback
  worker-monitor       browser · camofox · persistent · user_id=haa-worker-monitor · visible-fallback
  worker-quests        browser · camofox · persistent · user_id=haa-worker-quests · visible-fallback
```

Missing browser tools, missing persistence, or a colliding `user_id` are
**errors**; a missing GUI is a warning that names the reason.

Details: [`docs/research/browser.md`](docs/research/browser.md).

---

## Install

```bash
git clone <repo> && cd <repo>/hermes-airdrop-agent
./install.sh --dry-run    # prints all 8 steps, changes nothing
./install.sh
```

Prerequisites: `git`, `curl`, `python3` 3.10+, and Docker (or Node.js). On Linux
also `xz-utils` — Hermes' installer downloads Node as a `.tar.xz`.

| Step | What it does |
|---|---|
| 1 | Checks prerequisites |
| 2 | Installs Hermes → `~/.hermes/` |
| 3 | Starts Camofox **with the GUI on** |
| 4 | Installs `haa` |
| 5 | Copies config, profiles, `SOUL.md`, skills |
| 6 | Creates `.env` — **never overwrites an existing one** |
| 7 | Installs Hermes cron jobs |
| 8 | Runs `haa doctor` |

Idempotent. Re-running repairs a partial install without destroying state.

### Without Docker

`install.sh` falls back to `npx -y @askjo/camofox-browser` with `ENABLE_VNC=1`.
Docker is preferred — it survives reboots via `--restart unless-stopped`.

### Then

```bash
nano .env                              # one model API key is enough
./scripts/start-browser.sh             # starts Camofox, verifies :9377 AND :6080
haa doctor
hermes --profile worker-analyzer
```

---

## Workers

Each profile is a separate Hermes home: its own `config.yaml`, `.env`,
`SOUL.md`, memory, skills and cron jobs.

| Profile | Job | Model | Turns |
|---|---|---|---|
| `worker-analyzer` | Score projects on 4 dimensions | strong | 60 |
| `worker-daily` | 09:00 check-ins | cheap | 30 |
| `worker-quests` | Onboarding + quest sequences | strong | 120 |
| `worker-discord` | Read communities, **draft** replies | mid | 40 |
| `worker-monitor` | Verify, report, alert | mid | 40 |

Identity lives in `SOUL.md`, not in a `system_prompt:` config key — that key
does not exist in Hermes.

```bash
hermes --profile worker-daily
hermes --profile worker-analyzer chat -q "Analyze https://example.org"
```

Note `-q`. Hermes takes a non-interactive prompt as `chat -q "..."`, not as a
bare positional argument.

## Skills

| Skill | Purpose |
|---|---|
| `airdrop-analyzer` | Gather evidence, fill 12 ratings, call the scorer |
| `daily-executor` | Run, verify, screenshot, log — or halt |
| `quest-executor` | Ordered multi-step onboarding with spend gating |
| `discord-engager` | Read and draft; **never auto-post** |
| `portfolio-tracker` | Rollups, staleness detection, ledger verification |
| `wallet-isolation` | Tier separation; no keys, ever |

`tests/test_skills.py` checks each skill's frontmatter **and** that every
`haa ...` command it documents actually exists in the CLI. A skill telling the
agent to run a command that isn't there produces an agent that fails
confidently every morning.

---

## Scheduled jobs

Installed with **Hermes' own cron**, not the system crontab. Hermes jobs run
through the same guardrails as an interactive session — which is what makes
`approvals.cron_mode: deny` enforceable. The system crontab cannot do that.

| Schedule | Job | Profile |
|---|---|---|
| `0 9 * * *` | Daily check-ins | `worker-daily` |
| `0 13 * * *` | Verify the morning run + `haa evidence verify` | `worker-monitor` |
| `0 20 * * 0` | Weekly report | `worker-monitor` |
| `0 11 * * 1` | Discord scan | `worker-discord` |

```bash
hermes cron list
hermes cron run <job_id>
hermes cron pause <job_id>
```

Prompts are self-contained: a cron run has no conversation history.

---

## The project filter

Twelve ratings, each **0–3**, from the "Sniper" checklist in HTX Insights'
*"The Last Time I'll Talk About Backpack…"* (2026-03-23):

- **Team** — insight, execution, integrity. All three required; a `0` zeroes it.
- **Product** — PMF, delivery quality, ownership. Weighted highest.
- **Narrative** — Web3 narrative, Web2 capital alignment, premium.
- **Timing** — FOMO, cost, crowding. **Inverted**: 0 is good.

```bash
haa analyze --project "Foo" --url https://foo.xyz \
  --team-insight 3 --team-execution 3 --team-integrity 3 \
  --product-pmf 3 --product-delivery 3 --product-responsibility 3 \
  --narrative-web3 3 --narrative-web2 2 --narrative-premium 2 \
  --timing-fomo 1 --timing-cost 1 --timing-crowding 1 --save-to
```

Hard vetoes force `SKIP` and cap the score at 4.0, so a report can never read
"9/10 but skipped": unusable delivery, everyone already farming it, operator
hesitation, or high cost during peak FOMO.

A `1` rating is honest — it means "looked, couldn't confirm". Enough of them
push confidence under 0.70, which routes the decision to a human.

Scoring is code, not an LLM. Two runs on the same ratings give the same verdict
forever, so a decision can be audited months later.

---

## Guardrails

| Condition | Behaviour |
|---|---|
| CAPTCHA / Cloudflare challenge | Halt. **Never** solved. |
| MFA / one-time code | Halt. Operator completes it. |
| Wallet signature or approval prompt | Halt. Signing is a human decision. |
| Session expired | Halt. No autonomous re-auth. |
| Private key / mnemonic / keystore detected | Refused — in `.env`, in the ledger, in `wallets add` |
| Spend action (`bridge`, `swap`, `approve`, `transfer`, …) | Always needs approval; **cannot** be pre-approved from config |
| Above `HAA_MAX_SPEND_USD` | Halt |
| Repeated identical tool failures | Hermes' `tool_loop_guardrails` hard-stops |

`approvals.deny` in every config hard-blocks `cast send`, `solana transfer`,
`--private-key`, `mnemonic` and friends — refused even under `mode: off` or
`--yolo`.

The single most important rule, in `daily-executor`: **never log `ok` for an
action you did not verify.** An operation that records successes it did not
confirm is worse than one that does nothing, because the operator keeps
believing it works.

---

## Data

```
data/
├── campaigns/<slug>/
│   ├── info.json          # campaign + analyzer verdict
│   ├── progress.json      # tallies + append-only action log
│   └── screenshots/
├── logs/evidence.jsonl    # hash-stamped audit trail
└── wallets.json           # addresses only, mode 0600
```

Plain JSON, atomic writes. Git-ignored — this is your audit trail; back it up
yourself.

```bash
haa plan                     # what is due today
haa report --days 7          # weekly rollup
haa evidence tail -n 20
haa evidence verify          # re-hash every artifact
```

`haa evidence verify` re-hashes each referenced screenshot. A mismatch means a
proof changed after it was recorded — that leads the report, because the ledger
is the only way to tell "I did this" from "I believe I did this".

---

## Scope and limits

**What this does not do: it does not help you present multiple wallets as
multiple people.**

There is no fingerprint spoofing, no per-wallet proxy assignment, and no timing
jitter aimed at defeating a protocol's clustering. Those exist for one purpose —
to make one operator's wallets look like several unrelated humans so a
fraud-detection system allocates rewards multiple times. A protocol that detects
that is not malfunctioning; it is working.

The brief this project was built from described a "4-layer identity isolation"
model. **Layer 1 is implemented** — wallet tiers, no keys on disk, funding
hygiene, main wallet never touches a dApp. That is ordinary risk management and
worth doing with a single wallet. **Layers 2–4 are not**, because their stated
purpose is evading the counterparty's anti-fraud system.

Practically: getting flagged usually costs the allocation *and* the reputation
of every linked address. If a project says one identity gets one allocation,
running thirty wallets is breaking the rule, not interpreting it cleverly.

Also out of scope: automated Discord posting (violates their ToS and risks the
accounts a campaign depends on — the agent drafts, you send), and solving
CAPTCHAs.

---

## Development

```bash
make dev      # venv + package + tests
make test     # 599 tests
make lint     # shellcheck/bash -n + compileall
```

The test suite runs the real code: it executes `install.sh --dry-run` and
asserts it changes nothing, parses the shipped YAML through the schema
validator, drives `main()` end to end, and checks the Camofox GUI defaults in
`docker-compose.yml`. One test asserts no test run creates files in the repo —
added after `haa init` was caught writing a `.env` into the working tree.

## Troubleshooting

| Symptom | Fix |
|---|---|
| `haa doctor` reports no model key | Placeholders like `sk-xxx` count as unset. Put a real key in `.env`. |
| Browser unreachable | `./scripts/start-browser.sh`, then `docker compose logs camofox` |
| GUI at `:6080` dead | Needs `ENABLE_VNC=1`. `docker compose up -d` sets it; the `headless` profile deliberately doesn't |
| Config edit had no effect | `haa config check` — Hermes ignores unknown keys silently |
| Logins keep expiring | Check `user_id` is set and non-empty, and the Camofox volume persisted |
| `hermes` not found | `export PATH=$HOME/.local/bin:$PATH` |

## Sources

Every claim is traced in [`docs/research/sources.md`](docs/research/sources.md) —
including two URLs from the original brief that return 404 and one that could
not be fetched. Nothing attributed to an unverified source is implemented here.

Schema derivation: [`docs/research/hermes-schema.md`](docs/research/hermes-schema.md).
Browser findings: [`docs/research/browser.md`](docs/research/browser.md).

## License

MIT
