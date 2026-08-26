"""Campaign store — the durable record of what we are farming and how far along.

Layout on disk (one directory per campaign, plain JSON, git-diffable):

    data/campaigns/<slug>/
        info.json         # what the campaign is + the analyzer verdict
        progress.json     # running tallies + append-only action log
        screenshots/      # proof, referenced by evidence.py

JSON rather than SQLite on purpose: a farming operation is audited by reading
files, and a corrupt DB at 3am is worse than a merge conflict.

All writes are atomic (tmp file + ``os.replace``) so a crash mid-write cannot
truncate a progress file.
"""

from __future__ import annotations

import json
import os
import re
from dataclasses import asdict, dataclass, field
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Iterator

from .analyzer import Verdict

# Campaign lifecycle. Only ACTIVE campaigns get scheduled work.
STATUS_RESEARCH = "research"
STATUS_ACTIVE = "active"
STATUS_PAUSED = "paused"
STATUS_DONE = "done"
STATUS_DROPPED = "dropped"

VALID_STATUSES = frozenset(
    {STATUS_RESEARCH, STATUS_ACTIVE, STATUS_PAUSED, STATUS_DONE, STATUS_DROPPED}
)

_SLUG_RE = re.compile(r"[^a-z0-9]+")


class CampaignError(Exception):
    pass


def slugify(name: str) -> str:
    """Stable filesystem-safe identifier for a campaign."""
    s = _SLUG_RE.sub("-", name.strip().lower()).strip("-")
    if not s:
        raise CampaignError(f"cannot derive a slug from {name!r}")
    return s[:64]


def _utcnow() -> datetime:
    return datetime.now(timezone.utc)


# ---------------------------------------------------------------------------
# Models
# ---------------------------------------------------------------------------


@dataclass
class ActionSpec:
    """One repeatable thing the campaign asks for."""

    name: str
    schedule: str = "0 9 * * *"  # cron expression
    kind: str = "browser"  # browser | manual | wallet
    needs_approval: bool = False
    notes: str = ""

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> "ActionSpec":
        known = cls.__dataclass_fields__  # type: ignore[attr-defined]
        return cls(**{k: v for k, v in d.items() if k in known})


@dataclass
class Campaign:
    slug: str
    project: str
    url: str = ""
    status: str = STATUS_RESEARCH
    wallet_tier: str = "farming"  # see wallets.py — never "main"
    started_at: str = ""
    ended_at: str | None = None
    verdict: dict[str, Any] | None = None
    actions: list[ActionSpec] = field(default_factory=list)
    notes: str = ""

    def __post_init__(self) -> None:
        if self.status not in VALID_STATUSES:
            raise CampaignError(
                f"invalid status {self.status!r}; expected one of {sorted(VALID_STATUSES)}"
            )
        if not self.started_at:
            self.started_at = _utcnow().isoformat(timespec="seconds")

    # ---------------------------------------------------------------- (de)ser
    def to_dict(self) -> dict[str, Any]:
        d = asdict(self)
        d["actions"] = [a.to_dict() for a in self.actions]
        return d

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> "Campaign":
        known = set(cls.__dataclass_fields__)  # type: ignore[attr-defined]
        data = {k: v for k, v in d.items() if k in known}
        data["actions"] = [ActionSpec.from_dict(a) for a in d.get("actions", [])]
        return cls(**data)

    @property
    def is_active(self) -> bool:
        return self.status == STATUS_ACTIVE


@dataclass
class LogEntry:
    ts: str
    action: str
    status: str  # ok | failed | skipped | halted
    detail: str = ""
    evidence: str = ""  # path or hash of the proof artifact

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> "LogEntry":
        known = set(cls.__dataclass_fields__)  # type: ignore[attr-defined]
        return cls(**{k: v for k, v in d.items() if k in known})


@dataclass
class Progress:
    """Matches the ``progress.json`` shape the daily-executor skill documents."""

    campaign: str
    days_active: int = 0
    total_days: int = 30
    today: str = ""  # ISO date the "today_*" fields refer to
    today_actions: list[str] = field(default_factory=list)
    points_today: int = 0
    total_points: int = 0
    issues: list[str] = field(default_factory=list)
    next_action: str = ""
    next_action_time: str = ""
    log: list[LogEntry] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        d = asdict(self)
        d["log"] = [e.to_dict() for e in self.log]
        return d

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> "Progress":
        known = set(cls.__dataclass_fields__)  # type: ignore[attr-defined]
        data = {k: v for k, v in d.items() if k in known}
        data["log"] = [LogEntry.from_dict(e) for e in d.get("log", [])]
        return cls(**data)


# ---------------------------------------------------------------------------
# Store
# ---------------------------------------------------------------------------


def _atomic_write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    os.replace(tmp, path)


