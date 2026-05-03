'use client'
import { useState, useEffect } from 'react'
import { Card, Metric } from '@/components/ui'
import { ExitChart } from '@/components/charts'
import type { DashboardData } from '@/types'

export function Learning({ data }: { data: DashboardData }) {
  const { evolution, brier, exit_breakdown, stats } = data
  return (
    <div className="space-y-5">
      <div>
        <h2 className="text-base font-semibold text-[#e2e8f0] mb-1">🧠 Evolution Learning</h2>
        <p className="text-xs text-[#6b7280]">Agent learns from every resolved trade. Lessons injected into LLM each cycle.</p>
      </div>
      <div className="grid grid-cols-4 gap-3">
        <Metric label="Resolved Trades" value={String(evolution?.total_resolved||0)} />
        <Metric label="Overall WR" value={`${((evolution?.overall_win_rate||0)*100).toFixed(0)}%`} />
        <Metric label="Model Improvement" value={`+${brier.improvement}%`} color="#22c55e" sub="vs naive baseline" />
        <Metric label="New Arch WR" value={`${((stats.new_arch?.wr||0)*100).toFixed(0)}%`} sub={`${stats.new_arch?.total||0} trades (May1+)`} color={stats.new_arch?.wr >= 0.54 ? '#22c55e' : '#f59e0b'} />
      </div>
      <div className="grid grid-cols-2 gap-5">
        <Card title="Exit Breakdown"><ExitChart data={exit_breakdown||{}} /></Card>
        <Card title="Entry Price → Win Rate">
          <div className="space-y-2">
            {Object.entries(evolution?.price_movement_patterns||{}).map(([b, d]: any) => (
              <div key={b} className="flex items-center gap-3 text-xs">
                <span className="text-[#94a3b8] w-20">{b}</span>
                <div className="flex-1 h-2 bg-[#1e1e3a] rounded-full">
                  <div className="h-full rounded-full bg-[#6366f1]" style={{ width: `${(d.win_rate||0)*100}%` }} />
                </div>
                <span className="text-[#94a3b8] w-12 text-right">WR {((d.win_rate||0)*100).toFixed(0)}%</span>
                <span className={`w-14 text-right font-mono text-xs ${(d.avg_pnl||0)>=0?'text-green-400':'text-red-400'}`}>${(d.avg_pnl||0)>=0?'+':''}{(d.avg_pnl||0).toFixed(2)}</span>
                <span className="text-[#4b5563] w-8 text-right">n={d.n}</span>
              </div>
            ))}
          </div>
        </Card>
      </div>
      <div className="grid grid-cols-2 gap-5">
        <Card title="What Worked">
          {!(evolution?.momentum_lessons?.length) ? <div className="text-xs text-[#6b7280]">Collecting data...</div> : (
            <div className="space-y-2">
              {(evolution.momentum_lessons||[]).map((m: any, i: number) => (
                <div key={i} className="p-2 bg-[#0d0d1a] rounded-lg border border-green-500/20">
                  <div className="flex gap-2 text-xs mb-1">
                    <span className="text-green-400 font-semibold">${(m.pnl||0).toFixed(2)}</span>
                    <span className="text-[#6b7280]">{m.exit_reason}</span>
                    <span className="text-[#4b5563]">[{m.category}]</span>
                  </div>
                  <div className="text-[10px] text-[#6b7280]">{m.catalyst?.slice(0,100)}</div>
                </div>
              ))}
            </div>
          )}
        </Card>
        <Card title="Recent Losses">
          {!(evolution?.recent_mistakes?.length) ? <div className="text-xs text-[#6b7280]">No mistakes yet</div> : (
            <div className="space-y-2">
              {(evolution.recent_mistakes||[]).map((m: any, i: number) => (
                <div key={i} className="p-2 bg-[#0d0d1a] rounded-lg border border-red-500/20">
                  <div className="text-xs text-[#94a3b8] truncate mb-1">{m.question?.slice(0,55)}</div>
                  <div className="text-[10px] text-red-400">{m.lesson?.slice(0,100)}</div>
                </div>
              ))}
            </div>
          )}
        </Card>
      </div>
    </div>
  )
}
