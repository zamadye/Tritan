"""Kelly Criterion position sizer with R:R filter + stepped compounding."""
import os


def calculate_position(p_true: float, p_market: float, bankroll: float) -> tuple[float, str, float]:
    # Stepped compounding: Kelly fraction adjusts based on win/loss streak
    from agent.bankroll import get_kelly_multiplier
    base_kelly     = float(os.getenv("KELLY_FRACTION", 0.25))
    kelly_fraction = round(base_kelly * get_kelly_multiplier(), 4)

    max_bet_pct    = float(os.getenv("MAX_BET_PCT_OF_BANKROLL", 0.15))
    min_bet        = float(os.getenv("MIN_BET_SIZE", 1.0))
    max_bet        = float(os.getenv("MAX_BET_SIZE", 3.0))
    edge_threshold = float(os.getenv("EDGE_THRESHOLD", 0.10))
    min_rr         = float(os.getenv("MIN_RR_RATIO", 0.8))

    edge_yes = p_true - p_market
    edge_no  = (1 - p_true) - (1 - p_market)

    if edge_yes >= edge_no and edge_yes > edge_threshold:
        full_kelly = edge_yes / (1 - p_market)
        side = "YES"
        rr = (1 / p_market) - 1
    elif edge_no > edge_threshold:
        full_kelly = edge_no / p_market
        side = "NO"
        rr = (1 / (1 - p_market)) - 1
    else:
        return 0.0, "SKIP", 0.0

    if rr < min_rr:
        return 0.0, "SKIP", 0.0

    size = full_kelly * kelly_fraction * bankroll
    size = min(size, bankroll * max_bet_pct, max_bet)
    size = max(size, min_bet)
    return round(size, 2), side, round(full_kelly, 4)
