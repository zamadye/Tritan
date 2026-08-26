"""Skills must be well-formed AND their documented commands must exist.

The second half matters more than the first: a SKILL.md telling the agent to
run `haa campaign record` when the CLI only has `haa campaign log` produces an
agent that confidently fails every morning.
"""
from __future__ import annotations

import re
from pathlib import Path

import pytest
import yaml

from hermes_airdrop.cli import build_parser

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
SKILL_FILES = sorted(SKILLS_DIR.glob("*/SKILL.md"))

EXPECTED = {
    "airdrop-analyzer",
    "daily-executor",
    "discord-engager",
    "portfolio-tracker",
    "quest-executor",
    "wallet-isolation",
}


def _command_paths(parser=None, prefix: list[str] | None = None) -> set[tuple[str, ...]]:
    """Walk the argparse tree and collect every valid command path."""
    import argparse

    parser = parser or build_parser()
    prefix = prefix or []
    paths: set[tuple[str, ...]] = set()
    for action in parser._actions:
        if isinstance(action, argparse._SubParsersAction):
            for name, sub in action.choices.items():
                full = prefix + [name]
                paths.add(tuple(full))
                paths |= _command_paths(sub, full)
    return paths


COMMANDS = _command_paths()


def _commands_in_text(text: str) -> list[list[str]]:
    """Extract `haa ...` invocations from markdown, dropping flags and values."""
    out: list[list[str]] = []
    for block in re.findall(r"```(?:bash|sh)?\n(.*?)```", text, re.S):
        for line in block.splitlines():
            line = line.strip()
            if not line.startswith("haa "):
                continue
            tokens: list[str] = []
            for tok in line.split():
                if tok.startswith("-"):
                    continue
                if tok.startswith("<") or tok.startswith("$") or tok.startswith('"'):
                    break
                tokens.append(tok)
            if tokens:
                out.append(tokens)
    return out


class TestInventory:
    def test_all_expected_skills_present(self):
        assert {p.parent.name for p in SKILL_FILES} == EXPECTED

    def test_no_stray_skill_directories(self):
        dirs = {p.name for p in SKILLS_DIR.iterdir() if p.is_dir()}
        assert dirs == EXPECTED


class TestFrontmatter:
    @pytest.mark.parametrize("path", SKILL_FILES, ids=lambda p: p.parent.name)
    def test_has_yaml_frontmatter(self, path):
        text = path.read_text(encoding="utf-8")
        assert text.startswith("---\n"), "SKILL.md must open with YAML frontmatter"
        fm = text.split("---", 2)[1]
        data = yaml.safe_load(fm)
        assert isinstance(data, dict)

    @pytest.mark.parametrize("path", SKILL_FILES, ids=lambda p: p.parent.name)
    def test_required_fields(self, path):
        fm = yaml.safe_load(path.read_text(encoding="utf-8").split("---", 2)[1])
        for field in ("name", "description", "version", "author", "license", "platforms"):
            assert field in fm, f"{path.parent.name}: missing '{field}'"

    @pytest.mark.parametrize("path", SKILL_FILES, ids=lambda p: p.parent.name)
    def test_name_matches_directory(self, path):
        fm = yaml.safe_load(path.read_text(encoding="utf-8").split("---", 2)[1])
        assert fm["name"] == path.parent.name

    @pytest.mark.parametrize("path", SKILL_FILES, ids=lambda p: p.parent.name)
    def test_description_is_a_real_sentence(self, path):
        fm = yaml.safe_load(path.read_text(encoding="utf-8").split("---", 2)[1])
        d = fm["description"]
        assert len(d) > 40, "description should explain what the skill does"
        assert d.endswith("."), "description should end with a period"

    @pytest.mark.parametrize("path", SKILL_FILES, ids=lambda p: p.parent.name)
    def test_hermes_metadata(self, path):
        fm = yaml.safe_load(path.read_text(encoding="utf-8").split("---", 2)[1])
        hermes = fm["metadata"]["hermes"]
        assert isinstance(hermes["tags"], list) and hermes["tags"]
        for rel in hermes.get("related_skills", []):
            assert rel in EXPECTED, f"{path.parent.name}: unknown related skill '{rel}'"

    @pytest.mark.parametrize("path", SKILL_FILES, ids=lambda p: p.parent.name)
    def test_platforms_valid(self, path):
        fm = yaml.safe_load(path.read_text(encoding="utf-8").split("---", 2)[1])
        assert set(fm["platforms"]) <= {"linux", "macos", "windows"}

    @pytest.mark.parametrize("path", SKILL_FILES, ids=lambda p: p.parent.name)
    def test_has_body_beyond_frontmatter(self, path):
        body = path.read_text(encoding="utf-8").split("---", 2)[2]
        assert len(body.strip()) > 500, f"{path.parent.name}: body is too thin"


