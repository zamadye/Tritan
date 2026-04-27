"""
Stepped Compounding Bankroll Manager.

Rules:
- Bet size steps UP only after WIN_STREAK_TO_INCREASE consecutive wins
- Bet size steps DOWN after LOSS_STREAK_TO_DECREASE consecutive losses
- Steps are % of base bankroll, not absolute
- Prevents wild swings from single win/loss
"""
import os
import json
from pathlib import Path


WIN_STREAK_TO_INCREASE  = int(os.getenv("WIN_STREAK_TO_INCREASE", 3))
LOSS_STREAK_TO_DECREASE = int(os.getenv("LOSS_STREAK_TO_DECREASE", 3))  # 3 loss baru turun level
STEP_SIZE               = float(os.getenv("BANKROLL_STEP_SIZE", 0.10))
MAX_LEVEL               = int(os.getenv("MAX_BANKROLL_LEVEL", 5))
MIN_LEVEL               = int(os.getenv("MIN_BANKROLL_LEVEL", -2))
STATE_FILE              = os.getenv("BANKROLL_STATE_FILE", "./data/bankroll_state.json")


def _wins_needed(current_level: int) -> int:
    """
    Wins needed to go up one level:
    Level 0→1: 3 wins
    Level 1→2: 2 wins
    Level 2+→next: 1 win
    """
    if current_level <= 0:
        return 3
    elif current_level == 1:
        return 2
    else:
        return 1


def _load_state() -> dict:
    p = Path(STATE_FILE)
    if p.exists():
        return json.loads(p.read_text())
    return {"level": 0, "win_streak": 0, "loss_streak": 0, "total_trades": 0}


def _save_state(state: dict):
    Path(STATE_FILE).parent.mkdir(parents=True, exist_ok=True)
    Path(STATE_FILE).write_text(json.dumps(state, indent=2))


def update_streak(won: bool):
    """Call after each resolved trade to update streak and level."""
    state = _load_state()

    if won:
        state["win_streak"]  += 1
        state["loss_streak"]  = 0
        needed = _wins_needed(state["level"])
        if state["win_streak"] >= needed:
            if state["level"] < MAX_LEVEL:
                state["level"] += 1
                state["win_streak"] = 0
                print(f"[BANKROLL] 📈 Level UP → {state['level']} (after {needed} wins)")
    else:
        state["loss_streak"] += 1
        state["win_streak"]   = 0
        if state["loss_streak"] >= LOSS_STREAK_TO_DECREASE:
            if state["level"] > MIN_LEVEL:
                state["level"] -= 1
                state["loss_streak"] = 0  # reset streak after level down
                print(f"[BANKROLL] 📉 Level DOWN → {state['level']} (after {LOSS_STREAK_TO_DECREASE} losses)")

    state["total_trades"] += 1
    _save_state(state)
    return state


def get_kelly_multiplier() -> float:
    """
    Returns Kelly fraction multiplier based on current level.
    Level 0  = base (0.25 Kelly)
    Level +1 = 0.25 * 1.10 = 0.275
    Level +2 = 0.25 * 1.20 = 0.30
    Level -1 = 0.25 * 0.90 = 0.225
    Level -2 = 0.25 * 0.80 = 0.20
    """
    state = _load_state()
    level = state.get("level", 0)
    multiplier = 1.0 + (level * STEP_SIZE)
    multiplier = max(0.5, min(2.0, multiplier))  # clamp 0.5x to 2.0x
    return round(multiplier, 3)


def get_status() -> dict:
    state = _load_state()
    mult = get_kelly_multiplier()
    base_kelly = float(os.getenv("KELLY_FRACTION", 0.25))
    effective_kelly = round(base_kelly * mult, 4)
    return {
        "level":           state.get("level", 0),
        "win_streak":      state.get("win_streak", 0),
        "loss_streak":     state.get("loss_streak", 0),
        "multiplier":      mult,
        "effective_kelly": effective_kelly,
        "total_trades":    state.get("total_trades", 0),
    }
