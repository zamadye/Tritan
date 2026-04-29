import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from collections import Counter
import streamlit as st
from dashboard.components.shared import load_evolution, load_trades, get_current_mode

def render():
    mode = get_current_mode()
    evo  = load_evolution()

    st.markdown("<h2>🧠 Evolution Learning</h2>", unsafe_allow_html=True)

    if not evo:
        st.info("No evolution data yet — need resolved trades first."); return

    oc = len(evo.get("overconfidence_patterns",[]))
    c1,c2,c3 = st.columns(3)
    c1.metric("Resolved Trades",       evo.get("total_resolved",0))
    c2.metric("Overall Win Rate",      f"{evo.get('overall_win_rate',0):.0%}")
    c3.metric("Overconfidence Events", oc)

    st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)
    left, right = st.columns(2)

    with left:
        # Category bias
        st.markdown("<div class='card-title'>Category Bias</div>", unsafe_allow_html=True)
        bias = evo.get("category_bias",{})
        if bias:
            rows = ""
            for cat, info in bias.items():
                s = info.get("status","?")
                dot_c = "#ef4444" if s=="AVOID" else "#f59e0b"
                gap   = info.get("conf_gap",0)
                rows += (
                    f"<div style='display:flex;justify-content:space-between;align-items:center;"
                    f"padding:8px 0;border-bottom:1px solid #1e1e3a;font-size:13px'>"
                    f"<span><span style='color:{dot_c}'>●</span> <b>{cat}</b></span>"
                    f"<span style='color:#6b7280'>WR {info.get('win_rate',0):.0%} · gap {gap:+.0%}</span>"
                    f"<span style='color:{dot_c};font-size:11px;font-weight:600'>{s}</span></div>"
                )
            st.markdown(f"<div style='background:#16162a;border:1px solid #2a2a4a;border-radius:10px;padding:12px 16px'>{rows}</div>", unsafe_allow_html=True)
        else:
            st.caption("No bias detected yet (need 3+ bets per category)")

        st.markdown("<div style='height:12px'></div>", unsafe_allow_html=True)

        # Calibration adjustments
        st.markdown("<div class='card-title'>Calibration Adjustments</div>", unsafe_allow_html=True)
        cal = evo.get("calibration_adjustments",{})
        if cal:
            rows = ""
            for cat, adj in cal.items():
                c = "#22c55e" if adj>0 else "#ef4444"
                rows += (f"<div style='display:flex;justify-content:space-between;padding:6px 0;"
                         f"border-bottom:1px solid #1e1e3a;font-size:13px'>"
                         f"<span>{cat}</span><span style='color:{c};font-weight:600'>{adj:+.0%} to p_true</span></div>")
            st.markdown(f"<div style='background:#16162a;border:1px solid #2a2a4a;border-radius:10px;padding:12px 16px'>{rows}</div>", unsafe_allow_html=True)
        else:
            st.caption("None yet")

        st.markdown("<div style='height:12px'></div>", unsafe_allow_html=True)

        # Edge reality
        st.markdown("<div class='card-title'>Edge Reality (claimed → actual WR)</div>", unsafe_allow_html=True)
        er = evo.get("edge_reality",{})
        if er:
            rows = ""
            for b in sorted(er.keys(), key=lambda x: float(x.strip('%'))):
                d   = er[b]; wr = d["actual_wr"]; n = d["n"]
                gap = float(b.strip('%'))/100 - wr
                c   = "#ef4444" if gap>0.15 else "#22c55e"
                rows += (f"<div style='display:flex;justify-content:space-between;padding:5px 0;"
                         f"border-bottom:1px solid #1e1e3a;font-size:12px'>"
                         f"<span style='color:#94a3b8'>claimed {b}</span>"
                         f"<span>actual WR <b style='color:{c}'>{wr:.0%}</b></span>"
                         f"<span style='color:#6b7280'>n={n}</span></div>")
            st.markdown(f"<div style='background:#16162a;border:1px solid #2a2a4a;border-radius:10px;padding:12px 16px'>{rows}</div>", unsafe_allow_html=True)

    with right:
        # Recent mistakes
        st.markdown("<div class='card-title'>Recent Mistakes</div>", unsafe_allow_html=True)
        for m in evo.get("recent_mistakes",[]):
            q    = m.get("question_snippet") or m.get("question","?")
            conf = m.get("confidence",0)
            with st.expander(f"❌  [{m.get('category','?')}]  {str(q)[:52]}"):
                st.markdown(
                    f"<div style='font-size:13px;margin-bottom:6px'>"
                    f"Predicted <b>{m.get('predicted_side','?')}</b> → Actual <b>{m.get('actual_outcome','?')}</b> · "
                    f"Conf <b>{conf:.0%}</b></div>" if isinstance(conf,float) else
                    f"<div style='font-size:13px;margin-bottom:6px'>"
                    f"Predicted <b>{m.get('predicted_side','?')}</b> → Actual <b>{m.get('actual_outcome','?')}</b></div>",
                    unsafe_allow_html=True
                )
                st.warning(m.get("lesson","?"))

        st.markdown("<div style='height:12px'></div>", unsafe_allow_html=True)

        # LLM context preview
        st.markdown("<div class='card-title'>LLM Context Preview</div>", unsafe_allow_html=True)
        from agent.learner import get_evolution_context
        ctx = get_evolution_context(mode)
        st.code(ctx[:700] if ctx else "Empty", language=None)

    st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)
    if st.button("🔄 Regenerate Lessons", type="primary"):
        trades = load_trades(mode)
        from agent.learner import _generate_evolution_lessons
        _generate_evolution_lessons(trades, mode)
        st.cache_data.clear(); st.success("Regenerated!"); st.rerun()
