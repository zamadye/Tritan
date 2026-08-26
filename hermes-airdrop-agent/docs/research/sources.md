# Sources — what was verified, and what was not

Everything in this project traces back to a source that was fetched and read on
**2026-08-25**. This file records which ones actually resolved, because two of
the URLs this project was originally briefed against return 404 and one could
not be fetched at all. Anything unverified is marked as such rather than
quietly assumed.

## Verified

| Source | Status | What it established |
|---|---|---|
| [HTX Insights — "The Last Time I'll Talk About Backpack, and Also Discussing My Airdrop Farming Principles"](https://www.htx.com/news/the-last-time-ill-talk-about-backpack-and-also-discussing-my-hCoPXg2r/) (Princess Christine / @0xsexybanana, 2026-03-23) | ✅ fetched in full | The 4-dimension Sniper checklist: Team, Product, Narrative, Timing & Cost. Contrast with the "shotgun" approach. "If you feel hesitant, it's best not to participate." Overcrowded airdrops yield minimal or negative returns. |
| [Steemit — "How I Farm Crypto Airdrops Across 30 Wallets Without Getting Flagged as a Sybil"](https://steemitdev.com/crypto/@emilos232/how-i-farm-crypto-airdrops-across-30-wallets-without-getting-flagged-as-a-sybil) | ✅ fetched (chunk 1 of 2) | The 4-layer model. Layer 1 (wallet tiering) is adopted here as ordinary risk management. Layers 2–4 are **not** implemented — see "Scope and limits" in the README. |
| [Manus docs — Cloud Browser](https://manus.im/docs/features/cloud-browser) | ✅ fetched in full | The "Take Over" pattern: on CAPTCHA / SMS / MFA the agent stops, the human completes it, control returns. Also: no credential storage, isolated per-user environments, data-centre IPs trigger extra verification. |
| [Hermes Agent — Configuration](https://hermes-agent.nousresearch.com/docs/user-guide/configuration) | ✅ fetched (chunk 1 of 26) | `~/.hermes/` layout; `.env` for secrets, `config.yaml` for everything else; `${VAR}` substitution leaves unset placeholders verbatim; `hermes config set` routes values to the right file. |
| [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | ✅ cloned | `DEFAULT_CONFIG` (the real schema), `setup-hermes.sh`, `cli-config.yaml.example`, `website/docs/`, `toolsets.py` registry, `approvals`/`cron`/`security` sections. See [hermes-schema.md](./hermes-schema.md). |
| [browser-use/browser-use](https://github.com/browser-use/browser-use) | ✅ cloned, v0.13.8 | Confirmed as the harness Hermes' default browser mode drives — and that Camofox cannot use it (no CDP endpoint), which is why `browser.backend: "off"`. |
| [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | ✅ cloned | See [browser.md](./browser.md). |
| [`@askjo/camofox-browser`](https://www.npmjs.com/package/@askjo/camofox-browser) on npm | ✅ registry queried, latest `1.14.0` | The npm fallback path in `install.sh`. |
| Hermes install command | ✅ confirmed in `README.md` and `website/docs/getting-started/installation.md` | `curl -fsSL https://hermes-agent.nousresearch.com/install.sh \| bash`; only prerequisite is Git (+ `curl`, `xz-utils` on Linux); `--skip-browser` flag exists. |

## Could not be verified

| Source | Status | Consequence |
|---|---|---|
| `airdropalert.com/guide-to-airdrop-farming-2026-earning-crypto-the-smart-way/` | ❌ **HTTP 200 but the page body is "Oops! We couldn't find the page you were looking for."** | The "focus on 2–3 ecosystems, not 50 networks" and "2026 farming is about long-term consistency" claims could not be confirmed. They are **not** cited anywhere in this repo. |
| `madeonsol.com/solana-airdrop-farming-strategies-whats-still-working-in-2026/` | ❌ **404 — "Oops! This page doesn't exist or has moved."** | The "3–5 protocols, not 20" and "LST stacking" claims could not be confirmed. **Not** cited. |
| `skywork.ai/blog/ai-agent/prompt-engineering-manus-1-5-...` | ⚠️ **fetch failed** (proxy signature error, not a 404) | The "5-block modular prompt structure" could not be confirmed. The analyze → plan → execute → observe loop used in the `SOUL.md` files comes from Manus' own documentation instead, which was fetched successfully. |
| TechCrunch, "Browser Use — one of the tools powering Manus" | ⚠️ not fetched | Not load-bearing: browser-use's role was confirmed directly from the Hermes docs and the cloned repo. |

The two 404s are worth flagging explicitly: the specific guidance attributed to
them (ecosystem count, protocol count, LST stacking) appears nowhere in this
codebase. The strategy this project implements rests on the HTX article, which
resolved and was read end to end.

## Reproducing the checks

```bash
# Repo existence and metadata
for r in NousResearch/hermes-agent browser-use/browser-use \
         jo-inc/camofox-browser daijro/camoufox; do
  gh api "repos/$r" -q '.full_name + "  stars=" + (.stargazers_count|tostring)'
done

# npm package
curl -sS https://registry.npmjs.org/@askjo/camofox-browser | head -c 300

# Hermes' real config schema
git clone --depth 1 https://github.com/NousResearch/hermes-agent /tmp/ha
grep -n 'DEFAULT_CONFIG' /tmp/ha/hermes_cli/config_defaults.py
```

Note that direct `curl` to arbitrary hosts may fail in a sandboxed
environment (`SSL_ERROR_SYSCALL`); GitHub's API and the npm registry were
reachable here, the news sites were not.
