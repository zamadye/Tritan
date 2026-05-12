'use client'
import { EmptyState } from '@/components/ui'
import type { DashboardData } from '@/types'

export function Positions({ data }: { data: DashboardData }) {
  const { open_positions, stats } = data

  if (!open_positions?.length) return (
    <div className="fade-in">
      <div className="section-card">
        <div className="section-card-header">
          <div className="text-[13px] font-semibold" style={{ color: 'var(--muted)' }}>Open Positions</div>
          <div className="text-[11px]" style={{ color: 'var(--dim)' }}>
            {data.agent_mode === 'live' ? '💰 Live' : '📝 Demo'} · ${stats.deployed?.toFixed(2) || '0.00'} deployed
          </div>
        </div>
        <div className="section-card-body">
          <EmptyState icon="📭" title="No open positions" desc="Agent is scanning for opportunities" />
        </div>
      </div>
    </div>
  )

  return (
    <div className="flex flex-col gap-3 fade-in">
      {/* Header */}
      <div className="section-card">
        <div className="section-card-header">
          <div className="flex items-center justify-between">
            <div>
              <div className="text-[13px] font-semibold" style={{ color: 'var(--muted)' }}>Open Positions</div>
              <div className="text-[11px] mt-0.5" style={{ color: 'var(--dim)' }}>
                {open_positions.length} active · ${stats.deployed?.toFixed(2) || '0.00'} deployed
              </div>
            </div>
            <span className="status-pill" style={{
              borderColor: data.agent_mode === 'live' ? 'var(--green-border)' : 'var(--accent-border)',
              color: data.agent_mode === 'live' ? 'var(--green)' : 'var(--accent-light)',
              background: data.agent_mode === 'live' ? 'var(--green-bg)' : 'var(--accent-bg)',
              fontSize: 10,
              padding: '3px 8px',
            }}>
              {data.agent_mode === 'live' ? '💰 LIVE' : '📝 DEMO'}
            </span>
          </div>
        </div>
      </div>

      {/* Position Cards */}
      {open_positions.map((t: any) => {
        const isYes = t.side === 'YES'
        const accentColor = isYes ? 'var(--green)' : 'var(--red)'

        return (
          <div key={t.trade_id || t.market_id || t.market_question} className="section-card" style={{ borderLeft: `3px solid ${accentColor}` }}>
            <div className="section-card-body">
              {/* Market Question */}
              <div className="text-[13px] font-semibold leading-snug mb-2" style={{ color: 'var(--text2)' }}>
                {t.market_question?.slice(0, 70)}{t.market_question?.length > 70 ? '…' : ''}
              </div>

              {/* Badges */}
              <div className="flex gap-1.5 mb-3 flex-wrap">
                <span className="badge" style={{
                  background: isYes ? 'var(--green-bg)' : 'var(--red-bg)',
                  color: accentColor,
                  borderColor: isYes ? 'var(--green-border)' : 'var(--red-border)',
                }}>{t.side}</span>
                <span className="badge" style={{
                  background: 'var(--accent-bg)', color: 'var(--accent-light)', borderColor: 'var(--accent-border)',
                }}>{t.category || 'other'}</span>
              </div>

              {/* Stats Grid */}
              <div className="grid grid-cols-4 gap-px" style={{ background: 'var(--border2)' }}>
                {[
                  { label: 'Size', value: `$${t.size_usd}` },
                  { label: 'Entry', value: `${((t.price_at_entry || 0) * 100).toFixed(0)}%` },
                  { label: 'Current', value: t.current_yes_price != null ? `${(t.side === 'YES' ? t.current_yes_price : 1 - t.current_yes_price) * 100 | 0}%` : '—' },
                  { label: 'Opened', value: (() => { try { const d = new Date(t.timestamp); const h = Math.floor((Date.now()-d.getTime())/3600000); return h < 1 ? `${Math.floor((Date.now()-d.getTime())/60000)}m ago` : h < 24 ? `${h}h ago` : d.toLocaleDateString('en',{month:'short',day:'numeric'}); } catch { return '—'; } })() },
                ].map((s, j) => (
                  <div key={j} className="text-center py-2.5 px-3" style={{ background: 'var(--bg2)' }}>
                    <div className="text-[10px] mb-0.5" style={{ color: 'var(--dim)' }}>{s.label}</div>
                    <div className="text-sm font-semibold mono" style={{ color: 'var(--text2)' }}>{s.value}</div>
                  </div>
                ))}
              </div>

              {/* Unrealized P&L — like Polymarket UI */}
              {t.unrealized_pnl != null && (
                <div className="flex items-center justify-between mt-2.5 px-1">
                  <span className="text-[11px]" style={{ color: 'var(--dim)' }}>Unrealized P&L</span>
                  <div className="flex items-center gap-2">
                    <span className="text-sm font-bold mono" style={{ color: t.unrealized_pnl >= 0 ? 'var(--green)' : 'var(--red)' }}>
                      {t.unrealized_pnl >= 0 ? '+' : ''}${t.unrealized_pnl.toFixed(2)}
                    </span>
                    <span className="text-[11px] font-semibold" style={{ color: t.unrealized_pnl >= 0 ? 'var(--green)' : 'var(--red)' }}>
                      ({t.unrealized_pct >= 0 ? '+' : ''}{t.unrealized_pct?.toFixed(1)}%)
                    </span>
                  </div>
                </div>
              )}

              {/* Reasoning */}
              {t.reasoning_summary && (
                <div className="mt-2.5 text-xs leading-relaxed" style={{ color: 'var(--dim)' }}>
                  💡 {t.reasoning_summary.slice(0, 120)}…
                </div>
              )}
            </div>
          </div>
        )
      })}
    </div>
  )
}
