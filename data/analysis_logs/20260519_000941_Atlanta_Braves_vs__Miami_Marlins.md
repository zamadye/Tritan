# Market Analysis — 2026-05-19 00:09 UTC

## Market
- **Question:** Atlanta Braves vs. Miami Marlins
- **Category:** sports
- **YES Price:** 39.0%
- **Days Left:** 6
- **Volume 24h:** $630,145
- **Liquidity:** $55,485

## Statistical Prior
- **p_base:** 33.8%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 5.2%

## News Sources Fetched
### Macro Context
- Fear&Greed: 25/100 (Extreme Fear) | trend: deteriorating
- BTC: $76,966 (-0.6% 24h) → neutral
- Fear&Greed: 25/100 (Extreme Fear) | 7d trend: deteriorating
- BTC: $76,972 (-0.1% 24h) → neutral

### General
- [FEAR&GREED 7d trend] 25(Extr) → 28(Fear) → 27(Fear) → 31(Fear) | sentiment worsening
- [SPORTS] Recent games:
- ATL @ MIA | In Progress | Miami Marlins(home) 21-26 score:3 vs Atlanta Braves(away) 32-15 score:0
- [SPORTS] Injuries:
- ?: A.J. Puk — 60-Day-IL (Surgery)
- ?: Jordan Lawlar — 60-Day-IL (Fracture)
- ?: Pavin Smith — 60-Day-IL (Surgery)
- ?: Jacob Wilson — 10-Day-IL (Dislocated)

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: atlanta braves miami marlins
- [Bing News]
- [Mon, 18 May 2026] atlanta braves miami marlins
- → Plate umpire Alfonso M&#225;rquez left in the second inning of Monday's game between the Atlanta Braves and Miami Marlins after being hit in the mas
- [Mon, 18 May 2026] Umpire Alfonso M&#225;rquez leaves in 2nd inning of Braves-Marlins game after being struck by foul ball
- → The Atlanta Braves activated Ronald Acu&#241;a Jr. from the 10-day injured list ahead of Monday’s series opener against the Miami Marlins, clearing 
- [Mon, 18 May 2026] Braves activate Acu&#241;a Jr. from injured list
- → Here's how to watch Monday's Miami Marlins vs Atlanta Braves game, including start times, TV channels, scores and how to stream.

## LLM Decision
- **Action:** SKIP
- **Confidence:** 42%
- **p_true:** 33.8%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.15

### Reasoning
Market overprices YES by 5% (39% vs 34% base rate), suggesting potential NO value. However, critical information is missing: no verified starting pitchers, no current team form data, and odds API unavailable. Braves have 3 players on IL (Farmer, White, Jiménez) but none are core stars. Game is scheduled today (May 18) but no decisive intel found to exploit the gap. Two prior decisions on same matchup were SKIP due to insufficient edge. Without concrete catalyst (ace pitcher matchup, key player return, clear form advantage), cannot confidently take a position despite the apparent overpricing.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** low conf 42%<52%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Atlanta Braves'})` → INJURY [atlanta braves] Kyle Farmer (DH): 10-Day-IL
INJURY [atlanta braves] Eli White (CF): 7-Day IL
- `search_web({'query': 'Atlanta Braves vs Miami Marlins 2025 matchup preview pitching'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] The Scouting Report: Braves vs Marlins, Game One -
- `search_web({'query': 'Braves Marlins May 18 2026 game result score'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] How to watch Braves vs. Marlins: TV channel and st
- `get_market_context({'keyword': 'Braves Marlins MLB'})` → No related markets found for 'Braves Marlins MLB'
- `get_odds({'sport': 'baseball_mlb', 'team': 'Braves'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Braves vs Marlins May 18 2026 odds moneyline betting lines'})` → [Mon, 18 May 2026] Google News
[Sun, 17 May 2026] How to watch Braves vs. Marlins: TV channel and st
- `search_web({'query': '"Braves" "Marlins" "May 18" probable pitchers 2026'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] MLB Probable Pitchers Today: Full Starting Pitcher

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*