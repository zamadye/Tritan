# Market Analysis — 2026-05-18 11:01 UTC

## Market
- **Question:** Los Angeles Dodgers vs. San Diego Padres
- **Category:** sports
- **YES Price:** 57.0%
- **Days Left:** 7
- **Volume 24h:** $57,460
- **Liquidity:** $206,635

## Statistical Prior
- **p_base:** 60.4%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 3.4%

## News Sources Fetched
### Macro Context
- Fear&Greed: 28/100 (Fear) | trend: deteriorating
- BTC: $76,783 (-2.1% 24h) → risk-OFF
- Fear&Greed: 28/100 (Fear) | 7d trend: deteriorating
- BTC: $76,788 (-2.1% 24h) → risk-OFF
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 28(Fear) → 27(Fear) → 31(Fear) → 43(Fear) | sentiment worsening
- Will the Fed increase interest rates by 25 bps after the Jun → YES=50%
- [SPORTS] Injuries:
- ?: Pavin Smith — 60-Day-IL (Surgery)
- ?: Carlos Santana — 10-Day-IL (Strain)
- ?: Jordan Lawlar — 60-Day-IL (Fracture)
- ?: Denzel Clarke — 10-Day-IL (Bruise)
- ?: Brooks Kriske — 15-Day-IL (Pinched Nerve)

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: angeles dodgers diego padres
- [Bing News]
- [Mon, 18 May 2026] angeles dodgers diego padres
- → Los Angeles Dodgers (29-18, first in the NL West) vs. San Diego Padres (28-18, second in the NL West) San Diego; Monday, 9:40 p.m. EDT. PITCHING PRO
- [Mon, 18 May 2026] Dodgers take win streak into matchup with the Padres
- → Starting Monday night, one of the best rivalries in Major League Baseball will return. The Los Angeles Dodgers and the […] ...
- [Mon, 18 May 2026] Rivalry returns: Padres, Dodgers clash for first time this season
- → Here's how to watch Monday's San Diego Padres vs Los Angeles Dodgers game, including start times, TV channels, scores and how to stream.

## LLM Decision
- **Action:** SKIP
- **Confidence:** 64%
- **p_true:** 54.4%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_PATTERN
- **Catalyst Strength:** 0.65

### Reasoning
Large-sample statistical signal (n=13,967) shows markets at 57% resolve YES only 44.7% of the time — a 12.3% overpricing of YES. No game-specific catalyst (balanced injuries, no confirmed starters, 7 days out) contradicts this. While the Entry 50-60% WR=25% pattern is a warning, it's based on only 4 trades vs. 13,967 for the stat signal. Confidence moderate due to lack of bookmaker odds cross-verification and the small-sample warning pattern.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=3%<5%

## Tool Calls
- `get_sports_data({'team': 'Los Angeles Dodgers', 'sport': 'mlb'})` → INJURY [los angeles dodgers] Brusdar Graterol (RP): 60-Day-IL
INJURY [los angeles dodgers] Jack Drey
- `get_sports_data({'sport': 'mlb', 'team': 'San Diego Padres'})` → INJURY [san diego padres] German Marquez (SP): 15-Day-IL
INJURY [san diego padres] Jhony Brito (RP):
- `get_odds({'sport': 'baseball_mlb', 'team': 'Los Angeles Dodgers'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap
- `get_market_context({'keyword': 'Los Angeles Dodgers San Diego Padres'})` → No related markets found for 'Los Angeles Dodgers San Diego Padres'
- `search_web({'query': 'Los Angeles Dodgers vs San Diego Padres 2025 news and injuries'})` → [Sun, 17 May 2026] Google News
[Fri, 15 Aug 2025] Fantasy baseball: Gasser, Rodriguez called up for 
- `search_web({'query': 'MLB news today Dodgers Padres matchup prediction'})` → [Sun, 17 May 2026] Google News
[Fri, 24 Apr 2026] Padres vs. Mariners prediction: Seattle favored to
- `search_web({'query': 'Los Angeles Dodgers vs San Diego Padres May 20 2026'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] How to Watch Dodgers vs. Padres: Streaming &amp; T
- `search_web({'query': 'Padres vs Dodgers starting pitchers next week'})` → [Sun, 17 May 2026] Google News
[Fri, 15 May 2026] Dodgers Announce Starting Pitchers for Padres Seri
- `search_web({'query': 'Shohei Ohtani pitching or batting Padres series May 2026'})` → [Mon, 18 May 2026] Google News
[Sun, 17 May 2026] Dodgers take win streak into matchup with the Padr
- `search_web({'query': 'Padres starting pitcher May 20 2026'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] Los Angeles Dodgers vs San Diego Padres Odds - Wed
- `search_web({'query': 'Shohei Ohtani pitching May 2026 update'})` → [Mon, 18 May 2026] Google News
[Mon, 18 May 2026] Roki Sasaki, offense dominate as Dodgers rout Ange
- `search_web({'query': 'Padres Dodgers series preview betting odds May 20 2026'})` → [Mon, 18 May 2026] Google News
[Sun, 17 May 2026] Los Angeles Dodgers vs San Diego Padres Odds - Wed
- `get_odds({'sport': 'baseball_mlb', 'team': 'San Diego Padres'})` → Odds API error: 401 {"message":"Usage quota has been reached. See usage plans at https://the-odds-ap

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*