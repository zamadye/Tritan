# Hermes config schema — how it was derived

`src/hermes_airdrop/hermes_schema.py` validates our YAML against Hermes Agent's
real configuration schema. This file records where that schema came from and how
to refresh it, because the alternative — guessing key names — fails silently.

## Why this matters

Hermes **ignores unknown config keys without erroring**. A typo, or a plausible
key that does not exist, is simply dropped and the agent runs on a default you
never chose. Nothing breaks at startup. You find out days later when a browser
session behaves oddly and you have no idea which setting was never applied.

## Source of truth

`hermes_cli/config_defaults.py` in [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)
declares `DEFAULT_CONFIG`, a pure-data dict of every setting Hermes knows. The
module's own docstring calls it "Default configuration data for Hermes Agent.
Pure-data leaf module: `DEFAULT_CONFIG` and `OPTIONAL_ENV_VARS`".

`TOP_LEVEL` in `hermes_schema.py` is the union of:

1. the key tree of `DEFAULT_CONFIG` (89 top-level keys),
2. keys documented in `cli-config.yaml.example`,
3. keys documented under `website/docs/` (e.g. `browser.cloud_provider`,
   `session_reset`, `platform_toolsets`).

Enum value sets were read from the same places:

| Setting | Values | Source |
|---|---|---|
| `agent.reasoning_effort` | `none, minimal, low, medium, high, xhigh, max, ultra` | `hermes_cli/cli_commands_mixin.py` |
| `browser.cloud_provider` | `browserbase, browser-use, camofox, nous, firecrawl` | `website/docs/user-guide/features/browser.md` |
| `approvals.mode` | `smart, manual, off` | `website/docs/user-guide/security.md` |
| `approvals.cron_mode` | `deny, approve` | `website/docs/user-guide/security.md` |
| `toolsets` entries | 56 registered names | the registry in `toolsets.py` |

## How to refresh

```bash
git clone --depth 1 https://github.com/NousResearch/hermes-agent /tmp/ha
cd /tmp/ha && python3 - <<'PY'
import ast
tree = ast.parse(open('hermes_cli/config_defaults.py').read())

def walk(node):
    if not isinstance(node, ast.Dict):
        return None
    out = {}
    for k, v in zip(node.keys, node.values):
        key = k.value if isinstance(k, ast.Constant) else None
        if key is None:
            continue
        out[key] = walk(v) if isinstance(v, ast.Dict) else True
    return out

for n in tree.body:
    if isinstance(n, ast.Assign) and any(
        isinstance(t, ast.Name) and t.id == "DEFAULT_CONFIG" for t in n.targets
    ):
        cfg = walk(n.value)

print(sorted(cfg))
for s in ("browser", "security", "cron", "memory", "agent"):
    print(s, sorted(cfg[s]) if isinstance(cfg.get(s), dict) else cfg.get(s))
PY
```

`ast.literal_eval` fails on `DEFAULT_CONFIG` — it contains a string
concatenation — which is why the walker above collects keys structurally
instead of evaluating the dict.

## Corrections this caught

Keys proposed for this project that Hermes does **not** read. Each would have
been silently ignored:

| Proposed | Reality |
|---|---|
| `browser.camofox.url` | `CAMOFOX_URL` in `.env`. No config key exists. |
| `memory.path` | No such key. Memory lives at `~/.hermes/memories/`. |
| `memory.persistence` | Not a key. `memory.memory_enabled` is. |
| `cron.enabled` | Not a key. Jobs live in `~/.hermes/cron/jobs.json`. |
| `cron.jobs_dir` | Not a key. |
| `compression.summary_model` | Not a key. `cron.model` pins the cron fleet's model. |
| `security.never_store_private_keys` | Not a key. Enforced by our own code instead. |
| `security.stop_on_captcha` | Not a key. Enforced by our guardrails + skill instructions. |
| `security.burner_only` | Not a key. Enforced by the wallet-tier registry. |
| `security.require_approval_for_wallet` | Not a key. `approvals.mode` and `approvals.deny` are the real mechanism. |
| `toolsets: [..., file_ops]` | `file_ops` is not registered. The name is `file`. |
| `model.default: claude-sonnet-4-5` | Hermes wants `<provider>/<model>` slugs. |
| `system_prompt:` in a profile YAML | Not a key. Profile identity lives in `SOUL.md`. |

Keys that were proposed and **are** real — worth recording so they are not
"fixed" by mistake:

- `browser.camofox.managed_persistence`
- `agent.max_turns`, `agent.reasoning_effort`
- `compression.enabled`, `compression.threshold`
- `toolsets` (top-level list), `security` (section), `cron` (section)
- `display.skin`, `terminal.backend`

## Directory layout (confirmed)

From the official configuration docs:

```
~/.hermes/
├── config.yaml     # non-secret settings
├── .env            # API keys and secrets
├── auth.json       # OAuth provider credentials
├── SOUL.md         # primary agent identity (slot #1 in the system prompt)
├── memories/       # MEMORY.md, USER.md
├── skills/         # agent-created and installed skills
├── cron/           # scheduled jobs (jobs.json)
├── sessions/
└── logs/           # secrets auto-redacted
```

Profiles are **separate Hermes homes**, not sections of one config:

```
~/.hermes/profiles/<name>/
├── config.yaml
├── .env
├── SOUL.md
├── memories/
├── skills/
└── cron/
```

Created with `hermes profile create <name>` (add `--clone` to copy config,
`.env`, `SOUL.md` and skills). Selected with `hermes --profile <name>` or `-p`.

## CLI syntax (confirmed)

| Task | Command |
|---|---|
| Non-interactive query | `hermes chat -q "..."` (not a bare positional prompt) |
| Prompt from a file | `hermes chat --query-file prompt.txt` |
| Preload skills | `hermes chat -s skill-a,skill-b -q "..."` |
| Choose toolsets | `hermes chat --toolsets "web,terminal,skills"` |
| Create a job | `hermes cron create "0 9 * * *" "<prompt>" --name X --skill Y` |
| Manage jobs | `hermes cron list \| edit \| pause \| resume \| run \| remove` |
| Check config | `hermes config check` |

Cron is **not** the system crontab. Hermes jobs run through the same guardrails
as an interactive session, which is why `approvals.cron_mode: deny` matters —
the system crontab cannot enforce it.
