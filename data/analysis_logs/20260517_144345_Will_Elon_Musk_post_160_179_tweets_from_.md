# Market Analysis — 2026-05-17 14:43 UTC

## Market
- **Question:** Will Elon Musk post 160-179 tweets from May 15 to May 22, 2026?
- **Category:** social
- **YES Price:** 15.0%
- **Days Left:** 5
- **Volume 24h:** $53,859
- **Liquidity:** $33,408

## Statistical Prior
- **p_base:** 15.3%
- **Source:** logistic:social
- **N (historical):** 7829
- **Raw gap:** 0.3%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $78,029 (-0.0% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $77,958 (-0.3% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 27(Fear) → 31(Fear) → 43(Fear) → 34(Fear) | sentiment worsening
- MicroStrategy sells any Bitcoin by May 31, 2026? → YES=50%

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: elon musk post 160-179 tweets
- [Bing News]
- [] elon musk post 160-179 tweets
- [Metaculus]
- [] Will Bitcoin trade above $120,000 before August 1, 2026?
- → Community: pending
- [] Will Haiti hold the first round of its presidential election before Se
- → Community: pending

## LLM Decision
- **Action:** SKIP
- **Confidence:** 45%
- **p_true:** 15.3%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.10

### Reasoning
Market is efficiently priced at base rate (15% YES vs 15% base, gap=+0%). Past decisions confirm Musk is currently testifying in court (May 13), which REDUCES tweeting capacity - if anything, this pushes probability DOWN, not up. Similar market for 180-199 tweets was already decided NO (conf=65%) due to court testimony. No verifiable edge or catalyst exists to justify a YES bet. Pattern data shows no-gap trades have lower win rate (63% vs 67% for info-gap trades). SKIP due to no statistical advantage.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=0%<5%

## Tool Calls
- `search_web({'query': 'Elon Musk tweeting frequency 2026 May court testimony'})` → [Wed, 18 Jan 2023] Google News
[] In Elon Musk Tesla trial, lawyers tussle over a tweet that cost in
- `search_web({'query': 'Elon Musk Twitter X posts per day 2026'})` → [Wed, 13 May 2026] Google News
[Mon, 23 Mar 2026] Elon Musk’s anonymous online BFF spreads his ideas
- `get_market_context({'keyword': 'Elon Musk tweets'})` → No related markets found for 'Elon Musk tweets'
- `search_web({'query': 'Elon Musk X posting activity May 2026'})` → [Sun, 17 May 2026] Google News
[Wed, 13 May 2026] Musk Tweet Bets Top $3M - StartupHub.ai
[Thu, 14 M
- `search_web({'query': '"Elon Musk" tweets average per day 2026'})` → [Sat, 14 Mar 2026] Google News
[Fri, 13 Mar 2026] It’s Elon Musk’s world - but we don’t have to live
- `search_web({'query': 'Elon Musk court testimony May 13 2026 reducing tweeting'})` → [Wed, 13 May 2026] Google News
[Tue, 03 Mar 2026] OpenAI CEO Sam Altman pushes back against Elon Mus
- `search_web({'query': 'Elon Musk typical tweet count per week'})` → [Mon, 11 May 2026] Google News
[Fri, 13 Mar 2026] Elon Musk's Tweet Volume Forecasted - StartupHub.a
- `search_web({'query': 'Musk Tweet Bets Top $3M May 2026 Polymarket'})` → [Sun, 17 May 2026] Google News
[Mon, 11 May 2026] Musk Tweet Bets Top $3M - StartupHub.ai
[Fri, 15 M
- `search_web({'query': 'Elon Musk tweet volume forecast May 2026 StartupHub'})` → [Sun, 17 May 2026] Google News
[Mon, 11 May 2026] Musk Tweet Bets Top $3M - StartupHub.ai
[Fri, 15 M
- `search_web({'query': '"Elon Musk" "tweets per day" average statistics'})` → [Tue, 28 Apr 2026] Google News
[Fri, 06 Feb 2026] Twitter (X) Facts and Statistics - Investing.com
[
- `search_web({'query': 'Elon Musk tweeting behavior court case reduced posting'})` → [Wed, 04 Mar 2026] Google News
[Wed, 04 Mar 2026] Elon Musk takes stand in Twitter shareholder trial
- `search_web({'query': 'Elon Musk tweeting frequency 20-30 tweets per day average'})` → [Tue, 25 Nov 2025] Google News
[Wed, 08 May 2024] X/Twitter mDAU in the United States 2022 - Statist
- `search_web({'query': 'Elon Musk 160 tweets 170 tweets typical week X posting'})` → [Tue, 02 Dec 2025] Google News
[] Trump Posted More Than 160 Times on Truth Social in Late-Night Bli
- `search_web({'query': 'Elon Musk tweets per day statistics analysis 2025 2026'})` → [Tue, 28 Apr 2026] Google News
[Fri, 01 May 2026] Twitter (X) Facts and Statistics - Investing.com
[
- `get_market_context({'keyword': 'Musk posting tweets May 2026'})` → No related markets found for 'Musk posting tweets May 2026'

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*