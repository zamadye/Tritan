"""Long-horizon state: positions, locks and streaks.

The cases this exists for are all real, taken from the guides the design was
researched against: Base asks you to leave an LP position for 30 days,
Abstract asks for 30 consecutive daily upvotes for a permanent multiplier, and
flash badges expire if you do not check every 2-3 days.
"""
from __future__ import annotations

from datetime import date, timedelta

import pytest

from hermes_airdrop.positions import (
    Position,
    PositionError,
    PositionStore,
    State,
    Streak,
)

TODAY = date(2026, 8, 26)


@pytest.fixture
def store(tmp_path):
    return PositionStore(tmp_path / "campaigns")


# ---------------------------------------------------------------------------
# Position
# ---------------------------------------------------------------------------


class TestPosition:
    def test_defaults_to_open_today(self):
        p = Position(id="lp1", campaign="base")
        assert p.status == "open" and p.opened_at == date.today().isoformat()

    def test_invalid_kind_rejected(self):
        with pytest.raises(PositionError):
            Position(id="x", campaign="c", kind="vibes")

    def test_invalid_status_rejected(self):
        with pytest.raises(PositionError):
            Position(id="x", campaign="c", status="maybe")

    def test_bad_date_caught_at_construction(self):
        """A malformed date found three weeks later, when the position matters,
        is much worse than one caught now."""
        with pytest.raises(PositionError):
            Position(id="x", campaign="c", until="next tuesday")

    def test_days_remaining(self):
        p = Position(id="lp", campaign="base", until=(TODAY + timedelta(days=30)).isoformat())
        assert p.days_remaining(today=TODAY) == 30

    def test_open_ended_has_no_deadline(self):
        assert Position(id="x", campaign="c").days_remaining() is None

    def test_past_due(self):
        p = Position(id="lp", campaign="c", until=(TODAY - timedelta(days=1)).isoformat())
        assert p.is_past_due(today=TODAY)

    def test_round_trip(self):
        p = Position(id="lp", campaign="c", kind="lp", protocol="Aerodrome",
                     until="2026-09-25", amount="$80 ETH/USDC")
        assert Position.from_dict(p.to_dict()).to_dict() == p.to_dict()


# ---------------------------------------------------------------------------
# Store
# ---------------------------------------------------------------------------


class TestStore:
    def test_open_and_list(self, store):
        store.open_position("base", Position(id="lp1", campaign="base", kind="lp"))
        assert [p.id for p in store.open_positions("base")] == ["lp1"]

    def test_duplicate_id_rejected(self, store):
        store.open_position("base", Position(id="lp1", campaign="base"))
        with pytest.raises(PositionError):
            store.open_position("base", Position(id="lp1", campaign="base"))

    def test_close(self, store):
        store.open_position("base", Position(id="lp1", campaign="base"))
        p = store.close_position("base", "lp1")
        assert p.status == "closed" and p.closed_at
        assert store.open_positions("base") == []

    def test_close_as_expired(self, store):
        store.open_position("base", Position(id="b1", campaign="base", kind="badge"))
        assert store.close_position("base", "b1", expired=True).status == "expired"

    def test_close_unknown_raises(self, store):
        with pytest.raises(PositionError):
            store.close_position("base", "nope")

    def test_campaign_field_is_set_from_the_call(self, store):
        """Passing the wrong campaign on the object must not silently win."""
        store.open_position("base", Position(id="lp1", campaign="WRONG"))
        assert store.load("base").positions[0].campaign == "base"

    def test_persists_across_instances(self, tmp_path):
        s1 = PositionStore(tmp_path / "c")
        s1.open_position("base", Position(id="lp1", campaign="base", kind="lp"))
        s2 = PositionStore(tmp_path / "c")
        assert [p.id for p in s2.open_positions("base")] == ["lp1"]


class TestExpiringSoon:
    def test_finds_the_30_day_lp_approaching_its_deadline(self, store):
        store.open_position("base", Position(
            id="lp_far", campaign="base", kind="lp",
            until=(TODAY + timedelta(days=20)).isoformat()))
        store.open_position("base", Position(
            id="lp_soon", campaign="base", kind="lp",
            until=(TODAY + timedelta(days=2)).isoformat()))
        assert [p.id for p in store.expiring_soon("base", days=3)] == ["lp_soon"]

    def test_already_past_due_is_included(self, store):
        store.open_position("base", Position(
            id="lp_late", campaign="base", kind="lp",
            until=(TODAY - timedelta(days=1)).isoformat()))
        assert [p.id for p in store.expiring_soon("base", days=3)] == ["lp_late"]

    def test_sorted_by_urgency(self, store):
        for i, days in enumerate([3, 1, 2]):
            store.open_position("c", Position(
                id=f"p{i}", campaign="c",
                until=(TODAY + timedelta(days=days)).isoformat()))
        # monkeypatch "today" by choosing a window wide enough to include all
        ids = [p.id for p in store.expiring_soon("c", days=5)]
        assert ids == ["p1", "p2", "p0"]

    def test_open_ended_positions_never_expire(self, store):
        store.open_position("c", Position(id="forever", campaign="c"))
        assert store.expiring_soon("c", days=365) == []


