"""Packaging integrity — files that must actually be in the repository.

This exists because of a real, silent failure: the parent Tritan `.gitignore`
carried an unanchored `skills/` rule, which matches *every* `skills/` directory
in the repo. `git add` skips ignored paths without saying so, so all six
SKILL.md files were staged zero times across three separate commits while every
other check passed. The tests all ran green against the working tree and told
us nothing about what had been committed.

So these tests check git's view, not the filesystem's.
"""
from __future__ import annotations

import subprocess
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parent

MUST_BE_TRACKED = [
    "install.sh",
    "pyproject.toml",
    "README.md",
    "AGENTS.md",
    ".env.example",
    ".gitignore",
    "Makefile",
    "config/hermes/config.yaml",
    "knowledge/airdrop-task-patterns.md",
    "knowledge/verification-rules.md",
    "config/hermes/memories/MEMORY.md",
    "config/hermes/memories/USER.md",
]


def _tracked() -> set[str]:
    """Paths git knows about, relative to this project directory."""
    out = subprocess.run(
        ["git", "ls-files", "--", str(ROOT)],
        cwd=str(REPO), capture_output=True, text=True, check=True,
    ).stdout
    prefix = str(ROOT.relative_to(REPO)) + "/"
    return {line[len(prefix):] for line in out.splitlines() if line.startswith(prefix)}


def _ignored(rel: str) -> bool:
    r = subprocess.run(
        ["git", "check-ignore", "-q", str(ROOT / rel)],
        cwd=str(REPO), capture_output=True, text=True,
    )
    return r.returncode == 0


class TestSkillsAreCommitted:
    """The regression that motivated this file."""

    SKILLS = [
        "airdrop-analyzer",
        "daily-executor",
        "discord-engager",
        "portfolio-tracker",
        "quest-executor",
        "wallet-isolation",
    ]

    @pytest.mark.parametrize("name", SKILLS)
    def test_skill_exists_on_disk(self, name):
        assert (ROOT / "skills" / name / "SKILL.md").is_file()

    @pytest.mark.parametrize("name", SKILLS)
    def test_skill_is_not_gitignored(self, name):
        """An unanchored `skills/` anywhere up the tree silently swallows these."""
        rel = f"skills/{name}/SKILL.md"
        assert not _ignored(rel), (
            f"{rel} is gitignored — check for an unanchored `skills/` rule in a "
            "parent .gitignore. `git add` skips it without warning."
        )

    @pytest.mark.parametrize("name", SKILLS)
    def test_skill_is_tracked_by_git(self, name):
        rel = f"skills/{name}/SKILL.md"
        assert rel in _tracked(), (
            f"{rel} is not tracked. It exists on disk, tests pass against it, "
            "and a fresh clone would not have it."
        )


class TestEssentialFilesTracked:
    @pytest.mark.parametrize("rel", MUST_BE_TRACKED)
    def test_on_disk(self, rel):
        assert (ROOT / rel).is_file(), f"{rel} missing from the working tree"

    @pytest.mark.parametrize("rel", MUST_BE_TRACKED)
    def test_tracked(self, rel):
        assert rel in _tracked(), f"{rel} is on disk but not committed"


class TestProfilesAndSourcesTracked:
    def test_every_profile_config_tracked(self):
        on_disk = {
            str(p.relative_to(ROOT))
            for p in (ROOT / "config" / "hermes" / "profiles").glob("*/config.yaml")
        }
        tracked = _tracked()
        assert on_disk, "no profiles found on disk"
        missing = on_disk - tracked
        assert not missing, f"profiles on disk but not committed: {sorted(missing)}"

    def test_every_soul_tracked(self):
        on_disk = {
            str(p.relative_to(ROOT))
            for p in (ROOT / "config" / "hermes" / "profiles").glob("*/SOUL.md")
        }
        missing = on_disk - _tracked()
        assert not missing, f"SOUL.md files not committed: {sorted(missing)}"

    def test_every_source_module_tracked(self):
        on_disk = {
            str(p.relative_to(ROOT))
            for p in (ROOT / "src" / "hermes_airdrop").glob("*.py")
        }
        missing = on_disk - _tracked()
        assert not missing, f"source modules not committed: {sorted(missing)}"


