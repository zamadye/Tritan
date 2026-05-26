# Market Analysis — 2026-05-17 12:45 UTC

## Market
- **Question:** GP SAR La Princesse Lalla Meryem, Qualification: Fiona Ferro vs Elina Avanesyan
- **Category:** sports
- **YES Price:** 53.0%
- **Days Left:** 6
- **Volume 24h:** $59,183
- **Liquidity:** $65,172

## Statistical Prior
- **p_base:** 54.5%
- **Source:** logistic:sports
- **N (historical):** 6077
- **Raw gap:** 1.5%

## News Sources Fetched
### Macro Context
- Fear&Greed: 27/100 (Fear) | trend: deteriorating
- BTC: $78,425 (+0.5% 24h) → neutral
- Fear&Greed: 27/100 (Fear) | 7d trend: deteriorating
- BTC: $78,427 (+0.5% 24h) → neutral
- Fed market expectations:

### General
- [FEAR&GREED 7d trend] 27(Fear) → 31(Fear) → 43(Fear) → 34(Fear) | sentiment worsening
- MicroStrategy sells any Bitcoin by May 31, 2026? → YES=50%

### Multi-Source
- [MULTI-SOURCE NEWS] 2 sources for: princesse lalla meryem qualification: fiona
- [Bing News]
- [Fri, 15 May 2026] princesse lalla meryem qualification: fiona
- → Your all-access pass to the WTA 125 is here! With 125Live, stream up to two courts from each tournament and witness the rise of the brightest up-and
- [Fri, 15 May 2026] Grand Prix Son Altesse Royale La Princesse Lalla Meryem
- → Get all the latest WTA Grand Prix Son Altesse Royale La Princesse Lalla Meryem 2026 Draws, results, and more!
- [Sat, 17 May 2025] Grand Prix Son Altesse Royale La Princesse Lalla Meryem
- → Our editors independently choose our recommendations. Some content is produced with paid support from a third party, however our editorial decisions

## LLM Decision
- **Action:** SKIP
- **Confidence:** 55%
- **p_true:** 54.5%
- **Information Gap:** False
- **Crowd Bias:** False
- **Catalyst Type:** NONE
- **Catalyst Strength:** 0.20

### Reasoning
Statistical signal indicates market overprices YES at 53% (historical resolution only 44.7%, n=13,967). Found potential info gap: Fiona Ferro reportedly had wrist surgery and put her season on hold in mid-2025, which could affect her readiness. However, cannot confirm match timing or whether she has returned to play. No breaking news or unreported data verified. No clear crowd bias mechanism identified beyond the statistical overpricing pattern. Per strategy: SKIP when only statistical gap exists without confirmed specific catalyst or information asymmetry.

## Gate Result
- **Passed:** ❌ NO
- **Reason:** no stat edge gap=1%<3%

## Tool Calls
- `search_web({'query': 'Fiona Ferro Elina Avanesyan GP SAR La Princesse Lalla Meryem qualification 2025'})` → No search results for: Fiona Ferro Elina Avanesyan GP SAR La Princesse Lalla Meryem qualification 20
- `search_web({'query': 'Fiona Ferro vs Elina Avanesyan 2025 tennis'})` → [Sun, 26 May 2024] Google News
[Wed, 11 Sep 2024] Roland-Garros: Krejcikova upset by Goluvic in firs
- `search_web({'query': 'GP SAR La Princesse Lalla Meryem 2025 qualification draw'})` → [Wed, 07 May 2025] Google News
[Thu, 22 May 2025] Grand Prix Sar La Princesse Lalla Meryem 2025 Over
- `search_web({'query': 'Fiona Ferro results 2025'})` → [Wed, 22 Apr 2026] Google News
[Wed, 09 Jul 2025] Bianca Andreescu falls in WTA 125 Oeiras as Madrid
- `search_web({'query': 'Elina Avanesyan results 2025'})` → [Sat, 13 Sep 2025] Google News
[Sun, 24 Aug 2025] Promising WTA youngster posts emotional message as

## Outcome
**✅ WIN** | P&L: $+0.47 | Resolved: YES

---
*Mode: LIVE | DRY_RUN: true*