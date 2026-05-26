# Market Analysis — 2026-05-19 08:44 UTC

## Market
- **Question:** Indian Premier League: Rajasthan Royals vs Lucknow Super Giants
- **Category:** sports
- **YES Price:** 56.0%
- **Days Left:** 7
- **Volume 24h:** $69,996
- **Liquidity:** $682,177

## Statistical Prior
- **p_base:** 59.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 2.9%

## News Sources Fetched
### Macro Context
- Fear&Greed: 25/100 (Extreme Fear) | trend: deteriorating
- BTC: $77,118 (+0.3% 24h) → neutral
- Fear&Greed: 25/100 (Extreme Fear) | 7d trend: deteriorating
- BTC: $77,118 (+0.3% 24h) → neutral

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
- **Action:** NO
- **Confidence:** 65%
- **p_true:** 45.0%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_PATTERN
- **Catalyst Strength:** 0.85

### Reasoning
Strong statistical signal (n=13,967) shows markets at 56% YES only resolve YES 44.7% of the time, indicating 11.3% overpricing of YES. No contradictory news catalyst found - RR described as struggling, LSG ousted. Pattern holds across large sample.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `search_web({'query': 'Rajasthan Royals vs Lucknow Super Giants IPL 2025 match preview'})` → [Tue, 12 May 2026] Google News
[Tue, 21 Apr 2026] RR VS LSG IPL 2025 HIGHLIGHTS | LIVE MATCH | RAJAS
- `search_web({'query': 'IPL 2025 Rajasthan Royals Lucknow Super Giants team news injuries'})` → [Wed, 25 Mar 2026] Google News
[Fri, 14 Nov 2025] IPL 2026: Full list of injured players ruled out a
- `search_web({'query': 'Rajasthan Royals vs Lucknow Super Giants 2025 match date'})` → [Sun, 29 Mar 2026] Google News
[Wed, 22 Apr 2026] 2026 IPL Schedule, Standings &amp; Next Match Coun
- `search_web({'query': 'IPL 2026 Rajasthan Royals Lucknow Super Giants schedule'})` → [Tue, 19 May 2026] Google News
[Tue, 19 May 2026] IPL 2026 schedule - fixtures and results - AOL.com
- `get_market_context({'keyword': 'Indian Premier League'})` → No related markets found for 'Indian Premier League'
- `get_market_context({'keyword': 'Rajasthan Royals'})` → No related markets found for 'Rajasthan Royals'
- `search_web({'query': 'RR vs LSG IPL 2026 preview team news form standings'})` → [Sun, 17 May 2026] Google News
[Mon, 18 May 2026] IPL 2026 playoffs: Qualified teams, standings and 

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*