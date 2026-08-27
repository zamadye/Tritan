"""Activity log: every framework action recorded INSIDE the repo, committed.

The operator requires a full activity trail stored in the framework (not
outside), not gitignored, so that after they run on their machine and push, a
reader of the branch can immediately locate any failure.
"""
from __future__ import annotations

import json

from hermes_airdrop import activity_log
from hermes_airdrop.activity_log import failures, read, record


def test_log_lives_inside_the_framework():
    rel = activity_log.LOG_FILE.relative_to(activity_log.ROOT)
    assert str(rel).startswith("activity/"), rel
    # Not under data/ (which is gitignored).
    assert "data" not in rel.parts


def test_record_appends_and_read_returns(tmp_path, monkeypatch):
    monkeypatch.setattr(activity_log, "ACTIVITY_DIR", tmp_path / "activity")
    monkeypatch.setattr(activity_log, "LOG_FILE", tmp_path / "activity" / "activity.log")
    record("haa", cmd="campaign list", exit_code=0)
    record("haa", cmd="campaign show x", exit_code=1, error="no such campaign: x")
    rows = read()
    assert len(rows) == 2
    assert rows[0]["cmd"] == "campaign list" and rows[0]["exit"] == 0
    assert rows[1]["exit"] == 1 and "no such campaign" in rows[1]["error"]


def test_failures_filters_nonzero(tmp_path, monkeypatch):
    monkeypatch.setattr(activity_log, "ACTIVITY_DIR", tmp_path / "activity")
    monkeypatch.setattr(activity_log, "LOG_FILE", tmp_path / "activity" / "activity.log")
    record("haa", exit_code=0)
    record("debug-agent", agent="daily", exit_code=2, error="browser down")
    f = failures()
    assert len(f) == 1 and f[0]["agent"] == "daily"


def test_error_tail_is_bounded(tmp_path, monkeypatch):
    monkeypatch.setattr(activity_log, "ACTIVITY_DIR", tmp_path / "activity")
    monkeypatch.setattr(activity_log, "LOG_FILE", tmp_path / "activity" / "activity.log")
    record("install", exit_code=1, error="x" * 5000)
    assert len(read()[-1]["error"]) <= activity_log.ERROR_TAIL


def test_read_of_missing_log_is_empty(tmp_path, monkeypatch):
    monkeypatch.setattr(activity_log, "LOG_FILE", tmp_path / "nope.log")
    assert read() == [] and failures() == []


def test_record_never_raises_on_unwritable_dir(tmp_path, monkeypatch):
    bad = tmp_path / "ro"
    bad.mkdir()
    # Point at a path that is a FILE, so mkdir/open fail.
    monkeypatch.setattr(activity_log, "ACTIVITY_DIR", bad / "x" / "y")
    monkeypatch.setattr(activity_log, "LOG_FILE", bad / "x" / "y" / "activity.log")
    (bad / "x").write_text("i am a file")
    assert record("haa", exit_code=0) is None  # silent no-op, no exception


def test_record_carries_git_head_and_host(tmp_path, monkeypatch):
    monkeypatch.setattr(activity_log, "ACTIVITY_DIR", tmp_path / "activity")
    monkeypatch.setattr(activity_log, "LOG_FILE", tmp_path / "activity" / "activity.log")
    record("haa", exit_code=0)
    r = read()[-1]
    assert "git" in r and "host" in r and "ts" in r


def test_every_record_is_single_line_json(tmp_path, monkeypatch):
    monkeypatch.setattr(activity_log, "ACTIVITY_DIR", tmp_path / "activity")
    monkeypatch.setattr(activity_log, "LOG_FILE", tmp_path / "activity" / "activity.log")
    record("haa", task="multi\nline\ntask")
    raw = (tmp_path / "activity" / "activity.log").read_text()
    assert len(raw.strip().splitlines()) == 1
    json.loads(raw)
