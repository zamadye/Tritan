"""Operator activity log — lives INSIDE the framework and is committed.

The operator asked for every activity done with this framework to be recorded,
stored inside the project (not outside), and NOT gitignored, so that when they
run it on their machine and push, an agent reading the branch can immediately
see what was attempted and where it failed.

Design:

- One append-only JSONL file: ``activity/activity.log``.
- stdlib-only, so it can be called from the shell wrappers without the venv.
- Every record carries enough to locate a failure: timestamp, source (haa /
  debug-agent / install / start-browser), agent, command/task, exit code,
  duration, git HEAD, host, and a short error tail when something failed.
- Logging must NEVER break the thing being logged: every write is wrapped so a
  full disk or a read-only checkout degrades to a silent no-op.

Deliberately NOT under ``data/`` (which is gitignored) — this file is meant to
travel with the branch.
"""

from __future__ import annotations

import json
import os
import socket
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ACTIVITY_DIR = ROOT / "activity"
LOG_FILE = ACTIVITY_DIR / "activity.log"

#: How many trailing characters of error output to keep per record.
ERROR_TAIL = 1200


def _now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def _git_head() -> str:
    try:
        return subprocess.run(
            ["git", "rev-parse", "--short", "HEAD"],
            cwd=str(ROOT), capture_output=True, text=True, timeout=5,
        ).stdout.strip() or "-"
    except Exception:
        return "-"


def _host() -> str:
    try:
        return socket.gethostname()
    except Exception:
        return "-"


def record(
    source: str,
    *,
    agent: str = "",
    cmd: str = "",
    task: str = "",
    exit_code: int | None = None,
    duration_s: float | None = None,
    error: str | None = None,
) -> Path | None:
    """Append one JSONL record. Returns the log path, or None if it could not.

    Never raises.
    """
    try:
        ACTIVITY_DIR.mkdir(parents=True, exist_ok=True)
        entry = {
            "ts": _now(),
            "source": source,
            "agent": agent,
            "cmd": cmd,
            "task": task,
            "exit": exit_code,
            "duration_s": round(duration_s, 2) if duration_s is not None else None,
            "git": _git_head(),
            "host": _host(),
            "error": (error or "").strip()[-ERROR_TAIL:] or None,
        }
        with open(LOG_FILE, "a", encoding="utf-8") as fh:
            fh.write(json.dumps(entry, ensure_ascii=False) + "\n")
        return LOG_FILE
    except Exception:
        return None


def read(n: int | None = None) -> list[dict]:
    """Return the last ``n`` records (all if n is None)."""
    if not LOG_FILE.exists():
        return []
    out = []
    for line in LOG_FILE.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            out.append(json.loads(line))
        except json.JSONDecodeError:
            continue
    return out[-n:] if n else out


def failures(n: int = 50) -> list[dict]:
    """Records that exited non-zero — the first place to look on error."""
    return [r for r in read(n) if (r.get("exit") or 0) != 0]


# ---------------------------------------------------------------------------
# CLI: python -m hermes_airdrop.activity_log <verb>
# ---------------------------------------------------------------------------

def _main(argv: list[str]) -> int:
    if not argv:
        print("usage: activity_log record|tail|failures")
        return 2
    verb = argv[0]

    if verb == "record":
        # --source X --agent Y --exit N --task "..." --error-file F
        opts = {}
        i = 1
        while i < len(argv):
            k = argv[i].lstrip("-")
            if i + 1 < len(argv) and not argv[i + 1].startswith("--"):
                opts[k] = argv[i + 1]; i += 2
            else:
                opts[k] = ""; i += 1
        err = None
        ef = opts.get("error-file")
        if ef and Path(ef).exists():
            err = Path(ef).read_text(encoding="utf-8", errors="replace")
        record(
            opts.get("source", "shell"),
            agent=opts.get("agent", ""),
            cmd=opts.get("cmd", ""),
            task=opts.get("task", ""),
            exit_code=int(opts.get("exit", 0) or 0),
            duration_s=float(opts.get("duration", 0) or 0),
            error=err or opts.get("error") or None,
        )
        return 0

    if verb == "tail":
        n = int(argv[1]) if len(argv) > 1 else 20
        for r in read(n):
            print(json.dumps(r, ensure_ascii=False))
        return 0

    if verb == "failures":
        rows = failures()
        if not rows:
            print("(no failures recorded)")
            return 0
        for r in rows:
            print(json.dumps(r, ensure_ascii=False))
        return 0

    print(f"unknown verb: {verb}")
    return 2


if __name__ == "__main__":
    sys.exit(_main(sys.argv[1:]))
