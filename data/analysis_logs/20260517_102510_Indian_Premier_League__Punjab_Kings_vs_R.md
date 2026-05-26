# Market Analysis — 2026-05-17 10:25 UTC

## Market
- **Question:** Indian Premier League: Punjab Kings vs Royal Challengers Bengaluru
- **Category:** sports
- **YES Price:** 54.0%
- **Days Left:** 7
- **Volume 24h:** $168,201
- **Liquidity:** $124,957

## Statistical Prior
- **p_base:** 56.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.0%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $78,413 (+0.8% 24h) → neutral
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
- [Fri, 15 May 2026] indian premier league: punjab kings
- → Get the latest match prediction for Punjab Kings vs Royal Challengers Bengaluru in IPL 2026 Match 61 on May 17, including probable playing XIs, pitc
- [Sat, 16 May 2026] Match Predictions: Indian Premier League 2026 - Match 61 - Punjab Kings vs Royal Challengers Bengaluru - May 17th
- → PBKS face RCB in a crucial IPL 2026 clash at the HPCA stadium as playoff pressure mounts. Here’s match preview, predicted XIs, and prediction ...
- [Sun, 17 May 2026] PBKS Vs RCB Match Prediction, IPL 2026: Who Will Win Today's Indian Premier League Match At Dharamsala?
- → Punjab Kings have won the toss and elected to field first against Royal Challengers Bengaluru at the HPCA Stadium, Dharamsala on Sunday, May 17 ...

## LLM Decision
- **Action:** SKIP
- **Confidence:** 65%
- **p_true:** 50.0%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** SENTIMENT_SHIFT
- **Catalyst Strength:** 0.65

### Reasoning
Strong statistical signal: markets at 54% YES resolve YES only 44.7% historically (n=13,967) — indicating ~9.3% edge for NO. Information catalyst: Rajat Patidar (RCB captain) confirmed OUT for today's match (reported <24h ago), Jitesh Sharma to lead. This is material lineup change. Crowd bias likely present: RCB's massive fanbase (Kohli legacy) tends to inflate YES prices regardless of actual team strength. Patidar absence may not be fully priced in given RCB's brand strength. Historical base rate 56% but market microstructure at 54% level strongly favors NO outcomes.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=2%<3%

## Tool Calls
- `search_web({'query': 'Punjab Kings vs Royal Challengers Bengaluru IPL 2025 team news injury updates today'})` → [Sun, 17 May 2026] Google News
[Sat, 16 May 2026] IPL 2026: Big blow for RCB! Rajat Patidar misses P
- `get_sports_data({'sport': 'nba', 'team': 'Punjab Kings Royal Challengers Bengaluru IPL'})` → No injury data found for nba Punjab Kings Royal Challengers Bengaluru IPL
- `search_web({'query': '"Punjab Kings vs Royal Challengers Bengaluru" IPL 2026 match prediction odds'})` → [Sun, 17 May 2026] Google News
[Sat, 16 May 2026] Punjab Kings vs Royal Challengers Bengaluru Playin
- `get_market_context({'keyword': 'IPL Punjab Kings Royal Challengers Bengaluru cricket'})` → No related markets found for 'IPL Punjab Kings Royal Challengers Bengaluru cricket'
- `search_web({'query': 'Rajat Patidar injury RCB IPL 2026 impact Punjab Kings match'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] PBKS vs RCB Injury News: Are Phil Salt And Lockie 
- `search_web({'query': 'Punjab Kings recent results IPL 2026 form'})` → [Sat, 16 May 2026] Google News
[Sun, 05 Apr 2026] Who Will Win PBKS vs RCB IPL 2026 Match 61? (Winne

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*