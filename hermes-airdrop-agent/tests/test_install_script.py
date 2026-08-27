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

    def test_links_env_into_hermes_home(self):
        """Hermes reads $HERMES_HOME/.env. The project .env next to install.sh
        is read by nothing on its own."""
        text = INSTALL.read_text(encoding="utf-8")
        assert 'ln -s "$ENV_FILE" "$dst"' in text
        assert 'link_env "$HERMES_HOME"' in text

    def test_links_env_into_every_profile_home(self):
        """A profile is a SEPARATE Hermes home with its OWN .env. Missing this
        makes every ${VAR} resolve to a literal string."""
        text = INSTALL.read_text(encoding="utf-8")
        assert 'for pdir in "$PROJECT_DIR"/config/hermes/profiles/*/' in text
        assert "profile homes" in text

    def test_env_linking_is_visible_in_dry_run(self, repo_snapshot):
        out = run("./install.sh", "--dry-run").stdout
        assert "ln -s" in out and ".env" in out

    def test_existing_env_is_backed_up_not_overwritten(self):
        text = INSTALL.read_text(encoding="utf-8")
        assert 'mv "$dst" "${dst}.bak"' in text

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

    def test_all_five_jobs_registered(self, text):
        for name in ("airdrop-orchestrator", "airdrop-daily", "airdrop-verify",
                     "airdrop-weekly", "airdrop-discord"):
            assert name in text

    def test_orchestrator_runs_before_the_workers(self, text):
        """Layer 1 decides whether today's work is worth doing, so it must be
        scheduled ahead of the 09:00 lead run."""
        assert '"30 8 * * *"' in text
        assert text.index("airdrop-orchestrator") < text.index("airdrop-daily")

    def test_browser_jobs_preflight_cdp(self, text):
        """Chrome runs on the host. If the operator closed the window, the job
        must fail fast instead of spending an hour failing every click."""
        assert "haa browser check" in text
        assert "do NOT continue" in text
        # The lead and discord jobs are the browser-driven ones.
        assert text.count("${PREFLIGHT}") >= 2

    def test_lead_prompt_insists_on_per_project_rules(self, text):
        assert "Never assume one project's flow applies to another" in text

    def test_jobs_are_idempotent(self, text):
        # Re-running must not duplicate jobs.
        assert "exists:" in text

class TestExtractStandalone:
    """This project currently lives inside an unrelated repository (Tritan, a
    Polymarket trading agent). The extraction path has to work, and two bugs in
    it were found the hard way."""

    @pytest.fixture
    def script(self):
        return ROOT / "scripts" / "extract-standalone.sh"

    def test_exists_and_is_executable(self, script):
        import os
        assert script.is_file()
        assert os.access(script, os.X_OK)

    def test_syntax(self, script):
        r = subprocess.run(["bash", "-n", str(script)], capture_output=True, text=True)
        assert r.returncode == 0, r.stderr

    def test_uses_fully_qualified_refs(self, script):
        """The branch name collides with the directory name, so a bare
        `$BRANCH` makes git report 'ambiguous argument'."""
        text = script.read_text(encoding="utf-8")
        assert 'REF="refs/heads/$BRANCH"' in text
        assert 'ls-tree -r --name-only "$REF"' in text

    def test_guards_the_grep_pipefail_trap(self, script):
        """With `set -o pipefail`, a grep that finds nothing exits 1 and kills
        the script at exactly the moment it should report success."""
        text = script.read_text(encoding="utf-8")
        assert "|| true" in text

    def test_verifies_no_parent_files_leak(self, script):
        text = script.read_text(encoding="utf-8")
        assert "agent/" in text and "main" in text
        assert "no parent-project files present" in text

    def test_verifies_install_sh_is_at_the_root(self, script):
        """If the split left a wrapper directory, the repo would not be usable."""
        assert "install.sh is at the root" in script.read_text(encoding="utf-8")

    def test_does_not_modify_the_parent_repository(self, script):
        text = script.read_text(encoding="utf-8")
        # Only reads the parent repo and creates a branch; never rewrites it.
        for forbidden in ("filter-branch", "rebase", "git push --force"):
            assert forbidden not in text

