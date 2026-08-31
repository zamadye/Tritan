"""Schedule parsing and next-run computation.

Supports the two schedule syntaxes Hermes' own ``cron`` accepts (see
``website/docs/user-guide/features/cron.md``):

* **cron expressions** — ``"0 9 * * *"``, ``"*/15 9-18 * * 1-5"``
* **relative intervals** — ``"every 30m"``, ``"every 6h"``, ``"every 2d"``

Kept dependency-free and deterministic so ``haa plan`` can be tested and so a
scheduled run's timing can be reproduced exactly in an audit.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone

MINUTE = 0
HOUR = 1
DOM = 2
MONTH = 3
DOW = 4

FIELD_RANGES: dict[int, tuple[int, int]] = {
    MINUTE: (0, 59),
    HOUR: (0, 23),
    DOM: (1, 31),
    MONTH: (1, 12),
    # Cron accepts 0-7 for day-of-week, with both 0 and 7 meaning Sunday.
    # We parse the full 0-7 and normalise onto Python's weekday() below.
    DOW: (0, 7),
}

FIELD_NAMES = ("minute", "hour", "day-of-month", "month", "day-of-week")

#: ``every 30m`` / ``every 6h`` / ``every 2d``
_INTERVAL_RE = re.compile(r"^every\s+(\d+)\s*([mhd])$", re.I)
_UNIT_SECONDS = {"m": 60, "h": 3600, "d": 86400}

#: Cron day-of-week accepts 0-7 with both 0 and 7 meaning Sunday. We map that
#: onto Python's weekday() where Monday is 0, so we translate explicitly.
_CRON_DOW_TO_PY = {0: 6, 1: 0, 2: 1, 3: 2, 4: 3, 5: 4, 6: 5, 7: 6}


class ScheduleError(ValueError):
    """Raised for a malformed schedule string."""


def parse_field(expr: str, field_idx: int) -> frozenset[int]:
    """Parse one cron field into the set of matching values."""
    lo, hi = FIELD_RANGES[field_idx]
    expr = expr.strip()
    if not expr:
        raise ScheduleError("empty cron field")

    values: set[int] = set()
    for part in expr.split(","):
        part = part.strip()
        if not part:
            raise ScheduleError(f"empty element in cron field {FIELD_NAMES[field_idx]!r}")

        step = 1
        if "/" in part:
            rng, _, step_s = part.partition("/")
            try:
                step = int(step_s)
            except ValueError:
                raise ScheduleError(f"bad step {step_s!r} in cron field {part!r}") from None
            if step < 1:
                raise ScheduleError(f"step must be >= 1, got {step}")
            part = rng.strip()

        if part in ("*", "?"):
            start, end = lo, hi
        elif "-" in part:
            a, _, b = part.partition("-")
            start, end = _num(a, field_idx), _num(b, field_idx)
        else:
            start = end = _num(part, field_idx)

        if start > end:
            # Wrap-around ranges like "22-2" (hours) or "5-1" (dow) are legal.
            values.update(range(start, hi + 1, step))
            values.update(range(lo, end + 1, step))
            continue

        values.update(range(start, end + 1, step))

    out = {v for v in values if lo <= v <= hi}
    if not out:
        raise ScheduleError(f"cron field {FIELD_NAMES[field_idx]!r} matches nothing: {expr!r}")
    return frozenset(out)


def _num(tok: str, field_idx: int) -> int:
    tok = tok.strip()
    try:
        return int(tok)
    except ValueError:
        raise ScheduleError(f"bad value {tok!r} in cron field {FIELD_NAMES[field_idx]!r}") from None


@dataclass(frozen=True)
class CronSchedule:
    """A parsed 5-field cron expression."""

    expression: str
    minutes: frozenset[int]
    hours: frozenset[int]
    days_of_month: frozenset[int]
    months: frozenset[int]
    days_of_week: frozenset[int]
    #: True when the day-of-month / day-of-week fields were restricted.
    day_restricted: bool

    @classmethod
    def parse(cls, expression: str) -> "CronSchedule":
        parts = expression.split()
        if len(parts) != 5:
            raise ScheduleError(
                f"expected 5 cron fields, got {len(parts)}: {expression!r}"
            )
        minutes = parse_field(parts[0], MINUTE)
        hours = parse_field(parts[1], HOUR)
        dom = parse_field(parts[2], DOM)
        months = parse_field(parts[3], MONTH)
        raw_dow = parse_field(parts[4], DOW)
        dow = frozenset(_CRON_DOW_TO_PY[d] for d in raw_dow)
        day_restricted = parts[2] not in ("*", "?") or parts[4] not in ("*", "?")
        return cls(expression, minutes, hours, dom, months, dow, day_restricted)

    def matches_day(self, dt: datetime) -> bool:
        """Standard cron semantics: when both DOM and DOW are restricted the
        match is a **union** (POSIX behaviour), otherwise an intersection."""
        dom_ok = dt.day in self.days_of_month
        dow_ok = dt.weekday() in self.days_of_week
        if self.day_restricted:
            dom_set = self.days_of_month != frozenset(range(1, 32))
            dow_set = self.days_of_week != frozenset(range(0, 7))
            if dom_set and dow_set:
                return dom_ok or dow_ok
        return dom_ok and dow_ok

    def matches(self, dt: datetime) -> bool:
        return (
            dt.minute in self.minutes
            and dt.hour in self.hours
            and dt.month in self.months
            and self.matches_day(dt)
        )


@dataclass(frozen=True)
class IntervalSchedule:
    """A relative ``every Nh`` schedule, anchored at :attr:`epoch`."""

    expression: str
    seconds: int
    epoch: datetime

    def matches(self, dt: datetime) -> bool:  # pragma: no cover - not used directly
        delta = (dt - self.epoch).total_seconds()
        return delta >= 0 and abs(delta % self.seconds) < 1


Schedule = CronSchedule | IntervalSchedule


def parse(expression: str, *, epoch: datetime | None = None) -> Schedule:
    """Parse either syntax into a :class:`Schedule`."""
    if not expression or not expression.strip():
        raise ScheduleError("schedule must not be empty")
    expr = expression.strip()

    if m := _INTERVAL_RE.match(expr):
        n, unit = int(m.group(1)), m.group(2).lower()
        if n < 1:
            raise ScheduleError(f"interval must be >= 1, got {expr!r}")
        base = epoch or datetime(2000, 1, 1, tzinfo=timezone.utc)
        return IntervalSchedule(expression=expr, seconds=n * _UNIT_SECONDS[unit], epoch=base)

    return CronSchedule.parse(expr)


def _floor_minute(dt: datetime) -> datetime:
    return dt.replace(second=0, microsecond=0)


def next_run(
    schedule: Schedule | str,
    *,
    after: datetime | None = None,
    horizon_days: int = 400,
) -> datetime:
    """First fire time strictly after ``after``.

    Raises :class:`ScheduleError` if nothing fires within ``horizon_days``
    (e.g. ``"0 0 30 2 *"`` — 30 February never happens).
    """
    sched = parse(schedule) if isinstance(schedule, str) else schedule
    now = _floor_minute(after or datetime.now(timezone.utc))
    cursor = now + timedelta(minutes=1)

    if isinstance(sched, IntervalSchedule):
        elapsed = (cursor - sched.epoch).total_seconds()
        if elapsed <= 0:
            return sched.epoch
        periods = int(elapsed // sched.seconds)
        return sched.epoch + timedelta(seconds=(periods + 1) * sched.seconds)

    limit = now + timedelta(days=horizon_days)
    while cursor <= limit:
        if cursor.month not in sched.months:
            # Jump to the first of the next month.
            cursor = (cursor.replace(day=1) + timedelta(days=32)).replace(
                day=1, hour=0, minute=0
            )
            continue
        if not sched.matches_day(cursor):
            cursor = (cursor + timedelta(days=1)).replace(hour=0, minute=0)
            continue
        if cursor.hour not in sched.hours:
            cursor = (cursor + timedelta(hours=1)).replace(minute=0)
            continue
        if cursor.minute not in sched.minutes:
            cursor += timedelta(minutes=1)
            continue
        return cursor

    raise ScheduleError(
        f"schedule {getattr(sched, 'expression', sched)!r} never fires within {horizon_days} days"
    )


def describe(expression: str) -> str:
    """Short human-readable description, for reports and ``haa plan``."""
    sched = parse(expression)
    if isinstance(sched, IntervalSchedule):
        for secs, name in ((86400, "day"), (3600, "hour"), (60, "minute")):
            if sched.seconds % secs == 0:
                n = sched.seconds // secs
                return f"every {n} {name}{'s' if n != 1 else ''}"
        return f"every {sched.seconds}s"

    def fmt(vals: frozenset[int], lo: int, hi: int) -> str:
        full = frozenset(range(lo, hi + 1))
        if vals == full:
            return "*"
        return ",".join(str(v) for v in sorted(vals))

    dom = fmt(sched.days_of_month, 1, 31)
    dow_names = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    dow = (
        "*"
        if sched.days_of_week == frozenset(range(0, 7))
        else ",".join(dow_names[d] for d in sorted(sched.days_of_week))
    )
    return (
        f"minute={fmt(sched.minutes, 0, 59)} hour={fmt(sched.hours, 0, 23)} "
        f"dom={dom} month={fmt(sched.months, 1, 12)} dow={dow}"
    )
