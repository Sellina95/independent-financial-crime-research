import csv
import json
import time
import urllib.request
from collections import Counter
from pathlib import Path

TXID = "64a87c3d7540876516d0bf274fcc4773c0d59d07e960287b1d1ddbf690335b08"
BASE = "https://mempool.space/api"
OUT = Path("research/547_sat_investigation")
OUT.mkdir(parents=True, exist_ok=True)

def fetch(txid):
    url = f"{BASE}/tx/{txid}"
    for attempt in range(4):
        try:
            with urllib.request.urlopen(url, timeout=30) as r:
                return json.load(r)
        except Exception:
            if attempt == 3:
                raise
            time.sleep(2 ** attempt)

tx = fetch(TXID)

dust = [
    (i, vin)
    for i, vin in enumerate(tx["vin"])
    if vin.get("prevout", {}).get("value") == 547
]

print(f"Total inputs: {len(tx['vin'])}")
print(f"547-sat inputs: {len(dust)}")

if len(tx["vin"]) != 78 or len(dust) != 46:
    raise SystemExit("STOP: Input count mismatch")

rows = []
parents = {}

for n, (index, vin) in enumerate(dust, 1):
    parent_id = vin["txid"]
    vout = vin["vout"]

    if parent_id not in parents:
        parents[parent_id] = fetch(parent_id)
        time.sleep(0.2)

    parent = parents[parent_id]
    output = parent["vout"][vout]

    if output["value"] != 547:
        raise RuntimeError(f"Outpoint mismatch: {parent_id}:{vout}")

    funding = []
    for pvin in parent["vin"]:
        prev = pvin.get("prevout") or {}
        funding.append({
            "address": prev.get("scriptpubkey_address"),
            "value": prev.get("value"),
            "txid": pvin.get("txid"),
            "vout": pvin.get("vout"),
        })

    addresses = sorted({
        item["address"]
        for item in funding
        if item["address"]
    })

    rows.append({
        "consolidation_input_index": index,
        "parent_txid": parent_id,
        "parent_vout": vout,
        "received_address": output.get("scriptpubkey_address", ""),
        "received_sats": output["value"],
        "parent_block_time": parent.get("status", {}).get("block_time", ""),
        "parent_input_count": len(parent["vin"]),
        "parent_output_count": len(parent["vout"]),
        "funding_addresses": " | ".join(addresses),
        "funding_outpoints_json": json.dumps(funding),
        "evidence": "OBSERVED_ONCHAIN",
    })

    print(f"[{n}/{len(dust)}] {parent_id}:{vout}")

fields = list(rows[0].keys())

with (OUT / "547_input_provenance.csv").open(
    "w", newline="", encoding="utf-8"
) as f:
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    writer.writerows(rows)

print("\n=== PARENT TRANSACTIONS ===")
for txid, count in Counter(r["parent_txid"] for r in rows).most_common():
    print(count, txid)

print("\n=== FUNDING ADDRESS SETS ===")
for addresses, count in Counter(
    r["funding_addresses"] for r in rows
).most_common():
    print(count, addresses or "UNKNOWN")

print("\nSaved:", OUT / "547_input_provenance.csv")