# ---------------------------------------------------------------------------
# Streaks
# ---------------------------------------------------------------------------


class TestStreak:
    def test_consecutive_days_increment(self, store):
        for d in (24, 25, 26):
            s = store.record_streak_day("abs", "discover", on=date(2026, 8, d))
        assert s.current == 3 and s.longest == 3

    def test_a_missed_day_resets_it(self, store):
        """Abstract's Discover streak is 30 CONSECUTIVE days. One gap and the
        multiplier is gone — so the model must not paper over a gap."""
        store.record_streak_day("abs", "discover", on=date(2026, 8, 24))
        store.record_streak_day("abs", "discover", on=date(2026, 8, 25))
        s = store.record_streak_day("abs", "discover", on=date(2026, 8, 27))  # skipped 26
        assert s.current == 1
        assert s.longest == 2, "longest must remember the run that was lost"

    def test_same_day_twice_is_idempotent(self, store):
        """A retried run must not inflate a streak."""
        store.record_streak_day("abs", "discover", on=date(2026, 8, 26))
        s = store.record_streak_day("abs", "discover", on=date(2026, 8, 26))
        assert s.current == 1

    def test_at_risk_when_a_daily_streak_missed_today(self, store):
        store.record_streak_day("abs", "discover", on=date(2026, 8, 25))
        assert [s.name for s in store.at_risk_streaks("abs", today=date(2026, 8, 26))] == ["discover"]

    def test_not_at_risk_when_done_today(self, store):
        store.record_streak_day("abs", "discover", on=date(2026, 8, 26))
        assert store.at_risk_streaks("abs", today=date(2026, 8, 26)) == []

    def test_non_daily_streak_is_never_at_risk(self, store):
        st = store.ensure_streak("c", "weekly", required_daily=False)
        store.record_streak_day("c", "weekly", on=date(2026, 8, 1))
        assert store.at_risk_streaks("c", today=date(2026, 8, 26)) == []
        assert st.required_daily is False

    def test_target_completion(self, store):
        st = store.ensure_streak("abs", "discover", target_days=30)
        for i in range(30):
            st = store.record_streak_day("abs", "discover", on=date(2026, 7, 1) + timedelta(days=i))
        assert st.current == 30 and st.is_complete()

    def test_ensure_streak_is_idempotent(self, store):
        a = store.ensure_streak("c", "x", target_days=10)
        b = store.ensure_streak("c", "x", target_days=99)
        assert a is not None and b.target_days == 10, "must not overwrite an existing streak"


# ---------------------------------------------------------------------------
# Summary
# ---------------------------------------------------------------------------


class TestSummary:
    def test_empty_campaign(self, store):
        s = store.summary("nothing", today=TODAY)
        assert s["open_positions"] == 0 and s["streaks"] == {}

    def test_reports_past_due_and_expiring(self, store):
        store.open_position("base", Position(
            id="lp_late", campaign="base", until=(TODAY - timedelta(days=1)).isoformat()))
        store.open_position("base", Position(
            id="lp_soon", campaign="base", until=(TODAY + timedelta(days=2)).isoformat()))
        s = store.summary("base", today=TODAY)
        assert s["past_due"] == ["lp_late"]
        assert set(s["expiring_3d"]) == {"lp_late", "lp_soon"}

    def test_streak_flags(self, store):
        store.ensure_streak("abs", "discover", target_days=30)
        store.record_streak_day("abs", "discover", on=date(2026, 8, 25))
        s = store.summary("abs", today=TODAY)
        assert s["streaks"]["discover"]["at_risk"] is True
        assert s["streaks"]["discover"]["complete"] is False


class TestStateRoundTrip:
    def test_state_serialises_both_collections(self):
        st = State(
            positions=[Position(id="p", campaign="c", kind="lp")],
            streaks=[Streak(name="s", campaign="c", current=5)],
        )
        back = State.from_dict(st.to_dict())
        assert back.positions[0].id == "p"
        assert back.streaks[0].current == 5

    def test_missing_file_gives_empty_state(self, store):
        assert store.load("never-written").positions == []
