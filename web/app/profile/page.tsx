'use client'
import { useState, useEffect } from 'react'
import { useRouter } from 'next/navigation'
import { useAuth } from '@/lib/auth'
import { useData } from '@/hooks/useData'
import { ArrowLeft, Wallet, User, Shield, Activity, TrendingUp, LogOut } from 'lucide-react'
import Link from 'next/link'

export default function ProfilePage() {
  const { user, logout, updateUser } = useAuth()
  const { data, agent, account } = useData()
  const router = useRouter()
  const [editing, setEditing] = useState(false)
  const [email, setEmail] = useState('')

  useEffect(() => {
    if (!user) router.push('/login')
    else setEmail(user.email)
  }, [user, router])

  if (!user) return null

  const isLive = data?.agent_mode === 'live' || agent?.mode === 'live'
  const resolved = data?.stats?.resolved || 0
  const wins = data?.stats?.wins || 0
  const losses = data?.stats?.losses || 0
  const pnl = data?.stats?.pnl || 0
  const wr = data?.stats?.wr || 0

  const handleSave = () => {
    if (email.includes('@')) {
      updateUser({ email })
      setEditing(false)
    }
  }

  return (
    <div className="min-h-screen" style={{ background: 'var(--bg)', color: 'var(--text)' }}>
      {/* Header */}
      <div className="flex items-center gap-3 p-4" style={{ borderBottom: '1px solid var(--border2)' }}>
        <Link href="/" className="icon-btn" style={{ background: 'var(--bg3)', color: 'var(--muted)' }}>
          <ArrowLeft size={16} />
        </Link>
        <div className="text-base font-bold">Profile</div>
      </div>

      <div className="p-4 max-w-lg mx-auto flex flex-col gap-4 fade-in">
        {/* User Card */}
        <div className="section-card p-5">
          <div className="flex items-center gap-4 mb-4">
            <div className="w-14 h-14 rounded-2xl flex items-center justify-center text-xl font-bold" style={{
              background: isLive ? 'var(--green-bg)' : 'var(--accent-bg)',
              color: isLive ? 'var(--green)' : 'var(--accent-light)',
              border: `1px solid ${isLive ? 'var(--green-border)' : 'var(--accent-border)'}`,
            }}>
              {user.email.charAt(0).toUpperCase()}
            </div>
            <div className="flex-1">
              {editing ? (
                <div className="flex gap-2">
                  <input value={email} onChange={e => setEmail(e.target.value)}
                    className="input" style={{ padding: '8px 12px', fontSize: 13 }} />
                  <button onClick={handleSave} className="btn btn-primary btn-sm">Save</button>
                  <button onClick={() => { setEditing(false); setEmail(user.email) }} className="btn btn-ghost btn-sm">Cancel</button>
                </div>
              ) : (
                <>
                  <div className="text-sm font-semibold" style={{ color: 'var(--text2)' }}>{user.email}</div>
                  <div className="text-xs mt-0.5" style={{ color: 'var(--dim)' }}>
                    Member since {new Date(user.createdAt).toLocaleDateString()}
                  </div>
                </>
              )}
            </div>
          </div>

          {/* Mode badge */}
          <div className="flex items-center justify-between p-3 rounded-xl" style={{
            background: isLive ? 'var(--green-bg)' : 'var(--accent-bg)',
            border: `1px solid ${isLive ? 'var(--green-border)' : 'var(--accent-border)'}`,
          }}>
            <div className="flex items-center gap-2">
              <span className="text-sm">{isLive ? '💰' : '📝'}</span>
              <span className="text-xs font-semibold" style={{ color: isLive ? 'var(--green)' : 'var(--accent-light)' }}>
                {isLive ? 'Live Trading Mode' : 'Demo Mode'}
              </span>
            </div>
            <span className="text-[10px] mono px-2 py-0.5 rounded-md" style={{ background: 'var(--bg)', color: 'var(--dim)' }}>
              {isLive ? 'REAL MONEY' : 'SIMULATION'}
            </span>
          </div>
        </div>

        {/* Wallet Info (Live only) */}
        {isLive && account && (
          <div className="section-card p-5">
            <div className="flex items-center gap-2 mb-4">
              <Wallet size={16} style={{ color: 'var(--accent)' }} />
              <div className="text-sm font-semibold" style={{ color: 'var(--text2)' }}>Wallet</div>
            </div>
            <div className="flex flex-col gap-3">
              <div className="flex justify-between items-center py-2" style={{ borderBottom: '1px solid var(--border2)' }}>
                <span className="text-xs" style={{ color: 'var(--dim)' }}>Address</span>
                <span className="text-xs mono" style={{ color: 'var(--text2)' }}>{account.wallet || '—'}</span>
              </div>
              <div className="flex justify-between items-center py-2" style={{ borderBottom: '1px solid var(--border2)' }}>
                <span className="text-xs" style={{ color: 'var(--dim)' }}>USDC Balance</span>
                <span className="text-sm font-bold mono" style={{ color: 'var(--green)' }}>
                  ${account.usdc_balance?.toFixed(2) || '0.00'}
                </span>
              </div>
              <div className="flex justify-between items-center py-2" style={{ borderBottom: '1px solid var(--border2)' }}>
                <span className="text-xs" style={{ color: 'var(--dim)' }}>Deployed</span>
                <span className="text-xs mono" style={{ color: 'var(--yellow)' }}>
                  ${data?.stats?.deployed?.toFixed(2) || '0.00'}
                </span>
              </div>
              <div className="flex justify-between items-center py-2">
                <span className="text-xs" style={{ color: 'var(--dim)' }}>Available</span>
                <span className="text-xs mono" style={{ color: 'var(--text2)' }}>
                  ${((account.usdc_balance || 0) - (data?.stats?.deployed || 0)).toFixed(2)}
                </span>
              </div>
            </div>
          </div>
        )}

        {/* Trading Stats */}
        <div className="section-card p-5">
          <div className="flex items-center gap-2 mb-4">
            <Activity size={16} style={{ color: 'var(--accent)' }} />
            <div className="text-sm font-semibold" style={{ color: 'var(--text2)' }}>Trading Stats</div>
          </div>
          <div className="grid grid-cols-2 gap-3">
            <div className="p-3 rounded-xl text-center" style={{ background: 'var(--bg)', border: '1px solid var(--border2)' }}>
              <div className="text-lg font-bold mono" style={{ color: pnl >= 0 ? 'var(--green)' : 'var(--red)' }}>
                {pnl >= 0 ? '+' : ''}${pnl.toFixed(2)}
              </div>
              <div className="text-[10px]" style={{ color: 'var(--dim)' }}>Total P&L</div>
            </div>
            <div className="p-3 rounded-xl text-center" style={{ background: 'var(--bg)', border: '1px solid var(--border2)' }}>
              <div className="text-lg font-bold mono" style={{ color: wr >= 0.55 ? 'var(--green)' : 'var(--yellow)' }}>
                {(wr * 100).toFixed(1)}%
              </div>
              <div className="text-[10px]" style={{ color: 'var(--dim)' }}>Win Rate</div>
            </div>
            <div className="p-3 rounded-xl text-center" style={{ background: 'var(--bg)', border: '1px solid var(--border2)' }}>
              <div className="text-lg font-bold mono" style={{ color: 'var(--text2)' }}>{resolved}</div>
              <div className="text-[10px]" style={{ color: 'var(--dim)' }}>Resolved</div>
            </div>
            <div className="p-3 rounded-xl text-center" style={{ background: 'var(--bg)', border: '1px solid var(--border2)' }}>
              <div className="text-lg font-bold mono" style={{ color: 'var(--text2)' }}>{data?.stats?.open || 0}</div>
              <div className="text-[10px]" style={{ color: 'var(--dim)' }}>Open</div>
            </div>
          </div>
          <div className="flex justify-between items-center py-2 mt-3" style={{ borderTop: '1px solid var(--border2)' }}>
            <span className="text-xs" style={{ color: 'var(--dim)' }}>Record</span>
            <span className="text-xs mono" style={{ color: 'var(--text2)' }}>
              <span style={{ color: 'var(--green)' }}>{wins}W</span> · <span style={{ color: 'var(--red)' }}>{losses}L</span>
            </span>
          </div>
        </div>

        {/* Actions */}
        <div className="section-card p-4">
          <button onClick={() => { setEditing(true); setEmail(user.email) }}
            className="flex items-center gap-3 w-full p-3 rounded-xl" style={{ background: 'transparent', border: 'none', cursor: 'pointer', color: 'var(--text2)' }}>
            <User size={16} style={{ color: 'var(--dim)' }} />
            <span className="text-sm">Edit Profile</span>
          </button>
          <div className="divider my-1" />
          <button onClick={() => { logout(); router.push('/login') }}
            className="flex items-center gap-3 w-full p-3 rounded-xl" style={{ background: 'transparent', border: 'none', cursor: 'pointer', color: 'var(--red)' }}>
            <LogOut size={16} />
            <span className="text-sm">Logout</span>
          </button>
        </div>
      </div>
    </div>
  )
}
