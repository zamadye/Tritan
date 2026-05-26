# Market Analysis — 2026-05-17 17:01 UTC

## Market
- **Question:** Milwaukee Brewers vs. Minnesota Twins
- **Category:** sports
- **YES Price:** 56.0%
- **Days Left:** 7
- **Volume 24h:** $169,143
- **Liquidity:** $374,520

## Statistical Prior
- **p_base:** 59.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.9%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $78,015 (-0.2% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $78,015 (-0.2% 24h) → neutral

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
- → Here's how to watch Sunday's Minnesota Twins vs Milwaukee Brewers game, including start times, TV channels, scores and how to stream.
- [Sun, 17 May 2026] Where to watch Milwaukee Brewers vs Minnesota Twins: TV channel, start time, streaming for May 17
- → &quot;I think we came into this series ​knowing that you cannot give away opportunities against the Brewers just because of the brand of baseball th
- [Sat, 16 May 2026] Brewers turn to another young pitcher in finale vs. Twins
- → View news about the Milwaukee Brewers vs. Minnesota Twins game played on May 17, 2026 including player news, injury news, predictions, analysis and 

## LLM Decision
- **Action:** SKIP
- **Confidence:** 50%
- **p_true:** 59.0%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.20

### Reasoning
Stat signal shows YES overpriced (56% market resolves YES only 44.7% historically, n=13,967), suggesting ~11% edge for NO. However, bookmaker odds align with market price (Brewers 1.73-1.75 = 57-58% implied), indicating market efficiency. Gap is only 3% (below 5% threshold). Injury reports show both teams have minor absences (Woodruff/Buxton). News previews suggest Joe Ryan (Twins) may have an edge, but no breaking catalyst identified. Past decisions for this exact market both SKIPped. Pattern shows sports WR=85% but requires stronger edge threshold.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Brewers'})` → INJURY [milwaukee brewers] Brandon Woodruff (SP): 15-Day-IL
INJURY [milwaukee brewers] Akil Baddoo (
- `get_sports_data({'sport': 'mlb', 'team': 'Twins'})` → INJURY [minnesota twins] Byron Buxton (CF): Day-To-Day
INJURY [minnesota twins] Taj Bradley (SP): 15
- `search_web({'query': 'Milwaukee Brewers recent performance 2025'})` → [Tue, 14 Oct 2025] Google News
[Sun, 19 Oct 2025] Freddy Peralta on his Game 2 performance | 10/14/2
- `search_web({'query': 'Minnesota Twins recent results 2025'})` → [Sat, 27 Sep 2025] Google News
[Fri, 19 Sep 2025] Minnesota Twins at Philadelphia Phillies Game Stor
- `get_market_context({'keyword': 'Brewers Twins'})` → No related markets found for 'Brewers Twins'
- `search_web({'query': 'Brewers vs Twins 2025 game 3 odds'})` → [Sun, 17 May 2026] Google News
[Sat, 16 May 2026] Brewers vs Twins Prediction, Odds, Moneyline, Spre
- `get_odds({'sport': 'baseball_mlb', 'team': 'Brewers'})` → [ODDS] baseball_mlb — 1 events
  Minnesota Twins vs Milwaukee Brewers (2026-05-17)
    [FanDuel] Mil
- `search_web({'query': '"Brewers vs Twins" May 2026 preview pitching matchup'})` → [Sun, 17 May 2026] Google News
[Fri, 15 May 2026] Brewers vs Twins match player stats | 2026 Series 
- `get_odds({'sport': 'baseball_mlb', 'team': 'Twins'})` → [ODDS] baseball_mlb — 1 events
  Minnesota Twins vs Milwaukee Brewers (2026-05-17)
    [FanDuel] Mil
- `search_web({'query': 'Joe Ryan Twins May 17 2026 vs Brewers pitching'})` → [Fri, 15 May 2026] Google News
[Fri, 15 May 2026] Brewers vs. Twins (May 15, 2026) Pregame - ESPN
[S
- `search_web({'query': 'Brewers starting pitcher May 17 2026'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] How to watch Brewers vs. Twins: TV channel and str

## Outcome
**✅ WIN** | P&L: $+0.39 | Resolved: NO

---
*Mode: LIVE | DRY_RUN: true*