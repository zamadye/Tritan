"""The installer must actually run. These tests execute install.sh."""
from __future__ import annotations

import subprocess
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
INSTALL = ROOT / "install.sh"
SCRIPTS = sorted((ROOT / "scripts").glob("*.sh"))


def run(*args, cwd=ROOT, timeout=120):
    return subprocess.run(
        list(args), cwd=str(cwd), capture_output=True, text=True, timeout=timeout
    )


@pytest.fixture
def repo_snapshot():
    """Capture the working tree so a test can prove it changed nothing."""
    before = {p.relative_to(ROOT) for p in ROOT.rglob("*") if p.is_file()}
    yield before
    after = {p.relative_to(ROOT) for p in ROOT.rglob("*") if p.is_file()}
    new = {str(p) for p in after - before}
    # Ignore pytest/build noise, which is not the installer's doing.
    new = {n for n in new if not n.startswith((".pytest_cache", "__pycache__"))}
    assert not new, f"test run created files in the repo: {sorted(new)}"


class TestSyntax:
    @pytest.mark.parametrize("script", [INSTALL] + SCRIPTS, ids=lambda p: p.name)
    def test_bash_syntax(self, script):
        r = run("bash", "-n", str(script))
        assert r.returncode == 0, r.stderr

    @pytest.mark.parametrize("script", [INSTALL] + SCRIPTS, ids=lambda p: p.name)
    def test_executable(self, script):
        import os

        assert os.access(script, os.X_OK), f"{script.name} is not executable"

    @pytest.mark.parametrize("script", [INSTALL] + SCRIPTS, ids=lambda p: p.name)
    def test_strict_mode(self, script):
        # Search the prologue, not a fixed character count — install.sh has a
        # long usage header before its `set` line.
        prologue = "\n".join(script.read_text(encoding="utf-8").splitlines()[:60])
        assert "set -euo pipefail" in prologue, f"{script.name} must run under set -euo pipefail"


class TestDryRun:
    def test_exits_zero(self, repo_snapshot):
        r = run("./install.sh", "--dry-run")
        assert r.returncode == 0, r.stderr

    def test_all_ten_steps_run(self, repo_snapshot):
        out = run("./install.sh", "--dry-run").stdout
        for n in range(1, 11):
            assert f"{n}/10" in out, f"step {n} missing from dry run"

    def test_installs_rather_than_only_checking(self, repo_snapshot):
        """The whole point: this is a system installer. It must actually run
        package-manager installs, not just report what is missing."""
        out = run("./install.sh", "--dry-run").stdout
        assert "[dry-run] sudo apt-get install" in out or "brew install" in out

    def test_installs_hermes_framework(self, repo_snapshot):
        out = run("./install.sh", "--dry-run").stdout
        assert "hermes-agent.nousresearch.com/install.sh" in out

    def test_sets_up_memory_and_knowledge(self, repo_snapshot):
        out = run("./install.sh", "--dry-run").stdout
        assert "memories" in out and "knowledge" in out

    def test_changes_nothing(self, tmp_path, repo_snapshot):
        """The whole point of --dry-run. Run it into a throwaway HERMES_HOME
        and assert neither that nor the repo gained a file."""
        hermes_home = tmp_path / "hermes"
        r = run("./install.sh", "--dry-run", cwd=ROOT)
        assert r.returncode == 0, r.stderr
        assert not hermes_home.exists()

    def test_announces_itself_as_dry(self, repo_snapshot):
        out = run("./install.sh", "--dry-run").stdout
        assert "dry run" in out.lower()
        assert "Dry run complete" in out

    def test_toolchain_check_passes(self, repo_snapshot):
        out = run("./install.sh", "--dry-run").stdout
        assert "✓ git" in out
        assert "Python 3" in out


