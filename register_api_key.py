"""
Run this on your LOCAL machine (not server) to register API key under deposit wallet.

Install first:
  pip install py-clob-client-v2 py-builder-relayer-client py-builder-signing-sdk

Then run:
  python register_api_key.py
"""

import os

# ── CONFIG ────────────────────────────────────────────────────────────────────
PRIVATE_KEY   = "0x93f8c1a709446b97e69499507f82d532ddf36964fda2fa7c6042f317ccf59d72"
DEPOSIT_WALLET = "0xdEc58Ebfc22feaC835B337c3127b0d45a8B85359"  # your safe/deposit wallet
CLOB_HOST     = "https://clob.polymarket.com"
RELAYER_URL   = "https://relayer.polymarket.com"
CHAIN_ID      = 137

# Builder API key (from Polymarket settings → API Keys)
BUILDER_API_KEY    = "019e07bc-c2d1-7efb-9024-1a808a23da50"
BUILDER_SECRET     = "-JetVL5CRRV8OvbUcK2458ZAJL7sQt66Yp67Ja4jNLM="
BUILDER_PASSPHRASE = "2bdfb4d8ba2e581be88cc4166fde199e28c31d68f2fd006dbb4398b5b77f215b"
# ─────────────────────────────────────────────────────────────────────────────

from py_clob_client_v2 import ClobClient
from py_clob_client_v2.clob_types import BalanceAllowanceParams, AssetType

print(f"Deposit wallet: {DEPOSIT_WALLET}")
print(f"CLOB host: {CLOB_HOST}")
print()

# Step 1: Register/derive API key under deposit wallet (sig_type=3)
print("Step 1: Registering API key under deposit wallet...")
client = ClobClient(
    host=CLOB_HOST,
    key=PRIVATE_KEY,
    chain_id=CHAIN_ID,
    signature_type=3,
    funder=DEPOSIT_WALLET,
)

try:
    creds = client.create_or_derive_api_key()
    client.set_api_creds(creds)
    print(f"✅ API Key: {creds.api_key}")
    print(f"   Secret:     {creds.api_secret}")
    print(f"   Passphrase: {creds.api_passphrase}")
except Exception as e:
    print(f"❌ create_or_derive failed: {e}")
    print("Trying create_api_key with nonce=0...")
    try:
        creds = client.create_api_key(nonce=0)
        client.set_api_creds(creds)
        print(f"✅ API Key: {creds.api_key}")
        print(f"   Secret:     {creds.api_secret}")
        print(f"   Passphrase: {creds.api_passphrase}")
    except Exception as e2:
        print(f"❌ create_api_key failed: {e2}")
        exit(1)

# Step 2: Verify balance is readable
print()
print("Step 2: Verifying balance...")
try:
    r = client.get_balance_allowance(BalanceAllowanceParams(asset_type=AssetType.COLLATERAL))
    bal = float(r.get("balance", 0)) / 1e6
    print(f"✅ Balance: ${bal:.4f} pUSD")
except Exception as e:
    print(f"❌ Balance check failed: {e}")

# Step 3: Print .env update
print()
print("=" * 60)
print("Update your .env on the server with these values:")
print("=" * 60)
print(f"POLYGON_WALLET_ADDRESS={DEPOSIT_WALLET}")
print(f"SIGNATURE_TYPE=3")
print(f"POLY_API_KEY={creds.api_key}")
print(f"POLY_API_SECRET={creds.api_secret}")
print(f"POLY_API_PASSPHRASE={creds.api_passphrase}")
print("=" * 60)
