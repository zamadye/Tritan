# Market Analysis — 2026-05-20 07:20 UTC

## Market
- **Question:** Bengaluru 3: Alex Hernandez vs Naoya Honda
- **Category:** sports
- **YES Price:** 53.0%
- **Days Left:** 6
- **Volume 24h:** $47,222
- **Liquidity:** $23,187

## Statistical Prior
- **p_base:** 54.5%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 1.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $77,275 (+0.2% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $77,258 (+0.2% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 27(Fear) → 25(Extr) → 28(Fear) → 27(Fear) | sentiment worsening
- MicroStrategy sells any Bitcoin by May 31, 2026? → YES=50%

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: bengaluru alex hernandez naoya honda
- [Bing News]
- [] bengaluru alex hernandez naoya honda
- [Metaculus]
- [] Will a case of Bundibugyo Ebola disease be first confirmed in the US b
- → Community: pending
- [] Will the next IPC Sudan acute food insecurity analysis classify at lea
- → Community: pending

## LLM Decision
- **Action:** SKIP
- **Confidence:** 40%
- **p_true:** 54.5%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.10

### Reasoning
Unable to verify existence of this specific fight or fighters. No search results, no related markets, and no sportsbook odds available. While statistical signal suggests market overprices YES at 53% (historical YES rate only 44.7%), this is a pattern-based signal without concrete evidence about this specific matchup. Cannot confirm fighters, event, or any specific details to make informed bet.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=1%<5%

## Tool Calls
- `get_odds({'sport': 'mma_mixed_martial_arts'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `search_web({'query': 'Alex Hernandez vs Naoya Honda MMA fight 2025'})` → No search results for: Alex Hernandez vs Naoya Honda MMA fight 2025
- `search_web({'query': 'Honda vs Hernandez MMA odds predictions'})` → [Sat, 21 Feb 2026] Google News
[Fri, 20 Feb 2026] UFC Houston Parlay Picks: How to Get +471 Odds on 
- `search_web({'query': '"Bengaluru 3" MMA event fight card'})` → [Fri, 27 Mar 2026] Google News
[] M Chinnaswamy Stadium Schedule IPL 2026: RCB home match list, date
- `get_market_context({'keyword': 'Hernandez Honda MMA'})` → No related markets found for 'Hernandez Honda MMA'
- `search_web({'query': 'Naoya Honda fighter MMA record'})` → [Fri, 21 Mar 2025] Google News
[Mon, 06 May 2024] Roman Gonzalez Says Naoya Inoue Clash Possible - B
- `search_web({'query': 'Alex Hernandez MMA fighter record 2025'})` → [Sat, 13 Sep 2025] Google News
[Wed, 21 Jan 2026] Alexander Hernandez Feels Like He Has Nothing To L
- `get_sports_data({'sport': 'mma', 'team': 'Hernandez'})` → No injury data found for mma Hernandez
- `search_web({'query': '"Bengaluru 3" fight card 2025 MMA India'})` → [Wed, 17 Dec 2025] Google News
[Fri, 09 Jan 2026] World Tennis League 2025: Kyrgios, Medvedev, Monfi
- `get_market_context({'keyword': 'Bengaluru MMA'})` → No related markets found for 'Bengaluru MMA'
- `search_web({'query': 'Alex Hernandez vs Naoya Honda fighter'})` → No search results for: Alex Hernandez vs Naoya Honda fighter
- `get_market_context({'keyword': 'Alex Hernandez'})` → No related markets found for 'Alex Hernandez'
- `search_web({'query': 'Naoya Honda MMA fighter Japan'})` → [Sun, 26 Apr 2026] Google News
[Sun, 14 Sep 2025] Tokyo Dome Sells Out for Inoue vs. Nakatani: Japan
- `get_market_context({'keyword': 'Naoya Honda'})` → No related markets found for 'Naoya Honda'

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*