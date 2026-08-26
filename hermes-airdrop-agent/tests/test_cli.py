"""End-to-end CLI tests. These exercise the real ``main()`` entry point."""
from __future__ import annotations

import json
from pathlib import Path

import pytest

from fakes import ANTHROPIC, PLACEHOLDER_ANT
from hermes_airdrop.cli import main

ROOT = Path(__file__).resolve().parents[1]
MAIN_CONFIG = ROOT / "config" / "hermes" / "config.yaml"


@pytest.fixture
def data(tmp_path):
    return str(tmp_path / "data")


def run(capsys, *argv):
    code = main(list(argv))
    out, err = capsys.readouterr()
    return code, out, err


class TestBasics:
    def test_version(self, capsys):
        with pytest.raises(SystemExit) as ei:
            main(["--version"])
        assert ei.value.code == 0

    def test_no_subcommand_errors(self):
        with pytest.raises(SystemExit):
            main([])

    def test_init_creates_dirs(self, capsys, tmp_path):
        d = tmp_path / "data"
        assert main(["--data-dir", str(d), "init"]) == 0
        assert (d / "campaigns").is_dir()
        assert (d / "logs").is_dir()
        assert (d / "screenshots").is_dir()


class TestConfigCommands:
    def test_check_shipped_config_passes(self, capsys):
        code, out, _ = run(capsys, "config", "check", str(MAIN_CONFIG))
        assert code == 0, out
        assert "schema valid" in out

    def test_check_bad_inline_yaml(self, capsys):
        code, out, _ = run(capsys, "config", "check", "--text",
                           "security:\n  never_store_private_keys: true\n")
        assert code == 1
        assert "security.never_store_private_keys" in out

    def test_check_missing_file(self, capsys):
        code, _, err = run(capsys, "config", "check", "/no/such.yaml")
        assert code == 1
        assert "error:" in err

    def test_show_redacts_secrets(self, capsys, tmp_path):
        env = tmp_path / ".env"
        env.write_text(f"ANTHROPIC_API_KEY={ANTHROPIC}\n")
        code, out, _ = run(capsys, "--env-file", str(env), "config", "show")
        assert code == 0
        assert "abcdefghijklmno" not in out
        assert "sk-a" in out


class TestAnalyze:
    def test_strong_project_is_prioritize(self, capsys):
        args = ["analyze", "--project", "Good Protocol"]
        for f in ("team-insight", "team-execution", "team-integrity",
                  "product-pmf", "product-delivery", "product-responsibility",
                  "narrative-web3", "narrative-web2", "narrative-premium"):
            args += [f"--{f}", "3"]
        code, out, _ = run(capsys, *args)
        assert code == 0
        assert "Decision: PRIORITIZE" in out

    def test_shoddy_delivery_is_skip(self, capsys):
        code, out, _ = run(capsys, "analyze", "--project", "Bad",
                           "--product-delivery", "0", "--team-insight", "3")
        assert code == 2
        assert "Decision: SKIP" in out

    def test_json_output_parses(self, capsys):
        code, out, _ = run(capsys, "analyze", "--project", "X", "--json")
        assert code == 2  # all-zero ratings -> SKIP
        assert json.loads(out)["decision"] == "SKIP"

    def test_from_json_file(self, capsys, tmp_path):
        p = tmp_path / "ev.json"
        p.write_text(json.dumps({"project": "From File", "product_delivery": 3,
                                 "team_insight": 3, "team_execution": 3,
                                 "team_integrity": 3}))
        code, out, _ = run(capsys, "analyze", "--from-json", str(p))
        assert code == 0
        assert "From File" in out

    def test_low_confidence_warns(self, capsys):
        # A rating of 1 or 2 means "looked but could not confirm", which drags
        # confidence under the 0.70 review threshold.
        code, out, _ = run(capsys, "analyze", "--project", "Meh",
                           "--team-insight", "2", "--team-execution", "2",
                           "--product-pmf", "2", "--product-delivery", "2",
                           "--narrative-web3", "1")
        assert "below 0.70" in out

    def test_high_confidence_does_not_warn(self, capsys):
        _, out, _ = run(capsys, "analyze", "--project", "Clear",
                        "--team-insight", "3", "--product-pmf", "0")
        assert "below 0.70" not in out

    def test_save_to_creates_campaign(self, capsys, data):
        run(capsys, "--data-dir", data, "analyze", "--project", "Saved Proj",
            "--team-insight", "3", "--team-execution", "3", "--team-integrity", "3",
            "--product-pmf", "3", "--product-delivery", "3",
            "--product-responsibility", "3", "--narrative-web3", "3",
            "--narrative-web2", "3", "--narrative-premium", "3", "--save-to")
        code, out, _ = run(capsys, "--data-dir", data, "campaign", "list")
        assert "saved-proj" in out

    def test_invalid_rating_rejected_by_argparse(self):
        with pytest.raises(SystemExit):
            main(["analyze", "--project", "X", "--team-insight", "9"])


