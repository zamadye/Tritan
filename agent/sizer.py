"""Kelly-fractional position sizer — adaptive to edge × confidence."""
import os


def calculate_position(p_true: float, p_market: float, bankroll: float, mode: str = None) -> tuple[float, str, float]:
    from agent.bankroll import get_kelly_multiplier

    min_bet        = float(os.getenv("MIN_BET_SIZE", 0.25))
    max_bet        = float(os.getenv("MAX_BET_SIZE", 3.00))
    edge_threshold = float(os.getenv("EDGE_THRESHOLD", 0.04))
    min_rr         = float(os.getenv("MIN_RR_RATIO", 0.5))

    # Polymarket CLOB minimum order is $1
    if mode == "live" and min_bet < 1.0:
        min_bet = 1.0

    edge_yes = p_true - p_market
    edge_no  = (1 - p_true) - (1 - p_market)

    if edge_yes >= edge_no and edge_yes > edge_threshold:
        side       = "YES"
        edge       = edge_yes
        entry_price = p_market
        rr         = (1 / p_market) - 1
    elif edge_no > edge_threshold:
        side       = "NO"
        edge       = edge_no
        entry_price = 1 - p_market
        rr         = (1 / (1 - p_market)) - 1
    else:
        return 0.0, "SKIP", 0.0

    if rr < min_rr:
        return 0.0, "SKIP", 0.0

    mult = get_kelly_multiplier(mode)
    size = bankroll * 0.25 * edge * mult
    bankroll_cap = max(bankroll * 0.05, min_bet)  # cap never below minimum
    size = min(max(size, min_bet), max_bet, bankroll_cap)
    # Polymarket CLOB hard minimum — never go below $1
    if mode == "live" and size < 1.0:
        size = 1.0
    return round(size, 2), side, round(edge, 4)
