# Market Analysis — 2026-05-19 08:33 UTC

## Market
- **Question:** Indian Premier League: Rajasthan Royals vs Lucknow Super Giants
- **Category:** sports
- **YES Price:** 56.0%
- **Days Left:** 7
- **Volume 24h:** $63,010
- **Liquidity:** $823,523

## Statistical Prior
- **p_base:** 59.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.9%

## News Sources Fetched
### Macro Context
- Fear&Greed: 25/100 (Extreme Fear) | trend: deteriorating
- BTC: $76,956 (-0.0% 24h) → neutral
- Fear&Greed: 25/100 (Extreme Fear) | 7d trend: deteriorating
- BTC: $77,147 (+0.1% 24h) → neutral

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
- → Rajasthan Royals face Lucknow Super Giants in a crucial IPL 2026 clash at the Sawai Mansingh Stadium as playoff pressure mounts. Here’s match previe
- [Mon, 18 May 2026] RR Vs LSG Match Prediction, IPL 2026: Who Will Win Today's Indian Premier League Match In Jaipur?
- → Read the full preview for IPL 2026 Match 64 between Rajasthan Royals and Lucknow Super Giants on May 19, featuring player form, team analysis, head-
- [Tue, 19 May 2026] Match Predictions: Indian Premier League 2026 - Match 64 - Rajasthan Royals vs Lucknow Super Giants - May 19th
- → Rajasthan Royals face Lucknow Super Giants in IPL 2026 Match 64 on Tuesday. Check RR’s playoff qualification scenarios ahead of the big match tonigh

## LLM Decision
- **Action:** SKIP
- **Confidence:** 45%
- **p_true:** 59.0%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL
- **Catalyst Strength:** 0.40

### Reasoning
Strong statistical signal shows markets at 56% resolve YES only 44.7% of time (n=13,967), indicating market overprices YES. Contextual evidence supports this: RR described as struggling needing 'urgent revival' while LSG is 'resurgent'. However, gap (+3%) is below 5% threshold required by decision rules. Entry range 50-60% has poor historical WR (33% from 6 trades). Missing concrete catalyst - no injury news, pitch report, or head-to-head data that would directly affect outcome. Jadeja return is positive for RR but insufficient to overcome statistical edge. Consistent with previous similar decisions to SKIP.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'cricket', 'team': 'Rajasthan Royals'})` → No injury data found for cricket Rajasthan Royals
- `search_web({'query': 'Rajasthan Royals vs Lucknow Super Giants IPL 2025 recent results form'})` → [Tue, 21 Apr 2026] Google News
[Tue, 03 Jun 2025] IPL 2026, LSG vs RR 32nd Match Match Preview - RR 
- `search_web({'query': '"Rajasthan Royals vs Lucknow Super Giants" 2026 match preview team news'})` → [Tue, 19 May 2026] Google News
[Mon, 18 May 2026] RR vs LSG IPL 2026 Playing 11 Today Match: Ravindr
- `get_market_context({'keyword': 'IPL Rajasthan Royals Lucknow Super Giants'})` → No related markets found for 'IPL Rajasthan Royals Lucknow Super Giants'
- `search_web({'query': 'Rajasthan Royals 2026 IPL results standings form'})` → [Tue, 28 Apr 2026] Google News
[Fri, 01 May 2026] PBKS vs RR IPL 2026: Players, standings, stats and
- `search_web({'query': 'Lucknow Super Giants 2026 IPL results standings form'})` → [Sun, 17 May 2026] Google News
[Sun, 12 Apr 2026] IPL 2026 playoffs: Qualified teams, standings and 
- `search_web({'query': '"RR vs LSG" "64th Match" IPL 2026 preview team news playing XI'})` → [Tue, 19 May 2026] Google News
[Tue, 19 May 2026] RR vs LSG IPL 2026 Playing 11 Today Match: Ravindr

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*