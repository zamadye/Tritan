# Market Analysis — 2026-05-21 21:47 UTC

## Market
- **Question:** Will Arsenal win the 2025–26 Champions League?
- **Category:** other
- **YES Price:** 43.0%
- **Days Left:** 9
- **Volume 24h:** $161,617
- **Liquidity:** $784,374

## Statistical Prior
- **p_base:** 33.2%
- **Source:** logistic:other
- **N (historical):** 7829
- **Raw gap:** 9.8%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,700 (+0.2% 24h) → neutral
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $77,698 (+0.2% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 29(Fear) → 27(Fear) → 25(Extr) → 28(Fear) | sentiment improving
- Will the Fed increase interest rates by 50+ bps after the Ju → YES=50%

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: arsenal 2025–26 champions league
- [Bing News]
- [Tue, 19 May 2026] arsenal 2025–26 champions league
- → We have been crowned 2025/26 Premier League champions with a game to spare, after an incredible campaign in N5 has ended with us claiming our 14th t
- [Tue, 19 May 2026] Arsenal crowned 2025/26 Premier League champions
- → Arsenal were crowned champions of the 2025–26 Premier League season and will also look to win the Champions League.
- [Tue, 19 May 2026] Arsenal win Premier League before Champions League final: How many English teams have achieved ‘the double’?
- → Arsenal and Manchester City are battling for more than Premier League glory in 2025-26. With massive TV revenue, bonus payouts and Champions League 

## LLM Decision
- **Action:** SKIP
- **Confidence:** 45%
- **p_true:** 33.2%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.10

### Reasoning
Arsenal confirmed in Champions League final vs PSG (~May 30). Market at 43% reflects reasonable estimate for single-match final between two elite teams. Base rate (33%) likely reflects historical CL performance, while market correctly prices in Arsenal's current form. No clear edge detected - market appears efficiently priced. Past decisions also skipped this market with low confidence.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** low conf 45%<52%

## Tool Calls
- `get_sports_data({'sport': 'soccer_epl', 'team': 'Arsenal'})` → No injury data found for soccer_epl Arsenal
- `get_odds({'sport': 'soccer_epl', 'team': 'Arsenal'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `get_market_context({'keyword': 'Arsenal Champions League final PSG'})` → No related markets found for 'Arsenal Champions League final PSG'
- `search_web({'query': 'Arsenal vs PSG Champions League final 2025 odds predictions'})` → [Thu, 07 May 2026] Google News
[Wed, 20 May 2026] Champions League final: PSG-Arsenal predictions, o
- `search_web({'query': 'Arsenal Champions League final 2025 team news injuries lineup'})` → [Tue, 07 Apr 2026] Google News
[Fri, 15 May 2026] Sporting CP vs Arsenal: TV channel, kick-off time,
- `search_web({'query': '"PSG vs Arsenal" "Champions League final" May 2026 odds winner'})` → [Thu, 21 May 2026] Google News
[Tue, 19 May 2026] How to get PSG Champions League Final 2026 tickets
- `search_web({'query': 'Champions League final 2026 PSG Arsenal betting odds favorite'})` → [Wed, 06 May 2026] Google News
[Fri, 08 May 2026] Champions League semi-final betting odds: Arsenal 
- `search_web({'query': 'Champions League final 2026 PSG Arsenal Squawka predictions odds May 8'})` → [Wed, 20 May 2026] Google News
[Wed, 20 May 2026] Champions League final predictions: Arsenal vs PSG
- `search_web({'query': 'Arsenal squad fitness PSG final key players form 2026'})` → [Mon, 18 May 2026] Google News
[Thu, 21 May 2026] Will Ousmane Dembele Be Fit for PSG in Champions L

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*