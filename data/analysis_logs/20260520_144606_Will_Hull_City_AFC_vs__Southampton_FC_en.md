# Market Analysis — 2026-05-20 14:46 UTC

## Market
- **Question:** Will Hull City AFC vs. Southampton FC end in a draw?
- **Category:** sports
- **YES Price:** 93.2%
- **Days Left:** 2
- **Volume 24h:** $141,222
- **Liquidity:** $14,798

## Statistical Prior
- **p_base:** 98.1%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 4.9%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $77,247 (+1.2% 24h) → risk-ON
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $77,354 (+1.2% 24h) → risk-ON
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 27(Fear) → 25(Extr) → 28(Fear) → 27(Fear) | sentiment worsening
- MicroStrategy sells any Bitcoin by May 31, 2026? → YES=50%

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: hull city southampton draw
- [Bing News]
- [Tue, 19 May 2026] hull city southampton draw
- → Southampton have been ejected from the Championship play-off final by the English Football League over a spying scandal. Tonda Eckert’s side beat Mi
- [Wed, 20 May 2026] Southampton kicked out of Championship play-off final over spying scandal
- → Hull City will take on Middlesbrough in the play-off final at Wembley Stadium after Southampton were expelled from the competition.
- [Wed, 20 May 2026] Hull City discover play-off final times as EFL confirm plan for Southampton winning appeal
- → Express Sport keeps you across all of the latest news surrounding 'spygate'.

## LLM Decision
- **Action:** NO
- **Confidence:** 65%
- **p_true:** 80.1%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** REGULATORY_ACTION
- **Catalyst Strength:** 0.95

### Reasoning
Southampton has been EXPULLED from the Championship playoffs due to the 'Spygate' scandal (confirmed by ESPN, Sky Sports, The Athletic, Yahoo Sports - all dated May 19-20, 2026). Middlesbrough has been reinstated to face Hull City in the playoff final instead. The original 'Hull City vs Southampton' match WILL NOT HAPPEN. Therefore it cannot end in a draw. The market at 93% YES is severely mispriced - the crowd appears unaware of this expulsion. This is a direct, concrete catalyst that fundamentally eliminates the possibility of a draw in this specific matchup. Strong edge betting NO.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=5%<5%

## Tool Calls
- `get_sports_data({'sport': 'soccer_epl', 'team': 'Southampton'})` → No injury data found for soccer_epl Southampton
- `get_odds({'sport': 'soccer_epl', 'team': 'Southampton'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `get_sports_data({'sport': 'soccer_epl', 'team': 'Hull City'})` → No injury data found for soccer_epl Hull City
- `search_web({'query': 'Hull City vs Southampton match preview 2025'})` → [Tue, 10 Feb 2026] Google News
[Sat, 20 Sep 2025] Where to watch Hull City vs Chelsea live in the US
- `search_web({'query': 'Southampton spygate scandal expelled playoffs Championship 2025'})` → [Tue, 19 May 2026] Google News
[Wed, 20 May 2026] Southampton expelled from Championship playoffs ov
- `get_market_context({'keyword': 'Hull Southampton draw'})` → No related markets found for 'Hull Southampton draw'
- `search_web({'query': 'Hull City Southampton playoff 2026'})` → [Wed, 20 May 2026] Google News
[Tue, 19 May 2026] Southampton expelled from Championship play-offs o
- `search_web({'query': '"Hull City" "Southampton" draw 2026'})` → [Tue, 12 May 2026] Google News
[Thu, 14 May 2026] Hull vs. Southampton (May 23, 2026) Live Score - E
- `search_web({'query': 'Southampton expelled Championship playoff consequences Hull City match'})` → [Wed, 20 May 2026] Google News
[Wed, 20 May 2026] Southampton expelled from Championship play-offs o
- `search_web({'query': 'Hull City vs Southampton what happens now playoff expelled'})` → [Tue, 19 May 2026] Google News
[Wed, 20 May 2026] Spygate explainer: Why Southampton were booted fro
- `search_web({'query': 'Hull City vs Southampton playoff final May 23 2026'})` → [Tue, 19 May 2026] Google News
[Tue, 19 May 2026] Hull vs. Boro (May 23, 2026) Live Score - ESPN
[Th
- `search_web({'query': 'Middlesbrough reinstated Championship playoff Southampton expelled May 2026'})` → [Wed, 20 May 2026] Google News
[Wed, 20 May 2026] Southampton players exploring possible legal actio

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*