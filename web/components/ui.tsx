'use client'

/* ═══════════════════════════════════════════════════════
   TRITAN Shared Component Library
   All visual components use CSS variables from globals.css
   ═══════════════════════════════════════════════════════ */

// ── Metric Card ────────────────────────────────────
export function Metric({ label, value, sub, color, badge, trend }: {
  label: string; value: string; sub?: string; color?: string; badge?: string; trend?: 'up' | 'down' | 'neutral'
}) {
  const trendIcon = trend === 'up' ? '↑' : trend === 'down' ? '↓' : ''
  return (
    <div className="metric-card">
      <div className="flex items-start justify-between mb-2">
        <div className="metric-label">{label}</div>
        {badge && <span className="badge" style={{
          background: 'var(--green-bg)', color: 'var(--green)', borderColor: 'var(--green-border)', fontSize: 10,
        }}>{badge}</span>}
      </div>
      <div className="metric-value" style={{ color: color || 'var(--text)' }}>
        {trendIcon && <span style={{ fontSize: '0.7em', marginRight: 4 }}>{trendIcon}</span>}
        {value}
      </div>
      {sub && <div className="metric-sub">{sub}</div>}
    </div>
  )
}

// ── Card ───────────────────────────────────────────
export function Card({ title, icon, children, className = '', onClick }: {
  title?: string; icon?: React.ReactNode; children: React.ReactNode; className?: string; onClick?: () => void
}) {
  return (
    <div className={`card ${className}`} onClick={onClick} style={onClick ? { cursor: 'pointer' } : undefined}>
      {title && <div className="card-title">{icon}{title}</div>}
      {children}
    </div>
  )
}

// ── Section Card ───────────────────────────────────
export function SectionCard({ title, sub, action, children }: {
  title?: string; sub?: string; action?: React.ReactNode; children: React.ReactNode
}) {
  return (
    <div className="section-card fade-in">
      {(title || sub || action) && (
        <div className="section-card-header">
          <div className="flex items-center justify-between">
            <div>
              {title && <div className="text-[13px] font-semibold text-[var(--muted)]">{title}</div>}
              {sub && <div className="text-[11px] text-[var(--dim)] mt-0.5">{sub}</div>}
            </div>
            {action}
          </div>
        </div>
      )}
      <div className={title || sub || action ? 'section-card-body' : 'p-4'}>
        {children}
      </div>
    </div>
  )
}

// ── Badge ──────────────────────────────────────────
const BADGE_STYLES: Record<string, { bg: string; color: string; border: string }> = {
  green:  { bg: 'var(--green-bg)',  color: 'var(--green)',  border: 'var(--green-border)' },
  red:    { bg: 'var(--red-bg)',    color: 'var(--red)',    border: 'var(--red-border)' },
  blue:   { bg: 'var(--accent-bg)', color: 'var(--accent)', border: 'var(--accent-border)' },
  yellow: { bg: 'var(--yellow-bg)', color: 'var(--yellow)', border: 'var(--yellow-border)' },
  gray:   { bg: 'rgba(107,114,128,0.08)', color: 'var(--muted)', border: 'rgba(107,114,128,0.2)' },
}

export function Badge({ text, color = 'gray' }: {
  text: string; color?: 'green' | 'red' | 'blue' | 'yellow' | 'gray'
}) {
  const s = BADGE_STYLES[color] || BADGE_STYLES.gray
  return (
    <span className="badge" style={{ background: s.bg, color: s.color, borderColor: s.border }}>
      {text}
    </span>
  )
}

// ── Info Row ───────────────────────────────────────
export function InfoRow({ label, value, color, mono = true }: {
  label: string; value: string; color?: string; mono?: boolean
}) {
  return (
    <div className="flex justify-between items-center py-2" style={{ borderBottom: '1px solid var(--border2)' }}>
      <span className="text-xs" style={{ color: 'var(--muted)' }}>{label}</span>
      <span className={`text-xs font-semibold ${mono ? 'mono' : ''}`} style={{ color: color || 'var(--text2)' }}>
        {value}
      </span>
    </div>
  )
}

