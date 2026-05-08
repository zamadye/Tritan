"""Core unit tests for TRITAN — no API calls, no external dependencies."""
import json
import sys
import os
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))


# ── Category Inference ────────────────────────────────────────────────────────

from agent.learner import _infer_category

class TestCategoryInference:
    def test_geopolitik_before_sports(self):
        """US-Iran diplomatic meeting must be geopolitik, not sports."""
        t = {"market_question": "US x Iran diplomatic meeting by May 15, 2026?"}
        assert _infer_category(t) == "geopolitik"

    def test_sports_detection(self):
        assert _infer_category({"market_question": "Cavaliers vs Pistons NBA"}) == "sports"

    def test_crypto_detection(self):
        assert _infer_category({"market_question": "Will Bitcoin reach $90,000?"}) == "crypto"

    def test_politics_detection(self):
        assert _infer_category({"market_question": "Will the Senate pass the bill?"}) == "politics"

    def test_category_field_takes_priority(self):
        """Explicit category field overrides keyword inference."""
        t = {"category": "economics", "market_question": "Will Bitcoin crash?"}
        assert _infer_category(t) == "economics"

    def test_fallback_to_other(self):
        assert _infer_category({"market_question": "Will it rain tomorrow?"}) == "other"


# ── Position Sizer ────────────────────────────────────────────────────────────

from agent.sizer import calculate_position

class TestPositionSizer:
    def test_bet_yes_when_p_true_above_market(self):
        size, side, _ = calculate_position(p_true=0.70, p_market=0.50, bankroll=20.0)
        assert side == "YES"
        assert size > 0

    def test_bet_no_when_p_true_below_market(self):
        size, side, _ = calculate_position(p_true=0.30, p_market=0.55, bankroll=20.0)
        assert side == "NO"
        assert size > 0

    def test_skip_when_no_edge(self):
        size, side, _ = calculate_position(p_true=0.50, p_market=0.50, bankroll=20.0)
        assert side == "SKIP" or size == 0

    def test_size_capped_at_max_bet(self):
        """Position size must not exceed MAX_BET_SIZE."""
        os.environ["MAX_BET_SIZE"] = "3.00"
        size, side, _ = calculate_position(p_true=0.99, p_market=0.01, bankroll=1000.0)
        assert size <= 3.0

    def test_size_floored_at_min_bet(self):
        """Position size must be at least MIN_BET_SIZE when betting."""
        os.environ["MIN_BET_SIZE"] = "1.00"
        size, side, _ = calculate_position(p_true=0.60, p_market=0.50, bankroll=20.0)
        if side != "SKIP":
            assert size >= 1.0

    def test_zero_bankroll_returns_skip(self):
        size, side, _ = calculate_position(p_true=0.70, p_market=0.50, bankroll=0.0)
        assert side == "SKIP" or size == 0


# ── Statistical Prior ─────────────────────────────────────────────────────────

from agent.analyzer import get_statistical_prior

class TestStatisticalPrior:
    def test_returns_p_base(self):
        market = {"question": "Will X happen?", "price": 0.50, "category": "sports"}
        result = get_statistical_prior(market)
        assert "p_base" in result
        assert 0 < result["p_base"] < 1

    def test_p_base_is_float(self):
        market = {"question": "Will BTC hit 90k?", "price": 0.35, "category": "crypto"}
        result = get_statistical_prior(market)
        assert isinstance(result["p_base"], float)

    def test_returns_sample_size(self):
        market = {"question": "Will X happen?", "price": 0.60, "category": "other"}
        result = get_statistical_prior(market)
        assert "n" in result
        assert result["n"] >= 0

    def test_source_field_present(self):
        market = {"question": "Will X happen?", "price": 0.50, "category": "sports"}
        result = get_statistical_prior(market)
        assert "source" in result


# ── Pattern Library ───────────────────────────────────────────────────────────

from agent.patterns import get_pattern_context, build_pattern_library

class TestPatternLibrary:
    def test_returns_string(self):
        result = get_pattern_context("sports", 0.52, 0.60)
        assert isinstance(result, str)

    def test_no_crash_on_missing_data(self):
        """Should return empty string gracefully when no data."""
        result = get_pattern_context("unknown_category", 0.5, 0.5)
        assert isinstance(result, str)

    def test_build_does_not_crash(self):
        """build_pattern_library should not raise even with minimal data."""
        try:
            build_pattern_library("demo")
        except Exception as e:
            pytest.fail(f"build_pattern_library raised: {e}")


# ── Trade Log Integrity ───────────────────────────────────────────────────────

class TestTradeLogIntegrity:
    def setup_method(self):
        from pathlib import Path
        log = Path("data/demo_trades.json")
        self.trades = json.loads(log.read_text()) if log.exists() else []

    def test_trade_log_is_list(self):
        assert isinstance(self.trades, list)

    def test_required_fields_present(self):
        required = ["trade_id", "timestamp", "market_question", "side", "size_usd", "price_at_entry"]
        for trade in self.trades[:10]:
            for field in required:
                assert field in trade, f"Missing field '{field}' in trade {trade.get('trade_id')}"

    def test_no_duplicate_open_positions(self):
        """Same market should not have more than one open position."""
        open_trades = [t for t in self.trades if not t.get("actual_outcome")]
        questions = [t["market_question"][:60] for t in open_trades]
        assert len(questions) == len(set(questions)), "Duplicate open positions detected"

    def test_pnl_present_on_resolved(self):
        resolved = [t for t in self.trades if t.get("actual_outcome")]
        for t in resolved:
            assert "pnl" in t, f"Missing pnl on resolved trade {t.get('trade_id')}"
