"""Long-horizon state: positions, locks and streaks.

A real campaign is not a list of clicks. From the guides this was designed
against:

* **Base** — open an LP position and *leave it for at least 30 days*.
* **Abstract** — upvote on Discover *every day for 30 consecutive days* to
  unlock a permanent multiplier; flash badges expire and cannot be
  retroactively claimed.
* **Monad** — stake on aPriori / Kintsu and keep it there; visit faucets
  daily because they reset on a timer.

None of that is expressible as "run this action today". It needs durable state
that survives weeks of runs and can answer:

* what is currently open, and when must it stay open until?
* what expires soon, and what breaks if a day is missed?

So this store exists separately from the action log. The log answers "what did
I do"; this answers "what am I committed to".
"""

from __future__ import annotations

import json
import os
from dataclasses import asdict, dataclass, field
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Any

POSITION_KINDS = frozenset({"lp", "stake", "lock", "badge", "vesting", "other"})
POSITION_STATUSES = frozenset({"open", "closed", "expired"})


class PositionError(Exception):
    pass


def _today() -> date:
    return datetime.now(timezone.utc).date()


def _parse_day(value: str) -> date:
    try:
        return datetime.fromisoformat(value).date()
    except ValueError as exc:
        raise PositionError(f"not an ISO date: {value!r}") from exc


@dataclass
class Position:
    """Something opened that must stay open, or that expires."""

    id: str
    campaign: str
    kind: str = "other"
    protocol: str = ""
    opened_at: str = ""
    until: str = ""  # ISO date; empty means open-ended
    amount: str = ""  # free-form: "0.5 MON", "$80 ETH/USDC"
    notes: str = ""
    status: str = "open"
    closed_at: str = ""

    def __post_init__(self) -> None:
        if self.kind not in POSITION_KINDS:
            raise PositionError(
                f"invalid kind {self.kind!r}; expected one of {sorted(POSITION_KINDS)}"
            )
        if self.status not in POSITION_STATUSES:
            raise PositionError(
                f"invalid status {self.status!r}; expected one of {sorted(POSITION_STATUSES)}"
            )
        if not self.opened_at:
            self.opened_at = _today().isoformat()
        # Validate eagerly: a malformed date found three weeks later, when the
        # position matters, is much worse than one found now.
        _parse_day(self.opened_at)
        if self.until:
            _parse_day(self.until)

    @property
    def is_open(self) -> bool:
        return self.status == "open"

    def days_remaining(self, *, today: date | None = None) -> int | None:
        """Days until ``until``. None when open-ended or already past."""
        if not self.until:
            return None
        return (_parse_day(self.until) - (today or _today())).days

    def is_past_due(self, *, today: date | None = None) -> bool:
        d = self.days_remaining(today=today)
        return d is not None and d < 0

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> "Position":
        known = set(cls.__dataclass_fields__)  # type: ignore[attr-defined]
        return cls(**{k: v for k, v in d.items() if k in known})


@dataclass
class Streak:
    """A consecutive-day commitment. Missing a day resets it to zero."""

    name: str
    campaign: str
    required_daily: bool = True
    current: int = 0
    longest: int = 0
    last_day: str = ""
    target_days: int = 0  # 0 = no target; Abstract's Discover streak is 30

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> "Streak":
        known = set(cls.__dataclass_fields__)  # type: ignore[attr-defined]
        return cls(**{k: v for k, v in d.items() if k in known})

    def days_since_last(self, *, today: date | None = None) -> int | None:
        if not self.last_day:
            return None
        return ((today or _today()) - _parse_day(self.last_day)).days

    def is_at_risk(self, *, today: date | None = None) -> bool:
        """True when a required daily streak has already missed today."""
        if not self.required_daily:
            return False
        gap = self.days_since_last(today=today)
        return gap is not None and gap >= 1

    def is_complete(self) -> bool:
        return self.target_days > 0 and self.current >= self.target_days


@dataclass
class State:
    positions: list[Position] = field(default_factory=list)
    streaks: list[Streak] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "positions": [p.to_dict() for p in self.positions],
            "streaks": [s.to_dict() for s in self.streaks],
        }

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> "State":
        return cls(
            positions=[Position.from_dict(p) for p in d.get("positions", [])],
            streaks=[Streak.from_dict(s) for s in d.get("streaks", [])],
        )


