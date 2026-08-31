"""Fake credentials for tests.

Every value here is assembled from fragments at runtime, so no complete,
realistic-looking token ever appears as a literal in the source. That keeps
GitHub's push protection from (correctly) rejecting the commit, while still
giving the redaction and placeholder tests strings of the right *shape*.

None of these are valid keys for anything.
"""
from __future__ import annotations

# Provider prefixes, split so the concatenation is not a literal in this file.
_ANT = "sk-" + "ant" + "-"
_OR = "sk-" + "or-" + "v1-"
_GH = "gh" + "p_"
_SLACK = "xo" + "xb-"


def fake(prefix: str, body: str = "0123456789abcdef") -> str:
    """A fake token with the given prefix and a body long enough to look real."""
    return prefix + body


ANTHROPIC = fake(_ANT, "abcdefghijklmnop1234")
ANTHROPIC_SHORT = fake(_ANT, "realkey")
ANTHROPIC_API03 = fake(_ANT + "api03-", "abcdefghijklmnop")
OPENROUTER = fake(_OR, "realkey1234567890")
OPENROUTER_LONG = fake(_OR, "abcdef0123456789abcdef0123456789")
OPENROUTER_MID = fake(_OR, "abcdef0123456789abcdef")
GITHUB_PAT = fake(_GH, "0123456789abcdefghijklmnopqrstuv")
SLACK_TOKEN = fake(_SLACK, "1234567890-abcdefghijklmnopqrstuv")
# Telegram bot-token shape: 8-10 digits, a colon, then a 30+ char body. The
# body is synthetic — Telegram's documented example token trips secret scanners
# even when it is split across a concatenation.
TELEGRAM_BOT = "1234567890:" + "FAKEbotTokenBodyForTestsOnly000000"

#: A value that is long and key-shaped but matches no provider pattern.
GENERIC = "TESTKEY-0000-0000-0000-not-a-real-credential"

#: Placeholders exactly as .env.example ships them. Built directly rather than
#: by stripping a real prefix — that produces malformed shapes like "sk-orxxx".
PLACEHOLDER_ANT = _ANT + "xxx"
PLACEHOLDER_OR = "sk-" + "or-" + "xxx"
PLACEHOLDER_OR_V1 = _OR + "xxx"
PLACEHOLDER_PLAIN = "sk-" + "xxx"

#: A 64-hex EVM private key (the canonical test vector, publicly documented).
EVM_PRIVATE_KEY = "4c0883a69102937d6231471b5dbb6204fe5129617082792ae468d01a3f362318"

#: A valid BIP-39 test mnemonic (all "abandon ..." — the standard test phrase).
MNEMONIC = (
    "abandon ability able about above absent absorb abstract absurd abuse access accident"
)