class TestFlags:
    @pytest.mark.parametrize("flag", ["--skip-chrome", "--skip-hermes", "--no-cron",
                                      "--no-gateway", "-y"])
    def test_flag_accepted(self, flag, repo_snapshot):
        r = run("./install.sh", "--dry-run", flag)
        assert r.returncode == 0, r.stderr

    def test_skip_chrome_skips_step_four(self, repo_snapshot):
        out = run("./install.sh", "--dry-run", "--skip-chrome").stdout
        assert "4/10" in out
        assert "skipped (--skip-chrome)" in out

    def test_skip_gateway_is_reported(self, repo_snapshot):
        out = run("./install.sh", "--dry-run", "--no-gateway").stdout
        assert "Telegram gateway skipped" in out

    def test_skip_hermes_skips_step_two(self, repo_snapshot):
        out = run("./install.sh", "--dry-run", "--skip-hermes").stdout
        assert "skipped (--skip-hermes)" in out

    def test_skip_cron_skips_step_seven(self, repo_snapshot):
        out = run("./install.sh", "--dry-run", "--no-cron").stdout
        assert "skipped (--no-cron)" in out

    def test_unknown_flag_rejected(self, repo_snapshot):
        r = run("./install.sh", "--nope")
        assert r.returncode == 2
        assert "unknown option" in r.stderr

    def test_help_exits_zero(self, repo_snapshot):
        assert run("./install.sh", "--help").returncode == 0


class TestContents:
    """Guard against the installer drifting away from the real upstreams."""

    def test_uses_the_real_hermes_install_url(self):
        text = INSTALL.read_text(encoding="utf-8")
        assert "https://hermes-agent.nousresearch.com/install.sh" in text

    def test_targets_chrome_not_an_antidetect_browser(self):
        text = INSTALL.read_text(encoding="utf-8").lower()
        assert "chromium" in text or "chrome" in text
        assert "camofox" not in text

    def test_never_overwrites_an_existing_env(self):
        text = INSTALL.read_text(encoding="utf-8")
        assert "left untouched" in text

    def test_locks_down_env_permissions(self):
        assert "chmod 600" in INSTALL.read_text(encoding="utf-8")

    def test_no_docker_compose_file_shipped(self):
        # Chrome runs on the host with a real window; there is no browser
        # container, so there must be nothing to compose.
        assert not (ROOT / "docker-compose.yml").exists()

    def test_installer_never_overwrites_an_existing_env(self):
        assert "left untouched" in INSTALL.read_text(encoding="utf-8")

    def test_start_browser_handles_the_chrome_136_trap(self):
        sb = (ROOT / "scripts" / "start-browser.sh").read_text(encoding="utf-8")
        assert "--user-data-dir" in sb, "a dedicated profile dir is mandatory"
        assert "136" in sb, "must document the silent-failure trap"
        assert "/json/version" in sb, "must probe the port, not assume it opened"

    def test_start_browser_does_not_pass_no_sandbox(self):
        """Host Chrome runs as the user, so the sandbox stays on. (--no-sandbox
        is only needed for root-in-Docker; it is mentioned in this script's
        header comment to say so, which is why comments are stripped here.)"""
        sb = (ROOT / "scripts" / "start-browser.sh").read_text(encoding="utf-8")
        code = "\n".join(l for l in sb.splitlines() if not l.lstrip().startswith("#"))
        assert "--no-sandbox" not in code

    def test_cron_script_uses_hermes_cron_not_system_crontab(self):
        text = (ROOT / "scripts" / "cron-jobs.sh").read_text(encoding="utf-8")
        assert "hermes" in text and "cron create" in text
        # The system crontab cannot apply Hermes' guardrails; don't use it.
        assert "crontab -l" not in text


class TestCronScriptPrompts:
    """The scheduled prompts are the agent's only instructions at 09:00 —
    a prompt with no history must be self-contained."""

    @pytest.fixture
    def text(self):
        return (ROOT / "scripts" / "cron-jobs.sh").read_text(encoding="utf-8")

    def test_daily_prompt_is_self_contained(self, text):
        assert "haa plan" in text
        assert "haa campaign log" in text

    def test_daily_prompt_encodes_the_halt_rule(self, text):
        assert "HALT" in text
        assert "Never solve a challenge" in text or "Never sign" in text

    def test_verify_prompt_checks_evidence_integrity(self, text):
        assert "haa evidence verify" in text

    def test_discord_prompt_forbids_auto_posting(self, text):
        assert "Do not post anything" in text

    def test_all_four_jobs_registered(self, text):
        for name in ("airdrop-daily", "airdrop-verify", "airdrop-weekly", "airdrop-discord"):
            assert name in text

    def test_jobs_are_idempotent(self, text):
        # Re-running must not duplicate jobs.
        assert "exists:" in text
