# Market Analysis — 2026-05-18 14:10 UTC

## Market
- **Question:** Indian Premier League: Chennai Super Kings vs Sunrisers Hyderabad
- **Category:** sports
- **YES Price:** 45.0%
- **Days Left:** 7
- **Volume 24h:** $134,445
- **Liquidity:** $110,510

## Statistical Prior
- **p_base:** 42.5%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 28/100 (Fear) | trend: deteriorating
- BTC: $76,915 (-1.6% 24h) → risk-OFF
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
- **p_true:** 42.5%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** INJURY
- **Catalyst Strength:** 0.30

### Reasoning
Gap of -2% is below the 5% threshold required for a bet. Market (45%) is actually ABOVE base rate (43%), meaning CSK is slightly overpriced relative to historical performance - no edge for YES bet. Both teams have significant injuries: CSK lost MS Dhoni at season start, SRH lost key all-rounder and Pat Cummins injured. Injuries create uncertainty but no clear directional catalyst for either side. Same matchup was previously skipped for identical gap reason. No concrete verifiable evidence suggests which team has an advantage.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=2%<5%

## Tool Calls
- `search_web({'query': 'Chennai Super Kings injury report team form IPL 2025'})` → [Mon, 30 Mar 2026] Google News
[Sun, 10 May 2026] RR vs CSK, Match 3 Preview: Head-to-Head Record, P
- `search_web({'query': 'Chennai Super Kings vs Sunrisers Hyderabad IPL 2026 preview match preview'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] CSK vs SRH IPL 2026 preview: Live streaming, pitch
- `search_web({'query': 'Chennai Super Kings injury update March 2026 IPL players unavailable'})` → [Sun, 29 Mar 2026] Google News
[Wed, 25 Mar 2026] CSK in trouble! After MS Dhoni injury, star player
- `search_web({'query': 'Sunrisers Hyderabad injury update March 2026 SRH team news'})` → [Fri, 20 Mar 2026] Google News
[Tue, 24 Mar 2026] SRH’s IPL 2026 plans shaken as key all-rounder rul
- `get_market_context({'keyword': 'Indian Premier League Chennai Sunrisers'})` → No related markets found for 'Indian Premier League Chennai Sunrisers'
- `search_web({'query': 'CSK vs SRH head to head record IPL all time wins'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] CSK vs SRH preview: MS Dhoni may finally have his 
- `search_web({'query': 'IPL 2026 Chennai Super Kings recent results wins losses'})` → [Wed, 06 May 2026] Google News
[Sat, 16 May 2026] CSK IPL 2026 playoff qualification scenarios: Revi
- `search_web({'query': 'CSK vs SRH 2026 schedule date April March'})` → [Sat, 16 May 2026] Google News
[Wed, 06 May 2026] Indian Premier League 2026 | Dates, Format, Player
- `search_web({'query': '"CSK vs SRH" April 2026 IPL schedule'})` → [Sat, 16 May 2026] Google News
[Tue, 17 Mar 2026] Indian Premier League 2026 | Dates, Format, Player

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*