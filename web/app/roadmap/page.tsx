'use client'
import { ArrowLeft, CheckCircle2, Circle, Clock, Rocket, Users, Target, TrendingUp } from 'lucide-react'

type Status = 'done' | 'progress' | 'planned' | 'future'

const ROADMAP = [
  {
    phase: 'Phase 1 — Foundation',
    icon: <Target size={16} />,
    status: 'done' as Status,
    items: [
      { text: 'Core trading agent (Python + PM2)', status: 'done' as Status },
      { text: 'Polymarket CLOB integration', status: 'done' as Status },
      { text: 'Statistical edge model (Brier, calibration)', status: 'done' as Status },
      { text: 'Demo mode with real market prices', status: 'done' as Status },
      { text: 'AI analysis pipeline (LLM-powered)', status: 'done' as Status },
      { text: 'Exit strategy (TP, SL, trailing, time)', status: 'done' as Status },
      { text: 'Bankroll compounding system', status: 'done' as Status },
    ],
  },
  {
    phase: 'Phase 2 — Dashboard',
    icon: <TrendingUp size={16} />,
    status: 'done' as Status,
    items: [
      { text: 'Next.js dashboard with mobile-first design', status: 'done' as Status },
      { text: 'Real-time stats, P&L chart, trade history', status: 'done' as Status },
      { text: 'AI chat assistant with config suggestions', status: 'done' as Status },
      { text: 'Config editor with descriptions', status: 'done' as Status },
      { text: 'Proof of Edge page (Brier, calibration, audit)', status: 'done' as Status },
      { text: 'Onboarding guide (EN/ID)', status: 'done' as Status },
    ],
  },
  {
    phase: 'Phase 3 — Platform',
    icon: <Users size={16} />,
    status: 'progress' as Status,
    items: [
      { text: 'Email login + Polymarket account setup', status: 'progress' as Status },
      { text: 'Subscription plans (Free / Early Adopter / Pro)', status: 'progress' as Status },
      { text: 'Documentation site', status: 'progress' as Status },
      { text: 'Roadmap & progress tracking', status: 'progress' as Status },
      { text: 'Live mode with real execution', status: 'done' as Status },
      { text: 'Account sync (balance, positions, P&L)', status: 'done' as Status },
      { text: 'SAFE wallet (POLY_1271) integration', status: 'planned' as Status },
    ],
  },
  {
    phase: 'Phase 4 — Scale',
    icon: <Rocket size={16} />,
    status: 'future' as Status,
    items: [
      { text: 'Multi-strategy support (sports, crypto, geo separate)', status: 'future' as Status },
      { text: 'Portfolio-level risk management', status: 'future' as Status },
      { text: 'Telegram/Discord notifications', status: 'future' as Status },
      { text: 'API access for external integrations', status: 'future' as Status },
      { text: 'Backtesting framework', status: 'future' as Status },
      { text: 'Community strategy marketplace', status: 'future' as Status },
    ],
  },
]

const STATUS_ICONS: Record<Status, { icon: React.ReactNode; color: string; label: string }> = {
  done:     { icon: <CheckCircle2 size={14} />, color: 'var(--green)',   label: 'Done' },
  progress: { icon: <Clock size={14} />,        color: 'var(--yellow)', label: 'In Progress' },
  planned:  { icon: <Circle size={14} />,       color: 'var(--accent)', label: 'Planned' },
  future:   { icon: <Circle size={14} />,       color: 'var(--dim)',    label: 'Future' },
}

export default function RoadmapPage() {
  const doneCount = ROADMAP.flatMap(p => p.items).filter(i => i.status === 'done').length
  const totalCount = ROADMAP.flatMap(p => p.items).length

  return (
    <div className="min-h-screen p-4 pb-20" style={{ background: 'var(--bg)' }}>
      <div className="max-w-2xl mx-auto fade-in">
        {/* Header */}
        <div className="mb-6">
          <a href="/" className="flex items-center gap-1.5 text-xs mb-4" style={{ color: 'var(--dim)' }}>
            <ArrowLeft size={14} /> Back to Dashboard
          </a>
          <h1 className="text-lg font-bold mb-1" style={{ color: 'var(--text)' }}>Roadmap</h1>
          <p className="text-sm" style={{ color: 'var(--dim)' }}>
            What we&apos;ve built, what we&apos;re building, and what&apos;s next.
          </p>
        </div>

        {/* Progress bar */}
        <div className="section-card p-4 mb-6">
          <div className="flex justify-between items-center mb-2">
            <span className="text-xs font-semibold" style={{ color: 'var(--text2)' }}>Overall Progress</span>
            <span className="text-xs mono" style={{ color: 'var(--accent-light)' }}>{doneCount}/{totalCount}</span>
          </div>
          <div className="progress-bar">
            <div className="progress-fill" style={{ width: `${(doneCount / totalCount) * 100}%`, background: 'var(--accent)' }} />
          </div>
        </div>

        {/* Legend */}
        <div className="flex gap-4 mb-6 flex-wrap">
          {Object.entries(STATUS_ICONS).map(([key, { icon, color, label }]) => (
            <div key={key} className="flex items-center gap-1.5 text-xs" style={{ color }}>
              {icon} {label}
            </div>
          ))}
        </div>

        {/* Roadmap phases */}
        <div className="flex flex-col gap-6">
          {ROADMAP.map(phase => {
            const phaseStatus = STATUS_ICONS[phase.status]
            const doneInPhase = phase.items.filter(i => i.status === 'done').length
            return (
              <div key={phase.phase} className="section-card">
                <div className="p-4 pb-0">
                  <div className="flex items-center justify-between mb-1">
                    <div className="flex items-center gap-2">
                      <span style={{ color: phaseStatus.color }}>{phase.icon}</span>
                      <h2 className="text-sm font-bold" style={{ color: 'var(--text)' }}>{phase.phase}</h2>
                    </div>
                    <span className="badge" style={{
                      background: `${phaseStatus.color}15`, color: phaseStatus.color, borderColor: `${phaseStatus.color}30`,
                    }}>{doneInPhase}/{phase.items.length}</span>
                  </div>
                </div>
                <div className="p-4">
                  <div className="flex flex-col gap-0">
                    {phase.items.map(item => {
                      const s = STATUS_ICONS[item.status]
                      return (
                        <div key={item.text} className="flex items-center gap-2.5 py-2" style={{ borderBottom: '1px solid var(--border2)' }}>
                          <span style={{ color: s.color, flexShrink: 0 }}>{s.icon}</span>
                          <span className="text-xs" style={{
                            color: item.status === 'done' ? 'var(--muted)' : 'var(--text2)',
                            textDecoration: item.status === 'done' ? 'line-through' : 'none',
                          }}>{item.text}</span>
                        </div>
                      )
                    })}
                  </div>
                </div>
              </div>
            )
          })}
        </div>

        {/* CTA */}
        <div className="text-center mt-8 section-card p-6">
          <h3 className="text-sm font-bold mb-2" style={{ color: 'var(--text)' }}>Want early access?</h3>
          <p className="text-xs mb-4" style={{ color: 'var(--dim)' }}>
            50 early adopter spots available with 1 month free full access.
          </p>
          <a href="/subscribe" className="btn btn-primary">
            <Users size={14} /> Join Waitlist
          </a>
        </div>
      </div>
    </div>
  )
}
