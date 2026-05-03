'use client'
import { Card, Badge } from '@/components/ui'
import type { DashboardData } from '@/types'

export function Positions({ data }: { data: DashboardData }) {
  const { open_positions, stats } = data

  if (!open_positions?.length) return (
    <div className="text-center text-[#6b7280] py-20 text-sm">No open positions</div>
  )

  return (
    <div className="space-y-4">
      <div className="flex items-center gap-3">
        <h2 className="text-base font-semibold">Active Trades ({open_positions.length})</h2>
        <span className="text-xs text-[#6b7280]">${stats.deployed.toFixed(2)} in active trades</span>
      </div>
      {open_positions.map((t: any, i: number) => (
        <Card key={i} className={`border-l-4 ${t.side==='YES' ? 'border-l-green-500' : 'border-l-red-500'}`}>
          <div className="flex items-start justify-between mb-3">
            <div className="flex-1">
              <div className="flex items-center gap-2 mb-1">
                <Badge text={t.side} color={t.side==='YES'?'green':'red'} />
                <Badge text={t.category||'?'} color="purple" />
                {t.partial_exited && <Badge text="PARTIAL" color="yellow" />}
              </div>
              <div className="text-sm text-[#e2e8f0] font-medium">{t.market_question}</div>
            </div>
          </div>
          <div className="grid grid-cols-5 gap-3 text-xs">
            <div><div className="text-[#6b7280] mb-0.5">Entry Price</div><div className="font-mono text-[#e2e8f0]">{((t.price_at_entry||0)*100).toFixed(1)}%</div></div>
            <div><div className="text-[#6b7280] mb-0.5">Size</div><div className="font-mono text-[#e2e8f0]">${t.size_usd}</div></div>
            <div><div className="text-[#6b7280] mb-0.5">Peak P&L</div><div className="font-mono text-[#e2e8f0]">{t.peak_pnl_pct != null ? `${(t.peak_pnl_pct*100).toFixed(0)}%` : '—'}</div></div>
            <div><div className="text-[#6b7280] mb-0.5">Confidence</div><div className="font-mono text-[#e2e8f0]">{t.confidence_at_bet ? `${(t.confidence_at_bet*100).toFixed(0)}%` : '—'}</div></div>
            <div><div className="text-[#6b7280] mb-0.5">Category</div><div className="font-mono text-[#e2e8f0]">{t.category||'?'}</div></div>
          </div>
          {t.reasoning_summary && (
            <div className="mt-2 text-[10px] text-[#6b7280] bg-[#0d0d1a] rounded-lg p-2 leading-relaxed">
              💡 {t.reasoning_summary.slice(0, 150)}
            </div>
          )}
          {t.calibration_applied && (
            <div className="mt-1 text-[10px] text-[#4b5563]">⚙️ {t.calibration_applied.slice(0, 100)}</div>
          )}
        </Card>
      ))}
    </div>
  )
}
