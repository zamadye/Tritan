"""High-frequency flat bet sizer with stepped compounding multiplier."""
import os


def calculate_position(p_true: float, p_market: float, bankroll: float) -> tuple[float, str, float]:
    from agent.bankroll import get_kelly_multiplier

    min_bet        = float(os.getenv("MIN_BET_SIZE", 0.50))
    max_bet        = float(os.getenv("MAX_BET_SIZE", 1.00))
    edge_threshold = float(os.getenv("EDGE_THRESHOLD", 0.04))
    min_rr         = float(os.getenv("MIN_RR_RATIO", 0.5))

    edge_yes = p_true - p_market
    edge_no  = (1 - p_true) - (1 - p_market)

    if edge_yes >= edge_no and edge_yes > edge_threshold:
        side = "YES"
        rr   = (1 / p_market) - 1
    elif edge_no > edge_threshold:
        side = "NO"
        rr   = (1 / (1 - p_market)) - 1
    else:
        return 0.0, "SKIP", 0.0

    if rr < min_rr:
        return 0.0, "SKIP", 0.0

    # Flat bet size scaled by compounding level
    mult = get_kelly_multiplier()  # 0.8x to 2.0x based on streak
    size = min_bet * mult
    size = min(max(size, min_bet), max_bet, bankroll * 0.05)  # never >5% bankroll
    return round(size, 2), side, round(edge_yes if side=="YES" else edge_no, 4)
