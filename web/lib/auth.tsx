'use client'
import { createContext, useContext, useState, useEffect, ReactNode } from 'react'

export interface User {
  email: string
  polyApiKey?: string
  polySecret?: string
  polyPassphrase?: string
  mode: 'demo' | 'live'
  subscribed: boolean
  createdAt: string
}

interface AuthContextType {
  user: User | null
  loading: boolean
  login: (email: string) => void
  setupPoly: (apiKey: string, secret: string, passphrase: string) => void
  skipPoly: () => void
  logout: () => void
  updateUser: (updates: Partial<User>) => void
}

const AuthContext = createContext<AuthContextType | null>(null)

export function AuthProvider({ children }: { children: ReactNode }) {
  const [user, setUser] = useState<User | null>(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    try {
      const stored = localStorage.getItem('tritan_user')
      if (stored) setUser(JSON.parse(stored))
    } catch {}
    setLoading(false)
  }, [])

  const saveUser = (u: User | null) => {
    if (u) localStorage.setItem('tritan_user', JSON.stringify(u))
    else localStorage.removeItem('tritan_user')
    setUser(u)
  }

  const login = (email: string) => {
    saveUser({
      email,
      mode: 'demo',
      subscribed: false,
      createdAt: new Date().toISOString(),
    })
  }

  const setupPoly = (apiKey: string, secret: string, passphrase: string) => {
    if (!user) return
    saveUser({ ...user, polyApiKey: apiKey, polySecret: secret, polyPassphrase: passphrase, mode: 'live' })
  }

  const skipPoly = () => {
    if (!user) return
    saveUser({ ...user, mode: 'demo' })
  }

  const logout = () => saveUser(null)

  const updateUser = (updates: Partial<User>) => {
    if (!user) return
    saveUser({ ...user, ...updates })
  }

  return (
    <AuthContext.Provider value={{ user, loading, login, setupPoly, skipPoly, logout, updateUser }}>
      {children}
    </AuthContext.Provider>
  )
}

export function useAuth() {
  const ctx = useContext(AuthContext)
  if (!ctx) throw new Error('useAuth must be used within AuthProvider')
  return ctx
}
