"""Every worker must have a working, visible, persistent GUI browser.

Airdrop work is GUI: connect wallet, click claim, approve, sign, read a quest
board. There is no CLI path for any of it, so a worker without a browser is not
degraded — it is useless. These tests pin that requirement down.
"""
from __future__ import annotations

import urllib.error
from pathlib import Path
from unittest import mock

import pytest
import yaml

from hermes_airdrop.browser_check import (
    Finding,
    NOVNC_PATH,
    ProfileBrowser,
    _guess_novnc,
    _label,
    audit_all,
    audit_profile,
    audit_user_id_collisions,
    inspect_profile,
    probe,
)

ROOT = Path(__file__).resolve().parents[1]
CONFIG_ROOT = ROOT / "config" / "hermes"
PROFILES = sorted((CONFIG_ROOT / "profiles").glob("*/config.yaml"))
ALL_CONFIGS = [CONFIG_ROOT / "config.yaml"] + PROFILES

WORKERS = ["worker-analyzer", "worker-daily", "worker-discord", "worker-monitor", "worker-quests"]


def write_profile(tmp_path: Path, data: dict) -> Path:
    d = tmp_path / "worker-x"
    d.mkdir(parents=True, exist_ok=True)
    p = d / "config.yaml"
    p.write_text(yaml.safe_dump(data))
    return p