class TestCampaignFlow:
    def test_add_list_show_roundtrip(self, capsys, data):
        assert run(capsys, "--data-dir", data, "campaign", "add",
                   "--project", "Loqua", "--action", "check_in@0 9 * * *")[0] == 0
        code, out, _ = run(capsys, "--data-dir", data, "campaign", "list")
        assert "loqua" in out
        code, out, _ = run(capsys, "--data-dir", data, "campaign", "show", "loqua")
        assert json.loads(out)["campaign"]["actions"][0]["name"] == "check_in"

    def test_duplicate_add_refused(self, capsys, data):
        run(capsys, "--data-dir", data, "campaign", "add", "--project", "Dup")
        code, _, err = run(capsys, "--data-dir", data, "campaign", "add", "--project", "Dup")
        assert code == 1
        assert "already exists" in err

    def test_duplicate_add_with_force(self, capsys, data):
        run(capsys, "--data-dir", data, "campaign", "add", "--project", "Dup")
        assert run(capsys, "--data-dir", data, "campaign", "add",
                   "--project", "Dup", "--force")[0] == 0

    def test_main_tier_refused(self, capsys, data):
        code, _, err = run(capsys, "--data-dir", data, "campaign", "add",
                           "--project", "X", "--tier", "main")
        assert code == 1
        assert "never farmed" in err

    def test_set_status(self, capsys, data):
        run(capsys, "--data-dir", data, "campaign", "add", "--project", "X")
        assert run(capsys, "--data-dir", data, "campaign", "set-status", "x", "active")[0] == 0
        _, out, _ = run(capsys, "--data-dir", data, "campaign", "list")
        assert "active" in out

    def test_set_invalid_status(self, capsys, data):
        run(capsys, "--data-dir", data, "campaign", "add", "--project", "X")
        code, _, err = run(capsys, "--data-dir", data, "campaign", "set-status", "x", "yolo")
        assert code == 1 and "status must be" in err

    def test_add_action_validates_schedule(self, capsys, data):
        run(capsys, "--data-dir", data, "campaign", "add", "--project", "X")
        code, _, err = run(capsys, "--data-dir", data, "campaign", "add-action", "x", "a@nonsense")
        assert code == 1
        assert "bad schedule" in err

    def test_add_action_duplicate(self, capsys, data):
        run(capsys, "--data-dir", data, "campaign", "add", "--project", "X",
            "--action", "check_in@0 9 * * *")
        code, _, err = run(capsys, "--data-dir", data, "campaign", "add-action",
                           "x", "check_in@0 10 * * *")
        assert code == 1 and "already exists" in err

    def test_log_records_points(self, capsys, data):
        run(capsys, "--data-dir", data, "campaign", "add", "--project", "X")
        code, out, _ = run(capsys, "--data-dir", data, "campaign", "log",
                           "x", "check_in", "ok", "--points", "150")
        assert code == 0 and "150" in out

    def test_log_invalid_status(self, capsys, data):
        run(capsys, "--data-dir", data, "campaign", "add", "--project", "X")
        with pytest.raises(SystemExit):
            main(["--data-dir", data, "campaign", "log", "x", "a", "maybe"])

    def test_show_missing_campaign(self, capsys, data):
        code, _, err = run(capsys, "--data-dir", data, "campaign", "show", "ghost")
        assert code == 1 and "no such campaign" in err

    def test_list_empty(self, capsys, data):
        _, out, _ = run(capsys, "--data-dir", data, "campaign", "list")
        assert "no campaigns" in out


