"""Kelly-fractional position sizer — adaptive to edge × confidence."""
import os


def calculate_position(p_true: float, p_market: float, bankroll: float) -> tuple[float, str, float]:
    from agent.bankroll import get_kelly_multiplier

    min_bet        = float(os.getenv("MIN_BET_SIZE", 0.25))
    max_bet        = float(os.getenv("MAX_BET_SIZE", 1.00))
    edge_threshold = float(os.getenv("EDGE_THRESHOLD", 0.04))
    min_rr         = float(os.getenv("MIN_RR_RATIO", 0.5))

    edge_yes = p_true - p_market
    edge_no  = (1 - p_true) - (1 - p_market)

    if edge_yes >= edge_no and edge_yes > edge_threshold:
        side = "YES"
        edge = edge_yes
        rr   = (1 / p_market) - 1
    elif edge_no > edge_threshold:
        side = "NO"
        edge = edge_no
        rr   = (1 / (1 - p_market)) - 1
    else:
        return 0.0, "SKIP", 0.0

    if rr < min_rr:
        return 0.0, "SKIP", 0.0

    # Kelly-fractional: size = bankroll × 0.25 × edge × confidence_multiplier
    # confidence injected via get_kelly_multiplier (streak-based)
    mult = get_kelly_multiplier()  # 0.8x–2.0x based on win/loss streak
    size = bankroll * 0.25 * edge * mult

    # Clamp to min/max and 5% bankroll
    size = min(max(size, min_bet), max_bet, bankroll * 0.05)
    return round(size, 2), side, round(edge, 4)
