# Market Analysis — 2026-05-19 11:10 UTC

## Market
- **Question:** Will Elon Musk post 180-199 tweets from May 15 to May 22, 2026?
- **Category:** social
- **YES Price:** 6.0%
- **Days Left:** 3
- **Volume 24h:** $80,599
- **Liquidity:** $31,526

## Statistical Prior
- **p_base:** 8.1%
- **Source:** logistic:social
- **N (historical):** 7829
- **Raw gap:** 2.1%

## News Sources Fetched
### Macro Context
- Fear&Greed: 25/100 (Extreme Fear) | trend: deteriorating
- BTC: $77,000 (+0.3% 24h) → neutral
- Fear&Greed: 25/100 (Extreme Fear) | 7d trend: deteriorating
- BTC: $76,787 (-0.0% 24h) → neutral

### General
- [FEAR&GREED 7d trend] 25(Extr) → 28(Fear) → 27(Fear) → 31(Fear) | sentiment worsening

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: elon musk post 180-199 tweets
- [Bing News]
- [] elon musk post 180-199 tweets
- [Metaculus]
- [] Will the next IPC Sudan acute food insecurity analysis classify at lea
- → Community: pending
- [] Will the Senate of the Philippines remove Vice President Sara Duterte
- → Community: pending

## LLM Decision
- **Action:** SKIP
- **Confidence:** 62%
- **p_true:** 8.1%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** SCHEDULED_EVENT
- **Catalyst Strength:** 0.55

### Reasoning
Starship Flight 12 launch on May 21 provides moderate catalyst but gap is only +2% vs 5% threshold. Market already partially accounts for event. Base rate 8% vs YES price 6% shows slight underpricing but insufficient edge for confident bet. Pattern suggests info gap trades have better edge when gap is larger.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=2%<5%

## Tool Calls
- `search_web({'query': 'Elon Musk tweet count prediction market May 2026'})` → [Mon, 18 May 2026] Google News
[Sun, 17 May 2026] Kalshi Volume Levels Off at $3.86B as Transactions
- `search_web({'query': 'Starship Flight 12 launch May 21 Elon Musk tweets'})` → [Tue, 19 May 2026] Google News
[Tue, 19 May 2026] SpaceX Reschedules Starship Launch On May 21: When
- `get_market_context({'keyword': 'Elon Musk'})` → No related markets found for 'Elon Musk'
- `search_web({'query': 'SpaceX Reschedules Starship Launch On May 21: When And Where To Watch'})` → [Tue, 19 May 2026] Google News
[Tue, 19 May 2026] 12th Starship launch date rescheduled again - Vall
- `search_web({'query': 'Musk Tweet Bets Top $3M prediction market'})` → [Sun, 17 May 2026] Google News
[Tue, 19 May 2026] Musk Tweet Bets Top $3M - StartupHub.ai
[Fri, 15 M
- `search_web({'query': 'Polymarket Elon Musk tweet count 2026'})` → [Mon, 18 May 2026] Google News
[Sun, 17 May 2026] Kalshi Volume Levels Off at $3.86B as Transactions
- `search_web({'query': 'Elon Musk tweet frequency per day 2026'})` → [Sun, 17 May 2026] Google News
[Thu, 14 May 2026] Musk Tweet Bets Top $3M - StartupHub.ai
[Fri, 20 M
- `search_web({'query': 'Starship launch Elon Musk tweet count'})` → [Tue, 27 Jan 2026] Google News
[Mon, 11 Aug 2025] Elon Musk Haters Have Found a Hilariously Easy Way
- `get_market_context({'keyword': 'tweet'})` → No related markets found for 'tweet'

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*