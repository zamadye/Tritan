# Market Analysis — 2026-05-17 17:50 UTC

## Market
- **Question:** Milwaukee Brewers vs. Minnesota Twins
- **Category:** sports
- **YES Price:** 56.0%
- **Days Left:** 7
- **Volume 24h:** $170,661
- **Liquidity:** $390,486

## Statistical Prior
- **p_base:** 59.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.9%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $78,005 (-0.3% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $77,915 (-0.4% 24h) → neutral

### General
- [FEAR&GREED 7d trend] 27(Fear) → 31(Fear) → 43(Fear) → 34(Fear) | sentiment worsening
- [SPORTS] Recent games:
- MIL @ MIN | Scheduled | Minnesota Twins(home) 20-26 score:0 vs Milwaukee Brewers(away) 26-17 score:0
- [SPORTS] Injuries:
- ?: Pavin Smith — 60-Day-IL (Surgery)
- ?: Carlos Santana — 10-Day-IL (Strain)
- ?: Jordan Lawlar — 60-Day-IL (Fracture)
- ?: Denzel Clarke — 10-Day-IL (Bruise)

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: milwaukee brewers minnesota twins
- [Bing News]
- [Sun, 17 May 2026] milwaukee brewers minnesota twins
- → Robert Gasser makes his season debut for the Brewers on May 17 against the Twins ...
- [Sun, 17 May 2026] Milwaukee Brewers vs Minnesota Twins score, lineups, live updates
- → Gasser’s back… back… back… back again ...
- [Sun, 17 May 2026] Game thread #44: Milwaukee Brewers (26-17) @ Minnesota Twins (20-26)
- → Milwaukee Brewers right-hander Logan Henderson was a key piece in another win, this time over the Minnesota Twins.

## LLM Decision
- **Action:** SKIP
- **Confidence:** 58%
- **p_true:** 59.0%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_PATTERN
- **Catalyst Strength:** 0.45

### Reasoning
Stat signal shows markets at 56% YES resolve YES only 44.7% historically (n=13,967), suggesting YES is overpriced by ~11%. However, the gap between market (56%) and base rate (59%) is only 3%, falling below the 5% action threshold. Bookmaker odds (FanDuel/Paddy Power) imply Brewers at 58-60%, which aligns with base rate but exceeds market price, creating conflicting signals. No game-specific breaking catalyst: Brewers won previous meeting 2-1, Yelich (back) out but not a major lineup impact, Buxton (Day-to-Day) for Twins. Two prior SKIP decisions on this exact market due to gap <5%. While the statistical pattern is verifiable, the gap remains too narrow for actionable edge. Monitor for gap widening to 5%+ or concrete injury news affecting starting pitchers.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Brewers'})` → INJURY [milwaukee brewers] Brandon Woodruff (SP): 15-Day-IL
INJURY [milwaukee brewers] Akil Baddoo (
- `get_sports_data({'sport': 'mlb', 'team': 'Twins'})` → INJURY [minnesota twins] Byron Buxton (CF): Day-To-Day
INJURY [minnesota twins] Taj Bradley (SP): 15
- `search_web({'query': 'Milwaukee Brewers vs Minnesota Twins 2025 game'})` → [Fri, 15 May 2026] Google News
[Sat, 16 May 2026] Brewers vs Twins betting preview: Why Minnesota's 
- `search_web({'query': 'Brewers Twins injury update'})` → [Sun, 17 May 2026] Google News
[Sat, 16 May 2026] Jackson Chourio spoils strong Connor Prielipp star
- `get_odds({'sport': 'baseball_mlb', 'team': 'Brewers'})` → [ODDS] baseball_mlb — 1 events
  Minnesota Twins vs Milwaukee Brewers (2026-05-17)
    [FanDuel] Mil
- `get_market_context({'keyword': 'Brewers Twins'})` → No related markets found for 'Brewers Twins'
- `get_odds({'sport': 'baseball_mlb', 'team': 'Twins'})` → [ODDS] baseball_mlb — 1 events
  Minnesota Twins vs Milwaukee Brewers (2026-05-17)
    [FanDuel] Mil

## Outcome
**✅ WIN** | P&L: $+0.39 | Resolved: NO

---
*Mode: LIVE | DRY_RUN: true*