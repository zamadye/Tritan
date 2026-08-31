"""Campaign store: persistence, progress tallies, streaks."""
from __future__ import annotations

import json
from datetime import datetime, timedelta, timezone

import pytest

from hermes_airdrop.analyzer import Evidence, score
from hermes_airdrop.campaign import (
    DependencyError,
    STATUS_ACTIVE,
    STATUS_PAUSED,
    ActionSpec,
    Campaign,
    CampaignError,
    Progress,
    Store,
    blocked_by_dependencies,
    resolve_order,
    runnable_now,
    slugify,
)

UTC = timezone.utc


@pytest.fixture
def store(tmp_path):
    return Store(tmp_path / "campaigns")


def camp(**kw):
    base = dict(slug="demo", project="Demo Protocol", url="https://demo.test")
    base.update(kw)
    return Campaign(**base)


class TestSlugify:
    @pytest.mark.parametrize("name,slug", [
        ("Loqua Airdrop", "loqua-airdrop"),
        ("  Weird__Name!!  ", "weird-name"),
        ("ALLCAPS", "allcaps"),
        ("a" * 100, "a" * 64),
    ])
    def test_slugify(self, name, slug):
        assert slugify(name) == slug

    def test_unusable_name_rejected(self):
        with pytest.raises(CampaignError):
            slugify("!!!")


class TestStatuses:
    def test_invalid_status_rejected(self):
        with pytest.raises(CampaignError):
            camp(status="vibing")

    def test_started_at_autofilled(self):
        assert camp().started_at != ""


class TestStore:
    def test_save_and_load(self, store):
        store.save(camp())
        assert store.load("demo").project == "Demo Protocol"

    def test_save_creates_progress_and_screenshot_dir(self, store):
        store.save(camp())
        assert store.progress_path("demo").exists()
        assert store.screenshots_dir("demo").is_dir()

    def test_load_missing_raises(self, store):
        with pytest.raises(CampaignError):
            store.load("ghost")

    def test_main_wallet_tier_is_refused(self, store):
        with pytest.raises(CampaignError) as ei:
            store.save(camp(wallet_tier="main"))
        assert "never used for farming" in str(ei.value)

    def test_farming_tier_accepted(self, store):
        store.save(camp(wallet_tier="farming"))
        assert store.load("demo").wallet_tier == "farming"

    def test_listing_skips_corrupt_entries(self, store):
        store.save(camp())
        store.info_path("demo").write_text("{not json", encoding="utf-8")
        assert store.all() == []

    def test_listing_is_sorted(self, store):
        store.save(camp(slug="b", project="B"))
        store.save(camp(slug="a", project="A"))
        assert [c.slug for c in store.all()] == ["a", "b"]

    def test_len_and_iter(self, store):
        store.save(camp(slug="a", project="A"))
        store.save(camp(slug="b", project="B"))
        assert len(store) == 2
        assert len(list(store)) == 2

    def test_by_status(self, store):
        store.save(camp(slug="a", project="A", status=STATUS_ACTIVE))
        store.save(camp(slug="b", project="B", status="research"))
        assert [c.slug for c in store.by_status(STATUS_ACTIVE)] == ["a"]

    def test_delete(self, store):
        store.save(camp())
        assert store.delete("demo") is True
        assert store.delete("demo") is False

    def test_atomic_write_leaves_no_tmp(self, store):
        store.save(camp())
        assert not list(store.campaign_dir("demo").glob("*.tmp"))

    def test_action_spec_round_trip(self, store):
        c = camp(actions=[ActionSpec(name="check_in", schedule="0 9 * * *", kind="browser")])
        store.save(c)
        loaded = store.load("demo")
        assert loaded.actions[0].name == "check_in"
        assert loaded.actions[0].schedule == "0 9 * * *"


class TestVerdictLinking:
    def test_verdict_stored(self, store):
        store.save(camp())
        v = score(Evidence(project="Demo Protocol", team_insight=3, team_execution=3,
                           team_integrity=3, product_pmf=3, product_delivery=3,
                           product_responsibility=3, narrative_web3=3, narrative_web2=3,
                           narrative_premium=3))
        c = store.record_verdict("demo", v)
        store.save(c)
        assert store.load("demo").verdict["decision"] == "PRIORITIZE"

    def test_skip_verdict_pauses_an_active_campaign(self, store):
        """A SKIP must not leave a campaign running unattended."""
        store.save(camp(status=STATUS_ACTIVE))
        v = score(Evidence(project="Demo Protocol", product_delivery=0))
        assert v.decision == "SKIP"
        c = store.record_verdict("demo", v)
        assert c.status == STATUS_PAUSED

    def test_skip_verdict_leaves_research_alone(self, store):
        store.save(camp(status="research"))
        v = score(Evidence(project="Demo Protocol", product_delivery=0))
        assert store.record_verdict("demo", v).status == "research"


