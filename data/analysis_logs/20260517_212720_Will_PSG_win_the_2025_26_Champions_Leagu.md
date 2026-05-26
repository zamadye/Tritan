# Market Analysis — 2026-05-17 21:27 UTC

## Market
- **Question:** Will PSG win the 2025–26 Champions League?
- **Category:** other
- **YES Price:** 59.0%
- **Days Left:** 13
- **Volume 24h:** $96,491
- **Liquidity:** $1,082,178

## Statistical Prior
- **p_base:** 43.9%
- **Source:** logistic:other
- **N (historical):** 7829
- **Raw gap:** 15.1%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $78,230 (-0.0% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $78,378 (+0.2% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 27(Fear) → 31(Fear) → 43(Fear) → 34(Fear) | sentiment worsening
- Philadelphia Phillies vs. Pittsburgh Pirates: O/U 7.5 → YES=50%

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: 2025–26 champions league
- [Bing News]
- [Sat, 16 May 2026] 2025–26 champions league
- → Al-Nassr Vs Gamba Osaka AFC Champions League Two 2025-26 Final: Get preview, live streaming details and other information about the AFC Champions Le
- [Fri, 20 Mar 2026] Al-Nassr Vs Gamba Osaka Live Streaming, AFC Champions League Two 2025-26 Final: Preview, When And Where To Watch
- → The 2025-26 UEFA Champions League has its final eight teams, but the road here completely reshaped the tournament narrative. Heavy scorelines, shock
- [Mon, 15 Sep 2025] Opta Supercomputer Reveals Favorites To Win The 2025-26 Champions League
- → The Champions League is back, and Big Data is also in play. According to Opta’s calculations, these are the probabilities for each team to lift the 

## LLM Decision
- **Action:** NO
- **Confidence:** 52%
- **p_true:** 43.9%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** TOURNAMENT_PROGRESSION
- **Catalyst Strength:** 0.45

### Reasoning
Statistical mispricing + catalyst: p_base=44% vs market=59% gap=15% (n=7829)

## Gate Result
- **Passed:** ✅ YES
- **Reason:** BET NO $1.00

## Tool Calls
- `search_web({'query': 'PSG Champions League 2025-26 odds predictions'})` → [Thu, 14 May 2026] Google News
[Wed, 06 May 2026] Champions League winner odds: Predictions updated 
- `search_web({'query': 'PSG Arsenal Champions League final 2026 odds'})` → [Sun, 17 May 2026] Google News
[Fri, 08 May 2026] PSG vs Arsenal predictions: Champions League final
- `get_odds({'sport': 'soccer_epl', 'team': 'PSG'})` → [ODDS] soccer_epl — 0 events
- `search_web({'query': 'Champions League final 2026 odds PSG Arsenal bookmakers'})` → [Fri, 08 May 2026] Google News
[Tue, 12 May 2026] Champions League Winner Odds: Arsenal and PSG Rema
- `get_market_context({'keyword': 'Champions League'})` → No related markets found for 'Champions League'
- `search_web({'query': 'PSG Champions League 2026 final opponent bracket path'})` → [Tue, 10 Mar 2026] Google News
[Fri, 08 May 2026] Every Club’s Route to Champions League Final Ranke
- `search_web({'query': 'PSG Bayern Munich Champions League semi-final 2026 result'})` → [Thu, 07 May 2026] Google News
[Wed, 06 May 2026] UEFA Champions League Semi Final Results Leave Bay

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*