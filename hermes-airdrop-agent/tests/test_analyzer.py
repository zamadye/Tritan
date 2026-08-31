"""Scoring behaviour of the 4-dimension filter."""
from __future__ import annotations

import pytest

from hermes_airdrop.analyzer import (
    CONSIDER,
    PRIORITIZE,
    SKIP,
    Evidence,
    Verdict,
    score,
)

STRONG = dict(
    team_insight=3, team_execution=3, team_integrity=3,
    product_pmf=3, product_delivery=3, product_responsibility=3,
    narrative_web3=3, narrative_web2=3, narrative_premium=3,
    timing_fomo=0, timing_cost=0, timing_crowding=0,
)


def make(**kw):
    return Evidence(project=kw.pop("project", "Test Protocol"), **{**STRONG, **kw})


class TestScoring:
    def test_perfect_project_is_prioritize(self):
        v = score(make())
        assert v.decision == PRIORITIZE
        assert v.overall == 10.0

    def test_all_zero_is_skip(self):
        v = score(make(**{k: (0 if k.startswith(("team", "product", "narrative")) else 3)
                          for k in STRONG}))
        assert v.decision == SKIP

    def test_score_is_deterministic(self):
        e = make(product_pmf=2, narrative_web2=1)
        assert score(e).to_dict() == score(e).to_dict()

    def test_weights_sum_to_one(self):
        from hermes_airdrop.analyzer import WEIGHTS
        assert abs(sum(WEIGHTS.values()) - 1.0) < 1e-9

    def test_product_weighs_more_than_narrative(self):
        # Degrade product vs degrade narrative by the same amount.
        from hermes_airdrop.analyzer import WEIGHTS
        assert WEIGHTS["product"] > WEIGHTS["narrative"]

    def test_empty_project_rejected(self):
        with pytest.raises(ValueError):
            score(Evidence(project="   "))

    def test_rating_out_of_range_rejected(self):
        with pytest.raises(ValueError):
            Evidence(project="X", team_insight=4)

    def test_non_int_rating_rejected(self):
        with pytest.raises(TypeError):
            Evidence(project="X", product_pmf=2.5)  # type: ignore[arg-type]


class TestTeamGate:
    """The source is explicit: 'Smart enough, good enough execution, good
    enough heart. None can be missing.' A weak link must cap the dimension."""

    def test_weak_integrity_caps_team_score(self):
        good = score(make(team_integrity=3))
        capped = score(make(team_integrity=0))
        team = {d.name: d.score for d in good.dimensions}
        team_capped = {d.name: d.score for d in capped.dimensions}
        assert team_capped["team"] < team["team"]
        assert team_capped["team"] == 0.0  # a 0 anywhere in team zeroes it

    def test_other_dimensions_unaffected_by_team_cap(self):
        a = score(make(team_integrity=3))
        b = score(make(team_integrity=0))
        da = {d.name: d.score for d in a.dimensions}
        db = {d.name: d.score for d in b.dimensions}
        assert da["product"] == db["product"]
        assert da["narrative"] == db["narrative"]


class TestVetoes:
    def test_shoddy_delivery_forces_skip_despite_high_score(self):
        v = score(make(product_delivery=0))
        assert v.decision == SKIP
        assert any("delivery" in x.lower() for x in v.vetoes)
        assert v.overall <= 4.0  # capped so the report can't read "great but skipped"

    def test_crowded_forces_skip(self):
        v = score(make(timing_crowding=3))
        assert v.decision == SKIP
        assert any("crowd" in x.lower() for x in v.vetoes)

    def test_hesitation_forces_skip(self):
        v = score(make(hesitating=True))
        assert v.decision == SKIP
        assert any("hesitat" in x.lower() for x in v.vetoes)

    def test_high_cost_plus_fomo_forces_skip(self):
        v = score(make(timing_cost=3, timing_fomo=2))
        assert v.decision == SKIP

    def test_high_cost_without_fomo_does_not_veto(self):
        v = score(make(timing_cost=3, timing_fomo=0))
        assert not any("FOMO" in x for x in v.vetoes)

    def test_no_vetoes_on_strong_project(self):
        assert score(make()).vetoes == ()


class TestTimingIsInverse:
    def test_peak_fomo_scores_worse_than_calm(self):
        calm = score(make(timing_fomo=0))
        peak = score(make(timing_fomo=3))
        tc = {d.name: d.score for d in calm.dimensions}["timing"]
        tp = {d.name: d.score for d in peak.dimensions}["timing"]
        assert tp < tc

    def test_all_inverse_signals_at_zero_is_perfect_timing(self):
        v = score(make(timing_fomo=0, timing_cost=0, timing_crowding=0))
        assert {d.name: d.score for d in v.dimensions}["timing"] == 10.0


class TestConfidence:
    def test_decisive_ratings_give_full_confidence(self):
        assert score(make()).confidence == 1.0

    def test_middle_ratings_drop_confidence_below_review_threshold(self):
        middles = {k: 2 for k in STRONG if k.startswith(("team", "product", "narrative"))}
        v = score(make(**middles))
        assert v.confidence < 0.7
        assert v.needs_review is True

    def test_confidence_bounds(self):
        for ev in (make(), make(**{k: 1 for k in STRONG})):
            assert 0.0 <= score(ev).confidence <= 1.0


class TestOutput:
    def test_render_contains_required_fields(self):
        text = score(make()).render()
        for token in ("Project:", "Overall Score:", "Decision:", "Reasoning:", "Recommended Actions:"):
            assert token in text

    def test_to_dict_round_trips_through_json(self):
        import json
        d = score(make()).to_dict()
        assert json.loads(json.dumps(d))["decision"] == PRIORITIZE

    def test_needs_review_false_when_confident(self):
        assert score(make()).needs_review is False


class TestEvidenceIO:
    def test_dict_round_trip(self):
        e = make(project="Round Trip", url="https://x.test")
        assert Evidence.from_dict(e.to_dict()).to_dict() == e.to_dict()

    def test_unknown_keys_ignored_on_load(self):
        d = make().to_dict()
        d["not_a_field"] = 1
        Evidence.from_dict(d)  # must not raise
