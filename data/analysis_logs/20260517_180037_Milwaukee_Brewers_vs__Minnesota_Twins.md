# Market Analysis — 2026-05-17 18:00 UTC

## Market
- **Question:** Milwaukee Brewers vs. Minnesota Twins
- **Category:** sports
- **YES Price:** 55.0%
- **Days Left:** 7
- **Volume 24h:** $170,667
- **Liquidity:** $386,242

## Statistical Prior
- **p_base:** 57.5%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $78,035 (-0.2% 24h) → neutral
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
- → The Milwaukee Brewers go for the sweep of the Minnesota Twins on May 17 at Target Field. Robert Gasser, freshly called up from Class AAA Nashville, 
- [Sun, 17 May 2026] Milwaukee Brewers vs Minnesota Twins score, lineups, live updates
- → Gasser’s back… back… back… back again ...
- [Sun, 17 May 2026] Game thread #44: Milwaukee Brewers (26-17) @ Minnesota Twins (20-26)
- → Here's how to watch Sunday's Minnesota Twins vs Milwaukee Brewers game, including start times, TV channels, scores and how to stream.

## LLM Decision
- **Action:** SKIP
- **Confidence:** 52%
- **p_true:** 57.5%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_PATTERN
- **Catalyst Strength:** 0.60

### Reasoning
Stat signal suggests YES at 55% is overpriced (historical 44.7% resolution), but bookmaker odds show Brewers as favorites (~58.7% implied). Gap of only 2% is below 5% threshold. Conflicting signals prevent actionable edge.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=2%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Brewers'})` → INJURY [milwaukee brewers] Brandon Woodruff (SP): 15-Day-IL
INJURY [milwaukee brewers] Akil Baddoo (
- `get_sports_data({'sport': 'mlb', 'team': 'Twins'})` → INJURY [minnesota twins] Byron Buxton (CF): Day-To-Day
INJURY [minnesota twins] Taj Bradley (SP): 15
- `search_web({'query': 'Milwaukee Brewers vs Minnesota Twins 2025 season series'})` → [Sun, 22 Jun 2025] Google News
[Fri, 06 Mar 2026] Milwaukee Brewers at Minnesota Twins Game Story, S
- `search_web({'query': 'Minnesota Twins recent performance June 2025'})` → [Mon, 17 Nov 2025] Google News
[Sun, 17 Aug 2025] Which Minnesota Twins All-Star Will Be Traded Firs
- `search_web({'query': 'Twins vs Brewers series June 2025'})` → [Sun, 22 Jun 2025] Google News
[Fri, 06 Mar 2026] Milwaukee Brewers at Minnesota Twins Game Story, S
- `get_odds({'sport': 'baseball_mlb', 'team': 'Brewers'})` → [ODDS] baseball_mlb — 2 events
  Minnesota Twins vs Milwaukee Brewers (2026-05-17)
    [FanDuel] Mil
- `search_web({'query': 'Milwaukee Brewers schedule next game June 2025'})` → [Mon, 03 Nov 2025] Google News
[Sat, 11 Oct 2025] Play ball! The 2026 Milwaukee Brewers schedule is 

## Outcome
**✅ WIN** | P&L: $+0.39 | Resolved: NO

---
*Mode: LIVE | DRY_RUN: true*