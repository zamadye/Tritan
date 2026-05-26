# Market Analysis — 2026-05-17 10:55 UTC

## Market
- **Question:** Indian Premier League: Punjab Kings vs Royal Challengers Bengaluru
- **Category:** sports
- **YES Price:** 51.0%
- **Days Left:** 7
- **Volume 24h:** $262,805
- **Liquidity:** $53,218

## Statistical Prior
- **p_base:** 51.5%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 0.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $78,427 (+0.7% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $78,427 (+0.7% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 27(Fear) → 31(Fear) → 43(Fear) → 34(Fear) | sentiment worsening
- MicroStrategy sells any Bitcoin by May 31, 2026? → YES=50%
- [SPORTS] Injuries:
- ?: Keshon Gilbert — Out (Surgery)
- ?: Jock Landale — Out (Sprain)
- ?: Jayson Tatum — Out (Soreness)
- ?: Nolan Traore — Out (Not Specified)
- ?: Nic Claxton — Out (Sprain)

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: indian premier league: punjab kings
- [Bing News]
- [Sun, 17 May 2026] indian premier league: punjab kings
- → Punjab Kings (PBKS) will look to end their five-match losing streak as they take on defending champions Royal Challengers Bengaluru (RCB) in Match 6
- [Sun, 17 May 2026] PBKS Vs RCB, IPL 2026: See Best Photos From Indian Premier League Match 61 At Dharamsala's HPCA Stadium
- → Venue: Himachal Pradesh Cricket Association Stadium Dharamshala Match coverage has started! Live updates will appear here. This live blog is AI gene
- [Sat, 16 May 2026] Punjab Kings vs Royal Challengers Bengaluru - 61st match - Indian Premier League, 2026
- → PBKS face RCB in a crucial IPL 2026 clash at the HPCA stadium as playoff pressure mounts. Here’s match preview, predicted XIs, and prediction ...

## LLM Decision
- **Action:** SKIP
- **Confidence:** 55%
- **p_true:** 51.5%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** STAT_EDGE
- **Catalyst Strength:** 0.65

### Reasoning
Strong statistical signal (markets at 51% resolve YES only 44.7% historically, n=13,967) suggests YES is overpriced by ~6%. However, cannot confirm fresh information (<2h) on RCB captain Rajat Patidar's absence is unpriced - news appears in search results but timing unclear. Price gap (+1%) is below 3% entry threshold. No clear home/recency/narrative bias identified. Past decisions for this same market correctly SKIPped due to insufficient gap. Stat edge alone insufficient per criteria without confirmed information gap or crowd bias.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=1%<3%

## Tool Calls
- `search_web({'query': 'Punjab Kings vs Royal Challengers Bengaluru IPL 2025 news today'})` → [Sat, 16 May 2026] Google News
[Sun, 17 May 2026] PBKS vs RCB Head To Head Records In IPL (2026 Upda
- `search_web({'query': 'Punjab Kings vs Royal Challengers Bengaluru IPL 2025 match preview team news injuries'})` → [Sun, 29 Mar 2026] Google News
[Sat, 16 May 2026] Match Preview - Rajasthan Royals vs Chennai Super 
- `search_web({'query': 'today IPL match Punjab Kings vs Royal Challengers Bengaluru playing XI injury update 2026'})` → [Sun, 17 May 2026] Google News
[Sun, 17 May 2026] PBKS vs RCB Injury News: Are Phil Salt And Lockie 

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*