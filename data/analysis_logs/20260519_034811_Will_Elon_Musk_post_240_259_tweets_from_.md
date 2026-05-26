# Market Analysis — 2026-05-19 03:48 UTC

## Market
- **Question:** Will Elon Musk post 240-259 tweets from May 15 to May 22, 2026?
- **Category:** social
- **YES Price:** 26.2%
- **Days Left:** 3
- **Volume 24h:** $58,150
- **Liquidity:** $42,456

## Statistical Prior
- **p_base:** 22.7%
- **Source:** logistic:social
- **N (historical):** 7829
- **Raw gap:** 3.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 25/100 (Extreme Fear) | trend: deteriorating
- BTC: $76,744 (-0.1% 24h) → neutral
- Fear&Greed: 25/100 (Extreme Fear) | 7d trend: deteriorating
- BTC: $76,773 (-0.2% 24h) → neutral

### General
- [FEAR&GREED 7d trend] 25(Extr) → 28(Fear) → 27(Fear) → 31(Fear) | sentiment worsening

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: elon musk post 240-259 tweets
- [Bing News]
- [] elon musk post 240-259 tweets
- [Metaculus]
- [] Will the next IPC Sudan acute food insecurity analysis classify at lea
- → Community: pending
- [] Will the Senate of the Philippines remove Vice President Sara Duterte
- → Community: pending

## LLM Decision
- **Action:** SKIP
- **Confidence:** 65%
- **p_true:** 22.7%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.00

### Reasoning
Market efficiently priced at 26% vs extremely robust 23% base rate (n=7,829). Negative gap of -3% suggests market may be slightly overpricing YES, but insufficient edge for a NO bet. No catalysts identified - no news suggesting Musk will tweet significantly more/less than usual. Past decisions correctly SKIPped similar setups. Days left=3 but no new information to create edge.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `search_web({'query': 'Elon Musk tweet count frequency 2025 2026 posting habits'})` → [Tue, 20 Jan 2026] Google News
[Tue, 14 Jan 2025] X (Formerly Twitter) Age, Gender, &amp; Demo Stats
- `search_web({'query': 'Elon Musk X Twitter activity recent posting volume'})` → [Sun, 17 May 2026] Google News
[Mon, 11 May 2026] Musk Tweet Bets Top $3M - StartupHub.ai
[Mon, 11 M
- `get_market_context({'keyword': 'Elon Musk tweets'})` → No related markets found for 'Elon Musk tweets'
- `search_web({'query': 'Elon Musk tweeting frequency per day 2026 how many tweets daily'})` → [Sun, 17 May 2026] Google News
[Tue, 20 Jan 2026] Musk Tweet Bets Top $3M - StartupHub.ai
[Wed, 19 N
- `search_web({'query': 'Elon Musk news May 2026 events announcements'})` → [Mon, 18 May 2026] Google News
[Wed, 06 May 2026] Jury dismisses all claims in Elon Musk's lawsuit a
- `get_market_context({'keyword': 'social media posting frequency prediction'})` → No related markets found for 'social media posting frequency prediction'

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*