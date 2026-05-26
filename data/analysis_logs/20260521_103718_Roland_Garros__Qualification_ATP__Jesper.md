# Market Analysis — 2026-05-21 10:37 UTC

## Market
- **Question:** Roland Garros, Qualification ATP: Jesper de Jong vs Michael Zheng
- **Category:** sports
- **YES Price:** 52.0%
- **Days Left:** 7
- **Volume 24h:** $50,961
- **Liquidity:** $39,751

## Statistical Prior
- **p_base:** 53.0%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 1.0%

## News Sources Fetched
### Macro Context
- Fear&Greed: 29/100 (Fear) | trend: improving
- BTC: $77,206 (-0.4% 24h) → neutral
- Fear&Greed: 29/100 (Fear) | 7d trend: improving
- BTC: $77,322 (-0.2% 24h) → neutral

### General
- [FEAR&GREED 7d trend] 29(Fear) → 27(Fear) → 25(Extr) → 28(Fear) | sentiment improving

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: roland garros qualification atp: jesper
- [Bing News]
- [Mon, 15 Dec 2025] roland garros qualification atp: jesper
- → The schedule for Day Seven of Roland Garros French Open 2025 has been released, marking the conclusion of the third round, featuring the top-half of
- [Wed, 28 May 2025] Schedule ATP WTA Roland Garros 2025 Day Seven featuring Jannik Sinner, Coco Gauff and Novak Djokovic
- → World No. 3 Alexander Zverev will continue his campaign at Roland Garros with a second-round clash against Dutch player Jesper de Jong. Zverev overc
- [Mon, 19 May 2025] French Open 2025: Alexander Zverev vs Jesper De Jong preview, head-to-head, prediction and pick | Roland Garros
- → With the Entry Lists now confirmed for the 2025 French Open at Roland Garros between May 25 - June 8, the Prize Money has now been set with a record

## LLM Decision
- **Action:** SKIP
- **Confidence:** 65%
- **p_true:** 45.0%
- **Information Gap:** True
- **Crowd Bias:** False
- **Catalyst Type:** STATISTICAL_BASE_RATE
- **Catalyst Strength:** 0.70

### Reasoning
Strong statistical signal (n=13,967) indicates markets at 52% YES historically resolve YES only 44.7% of time — a 7.3pp overpricing of YES. While De Jong appears more experienced (ATP tour level) vs Zheng (NCAA champion), qualification matches show systematic overpricing of the perceived favorite at near coin-flip prices. The 7.3pp edge is substantial with large sample backing. However, confidence capped at 0.67 due to: (1) limited player-specific injury/form data, (2) general pattern rather than match-specific catalyst, (3) low WR for 50-60% entry points (25% from 12 trades) warrants caution despite overall sports pattern strength (70% WR).

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=1%<5%

## Tool Calls
- `get_odds({'sport': 'tennis_atp', 'team': 'de Jong'})` → Odds API error: 404 {"message":"Unknown sport","error_code":"UNKNOWN_SPORT","details_url":"https://t
- `search_web({'query': 'Jesper de Jong Michael Zheng Roland Garros qualification 2025'})` → [Sun, 17 May 2026] Google News
[Mon, 18 May 2026] Big names headline qualifying draws - Roland-Garro
- `search_web({'query': 'Jesper de Jong recent form tennis 2025'})` → [Tue, 22 Jul 2025] Google News
[Fri, 12 Sep 2025] Highlights: De Jong continues impressive form in U
- `get_market_context({'keyword': 'Roland Garros qualification'})` → No related markets found for 'Roland Garros qualification'
- `search_web({'query': 'Jesper de Jong Roland Garros 2026 qualification form'})` → [Mon, 18 May 2026] Google News
[Wed, 20 May 2026] Early riser De Jong advances - Roland-Garros 2026

- `search_web({'query': 'Jesper de Jong 2025 ATP results form'})` → [Tue, 22 Jul 2025] Google News
[Mon, 18 Aug 2025] Highlights: De Jong continues impressive form in U
- `search_web({'query': 'Michael Zheng tennis 2025 results'})` → [Sun, 23 Nov 2025] Google News
[Thu, 12 Mar 2026] Michael Zheng Defends NCAA Singles Crown - Columbi
- `get_sports_data({'sport': 'tennis', 'team': 'de Jong'})` → No injury data found for tennis de Jong
- `search_web({'query': 'Roland Garros 2026 qualifying results Jesper de Jong Michael Zheng'})` → [Wed, 20 May 2026] Google News
[Mon, 18 May 2026] Zheng hoping to graduate to big time in Paris - Ro
- `search_web({'query': '"Zheng hoping to graduate to big time in Paris" Roland Garros'})` → [Wed, 20 May 2026] Google News
[Wed, 20 May 2026] Zheng hoping to graduate to big time in Paris - Ro

## Outcome
_Pending — will be updated when market resolves_

---
*Mode: LIVE | DRY_RUN: true*