class TestProgress:
    def test_log_ok_accumulates_points(self, store):
        store.save(camp())
        p = store.log_action("demo", "check_in", "ok", points=150)
        store.save_progress(p)
        p = store.log_action("demo", "claim", "ok", points=50)
        assert p.points_today == 200
        assert p.total_points == 200
        assert p.today_actions == ["check_in", "claim"]

    def test_failed_action_records_an_issue(self, store):
        store.save(camp())
        p = store.log_action("demo", "check_in", "failed", "timeout")
        assert p.issues and "timeout" in p.issues[0]
        assert p.total_points == 0

    def test_halted_counts_as_a_problem(self, store):
        store.save(camp())
        p = store.log_action("demo", "check_in", "halted", "captcha")
        assert len(p.issues) == 1

    def test_invalid_log_status_rejected(self, store):
        store.save(camp())
        with pytest.raises(CampaignError):
            store.log_action("demo", "x", "maybe")

    def test_day_rollover_resets_today(self, store):
        store.save(camp())
        d1 = datetime(2026, 8, 25, 9, 0, tzinfo=UTC)
        d2 = datetime(2026, 8, 26, 9, 0, tzinfo=UTC)
        p = store.log_action("demo", "check_in", "ok", points=100, when=d1)
        store.save_progress(p)
        p = store.log_action("demo", "check_in", "ok", points=75, when=d2)
        assert p.points_today == 75
        assert p.total_points == 175
        assert p.days_active == 2

    def test_same_day_does_not_double_count_days(self, store):
        store.save(camp())
        d = datetime(2026, 8, 25, 9, 0, tzinfo=UTC)
        p = store.log_action("demo", "a", "ok", when=d)
        store.save_progress(p)
        p = store.log_action("demo", "b", "ok", when=d + timedelta(hours=1))
        assert p.days_active == 1

    def test_log_is_capped(self, store):
        from hermes_airdrop.campaign import LogEntry

        store.save(camp())
        p = Progress(campaign="demo")
        p.log = [
            LogEntry(ts="2026-08-01T00:00:00+00:00", action="x", status="ok")
            for _ in range(2500)
        ]
        store.save_progress(p)
        p2 = store.log_action("demo", "y", "ok")
        assert len(p2.log) <= 2001
        # The newest entries survive the trim, not the oldest.
        assert p2.log[-1].action == "y"

    def test_progress_round_trip(self, store):
        store.save(camp())
        p = store.log_action("demo", "check_in", "ok", points=10)
        store.save_progress(p)
        loaded = store.load_progress("demo")
        assert loaded.total_points == 10
        assert loaded.log[0].action == "check_in"

    def test_missing_progress_file_gives_defaults(self, store):
        p = store.load_progress("never-saved")
        assert p.campaign == "never-saved"
        assert p.log == []


class TestActionsDue:
    def test_daily_action_is_due(self, store):
        store.save(camp(actions=[ActionSpec(name="check_in", schedule="0 9 * * *")]))
        due = store.actions_due("demo", on=datetime(2026, 8, 26, 0, 0, tzinfo=UTC))
        assert [a.name for a in due] == ["check_in"]

    def test_weekday_action_not_due_on_sunday(self, store):
        store.save(camp(actions=[ActionSpec(name="quest", schedule="0 9 * * 1-5")]))
        sunday = datetime(2026, 8, 30, 0, 0, tzinfo=UTC)  # a Sunday
        assert store.actions_due("demo", on=sunday) == []

    def test_bad_schedule_is_skipped_not_fatal(self, store):
        store.save(camp(actions=[
            ActionSpec(name="broken", schedule="nonsense"),
            ActionSpec(name="good", schedule="0 9 * * *"),
        ]))
        due = store.actions_due("demo", on=datetime(2026, 8, 26, 0, 0, tzinfo=UTC))
        assert [a.name for a in due] == ["good"]