GOOD = {
    "toolsets": ["hermes-cli", "browser", "file"],
    "browser": {
        "cloud_provider": "camofox",
        "backend": "off",
        "headed": True,
        "inactivity_timeout": 900,
        "camofox": {
            "managed_persistence": True,
            "user_id": "haa-worker-daily",
            "adopt_existing_tab": True,
        },
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
    def test_worker_uses_camofox(self, path):
        assert inspect_profile(path).cloud_provider == "camofox"

    @pytest.mark.parametrize("path", PROFILES, ids=lambda p: p.parent.name)
    def test_worker_session_is_persistent(self, path):
        """Persistence needs BOTH managed_persistence and a stable user_id."""
        pb = inspect_profile(path)
        assert pb.managed_persistence, "managed_persistence is off"
        assert pb.user_id, "user_id is empty — profile would be random per session"
        assert pb.persistent

    @pytest.mark.parametrize("path", PROFILES, ids=lambda p: p.parent.name)
    def test_worker_visible_fallback(self, path):
        assert inspect_profile(path).headed

    @pytest.mark.parametrize("path", PROFILES, ids=lambda p: p.parent.name)
    def test_worker_records_sessions(self, path):
        assert inspect_profile(path).record_sessions

    @pytest.mark.parametrize("path", PROFILES, ids=lambda p: p.parent.name)
    def test_worker_timeout_long_enough_for_dapps(self, path):
        assert inspect_profile(path).inactivity_timeout >= 900

    def test_every_expected_worker_present(self):
        assert [p.parent.name for p in PROFILES] == WORKERS

    def test_user_ids_are_unique(self):
        ids = [inspect_profile(p).user_id for p in ALL_CONFIGS]
        assert len(ids) == len(set(ids)), f"colliding user_ids: {ids}"

    def test_user_ids_are_stable_strings(self):
        """An unresolved ${VAR} would silently become a per-install identity."""
        for p in ALL_CONFIGS:
            uid = inspect_profile(p).user_id
            assert uid.startswith("haa-worker-"), uid
            assert "$" not in uid and "{" not in uid

    def test_audit_of_shipped_configs_is_clean(self):
        report = audit_all(CONFIG_ROOT, live=False)
        assert report.ok, "\n".join(str(f) for f in report.errors)
        assert not report.findings

    def test_main_config_also_has_browser(self):
        assert inspect_profile(CONFIG_ROOT / "config.yaml").has_browser_toolset


class TestComposeDefaults:
    """The GUI must be on by default, not behind an opt-in profile."""

    @pytest.fixture
    def compose(self):
        return yaml.safe_load((ROOT / "docker-compose.yml").read_text(encoding="utf-8"))

    def test_default_service_enables_vnc(self, compose):
        env = compose["services"]["camofox"]["environment"]
        assert str(env["ENABLE_VNC"]) == "1"

    def test_default_service_exposes_novnc_port(self, compose):
        ports = compose["services"]["camofox"]["ports"]
        assert any("6080" in str(p) for p in ports)

    def test_default_service_exposes_native_vnc(self, compose):
        ports = compose["services"]["camofox"]["ports"]
        assert any(":5900" in str(p) for p in ports)

    def test_vnc_is_not_behind_a_profile(self, compose):
        """If the GUI service had `profiles:`, plain `up -d` would skip it."""
        assert "profiles" not in compose["services"]["camofox"]

    def test_headless_is_the_opt_in(self, compose):
        assert compose["services"]["camofox-headless"]["profiles"] == ["headless"]

    def test_resolution_is_human_usable(self, compose):
        env = compose["services"]["camofox"]["environment"]
        assert env["VNC_RESOLUTION"] == "1920x1080"

    def test_session_timeouts_raised_for_sustained_runs(self, compose):
        """Defaults are 30 min session / 5 min browser idle — far too short."""
        env = compose["services"]["camofox"]["environment"]
        assert int(env["SESSION_TIMEOUT_MS"]) >= 3600000
        assert int(env["BROWSER_IDLE_TIMEOUT_MS"]) >= 1800000

    def test_profile_dir_is_persisted_on_a_volume(self, compose):
        svc = compose["services"]["camofox"]
        assert any("/root/.camofox" in str(v) for v in svc["volumes"])
        assert "camofox-data" in compose["volumes"]

    def test_vnc_password_is_configurable(self, compose):
        env = compose["services"]["camofox"]["environment"]
        assert "VNC_PASSWORD" in env

    def test_headless_service_has_no_vnc(self, compose):
        env = compose["services"]["camofox-headless"]["environment"]
        assert "ENABLE_VNC" not in env


# ---------------------------------------------------------------------------
# The audit must actually reject broken profiles
# ---------------------------------------------------------------------------


class TestAuditRejectsBrokenProfiles:
    def test_clean_profile_passes(self, tmp_path):
        assert audit_profile(inspect_profile(write_profile(tmp_path, GOOD))) == []

    def test_missing_browser_toolset_is_an_error(self, tmp_path):
        pb = inspect_profile(write_profile(tmp_path, mutate(toolsets=["hermes-cli", "file"])))
        errs = [f for f in audit_profile(pb) if f.level == "error"]
        assert any("cannot open a page" in f.message for f in errs)

    def test_missing_cloud_provider_is_an_error(self, tmp_path):
        pb = inspect_profile(write_profile(tmp_path, mutate(browser__cloud_provider="")))
        assert any("no browser backend" in f.message for f in audit_profile(pb))

    def test_persistence_off_is_an_error(self, tmp_path):
        pb = inspect_profile(
            write_profile(tmp_path, mutate(browser__camofox={"user_id": "x"}))
        )
        assert any("starts logged out" in f.message for f in audit_profile(pb))

    def test_persistence_without_user_id_is_an_error(self, tmp_path):
        """managed_persistence alone is not enough — Camofox keys the profile
        store by userId, so an empty id means a random one every session."""
        pb = inspect_profile(
            write_profile(tmp_path, mutate(browser__camofox={"managed_persistence": True}))
        )
        assert any("user_id is empty" in f.message for f in audit_profile(pb))
        assert pb.persistent is False

    def test_headless_fallback_is_a_warning(self, tmp_path):
        pb = inspect_profile(write_profile(tmp_path, mutate(browser__headed=False)))
        warns = [f for f in audit_profile(pb) if f.level == "warn"]
        assert any("ENABLE_VNC" in f.fix for f in warns)

    def test_short_timeout_is_a_warning(self, tmp_path):
        pb = inspect_profile(write_profile(tmp_path, mutate(browser__inactivity_timeout=60)))
        assert any("reaped mid-action" in f.message for f in audit_profile(pb))

    def test_browser_use_backend_on_camofox_is_a_warning(self, tmp_path):
        """Camofox has no CDP endpoint for the harness to attach to."""
        pb = inspect_profile(write_profile(tmp_path, mutate(browser__backend="browser-use")))
        assert any("cannot attach" in f.message for f in audit_profile(pb))

    def test_toolsets_as_comma_string_still_parsed(self, tmp_path):
        pb = inspect_profile(write_profile(tmp_path, mutate(toolsets="browser,file")))
        assert pb.has_browser_toolset

    def test_empty_browser_section_does_not_crash(self, tmp_path):
        pb = inspect_profile(write_profile(tmp_path, {"toolsets": []}))
        assert pb.has_browser_toolset is False
        assert audit_profile(pb)


class TestCollisions:
    def test_shared_user_id_is_an_error(self, tmp_path):
        profiles = [
            ProfileBrowser(name="a", path=Path("a"), user_id="same"),
            ProfileBrowser(name="b", path=Path("b"), user_id="same"),
        ]
        errs = audit_user_id_collisions(profiles)
        assert len(errs) == 1
        assert "share one cookie jar" in errs[0].message

    def test_distinct_ids_pass(self):
        profiles = [
            ProfileBrowser(name="a", path=Path("a"), user_id="one"),
            ProfileBrowser(name="b", path=Path("b"), user_id="two"),
        ]
        assert audit_user_id_collisions(profiles) == []

    def test_empty_ids_are_not_a_collision(self):
        profiles = [
            ProfileBrowser(name="a", path=Path("a"), user_id=""),
            ProfileBrowser(name="b", path=Path("b"), user_id=""),
        ]
        assert audit_user_id_collisions(profiles) == []


class TestAuditAll:
    def test_reports_every_profile(self):
        report = audit_all(CONFIG_ROOT, live=False)
        assert {pb.name for pb in report.profiles} == {"main", *WORKERS}

    def test_main_is_labelled_main(self):
        report = audit_all(CONFIG_ROOT, live=False)
        assert "main" in {pb.name for pb in report.profiles}

    def test_missing_root_reports_error(self, tmp_path):
        report = audit_all(tmp_path / "nothing", live=False)
        assert not report.ok
        assert any("no Hermes config" in f.message for f in report.findings)

    def test_failing_api_adds_an_error(self):
        with mock.patch("hermes_airdrop.browser_check.probe") as m:
            m.return_value = type("R", (), {"ok": False, "detail": "refused", "__str__": lambda s: "x"})()
            report = audit_all(CONFIG_ROOT, camofox_url="http://localhost:9377", live=True)
        assert not report.ok

    def test_render_lists_every_worker(self):
        text = audit_all(CONFIG_ROOT, live=False).render()
        for w in WORKERS:
            assert w in text


class TestProbe:
    def _resp(self, status=200):
        m = mock.MagicMock()
        m.__enter__.return_value.status = status
        return m

    def test_success(self):
        with mock.patch("urllib.request.urlopen", return_value=self._resp()):
            r = probe("http://localhost:9377")
        assert r.ok and "200" in r.detail

    def test_http_error_still_means_the_server_is_up(self):
        err = urllib.error.HTTPError("u", 404, "Not Found", {}, None)
        with mock.patch("urllib.request.urlopen", side_effect=err):
            r = probe("http://localhost:9377")
        assert r.ok, "a 404 still proves something is listening"

    def test_connection_refused(self):
        with mock.patch("urllib.request.urlopen", side_effect=urllib.error.URLError("refused")):
            r = probe("http://localhost:9377")
        assert not r.ok and "refused" in r.detail

    def test_timeout(self):
        with mock.patch("urllib.request.urlopen", side_effect=TimeoutError()):
            assert not probe("http://localhost:9377").ok

    def test_path_is_appended(self):
        with mock.patch("urllib.request.urlopen", return_value=self._resp()) as m:
            probe("http://localhost:6080/", path=NOVNC_PATH)
        assert m.call_args[0][0].full_url.endswith("/vnc.html")

    def test_str_marks_success_and_failure(self):
        from hermes_airdrop.browser_check import ProbeResult

        assert str(ProbeResult("http://x", True, "HTTP 200")).startswith("✓")
        assert str(ProbeResult("http://x", False, "refused")).startswith("✗")


class TestHelpers:
    @pytest.mark.parametrize("url,expected", [
        ("http://localhost:9377", "http://localhost:6080"),
        ("http://localhost:9377/", "http://localhost:6080"),
        ("http://192.168.1.5:9377", "http://192.168.1.5:6080"),
        ("https://camofox.example.com:9377", "https://camofox.example.com:6080"),
    ])
    def test_guess_novnc(self, url, expected):
        assert _guess_novnc(url) == expected

    def test_guess_novnc_gives_up_on_junk(self):
        assert _guess_novnc("not a url") == ""

    def test_label_main(self):
        assert _label(CONFIG_ROOT / "config.yaml", CONFIG_ROOT) == "main"

    def test_label_profile_uses_parent_dir(self):
        p = CONFIG_ROOT / "profiles" / "worker-daily" / "config.yaml"
        assert _label(p, CONFIG_ROOT) == "worker-daily"

    def test_finding_str_with_fix(self):
        s = str(Finding("error", "x", "broken", fix="do this"))
        assert "✗ x: broken" in s and "do this" in s

    def test_finding_str_without_fix(self):
        assert "↳" not in str(Finding("warn", "x", "meh"))
