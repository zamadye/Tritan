# Market Analysis — 2026-05-20 14:30 UTC

## Market
- **Question:** Will Hull City AFC vs. Southampton FC end in a draw?
- **Category:** sports
- **YES Price:** 93.9%
- **Days Left:** 2
- **Volume 24h:** $137,291
- **Liquidity:** $16,735

## Statistical Prior
- **p_base:** 98.4%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 4.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $77,341 (+1.3% 24h) → risk-ON
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $77,354 (+1.2% 24h) → risk-ON
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 27(Fear) → 25(Extr) → 28(Fear) → 27(Fear) | sentiment worsening
- MicroStrategy sells any Bitcoin by May 31, 2026? → YES=50%

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: hull city southampton draw
- [Bing News]
- [Wed, 20 May 2026] hull city southampton draw
- → Express Sport keeps you across all of the latest news surrounding 'spygate'.
- [Wed, 20 May 2026] Spygate LIVE: Southampton decision imminent with play-off final in jeopardy
- → Oli McBurnie has insisted “nothing changes” for Hull City after Middlesbrough were reinstated to the Championship play-offs at the expense of Southa
- [Tue, 19 May 2026] Hull City star Oli McBurnie sends defiant message after Southampton decision and Middlesbrough FC reprieve
- → Southampton have been ejected from the Championship play-off final by the English Football League over a spying scandal. Tonda Eckert’s side beat Mi

## LLM Decision
- **Action:** NO
- **Confidence:** 65%
- **p_true:** 82.4%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** TEAM EXPULSION FROM PLAYOFF DUE TO SCANDAL
- **Catalyst Strength:** 0.90

### Reasoning
Southampton has been expelled from the Championship playoffs due to 'spygate' scandal, making the scheduled Hull City vs. Southampton match unlikely to occur as planned. The market is pricing a 94% chance of a draw, likely based on historical base rates (98%), but this major off-field development significantly reduces the probability of the match proceeding normally, let alone ending in a draw. The crowd hasn't fully adjusted for this catalyst.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=4%<5%

## Tool Calls
- `get_sports_data({'sport': 'soccer', 'team': 'Hull City'})` → No injury data found for soccer Hull City
- `get_odds({'sport': 'soccer_epl', 'team': 'Hull'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `get_market_context({'keyword': 'Hull City Southampton draw'})` → No related markets found for 'Hull City Southampton draw'
- `search_web({'query': 'Hull City vs Southampton match preview draw probability'})` → [Fri, 15 May 2026] Google News
[Fri, 24 Apr 2026] Hull vs Southampton: Prediction, kick-off time, te
- `search_web({'query': 'Hull City Southampton 2026 Championship standings form'})` → [Wed, 20 May 2026] Google News
[Tue, 05 May 2026] Hull - Middlesbrough - Flashscore.com
[Wed, 06 May
- `search_web({'query': 'Hull City Southampton Championship playoff May 2026'})` → [Wed, 20 May 2026] Google News
[Wed, 20 May 2026] Southampton players exploring possible legal actio
- `search_web({'query': 'Southampton expelled Championship playoff Hull City match impact'})` → [Tue, 19 May 2026] Google News
[Wed, 20 May 2026] Southampton may face legal challenge from own play

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*