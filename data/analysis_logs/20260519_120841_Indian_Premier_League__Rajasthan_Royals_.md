# Market Analysis — 2026-05-19 12:08 UTC

## Market
- **Question:** Indian Premier League: Rajasthan Royals vs Lucknow Super Giants
- **Category:** sports
- **YES Price:** 58.0%
- **Days Left:** 7
- **Volume 24h:** $92,914
- **Liquidity:** $292,411

## Statistical Prior
- **p_base:** 61.9%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.9%

## News Sources Fetched
### Macro Context
- Fear&Greed: 25/100 (Extreme Fear) | trend: deteriorating
- BTC: $76,679 (-0.8% 24h) → neutral
- Fear&Greed: 25/100 (Extreme Fear) | 7d trend: deteriorating
- BTC: $76,669 (-0.9% 24h) → neutral

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
- → RR Vs LSG Live Cricket Score, IPL 2026: Hello and welcome to our live coverage of the 64th match of Indian Premier League 2026, between Rajasthan Ro
- [Tue, 19 May 2026] RR Vs LSG Live Cricket Score, IPL 2026: Playoffs-Seeking Royals Desperate For First Win In Jaipur
- → RR vs LSG IPL 2026 preview featuring Rajasthan Royals’ playoff battle against eliminated Lucknow Super Giants in a crucial clash at Jaipur, know eve

## LLM Decision
- **Action:** NO
- **Confidence:** 65%
- **p_true:** 49.9%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_EDGE
- **Catalyst Strength:** 0.80

### Reasoning
Strong statistical signal (n=13,967) shows markets at 58% YES resolve YES only 44.7% of the time, indicating YES is overpriced by ~13 percentage points. While the gap between market price (58%) and base rate (62%) is only +4% (below the 5% gate threshold), the historical resolution rate provides a clear edge for NO bets. Recent news shows RR lost last match and LSG suffered star player departure, but the statistical pattern suggests systematic overpricing of YES in this price range regardless of specific match circumstances.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=4%<5%

## Tool Calls
- `get_market_context({'keyword': 'Rajasthan Royals Lucknow Super Giants IPL'})` → No related markets found for 'Rajasthan Royals Lucknow Super Giants IPL'
- `search_web({'query': 'Rajasthan Royals vs Lucknow Super Giants IPL 2025 preview'})` → [Sun, 10 May 2026] Google News
[Tue, 21 Apr 2026] Rajasthan Royals Vs Lucknow Super Giants Today Dre
- `search_web({'query': 'IPL 2026 Rajasthan Royals Lucknow Super Giants preview'})` → [Tue, 19 May 2026] Google News
[Tue, 19 May 2026] RR vs LSG, IPL 2026 preview: Rajasthan Royals seek
- `search_web({'query': 'Rajasthan Royals injury news IPL 2026'})` → [Tue, 19 May 2026] Google News
[Mon, 18 May 2026] RR vs LSG Injury News: Is Ravindra Jadeja Playing 
- `search_web({'query': 'RR vs LSG predicted XI IPL 2026'})` → [Tue, 19 May 2026] Google News
[Tue, 19 May 2026] IPL Match Today, RR vs LSG: Predicted playing XI, 
- `search_web({'query': 'Rajasthan Royals recent results IPL 2026'})` → [Sun, 17 May 2026] Google News
[Tue, 19 May 2026] DC vs RR IPL 2026: Score, result and highlights as
- `search_web({'query': 'LSG star player leaves camp IPL 2026'})` → [Tue, 19 May 2026] Google News
[Fri, 15 May 2026] IPL 2026: Massive blow for LSG as star player leav

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*