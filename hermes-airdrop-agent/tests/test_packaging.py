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
