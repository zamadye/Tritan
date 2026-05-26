# Market Analysis — 2026-05-17 12:44 UTC

## Market
- **Question:** Shanghai Sharks vs. Beijing Ducks
- **Category:** sports
- **YES Price:** 59.0%
- **Days Left:** 6
- **Volume 24h:** $67,169
- **Liquidity:** $22,129

## Statistical Prior
- **p_base:** 63.3%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 4.3%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $78,425 (+0.5% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $78,425 (+0.5% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 27(Fear) → 31(Fear) → 43(Fear) → 34(Fear) | sentiment worsening
- MicroStrategy sells any Bitcoin by May 31, 2026? → YES=50%
- [SPORTS] Injuries:
- ?: Radko Gudas — Out ()
- ?: Drew Helleson — Out ()
- ?: Ryan Poehling — Out ()
- ?: Charlie McAvoy — Suspension ()
- ?: Viktor Arvidsson — Out ()

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: shanghai sharks beijing ducks
- [Bing News]
- [Wed, 06 May 2026] shanghai sharks beijing ducks
- → Top seed Shanghai defeated Shandong 84-79 to take a 1-0 lead in the best-of-three quarterfinals as Hassan Whiteside came off the bench to contribute
- [Fri, 24 Apr 2026] Shanghai, Beijing snatch opening wins in CBA quarterfinals
- → The 2025-26 Chinese Basketball Association (CBA) regular season concluded on Friday with the Shanghai Sharks capping a dominant campaign with a 94-8
- [Sat, 25 Apr 2026] CBA Roundup: Shanghai seals top seed with record streak, Sichuan completes winless season
- → The Shanghai Sharks carried over momentum from last season and finished top with a 38-4 record, powered by a 23-game winning streak to close the reg

## LLM Decision
- **Action:** NO
- **Confidence:** 65%
- **p_true:** 49.3%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** STAT_EDGE
- **Catalyst Strength:** 0.85

### Reasoning
Historical data shows markets priced at 59% resolve YES only 44.7% of the time (n=13,967), indicating significant crowd overpricing of YES. No specific information gap or recent catalyst was identified in news searches.

## Gate Result
- **Passed:** ✅ YES
- **Reason:** BET NO $1.00

## Tool Calls
- `search_web({'query': 'Shanghai Sharks vs Beijing Ducks CBA 2024'})` → [Wed, 20 Mar 2024] Google News
[Mon, 14 Oct 2024] CBA league: Beijing Ducks vs. Shanghai Sharks - Xi
- `search_web({'query': 'Shanghai Sharks Beijing Ducks injury report 2024'})` → [Wed, 02 Apr 2025] Google News
[Thu, 20 Mar 2025] Excitement rises for the finals push - China Daily
- `get_market_context({'keyword': 'Shanghai Sharks Beijing Ducks'})` → No related markets found for 'Shanghai Sharks Beijing Ducks'
- `search_web({'query': 'Shanghai Sharks recent results CBA 2025'})` → [Thu, 11 Dec 2025] Google News
[Mon, 03 Nov 2025] Shanghai Sharks Welcome New CBA Season With Revamp
- `search_web({'query': 'Beijing Ducks recent results CBA 2025'})` → [Mon, 26 Jan 2026] Google News
[Fri, 26 Dec 2025] Shanxi Loongs vs Beijing Ducks scores &amp; predic
- `search_web({'query': 'CBA Shanghai Sharks Beijing Ducks odds prediction'})` → [Tue, 14 Apr 2026] Google News
[Tue, 06 Jan 2026] Beijing Ducks vs Qingdao Eagles Prediction, Bettin
- `search_web({'query': 'Beijing Ducks vs Shanghai Sharks prediction 29 Dec 2025'})` → [Mon, 29 Dec 2025] Google News
[Fri, 26 Dec 2025] Beijing Ducks vs Shanghai Sharks prediction 29 Dec
- `search_web({'query': 'Shanghai Sharks injury report December 2025'})` → [Tue, 28 Oct 2025] Google News
[Thu, 01 Jan 2026] Obi Toppin injury update: Recovery timeline announ
- `search_web({'query': 'CBA standings 2025-2026 season'})` → [Mon, 05 Jan 2026] Google News
[Tue, 04 Nov 2025] 2026 Unrivaled megapreview: Rosters, rankings, rul

## Outcome
**✅ WIN** | P&L: $+1.44 | Resolved: NO

---
*Mode: LIVE | DRY_RUN: true*