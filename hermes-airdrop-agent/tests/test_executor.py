"""Plan building and weekly rollup."""
from __future__ import annotations

from datetime import datetime, timezone

import pytest

from hermes_airdrop.campaign import STATUS_ACTIVE, ActionSpec, Campaign, Store
from hermes_airdrop.executor import build_plan, summarize

UTC = timezone.utc
TUE = datetime(2026, 8, 25, 8, 0, tzinfo=UTC)   # a Tuesday
SUN = datetime(2026, 8, 30, 8, 0, tzinfo=UTC)   # a Sunday


@pytest.fixture
def store(tmp_path):
    s = Store(tmp_path / "campaigns")
    s.save(Campaign(slug="loqua", project="Loqua", status=STATUS_ACTIVE,
                    actions=[ActionSpec(name="check_in", schedule="0 9 * * *")]))
    s.save(Campaign(slug="orbital", project="Orbital", status=STATUS_ACTIVE,
                    actions=[ActionSpec(name="quest", schedule="0 9 * * 1-5")]))
    s.save(Campaign(slug="sleeping", project="Sleeping", status="research"))
    return s


class TestPlan:
    def test_active_campaigns_are_planned(self, store):
        plan = build_plan(store, on=TUE)
        names = {(a.campaign, a.action) for a in plan.actions}
        assert ("loqua", "check_in") in names

    def test_inactive_campaigns_excluded(self, store):
        plan = build_plan(store, on=TUE)
        assert all(a.campaign != "sleeping" for a in plan.actions)

    def test_weekday_action_skipped_on_sunday(self, store):
        plan = build_plan(store, on=SUN)
        assert {(a.campaign, a.action) for a in plan.actions} == {("loqua", "check_in")}

    def test_spend_action_needs_approval(self, store):
        store.save(Campaign(slug="br", project="Bridge Test", status=STATUS_ACTIVE,
                            actions=[ActionSpec(name="bridge", schedule="0 9 * * *")]))
        plan = build_plan(store, on=TUE)
        bridge = next(a for a in plan.actions if a.action == "bridge")
        assert bridge.needs_approval is True
        assert bridge.severity == "needs_approval"

    def test_preapproved_action_runs_unattended(self, store):
        plan = build_plan(store, on=TUE, approved_actions=frozenset({"check_in"}))
        ci = next(a for a in plan.actions if a.action == "check_in")
        assert ci.needs_approval is False
        assert ci.severity == "scheduled"

    def test_wallet_action_is_blocked(self, store):
        store.save(Campaign(slug="sig", project="Sig", status=STATUS_ACTIVE,
                            actions=[ActionSpec(name="claim", schedule="0 9 * * *", kind="wallet")]))
        plan = build_plan(store, on=TUE)
        claim = next(a for a in plan.actions if a.campaign == "sig")
        assert claim.severity == "blocked"
        assert "does not hold keys" in claim.blocked_by

    def test_no_active_campaigns_warns(self, tmp_path):
        plan = build_plan(Store(tmp_path / "c"), on=TUE)
        assert any("No campaigns have status 'active'" in w for w in plan.warnings)

    def test_active_but_unscheduled_warns(self, tmp_path):
        s = Store(tmp_path / "c")
        s.save(Campaign(slug="idle", project="Idle", status=STATUS_ACTIVE))
        plan = build_plan(s, on=TUE)
        assert any("nothing scheduled" in w for w in plan.warnings)

    def test_bad_schedule_warns_but_does_not_crash(self, store):
        store.save(Campaign(slug="bad", project="Bad", status=STATUS_ACTIVE,
                            actions=[ActionSpec(name="x", schedule="garbage")]))
        plan = build_plan(store, on=TUE)
        assert any("bad schedule" in w for w in plan.warnings)

    def test_plan_shape(self, store):
        d = build_plan(store, on=TUE).to_dict()
        assert d["on"] == "2026-08-25"
        assert d["counts"]["total"] == len(d["actions"])
        for a in d["actions"]:
            assert "severity" in a

    def test_render_lists_every_action(self, store):
        text = build_plan(store, on=TUE).render()
        assert "loqua" in text and "check_in" in text
        assert "Airdrop plan for 2026-08-25" in text

    def test_render_when_empty(self, tmp_path):
        assert "nothing due" in build_plan(Store(tmp_path / "c"), on=TUE).render()

    def test_streaks_included(self, store):
        store.log_action("loqua", "check_in", "ok", when=TUE)
        plan = build_plan(store, on=TUE)
        assert plan.streaks["loqua"] == 1


class TestSummarize:
    def test_rollup_counts(self, store):
        store.log_action("loqua", "check_in", "ok", points=100, when=TUE)
        store.log_action("loqua", "claim", "failed", when=TUE)
        data = summarize(store, since_days=7, now=TUE)
        row = next(r for r in data["campaigns"] if r["campaign"] == "loqua")
        assert row["actions_7d"] == 2
        assert row["ok_7d"] == 1
        assert row["failure_rate_7d"] == 0.5
        assert row["total_points"] == 100

    def test_totals(self, store):
        store.log_action("loqua", "check_in", "ok", points=100, when=TUE)
        t = summarize(store, now=TUE)["totals"]
        assert t["campaigns"] == 3
        assert t["active"] == 2
        assert t["points"] == 100

    def test_old_actions_excluded_from_window(self, store):
        old = datetime(2026, 8, 1, 9, 0, tzinfo=UTC)
        store.log_action("loqua", "check_in", "ok", when=old)
        row = next(r for r in summarize(store, since_days=7, now=TUE)["campaigns"]
                   if r["campaign"] == "loqua")
        assert row["actions_7d"] == 0

    def test_empty_store(self, tmp_path):
        data = summarize(Store(tmp_path / "c"), now=TUE)
        assert data["campaigns"] == []
        assert data["totals"]["campaigns"] == 0

    def test_rows_sorted_by_activity(self, store):
        store.log_action("orbital", "quest", "ok", when=TUE)
        data = summarize(store, now=TUE)
        assert data["campaigns"][0]["campaign"] == "orbital"

    def test_unrated_campaign_labelled(self, store):
        row = next(r for r in summarize(store, now=TUE)["campaigns"]
                   if r["campaign"] == "sleeping")
        assert row["verdict"] == "unrated"
