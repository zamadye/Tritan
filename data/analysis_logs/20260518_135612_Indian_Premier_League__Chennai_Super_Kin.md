# Market Analysis — 2026-05-18 13:56 UTC

## Market
- **Question:** Indian Premier League: Chennai Super Kings vs Sunrisers Hyderabad
- **Category:** sports
- **YES Price:** 45.0%
- **Days Left:** 7
- **Volume 24h:** $63,902
- **Liquidity:** $155,676

## Statistical Prior
- **p_base:** 42.5%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 28/100 (Fear) | trend: deteriorating
- BTC: $76,916 (-1.7% 24h) → risk-OFF
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
- → Chennai Super Kings have 12 points from 12 games, while SunRisers Hyderabad have 14 points from 12 matches and must win to strengthen their playoff 
- [Mon, 18 May 2026] CSK Vs SRH Live Cricket Score, IPL 2026: Chennai Super Kings Win Toss, Opt To Bat At Chepauk
- → Chennai Super Kings have won the toss and skipper Ruturaj Gaikwad has opted to bat first in the must-win clash. There is one change in their playing
- [Sun, 17 May 2026] CSK vs SRH LIVE Score, IPL 2026: Chennai go in without MS Dhoni, opt to bat first in pressure game
- → Check today's hourly weather update for the MA Chidamabaram Stadium in Chennai for the Chennai Super Kings vs SunRisers Hyderabad match in the India

## LLM Decision
- **Action:** SKIP
- **Confidence:** 60%
- **p_true:** 42.5%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.00

### Reasoning
Gap of -2% is below the 5% threshold required for a bet. No strong evidence or direct catalyst found to suggest a profitable edge. Sports category shows strong historical performance but poor performance in the 40-50% entry range.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=2%<5%

## Tool Calls
- `search_web({'query': 'Chennai Super Kings vs Sunrisers Hyderabad IPL 2025 match preview'})` → [Mon, 18 May 2026] Google News
[Sun, 17 May 2026] CSK vs SRH IPL 2026 63rd Match Prediction &amp; Od
- `get_sports_data({'sport': 'cricket', 'team': 'Chennai Super Kings'})` → No injury data found for cricket Chennai Super Kings
- `get_sports_data({'sport': 'ipl', 'team': 'Chennai Super Kings'})` → No injury data found for ipl Chennai Super Kings
- `search_web({'query': 'CSK vs SRH IPL 2026 injuries squad updates'})` → [Sun, 17 May 2026] Google News
[Sat, 09 May 2026] MS Dhoni Farewell: Will Thala Return In CSK vs SRH
- `get_market_context({'keyword': 'IPL Chennai Sunrisers'})` → No related markets found for 'IPL Chennai Sunrisers'
- `search_web({'query': 'Chennai Super Kings vs Sunrisers Hyderabad 2026 form standings points table'})` → [Sun, 17 May 2026] Google News
[Mon, 18 May 2026] IPL 2026 playoffs: Qualified teams, standings and 
- `search_web({'query': 'CSK SRH head to head record IPL 2026'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] CSK vs SRH preview: MS Dhoni may finally have his 
- `get_market_context({'keyword': 'IPL cricket'})` → No related markets found for 'IPL cricket'
- `search_web({'query': '"CSK vs SRH" IPL 2026 match prediction winner odds betting'})` → [Sun, 17 May 2026] Google News
[Mon, 18 May 2026] IPL 2026: CSK vs. SRH prediction, lineups, pitch r
- `search_web({'query': 'CSK vs SRH IPL 2026 match preview pitch report Chepauk'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] CSK vs SRH IPL 2026 preview: Live streaming, pitch
- `get_market_context({'keyword': 'IPL cricket Polymarket'})` → No related markets found for 'IPL cricket Polymarket'

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*