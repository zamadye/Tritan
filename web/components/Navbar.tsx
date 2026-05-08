'use client'
import { RefreshCw, Play, Square, RotateCcw } from 'lucide-react'

type Tab = 'Overview' | 'Proof' | 'Positions' | 'Trades' | 'Learning' | 'Config'

const BOTTOM_TABS: { id: Tab; label: string; d: string }[] = [
  { id: 'Overview',  label: 'Overview',  d: 'M3 3h7v7H3zM14 3h7v7h-7zM14 14h7v7h-7zM3 14h7v7H3z' },
  { id: 'Positions', label: 'Positions', d: 'M12 1v22M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6' },
  { id: 'Trades',    label: 'Trades',    d: 'M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8zM14 2v6h6M16 13H8M16 17H8M10 9H8' },
  { id: 'Learning',  label: 'Learning',  d: 'M22 10v6M2 10l10-5 10 5-10 5zM6 12v5c3 3 9 3 12 0v-5' },
  { id: 'Config',    label: 'Config',    d: 'M12 15a3 3 0 1 0 0-6 3 3 0 0 0 0 6zM19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1-2.83 2.83l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-4 0v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83-2.83l.06-.06A1.65 1.65 0 0 0 4.68 15a1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1 0-4h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 2.83-2.83l.06.06A1.65 1.65 0 0 0 9 4.68a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 4 0v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 2.83l-.06.06A1.65 1.65 0 0 0 19.4 9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 0 4h-.09a1.65 1.65 0 0 0-1.51 1z' },
]

const DESKTOP_TABS: Tab[] = ['Overview', 'Proof', 'Positions', 'Trades', 'Learning', 'Config']

interface NavbarProps {
  tab: Tab; setTab: (t: Tab) => void
  agent: { active: boolean; mode: string }
  loading: boolean; onAction: (a: string) => void; onRefresh: () => void
}

export function Navbar({ tab, setTab, agent, loading, onAction, onRefresh }: NavbarProps) {
  const isActive = agent.active
  const isLive   = agent.mode === 'live'

  return (
    <>
      {/* ── Mobile top header ── */}
      <header className="top-header">
        <span className="top-header-brand">⚡ Tritan</span>
        <div className="top-header-actions">
          <span className="status-pill" style={{
            borderColor: isActive ? '#22c55e44' : '#ef444444',
            color: isActive ? '#22c55e' : '#ef4444',
            background: isActive ? 'rgba(34,197,94,0.08)' : 'rgba(239,68,68,0.08)',
          }}>
            <span style={{ width: 6, height: 6, borderRadius: '50%', background: 'currentColor', display: 'inline-block' }} />
            {isActive ? 'ON' : 'OFF'}
          </span>
          <span className="status-pill" style={{
            borderColor: isLive ? '#f59e0b44' : '#60a5fa44',
            color: isLive ? '#f59e0b' : '#60a5fa',
            background: isLive ? 'rgba(245,158,11,0.08)' : 'rgba(96,165,250,0.08)',
          }}>
            {isLive ? '💰' : '📝'} {isLive ? 'LIVE' : 'DEMO'}
          </span>
          <button onClick={onRefresh} className="icon-btn" style={{ color: '#94a3b8', background: '#1e1e3a' }}>
            <RefreshCw size={13} />
          </button>
        </div>
      </header>

      {/* ── Mobile bottom nav ── */}
      <nav className="bottom-nav">
        {BOTTOM_TABS.map(t => (
          <button key={t.id} onClick={() => setTab(t.id)}
            className={`bottom-nav-item ${tab === t.id ? 'active' : ''}`}>
            <span className="nav-icon">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round">
                <path d={t.d} />
              </svg>
            </span>
            <span>{t.label}</span>
          </button>
        ))}
      </nav>

      {/* ── Desktop top nav ── */}
      <nav className="desktop-nav">
        <span className="desktop-nav-brand">⚡ Tritan</span>
        <div className="desktop-nav-tabs">
          {DESKTOP_TABS.map(t => (
            <button key={t} onClick={() => setTab(t)}
              className={`desktop-nav-tab ${tab === t ? 'active' : ''}`}>{t}</button>
          ))}
        </div>
        <div className="desktop-nav-actions">
          <span className="status-pill" style={{
            borderColor: isActive ? '#22c55e44' : '#ef444444',
            color: isActive ? '#22c55e' : '#ef4444',
            background: isActive ? 'rgba(34,197,94,0.08)' : 'rgba(239,68,68,0.08)',
          }}>
            <span style={{ width: 6, height: 6, borderRadius: '50%', background: 'currentColor', display: 'inline-block' }} />
            {isActive ? 'ACTIVE' : 'STOPPED'}
          </span>
          <span className="status-pill" style={{
            borderColor: isLive ? '#f59e0b44' : '#60a5fa44',
            color: isLive ? '#f59e0b' : '#60a5fa',
            background: isLive ? 'rgba(245,158,11,0.08)' : 'rgba(96,165,250,0.08)',
          }}>
            {isLive ? '💰 LIVE' : '📝 DEMO'}
          </span>
          {[
            { icon: <Play size={13} />, action: 'start',   color: '#22c55e', bg: 'rgba(34,197,94,0.1)'   },
            { icon: <Square size={13} />, action: 'stop',  color: '#ef4444', bg: 'rgba(239,68,68,0.1)'   },
            { icon: <RotateCcw size={13} />, action: 'restart', color: '#60a5fa', bg: 'rgba(96,165,250,0.1)' },
            { icon: <RefreshCw size={13} />, action: 'refresh', color: '#94a3b8', bg: '#1e1e3a'           },
          ].map(({ icon, action, color, bg }) => (
            <button key={action}
              onClick={() => action === 'refresh' ? onRefresh() : onAction(action)}
              disabled={loading} className="icon-btn" style={{ color, background: bg }}>
              {icon}
            </button>
          ))}
        </div>
      </nav>
    </>
  )
}
