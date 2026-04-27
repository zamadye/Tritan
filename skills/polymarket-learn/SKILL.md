---
name: polymarket-learn
description: Show agent learning stats, calibration data, evolution lessons, and performance report by category. Helps understand where the agent is right or wrong.
user-invocable: true
metadata: {"openclaw":{"emoji":"🧠","requires":{"bins":["python3"]}}}
---

## polymarket-learn

Show learning stats, calibration, and evolution lessons from past trades.

### Usage
User says: "show learning", "calibration stats", "performance report", "what am I bad at"

### Execution
Performance report:
```
cd /root/polymarket && python3 main.py report
```

Full stats:
```
cd /root/polymarket && python3 main.py learn
```

Evolution lessons (what the agent learned from mistakes):
```
cd /root/polymarket && python3 -c "
from dotenv import load_dotenv; load_dotenv('/root/polymarket/.env')
import json
from pathlib import Path
evo = Path('/root/polymarket/data/evolution_lessons.json')
if evo.exists():
    d = json.loads(evo.read_text())
    print(f'Resolved trades: {d.get(\"total_resolved\",0)}')
    print(f'Win rate: {d.get(\"overall_win_rate\",0):.0%}')
    print('Category bias:', json.dumps(d.get('category_bias',{}), indent=2))
    print('Calibration adjustments:', d.get('calibration_adjustments',{}))
    print('Recent mistakes:')
    for m in d.get('recent_mistakes',[]):
        print(f'  - {m[\"question\"][:60]} → {m[\"lesson\"]}')
else:
    print('No evolution data yet — need resolved trades first.')
"
```

### Output
Show win rate, category performance, calibration errors, and lessons learned.
