"""Environment loading, redaction, and leak detection."""
from __future__ import annotations

import pytest

from fakes import (
    ANTHROPIC,
    ANTHROPIC_SHORT,
    EVM_PRIVATE_KEY,
    OPENROUTER,
    OPENROUTER_MID,
    PLACEHOLDER_ANT,
    PLACEHOLDER_OR,
    PLACEHOLDER_OR_V1,
    PLACEHOLDER_PLAIN,
)
from hermes_airdrop.config import (
    PLACEHOLDER_RE,
    SECRET_KEYS,
    Settings,
    expand_env,
    is_placeholder,
    load_yaml,
    parse_env_text,
    redact,
    unresolved_refs,
)


class TestParseEnvText:
    def test_basic_pairs(self):
        assert parse_env_text("A=1\nB=2\n") == {"A": "1", "B": "2"}

    def test_comments_and_blanks_skipped(self):
        assert parse_env_text("# c\n\nA=1\n") == {"A": "1"}

    def test_export_prefix(self):
        assert parse_env_text("export A=1") == {"A": "1"}

    def test_quotes_stripped(self):
        assert parse_env_text('A="x y"\nB=\'z\'') == {"A": "x y", "B": "z"}

    def test_equals_in_value_preserved(self):
        assert parse_env_text("A=x=y") == {"A": "x=y"}

    def test_line_without_equals_skipped(self):
        assert parse_env_text("NOEQUALS\nA=1") == {"A": "1"}

    def test_inline_comment_is_kept(self):
        # .env files do not support trailing comments; don't pretend they do.
        assert parse_env_text("A=1 # not a comment") == {"A": "1 # not a comment"}


class TestPlaceholders:
    @pytest.mark.parametrize("v", ["", "   ", None, PLACEHOLDER_PLAIN, PLACEHOLDER_ANT,
                                 PLACEHOLDER_OR, PLACEHOLDER_OR_V1, "xxx", "xxxx",
                                 "changeme", "<your-key>", "your_key_here"])
    def test_treated_as_unset(self, v):
        assert is_placeholder(v)

    @pytest.mark.parametrize("v", [OPENROUTER, "http://localhost:9377"])
    def test_real_values_accepted(self, v):
        assert not is_placeholder(v)

    @pytest.mark.parametrize("v", ["sk-xxx", "sk-ant-xxx", "sk-or-xxx",
                                   "sk-or-v1-xxx", "sk-proj-xxxx"])
    def test_multi_segment_prefixes_still_count_as_unset(self, v):
        """Regression: a single optional prefix segment matched 'sk-xxx' but
        not 'sk-ant-xxx', so a two-hyphen placeholder read as a real key."""
        assert is_placeholder(v)

    @pytest.mark.parametrize("v", ["sk-orxxx", "antxxx", "axxx"])
    def test_malformed_shapes_are_not_treated_as_placeholders(self, v):
        # No hyphen before the x-run: this is a value, not a placeholder.
        assert not is_placeholder(v)


class TestRedaction:
    def test_non_secret_key_shown_verbatim(self):
        assert redact("CAMOFOX_URL", "http://x:9377") == "http://x:9377"

    def test_secret_shows_only_ends(self):
        out = redact("ANTHROPIC_API_KEY", ANTHROPIC)
        assert out.startswith("sk-a") and out.endswith("1234")
        assert "abcdefghijklmno" not in out

    def test_short_secret_fully_masked(self):
        assert redact("OPENAI_API_KEY", "short") == "*****"

    def test_unset_secret_reads_unset(self):
        assert redact("OPENAI_API_KEY", "") == "<unset>"

    def test_no_secret_key_is_a_plain_name(self):
        for k in SECRET_KEYS:
            assert k.endswith(("_KEY", "_TOKEN")), k

    def test_telegram_bot_token_is_a_secret(self):
        # It drives the whole UI; leaking it lets anyone impersonate the bot.
        assert "TELEGRAM_BOT_TOKEN" in SECRET_KEYS



