# Market Analysis — 2026-05-19 01:52 UTC

## Market
- **Question:** Athletics vs. Los Angeles Angels
- **Category:** sports
- **YES Price:** 56.0%
- **Days Left:** 6
- **Volume 24h:** $137,929
- **Liquidity:** $32,319

## Statistical Prior
- **p_base:** 59.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.9%

## News Sources Fetched
### Macro Context
- Fear&Greed: 25/100 (Extreme Fear) | trend: deteriorating
- BTC: $76,720 (-0.2% 24h) → neutral
- Fear&Greed: 25/100 (Extreme Fear) | 7d trend: deteriorating
- BTC: $76,802 (+0.0% 24h) → neutral

### General
- [FEAR&GREED 7d trend] 25(Extr) → 28(Fear) → 27(Fear) → 31(Fear) | sentiment worsening
- [SPORTS] Injuries:
- ?: A.J. Puk — 60-Day-IL (Surgery)
- ?: Jordan Lawlar — 60-Day-IL (Fracture)
- ?: Pavin Smith — 60-Day-IL (Surgery)
- ?: Jacob Wilson — 10-Day-IL (Dislocated)
- ?: Max Muncy — 10-Day-IL (Fracture)
- ?: Brooks Kriske — 15-Day-IL (Pinched Nerve)

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: athletics angeles angels
- [Bing News]
- [Mon, 18 May 2026] athletics angeles angels
- → The Angels seem destined to waste another year of future Hall of Famer Mike Trout ’s career as their record (16-31) is the worst in MLB. First-year 
- [Mon, 18 May 2026] Game #47: Athletics at Angels Game Thread
- → The Sacramento Athletics (23-22) are headed to Angel Stadium on Monday where they will go up against the Los Angeles Angels (16-30). The moneyline o
- [Mon, 18 May 2026] Sacramento Athletics vs Los Angeles Angels Prediction, 5/18/2026 MLB Picks, Best Bets &amp; Odds
- → Athletics (23-23, first in the AL West) vs. Los Angeles Angels (16-31, fifth in the AL West) Anaheim, California; Monday, 9:38 p.m. EDT PITCHING PRO

## LLM Decision
- **Action:** SKIP
- **Confidence:** 65%
- **p_true:** 50.9%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL/HISTORICAL_PATTERN
- **Catalyst Strength:** 0.70

### Reasoning
Strong statistical signal (n=13,967) shows markets at 56% resolve YES only 44.7% of the time, indicating systematic overpricing of YES. Despite Athletics' strong form, the historical pattern provides a significant edge (~11.3%) for NO bet.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'mlb', 'team': 'Athletics'})` → INJURY [athletics] Jacob Wilson (SS): 10-Day-IL
INJURY [athletics] Max Muncy (3B): 10-Day-IL
INJURY 
- `get_sports_data({'sport': 'mlb', 'team': 'Angels'})` → INJURY [los angeles angels] Travis d'Arnaud (C): 10-Day-IL
INJURY [los angeles angels] Ben Joyce (RP
- `search_web({'query': 'Oakland Athletics recent results form 2025'})` → [Wed, 13 May 2026] Google News
[Sun, 10 May 2026] World Series | History, Winners, &amp; Facts - Bri
- `search_web({'query': 'Los Angeles Angels recent performance injuries 2025'})` → [2026-05-10] Top 10 Moments From the 2026 MLB Season — The MLB season is in full swing, with players
- `get_market_context({'keyword': 'Athletics Angels'})` → No related markets found for 'Athletics Angels'
- `search_web({'query': 'Athletics vs Angels head to head 2025 MLB'})` → [2026-05-01] Two-start pitchers: Tarik Skubal headlines a gaggle of elite options as we steamroll in
- `search_web({'query': 'MLB standings 2025 AL West Athletics Angels'})` → [2026-05-11] We Have a Problem: Mariners at Astros Series Preview — The Mariners head to Houston for
- `get_odds({'sport': 'baseball_mlb', 'team': 'Athletics'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*