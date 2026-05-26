# Market Analysis — 2026-05-20 15:03 UTC

## Market
- **Question:** Will Hull City AFC vs. Southampton FC end in a draw?
- **Category:** sports
- **YES Price:** 93.1%
- **Days Left:** 2
- **Volume 24h:** $149,221
- **Liquidity:** $11,996

## Statistical Prior
- **p_base:** 98.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 4.9%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $77,468 (+1.5% 24h) → risk-ON
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $77,397 (+1.3% 24h) → risk-ON

### General
- [FEAR&GREED 7d trend] 27(Fear) → 25(Extr) → 28(Fear) → 27(Fear) | sentiment worsening

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: hull city southampton draw
- [Bing News]
- [Wed, 20 May 2026] hull city southampton draw
- → Express Sport keeps you across all of the latest news surrounding 'spygate'.
- [Wed, 20 May 2026] Spygate LIVE: Southampton decision imminent with play-off final in jeopardy
- → Hull City will take on Middlesbrough in the play-off final at Wembley Stadium after Southampton were expelled from the competition.
- [Wed, 20 May 2026] Hull City discover play-off final times as EFL confirm plan for Southampton winning appeal
- → Oli McBurnie has insisted “nothing changes” for Hull City after Middlesbrough were reinstated to the Championship play-offs at the expense of Southa

## LLM Decision
- **Action:** SKIP
- **Confidence:** 65%
- **p_true:** 92.0%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** REGULATORY/PUNISHMENT + TEAM CHAOS
- **Catalyst Strength:** 0.75

### Reasoning
Southampton officially expelled from playoffs due to Spygate scandal (confirmed by ESPN, Sky Sports, The Athletic, BBC). Players exploring legal action against club, boss facing FA ban. This creates maximum chaos and zero motivation. Hull focused on playoff final vs Middlesbrough (reinstated). Base rate 98% (n=6077) vs YES price 93% = 5% edge. Dead rubber + demotivated team + Hull resting players = draw probability near-certain.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=5%<5%

## Tool Calls
- `get_sports_data({'sport': 'soccer_epl', 'team': 'Hull City'})` → No injury data found for soccer_epl Hull City
- `get_sports_data({'sport': 'soccer_epl', 'team': 'Southampton'})` → No injury data found for soccer_epl Southampton
- `search_web({'query': 'Hull City vs Southampton 2025 prediction'})` → [Thu, 02 Apr 2026] Google News
[Mon, 22 Sep 2025] PREVIEW | Oxford United vs Hull City - team news, 
- `search_web({'query': 'Southampton expelled Championship Spygate 2025'})` → [Tue, 19 May 2026] Google News
[Wed, 20 May 2026] Southampton expelled from Championship playoffs ov
- `get_odds({'sport': 'soccer_epl', 'team': 'Hull City'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `get_market_context({'keyword': 'Hull City Southampton draw'})` → No related markets found for 'Hull City Southampton draw'
- `search_web({'query': 'Southampton spygate expelled playoffs May 2026 details'})` → [Wed, 20 May 2026] Google News
[Wed, 20 May 2026] Southampton expelled from Championship play-offs o
- `search_web({'query': 'Hull City Southampton Championship 2025-26 season standings'})` → [Wed, 20 May 2026] Google News
[Sat, 02 May 2026] EFL playoffs 2025-26: Schedule, results, how to wa
- `search_web({'query': '"Hull City" "Southampton" May 2026 match final day'})` → [Wed, 20 May 2026] Google News
[Tue, 19 May 2026] Southampton expelled from Championship play-offs o
- `search_web({'query': 'Southampton players legal action spygate expulsion May 2026'})` → [Wed, 20 May 2026] Google News
[Wed, 20 May 2026] Southampton players exploring possible legal actio

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*