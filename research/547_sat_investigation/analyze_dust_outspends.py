import csv
import json
import time
import urllib.request
from collections import Counter
from pathlib import Path

BASE = "https://mempool.space/api"
OUT = Path("research/547_sat_investigation")
MAX_SPENDING_TX = 100

def api(path):
    for attempt in range(5):
        try:
            req = urllib.request.Request(
                BASE + path,
                headers={"User-Agent": "IndependentResearch/1.0"}
            )
            with urllib.request.urlopen(req, timeout=30) as r:
                data = json.load(r)
            time.sleep(0.25)
            return data
        except Exception:
            if attempt == 4:
                raise
            time.sleep(2 ** attempt)

with (OUT / "547_input_provenance.csv").open(
    encoding="utf-8", newline=""
) as f:
    rows = list(csv.DictReader(f))

if len(rows) != 46:
    raise SystemExit("STOP: expected 46 dust inputs")

parents = sorted({r["parent_txid"] for r in rows})

if len(parents) != 40:
    raise SystemExit("STOP: expected 40 source transactions")

# Stage 1: enumerate ALL 547-sat outputs.
outputs = []

for n, txid in enumerate(parents, 1):
    tx = api(f"/tx/{txid}")
    spends = api(f"/tx/{txid}/outspends")

    if len(tx["vout"]) != len(spends):
        raise RuntimeError(f"Output count mismatch: {txid}")

    for vout, (output, spend) in enumerate(
        zip(tx["vout"], spends)
    ):
        if output["value"] != 547:
            continue

        outputs.append({
            "source_txid": txid,
            "vout": vout,
            "address": output.get("scriptpubkey_address", ""),
            "spent": bool(spend.get("spent")),
            "spending_txid": (
                spend.get("txid", "") if spend.get("spent") else ""
            ),
            "spending_vin": (
                spend.get("vin", "") if spend.get("spent") else ""
            ),
        })

    print(f"Source transactions: {n}/40")

def write_csv(path, data, fields):
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(data)

write_csv(
    OUT / "all_547_outputs.csv",
    outputs,
    ["source_txid", "vout", "address",
     "spent", "spending_txid", "spending_vin"]
)

# Stage 2: inspect a capped set of unique spending TXs.
spent_ids = sorted({
    r["spending_txid"]
    for r in outputs if r["spending_txid"]
})

sample_ids = spent_ids[:MAX_SPENDING_TX]
sample = []

for n, txid in enumerate(sample_ids, 1):
    tx = api(f"/tx/{txid}")

    values = [
        vin.get("prevout", {}).get("value")
        for vin in tx["vin"]
    ]

    if any(v is None for v in values):
        raise RuntimeError(f"Missing input value: {txid}")

    dust_count = sum(v == 547 for v in values)
    other_sats = sum(v for v in values if v != 547)
    total_sats = sum(values)

    sample.append({
        "spending_txid": txid,
        "input_count": len(values),
        "input_547_count": dust_count,
        "other_input_btc": f"{other_sats / 1e8:.8f}",
        "total_input_btc": f"{total_sats / 1e8:.8f}",
        "with_other_inputs": other_sats > 0,
        "with_1_btc_other_inputs": other_sats >= 1e8,
        "with_100_btc_other_inputs": other_sats >= 100e8,
    })

    if n % 10 == 0:
        print(f"Spending transactions: {n}/{len(sample_ids)}")

write_csv(
    OUT / "spending_transactions_sample.csv",
    sample,
    [
        "spending_txid", "input_count",
        "input_547_count", "other_input_btc",
        "total_input_btc", "with_other_inputs",
        "with_1_btc_other_inputs",
        "with_100_btc_other_inputs"
    ]
)

report = {
    "source_transactions": len(parents),
    "all_547_outputs": len(outputs),
    "spent_547_outputs": sum(r["spent"] for r in outputs),
    "unspent_547_outputs": sum(not r["spent"] for r in outputs),
    "unique_spending_transactions": len(spent_ids),
    "spending_transactions_analyzed": len(sample),
    "sample_selection": "First 100 spending TXIDs sorted lexically",
    "sample_is_representative": False,
    "sample_with_other_inputs": sum(
        r["with_other_inputs"] for r in sample
    ),
    "sample_with_1_btc_other_inputs": sum(
        r["with_1_btc_other_inputs"] for r in sample
    ),
    "sample_with_100_btc_other_inputs": sum(
        r["with_100_btc_other_inputs"] for r in sample
    ),
    "note": (
        "Amounts describe transaction inputs, not a person's "
        "balance, identity, or ownership."
    )
}

(OUT / "outspend_summary_v1.json").write_text(
    json.dumps(report, indent=2),
    encoding="utf-8"
)

print("\n=== FULL OUTPUT INVENTORY ===")
for k in [
    "source_transactions", "all_547_outputs",
    "spent_547_outputs", "unspent_547_outputs",
    "unique_spending_transactions"
]:
    print(f"{k}: {report[k]}")

print("\n=== EXPLORATORY SPENDING SAMPLE ===")
for k in [
    "spending_transactions_analyzed",
    "sample_with_other_inputs",
    "sample_with_1_btc_other_inputs",
    "sample_with_100_btc_other_inputs"
]:
    print(f"{k}: {report[k]}")

print("\nSaved CSV files and outspend_summary_v1.json")
