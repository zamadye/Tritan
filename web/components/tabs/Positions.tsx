'use client'
import type { DashboardData } from '@/types'

export function Positions({ data }: { data: DashboardData }) {
  const { open_positions, stats } = data

  if (!open_positions?.length) return (
    <div style={{ textAlign: 'center', padding: '60px 20px', color: '#6b7280' }}>
      <div style={{ fontSize: 40, marginBottom: 12 }}>📭</div>
      <div style={{ fontSize: 14, fontWeight: 600, color: '#94a3b8' }}>No open positions</div>
      <div style={{ fontSize: 12, marginTop: 4 }}>Agent is scanning for opportunities</div>
    </div>
  )

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: 12 }}>
      {/* Header */}
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
        <div>
          <div style={{ fontSize: 15, fontWeight: 700, color: '#e2e8f0' }}>Active Trades</div>
          <div style={{ fontSize: 11, color: '#6b7280', marginTop: 2 }}>{open_positions.length} open · ${stats.deployed.toFixed(2)} deployed</div>
        </div>
      </div>

      {open_positions.map((t: any, i: number) => {
        const isYes = t.side === 'YES'
        const accentColor = isYes ? '#22c55e' : '#ef4444'
        const accentBg = isYes ? 'rgba(34,197,94,0.06)' : 'rgba(239,68,68,0.06)'
        const accentBorder = isYes ? 'rgba(34,197,94,0.2)' : 'rgba(239,68,68,0.2)'

        return (
          <div key={i} style={{
            background: '#13132a',
            border: `1px solid #2a2a4a`,
            borderLeft: `3px solid ${accentColor}`,
            borderRadius: 16,
            overflow: 'hidden',
          }}>
            {/* Top row */}
            <div style={{ padding: '14px 16px 10px', display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', gap: 12 }}>
              <div style={{ flex: 1, minWidth: 0 }}>
                <div style={{ display: 'flex', gap: 6, marginBottom: 6, flexWrap: 'wrap' }}>
                  <span style={{ fontSize: 10, fontWeight: 700, padding: '2px 8px', borderRadius: 20, background: accentBg, color: accentColor, border: `1px solid ${accentBorder}` }}>
                    {t.side}
                  </span>
                  <span style={{ fontSize: 10, fontWeight: 600, padding: '2px 8px', borderRadius: 20, background: 'rgba(165,180,252,0.1)', color: '#a5b4fc', border: '1px solid rgba(165,180,252,0.2)' }}>
                    {t.category || 'other'}
                  </span>
                </div>
                <div style={{ fontSize: 13, fontWeight: 600, color: '#e2e8f0', lineHeight: 1.4 }}>
                  {t.market_question?.slice(0, 70)}{t.market_question?.length > 70 ? '…' : ''}
                </div>
              </div>
              <div style={{ textAlign: 'right', flexShrink: 0 }}>
                <div style={{ fontSize: 11, color: '#6b7280' }}>Size</div>
                <div style={{ fontSize: 16, fontWeight: 700, color: '#e2e8f0' }}>${t.size_usd}</div>
              </div>
            </div>

            {/* Stats row */}
            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: 1, background: '#1e1e3a' }}>
              {[
                { label: 'Entry', value: `${((t.price_at_entry || 0) * 100).toFixed(0)}%` },
                { label: 'Confidence', value: t.confidence_at_bet ? `${(t.confidence_at_bet * 100).toFixed(0)}%` : '—' },
                { label: 'Peak P&L', value: t.peak_pnl_pct != null ? `${(t.peak_pnl_pct * 100).toFixed(0)}%` : '—', color: t.peak_pnl_pct > 0 ? '#22c55e' : undefined },
              ].map((s, j) => (
                <div key={j} style={{ background: '#13132a', padding: '10px 12px', textAlign: 'center' }}>
                  <div style={{ fontSize: 10, color: '#6b7280', marginBottom: 3 }}>{s.label}</div>
                  <div style={{ fontSize: 13, fontWeight: 600, color: s.color || '#e2e8f0', fontFamily: 'ui-monospace, monospace' }}>{s.value}</div>
                </div>
              ))}
            </div>

            {/* Reasoning */}
            {t.reasoning_summary && (
              <div style={{ padding: '10px 16px', fontSize: 11, color: '#6b7280', lineHeight: 1.5, borderTop: '1px solid #1e1e3a' }}>
                💡 {t.reasoning_summary.slice(0, 120)}…
              </div>
            )}
          </div>
        )
      })}
    </div>
  )
}
