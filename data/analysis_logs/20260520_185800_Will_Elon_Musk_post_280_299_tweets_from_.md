# Market Analysis — 2026-05-20 18:58 UTC

## Market
- **Question:** Will Elon Musk post 280-299 tweets from May 15 to May 22, 2026?
- **Category:** social
- **YES Price:** 7.7%
- **Days Left:** 1
- **Volume 24h:** $137,875
- **Liquidity:** $31,727

## Statistical Prior
- **p_base:** 9.6%
- **Source:** logistic:social
- **N (historical):** 7829
- **Raw gap:** 1.9%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $77,352 (+0.7% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $77,412 (+0.8% 24h) → neutral

### General
- [FEAR&GREED 7d trend] 27(Fear) → 25(Extr) → 28(Fear) → 27(Fear) | sentiment worsening

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: elon musk post 280-299 tweets
- [Bing News]
- [] elon musk post 280-299 tweets
- [Metaculus]
- [] Will a case of Bundibugyo Ebola disease be first confirmed in the US b
- → Community: pending
- [] Will the next IPC Sudan acute food insecurity analysis classify at lea
- → Community: pending

## LLM Decision
- **Action:** SKIP
- **Confidence:** 45%
- **p_true:** 9.6%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** AMBIGUOUS_EVENT
- **Catalyst Strength:** 0.30

### Reasoning
No verifiable edge with 1 day left. SpaceX Flight 12 launch is ambiguous directionally - could increase or decrease tweet volume. Narrow 280-299 range requires precise outcome prediction. Past decisions correctly skipped identical market. Gap of 2% is below 5% threshold for statistical edge.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=2%<5%

## Tool Calls
- `search_web({'query': 'Elon Musk tweet frequency May 2026'})` → [Sun, 17 May 2026] Google News
[Thu, 14 May 2026] Musk Tweet Bets Top $3M - StartupHub.ai
[Tue, 05 M
- `search_web({'query': '"Elon Musk" "tweet" "May 2026" frequency'})` → [Tue, 31 Mar 2026] Google News
[Fri, 17 Apr 2026] SpaceX Plans One Launch Per Hour Within 5 Years - 
- `search_web({'query': 'Elon Musk X Twitter activity May 2026'})` → [Wed, 20 May 2026] Google News
[Wed, 20 May 2026] Prediction Markets Track Elon Musk's Tweet Volume 
- `get_market_context({'keyword': 'Elon Musk tweets'})` → No related markets found for 'Elon Musk tweets'
- `search_web({'query': 'Elon Musk tweet count per week average 2026'})` → [Mon, 18 May 2026] Google News
[Mon, 11 May 2026] Kalshi Volume Levels Off at $3.86B as Transactions
- `search_web({'query': 'SpaceX Starship Flight 12 launch date May 2026'})` → [Wed, 20 May 2026] Google News
[Tue, 19 May 2026] Starship isn't launching today. When SpaceX target
- `search_web({'query': 'Polymarket Elon Musk tweet volume prediction market 2026'})` → [Wed, 20 May 2026] Google News
[Sun, 17 May 2026] Prediction Markets Track Elon Musk's Tweet Volume 

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*