class TestSettings:
    def test_load_from_file(self, tmp_path):
        p = tmp_path / ".env"
        p.write_text(f"OPENROUTER_API_KEY={OPENROUTER}\nCAMOFOX_URL=http://localhost:9377\n")
        s = Settings.load(p)
        assert s.get("OPENROUTER_API_KEY") == OPENROUTER
        assert s.get("CAMOFOX_URL") == "http://localhost:9377"

    def test_placeholder_counts_as_absent(self):
        s = Settings(env={"OPENROUTER_API_KEY": PLACEHOLDER_OR})
        assert s.get("OPENROUTER_API_KEY") is None
        assert s.has("OPENROUTER_API_KEY") is False

    def test_missing_env_file_is_not_fatal(self, tmp_path):
        s = Settings.load(tmp_path / "nope.env")
        assert s.source is None
        assert s.env == {}

    def test_dump_redacts_secrets(self):
        s = Settings(env={"OPENROUTER_API_KEY": OPENROUTER_MID, "OTHER": "plain"})
        d = s.dump()
        assert d["OTHER"] == "plain"
        assert "abcdefghijklmno" not in d["OPENROUTER_API_KEY"]

    def test_get_secret_refuses_non_secret_key(self):
        from hermes_airdrop.config import ConfigError

        with pytest.raises(ConfigError):
            Settings().get_secret("CAMOFOX_URL")

    def test_model_provider_keys_detects_what_is_set(self):
        s = Settings(env={"ANTHROPIC_API_KEY": ANTHROPIC_SHORT, "OPENROUTER_API_KEY": PLACEHOLDER_OR})
        assert s.model_provider_keys() == ["ANTHROPIC_API_KEY"]


class TestValidation:
    def test_no_model_key_is_a_problem(self):
        problems = Settings(env={}).validate()
        assert any("No usable model API key" in p for p in problems)

    def test_valid_model_key_is_clean(self):
        assert Settings(env={"ANTHROPIC_API_KEY": ANTHROPIC_SHORT}).validate() == []

    def test_telegram_token_without_chat_id(self):
        s = Settings(env={"ANTHROPIC_API_KEY": ANTHROPIC_SHORT, "TELEGRAM_BOT_TOKEN": "123:abc"})
        assert any("TELEGRAM_CHAT_ID" in p for p in s.validate())

    def test_custom_key_without_base_url(self):
        s = Settings(env={"CUSTOM_API_KEY": "k", "CUSTOM_BASE_URL": ""})
        assert any("CUSTOM_BASE_URL" in p for p in s.validate())

    def test_can_skip_model_requirement(self):
        assert Settings(env={}).validate(require_model_key=False) == []


class TestLeakDetection:
    def test_private_key_in_env_is_refused(self):
        key = EVM_PRIVATE_KEY
        s = Settings(env={"ANTHROPIC_API_KEY": ANTHROPIC_SHORT, "MY_WALLET": key})
        problems = s.validate()
        assert any("private key material" in p for p in problems)

    def test_leak_report_names_the_key_not_the_value(self):
        key = EVM_PRIVATE_KEY
        s = Settings(env={"SECRET_THING": key})
        found = s.find_leaked_secrets()
        assert found == ["SECRET_THING"]
        assert key not in " ".join(found)

    def test_clean_env_has_no_leaks(self):
        s = Settings(env={"A": "hello", "B": "https://example.com"})
        assert s.find_leaked_secrets() == []


class TestEnvExpansion:
    def test_simple_reference(self):
        assert expand_env("${CAMOFOX_URL}", {"CAMOFOX_URL": "http://x"}) == "http://x"

    def test_env_prefix_form(self):
        assert expand_env("${env:CAMOFOX_URL}", {"CAMOFOX_URL": "http://x"}) == "http://x"

    def test_multiple_references(self):
        assert expand_env("${H}:${P}", {"H": "a", "P": "b"}) == "a:b"

    def test_unknown_variable_stays_verbatim(self):
        # Matches Hermes: an undefined placeholder is kept, not blanked.
        assert expand_env("${NOPE}", {}) == "${NOPE}"

    def test_nested_structures(self):
        out = expand_env({"a": ["${X}"], "b": {"c": "${Y}"}}, {"X": "1", "Y": "2"})
        assert out == {"a": ["1"], "b": {"c": "2"}}

    def test_unresolved_refs_lists_missing_names(self):
        assert unresolved_refs({"a": "${MISSING}", "b": ["${ALSO}"]}) == ["ALSO", "MISSING"]


class TestLoadYaml:
    def test_missing_file_raises(self):
        from hermes_airdrop.config import ConfigError

        with pytest.raises(ConfigError):
            load_yaml("/no/such.yaml")

    def test_non_mapping_raises(self, tmp_path):
        from hermes_airdrop.config import ConfigError

        p = tmp_path / "x.yaml"
        p.write_text("- a\n- b\n")
        with pytest.raises(ConfigError):
            load_yaml(p)

    def test_empty_file_is_empty_dict(self, tmp_path):
        p = tmp_path / "x.yaml"
        p.write_text("")
        assert load_yaml(p) == {}
