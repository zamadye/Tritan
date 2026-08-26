"""Alerting: redaction before anything leaves the box."""
from __future__ import annotations

import json
import urllib.error
from unittest import mock

import pytest

from fakes import (
    ANTHROPIC,
    ANTHROPIC_API03,
    GITHUB_PAT,
    OPENROUTER_LONG,
    OPENROUTER_MID,
    SLACK_TOKEN,
    TELEGRAM_BOT,
)
from hermes_airdrop.notify import NotifyError, Telegram, build_message, redact_text


class TestRedaction:
    @pytest.mark.parametrize("secret", [
        OPENROUTER_LONG,
        ANTHROPIC_API03,
        GITHUB_PAT,
        SLACK_TOKEN,
        TELEGRAM_BOT,
    ])
    def test_token_shapes_scrubbed(self, secret):
        assert secret not in redact_text(f"failed with {secret}")
        assert "[redacted]" in redact_text(f"failed with {secret}")

    def test_plain_text_untouched(self):
        assert redact_text("campaign loqua halted on captcha") == "campaign loqua halted on captcha"

    def test_empty(self):
        assert redact_text("") == ""
        assert redact_text(None) is None


class TestBuildMessage:
    def test_contains_title(self):
        assert "halted" in build_message(title="Run halted")

    def test_includes_campaign(self):
        assert "campaign: loqua" in build_message(title="X", campaign="loqua")

    def test_includes_fields(self):
        out = build_message(title="X", fields={"action": "check_in"})
        assert "action: check_in" in out

    def test_redacts_secret_named_fields(self):
        out = build_message(title="X", fields={"ANTHROPIC_API_KEY": ANTHROPIC})
        assert "[redacted]" in out
        assert "abcdefghij" not in out

    def test_severity_icons(self):
        assert build_message(title="t", severity="halt").startswith("⛔")
        assert build_message(title="t", severity="warn").startswith("⚠️")
        assert build_message(title="t", severity="ok").startswith("✅")

    def test_unknown_severity_falls_back(self):
        assert build_message(title="t", severity="wat").startswith("ℹ️")

    def test_body_appended(self):
        out = build_message(title="t", body="detail line")
        assert out.rstrip().endswith("detail line")

    def test_scrubs_secrets_embedded_in_body(self):
        out = build_message(title="t", body=f"key was {OPENROUTER_MID}")
        assert OPENROUTER_MID[6:] not in out


class TestTelegramConfigured:
    def test_configured_when_both_present(self):
        assert Telegram(bot_token="123:abc", chat_id="42").configured is True

    def test_not_configured_without_token(self):
        assert Telegram(bot_token="", chat_id="42").configured is False

    def test_placeholder_counts_as_missing(self):
        assert Telegram(bot_token="xxx", chat_id="xxx").configured is False


class TestTelegramSend:
    def test_unconfigured_raises_without_network(self):
        with pytest.raises(NotifyError) as ei:
            Telegram(bot_token="", chat_id="").send("hi")
        assert "not configured" in str(ei.value)

    def _ok_response(self):
        m = mock.MagicMock()
        m.__enter__.return_value.read.return_value = json.dumps(
            {"ok": True, "result": {"message_id": 1}}
        ).encode()
        return m

    def test_success_returns_parsed_json(self):
        t = Telegram(bot_token="123:abc", chat_id="42")
        with mock.patch("urllib.request.urlopen", return_value=self._ok_response()) as m:
            out = t.send("hello")
        assert out["ok"] is True
        assert m.call_args[0][0].full_url.endswith("/sendMessage")

    def test_sends_redacted_text(self):
        t = Telegram(bot_token="123:abc", chat_id="42")
        with mock.patch("urllib.request.urlopen", return_value=self._ok_response()) as m:
            t.send(f"token {OPENROUTER_MID} leaked")
        payload = json.loads(m.call_args[1]["data"] if "data" in m.call_args[1] else m.call_args[0][0].data)
        assert OPENROUTER_MID[len("sk-"):] not in payload["text"]

    def test_http_error_becomes_notify_error(self):
        t = Telegram(bot_token="123:abc", chat_id="42")
        err = urllib.error.HTTPError("u", 401, "Unauthorized", {}, None)
        with mock.patch("urllib.request.urlopen", side_effect=err):
            with pytest.raises(NotifyError) as ei:
                t.send("hi")
        assert "401" in str(ei.value)

    def test_url_error_becomes_notify_error(self):
        t = Telegram(bot_token="123:abc", chat_id="42")
        with mock.patch("urllib.request.urlopen",
                        side_effect=urllib.error.URLError("no route")):
            with pytest.raises(NotifyError):
                t.send("hi")

    def test_timeout_becomes_notify_error(self):
        t = Telegram(bot_token="123:abc", chat_id="42")
        with mock.patch("urllib.request.urlopen", side_effect=TimeoutError()):
            with pytest.raises(NotifyError):
                t.send("hi")


class TestFromEnv:
    def test_builds_from_settings(self):
        from hermes_airdrop.config import Settings

        s = Settings(env={"TELEGRAM_BOT_TOKEN": "123:abc", "TELEGRAM_CHAT_ID": "42"})
        from hermes_airdrop.notify import from_env

        t = from_env(s)
        assert t.configured is True

    def test_placeholder_gives_unconfigured(self):
        from hermes_airdrop.config import Settings
        from hermes_airdrop.notify import from_env

        s = Settings(env={"TELEGRAM_BOT_TOKEN": "xxx", "TELEGRAM_CHAT_ID": "xxx"})
        assert from_env(s).configured is False
