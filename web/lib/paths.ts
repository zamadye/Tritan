import fs from 'fs'
import path from 'path'

// Resolve project root — works in both dev (cwd=web/) and standalone (cwd=.next/standalone/)
function findRoot(): string {
  const candidates = [
    path.join(process.cwd(), '..'),          // dev: web/ → Tritan/
    path.join(process.cwd(), '..', '..', '..'), // standalone: .next/standalone/ → Tritan/
    '/root/Tritan',                           // absolute fallback
  ]
  for (const dir of candidates) {
    if (fs.existsSync(path.join(dir, '.env'))) return dir
  }
  return '/root/Tritan'
}

export const ROOT = findRoot()
export const DATA_DIR = path.join(ROOT, 'data')
export const ENV_FILE = path.join(ROOT, '.env')

export function readJSON(file: string) {
  try { return JSON.parse(fs.readFileSync(path.join(DATA_DIR, file), 'utf-8')) }
  catch { return null }
}

export function readEnvValue(key: string): string {
  try {
    const m = fs.readFileSync(ENV_FILE, 'utf-8').match(new RegExp(`^${key}=(.+)$`, 'm'))
    return m?.[1]?.trim() ?? ''
  } catch { return '' }
}
