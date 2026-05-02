import { NextResponse } from 'next/server'
import fs from 'fs'
import path from 'path'
import { exec } from 'child_process'
import { promisify } from 'util'

const execAsync = promisify(exec)
const ENV_FILE = path.join(process.cwd(), '..', '.env')

function readEnv(): Record<string, string> {
  const lines = fs.readFileSync(ENV_FILE, 'utf-8').split('\n')
  const env: Record<string, string> = {}
  for (const line of lines) {
    const m = line.match(/^([A-Z_]+)=(.*)$/)
    if (m) env[m[1]] = m[2]
  }
  return env
}

export async function GET() {
  return NextResponse.json(readEnv())
}

export async function POST(req: Request) {
  const updates: Record<string, string> = await req.json()
  let content = fs.readFileSync(ENV_FILE, 'utf-8')
  for (const [k, v] of Object.entries(updates)) {
    const re = new RegExp(`^${k}=.*`, 'm')
    if (re.test(content)) content = content.replace(re, `${k}=${v}`)
    else content += `\n${k}=${v}`
  }
  fs.writeFileSync(ENV_FILE, content)
  await execAsync('systemctl restart polymarket-agent').catch(() => {})
  return NextResponse.json({ ok: true })
}
