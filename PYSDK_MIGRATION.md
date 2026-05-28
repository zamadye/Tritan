# Polymarket SDK Migration: py-clob-client to polymarket-client

Migration mapping from `py_clob_client_v2` (old) to `polymarket` (new SDK beta).

---

## 1. Client Initialization (`core.py`)

### Old
```python
from py_clob_client_v2.client import ClobClient
client = ClobClient(host, key=key, chain_id=137, signature_type=sig_type, funder=funder)
client.set_api_creds(client.create_or_derive_api_key())
```

### New
```python
from polymarket import SecureClient, PRODUCTION
client = SecureClient.create(private_key=private_key, wallet=funder, environment=PRODUCTION)
```

---

## 2. Balance Check (`core.py`)

### Old
```python
from py_clob_client_v2.clob_types import BalanceAllowanceParams, AssetType
result = clob_client.get_balance_allowance(BalanceAllowanceParams(asset_type=AssetType.COLLATERAL))
bal = float(result.get("balance", 0)) / 1e6
```

### New
```python
ba = client.get_balance_allowance(asset_type="COLLATERAL")
bal = ba.balance / 1e6
```

---

## 3. Market Buy (`executor.py`)

### Old
```python
from py_clob_client_v2.clob_types import MarketOrderArgs, OrderType
from py_clob_client_v2.order_builder.constants import BUY
signed_order = clob_client.create_market_order(MarketOrderArgs(token_id=token_id, amount=size, side=BUY))
resp = clob_client.post_order(signed_order, OrderType.FOK)
```

### New
```python
resp = client.place_market_order(token_id=token_id, side="BUY", amount=size, order_type="FOK")
# resp is AcceptedOrder or RejectedOrder
```

---

## 4. Market Sell / Limit Order (`monitor.py`)

### Old
```python
from py_clob_client_v2.clob_types import OrderArgs, PartialCreateOrderOptions, OrderType
from py_clob_client_v2.order_builder.constants import SELL
resp = clob_client.create_and_post_order(
    OrderArgs(token_id=token_id, price=price, size=sell_size, side=SELL),
    PartialCreateOrderOptions(tick_size=tick, neg_risk=False),
    OrderType.GTC
)
```

### New
```python
resp = client.place_limit_order(token_id=token_id, price=price, size=sell_size, side="SELL")
```

---

## 5. Market Info (`monitor.py`, `executor.py`, `sync_live.py`)

### Old
```python
market = clob_client.get_market(condition_id)  # returns dict
tokens = market.get("tokens", [])
```

### New
```python
market = client.get_market(id=condition_id)  # returns Market object
# tokens at market.outcomes.yes / market.outcomes.no
```

---

## 6. Trade History (`sync_live.py`)

### Old
```python
resp = clob_client.get_trades()
clob_trades = resp.get("data", [])
```

### New
```python
paginator = client.list_account_trades()
all_trades = list(paginator.items())
```

---

## Key Breaking Changes

1. `SecureClient.create()` is factory method, not constructor
2. No `host`/`chain_id`/`signature_type` params - environment handles it
3. `get_market()` requires keyword arg: `id=`, `slug=`, or `url=`
4. Response is typed `AcceptedOrder|RejectedOrder`, not dict
5. All amounts are `Decimal`, not strings
6. `list_account_trades()` returns `Paginator`, not dict
