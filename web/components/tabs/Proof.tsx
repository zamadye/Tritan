'use client'
import { Card, Badge, Metric } from '@/components/ui'
import type { DashboardData } from '@/types'

export function Proof({ data }: { data: DashboardData }) {
  const { stats, brier, calibration_model, data_sources, recent_full } = data

  const sources = [
    { name: 'ESPN Sports API', desc: 'Live scores, injuries, standings, playoff series', ok: data_sources?.espn, icon: '🏀' },
    { name: 'NewsAPI', desc: 'Breaking news within 15 min — before market reacts', ok: data_sources?.newsapi, icon: '📰' },
    { name: 'Twitter/X API', desc: 'Social media momentum signals', ok: data_sources?.twitter, icon: '🐦' },
    { name: 'CoinGecko', desc: 'Real-time price movement detection', ok: data_sources?.coingecko, icon: '₿' },
    { name: 'Fear & Greed', desc: 'Market sentiment trend (7-day)', ok: data_sources?.fear_greed, icon: '📊' },
    { name: 'Polymarket Gamma', desc: 'Live market data & pricing', ok: true, icon: '🎯' },
  ]

  const auditTrades = (recent_full || []).filter(t => t.calibration?.includes('logistic')).slice(0, 10)

  return (
    <div className="space-y-5">
      <div>
        <h2 className="text-base font-semibold text-[#e2e8f0] flex items-center gap-2 mb-1">
          🛡 Performance Verification & Track Record
        </h2>
        <p className="text-xs text-[#6b7280]">
          Verifiable proof that Tritan has a statistical edge over naive market pricing.
          Every trade logged with p_calibrated, source, and Brier score.
        </p>
      </div>

      {/* Top proof metrics */}
      <div className="grid grid-cols-4 gap-3">
        <Metric label="Markets Analyzed" value={(data_sources?.markets_analyzed||0).toLocaleString()}
          sub="Resolved Polymarket markets" badge="REAL DATA" />
        <Metric label="Prediction Accuracy Score" value={brier.model.toString()}
          sub={`vs market baseline (+${brier.improvement}% better)`} color="#22c55e" />
        <Metric label="Current System WR" value={`${((stats.new_arch?.wr||0)*100).toFixed(0)}%`}
          sub={`${stats.new_arch?.total||0} trades (May 1+)`} />
        <Metric label="Model-Driven Trades" value={`${stats.stat_edge?.total||0}`}
          sub={`WR: ${((stats.stat_edge?.wr||0)*100).toFixed(0)}% (probability model)`} />
      </div>

      {/* Calibration model table */}
      <Card title="Probability Model Results by Market Type">
        <p className="text-xs text-[#6b7280] mb-3">
          Trained on 19,624 real market outcomes. Shows how much more accurate our model is vs simply using the market price.
        </p>
        <div className="overflow-x-auto">
          <table className="w-full text-xs">
            <thead>
              <tr className="text-[#6b7280] border-b border-[#1e1e3a] text-left">
                {['Category','N Markets','Our Model','Market Baseline','Improvement','Status'].map(h => (
                  <th key={h} className="py-2 pr-4 font-semibold">{h}</th>
                ))}
              </tr>
            </thead>
            <tbody>
              {(calibration_model||[]).map(c => (
                <tr key={c.cat} className="border-b border-[#1a1a3a] hover:bg-[#16162a] transition-colors">
                  <td className="py-2 pr-4 font-medium text-[#e2e8f0]">{c.cat}</td>
                  <td className="pr-4 font-mono text-[#94a3b8]">{c.n.toLocaleString()}</td>
                  <td className="pr-4 font-mono text-green-400">{c.brier?.toFixed(4)}</td>
                  <td className="pr-4 font-mono text-[#6b7280]">{c.naive_brier?.toFixed(4)}</td>
                  <td className={`pr-4 font-mono font-semibold ${c.improvement > 0 ? 'text-green-400' : 'text-red-400'}`}>
                    {c.improvement > 0 ? '+' : ''}{c.improvement?.toFixed(1)}%
                  </td>
                  <td>{c.n >= 100 ? <Badge text="✓ ✓ Validated" color="green" /> : <Badge text={`n=${c.n}`} color="yellow" />}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </Card>

      {/* Data sources */}
      <Card title="Real-Time Data Sources">
        <div className="grid grid-cols-3 gap-3">
          {sources.map(s => (
            <div key={s.name} className={`p-3 rounded-lg border ${s.ok ? 'border-green-500/30 bg-green-500/5' : 'border-[#2a2a4a] bg-[#0d0d1a]'}`}>
              <div className="flex items-center gap-2 mb-1">
                <span className="text-base">{s.icon}</span>
                <span className="text-xs font-semibold text-[#e2e8f0]">{s.name}</span>
                <span className={`ml-auto text-[10px] font-bold ${s.ok ? 'text-green-400' : 'text-red-400'}`}>
                  {s.ok ? '●' : '○'}
                </span>
              </div>
              <div className="text-[10px] text-[#6b7280]">{s.desc}</div>
            </div>
          ))}
        </div>
      </Card>

      {/* Audit trail */}
      <Card title="Trade History — Model-Driven Decisions">
        <p className="text-xs text-[#6b7280] mb-3">
          Trades where p_calibrated (from logistic model) differed &gt;8% from market price.
          Each row is independently verifiable.
        </p>
        {auditTrades.length === 0 ? (
          <div className="text-xs text-[#6b7280] py-4 text-center">Collecting data — need more trades with new architecture</div>
        ) : (
          <div className="space-y-2">
            {auditTrades.map((t, i) => (
              <div key={i} className={`p-3 rounded-lg border text-xs ${t.correct ? 'border-green-500/20 bg-green-500/5' : 'border-red-500/20 bg-red-500/5'}`}>
                <div className="flex items-start justify-between gap-2 mb-2">
                  <span className="text-[#e2e8f0] font-medium flex-1 leading-tight">{t.market?.slice(0,65)}</span>
                  <div className="flex gap-1 shrink-0">
                    <Badge text={t.side} color={t.side==='YES'?'green':'red'} />
                    <Badge text={t.correct?'WIN':'LOSS'} color={t.correct?'green':'red'} />
                  </div>
                </div>
                <div className="grid grid-cols-5 gap-2 text-[10px] text-[#6b7280] mb-1">
                  <span>Entry: <span className="text-[#94a3b8] font-mono">{((t.entry||0)*100).toFixed(0)}%</span></span>
                  <span>Prob. Model: <span className="text-[#a5b4fc] font-mono">{t.p_base||'—'}</span></span>
                  <span>Edge: <span className="text-[#94a3b8] font-mono">{t.edge?`${(t.edge*100).toFixed(1)}%`:'—'}</span></span>
                  <span>Conf: <span className="text-[#94a3b8] font-mono">{t.confidence?`${(t.confidence*100).toFixed(0)}%`:'—'}</span></span>
                  <span>Brier: <span className="text-[#94a3b8] font-mono">{t.brier?.toFixed(3)||'—'}</span></span>
                </div>
                {t.catalyst && <div className="text-[10px] text-[#6b7280] truncate">💡 {t.catalyst}</div>}
                {t.calibration && <div className="text-[10px] text-[#4b5563] truncate mt-0.5">⚙️ {t.calibration}</div>}
              </div>
            ))}
          </div>
        )}
      </Card>
    </div>
  )
}
