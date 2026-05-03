'use client'
import { RefreshCw, Play, Square, RotateCcw } from 'lucide-react'

type Tab = 'Overview' | 'Proof' | 'Positions' | 'Trades' | 'Learning' | 'Settings'
const TABS: Tab[] = ['Overview', 'Proof', 'Positions', 'Trades', 'Learning', 'Settings']

interface NavbarProps {
  tab: Tab; setTab: (t: Tab) => void
  agent: { active: boolean; mode: string }
  loading: boolean; onAction: (a: string) => void; onRefresh: () => void
}

export function Navbar({ tab, setTab, agent, loading, onAction, onRefresh }: NavbarProps) {
  return (
    <nav className="navbar">
      <span className="nav-brand">🤖 Tritan</span>

      <div className="nav-tabs">
        {TABS.map(t => (
          <button key={t} onClick={() => setTab(t)} className={`nav-tab ${tab === t ? 'active' : ''}`}>{t}</button>
        ))}
      </div>

      <div className="nav-actions">
        <span className="status-badge" style={{
          border: `1px solid ${agent.active ? '#22c55e' : '#ef4444'}`,
          color: agent.active ? '#22c55e' : '#ef4444',
          background: agent.active ? 'rgba(34,197,94,0.1)' : 'rgba(239,68,68,0.1)',
        }}>
          {agent.active ? '● ACTIVE' : '● STOPPED'}
        </span>
        <span className="status-badge" style={{
          border: `1px solid ${agent.mode === 'demo' ? '#60a5fa' : '#f59e0b'}`,
          color: agent.mode === 'demo' ? '#60a5fa' : '#f59e0b',
          background: agent.mode === 'demo' ? 'rgba(96,165,250,0.1)' : 'rgba(245,158,11,0.1)',
        }}>
          {agent.mode === 'demo' ? '📝 DEMO' : '💰 LIVE'}
        </span>

        {[
          { icon: <Play size={13} />, action: 'start', color: '#22c55e', bg: 'rgba(34,197,94,0.1)' },
          { icon: <Square size={13} />, action: 'stop', color: '#ef4444', bg: 'rgba(239,68,68,0.1)' },
          { icon: <RotateCcw size={13} />, action: 'restart', color: '#60a5fa', bg: 'rgba(96,165,250,0.1)' },
        ].map(({ icon, action, color, bg }) => (
          <button key={action} onClick={() => onAction(action)} disabled={loading}
            className="icon-btn" style={{ color, background: bg }} title={action}>
            {icon}
          </button>
        ))}

        <button onClick={onRefresh} className="icon-btn" style={{ color: '#94a3b8', background: '#1e1e3a' }} title="Refresh">
          <RefreshCw size={13} />
        </button>
      </div>
    </nav>
  )
}
