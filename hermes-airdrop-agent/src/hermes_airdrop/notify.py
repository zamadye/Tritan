"""Operator alerting.

Split in two on purpose:

* :func:`build_message` — pure, testable, redacts secrets
* :func:`Telegram.send` — the only part that touches the network

Alerts exist for the cases the guardrails define: a halt, a repeated failure, a
spend-limit breach. They are not a status feed — the ledger is for that.
"""

from __future__ import annotations

import json
import re
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from typing import Any

from .config import SECRET_KEYS, is_placeholder

#: Anything that looks like a bearer token pasted into a log line.
_TOKENISH_RE = re.compile(
    r"(?i)\b(sk-[a-z0-9\-_]{12,}|ghp_[a-z0-9]{20,}|xox[baprs]-[a-z0-9\-]{10,}|"
    r"[0-9]{8,10}:[a-z0-9_\-]{30,})\b"
)


def redact_text(text: str) -> str:
    """Scrub anything token-shaped out of a message before it leaves the box.

    A Telegram alert is an outbound network call containing operator data; if a
    log line happens to carry an API key it must not ride along.
    """
    if not text:
        return text
    return _TOKENISH_RE.sub("[redacted]", text)


def build_message(
    *,
    title: str,
    campaign: str = "",
    body: str = "",
    severity: str = "info",
    fields: dict[str, Any] | None = None,
) -> str:
    """Compose an alert body. Never raises, never includes raw secrets."""
    icon = {"info": "ℹ️", "warn": "⚠️", "halt": "⛔", "ok": "✅"}.get(severity, "ℹ️")
    lines = [f"{icon} {title}"]
    if campaign:
        lines.append(f"campaign: {campaign}")
    for k, v in (fields or {}).items():
        shown = "[redacted]" if k in SECRET_KEYS else str(v)
        lines.append(f"{k}: {shown}")
    if body:
        lines += ["", body]
    return redact_text("\n".join(lines))


@dataclass
class Telegram:
    bot_token: str
    chat_id: str
    timeout: float = 15.0

    @property
    def configured(self) -> bool:
        return not (is_placeholder(self.bot_token) or is_placeholder(self.chat_id))

    def send(self, text: str) -> dict[str, Any]:
        """POST to the Telegram Bot API. Returns the parsed JSON response.

        Raises :class:`NotifyError` on a transport or API failure — callers
        decide whether an undelivered alert is fatal (it usually is not, but it
        must be surfaced, not swallowed).
        """
        if not self.configured:
            raise NotifyError(
                "Telegram is not configured — set TELEGRAM_BOT_TOKEN and "
                "TELEGRAM_CHAT_ID in .env"
            )
        url = f"https://api.telegram.org/bot{self.bot_token}/sendMessage"
        payload = json.dumps(
            {"chat_id": self.chat_id, "text": redact_text(text), "disable_web_page_preview": True}
        ).encode("utf-8")
        req = urllib.request.Request(
            url, data=payload, headers={"Content-Type": "application/json"}, method="POST"
        )
        try:
            with urllib.request.urlopen(req, timeout=self.timeout) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as exc:  # noqa: PERF203
            raise NotifyError(
                f"Telegram API returned {exc.code}: {exc.reason}"
            ) from exc
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
            raise NotifyError(f"Telegram request failed: {exc}") from exc


class NotifyError(Exception):
    pass


def from_env(settings: Any) -> Telegram:
    """Build a :class:`Telegram` from a loaded :class:`~.config.Settings`."""
    return Telegram(
        bot_token=settings.get("TELEGRAM_BOT_TOKEN") or "",
        chat_id=settings.get("TELEGRAM_CHAT_ID") or "",
    )