class TestStreak:
    def test_no_log_is_zero(self, store):
        store.save(camp())
        assert store.streak("demo", today=datetime(2026, 8, 25, tzinfo=UTC).date()) == 0

    def test_consecutive_days_counted(self, store):
        store.save(camp())
        for day in (23, 24, 25):
            p = store.log_action("demo", "check_in", "ok",
                                 when=datetime(2026, 8, day, 9, 0, tzinfo=UTC))
            store.save_progress(p)
        from datetime import date
        assert store.streak("demo", today=date(2026, 8, 25)) == 3

    def test_gap_breaks_the_streak(self, store):
        store.save(camp())
        for day in (22, 25):
            p = store.log_action("demo", "check_in", "ok",
                                 when=datetime(2026, 8, day, 9, 0, tzinfo=UTC))
            store.save_progress(p)
        from datetime import date
        assert store.streak("demo", today=date(2026, 8, 25)) == 1

    def test_failed_actions_do_not_count(self, store):
        store.save(camp())
        p = store.log_action("demo", "check_in", "failed",
                             when=datetime(2026, 8, 25, 9, 0, tzinfo=UTC))
        store.save_progress(p)
        from datetime import date
        assert store.streak("demo", today=date(2026, 8, 25)) == 0

    def test_yesterday_only_still_reports(self, store):
        store.save(camp())
        p = store.log_action("demo", "check_in", "ok",
                             when=datetime(2026, 8, 24, 9, 0, tzinfo=UTC))
        store.save_progress(p)
        from datetime import date
        assert store.streak("demo", today=date(2026, 8, 25)) == 1

class TestDependencies:
    """A real campaign is dozens of ordered actions: the faucet must work
    before you can swap, the wallet must be connected before either."""

    def actions(self):
        return [
            ActionSpec(name="swap", depends_on=["faucet"]),
            ActionSpec(name="faucet", depends_on=["add_rpc"]),
            ActionSpec(name="add_rpc"),
            ActionSpec(name="stake", depends_on=["faucet"]),
        ]

    def test_topological_order(self):
        names = [a.name for a in resolve_order(self.actions())]
        assert names.index("add_rpc") < names.index("faucet") < names.index("swap")
        assert names.index("faucet") < names.index("stake")

    def test_missing_dependency_fails_loudly(self):
        """A silently ignored dependency means the agent swaps before the
        faucet ran, and the failure looks like a broken dApp."""
        with pytest.raises(DependencyError) as ei:
            resolve_order([ActionSpec(name="swap", depends_on=["nope"])])
        assert "not defined" in str(ei.value)

    def test_cycle_detected(self):
        with pytest.raises(DependencyError) as ei:
            resolve_order([
                ActionSpec(name="a", depends_on=["b"]),
                ActionSpec(name="b", depends_on=["a"]),
            ])
        assert "circular" in str(ei.value)

    def test_self_cycle_detected(self):
        with pytest.raises(DependencyError):
            resolve_order([ActionSpec(name="a", depends_on=["a"])])

    def test_blocked_by_dependencies(self):
        blocked = blocked_by_dependencies(self.actions(), completed={"add_rpc"})
        assert blocked == {"swap": ["faucet"], "stake": ["faucet"]}

    def test_runnable_now_respects_order_and_completion(self):
        acts = self.actions()
        assert [a.name for a in runnable_now(acts, set())] == ["add_rpc"]
        assert [a.name for a in runnable_now(acts, {"add_rpc"})] == ["faucet"]
        assert sorted(a.name for a in runnable_now(acts, {"add_rpc", "faucet"})) == ["stake", "swap"]
        assert runnable_now(acts, {"add_rpc", "faucet", "swap", "stake"}) == []

    def test_actionspec_round_trip_keeps_dependencies(self):
        a = ActionSpec(name="stake", depends_on=["faucet"], group="apriori",
                       tier="testnet", network="monad-testnet", url="https://stake.apr.io")
        assert ActionSpec.from_dict(a.to_dict()).to_dict() == a.to_dict()

    def test_from_dict_tolerates_null_depends_on(self):
        """JSON null must not become a crash on load."""
        a = ActionSpec.from_dict({"name": "x", "depends_on": None})
        assert a.depends_on == []


class TestResumeFromLedger:
    """A run that dies at step 14 of 40 must resume at 14, not restart."""

    def test_completed_derives_from_verified_log_only(self, store):
        store.save(camp(actions=[ActionSpec(name="a"), ActionSpec(name="b"), ActionSpec(name="c")]))
        store.log_action("demo", "a", "ok")
        store.log_action("demo", "b", "failed", "503")
        assert store.completed_actions("demo") == {"a"}

    def test_next_runnable_skips_completed(self, store):
        store.save(camp(actions=[
            ActionSpec(name="add_rpc"),
            ActionSpec(name="faucet", depends_on=["add_rpc"]),
            ActionSpec(name="swap", depends_on=["faucet"]),
        ]))
        assert [a.name for a in store.next_runnable("demo")] == ["add_rpc"]
        store.log_action("demo", "add_rpc", "ok")
        assert [a.name for a in store.next_runnable("demo")] == ["faucet"]
        store.log_action("demo", "faucet", "ok")
        assert [a.name for a in store.next_runnable("demo")] == ["swap"]

    def test_blocked_reports_what_is_missing(self, store):
        store.save(camp(actions=[
            ActionSpec(name="faucet"),
            ActionSpec(name="swap", depends_on=["faucet"]),
        ]))
        assert store.blocked("demo") == {"swap": ["faucet"]}
