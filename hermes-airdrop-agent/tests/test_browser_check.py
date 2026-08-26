"""Every worker must have a working, visible CDP browser.

Airdrop work is GUI: connect wallet, click claim, approve, sign, read a quest
board. There is no CLI path for any of it, so a worker without a browser is not
degraded — it is useless. These tests pin that requirement down for the
CDP-Chrome-on-host setup.
"""
from __future__ import annotations

import urllib.error
from pathlib import Path
from unittest import mock

import pytest
import yaml

from hermes_airdrop.browser_check import (
    CDP_VERSION_PATH,
    Finding,
    ProbeResult,
    ProfileBrowser,
    _label,
    _looks_like_unresolved,
    audit_all,
    audit_profile,
    inspect_profile,
    probe,
)

ROOT = Path(__file__).resolve().parents[1]
CONFIG_ROOT = ROOT / "config" / "hermes"
PROFILES = sorted((CONFIG_ROOT / "profiles").glob("*/config.yaml"))
ALL_CONFIGS = [CONFIG_ROOT / "config.yaml"] + PROFILES

#: Three layers: orchestrator -> lead -> workers.
WORKERS = [
    "worker-analyzer",
    "worker-daily",
    "worker-discord",
    "worker-lead",
    "worker-monitor",
    "worker-orchestrator",
    "worker-quests",
]


def write_profile(tmp_path: Path, data: dict) -> Path:
    d = tmp_path / "worker-x"
    d.mkdir(parents=True, exist_ok=True)
    p = d / "config.yaml"
    p.write_text(yaml.safe_dump(data))
    return p


GOOD = {
    "toolsets": ["hermes-cli", "browser", "file"],
    "browser": {
        "cdp_url": "http://127.0.0.1:9222",
        "engine": "chrome",
        "backend": "off",
        "headed": True,
        "inactivity_timeout": 900,
        "command_timeout": 90,
        "record_sessions": True,
    },
}


def mutate(**kwargs):
    import copy

    d = copy.deepcopy(GOOD)
    for key, val in kwargs.items():
        section, _, leaf = key.partition("__")
        if leaf:
            d.setdefault(section, {})[leaf] = val
        else:
            d[section] = val
    return d


# ---------------------------------------------------------------------------
# The shipped configuration must satisfy the requirement
# ---------------------------------------------------------------------------


class TestShippedConfigs:
    @pytest.mark.parametrize("path", PROFILES, ids=lambda p: p.parent.name)
    def test_worker_has_browser_toolset(self, path):
        assert inspect_profile(path).has_browser_toolset

    @pytest.mark.parametrize("path", PROFILES, ids=lambda p: p.parent.name)
    def test_worker_points_at_cdp(self, path):
        pb = inspect_profile(path)
        assert pb.cdp_url.startswith("http"), f"{path.parent.name}: cdp_url={pb.cdp_url!r}"

    @pytest.mark.parametrize("path", PROFILES, ids=lambda p: p.parent.name)
    def test_worker_browser_is_visible(self, path):
        """headed is what makes local Chrome open a real window — the operator's
        only way to take over for a CAPTCHA or MFA prompt."""
        assert inspect_profile(path).headed

    @pytest.mark.parametrize("path", PROFILES, ids=lambda p: p.parent.name)
    def test_worker_uses_chrome(self, path):
        assert inspect_profile(path).engine == "chrome"

    @pytest.mark.parametrize("path", PROFILES, ids=lambda p: p.parent.name)
    def test_worker_records_sessions(self, path):
        assert inspect_profile(path).record_sessions

    @pytest.mark.parametrize("path", PROFILES, ids=lambda p: p.parent.name)
    def test_worker_timeout_long_enough_for_dapps(self, path):
        assert inspect_profile(path).inactivity_timeout >= 900

    @pytest.mark.parametrize("path", PROFILES, ids=lambda p: p.parent.name)
    def test_worker_is_config_ready(self, path):
        assert inspect_profile(path).ready

    def test_all_expected_workers_present(self):
        assert [p.parent.name for p in PROFILES] == WORKERS

    def test_three_layer_structure_exists(self):
        """Orchestrator (Telegram) -> lead (per project) -> workers."""
        names = {p.parent.name for p in PROFILES}
        assert "worker-orchestrator" in names
        assert "worker-lead" in names

    def test_delegating_layers_have_the_delegation_toolset(self):
        for layer in ("worker-orchestrator", "worker-lead"):
            pb = inspect_profile(CONFIG_ROOT / "profiles" / layer / "config.yaml")
            assert "delegation" in pb.toolsets, f"{layer} cannot delegate"

    def test_no_camofox_left_in_configs(self):
        for f in ALL_CONFIGS:
            assert "camofox" not in f.read_text().lower().replace(
                "under the old camofox", ""
            ), f"{f} still configures Camofox"

    def test_audit_of_shipped_configs_is_clean(self):
        report = audit_all(CONFIG_ROOT, live=False)
        assert report.ok, "\n".join(str(f) for f in report.errors)
        assert not report.findings

    def test_no_docker_compose_file(self):
        """Chrome runs on the host, so there is no browser container to compose."""
        assert not (ROOT / "docker-compose.yml").exists()


