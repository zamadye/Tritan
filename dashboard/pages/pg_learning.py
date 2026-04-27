import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from collections import Counter
import streamlit as st
from dashboard.components.shared import load_evolution, load_trades, get_current_mode

def render():
    mode = get_current_mode()
    evo  = load_evolution()

    st.subheader("🧠 Evolution Learning System")
    if not evo:
        st.info("No evolution data yet — need resolved trades first."); return

    c1,c2,c3 = st.columns(3)
    c1.metric("Resolved Trades",      evo.get("total_resolved",0))
    c2.metric("Overall Win Rate",     f"{evo.get('overall_win_rate',0):.0%}")
    c3.metric("Overconfidence Events",len(evo.get("overconfidence_patterns",[])))
    st.divider()

    left, right = st.columns(2)

    with left:
        st.markdown("**Category Bias**")
        bias = evo.get("category_bias",{})
        if bias:
            for cat, info in bias.items():
                ic = "🔴" if info.get("status")=="AVOID" else "🟡"
                st.markdown(f"{ic} **{cat}**: {info.get('win_rate',0):.0%} WR — {info.get('note','')[:70]}")
        else:
            st.caption("No bias detected yet (need 3+ bets per category)")

        st.markdown("**Calibration Adjustments**")
        cal = evo.get("calibration_adjustments",{})
        if cal:
            for cat, adj in cal.items():
                st.markdown(f"- **{cat}**: {adj:+.0%} to p_true")
        else:
            st.caption("None yet")

        st.markdown("**Overconfidence by Category**")
        oc = Counter(p.get("category","?") for p in evo.get("overconfidence_patterns",[]))
        for cat, cnt in oc.most_common():
            bar = "█" * min(cnt, 20)
            st.markdown(f"⚠️ **{cat}**: {cnt}x `{bar}`")

    with right:
        st.markdown("**Recent Mistakes (last 5)**")
        for m in evo.get("recent_mistakes",[]):
            q    = m.get("question_snippet") or m.get("question","?")
            conf = m.get("confidence",0)
            with st.expander(f"❌ [{m.get('category','?')}] {str(q)[:52]}"):
                st.markdown(f"Predicted **{m.get('predicted_side','?')}** → Actual **{m.get('actual_outcome','?')}**")
                st.markdown(f"Confidence: **{conf:.0%}**" if isinstance(conf,float) else f"Confidence: {conf}")
                st.warning(m.get("lesson","?"))

        st.markdown("**LLM Context Preview**")
        from agent.learner import get_evolution_context
        ctx = get_evolution_context(mode)
        st.code(ctx[:600] if ctx else "Empty", language=None)

    st.divider()
    if st.button("🔄 Force Regenerate Lessons"):
        trades = load_trades(mode)
        from agent.learner import _generate_evolution_lessons
        _generate_evolution_lessons(trades, mode)
        st.cache_data.clear(); st.success("Regenerated!"); st.rerun()