def _atomic_write(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    os.replace(tmp, path)


class PositionStore:
    """Per-campaign long-horizon state, stored at ``<campaign>/positions.json``."""

    def __init__(self, campaigns_root: Path | str) -> None:
        self.root = Path(campaigns_root)

    def path(self, campaign: str) -> Path:
        return self.root / campaign / "positions.json"

    def load(self, campaign: str) -> State:
        p = self.path(campaign)
        if not p.exists():
            return State()
        return State.from_dict(json.loads(p.read_text(encoding="utf-8")))

    def save(self, campaign: str, state: State) -> Path:
        p = self.path(campaign)
        _atomic_write(p, state.to_dict())
        return p

    # ------------------------------------------------------------- positions
    def open_position(self, campaign: str, position: Position) -> Position:
        state = self.load(campaign)
        if any(p.id == position.id for p in state.positions):
            raise PositionError(f"position '{position.id}' already exists")
        position.campaign = campaign
        state.positions.append(position)
        self.save(campaign, state)
        return position

    def close_position(
        self, campaign: str, position_id: str, *, expired: bool = False
    ) -> Position:
        state = self.load(campaign)
        for p in state.positions:
            if p.id == position_id:
                p.status = "expired" if expired else "closed"
                p.closed_at = _today().isoformat()
                self.save(campaign, state)
                return p
        raise PositionError(f"no such position: {position_id}")

    def open_positions(self, campaign: str) -> list[Position]:
        return [p for p in self.load(campaign).positions if p.is_open]

    def expiring_soon(self, campaign: str, *, days: int = 3) -> list[Position]:
        """Open positions whose ``until`` is within ``days`` (or already past).

        These are the ones worth interrupting someone for: an LP withdrawn a
        day early can cost the whole eligibility window.
        """
        out = []
        for p in self.open_positions(campaign):
            remaining = p.days_remaining()
            if remaining is not None and remaining <= days:
                out.append(p)
        return sorted(out, key=lambda p: p.days_remaining() or 0)

    # --------------------------------------------------------------- streaks
    def streak(self, campaign: str, name: str) -> Streak | None:
        for s in self.load(campaign).streaks:
            if s.name == name:
                return s
        return None

    def ensure_streak(self, campaign: str, name: str, **kwargs: Any) -> Streak:
        state = self.load(campaign)
        for s in state.streaks:
            if s.name == name:
                return s
        s = Streak(name=name, campaign=campaign, **kwargs)
        state.streaks.append(s)
        self.save(campaign, state)
        return s

    def record_streak_day(self, campaign: str, name: str, *, on: date | None = None) -> Streak:
        """Mark a streak day done. Handles gaps: a missed day resets it.

        Recording the same day twice is idempotent, so a retried run cannot
        inflate a streak.
        """
        day = on or _today()
        state = self.load(campaign)
        target = next((s for s in state.streaks if s.name == name), None)
        if target is None:
            target = Streak(name=name, campaign=campaign)
            state.streaks.append(target)

        if target.last_day == day.isoformat():
            self.save(campaign, state)
            return target

        gap = target.days_since_last(today=day)
        if gap == 1 or not target.last_day:
            target.current += 1
        else:
            # Missed at least one day — the streak is broken.
            target.current = 1
        target.last_day = day.isoformat()
        target.longest = max(target.longest, target.current)
        self.save(campaign, state)
        return target

    def at_risk_streaks(self, campaign: str, *, today: date | None = None) -> list[Streak]:
        return [s for s in self.load(campaign).streaks if s.is_at_risk(today=today)]

    # --------------------------------------------------------------- rollups
    def summary(self, campaign: str, *, today: date | None = None) -> dict[str, Any]:
        state = self.load(campaign)
        t = today or _today()
        return {
            "campaign": campaign,
            "open_positions": len([p for p in state.positions if p.is_open]),
            "past_due": [p.id for p in state.positions if p.is_open and p.is_past_due(today=t)],
            "expiring_3d": [p.id for p in self.expiring_soon(campaign, days=3)],
            "streaks": {
                s.name: {"current": s.current, "target": s.target_days,
                         "at_risk": s.is_at_risk(today=t), "complete": s.is_complete()}
                for s in state.streaks
            },
        }