# ---------------------------------------------------------------------------
# The audit must actually reject broken profiles
# ---------------------------------------------------------------------------


class TestAuditRejectsBrokenProfiles:
    def test_clean_profile_passes(self, tmp_path):
        assert audit_profile(inspect_profile(write_profile(tmp_path, GOOD))) == []

    def test_missing_browser_toolset_is_an_error(self, tmp_path):
        pb = inspect_profile(write_profile(tmp_path, mutate(toolsets=["hermes-cli", "file"])))
        assert any("cannot open a page" in f.message for f in audit_profile(pb))

    def test_missing_cdp_url_is_an_error(self, tmp_path):
        pb = inspect_profile(write_profile(tmp_path, mutate(browser__cdp_url="")))
        errs = audit_profile(pb)
        assert any("cdp_url is unset" in f.message for f in errs)
        assert any("start-browser.sh" in f.fix for f in errs)

    def test_unresolved_placeholder_is_an_error(self, tmp_path):
        """Hermes leaves an unset ${VAR} verbatim, which would land here."""
        pb = inspect_profile(write_profile(tmp_path, mutate(browser__cdp_url="${HAA_CDP_URL}")))
        errs = audit_profile(pb)
        assert any("not a URL" in f.message for f in errs)
        assert any("placeholder" in f.fix for f in errs)

    def test_headless_is_an_error_not_a_warning(self, tmp_path):
        """Unlike the Camofox setup, headed genuinely controls local Chrome —
        so a headless config means an unwatchable, un-take-over-able browser."""
        pb = inspect_profile(write_profile(tmp_path, mutate(browser__headed=False)))
        errs = [f for f in audit_profile(pb) if f.level == "error"]
        assert any("headed is off" in f.message for f in errs)
        assert any("take over" in f.message for f in errs)

    def test_short_timeout_is_a_warning(self, tmp_path):
        pb = inspect_profile(write_profile(tmp_path, mutate(browser__inactivity_timeout=60)))
        warns = [f for f in audit_profile(pb) if f.level == "warn"]
        assert any("reaped mid-action" in f.message for f in warns)

    def test_unknown_engine_is_a_warning(self, tmp_path):
        pb = inspect_profile(write_profile(tmp_path, mutate(browser__engine="lightpanda")))
        warns = [f for f in audit_profile(pb) if f.level == "warn"]
        assert any("cannot screenshot" in f.fix for f in warns)

    def test_toolsets_as_comma_string_still_parsed(self, tmp_path):
        pb = inspect_profile(write_profile(tmp_path, mutate(toolsets="browser,file")))
        assert pb.has_browser_toolset

    def test_empty_config_does_not_crash(self, tmp_path):
        pb = inspect_profile(write_profile(tmp_path, {}))
        assert pb.ready is False
        assert audit_profile(pb)


