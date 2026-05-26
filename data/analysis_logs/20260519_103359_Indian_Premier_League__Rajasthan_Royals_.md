# Market Analysis — 2026-05-19 10:33 UTC

## Market
- **Question:** Indian Premier League: Rajasthan Royals vs Lucknow Super Giants
- **Category:** sports
- **YES Price:** 57.0%
- **Days Left:** 7
- **Volume 24h:** $87,044
- **Liquidity:** $634,460

## Statistical Prior
- **p_base:** 60.4%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 25/100 (Extreme Fear) | trend: deteriorating
- BTC: $76,808 (+0.0% 24h) → neutral
- Fear&Greed: 25/100 (Extreme Fear) | 7d trend: deteriorating
- BTC: $76,765 (-0.0% 24h) → neutral

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
- → It's a massive game for Rajasthan Royals as they absolutely need to beat Lucknow Super Giants to keep their playoff dreams alive. They've really stu

## LLM Decision
- **Action:** SKIP
- **Confidence:** 65%
- **p_true:** 50.4%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_PATTERN
- **Catalyst Strength:** 0.75

### Reasoning
Strong statistical signal (n=13,967) shows markets at 57% YES historically resolve YES only 44.7%, indicating 12.3% overpricing of YES. Despite gap=3% being below typical 5% gate, the direct price-to-resolution comparison reveals actionable edge. Sports betting pattern shows 80% WR overall but only 33% WR in 50-60% entry range (weak zone). Macro fear/greed at extreme fear (25) suggests risk-averse environment where contrarian sports bets may perform better. Market appears to overprice favorites in this price band.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'cricket', 'team': 'Rajasthan Royals'})` → No injury data found for cricket Rajasthan Royals
- `search_web({'query': 'Rajasthan Royals vs Lucknow Super Giants IPL 2025 match preview'})` → [Tue, 12 May 2026] Google News
[Tue, 21 Apr 2026] RR VS LSG IPL 2025 HIGHLIGHTS | LIVE MATCH | RAJAS
- `search_web({'query': 'IPL 2026 Rajasthan Royals vs Lucknow Super Giants odds prediction'})` → [Tue, 19 May 2026] Google News
[Tue, 19 May 2026] RR vs LSG IPL 2026 Playing 11 Today Match: Ravindr
- `get_market_context({'keyword': 'Rajasthan Royals'})` → No related markets found for 'Rajasthan Royals'
- `get_market_context({'keyword': 'IPL'})` → No related markets found for 'IPL'
- `search_web({'query': 'IPL 2026 Rajasthan Royals standings form recent results'})` → [Sun, 17 May 2026] Google News
[Mon, 18 May 2026] Vaibhav Sooryavanshi sets sights on breaking huge 
- `search_web({'query': 'IPL 2026 Lucknow Super Giants standings form recent results'})` → [Sun, 17 May 2026] Google News
[Fri, 15 May 2026] IPL 2026 playoffs: Qualified teams, standings and 
- `search_web({'query': 'RR vs LSG IPL 2026 64th Match Prediction Odds Betting Tips'})` → [Tue, 19 May 2026] Google News
[Tue, 19 May 2026] RR vs LSG IPL 2026 64th Match Prediction &amp; Odd

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*