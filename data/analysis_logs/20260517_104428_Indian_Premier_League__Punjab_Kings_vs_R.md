# Market Analysis — 2026-05-17 10:44 UTC

## Market
- **Question:** Indian Premier League: Punjab Kings vs Royal Challengers Bengaluru
- **Category:** sports
- **YES Price:** 53.0%
- **Days Left:** 7
- **Volume 24h:** $180,574
- **Liquidity:** $131,915

## Statistical Prior
- **p_base:** 54.5%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 1.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $78,441 (+0.8% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $78,376 (+0.7% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 27(Fear) → 31(Fear) → 43(Fear) → 34(Fear) | sentiment worsening
- MicroStrategy sells any Bitcoin by May 31, 2026? → YES=50%
- Will the Fed decrease interest rates by 25 bps after the Jun → YES=50%
- [SPORTS] Injuries:
- ?: Keshon Gilbert — Out (Surgery)
- ?: Jock Landale — Out (Sprain)
- ?: Jayson Tatum — Out (Soreness)
- ?: Nolan Traore — Out (Not Specified)

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: indian premier league: punjab kings
- [Bing News]
- [Sat, 16 May 2026] indian premier league: punjab kings
- → PBKS face RCB in a crucial IPL 2026 clash at the HPCA stadium as playoff pressure mounts. Here’s match preview, predicted XIs, and prediction ...
- [Fri, 15 May 2026] PBKS Vs RCB Match Prediction, IPL 2026: Who Will Win Today's Indian Premier League Match At Dharamsala?
- → Get the latest match prediction for Punjab Kings vs Royal Challengers Bengaluru in IPL 2026 Match 61 on May 17, including probable playing XIs, pitc
- [Sun, 17 May 2026] Match Predictions: Indian Premier League 2026 - Match 61 - Punjab Kings vs Royal Challengers Bengaluru - May 17th
- → Punjab Kings have won the toss and elected to field first against Royal Challengers Bengaluru at the HPCA Stadium, Dharamsala on Sunday, May 17 ...

## LLM Decision
- **Action:** SKIP
- **Confidence:** 0%
- **p_true:** 54.5%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.00

### Reasoning


## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=1%<3%

## Tool Calls
- `search_web({'query': 'Indian Premier League Punjab Kings vs Royal Challengers Bengaluru today news team updates injury'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] PBKS vs RCB Injury News: Are Phil Salt And Lockie 
- `get_market_context({'query': 'Punjab Kings Royal Challengers Bengaluru'})` → get_market_context error: HTTPSConnectionPool(host='gamma-api.polymarket.com', port=443): Read timed
- `get_sports_data({'sport': 'nba', 'team': 'Punjab Kings'})` → get_sports_data error: HTTPSConnectionPool(host='site.api.espn.com', port=443): Max retries exceeded
- `search_web({'query': 'Punjab Kings vs Royal Challengers Bengaluru betting odds today IPL 2026'})` → [Sun, 17 May 2026] Google News
[Sat, 16 May 2026] PBKS vs RCB live win probability, prediction, odds

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*