"""Analysis logger — saves every market analysis as markdown for fine-tuning.

Each analysis includes:
- Market info (question, price, category, days_left)
- News sources fetched (Google News, BBC, ESPN, Binance)
- Statistical prior (p_base, model, n)
- LLM decision (action, confidence, reasoning)
- Gate result (pass/fail, why)
- Outcome (if resolved later)
"""
import os
import json
from pathlib import Path
from datetime import datetime, timezone

LOG_DIR = Path("data/analysis_logs")
LOG_DIR.mkdir(exist_ok=True)


def log_analysis(market: dict, news_ctx: str, analysis: dict, gate_passed: bool,
                 gate_reason: str = "", mode: str = "live") -> str:
    """Save full analysis to markdown file. Returns file path."""
    now = datetime.now(timezone.utc)
    ts = now.strftime("%Y%m%d_%H%M%S")
    q_slug = "".join(c if c.isalnum() else "_" for c in market.get("question","")[:40])
    fname = LOG_DIR / f"{ts}_{q_slug}.md"

    # Parse news sources
    news_sources = _parse_news_sources(news_ctx)

    lines = [
        f"# Market Analysis — {now.strftime('%Y-%m-%d %H:%M UTC')}",
        "",
        "## Market",
        f"- **Question:** {market.get('question','')}",
        f"- **Category:** {market.get('category','')}",
        f"- **YES Price:** {market.get('price',0):.1%}",
        f"- **Days Left:** {market.get('days_left','?')}",
        f"- **Volume 24h:** ${market.get('volume_24h',0):,.0f}",
        f"- **Liquidity:** ${market.get('liquidity',0):,.0f}",
        "",
        "## Statistical Prior",
        f"- **p_base:** {analysis.get('p_base', market.get('price',0)):.1%}",
        f"- **Source:** {analysis.get('p_base_source','?')}",
        f"- **N (historical):** {analysis.get('p_base_n','?')}",
        f"- **Raw gap:** {abs(analysis.get('p_base', market.get('price',0)) - market.get('price',0)):.1%}",
        "",
        "## News Sources Fetched",
    ]

    for src, items in news_sources.items():
        lines.append(f"### {src}")
        for item in items:
            lines.append(f"- {item}")
        lines.append("")

    if not news_sources:
        lines.append("_No news data available_")
        lines.append("")

    lines += [
        "## LLM Decision",
        f"- **Action:** {analysis.get('recommended_side','SKIP')}",
        f"- **Confidence:** {analysis.get('confidence',0):.0%}",
        f"- **p_true:** {analysis.get('p_true',0):.1%}",
        f"- **Information Gap:** {analysis.get('information_edge', False) or analysis.get('information_gap', False)}",
        f"- **Crowd Bias:** {analysis.get('crowd_bias', False)}",
        f"- **Catalyst Type:** {analysis.get('catalyst_type','NONE')}",
        f"- **Catalyst Strength:** {analysis.get('catalyst_score',0):.2f}",
        "",
        "### Reasoning",
        f"{analysis.get('reasoning_summary','No reasoning provided')}",
        "",
        "## Gate Result",
        f"- **Passed:** {'✅ YES' if gate_passed else '❌ NO'}",
        f"- **Reason:** {gate_reason}",
        "",
        "## Tool Calls",
    ]

    tool_log = analysis.get("tool_calls_log", [])
    if tool_log:
        for call in tool_log:
            if isinstance(call, dict):
                lines.append(f"- `{call.get('tool','')}({call.get('args','')})` → {str(call.get('result',''))[:100]}")
            else:
                lines.append(f"- {str(call)[:120]}")
    else:
        lines.append("_No tool calls_")

    lines += [
        "",
        "## Outcome",
        "_Pending — will be updated when market resolves_",
        "",
        "---",
        f"*Mode: {mode.upper()} | DRY_RUN: {os.getenv('DRY_RUN','false')}*",
    ]

    fname.write_text("\n".join(lines))
    return str(fname)


def _parse_news_sources(news_ctx: str) -> dict:
    """Parse news context string into structured sources."""
    sources = {}
    if not news_ctx:
        return sources

    current_source = "General"
    for line in news_ctx.split("\n"):
        line = line.strip()
        if not line:
            continue
        # Multi-source format
        if line.startswith("[MULTI-SOURCE NEWS]"):
            current_source = "Multi-Source"
            sources.setdefault(current_source, [])
            sources[current_source].append(line)
        elif line.startswith("  [") and line.endswith("]") and not line.startswith("  [20"):
            # Source header like "  [Bing News]"
            current_source = line.strip("[] ")
            sources.setdefault(current_source, [])
        elif line.startswith("    [") or line.startswith("    →"):
            sources.setdefault(current_source, [])
            sources[current_source].append(line.strip())
        elif line.startswith("[NEWS]"):
            current_source = "Bing/Google News"
            sources.setdefault(current_source, [])
            sources[current_source].append(line.replace("[NEWS]","").strip())
        elif line.startswith("[BBC]"):
            current_source = "BBC RSS"
            sources.setdefault(current_source, [])
            sources[current_source].append(line.replace("[BBC]","").strip())
        elif line.startswith("[OSINT:"):
            cat = line.split(":")[1].rstrip("]")
            current_source = f"OSINT ({cat})"
            sources.setdefault(current_source, [])
        elif line.startswith("[MACRO]"):
            sources.setdefault("Macro Context", [])
            sources["Macro Context"].append(line.replace("[MACRO]","").strip())
        elif line.startswith("  -") or line.startswith("  ["):
            sources.setdefault(current_source, [])
            sources[current_source].append(line.strip("- "))
        elif current_source and line and not line.startswith("#"):
            sources.setdefault(current_source, [])
            if len(sources[current_source]) < 8:
                sources[current_source].append(line[:150])

    return {k: v for k, v in sources.items() if v}


def update_outcome(market_question: str, outcome: str, pnl: float):
    """Update markdown files for a market with actual outcome."""
    if not LOG_DIR.exists():
        return
    q_lower = market_question[:50].lower()
    for f in LOG_DIR.glob("*.md"):
        try:
            content = f.read_text()
            # Match by question content
            if q_lower[:30] not in content.lower():
                continue
            if "_Pending_" not in content and "Pending —" not in content:
                continue
            icon = "✅ WIN" if pnl > 0 else "❌ LOSS"
            content = content.replace(
                "_Pending — will be updated when market resolves_",
                f"**{icon}** | P&L: ${pnl:+.2f} | Resolved: {outcome}"
            )
            f.write_text(content)
        except Exception:
            continue
