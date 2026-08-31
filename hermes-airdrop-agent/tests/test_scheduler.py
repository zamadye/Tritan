"""Cron parsing and next-run computation."""
from __future__ import annotations

from datetime import datetime, timedelta, timezone

import pytest

from hermes_airdrop.scheduler import (
    CronSchedule,
    IntervalSchedule,
    ScheduleError,
    describe,
    next_run,
    parse,
    parse_field,
)

UTC = timezone.utc


def dt(*a):
    return datetime(*a, tzinfo=UTC)


class TestParse:
    def test_cron_returns_cron_schedule(self):
        assert isinstance(parse("0 9 * * *"), CronSchedule)

    def test_interval_returns_interval_schedule(self):
        assert isinstance(parse("every 30m"), IntervalSchedule)

    def test_interval_is_case_insensitive(self):
        assert parse("Every 6H").seconds == 6 * 3600

    def test_empty_rejected(self):
        with pytest.raises(ScheduleError):
            parse("   ")

    def test_wrong_field_count_rejected(self):
        with pytest.raises(ScheduleError):
            parse("0 9 * *")

    def test_garbage_rejected(self):
        with pytest.raises(ScheduleError):
            parse("not a schedule")

    def test_interval_zero_rejected(self):
        with pytest.raises(ScheduleError):
            parse("every 0m")

    def test_out_of_range_value_rejected(self):
        with pytest.raises(ScheduleError):
            parse("60 9 * * *")

    def test_bad_step_rejected(self):
        with pytest.raises(ScheduleError):
            parse("*/0 9 * * *")


class TestParseField:
    @pytest.mark.parametrize("expr,expected", [
        ("*", set(range(0, 60))),
        ("0", {0}),
        ("1,2,3", {1, 2, 3}),
        ("1-4", {1, 2, 3, 4}),
        ("*/15", {0, 15, 30, 45}),
        ("10-30/10", {10, 20, 30}),
    ])
    def test_minute_field(self, expr, expected):
        assert set(parse_field(expr, 0)) == expected

    def test_wrap_around_range(self):
        # "22-2" in hours means 22,23,0,1,2
        assert set(parse_field("22-2", 1)) == {22, 23, 0, 1, 2}

    def test_empty_element_rejected(self):
        with pytest.raises(ScheduleError):
            parse_field("1,,2", 0)


class TestNextRunCron:
    def test_daily_nine_am(self):
        assert next_run("0 9 * * *", after=dt(2026, 8, 25, 8, 0)) == dt(2026, 8, 25, 9, 0)

    def test_daily_nine_am_rolls_to_tomorrow(self):
        assert next_run("0 9 * * *", after=dt(2026, 8, 25, 9, 0)) == dt(2026, 8, 26, 9, 0)

    def test_strictly_after_current_minute(self):
        # At exactly 09:00 the next fire is tomorrow, not now.
        assert next_run("0 9 * * *", after=dt(2026, 8, 25, 9, 0, 0)) == dt(2026, 8, 26, 9, 0)

    def test_seconds_are_truncated(self):
        r = next_run("0 9 * * *", after=dt(2026, 8, 25, 8, 59, 59))
        assert r == dt(2026, 8, 25, 9, 0)

    def test_every_fifteen_minutes(self):
        assert next_run("*/15 * * * *", after=dt(2026, 8, 25, 10, 7)) == dt(2026, 8, 25, 10, 15)

    def test_weekday_only(self):
        # 2026-08-25 is a Tuesday; "0 9 * * 1-5" should land Wed 09:00.
        r = next_run("0 9 * * 1-5", after=dt(2026, 8, 25, 10, 0))
        assert r == dt(2026, 8, 26, 9, 0)
        assert r.weekday() == 2  # Wednesday

    def test_skips_weekend(self):
        # Friday 2026-08-28 10:00 -> next weekday 09:00 is Monday 2026-08-31
        r = next_run("0 9 * * 1-5", after=dt(2026, 8, 28, 10, 0))
        assert r == dt(2026, 8, 31, 9, 0)
        assert r.weekday() == 0  # Monday

    def test_month_boundary(self):
        assert next_run("0 0 1 * *", after=dt(2026, 8, 15)) == dt(2026, 9, 1, 0, 0)

    def test_year_boundary(self):
        assert next_run("0 0 1 1 *", after=dt(2026, 6, 1)) == dt(2027, 1, 1, 0, 0)

    def test_impossible_date_raises(self):
        with pytest.raises(ScheduleError):
            next_run("0 0 30 2 *", after=dt(2026, 1, 1))

    def test_sunday_accepted_as_seven(self):
        a = next_run("0 9 * * 0", after=dt(2026, 8, 25))
        b = next_run("0 9 * * 7", after=dt(2026, 8, 25))
        assert a == b
        assert a.weekday() == 6  # Python Sunday

    def test_dom_and_dow_union_when_both_restricted(self):
        # POSIX: when both day fields are restricted the match is a union.
        # "0 9 13 * 5" should fire on the 13th OR on Fridays.
        r = next_run("0 9 13 * 5", after=dt(2026, 8, 1, 0, 0))
        candidates = {dt(2026, 8, 7, 9, 0), dt(2026, 8, 13, 9, 0)}
        assert r in candidates
        assert r == dt(2026, 8, 7, 9, 0)  # the Friday comes first


class TestNextRunInterval:
    def test_every_30m(self):
        epoch = dt(2026, 8, 25, 0, 0)
        s = parse("every 30m", epoch=epoch)
        assert next_run(s, after=dt(2026, 8, 25, 10, 7)) == dt(2026, 8, 25, 10, 30)

    def test_every_6h(self):
        epoch = dt(2026, 8, 25, 0, 0)
        s = parse("every 6h", epoch=epoch)
        assert next_run(s, after=dt(2026, 8, 25, 6, 0)) == dt(2026, 8, 25, 12, 0)

    def test_interval_before_epoch_returns_epoch(self):
        epoch = dt(2026, 8, 25, 12, 0)
        s = parse("every 1h", epoch=epoch)
        assert next_run(s, after=dt(2026, 8, 25, 0, 0)) == epoch


class TestDescribe:
    @pytest.mark.parametrize("expr,frag", [
        ("every 30m", "every 30 minutes"),
        ("every 6h", "every 6 hours"),
        ("every 1h", "every 1 hour"),
        ("every 2d", "every 2 days"),
    ])
    def test_intervals(self, expr, frag):
        assert describe(expr) == frag

    def test_daily_nine(self):
        d = describe("0 9 * * *")
        assert "minute=0" in d and "hour=9" in d

    def test_weekday_names_rendered(self):
        assert "Mon" in describe("0 9 * * 1-5")
