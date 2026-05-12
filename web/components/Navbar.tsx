'use client'
import { useState } from 'react'
import Link from 'next/link'
import { LayoutDashboard, ShieldCheck, Briefcase, FileText, Brain, Settings, RefreshCw, Play, Square, RotateCcw, MoreVertical, User } from 'lucide-react'

export type Tab = 'Overview' | 'Proof' | 'Positions' | 'History' | 'Learning' | 'Config'

const BOTTOM_TABS: { id: Tab; label: string; Icon: typeof LayoutDashboard }[] = [
  { id: 'Overview',  label: 'Overview',  Icon: LayoutDashboard },
  { id: 'Proof',     label: 'Proof',     Icon: ShieldCheck },
  { id: 'Positions', label: 'Positions', Icon: Briefcase },
  { id: 'History',   label: 'History',   Icon: FileText },
  { id: 'Learning',  label: 'AI Learn',  Icon: Brain },
  { id: 'Config',    label: 'Config',    Icon: Settings },
]

const DESKTOP_TABS: Tab[] = ['Overview', 'Proof', 'Positions', 'History', 'Learning', 'Config']

interface NavbarProps {
  tab: Tab; setTab: (t: Tab) => void
  agent: { active: boolean; mode: string }
  loading: boolean; onAction: (a: string) => void; onRefresh: () => void
}

export function Navbar({ tab, setTab, agent, loading, onAction, onRefresh }: NavbarProps) {
  const [mobileMenu, setMobileMenu] = useState(false)
  const isActive = agent.active
  const isLive   = agent.mode === 'live'

  const statusPill = (active: boolean, activeLabel: string, inactiveLabel: string, activeColor: string, inactiveColor: string) => (
    <span className="status-pill" style={{
      borderColor: active ? `color-mix(in srgb, ${activeColor} 20%, transparent)` : `color-mix(in srgb, ${inactiveColor} 20%, transparent)`,
      color: active ? activeColor : inactiveColor,
      background: active ? `color-mix(in srgb, ${activeColor} 5%, transparent)` : `color-mix(in srgb, ${inactiveColor} 5%, transparent)`,
    }}>
      <span style={{ width: 6, height: 6, borderRadius: '50%', background: 'currentColor', display: 'inline-block' }} />
      {active ? activeLabel : inactiveLabel}
    </span>
  )

  return (
    <>
      {/* ── Mobile top header ── */}
      <header className="top-header">
        <span className="top-header-brand">⚡ Tritan</span>
        <div className="top-header-actions">
          {statusPill(isActive, 'ON', 'OFF', 'var(--green)', 'var(--red)')}
          {statusPill(isLive, '💰 LIVE', '📝 DEMO', 'var(--yellow)', '#60a5fa')}
          <Link href="/profile" className="icon-btn" style={{ color: 'var(--muted)', background: 'var(--bg3)' }}>
            <User size={14} />
          </Link>
          <button onClick={onRefresh} className="icon-btn" style={{ color: 'var(--muted)', background: 'var(--bg3)' }}>
            <RefreshCw size={14} />
          </button>
          <button onClick={() => setMobileMenu(m => !m)} className="icon-btn" style={{ color: 'var(--muted)', background: 'var(--bg3)' }}>
            <MoreVertical size={14} />
          </button>
        </div>
        {/* Mobile agent controls dropdown */}
        {mobileMenu && (
          <div className="absolute top-14 right-3 flex gap-2 p-2 rounded-xl z-50" style={{ background: 'var(--bg2)', border: '1px solid var(--border)', boxShadow: 'var(--shadow-lg)' }}>
            <button onClick={() => { onAction('start'); setMobileMenu(false) }} disabled={loading || isActive}
              className="icon-btn" style={{ color: 'var(--green)', background: 'var(--green-bg)', opacity: (loading || isActive) ? 0.4 : 1 }}>
              <Play size={14} />
            </button>
            <button onClick={() => { onAction('stop'); setMobileMenu(false) }} disabled={loading || !isActive}
              className="icon-btn" style={{ color: 'var(--red)', background: 'var(--red-bg)', opacity: (loading || !isActive) ? 0.4 : 1 }}>
              <Square size={14} />
            </button>
            <button onClick={() => { onAction('restart'); setMobileMenu(false) }} disabled={loading}
              className="icon-btn" style={{ color: '#60a5fa', background: 'rgba(96,165,250,0.1)', opacity: loading ? 0.4 : 1 }}>
              <RotateCcw size={14} />
            </button>
          </div>
        )}
      </header>

      {/* ── Mobile bottom nav ── */}
      <nav className="bottom-nav">
        {BOTTOM_TABS.map(({ id, label, Icon }) => (
          <button key={id} onClick={() => setTab(id)}
            className={`bottom-nav-item ${tab === id ? 'active' : ''}`}>
            <span className="nav-icon">
              <Icon size={18} strokeWidth={1.8} />
            </span>
            <span>{label}</span>
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
          {statusPill(isActive, 'ACTIVE', 'STOPPED', 'var(--green)', 'var(--red)')}
          {statusPill(isLive, '💰 LIVE', '📝 DEMO', 'var(--yellow)', '#60a5fa')}
          <Link href="/profile" className="icon-btn" style={{ color: 'var(--muted)', background: 'var(--bg3)' }}>
            <User size={14} />
          </Link>
          {[
            { Icon: Play,       action: 'start',   color: 'var(--green)', bg: 'var(--green-bg)' },
            { Icon: Square,     action: 'stop',    color: 'var(--red)',   bg: 'var(--red-bg)' },
            { Icon: RotateCcw,  action: 'restart', color: '#60a5fa',     bg: 'rgba(96,165,250,0.1)' },
            { Icon: RefreshCw,  action: 'refresh', color: 'var(--muted)', bg: 'var(--bg3)' },
          ].map(({ Icon, action, color, bg }) => (
            <button key={action}
              onClick={() => action === 'refresh' ? onRefresh() : onAction(action)}
              disabled={loading} className="icon-btn" style={{ color, background: bg }}>
              <Icon size={14} />
            </button>
          ))}
        </div>
      </nav>
    </>
  )
}