class TestAuditAll:
    def test_reports_every_profile(self):
        names = {pb.name for pb in audit_all(CONFIG_ROOT, live=False).profiles}
        assert names == {"main", *WORKERS}

    def test_main_is_labelled_main(self):
        assert "main" in {pb.name for pb in audit_all(CONFIG_ROOT, live=False).profiles}

    def test_missing_root_reports_error(self, tmp_path):
        report = audit_all(tmp_path / "nothing", live=False)
        assert not report.ok
        assert any("no Hermes config" in f.message for f in report.findings)

    def test_failing_probe_adds_an_error_with_the_chrome_136_hint(self, tmp_path):
        cfg = tmp_path / "config.yaml"
        cfg.write_text(yaml.safe_dump(GOOD))
        with mock.patch("hermes_airdrop.browser_check.probe") as m:
            m.return_value = ProbeResult("http://x", False, "Connection refused")
            report = audit_all(tmp_path, cdp_url="http://127.0.0.1:9222", live=True)
        assert not report.ok
        msg = " ".join(f.message + " " + f.fix for f in report.findings)
        assert "Chrome 136" in msg, "must explain the silent-failure trap"

    def test_disagreeing_cdp_urls_warn(self, tmp_path):
        (tmp_path / "config.yaml").write_text(yaml.safe_dump(GOOD))
        other = mutate(browser__cdp_url="http://127.0.0.1:9333")
        (tmp_path / "profiles" / "a").mkdir(parents=True)
        (tmp_path / "profiles" / "a" / "config.yaml").write_text(yaml.safe_dump(other))
        with mock.patch("hermes_airdrop.browser_check.probe") as m:
            m.return_value = ProbeResult("http://x", True, "HTTP 200")
            report = audit_all(tmp_path, live=True)
        assert any("disagree" in f.message for f in report.findings)

    def test_unresolved_endpoint_short_circuits_before_probing(self, tmp_path):
        cfg = tmp_path / "config.yaml"
        cfg.write_text(yaml.safe_dump(mutate(browser__cdp_url="${MISSING_VAR}")))
        with mock.patch("hermes_airdrop.browser_check.probe") as m:
            report = audit_all(tmp_path, live=True)
        m.assert_not_called()
        assert any("unresolved" in f.message for f in report.findings)

    def test_render_lists_every_worker(self):
        text = audit_all(CONFIG_ROOT, live=False).render()
        for w in WORKERS:
            assert w in text

    def test_render_flags_a_headless_worker(self, tmp_path):
        (tmp_path / "config.yaml").write_text(
            yaml.safe_dump(mutate(browser__headed=False))
        )
        assert "HEADLESS" in audit_all(tmp_path, live=False).render()


class TestProbe:
    def _resp(self, status=200):
        m = mock.MagicMock()
        m.__enter__.return_value.status = status
        return m

    def test_success(self):
        with mock.patch("urllib.request.urlopen", return_value=self._resp()):
            r = probe("http://127.0.0.1:9222", path=CDP_VERSION_PATH)
        assert r.ok and "200" in r.detail

    def test_http_error_still_means_the_server_is_up(self):
        err = urllib.error.HTTPError("u", 404, "Not Found", {}, None)
        with mock.patch("urllib.request.urlopen", side_effect=err):
            assert probe("http://127.0.0.1:9222").ok

    def test_connection_refused(self):
        with mock.patch("urllib.request.urlopen", side_effect=urllib.error.URLError("refused")):
            r = probe("http://127.0.0.1:9222")
        assert not r.ok and "refused" in r.detail

    def test_timeout(self):
        with mock.patch("urllib.request.urlopen", side_effect=TimeoutError()):
            assert not probe("http://127.0.0.1:9222").ok

    def test_path_is_appended(self):
        with mock.patch("urllib.request.urlopen", return_value=self._resp()) as m:
            probe("http://127.0.0.1:9222/", path=CDP_VERSION_PATH)
        assert m.call_args[0][0].full_url.endswith("/json/version")

    def test_str_marks_success_and_failure(self):
        assert str(ProbeResult("http://x", True, "HTTP 200")).startswith("✓")
        assert str(ProbeResult("http://x", False, "refused")).startswith("✗")


class TestHelpers:
    def test_label_main(self):
        assert _label(CONFIG_ROOT / "config.yaml", CONFIG_ROOT) == "main"

    def test_label_profile_uses_parent_dir(self):
        p = CONFIG_ROOT / "profiles" / "worker-lead" / "config.yaml"
        assert _label(p, CONFIG_ROOT) == "worker-lead"

    @pytest.mark.parametrize("v,expected", [
        ("${HAA_CDP_URL}", True),
        ("http://127.0.0.1:${PORT}", True),
        ("http://127.0.0.1:9222", False),
        ("", False),
    ])
    def test_looks_like_unresolved(self, v, expected):
        assert _looks_like_unresolved(v) is expected

    def test_finding_str_with_fix(self):
        s = str(Finding("error", "x", "broken", fix="do this"))
        assert "✗ x: broken" in s and "do this" in s

    def test_finding_str_without_fix(self):
        assert "↳" not in str(Finding("warn", "x", "meh"))