class TestPlanAndReport:
    def test_plan_json(self, capsys, data):
        run(capsys, "--data-dir", data, "campaign", "add", "--project", "P",
            "--status", "active", "--action", "check_in@0 9 * * *")
        code, out, _ = run(capsys, "--data-dir", data, "plan",
                           "--date", "2026-08-25", "--json")
        assert code == 0
        d = json.loads(out)
        assert d["counts"]["total"] == 1
        assert d["actions"][0]["campaign"] == "p"

    def test_plan_text(self, capsys, data):
        run(capsys, "--data-dir", data, "campaign", "add", "--project", "P",
            "--status", "active", "--action", "check_in@0 9 * * *")
        _, out, _ = run(capsys, "--data-dir", data, "plan", "--date", "2026-08-25")
        assert "Airdrop plan for 2026-08-25" in out

    def test_plan_bad_date(self, capsys, data):
        # Should be a clean one-line error and exit 1, not a traceback.
        code, _, err = run(capsys, "--data-dir", data, "plan", "--date", "not-a-date")
        assert code == 1
        assert "ISO date" in err
        assert "Traceback" not in err

    def test_report(self, capsys, data):
        run(capsys, "--data-dir", data, "campaign", "add", "--project", "P")
        code, out, _ = run(capsys, "--data-dir", data, "report")
        assert code == 0 and "Airdrop report" in out

    def test_report_json(self, capsys, data):
        run(capsys, "--data-dir", data, "campaign", "add", "--project", "P")
        _, out, _ = run(capsys, "--data-dir", data, "report", "--json")
        assert json.loads(out)["totals"]["campaigns"] == 1


class TestWallets:
    EVM = "0x742d35Cc6634C0532925a3b844Bc9e7595f0bEb0"

    def test_add_and_list(self, capsys, data):
        assert run(capsys, "--data-dir", data, "wallets", "add",
                   "--address", self.EVM, "--tier", "main")[0] == 0
        _, out, _ = run(capsys, "--data-dir", data, "wallets", "list")
        assert "main" in out
        # The full address must not appear in output.
        assert self.EVM not in out

    def test_private_key_refused(self, capsys, data):
        key = "4c0883a69102937d6231471b5dbb6204fe5129617082792ae468d01a3f362318"
        code, _, err = run(capsys, "--data-dir", data, "wallets", "add", "--address", key)
        assert code == 1
        assert "never stored" in err

    def test_audit_flags_missing_main(self, capsys, data):
        code, out, _ = run(capsys, "--data-dir", data, "wallets", "audit")
        assert code == 1 and "main" in out

    def test_audit_clean(self, capsys, data):
        run(capsys, "--data-dir", data, "wallets", "add", "--address", self.EVM, "--tier", "main")
        run(capsys, "--data-dir", data, "wallets", "add", "--address",
            "0x1111111111111111111111111111111111111111", "--tier", "farming")
        code, out, _ = run(capsys, "--data-dir", data, "wallets", "audit")
        assert code == 0 and "OK" in out

    def test_list_empty(self, capsys, data):
        _, out, _ = run(capsys, "--data-dir", data, "wallets", "list")
        assert "no wallets" in out


class TestEvidence:
    def test_tail_empty(self, capsys, data):
        assert run(capsys, "--data-dir", data, "evidence", "tail")[0] == 0

    def test_tail_after_log(self, capsys, data):
        run(capsys, "--data-dir", data, "campaign", "add", "--project", "P")
        run(capsys, "--data-dir", data, "campaign", "log", "p", "check_in", "ok")
        _, out, _ = run(capsys, "--data-dir", data, "evidence", "tail")
        assert "check_in" in out

    def test_verify(self, capsys, data):
        code, out, _ = run(capsys, "--data-dir", data, "evidence", "verify")
        assert code == 0 and "verified" in out


class TestDoctor:
    def test_doctor_runs(self, capsys, data, tmp_path):
        env = tmp_path / ".env"
        env.write_text(f"ANTHROPIC_API_KEY={ANTHROPIC}\n")
        code, out, _ = run(capsys, "--data-dir", data, "--env-file", str(env),
                           "doctor", "--config", str(MAIN_CONFIG))
        assert "doctor:" in out
        assert "[1/6] environment" in out and "[6/6] campaigns" in out

    def test_doctor_flags_bad_config(self, capsys, data, tmp_path):
        env = tmp_path / ".env"
        env.write_text(f"ANTHROPIC_API_KEY={ANTHROPIC}\n")
        bad = tmp_path / "bad.yaml"
        bad.write_text("security:\n  never_store_private_keys: true\n")
        code, out, _ = run(capsys, "--data-dir", data, "--env-file", str(env),
                           "doctor", "--config", str(bad))
        assert code == 1
        assert "problems found" in out

    def test_doctor_flags_missing_api_key(self, capsys, data, tmp_path):
        env = tmp_path / ".env"
        env.write_text(f"ANTHROPIC_API_KEY={PLACEHOLDER_ANT}\n")
        code, out, _ = run(capsys, "--data-dir", data, "--env-file", str(env),
                           "doctor", "--config", str(MAIN_CONFIG))
        assert code == 1
        assert "No usable model API key" in out
