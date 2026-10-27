import csv
import json
import urllib.request
from pathlib import Path

BASE = "https://mempool.space/api"
TXID = "64a87c3d7540876516d0bf274fcc4773c0d59d07e960287b1d1ddbf690335b08"
OUT = Path("research/547_sat_investigation")

def fetch(txid):
    with urllib.request.urlopen(f"{BASE}/tx/{txid}", timeout=30) as r:
        return json.load(r)

with (OUT / "547_input_provenance.csv").open(encoding="utf-8") as f:
    dust = list(csv.DictReader(f))

dust_funding = set()
for row in dust:
    for item in json.loads(row["funding_outpoints_json"]):
        if item["address"]:
            dust_funding.add(item["address"])

tx = fetch(TXID)
large = [
    (i, vin)
    for i, vin in enumerate(tx["vin"])
    if vin.get("prevout", {}).get("value") != 547
]

large_addresses = {
    vin["prevout"].get("scriptpubkey_address")
    for _, vin in large
    if vin.get("prevout")
}
large_addresses.discard(None)

matches = dust_funding & large_addresses

print("=== DIRECT ADDRESS COMPARISON ===")
print("Dust funding addresses:", len(dust_funding))
print("Large input addresses:", len(large_addresses))
print("Shared addresses:", len(matches))

for address in sorted(matches):
    print("MATCH:", address)
    for i, vin in large:
        if vin["prevout"].get("scriptpubkey_address") == address:
            print("  Large input:", i, vin["txid"], vin["vout"])

with (OUT / "direct_address_overlap.json").open("w") as f:
    json.dump({
        "dust_funding_addresses": len(dust_funding),
        "large_input_addresses": len(large_addresses),
        "shared_addresses": sorted(matches),
        "scope": "Direct address overlap only",
    }, f, indent=2)

print("Saved:", OUT / "direct_address_overlap.json")
