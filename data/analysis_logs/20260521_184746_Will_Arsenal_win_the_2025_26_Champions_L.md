# Market Analysis — 2026-05-21 18:47 UTC

## Market
- **Question:** Will Arsenal win the 2025–26 Champions League?
- **Category:** other
- **YES Price:** 42.0%
- **Days Left:** 9
- **Volume 24h:** $163,509
- **Liquidity:** $817,682

## Statistical Prior
- **p_base:** 32.6%
- **Source:** logistic:other
- **N (historical):** 7829
- **Raw gap:** 9.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,674 (+0.3% 24h) → neutral
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $77,670 (+0.4% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 29(Fear) → 27(Fear) → 25(Extr) → 28(Fear) | sentiment improving
- Will the Fed increase interest rates by 50+ bps after the Ju → YES=50%
- Pittsburgh Pirates vs. St. Louis Cardinals → YES=50%

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: arsenal 2025–26 champions league
- [Bing News]
- [Tue, 19 May 2026] arsenal 2025–26 champions league
- → We have been crowned 2025/26 Premier League champions with a game to spare, after an incredible campaign in N5 has ended with us claiming our 14th t
- [Tue, 19 May 2026] Arsenal crowned 2025/26 Premier League champions
- → Arsenal and Manchester City are battling for more than Premier League glory in 2025-26. With massive TV revenue, bonus payouts and Champions League 
- [Tue, 19 May 2026] 2025-26 Premier League prize money: How much will Arsenal make for winning the title?
- → Arsenal were crowned champions of the 2025–26 Premier League season and will also look to win the Champions League.

## LLM Decision
- **Action:** SKIP
- **Confidence:** 45%
- **p_true:** 32.6%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.20

### Reasoning
Arsenal has reached the Champions League final vs PSG (May 21, 2026). Market price of 42% aligns with bookmaker consensus showing PSG as slight favorites (~58%). Arsenal won Premier League 2025-26 indicating strong form, but PSG has significant CL pedigree and experience. With 9 days until final and no concrete evidence of injury, lineup changes, or tactical advantages, the 42% price appears fair. Base rate of 33% reflects historical CL win rates for teams in similar positions. No verifiable edge to justify a bet at current price - would need ~50%+ estimated probability for YES bet given the pricing.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** low conf 45%<52%

## Tool Calls
- `get_sports_data({'sport': 'soccer', 'team': 'Arsenal'})` → No injury data found for soccer Arsenal
- `get_odds({'sport': 'soccer_epl', 'team': 'Arsenal'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Arsenal Champions League 2025-26 odds prediction'})` → [Wed, 20 May 2026] Google News
[Wed, 20 May 2026] Champions League winner odds: Predictions updated 
- `search_web({'query': 'Arsenal Champions League final 2026 betting market'})` → [Wed, 20 May 2026] Google News
[Fri, 15 May 2026] Champions League winner odds: Predictions updated 
- `search_web({'query': 'Arsenal Champions League final 2026 opponent preview'})` → [Thu, 07 May 2026] Google News
[Thu, 07 May 2026] Champions League final: PSG-Arsenal predictions, o
- `search_web({'query': 'Arsenal Champions League final 2026 May prediction'})` → [Wed, 20 May 2026] Google News
[Tue, 19 May 2026] Champions League final predictions: Arsenal vs PSG
- `get_market_context({'keyword': 'Champions League final Arsenal PSG'})` → No related markets found for 'Champions League final Arsenal PSG'
- `get_market_context({'keyword': 'Champions League winner'})` → No related markets found for 'Champions League winner'
- `search_web({'query': 'PSG vs Arsenal Champions League final odds May 2026 who will win'})` → [Thu, 21 May 2026] Google News
[Tue, 19 May 2026] How to get PSG Champions League Final 2026 tickets
- `search_web({'query': 'Arsenal Champions League final 2026 favorite underdog betting odds'})` → [Mon, 18 May 2026] Google News
[Thu, 14 May 2026] Arsenal vs. Burnley prediction: Odds, preview, bes

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*