# Market Analysis — 2026-05-19 08:30 UTC

## Market
- **Question:** Bengaluru 3: Maximus Jones vs Sasikumar Mukund
- **Category:** sports
- **YES Price:** 53.0%
- **Days Left:** 5
- **Volume 24h:** $70,269
- **Liquidity:** $18,416

## Statistical Prior
- **p_base:** 54.5%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 1.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 25/100 (Extreme Fear) | trend: deteriorating
- BTC: $76,956 (-0.0% 24h) → neutral
- Fear&Greed: 25/100 (Extreme Fear) | 7d trend: deteriorating
- BTC: $76,956 (-0.0% 24h) → neutral

### General
- [FEAR&GREED 7d trend] 25(Extr) → 28(Fear) → 27(Fear) → 31(Fear) | sentiment worsening

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: bengaluru maximus jones sasikumar mukund
- [Bing News]
- [Sat, 19 Mar 2022] bengaluru maximus jones sasikumar mukund
- → Bengaluru, March 15 (IANS) Top seed Mukund Sasikumar survived a first-round exit scare against unseeded Rishab Agarwal in the SKME ITF Open being at
- [Mon, 05 Jan 2026] Bengaluru ITF Open: Sasikumar survives scare, Nishant shines
- → BENGALURU: India hosted four ATP Challenger events in early 2025, but singles players from the host nation fired blanks. The win-loss record in the 
- [] Bengaluru Open: Focus on Sumit Nagal
- [Metaculus]

## LLM Decision
- **Action:** SKIP
- **Confidence:** 52%
- **p_true:** 54.5%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_PATTERN_ONLY
- **Catalyst Strength:** 0.45

### Reasoning
Market at 53% historically resolves YES only 44.7% (n=13,967), suggesting ~8% overpricing. However, entry 50-60% range has only 33% WR (n=6) in my trades, and no verifiable catalyst found — both players are low-ranked Challenger competitors with mixed recent results (Mukund lost 0-2 to Stewart May 13, Jones lost 1-2 to Sekulic April 7). The historical overpricing signal is notable but lacks a concrete informational edge or direct catalyst to act on. Macro fear sentiment irrelevant to sports. Without specific player form data, injury info, or surface advantage evidence, the edge remains purely statistical but insufficient for action.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=1%<5%

## Tool Calls
- `get_odds({'sport': 'tennis_atp', 'team': 'Maximus Jones'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `search_web({'query': 'Maximus Jones vs Sasikumar Mukund tennis Bengaluru 2025'})` → [Sat, 09 May 2026] Google News
[Mon, 11 May 2026] H2H Maximus Jones Vs Mukund Sasikumar stats, predi
- `search_web({'query': 'Sasikumar Mukund recent results ATP 2025'})` → [Tue, 05 Aug 2025] Google News
[Wed, 11 Feb 2026] Sasikumar Mukund Tianhui Zhang live score and H2H 
- `search_web({'query': 'Maximus Jones ATP tennis 2025'})` → [Mon, 18 May 2026] Google News
[Fri, 26 Dec 2025] Southeast Asia’s top tennis singles players: Who a
- `search_web({'query': '"Maximus Jones" tennis ranking 2026'})` → [Wed, 01 Apr 2026] Google News
[Tue, 22 Apr 2025] Ellis vs Jones - Miyazaki 2026 - Tennis Temple - L
- `search_web({'query': '"Mukund Sasikumar" tennis ranking 2026 Bengaluru'})` → [Mon, 05 Jan 2026] Google News
[Sun, 11 Feb 2024] Bengaluru Open: Focus on Sumit Nagal - The Times o
- `get_market_context({'keyword': 'Bengaluru tennis'})` → No related markets found for 'Bengaluru tennis'
- `search_web({'query': 'Maximus Jones tennis results 2026 recent matches'})` → [Sat, 07 Feb 2026] Google News
[Mon, 06 Apr 2026] Maximus Jones v Marko Mesarovic results, H2H stats
- `search_web({'query': 'Mukund Sasikumar results 2026 recent matches'})` → [Tue, 12 May 2026] Google News
[Wed, 13 May 2026] Sasi Kumar Mukund 0 - 2 Hamish Stewart (05/13) - G
- `search_web({'query': 'Maximus Jones Mukund Sasikumar betting odds Bengaluru challenger 2026'})` → [Mon, 11 May 2026] Google News
[Tue, 12 May 2026] H2H, prediction of Mukund Sasikumar vs Mitsuki Wei
- `search_web({'query': '"Jones" "Mukund" Bengaluru tennis prediction'})` → [Sat, 09 May 2026] Google News
[Tue, 12 May 2026] H2H Maximus Jones Vs Mukund Sasikumar stats, predi

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*