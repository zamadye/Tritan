# Market Analysis — 2026-05-19 10:23 UTC

## Market
- **Question:** Indian Premier League: Rajasthan Royals vs Lucknow Super Giants
- **Category:** sports
- **YES Price:** 57.0%
- **Days Left:** 7
- **Volume 24h:** $86,759
- **Liquidity:** $502,043

## Statistical Prior
- **p_base:** 60.4%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 25/100 (Extreme Fear) | trend: deteriorating
- BTC: $76,709 (-0.0% 24h) → neutral
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
- **Confidence:** 62%
- **p_true:** 60.4%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL
- **Catalyst Strength:** 0.70

### Reasoning
Strong statistical signal (n=13,967) indicates market overprices YES at 57% (historical resolution 44.7%), but the 3% gap is below the 5% threshold required for actionable edge. Additional uncertainty exists as the match may have already been played with LSG winning. Without new direct catalyst or larger edge, skipping is optimal.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `search_web({'query': 'Rajasthan Royals vs Lucknow Super Giants IPL 2025 recent news injuries'})` → [Fri, 18 Apr 2025] Google News
[Sat, 19 Apr 2025] IPL 2025, RR vs LSG 36th Match Match Preview - RR 
- `search_web({'query': 'Rajasthan Royals Sanju Samson injury status April 2025'})` → [Sat, 19 Apr 2025] Google News
[Thu, 24 Apr 2025] Sanju Samson Unlikely To Captain RR Against LSG Am
- `search_web({'query': 'Lucknow Super Giants recent form IPL 2025 injuries'})` → [Tue, 24 Mar 2026] Google News
[Wed, 25 Mar 2026] LSG team in IPL 2026: Lucknow Super Giants on a ti
- `search_web({'query': 'RR vs LSG IPL 2025 match preview prediction April 2025'})` → [Tue, 12 May 2026] Google News
[Sat, 19 Apr 2025] RR VS LSG IPL 2025 HIGHLIGHTS | LIVE MATCH | RAJAS
- `search_web({'query': 'RR vs LSG IPL 2025 match preview India Today April 19 2025'})` → [Fri, 18 Apr 2025] Google News
[Sun, 20 Apr 2025] IPL 2025, RR vs LSG 36th Match Match Preview - RR 
- `search_web({'query': 'ESPNcricinfo RR vs LSG 36th Match preview April 19 2025'})` → [Sat, 19 Apr 2025] Google News
[Fri, 18 Apr 2025] Ice-man Avesh holds his nerve as LSG edge past RR 
- `get_market_context({'keyword': 'Rajasthan Royals Lucknow Super Giants IPL'})` → No related markets found for 'Rajasthan Royals Lucknow Super Giants IPL'

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*