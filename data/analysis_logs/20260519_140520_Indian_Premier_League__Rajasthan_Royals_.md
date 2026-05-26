# Market Analysis — 2026-05-19 14:05 UTC

## Market
- **Question:** Indian Premier League: Rajasthan Royals vs Lucknow Super Giants
- **Category:** sports
- **YES Price:** 58.0%
- **Days Left:** 7
- **Volume 24h:** $183,693
- **Liquidity:** $98,254

## Statistical Prior
- **p_base:** 61.9%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.9%

## News Sources Fetched
### Macro Context
- Fear&Greed: 25/100 (Extreme Fear) | trend: deteriorating
- BTC: $76,811 (+0.0% 24h) → neutral
- Fear&Greed: 25/100 (Extreme Fear) | 7d trend: deteriorating
- BTC: $76,687 (-0.1% 24h) → neutral

### General
- [FEAR&GREED 7d trend] 25(Extr) → 28(Fear) → 27(Fear) → 31(Fear) | sentiment worsening
- [SPORTS] Recent games:
- BOS @ KC | Final | Kansas City Royals(home) 20-28 score:1 vs Boston Red Sox(away) 20-27 score:3
- [SPORTS] Injuries:
- ?: James McCann — Out (Strain)
- ?: A.J. Puk — 60-Day-IL (Surgery)
- ?: Jordan Lawlar — 60-Day-IL (Fracture)
- ?: Jacob Wilson — 10-Day-IL (Dislocated)

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: indian premier league: rajasthan royals
- [Bing News]
- [Mon, 18 May 2026] indian premier league: rajasthan royals
- → Read the full preview for IPL 2026 Match 64 between Rajasthan Royals and Lucknow Super Giants on May 19, featuring player form, team analysis, head-
- [Tue, 19 May 2026] Match Predictions: Indian Premier League 2026 - Match 64 - Rajasthan Royals vs Lucknow Super Giants - May 19th
- → Rajasthan Royals has left out captain Riyan Parag from the playing XI against Lucknow Super Giants in IPL 2026. Parag had injured his hamstring on M
- [Tue, 19 May 2026] RR vs LSG: Why Yashasvi Jaiswal is leading Rajasthan Royals instead of Riyan Parag in IPL 2026? Stand-in-captain reveals
- → Rajasthan Royals have 12 points from 12 games, while Lucknow Super Giants have eight points from 12 matches and are out of playoff contention. Follo

## LLM Decision
- **Action:** SKIP
- **Confidence:** 58%
- **p_true:** 61.9%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_INEFFICIENCY
- **Catalyst Strength:** 0.55

### Reasoning
Strong statistical signal (n=13,967) shows markets at 58% resolve YES only 44.7% of the time, suggesting ~13% overpricing. However, gate check FAILS (gap=4% < 5% threshold). Past identical market decisions also failed gate. Sports 50-60% entry zone has weak 33% WR historically. Unable to verify specific match catalysts due to tool limitations for cricket. Stat edge exists but doesn't meet systematic gate requirement.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=4%<5%

## Tool Calls
- `get_sports_data({'sport': 'cricket', 'team': 'Rajasthan Royals'})` → No injury data found for cricket Rajasthan Royals
- `search_web({'query': 'Rajasthan Royals vs Lucknow Super Giants IPL 2025 match preview'})` → [Tue, 19 May 2026] Google News
[Mon, 18 May 2026] IPL 2026 RR vs LSG: Match preview, head-to-head an
- `get_market_context({'keyword': 'Indian Premier League IPL cricket'})` → No related markets found for 'Indian Premier League IPL cricket'
- `search_web({'query': 'Rajasthan Royals recent form results IPL 2025 2026'})` → [Sat, 25 Apr 2026] Google News
[Tue, 07 Apr 2026] IPL 2026 RR vs SRH: Pitch report, highest score, J
- `search_web({'query': 'Lucknow Super Giants recent form results IPL 2025 2026'})` → [Fri, 15 May 2026] Google News
[Sun, 26 Apr 2026] LSG vs CSK IPL 2026 Head-To-Head Record: Key Stats
- `get_market_context({'keyword': 'Rajasthan Royals Lucknow'})` → No related markets found for 'Rajasthan Royals Lucknow'
- `search_web({'query': 'Rajasthan Royals Lucknow Super Giants head to head record IPL'})` → [Tue, 19 May 2026] Google News
[Tue, 19 May 2026] RR vs LSG Head-To-Head Record: Who Holds Edge Ahea
- `search_web({'query': '"Rajasthan Royals" "Lucknow Super Giants" odds betting 2025'})` → [Mon, 18 May 2026] Google News
[Wed, 15 Apr 2026] IPL 2026 winner odds &amp; latest betting: Who wil
- `search_web({'query': 'Rajasthan Royals 2025 IPL standings wins losses'})` → [Mon, 23 Feb 2026] Google News
[Tue, 05 May 2026] IPL Points Table All Seasons: Complete Records (20
- `search_web({'query': 'Lucknow Super Giants 2025 IPL standings wins losses'})` → [Mon, 23 Feb 2026] Google News
[Tue, 05 May 2026] IPL Points Table All Seasons: Complete Records (20

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*