// ── Divider ────────────────────────────────────────
export function Divider() {
  return <div className="divider my-3" />
}

// ── Section Title ──────────────────────────────────
export function SectionTitle({ icon, title, sub }: { icon?: React.ReactNode; title: string; sub?: string }) {
  return (
    <div className="mb-4">
      <h2 className="text-base font-semibold text-[var(--text)] flex items-center gap-2">
        {icon}{title}
      </h2>
      {sub && <p className="text-xs text-[var(--dim)] mt-0.5">{sub}</p>}
    </div>
  )
}

// ── Empty State ────────────────────────────────────
export function EmptyState({ icon, title, desc }: { icon: string; title: string; desc?: string }) {
  return (
    <div className="text-center py-12 px-4">
      <div className="text-4xl mb-3">{icon}</div>
      <div className="text-sm font-semibold" style={{ color: 'var(--muted)' }}>{title}</div>
      {desc && <div className="text-xs mt-1" style={{ color: 'var(--dim)' }}>{desc}</div>}
    </div>
  )
}

// ── Skeleton ───────────────────────────────────────
export function Skeleton({ className = '', style }: { className?: string; style?: React.CSSProperties }) {
  return <div className={`skeleton ${className}`} style={style} />
}

export function SkeletonCard() {
  return (
    <div className="card">
      <Skeleton className="skeleton-text mb-3" />
      <Skeleton className="skeleton-value mb-2" />
      <Skeleton className="skeleton-text" style={{ width: '40%' }} />
    </div>
  )
}

export function SkeletonPage() {
  return (
    <div className="flex flex-col gap-4">
      <div className="grid grid-cols-2 gap-3">
        <SkeletonCard /><SkeletonCard /><SkeletonCard /><SkeletonCard />
      </div>
      <Skeleton className="skeleton-chart" />
      <SkeletonCard />
    </div>
  )
}

// ── Toast ──────────────────────────────────────────
export function Toast({ message, type = 'info' }: { message: string; type?: 'success' | 'error' | 'info' }) {
  const colors = {
    success: { bg: 'var(--green-bg)', border: 'var(--green-border)', color: 'var(--green)' },
    error:   { bg: 'var(--red-bg)',   border: 'var(--red-border)',   color: 'var(--red)' },
    info:    { bg: 'var(--accent-bg)', border: 'var(--accent-border)', color: 'var(--accent-light)' },
  }
  const c = colors[type]
  return (
    <div className="toast" style={{ background: c.bg, border: `1px solid ${c.border}`, color: c.color }}>
      {message}
    </div>
  )
}

// ── Button variants ────────────────────────────────
export function Button({ children, variant = 'primary', size, disabled, onClick, className = '' }: {
  children: React.ReactNode; variant?: 'primary' | 'secondary' | 'ghost'; size?: 'sm'
  disabled?: boolean; onClick?: () => void; className?: string
}) {
  const cls = `btn btn-${variant}${size === 'sm' ? ' btn-sm' : ''} ${className}`
  return <button className={cls} disabled={disabled} onClick={onClick}>{children}</button>
}

// ── Mode Badge (top-right corner of each tab) ──────
export function ModeBadge({ mode }: { mode: 'live' | 'demo' }) {
  const isLive = mode === 'live'
  return (
    <span className="status-pill" style={{
      borderColor: isLive ? 'var(--green-border)' : 'var(--accent-border)',
      color: isLive ? 'var(--green)' : 'var(--accent-light)',
      background: isLive ? 'var(--green-bg)' : 'var(--accent-bg)',
      fontSize: 10,
      padding: '3px 8px',
    }}>
      <span style={{ width: 5, height: 5, borderRadius: '50%', background: 'currentColor', display: 'inline-block' }} />
      {isLive ? 'LIVE' : 'DEMO'}
    </span>
  )
}