class Store:
    """Filesystem-backed campaign store rooted at ``root``."""

    def __init__(self, root: Path | str) -> None:
        self.root = Path(root)
        self.root.mkdir(parents=True, exist_ok=True)

    # ----------------------------------------------------------------- paths
    def campaign_dir(self, slug: str) -> Path:
        return self.root / slug

    def info_path(self, slug: str) -> Path:
        return self.campaign_dir(slug) / "info.json"

    def progress_path(self, slug: str) -> Path:
        return self.campaign_dir(slug) / "progress.json"

    def screenshots_dir(self, slug: str) -> Path:
        return self.campaign_dir(slug) / "screenshots"

    # -------------------------------------------------------------------- CRUD
    def exists(self, slug: str) -> bool:
        return self.info_path(slug).exists()

    def save(self, campaign: Campaign) -> Path:
        if campaign.wallet_tier == "main":
            raise CampaignError(
                "refusing to attach a campaign to the 'main' wallet tier — "
                "the main wallet is never used for farming interactions"
            )
        p = self.info_path(campaign.slug)
        _atomic_write_json(p, campaign.to_dict())
        if not self.progress_path(campaign.slug).exists():
            _atomic_write_json(
                self.progress_path(campaign.slug), Progress(campaign=campaign.slug).to_dict()
            )
        self.screenshots_dir(campaign.slug).mkdir(parents=True, exist_ok=True)
        return p

    def load(self, slug: str) -> Campaign:
        p = self.info_path(slug)
        if not p.exists():
            raise CampaignError(f"no such campaign: {slug}")
        return Campaign.from_dict(json.loads(p.read_text(encoding="utf-8")))

    def load_progress(self, slug: str) -> Progress:
        p = self.progress_path(slug)
        if not p.exists():
            return Progress(campaign=slug)
        return Progress.from_dict(json.loads(p.read_text(encoding="utf-8")))

    def save_progress(self, progress: Progress) -> Path:
        p = self.progress_path(progress.campaign)
        _atomic_write_json(p, progress.to_dict())
        return p

    def delete(self, slug: str) -> bool:
        import shutil

        d = self.campaign_dir(slug)
        if not d.exists():
            return False
        shutil.rmtree(d)
        return True

    def all(self) -> list[Campaign]:
        out: list[Campaign] = []
        if not self.root.exists():
            return out
        for child in sorted(self.root.iterdir()):
            if child.is_dir() and (child / "info.json").exists():
                try:
                    out.append(self.load(child.name))
                except (json.JSONDecodeError, CampaignError, TypeError):
                    continue  # skip corrupt entries rather than failing the listing
        return out

    def by_status(self, status: str) -> list[Campaign]:
        return [c for c in self.all() if c.status == status]

    def __iter__(self) -> Iterator[Campaign]:
        return iter(self.all())

    def __len__(self) -> int:
        return len(self.all())

    # --------------------------------------------------------------- mutations
    def record_verdict(self, slug: str, verdict: Verdict) -> Campaign:
        c = self.load(slug)
        c.verdict = verdict.to_dict()
        # A SKIP verdict should never silently leave a campaign ACTIVE.
        if verdict.decision == "SKIP" and c.status == STATUS_ACTIVE:
            c.status = STATUS_PAUSED
        return c

    def log_action(
        self,
        slug: str,
        action: str,
        status: str,
        detail: str = "",
        *,
        points: int = 0,
        evidence: str = "",
        when: datetime | None = None,
    ) -> Progress:
        """Append an action to the log, update the daily tallies, and persist.

        Writes through immediately rather than returning a dirty object: an
        unsaved progress file is the difference between "the check-in ran" and
        "the check-in ran but nobody can prove it after the crash".
        """
        if status not in ("ok", "failed", "skipped", "halted"):
            raise CampaignError(f"invalid log status {status!r}")
        ts = when or _utcnow()
        prog = self.load_progress(slug)
        today = ts.date().isoformat()

        if prog.today != today:
            # Day rolled over — reset the "today" window.
            prog.today = today
            prog.today_actions = []
            prog.points_today = 0
            prog.days_active += 1

        prog.log.append(LogEntry(ts=ts.isoformat(timespec="seconds"), action=action, status=status, detail=detail, evidence=evidence))
        if status == "ok":
            prog.today_actions.append(action)
            prog.points_today += points
            prog.total_points += points
        elif status in ("failed", "halted"):
            prog.issues.append(f"{ts.isoformat(timespec='seconds')} {action}: {detail or status}")

        # Cap the log so a year of daily runs stays readable in a diff.
        if len(prog.log) > 2000:
            prog.log = prog.log[-2000:]
        self.save_progress(prog)
        return prog

    def actions_due(self, slug: str, *, on: datetime) -> list[ActionSpec]:
        """Which of this campaign's actions fire on date ``on``.

        Returns one entry per action even if it fires several times that day —
        the plan needs "do this today", not a tick-by-tick replay. An action
        with an unparseable schedule is skipped rather than aborting the plan;
        ``haa doctor`` is what surfaces the bad schedule.
        """
        from .scheduler import ScheduleError, next_run, parse

        c = self.load(slug)
        due: list[ActionSpec] = []
        day_start = on.replace(hour=0, minute=0, second=0, microsecond=0)
        day_end = day_start.replace(hour=23, minute=59)

        for spec in c.actions:
            try:
                sched = parse(spec.schedule)
                fire = next_run(sched, after=day_start - timedelta(minutes=1))
            except ScheduleError:
                continue
            if fire <= day_end:
                due.append(spec)
        return due

    def streak(self, slug: str, *, today: date | None = None) -> int:
        """Consecutive days with at least one successful action, ending today.

        A gap is tolerated only for "today", so a run at 09:00 still reports
        yesterday's streak before today's work lands.
        """
        prog = self.load_progress(slug)
        ok_days = {datetime.fromisoformat(e.ts).date() for e in prog.log if e.status == "ok"}
        if not ok_days:
            return 0
        cursor = today or _utcnow().date()
        if cursor not in ok_days:
            if (cursor - timedelta(days=1)) not in ok_days:
                return 0
            cursor = cursor - timedelta(days=1)
        n = 0
        while cursor in ok_days:
            n += 1
            cursor = cursor - timedelta(days=1)
        return n
