"""Validation against Hermes' real config schema.

The most important test in this suite: it asserts that the config files this
repo ships are ones Hermes will actually honour, and that the specific
invented keys we know about are rejected.
"""
from __future__ import annotations

from pathlib import Path

import pytest

from hermes_airdrop.hermes_schema import (
    BROWSER_PROVIDERS,
    REASONING_LEVELS,
    VALID_TOOLSETS,
    Issue,
    validate,
    validate_file,
)

ROOT = Path(__file__).resolve().parents[1]
SHIPPED_CONFIGS = sorted((ROOT / "config" / "hermes").rglob("*.yaml"))


class TestShippedConfigs:
    """Every YAML file we ship must pass the schema. If this fails, the repo
    is shipping configuration Hermes will silently ignore."""

    def test_we_ship_at_least_the_main_config(self):
        assert (ROOT / "config" / "hermes" / "config.yaml") in SHIPPED_CONFIGS

    @pytest.mark.parametrize("path", SHIPPED_CONFIGS, ids=lambda p: str(p.relative_to(ROOT)))
    def test_shipped_config_is_schema_valid(self, path):
        report = validate_file(path)
        assert report.ok, "\n".join(str(i) for i in report.errors)


class TestUnknownKeys:
    def test_unknown_top_level_key_is_an_error(self):
        r = validate({"not_a_real_section": {"x": 1}})
        assert not r.ok
        assert r.errors[0].path == "not_a_real_section"

    def test_known_top_level_key_passes(self):
        assert validate({"agent": {"max_turns": 30}}).ok

    def test_unknown_subkey_is_an_error(self):
        r = validate({"memory": {"path": "~/.hermes/memories/"}})
        assert not r.ok
        assert r.errors[0].path == "memory.path"
        assert "Valid keys under 'memory'" in r.errors[0].hint

    def test_unknown_deep_subkey_is_an_error(self):
        r = validate({"browser": {"camofox": {"fingerprint_seed": 1}}})
        assert not r.ok
        assert r.errors[0].path == "browser.camofox.fingerprint_seed"

    def test_real_camofox_subkey_passes(self):
        assert validate({"browser": {"camofox": {"managed_persistence": True}}}).ok

    def test_empty_config_passes(self):
        assert validate({}).ok


class TestKeysFromTheOriginalSpec:
    """These are the exact keys proposed in the task brief. Each assertion
    documents whether Hermes really reads it."""

    @pytest.mark.parametrize("cfg", [
        {"agent": {"max_turns": 90}},
        {"agent": {"reasoning_effort": "high"}},
        {"compression": {"enabled": True, "threshold": 0.50}},
        {"terminal": {"backend": "local", "cwd": "/tmp", "timeout": 180}},
        {"display": {"skin": "default", "tool_progress": "all"}},
        {"browser": {"camofox": {"managed_persistence": True}}},
        {"toolsets": ["hermes-cli", "browser", "terminal", "file"]},
    ])
    def test_valid(self, cfg):
        assert validate(cfg).ok, [str(i) for i in validate(cfg).errors]

    @pytest.mark.parametrize("cfg,bad_path", [
        ({"memory": {"persistence": True}}, "memory.persistence"),
        ({"memory": {"path": "/x"}}, "memory.path"),
        ({"cron": {"enabled": True}}, "cron.enabled"),
        ({"cron": {"jobs_dir": "/x"}}, "cron.jobs_dir"),
        ({"compression": {"summary_model": "x"}}, "compression.summary_model"),
        ({"security": {"never_store_private_keys": True}}, "security.never_store_private_keys"),
        ({"security": {"stop_on_captcha": True}}, "security.stop_on_captcha"),
        ({"security": {"burner_only": True}}, "security.burner_only"),
        ({"security": {"require_approval_for_wallet": True}}, "security.require_approval_for_wallet"),
    ])
    def test_invalid(self, cfg, bad_path):
        r = validate(cfg)
        assert not r.ok
        assert bad_path in {i.path for i in r.errors}


class TestToolsets:
    def test_file_ops_is_not_a_toolset(self):
        r = validate({"toolsets": ["file_ops"]})
        assert not r.ok
        assert r.errors[0].hint == "Did you mean 'file'?"

    def test_comma_string_is_accepted(self):
        assert validate({"toolsets": "browser,terminal"}).ok

    def test_unknown_toolset_without_close_match(self):
        r = validate({"toolsets": ["zzzzqqq"]})
        assert not r.ok
        assert r.errors[0].hint is None

    def test_all_shipped_profiles_use_valid_toolsets(self):
        for p in (ROOT / "config" / "hermes" / "profiles").rglob("config.yaml"):
            from hermes_airdrop.config import load_yaml

            ts = load_yaml(p).get("toolsets", [])
            for name in ts:
                assert name in VALID_TOOLSETS, f"{p.name}: bad toolset {name}"


class TestEnums:
    @pytest.mark.parametrize("bad", ["turbo", "", "HIGH", 5])
    def test_bad_reasoning_effort(self, bad):
        assert not validate({"agent": {"reasoning_effort": bad}}).ok

    @pytest.mark.parametrize("good", sorted(REASONING_LEVELS))
    def test_every_real_level_accepted(self, good):
        assert validate({"agent": {"reasoning_effort": good}}).ok

    @pytest.mark.parametrize("bad", ["chrome", "playwright", "Camofox"])
    def test_bad_browser_provider(self, bad):
        assert not validate({"browser": {"cloud_provider": bad}}).ok

    @pytest.mark.parametrize("good", sorted(BROWSER_PROVIDERS))
    def test_every_real_provider_accepted(self, good):
        assert validate({"browser": {"cloud_provider": good}}).ok

    @pytest.mark.parametrize("bad", [0, 1.5, -0.2, "half"])
    def test_bad_compression_threshold(self, bad):
        assert not validate({"compression": {"threshold": bad}}).ok

    def test_max_turns_must_be_positive_int(self):
        assert not validate({"agent": {"max_turns": 0}}).ok
        assert not validate({"agent": {"max_turns": "30"}}).ok
        assert not validate({"agent": {"max_turns": True}}).ok  # bool is not a count


class TestEnvOnlyKeys:
    def test_camofox_url_belongs_in_env(self):
        r = validate({"browser": {"camofox": {"url": "http://localhost:9377"}}})
        assert not r.ok
        issue = next(i for i in r.errors if i.path == "browser.camofox.url")
        assert "CAMOFOX_URL" in issue.hint

    def test_api_key_belongs_in_env(self):
        r = validate({"model": {"api_key": "sk-abc"}})
        assert any(i.path == "model.api_key" for i in r.errors)


class TestReport:
    def test_issue_str_includes_hint(self):
        s = str(Issue("error", "a.b", "nope", hint="fix it"))
        assert "[ERROR] a.b: nope" in s and "fix it" in s

    def test_issue_str_without_hint(self):
        assert "↳" not in str(Issue("warning", "a", "meh"))

    def test_warnings_do_not_fail_the_report(self):
        r = validate({"agent": {"max_turns": 10}})
        r.issues.append(Issue("warning", "x", "advisory"))
        assert r.ok

    def test_validate_file_missing_file_raises(self):
        from hermes_airdrop.config import ConfigError

        with pytest.raises(ConfigError):
            validate_file(Path("/nonexistent/config.yaml"))
