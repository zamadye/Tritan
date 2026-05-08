import type { NextConfig } from "next";
import { readFileSync } from "fs";
import { join } from "path";

// Read token from .env at build time
function readEnvToken(): string {
  try {
    const env = readFileSync(join(__dirname, '..', '.env'), 'utf-8')
    const match = env.match(/^API_SECRET_TOKEN=(.+)$/m)
    return match ? match[1].trim() : ''
  } catch { return '' }
}

const nextConfig: NextConfig = {
  env: {
    API_SECRET_TOKEN: readEnvToken(),
  },
  async headers() {
    return [
      {
        source: '/:path*',
        headers: [
          { key: 'X-Frame-Options',           value: 'DENY' },
          { key: 'X-Content-Type-Options',     value: 'nosniff' },
          { key: 'Referrer-Policy',            value: 'strict-origin-when-cross-origin' },
          { key: 'X-XSS-Protection',           value: '1; mode=block' },
          { key: 'Permissions-Policy',         value: 'camera=(), microphone=(), geolocation=()' },
          { key: 'Strict-Transport-Security',  value: 'max-age=63072000; includeSubDomains' },
          { key: 'Content-Security-Policy',    value: "default-src 'self'; script-src 'self' 'unsafe-inline' 'unsafe-eval'; style-src 'self' 'unsafe-inline'; img-src 'self' data:; connect-src 'self'" },
        ],
      },
    ]
  },
};

export default nextConfig;
