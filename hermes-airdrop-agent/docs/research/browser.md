# Browser layer — research notes

> ## ⚠️ SUPERSEDED — read this first
>
> This file records research done for the **Camofox** setup. On 2026-08-25 the
> project pivoted to **Chrome via CDP on the host** (decision D8 in
> `AGENTS.md`), so the configuration guidance below no longer applies.
>
> Still true and worth keeping:
>
> - **Camofox runs on Xvfb at 1×1 unless `ENABLE_VNC=1`.** Verified from the
>   `jo-inc/camofox-browser` source. Anyone revisiting an anti-detect browser
>   needs this — "headless" there means *unwatchable*, not merely windowless.
> - **Hermes' `browser.headed` only affects its local Chromium fallback.** It
>   never reaches a separate browser server. Still true, and now load-bearing
>   in the other direction: for local Chrome it *does* open the real window.
> - **Camofox default timeouts** (30 min session / 5 min browser idle) are far
>   too short for a campaign run. General lesson: check a browser server's
>   idle defaults before trusting session persistence.
>
> For the current setup read instead:
>
> - `README.md` § "Browser: Chrome asli via CDP"
> - `scripts/start-browser.sh` — including the Chrome 136+ silent-failure trap
> - `AGENTS.md` § 4a — that trap, quoted and explained
>
> The rest of this file is preserved as a research record, not as guidance.

Airdrop work is essentially all GUI: connect wallet, click claim, approve a
transaction, sign, read a quest board, scroll Discord. There is no CLI for any
of it. So "does this worker have a visible, persistent browser?" is the
precondition for the whole system.

Three independent things must be true, and each fails on its own. This file
records what was verified about each, from the
[jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) source and
the Hermes docs.

---

## 1. The worker must have browser tools at all

`toolsets` must include `browser`. Hermes drops an unregistered or missing
toolset **without erroring**, so this is easy to lose in an edit and hard to
notice — the agent just never offers a browser tool.

Every profile in `config/hermes/profiles/` includes it, including
`worker-monitor`. A monitor that cannot open the page can only report the
symptom ("campaign X stalled"), never the cause.

Checked by `haa browser check` and by `tests/test_browser_check.py`.

---

## 2. The browser must be *visible*

This is the part that is easy to get wrong.

### Camofox runs on a virtual display at 1×1 by default

From the camofox-browser `Dockerfile`:

```
# Xvfb virtual display -- runs Camoufox as if on a real desktop (better anti-detection)
xvfb \
```

And from `plugins/vnc/README.md`:

> The plugin overrides Camoufox's default **1x1 virtual display** with a
> human-usable resolution, then runs a watcher process that detects the Xvfb
> display and attaches x11vnc + noVNC.

So the browser is always on a display — but at 1×1 unless the VNC plugin is
enabled. Without it the browser is not merely headless, it is **unwatchable**.
Nobody can see the page, and nobody can take over.

### `ENABLE_VNC=1` is what turns the GUI on

```
Camoufox (Xvfb :99, 1920x1080)
    ↑
x11vnc (attaches to :99, port 5900)
    ↑
noVNC / websockify (port 6080)
    ↑
Your browser → http://localhost:6080/vnc.html
```

Its stated purpose, verbatim:

> Interactive browser access via VNC. Log into sites visually, **solve
> CAPTCHAs, approve OAuth prompts** — then export the authenticated storage
> state for reuse by your agent.

That is exactly the "Take Over" step the guardrails depend on. This is why
`docker-compose.yml` enables VNC **by default** and puts headless behind an
opt-in `headless` profile — the reverse of the usual arrangement.

Relevant variables: `ENABLE_VNC`, `VNC_RESOLUTION` (default `1920x1080`),
`VNC_BIND`, `NOVNC_PORT` (default `6080`), `VNC_PASSWORD`.

### `CAMOFOX_INTERACTIVE=desktop` is the other option, and usually the wrong one

> `CAMOFOX_INTERACTIVE` — Interactive browser mode: `desktop` opens a real local
> Camoufox window; `off` keeps normal headless behavior.
>
> This mode is intended for a person using the same machine; **it does not
> expose a remote browser-control service.**

Useful on a laptop with a desktop session. Useless on a server or in a
container, which is the normal deployment for this project.

### Hermes' `browser.headed` does *not* make Camofox visible

From `hermes_cli/config_defaults.py`:

```python
"headed": False,  # Local mode: launch Chromium with a visible window (also
                  # skips per-turn cleanup so the window persists between
                  # turns; idle reaper still applies)
```

It reads `config["browser"]["headed"]` with an `AGENT_BROWSER_HEADED` env
fallback, and it applies to **Hermes' local Chromium** path (`agent-browser`).
Camofox is a separate server that Hermes talks to over HTTP; the flag never
reaches it.

We still set `headed: true` so the fallback path is visible rather than silent,
and the config comment says plainly that `ENABLE_VNC` is what matters for
Camofox. Getting this backwards produces a system that looks configured for GUI
and isn't.

---

## 3. The session must persist

From the camofox-browser README:

> By default, camofox persists each user's cookies and localStorage to
> `~/.camofox/profiles/`. Sessions survive browser restarts — log in once (via
> cookies or VNC), and subsequent sessions restore the authenticated state
> automatically.
>
> ```
> └── profiles/         # Persisted session state (auto-managed)
>     └── <hashed-userId>/
> ```
>
> Override the directory with `CAMOFOX_PROFILE_DIR`.

**Keyed by `userId`.** So persistence needs *both*:

- `browser.camofox.managed_persistence: true` — Hermes sends a stable
  profile-scoped userId instead of a random one
- a non-empty `browser.camofox.user_id` — otherwise the "stable" id has
  nothing to be stable *as*

Each worker pins its own id (`haa-worker-daily`, `haa-worker-quests`, …) so
their cookie jars don't collide. One identity per **role**, not per wallet —
`tests/test_browser_check.py::test_user_ids_are_unique` enforces the
uniqueness, and `audit_user_id_collisions` reports a shared id as an error.

### Timeouts: the defaults will drop your session mid-run

| Variable | Default | Our value | Why |
|---|---|---|---|
| `SESSION_TIMEOUT_MS` | `1800000` (30 min) | `21600000` (6 h) | A campaign run across several dApps outlasts 30 min |
| `BROWSER_IDLE_TIMEOUT_MS` | `300000` (5 min) | `3600000` (1 h) | Otherwise the browser is reaped between two actions |
| `TAB_INACTIVITY_MS` | `300000` (5 min) | `3600000` (1 h) | A tab closed mid-flow loses page state |
| `MAX_OLD_SPACE_SIZE` | `128` MB | `2048` MB | dApp front-ends are heavy; a Node OOM presents as an inexplicable browser failure |

From the README: *"Sessions auto-expire after 30 minutes of inactivity. The
browser itself shuts down after 5 minutes with no active sessions, and
relaunches on the next request."* Left at defaults, a run that pauses to think
for six minutes comes back to a cold browser.

### Hermes-side timeout

`browser.inactivity_timeout` is raised to `900` in every profile (default 120).
At 120s, Hermes closes an idle session while a slow claim page is still
loading. `haa browser check` warns below 300.

---

## What this means operationally

```
docker compose up -d              # GUI on by default
open http://localhost:6080/vnc.html   # watch, and take over when it halts
haa browser check                 # verify all of the above
```

`haa browser check` audits the config offline and, with `--url`/network, probes
both `:9377` (control API) and `:6080/vnc.html` (GUI). A missing GUI is
reported as a warning with the reason spelled out, not left to be discovered at
09:00 when the daily run halts on a CAPTCHA nobody can see.
