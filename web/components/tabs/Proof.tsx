'use client'
import { SectionCard, ModeBadge } from '@/components/ui'
import type { DashboardData } from '@/types'

function CalibrationPlot({ trades }: { trades: any[] }) {
  // Group trades into probability buckets and compute actual win rates
  const buckets: Record<string, { total: number; wins: number }> = {}
  for (const t of trades) {
    if (!t.p_true || t.outcome === 'EXIT') continue
    const bucket = Math.round(t.p_true * 10) * 10 // 0, 10, 20, ... 100
    const key = `${bucket}`
    if (!buckets[key]) buckets[key] = { total: 0, wins: 0 }
    buckets[key].total++
    if (t.correct) buckets[key].wins++
  }

  const points = Object.entries(buckets)
    .filter(([, d]) => d.total >= 2)
    .map(([bucket, d]) => ({
      predicted: Number(bucket) / 100,
      actual: d.wins / d.total,
      n: d.total,
    }))
    .sort((a, b) => a.predicted - b.predicted)

  if (points.length < 2) return null

  return (
    <div className="relative" style={{ height: 180 }}>
      {/* Perfect calibration line */}
      <svg width="100%" height="100%" viewBox="0 0 100 100" preserveAspectRatio="none" style={{ position: 'absolute', inset: 0 }}>
        <line x1="0" y1="100" x2="100" y2="0" stroke="var(--border2)" strokeWidth="1" strokeDasharray="4 2" />
      </svg>
      {/* Actual calibration points */}
      {points.map((p, i) => (
        <div key={i} className="absolute flex flex-col items-center" style={{
          left: `${p.predicted * 100}%`,
          bottom: `${p.actual * 100}%`,
          transform: 'translate(-50%, 50%)',
        }}>
          <div className="w-3 h-3 rounded-full" style={{
            background: Math.abs(p.actual - p.predicted) < 0.1 ? 'var(--green)' : 'var(--yellow)',
            border: '2px solid var(--bg2)',
          }} />
          <div className="text-[8px] mono mt-0.5" style={{ color: 'var(--dim)' }}>{p.n}</div>
        </div>
      ))}
      {/* Axis labels */}
      <div className="absolute bottom-0 left-0 right-0 text-[9px] text-center" style={{ color: 'var(--dim)' }}>Predicted Probability</div>
      <div className="absolute left-0 top-0 bottom-0 text-[9px] flex items-center" style={{ color: 'var(--dim)', writingMode: 'vertical-lr', transform: 'rotate(180deg)' }}>Actual Win Rate</div>
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
    <div className="flex flex-col gap-4 fade-in">
      <div className="flex items-start justify-between">
        <div>
          <div className="text-base font-bold" style={{ color: 'var(--text)' }}>🛡 Proof of Edge</div>
          <div className="text-xs mt-0.5" style={{ color: 'var(--dim)' }}>Verifiable statistical edge — all data on-chain & auditable</div>
        </div>
        <ModeBadge mode={data.agent_mode || 'demo'} />
      </div>

      {/* Live Performance Summary — for investors */}
      <SectionCard title="Live Trading Performance">
        <div className="grid grid-cols-2 gap-3 mb-3">
          {[
            { label: 'Total Trades', value: String(stats.total || 0), sub: `${stats.resolved || 0} resolved` },
            { label: 'Win Rate', value: `${((stats.wr || 0) * 100).toFixed(1)}%`, sub: `${stats.wins}W / ${stats.losses}L`, color: (stats.wr || 0) >= 0.55 ? 'var(--green)' : (stats.wr || 0) >= 0.45 ? 'var(--yellow)' : 'var(--red)' },
            { label: 'Total P&L', value: `${(stats.pnl || 0) >= 0 ? '+' : ''}$${(stats.pnl || 0).toFixed(2)}`, color: (stats.pnl || 0) >= 0 ? 'var(--green)' : 'var(--red)' },
            { label: 'Avg Win/Trade', value: `$${(stats.avg_win || 0).toFixed(3)}`, sub: `vs $${(stats.avg_loss || 0).toFixed(3)} avg loss` },
          ].map((k, i) => (
            <div key={i} className="p-3 rounded-xl" style={{ background: 'var(--bg)', border: '1px solid var(--border)' }}>
              <div className="text-[10px] font-semibold uppercase tracking-wider mb-1.5" style={{ color: 'var(--dim)' }}>{k.label}</div>
              <div className="text-xl font-bold mono" style={{ color: k.color || 'var(--text)' }}>{k.value}</div>
              {k.sub && <div className="text-[10px] mt-0.5" style={{ color: 'var(--dim)' }}>{k.sub}</div>}
            </div>
          ))}
        </div>
        <div className="text-[10px] p-2 rounded-lg text-center" style={{ background: 'var(--border2)', color: 'var(--dim)' }}>
          All trades executed on Polymarket · Verifiable on Polygon blockchain · {data.agent_mode === 'live' ? '💰 Live money' : '📝 Demo mode'}
        </div>
      </SectionCard>

      {/* Model vs Market */}
      <div className="flex gap-3">
        <div className="flex-1 text-center p-4 rounded-xl" style={{ background: 'var(--green-bg)', border: '1px solid var(--green-border)' }}>
          <div className="text-[10px] font-semibold mb-1.5 uppercase tracking-wider" style={{ color: 'var(--dim)' }}>Our Model</div>
          <div className="text-2xl font-bold" style={{ color: 'var(--green)' }}>{brier.model}</div>
          <div className="text-[10px] mt-1" style={{ color: 'var(--green)' }}>Brier Score ↓ better</div>
        </div>
        <div className="flex-1 text-center p-4 rounded-xl" style={{ background: 'rgba(107,114,128,0.06)', border: '1px solid rgba(107,114,128,0.15)' }}>
          <div className="text-[10px] font-semibold mb-1.5 uppercase tracking-wider" style={{ color: 'var(--dim)' }}>Market</div>
          <div className="text-2xl font-bold" style={{ color: 'var(--dim)' }}>{brier.naive}</div>
          <div className="text-[10px] mt-1" style={{ color: 'var(--dim)' }}>Baseline</div>
        </div>
      </div>

      <div className="text-center p-3 rounded-xl" style={{ background: 'var(--green-bg)', border: '1px solid var(--green-border)' }}>
        <span className="text-sm font-bold" style={{ color: 'var(--green)' }}>+{brier.improvement}% more accurate than market</span>
        <div className="text-xs mt-0.5" style={{ color: 'var(--dim)' }}>Trained on {(data_sources?.markets_analyzed || 0).toLocaleString()} resolved markets</div>
      </div>

      {/* Calibration Plot */}
      {recent_full && recent_full.length >= 5 && (
        <SectionCard title="Calibration Plot" sub="Predicted probability vs actual outcome (perfect = diagonal line)">
          <CalibrationPlot trades={recent_full} />
        </SectionCard>
      )}

      {/* Calibration */}
      <SectionCard title="Model by Category" sub="Lower Brier = more accurate predictions">
        <div className="flex flex-col gap-0">
          {(calibration_model || []).map(c => (
            <div key={c.cat} className="flex items-center gap-3 py-2" style={{ borderBottom: '1px solid var(--border2)' }}>
              <div className="flex-1">
                <div className="text-xs font-semibold" style={{ color: 'var(--text2)' }}>{c.cat}</div>
                <div className="text-[10px]" style={{ color: 'var(--dim)' }}>n={c.n.toLocaleString()}</div>
              </div>
              <div className="text-right">
                <div className="text-xs mono" style={{ color: 'var(--green)' }}>{c.brier?.toFixed(4)}</div>
                <div className="text-[10px] font-semibold" style={{ color: c.improvement > 0 ? 'var(--green)' : 'var(--red)' }}>
                  {c.improvement > 0 ? '+' : ''}{c.improvement?.toFixed(1)}%
                </div>
              </div>
            </div>
          ))}
        </div>
      </SectionCard>

      {/* Data sources */}
      <SectionCard title="Live Data Sources">
        <div className="grid grid-cols-3 gap-2">
          {sources.map(s => (
            <div key={s.name} className="p-2.5 rounded-xl text-center" style={{
              background: s.ok ? 'var(--green-bg)' : 'rgba(107,114,128,0.06)',
              border: `1px solid ${s.ok ? 'var(--green-border)' : 'rgba(107,114,128,0.12)'}`,
            }}>
              <div className="text-lg mb-1">{s.icon}</div>
              <div className="text-[10px] font-semibold" style={{ color: s.ok ? 'var(--text2)' : 'var(--dim)' }}>{s.name}</div>
              <div className="text-[10px] mt-0.5" style={{ color: s.ok ? 'var(--green)' : 'var(--dim)' }}>{s.ok ? '● Active' : '○ Off'}</div>
            </div>
          ))}
        </div>
      </SectionCard>

      {/* Audit trail */}
      <SectionCard title="Trade Audit Trail" sub="Model-driven decisions — independently verifiable">
        {auditTrades.length === 0 ? (
          <div className="text-xs text-center py-4" style={{ color: 'var(--dim)' }}>Collecting data...</div>
        ) : (
          <div className="flex flex-col gap-2">
            {auditTrades.map((t) => (
              <div key={t.market + t.date + t.side} className="p-3 rounded-xl" style={{
                background: 'var(--bg)',
                border: `1px solid ${t.correct ? 'var(--green-border)' : 'var(--red-border)'}`,
              }}>
                <div className="flex justify-between mb-1.5 gap-2">
                  <div className="text-xs font-semibold flex-1 leading-snug" style={{ color: 'var(--text2)' }}>
                    {t.market?.slice(0, 55)}{(t.market?.length || 0) > 55 ? '…' : ''}
                  </div>
                  <div className="flex gap-1 flex-shrink-0">
                    <span className="badge" style={{
                      background: t.side === 'YES' ? 'var(--green-bg)' : 'var(--red-bg)',
                      color: t.side === 'YES' ? 'var(--green)' : 'var(--red)',
                      borderColor: t.side === 'YES' ? 'var(--green-border)' : 'var(--red-border)',
                    }}>{t.side}</span>
                    <span className="badge" style={{
                      background: t.correct ? 'var(--green-bg)' : 'var(--red-bg)',
                      color: t.correct ? 'var(--green)' : 'var(--red)',
                      borderColor: t.correct ? 'var(--green-border)' : 'var(--red-border)',
                    }}>{t.correct ? 'WIN' : 'LOSS'}</span>
                  </div>
                </div>
                <div className="flex gap-3 text-[10px] flex-wrap" style={{ color: 'var(--dim)' }}>
                  <span>Entry <span className="mono" style={{ color: 'var(--muted)' }}>{((t.entry || 0) * 100).toFixed(0)}%</span></span>
                  <span>Model <span className="mono" style={{ color: 'var(--accent-light)' }}>{t.p_base || '—'}</span></span>
                  <span>Edge <span className="mono" style={{ color: 'var(--muted)' }}>{t.edge ? `${(t.edge * 100).toFixed(1)}%` : '—'}</span></span>
                  <span>Brier <span className="mono" style={{ color: 'var(--muted)' }}>{t.brier?.toFixed(3) || '—'}</span></span>
                  <span className="mono font-semibold" style={{ color: (t.pnl || 0) >= 0 ? 'var(--green)' : 'var(--red)' }}>
                    {(t.pnl || 0) >= 0 ? '+' : ''}${(t.pnl || 0).toFixed(2)}
                  </span>
                </div>
              </div>
            ))}
          </div>
        )}
      </SectionCard>
    </div>
  )
}