class TestBrowserLaunchIsBlockedForAgents:
    """The agent's browser must be the one managed CDP instance, not one it
    spawns itself. `hermes-cli` bundles a terminal by default, so shell access
    cannot be removed by dropping a toolset -- the launch commands must be
    denied instead. These pin that guard into every config."""

    LAUNCH_PATTERNS = ["*google-chrome*", "*chromium*", "*--remote-debugging-port*",
                       "*Xvfb*", "*pkill*"]

    def _configs(self):
        import yaml
        yield ROOT / "config" / "hermes" / "config.yaml"
        yield from sorted((ROOT / "config" / "hermes" / "profiles").glob("*/config.yaml"))

    def test_every_config_denies_browser_launch(self):
        import yaml
        for f in self._configs():
            deny = yaml.safe_load(f.read_text()).get("approvals", {}).get("deny", [])
            missing = [x for x in self.LAUNCH_PATTERNS if x not in deny]
            assert not missing, f"{f.name} does not deny browser launch: {missing}"

    def test_no_profile_explicitly_grants_terminal(self):
        import yaml
        for f in sorted((ROOT / "config" / "hermes" / "profiles").glob("*/config.yaml")):
            ts = yaml.safe_load(f.read_text()).get("toolsets", [])
            assert "terminal" not in ts, f"{f.parent.name} explicitly grants terminal"

    def test_chromium_is_not_the_default_browser(self):
        for script in ("install.sh", "scripts/start-browser.sh"):
            text = (ROOT / script).read_text(encoding="utf-8")
            # Chrome detection must come before any chromium fallback.
            assert text.index("find_chrome") < text.index("find_chromium")
            # Chromium must sit behind the explicit opt-in, not run silently.
            assert "HAA_ALLOW_CHROMIUM" in text

    def test_no_silent_chromium_install_message(self):
        text = (ROOT / "install.sh").read_text(encoding="utf-8")
        assert "installing Chromium from the distro repository" not in text

    def test_start_browser_profile_follows_env(self):
        """The launched --user-data-dir must equal HAA_CHROME_PROFILE so the
        agent runs in the same profile the operator logged into."""
        text = (ROOT / "scripts" / "start-browser.sh").read_text(encoding="utf-8")
        assert 'HAA_CHROME_PROFILE' in text
        assert "--user-data-dir=\"$PROFILE_DIR\"" in text

class TestManagedBrowserControlIsNeverBlocked:
    """The deny-list stops the agent spawning its OWN browser, but must never
    impede its full control of the MANAGED one. browser_* tools are not shell
    commands (approvals only gate terminal_tool), so this asserts the deny
    patterns can never match a managed-browser tool name."""

    BROWSER_TOOLS = ["browser_navigate","browser_snapshot","browser_click","browser_type",
                     "browser_scroll","browser_back","browser_press","browser_get_images",
                     "browser_vision","browser_console","browser_cdp","browser_dialog",
                     "web_search"]

    def test_deny_patterns_never_match_browser_tools(self):
        import fnmatch, yaml
        deny = yaml.safe_load((ROOT/"config"/"hermes"/"config.yaml").read_text())["approvals"]["deny"]
        hit = [t for t in self.BROWSER_TOOLS for pat in deny if fnmatch.fnmatch(t, pat)]
        assert not hit, f"deny-list blocks managed-browser control: {hit}"


class TestAutonomyIsStatedNotStopAndAsk:
    """The agent must reason forward with full browser control, not stop and
    ask for the next instruction. These pin that principle into the prompts."""

    @pytest.mark.parametrize("name", ["daily-executor", "quest-executor"])
    def test_skill_states_full_browser_control(self, name):
        t = (ROOT/"skills"/name/"SKILL.md").read_text(encoding="utf-8")
        assert "Full control of the browser" in t
        assert "Do not stop to ask" in t

    @pytest.mark.parametrize("name", ["daily-executor", "quest-executor"])
    def test_skill_lists_only_the_three_legit_stops(self, name):
        t = (ROOT/"skills"/name/"SKILL.md").read_text(encoding="utf-8")
        for stop in ("signature", "CAPTCHA", "complete"):
            assert stop in t

    @pytest.mark.parametrize("name", ["worker-orchestrator", "worker-lead"])
    def test_coordinating_souls_reason_forward(self, name):
        t = (ROOT/"config"/"hermes"/"profiles"/name/"SOUL.md").read_text(encoding="utf-8")
        assert "## Autonomy" in t
        assert "what should I do?" in t
