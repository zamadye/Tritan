# Market Analysis — 2026-05-21 22:45 UTC

## Market
- **Question:** Will Arsenal win the 2025–26 Champions League?
- **Category:** other
- **YES Price:** 42.0%
- **Days Left:** 9
- **Volume 24h:** $157,845
- **Liquidity:** $844,716

## Statistical Prior
- **p_base:** 32.6%
- **Source:** logistic:other
- **N (historical):** 7829
- **Raw gap:** 9.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,633 (+0.3% 24h) → neutral
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $77,561 (+0.3% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 29(Fear) → 27(Fear) → 25(Extr) → 28(Fear) | sentiment improving
- Will the Fed increase interest rates by 50+ bps after the Ju → YES=50%

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: arsenal 2025–26 champions league
- [Bing News]
- [Tue, 19 May 2026] arsenal 2025–26 champions league
- → We have been crowned 2025/26 Premier League champions with a game to spare, after an incredible campaign in N5 has ended with us claiming our 14th t
- [Wed, 29 Apr 2026] Arsenal crowned 2025/26 Premier League champions
- → Atletico Madrid Vs Arsenal Highlights, UEFA Champions League 2025-26 Semi-Final: Viktor Gyokeres, Julian Alvarez score to keep things level. Check r
- [Tue, 19 May 2026] Atletico Madrid 1-1 Arsenal Highlights, UEFA Champions League 2025-26 SF: Gyokeres, Alvarez's Spotkicks Lead To Draw
- → Arsenal were crowned champions of the 2025–26 Premier League season and will also look to win the Champions League.

## LLM Decision
- **Action:** NO
- **Confidence:** 52%
- **p_true:** 32.6%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** SINGLE_MATCH_FINAL
- **Catalyst Strength:** 0.50

### Reasoning
Statistical mispricing + catalyst: p_base=33% vs market=42% gap=9% (n=7829)

## Gate Result
- **Passed:** ✅ YES
- **Reason:** BET NO $1.00

## Tool Calls
- `get_market_context({'keyword': 'Arsenal Champions League'})` → No related markets found for 'Arsenal Champions League'
- `search_web({'query': 'Arsenal Champions League final 2025 opponent date'})` → [Fri, 27 Feb 2026] Google News
[Thu, 28 Aug 2025] Champions League: Premier League clubs to learn la
- `search_web({'query': 'Arsenal Champions League 2025 injury news squad'})` → [Thu, 21 May 2026] Google News
[Thu, 21 May 2026] Arsenal Injury News Leaves Major Fear Before PSG C
- `search_web({'query': 'PSG vs Arsenal Champions League final 2026 date odds'})` → [Tue, 19 May 2026] Google News
[Thu, 21 May 2026] PSG vs Arsenal predictions: Champions League final
- `search_web({'query': 'Arsenal injury update Champions League final PSG May 2026'})` → [Thu, 21 May 2026] Google News
[Thu, 21 May 2026] Arsenal Injury News Leaves Major Fear Before PSG C
- `search_web({'query': 'Arsenal PSG Champions League final betting odds bookmakers'})` → [Wed, 20 May 2026] Google News
[Tue, 12 May 2026] Champions League winner odds: Predictions updated 
- `get_odds({'sport': 'soccer_epl', 'team': 'Arsenal'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'PSG vs Arsenal Champions League final 2026 winner odds 50-50'})` → [Tue, 19 May 2026] Google News
[Fri, 27 Feb 2026] So close! Arsenal star boy Bukayo Saka narrowly mi
- `search_web({'query': 'Arsenal vs PSG Champions League final winner odds Ladbrokes May 2026'})` → [Tue, 12 May 2026] Google News
[Thu, 07 May 2026] 2025/26 Champions League favourites and odds: PSG 

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*