"""Poly-Agent Admin — Entry point with top navbar."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import streamlit as st

st.set_page_config(
    page_title="Poly-Agent Admin",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

from dashboard.components.shared import (
    inject_css, service_active, get_current_mode,
    switch_mode, compute_stats
)

inject_css()

# Hide Streamlit default elements + sidebar completely
st.markdown("""<style>
section[data-testid="stSidebar"]{display:none!important}
#MainMenu{visibility:hidden!important}
header[data-testid="stHeader"]{display:none!important}
footer{display:none!important}
.block-container{padding-top:1rem!important}
</style>""", unsafe_allow_html=True)

# ── auto-refresh ──────────────────────────────────────────────────────────────
try:
    from streamlit_autorefresh import st_autorefresh
    st_autorefresh(interval=30000, key="ar")
except ImportError:
    pass

# ── state ─────────────────────────────────────────────────────────────────────
if "page" not in st.session_state:
    st.session_state.page = "dashboard"

mode   = get_current_mode()
active = service_active()

PAGES = [
    ("dashboard", "📊 Dashboard"),
    ("trades",    "📋 Trades"),
    ("positions", "📂 Positions"),
    ("scanner",   "🔍 Scanner"),
    ("learning",  "🧠 Learning"),
    ("settings",  "⚙️ Settings"),
]

# ── navbar ────────────────────────────────────────────────────────────────────
ac = "#22c55e" if active else "#ef4444"
mc = "#22c55e" if mode=="demo" else "#f59e0b"

# Brand + status on left, nav buttons in columns
brand_col, *nav_cols, status_col = st.columns([1.2] + [0.9]*len(PAGES) + [1.4])

brand_col.markdown(
    f"<div style='padding:6px 0;font-size:16px;font-weight:700;color:#7c7cff'>🤖 Poly-Agent</div>",
    unsafe_allow_html=True
)

for col, (key, label) in zip(nav_cols, PAGES):
    is_active = st.session_state.page == key
    # Active page button styled differently via CSS class trick
    if col.button(label, key=f"nav_{key}", use_container_width=True,
                  type="primary" if is_active else "secondary"):
        st.session_state.page = key
        st.rerun()

status_col.markdown(
    f"<div style='text-align:right;padding:6px 0'>"
    f"<span style='background:{ac}18;border:1px solid {ac};color:{ac};"
    f"padding:3px 8px;border-radius:12px;font-size:11px;font-weight:600;margin-right:6px'>"
    f"{'● ON' if active else '● OFF'}</span>"
    f"<span style='background:{mc}18;border:1px solid {mc};color:{mc};"
    f"padding:3px 8px;border-radius:12px;font-size:11px;font-weight:600'>"
    f"{'📝 DEMO' if mode=='demo' else '💰 LIVE'}</span></div>",
    unsafe_allow_html=True
)

st.markdown("<div style='height:1px;background:#1e1e3a;margin:4px 0 16px 0'></div>", unsafe_allow_html=True)

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
    f"<div style='text-align:right;color:#374151;font-size:11px;margin-top:24px;"
    f"padding-top:12px;border-top:1px solid #1e1e3a'>"
    f"Poly-Agent Admin v3.2 · {__import__('datetime').datetime.utcnow().strftime('%H:%M UTC')}</div>",
    unsafe_allow_html=True
)
