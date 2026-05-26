# Market Analysis — 2026-05-18 14:17 UTC

## Market
- **Question:** Indian Premier League: Chennai Super Kings vs Sunrisers Hyderabad
- **Category:** sports
- **YES Price:** 56.0%
- **Days Left:** 7
- **Volume 24h:** $179,574
- **Liquidity:** $107,489

## Statistical Prior
- **p_base:** 59.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.9%

## News Sources Fetched
### Macro Context
- Fear&Greed: 28/100 (Fear) | trend: deteriorating
- BTC: $76,677 (-1.8% 24h) → risk-OFF
- Fear&Greed: 28/100 (Fear) | 7d trend: deteriorating
- BTC: $76,990 (-1.6% 24h) → risk-OFF
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 28(Fear) → 27(Fear) → 31(Fear) → 43(Fear) | sentiment worsening
- Will the Fed increase interest rates by 25 bps after the Jun → YES=50%
- [SPORTS] Injuries:
- ?: Keshon Gilbert — Out (Surgery)
- ?: Jock Landale — Out (Sprain)
- ?: Jayson Tatum — Out (Soreness)
- ?: Nolan Traore — Out (Not Specified)
- ?: Nic Claxton — Out (Sprain)

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: indian premier league: chennai super
- [Bing News]
- [Mon, 18 May 2026] indian premier league: chennai super
- → Chennai Super Kings skipper Ruturaj Gaikwad confirmed that former skipper MS Dhoni will not be playing for the five-time champions as they take on S
- [Mon, 18 May 2026] MS Dhoni misses Chennai Super Kings' final home game of the IPL 2026, hosts opt to bat first in Chepauk
- → Chennai Super Kings have 12 points from 12 games, while SunRisers Hyderabad have 14 points from 12 matches and must win to strengthen their playoff 
- [Sun, 17 May 2026] CSK Vs SRH Live Cricket Score, IPL 2026: Chennai Super Kings Win Toss, Opt To Bat At Chepauk
- → Check today's hourly weather update for the MA Chidamabaram Stadium in Chennai for the Chennai Super Kings vs SunRisers Hyderabad match in the India

## LLM Decision
- **Action:** SKIP
- **Confidence:** 62%
- **p_true:** 54.9%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_EDGE
- **Catalyst Strength:** 0.60

### Reasoning
Strong statistical signal indicates market overprices YES: markets at 56% historically resolve YES only 44.7% of time (n=13,967). Market price (56%) slightly below base rate (59%), confirming potential mispricing. CSK injury concerns (Dhoni, Overton replaced by Forrester) add uncertainty. Entry 50-60% range has poor WR=25% historically. Confidence moderated due to: (1) missing SRH injury data, (2) no bookmaker odds available for cricket, (3) gap direction ambiguous but stat signal is clear. Edge is purely statistical from historical market resolution patterns.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `search_web({'query': 'Chennai Super Kings vs Sunrisers Hyderabad IPL 2024 match preview'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] CSK vs SRH Match Prediction: Who will win today’s 
- `search_web({'query': 'Chennai Super Kings recent form IPL 2026 injuries squad'})` → [Thu, 14 May 2026] Google News
[Thu, 07 May 2026] IPL 2026: CSK Signs Dian Forrester as Injury Repla
- `get_market_context({'keyword': 'IPL'})` → No related markets found for 'IPL'
- `get_market_context({'keyword': 'Chennai Super Kings'})` → No related markets found for 'Chennai Super Kings'
- `search_web({'query': 'CSK vs SRH head to head record 2024 2025 2026'})` → [Mon, 18 May 2026] Google News
[Sun, 10 May 2026] CSK vs SRH Head-to-Head In IPL (2026 Stats &amp; R
- `search_web({'query': '"CSK vs SRH" "who will win" IPL 2026'})` → [Mon, 18 May 2026] Google News
[Sun, 17 May 2026] CSK vs SRH Match Prediction: Who will win today’s 
- `search_web({'query': 'CSK injury news IPL 2026 players out'})` → [Wed, 13 May 2026] Google News
[Mon, 18 May 2026] CSK injured players list IPL 2026: Latest injury u

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*