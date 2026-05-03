'use client'
import { LineChart, Line, XAxis, YAxis, Tooltip, ResponsiveContainer, BarChart, Bar } from 'recharts'

export function Metric({ label, value, sub, color, badge }: { label: string; value: string; sub?: string; color?: string; badge?: string }) {
  return (
    <div className="bg-gradient-to-br from-[#13132a] to-[#16162e] border border-[#2a2a4a] rounded-xl p-4 hover:border-[#4a4a8a] transition-colors">
      <div className="flex items-start justify-between mb-1">
        <div className="text-[10px] font-semibold text-[#6b7280] uppercase tracking-widest">{label}</div>
        {badge && <span className="text-[10px] px-1.5 py-0.5 rounded bg-green-500/20 text-green-400 font-semibold">{badge}</span>}
      </div>
      <div className={`text-2xl font-bold ${color || 'text-[#f1f5f9]'}`}>{value}</div>
      {sub && <div className="text-xs text-[#6b7280] mt-1">{sub}</div>}
    </div>
  )
}

export function PnLChart({ data }: { data: any[] }) {
  return (
    <ResponsiveContainer width="100%" height={220}>
      <LineChart data={data}>
        <XAxis dataKey="i" hide />
        <YAxis tick={{ fill: '#6b7280', fontSize: 11 }} tickFormatter={v => `$${v}`} />
        <Tooltip
          contentStyle={{ background: '#16162a', border: '1px solid #2a2a4a', borderRadius: 8, fontSize: 12 }}
          formatter={(v: any) => [`$${Number(v).toFixed(2)}`, 'Cumulative P&L']}
          labelFormatter={(i) => `Trade #${i}`}
        />
        <Line type="monotone" dataKey="pnl" stroke="#6366f1" strokeWidth={2} dot={false} />
      </LineChart>
    </ResponsiveContainer>
  )
}

export function CategoryChart({ data }: { data: Record<string, any> }) {
  const chartData = Object.entries(data).map(([cat, s]: any) => ({
    cat: cat.slice(0, 8), wins: s.w, losses: s.l,
    wr: s.w + s.l > 0 ? Math.round(s.w / (s.w + s.l) * 100) : 0
  }))
  return (
    <ResponsiveContainer width="100%" height={180}>
      <BarChart data={chartData}>
        <XAxis dataKey="cat" tick={{ fill: '#6b7280', fontSize: 10 }} />
        <YAxis tick={{ fill: '#6b7280', fontSize: 10 }} />
        <Tooltip contentStyle={{ background: '#16162a', border: '1px solid #2a2a4a', borderRadius: 8, fontSize: 12 }} />
        <Bar dataKey="wins" fill="#22c55e" radius={[3, 3, 0, 0]} name="Wins" />
        <Bar dataKey="losses" fill="#ef4444" radius={[3, 3, 0, 0]} name="Losses" />
      </BarChart>
    </ResponsiveContainer>
  )
}

export function Card({ title, children, className = '' }: { title?: string; children: React.ReactNode; className?: string }) {
  return (
    <div className={`bg-[#13132a] border border-[#2a2a4a] rounded-xl p-4 ${className}`}>
      {title && <h3 className="text-sm font-semibold text-[#e2e8f0] mb-3">{title}</h3>}
      {children}
    </div>
  )
}

export function Badge({ text, color }: { text: string; color: 'green' | 'red' | 'blue' | 'yellow' | 'purple' }) {
  const colors = {
    green: 'bg-green-500/20 text-green-400 border-green-500/30',
    red: 'bg-red-500/20 text-red-400 border-red-500/30',
    blue: 'bg-blue-500/20 text-blue-400 border-blue-500/30',
    yellow: 'bg-yellow-500/20 text-yellow-400 border-yellow-500/30',
    purple: 'bg-purple-500/20 text-purple-400 border-purple-500/30',
  }
  return <span className={`text-[10px] px-2 py-0.5 rounded-full border font-semibold ${colors[color]}`}>{text}</span>
}