class TestDocumentedCommandsExist:
    """Every `haa ...` line in a skill must be a real CLI command."""

    @pytest.mark.parametrize("path", SKILL_FILES, ids=lambda p: p.parent.name)
    def test_commands_resolve(self, path):
        text = path.read_text(encoding="utf-8")
        invocations = _commands_in_text(text)
        assert invocations, f"{path.parent.name}: expected at least one haa example"
        for tokens in invocations:
            # COMMANDS holds subparser paths without the prog name, so drop the
            # leading "haa" before matching.
            cmd = tokens[1:] if tokens and tokens[0] == "haa" else tokens
            for end in range(len(cmd), 0, -1):
                if tuple(cmd[:end]) in COMMANDS:
                    break
            else:
                pytest.fail(f"{path.parent.name}: unknown command 'haa {' '.join(cmd)}'")


class TestPolicyContent:
    """The safety rules are the product. If they vanish from a skill, the
    agent loses them — so assert they are present in the text."""

    def read(self, name):
        return (SKILLS_DIR / name / "SKILL.md").read_text(encoding="utf-8")

    def test_daily_executor_forbids_unverified_ok(self):
        t = self.read("daily-executor")
        assert "Never log `ok`" in t

    def test_daily_executor_halts_on_captcha(self):
        assert "CAPTCHA" in self.read("daily-executor")

    def test_quest_executor_gates_spend(self):
        t = self.read("quest-executor")
        assert "HAA_MAX_SPEND_USD" in t
        assert "performed by the operator" in t

    def test_quest_executor_forbids_limit_splitting(self):
        assert "split it into smaller" in self.read("quest-executor")

    def test_skills_assume_a_gui_browser(self):
        """The workload is GUI: skills must tell the agent to open the page,
        not to reach for an API that does not exist."""
        for name in ("daily-executor", "quest-executor", "airdrop-analyzer"):
            t = self.read(name).lower()
            assert "open the" in t or "browser" in t, f"{name} never mentions a browser"

    def test_daily_executor_uses_the_site_as_evidence(self):
        assert "the confirmation the site itself gives" in self.read("daily-executor")

    def test_analyzer_uses_the_browser(self):
        """A docs page is marketing. The product has to be opened and used."""
        t = self.read("airdrop-analyzer")
        assert "open the product" in t
        assert "There is no API" in t

    def test_discord_forbids_auto_posting(self):
        t = self.read("discord-engager")
        assert "Never post automatically" in t
        assert "Terms of Service" in t

    def test_portfolio_tracker_checks_evidence(self):
        assert "haa evidence verify" in self.read("portfolio-tracker")

    def test_wallet_isolation_declines_evasion(self):
        t = self.read("wallet-isolation")
        assert "does not help you present multiple wallets as multiple people" in t
        assert "fingerprint" in t.lower()

    def test_wallet_isolation_stores_no_keys(self):
        t = self.read("wallet-isolation")
        assert "is ever stored" in t
        assert "hardware wallet" in t

    def test_analyzer_documents_vetoes(self):
        t = self.read("airdrop-analyzer")
        for word in ("veto", "PRIORITIZE", "SKIP", "0–3"):
            assert word in t

    def test_analyzer_attributes_the_framework(self):
        t = self.read("airdrop-analyzer")
        assert "HTX Insights" in t
