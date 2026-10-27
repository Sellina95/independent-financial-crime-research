import csv
import json
import time
import urllib.error
import urllib.request
from collections import defaultdict
from pathlib import Path

BASE = "https://mempool.space/api"
TXID = "64a87c3d7540876516d0bf274fcc4773c0d59d07e960287b1d1ddbf690335b08"
OUT = Path("research/547_sat_investigation")
MAX_TX_FETCHES = 500

cache = {}
fetch_count = 0

def fetch(txid):
    global fetch_count

    if txid in cache:
        return cache[txid]

    if fetch_count >= MAX_TX_FETCHES:
        raise RuntimeError("STOP: API fetch limit reached")

    for attempt in range(5):
        try:
            req = urllib.request.Request(
                f"{BASE}/tx/{txid}",
                headers={"User-Agent": "IndependentResearch/1.0"}
            )
            with urllib.request.urlopen(req, timeout=30) as r:
                data = json.load(r)

            cache[txid] = data
            fetch_count += 1
            time.sleep(0.2)
            return data

        except (urllib.error.URLError, TimeoutError):
            if attempt == 4:
                raise
            time.sleep(2 ** attempt)

def input_outpoints(tx):
    return [
        (vin["txid"], vin["vout"])
        for vin in tx["vin"]
        if "txid" in vin and "vout" in vin
    ]

def build_side(roots, side):
    tx_map = defaultdict(list)

    # Level 0: transactions that created the root UTXOs
    root_txids = sorted({txid for txid, _ in roots})

    for txid in root_txids:
        tx_map[txid].append({
            "side": side,
            "level": 0
        })

    # Level 1: transactions that funded those transactions
    for n, txid in enumerate(root_txids, 1):
        tx = fetch(txid)
        for parent_id, parent_vout in input_outpoints(tx):
            tx_map[parent_id].append({
                "side": side,
                "level": 1,
                "via_txid": txid,
                "via_parent_vout": parent_vout
            })

        if n % 10 == 0:
            print(f"{side}: {n}/{len(root_txids)} roots checked")

    return tx_map

with (OUT / "547_input_provenance.csv").open(
    encoding="utf-8"
) as f:
    dust_rows = list(csv.DictReader(f))

if len(dust_rows) != 46:
    raise SystemExit("STOP: Expected exactly 46 dust rows")

dust_roots = set()
for row in dust_rows:
    for item in json.loads(row["funding_outpoints_json"]):
        if item["txid"] is not None and item["vout"] is not None:
            dust_roots.add((item["txid"], item["vout"]))

consolidation = fetch(TXID)

if len(consolidation["vin"]) != 78:
    raise SystemExit("STOP: Expected 78 consolidation inputs")

large_roots = {
    (vin["txid"], vin["vout"])
    for vin in consolidation["vin"]
    if vin.get("prevout", {}).get("value") != 547
}

if len(large_roots) != 32:
    raise SystemExit("STOP: Expected 32 large inputs")

print("Dust funding outpoints:", len(dust_roots))
print("Large input outpoints:", len(large_roots))

dust_map = build_side(dust_roots, "DUST")
large_map = build_side(large_roots, "LARGE")

shared_txids = sorted(set(dust_map) & set(large_map))

results = []

for txid in shared_txids:
    results.append({
        "shared_txid": txid,
        "dust_paths": dust_map[txid],
        "large_paths": large_map[txid]
    })

report = {
    "consolidation_txid": TXID,
    "method": "Shared ancestor transaction ID comparison",
    "dust_root_outpoints": len(dust_roots),
    "large_root_outpoints": len(large_roots),
    "dust_ancestor_txids": len(dust_map),
    "large_ancestor_txids": len(large_map),
    "shared_ancestor_txids": len(shared_txids),
    "api_transactions_fetched": fetch_count,
    "scope": "Root generating transactions plus one previous transaction generation",
    "matches": results,
    "warning": (
        "Shared TXID proves a common historical transaction, "
        "not common beneficial ownership or sender identity."
    )
}

path = OUT / "ancestry_overlap_v1.json"
path.write_text(
    json.dumps(report, indent=2, ensure_ascii=False),
    encoding="utf-8"
)

print("\n=== ANCESTRY COMPARISON ===")
print("Dust ancestor TXIDs:", len(dust_map))
print("Large ancestor TXIDs:", len(large_map))
print("Shared ancestor TXIDs:", len(shared_txids))

for txid in shared_txids:
    print("\nMATCH:", txid)
    print("DUST:", json.dumps(dust_map[txid]))
    print("LARGE:", json.dumps(large_map[txid]))

print("\nSaved:", path)
