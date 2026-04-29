"""Poly-Agent Admin — Entry point with top navbar."""
import sys, os, subprocess
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Poly-Agent Admin",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

from dashboard.components.shared import (
    inject_css, badge, service_active, get_current_mode,
    switch_mode, load_trades, load_evolution, load_bankroll,
    compute_stats, get_usdc_balance
)

inject_css()

# ── auto-refresh ──────────────────────────────────────────────────────────────
try:
    from streamlit_autorefresh import st_autorefresh
    st_autorefresh(interval=30000, key="ar")
except ImportError:
    pass

# ── navbar ────────────────────────────────────────────────────────────────────
if "page" not in st.session_state:
    st.session_state.page = "dashboard"

mode   = get_current_mode()
active = service_active()

PAGES = [
    ("dashboard",  "📊 Dashboard"),
    ("trades",     "📋 Trades"),
    ("positions",  "📂 Positions"),
    ("scanner",    "🔍 Scanner"),
    ("learning",   "🧠 Learning"),
    ("settings",   "⚙️ Settings"),
]

# Status badges
ac = "#22c55e" if active else "#ef4444"
mc = "#22c55e" if mode == "demo" else "#f59e0b"
status_html = (
    f"<span class='badge' style='background:{ac}18;border:1px solid {ac};color:{ac}'>"
    f"{'● ON' if active else '● OFF'}</span>&nbsp;"
    f"<span class='badge' style='background:{mc}18;border:1px solid {mc};color:{mc}'>"
    f"{'📝 DEMO' if mode=='demo' else '💰 LIVE'}</span>"
)

# Build nav HTML
nav_items = "".join(
    f"<span class='nav-pill {'active' if st.session_state.page==key else ''}' "
    f"id='nav-{key}'>{label}</span>"
    for key, label in PAGES
)

st.markdown(f"""
<div class='navbar'>
  <span class='navbar-brand'>🤖 Poly-Agent</span>
  {nav_items}
  <span style='margin-left:auto'>{status_html}</span>
</div>
""", unsafe_allow_html=True)

# Nav buttons (invisible, positioned over HTML pills via columns)
nav_cols = st.columns([1.4] + [1.1]*len(PAGES) + [1.5])
for i, (key, label) in enumerate(PAGES):
    with nav_cols[i+1]:
        st.markdown("<div style='margin-top:-52px;opacity:0'>", unsafe_allow_html=True)
        if st.button(label, key=f"nav_{key}", use_container_width=True):
            st.session_state.page = key
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

# ── route ─────────────────────────────────────────────────────────────────────
page = st.session_state.page

if page == "dashboard":
    from dashboard.pages.pg_dashboard import render
elif page == "trades":
    from dashboard.pages.pg_trades import render
elif page == "positions":
    from dashboard.pages.pg_positions import render
elif page == "scanner":
    from dashboard.pages.pg_scanner import render
elif page == "learning":
    from dashboard.pages.pg_learning import render
elif page == "settings":
    from dashboard.pages.pg_settings import render
else:
    from dashboard.pages.pg_dashboard import render

render()

st.markdown(
    f"<div style='text-align:right;color:#374151;font-size:11px;margin-top:24px;padding-top:12px;"
    f"border-top:1px solid #1e1e3a'>Poly-Agent Admin v3.2 · "
    f"{__import__('datetime').datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}</div>",
    unsafe_allow_html=True
)
