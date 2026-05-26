# Market Analysis — 2026-05-17 17:16 UTC

## Market
- **Question:** Baltimore Orioles vs. Washington Nationals
- **Category:** sports
- **YES Price:** 53.0%
- **Days Left:** 7
- **Volume 24h:** $70,994
- **Liquidity:** $539,376

## Statistical Prior
- **p_base:** 54.5%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 1.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $77,984 (-0.3% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $77,873 (-0.4% 24h) → neutral

### General
- [FEAR&GREED 7d trend] 27(Fear) → 31(Fear) → 43(Fear) → 34(Fear) | sentiment worsening
- [SPORTS] Recent games:
- BAL @ WSH | Scheduled | Washington Nationals(home) 23-23 score:0 vs Baltimore Orioles(away) 20-26 score:0
- [SPORTS] Injuries:
- ?: Pavin Smith — 60-Day-IL (Surgery)
- ?: Carlos Santana — 10-Day-IL (Strain)
- ?: Jordan Lawlar — 60-Day-IL (Fracture)
- ?: Denzel Clarke — 10-Day-IL (Bruise)

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: baltimore orioles washington nationals
- [Bing News]
- [] baltimore orioles washington nationals
- [Metaculus]
- [] Will the next IPC Sudan acute food insecurity analysis classify at lea
- → Community: pending
- [] Will Bitcoin trade above $120,000 before August 1, 2026?
- → Community: pending

## LLM Decision
- **Action:** SKIP
- **Confidence:** 62%
- **p_true:** 46.5%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_PATTERN
- **Catalyst Strength:** 0.70

### Reasoning
Strong statistical signal: markets priced at 53% historically resolve YES only 44.7% (n=13,967), indicating 8.3% overpricing of YES. Both teams have comparable injury situations (Orioles: Mountcastle, Westburg, Helsley; Nationals: Herz, Henry, Beeter) with no clear advantage. Bookmaker odds (~52.5% true prob for Orioles) align with market, but the large-sample stat pattern overrides this consensus. No new breaking news or catalysts to change the assessment. The small gap (+1%) is misleading—edge comes from the stat signal, not the gap metric. Sports pattern WR=85% from 13 trades provides additional support.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=1%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Baltimore Orioles'})` → INJURY [baltimore orioles] Ryan Mountcastle (1B): 60-Day-IL
INJURY [baltimore orioles] Jordan Westbu
- `search_web({'query': 'Baltimore Orioles vs Washington Nationals game today'})` → [Sat, 16 May 2026] Google News
[Sat, 16 May 2026] Orioles vs. Nationals (May 16, 2026) Game Stats - 
- `search_web({'query': 'Orioles Nationals prediction May 2025'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Orioles vs Nationals Prediction, Odds, Moneyline, 
- `search_web({'query': 'Orioles Nationals prediction May 2025'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] Orioles vs Nationals Prediction, Odds, Moneyline, 
- `get_odds({'sport': 'baseball_mlb', 'team': 'Orioles'})` → [ODDS] baseball_mlb — 1 events
  Washington Nationals vs Baltimore Orioles (2026-05-17)
    [FanDuel
- `get_market_context({'keyword': 'Baltimore Orioles Washington Nationals'})` → No related markets found for 'Baltimore Orioles Washington Nationals'
- `get_sports_data({'sport': 'mlb', 'team': 'Washington Nationals'})` → INJURY [washington nationals] DJ Herz (SP): 60-Day-IL
INJURY [washington nationals] Cole Henry (RP):

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*