class TestSecretsAreNotTracked:
    """The mirror image of the above: .env must be invisible to git."""

    def test_env_is_gitignored(self):
        assert _ignored(".env"), ".env must be gitignored"

    def test_env_not_tracked_even_if_present(self):
        assert ".env" not in _tracked()

    def test_data_dir_not_tracked(self):
        tracked = _tracked()
        leaked = [p for p in tracked if p.startswith("data/") and not p.endswith(".gitkeep")]
        assert not leaked, f"runtime data committed: {leaked}"

    def test_wallets_json_not_tracked(self):
        assert "data/wallets.json" not in _tracked()

class TestWorkflowAndKnowledgeAreWired:
    """The workflow is only real if the toolsets and knowledge are actually
    there. These check git's view, like the rest of this file."""

    PROFILES = ["worker-orchestrator", "worker-lead", "worker-quests",
                "worker-daily", "worker-discord", "worker-monitor",
                "worker-analyzer"]

    @pytest.mark.parametrize("name", PROFILES)
    def test_profile_has_the_kanban_toolset(self, name):
        """Without it the agent cannot create, claim, complete or block a task,
        so the documented workflow cannot execute."""
        import yaml
        cfg = yaml.safe_load(
            (ROOT / "config" / "hermes" / "profiles" / name / "config.yaml").read_text()
        )
        assert "kanban" in cfg.get("toolsets", []), f"{name} cannot coordinate"

    def test_coordinating_layers_can_also_delegate(self):
        import yaml
        for name in ("worker-orchestrator", "worker-lead"):
            cfg = yaml.safe_load(
                (ROOT / "config" / "hermes" / "profiles" / name / "config.yaml").read_text()
            )
            assert "delegation" in cfg["toolsets"], f"{name} cannot spawn subagents"

    def test_main_config_runs_the_dispatcher_in_gateway(self):
        """kanban.dispatch_in_gateway is what means 'start one gateway and the
        workers come up on demand'. If it is off, nothing dispatches."""
        import yaml
        cfg = yaml.safe_load((ROOT / "config" / "hermes" / "config.yaml").read_text())
        kanban = cfg.get("kanban")
        assert kanban, "no kanban section in the main config"
        assert kanban.get("dispatch_in_gateway") is True
        assert kanban.get("auto_subscribe_on_create") is True, \
            "results would never reach the Telegram thread"

    def test_workflow_doc_exists_and_covers_every_agent(self):
        doc = ROOT / "docs" / "workflows.md"
        assert doc.is_file(), "docs/workflows.md missing"
        text = doc.read_text(encoding="utf-8")
        for name in self.PROFILES:
            assert name in text, f"{name} has no documented workflow"

    def test_workflow_doc_names_the_real_hermes_tools(self):
        """Guard against documenting a workflow that uses invented tool names."""
        text = (ROOT / "docs" / "workflows.md").read_text(encoding="utf-8")
        for tool in ("kanban_create", "kanban_complete", "kanban_block",
                     "kanban_show", "delegate_task"):
            assert tool in text, f"workflow references {tool} nowhere"

    def test_workflow_doc_documents_the_block_kinds(self):
        text = (ROOT / "docs" / "workflows.md").read_text(encoding="utf-8")
        for kind in ("needs_input", "capability", "dependency", "transient"):
            assert kind in text, f"block kind '{kind}' undocumented"

    @pytest.mark.parametrize("name", [
        "airdrop-task-patterns.md", "verification-rules.md",
        "worked-example-monad.md", "quest-platforms.md", "cycles-and-meta.md",
    ])
    def test_knowledge_file_tracked(self, name):
        assert f"knowledge/{name}" in _tracked(), f"knowledge/{name} not committed"

    def test_knowledge_covers_the_quest_platforms(self):
        text = (ROOT / "knowledge" / "quest-platforms.md").read_text(encoding="utf-8")
        for platform in ("Galxe", "Layer3", "Zealy", "Talentum"):
            assert platform in text

    def test_knowledge_records_the_silent_failures(self):
        """Address mismatch and verification lag are the two failures that
        produce no error anywhere. If the knowledge base loses them, runs will
        keep re-doing work that already happened."""
        text = (ROOT / "knowledge" / "quest-platforms.md").read_text(encoding="utf-8")
        assert "Verification lag" in text
        assert "Address mismatch" in text or "address" in text.lower()
