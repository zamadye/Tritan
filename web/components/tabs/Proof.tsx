'use client'
import type { DashboardData } from '@/types'

function SCard({ title, sub, children }: { title?: string; sub?: string; children: React.ReactNode }) {
  return (
    <div style={{ background: '#13132a', border: '1px solid #2a2a4a', borderRadius: 16, overflow: 'hidden' }}>
      {(title || sub) && (
        <div style={{ padding: '14px 16px 0' }}>
          {title && <div style={{ fontSize: 13, fontWeight: 600, color: '#94a3b8' }}>{title}</div>}
          {sub && <div style={{ fontSize: 11, color: '#6b7280', marginTop: 3 }}>{sub}</div>}
        </div>
      )}
      <div style={{ padding: title || sub ? '12px 16px 16px' : '16px' }}>{children}</div>
    </div>
  )
}

export function Proof({ data }: { data: DashboardData }) {
  const { stats, brier, calibration_model, data_sources, recent_full } = data

  const sources = [
    { name: 'ESPN Sports', ok: data_sources?.espn, icon: '🏀' },
    { name: 'NewsAPI', ok: data_sources?.newsapi, icon: '📰' },
    { name: 'Twitter/X', ok: data_sources?.twitter, icon: '🐦' },
    { name: 'CoinGecko', ok: data_sources?.coingecko, icon: '₿' },
    { name: 'Fear & Greed', ok: data_sources?.fear_greed, icon: '📊' },
    { name: 'Polymarket', ok: true, icon: '🎯' },
  ]

  const auditTrades = (recent_full || []).filter(t => t.calibration?.includes('logistic')).slice(0, 8)

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: 14 }}>
      <div>
        <div style={{ fontSize: 15, fontWeight: 700, color: '#e2e8f0' }}>🛡 Proof of Edge</div>
        <div style={{ fontSize: 12, color: '#6b7280', marginTop: 3 }}>Verifiable statistical edge over market baseline</div>
      </div>

      {/* Model vs Market */}
      <div style={{ display: 'flex', gap: 10 }}>
        <div style={{ flex: 1, background: 'rgba(34,197,94,0.06)', border: '1px solid rgba(34,197,94,0.2)', borderRadius: 14, padding: '14px', textAlign: 'center' }}>
          <div style={{ fontSize: 10, color: '#6b7280', marginBottom: 6, textTransform: 'uppercase', letterSpacing: '0.6px' }}>Our Model</div>
          <div style={{ fontSize: 26, fontWeight: 700, color: '#22c55e' }}>{brier.model}</div>
          <div style={{ fontSize: 10, color: '#22c55e', marginTop: 4 }}>Brier Score ↓ better</div>
        </div>
        <div style={{ flex: 1, background: 'rgba(107,114,128,0.06)', border: '1px solid rgba(107,114,128,0.2)', borderRadius: 14, padding: '14px', textAlign: 'center' }}>
          <div style={{ fontSize: 10, color: '#6b7280', marginBottom: 6, textTransform: 'uppercase', letterSpacing: '0.6px' }}>Market</div>
          <div style={{ fontSize: 26, fontWeight: 700, color: '#6b7280' }}>{brier.naive}</div>
          <div style={{ fontSize: 10, color: '#6b7280', marginTop: 4 }}>Baseline</div>
        </div>
      </div>
      <div style={{ background: 'rgba(34,197,94,0.06)', border: '1px solid rgba(34,197,94,0.2)', borderRadius: 12, padding: '12px 16px', textAlign: 'center' }}>
        <span style={{ fontSize: 14, fontWeight: 700, color: '#22c55e' }}>+{brier.improvement}% more accurate than market</span>
        <div style={{ fontSize: 11, color: '#6b7280', marginTop: 3 }}>Trained on {(data_sources?.markets_analyzed || 0).toLocaleString()} resolved markets</div>
      </div>

      {/* Calibration model */}
      <SCard title="Model by Category" sub="Lower Brier = more accurate predictions">
        <div style={{ display: 'flex', flexDirection: 'column', gap: 8 }}>
          {(calibration_model || []).map(c => (
            <div key={c.cat} style={{ display: 'flex', alignItems: 'center', gap: 10, padding: '8px 0', borderBottom: '1px solid #1e1e3a' }}>
              <div style={{ flex: 1 }}>
                <div style={{ fontSize: 12, fontWeight: 600, color: '#e2e8f0', marginBottom: 2 }}>{c.cat}</div>
                <div style={{ fontSize: 10, color: '#6b7280' }}>n={c.n.toLocaleString()}</div>
              </div>
              <div style={{ textAlign: 'right' }}>
                <div style={{ fontSize: 12, fontFamily: 'ui-monospace,monospace', color: '#22c55e' }}>{c.brier?.toFixed(4)}</div>
                <div style={{ fontSize: 10, color: c.improvement > 0 ? '#22c55e' : '#ef4444', fontWeight: 600 }}>
                  {c.improvement > 0 ? '+' : ''}{c.improvement?.toFixed(1)}%
                </div>
              </div>
            </div>
          ))}
        </div>
      </SCard>

      {/* Data sources */}
      <SCard title="Live Data Sources">
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: 8 }}>
          {sources.map(s => (
            <div key={s.name} style={{
              padding: '10px 8px', borderRadius: 12, textAlign: 'center',
              background: s.ok ? 'rgba(34,197,94,0.06)' : 'rgba(107,114,128,0.06)',
              border: `1px solid ${s.ok ? 'rgba(34,197,94,0.2)' : 'rgba(107,114,128,0.15)'}`,
            }}>
              <div style={{ fontSize: 18, marginBottom: 4 }}>{s.icon}</div>
              <div style={{ fontSize: 10, fontWeight: 600, color: s.ok ? '#e2e8f0' : '#6b7280' }}>{s.name}</div>
              <div style={{ fontSize: 10, color: s.ok ? '#22c55e' : '#6b7280', marginTop: 2 }}>{s.ok ? '● Active' : '○ Off'}</div>
            </div>
          ))}
        </div>
      </SCard>

      {/* Audit trail */}
      <SCard title="Trade Audit Trail" sub="Model-driven decisions — independently verifiable">
        {auditTrades.length === 0 ? (
          <div style={{ fontSize: 12, color: '#6b7280', textAlign: 'center', padding: '16px 0' }}>Collecting data...</div>
        ) : (
          <div style={{ display: 'flex', flexDirection: 'column', gap: 8 }}>
            {auditTrades.map((t, i) => (
              <div key={i} style={{
                padding: '10px 12px', borderRadius: 12,
                background: '#0d0d1a',
                border: `1px solid ${t.correct ? 'rgba(34,197,94,0.2)' : 'rgba(239,68,68,0.2)'}`,
              }}>
                <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: 6, gap: 8 }}>
                  <div style={{ fontSize: 12, fontWeight: 600, color: '#e2e8f0', flex: 1, lineHeight: 1.4 }}>
                    {t.market?.slice(0, 55)}{(t.market?.length || 0) > 55 ? '…' : ''}
                  </div>
                  <div style={{ display: 'flex', gap: 4, flexShrink: 0 }}>
                    <span style={{ fontSize: 10, fontWeight: 700, padding: '2px 7px', borderRadius: 20, background: t.side === 'YES' ? 'rgba(34,197,94,0.15)' : 'rgba(239,68,68,0.15)', color: t.side === 'YES' ? '#22c55e' : '#ef4444', border: `1px solid ${t.side === 'YES' ? 'rgba(34,197,94,0.3)' : 'rgba(239,68,68,0.3)'}` }}>{t.side}</span>
                    <span style={{ fontSize: 10, fontWeight: 700, padding: '2px 7px', borderRadius: 20, background: t.correct ? 'rgba(34,197,94,0.15)' : 'rgba(239,68,68,0.15)', color: t.correct ? '#22c55e' : '#ef4444', border: `1px solid ${t.correct ? 'rgba(34,197,94,0.3)' : 'rgba(239,68,68,0.3)'}` }}>{t.correct ? 'WIN' : 'LOSS'}</span>
                  </div>
                </div>
                <div style={{ display: 'flex', gap: 12, fontSize: 10, color: '#6b7280', flexWrap: 'wrap' }}>
                  <span>Entry <span style={{ color: '#94a3b8', fontFamily: 'ui-monospace,monospace' }}>{((t.entry || 0) * 100).toFixed(0)}%</span></span>
                  <span>Model <span style={{ color: '#a5b4fc', fontFamily: 'ui-monospace,monospace' }}>{t.p_base || '—'}</span></span>
                  <span>Edge <span style={{ color: '#94a3b8', fontFamily: 'ui-monospace,monospace' }}>{t.edge ? `${(t.edge * 100).toFixed(1)}%` : '—'}</span></span>
                  <span>Brier <span style={{ color: '#94a3b8', fontFamily: 'ui-monospace,monospace' }}>{t.brier?.toFixed(3) || '—'}</span></span>
                  <span style={{ color: (t.pnl || 0) >= 0 ? '#22c55e' : '#ef4444', fontFamily: 'ui-monospace,monospace', fontWeight: 600 }}>
                    {(t.pnl || 0) >= 0 ? '+' : ''}${(t.pnl || 0).toFixed(2)}
                  </span>
                </div>
              </div>
            ))}
          </div>
        )}
      </SCard>
    </div>
  )
}
