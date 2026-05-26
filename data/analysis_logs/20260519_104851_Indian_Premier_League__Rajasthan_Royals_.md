# Market Analysis — 2026-05-19 10:48 UTC

## Market
- **Question:** Indian Premier League: Rajasthan Royals vs Lucknow Super Giants
- **Category:** sports
- **YES Price:** 57.0%
- **Days Left:** 7
- **Volume 24h:** $88,144
- **Liquidity:** $509,618

## Statistical Prior
- **p_base:** 60.4%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 25/100 (Extreme Fear) | trend: deteriorating
- BTC: $76,710 (-0.2% 24h) → neutral
- Fear&Greed: 25/100 (Extreme Fear) | 7d trend: deteriorating
- BTC: $76,707 (-0.2% 24h) → neutral

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
- → Will the Rajasthan Royals get a step closer to their playoff aspirations, or will the Lucknow Super Giants spoil their party? Check out which team i

## LLM Decision
- **Action:** SKIP
- **Confidence:** 62%
- **p_true:** 60.4%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.00

### Reasoning
Stat signal (n=13,967) suggests market overprices YES at 57% (historical resolution 44.7%), but: (1) no concrete catalyst or information gap found, (2) entry in 50-60% range has terrible 33% WR historically, (3) gap of 3% is below 5% gate threshold, (4) no cricket-specific data available to confirm edge, (5) previous decisions for this exact market also correctly SKIPped. Despite strong statistical signal, lack of catalyst and poor historical performance in this price range makes action unjustified.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'sport': 'cricket', 'team': 'Rajasthan Royals'})` → No injury data found for cricket Rajasthan Royals
- `search_web({'query': 'Rajasthan Royals vs Lucknow Super Giants IPL 2025 recent form'})` → [Tue, 21 Apr 2026] Google News
[Thu, 18 Dec 2025] IPL 2026, LSG vs RR 32nd Match Match Preview - RR 
- `search_web({'query': 'IPL 2025 Rajasthan Royals injury news team update'})` → [Sun, 29 Mar 2026] Google News
[Wed, 18 Mar 2026] IPL 2026, RR vs CSK 3rd Match Match Preview - Reva
- `get_market_context({'keyword': 'Rajasthan Royals Lucknow Super Giants'})` → No related markets found for 'Rajasthan Royals Lucknow Super Giants'
- `search_web({'query': 'IPL 2024 Rajasthan Royals vs Lucknow Super Giants match preview today'})` → [Tue, 19 May 2026] Google News
[Fri, 08 May 2026] IPL 2026 RR vs LSG: Pitch report, highest score, J
- `search_web({'query': 'IPL current season 2024 Rajasthan Royals results'})` → [Fri, 07 Feb 2025] Google News
[Sat, 06 Apr 2024] Highest score in IPL: Teams with the biggest total
- `get_odds({'sport': 'cricket_ipl', 'team': 'Rajasthan Royals'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `get_crypto_price({'coin': 'bitcoin'})` → bitcoin: $76,707.00 | 24h: -0.18%

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*