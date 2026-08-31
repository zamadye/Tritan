"""Hermes Airdrop Agent — backend runtime.

A deterministic, testable control plane that sits *underneath* Hermes Agent.

Hermes (https://github.com/NousResearch/hermes-agent) is the LLM agent: it
drives the browser, calls the model, runs tools. This package is the boring,
auditable layer around it:

  * ``config``        — loads .env / config.yaml, refuses to leak secrets
  * ``hermes_schema`` — validates our YAML against Hermes' *real* config schema
  * ``analyzer``      — the 4-dimension project filter (Team/Product/Narrative/Timing)
  * ``campaign``      — campaign + progress store on disk (JSON)
  * ``scheduler``     — cron expression parsing and next-run computation
  * ``executor``      — turns campaigns + schedule into today's work plan
  * ``wallets``       — wallet tier registry (addresses only, never keys)
  * ``guardrails``    — hard stops: private keys, CAPTCHA, unapproved txns
  * ``evidence``      — hash-stamped audit trail for every action
  * ``notify``        — Telegram alerting

Nothing in here talks to an LLM. That is deliberate: every decision that moves
money or claims a reward must be reproducible from disk without a model call.
"""

__version__ = "0.1.0"

__all__ = [
    "analyzer",
    "campaign",
    "config",
    "evidence",
    "executor",
    "guardrails",
    "hermes_schema",
    "notify",
    "scheduler",
    "wallets",
]
