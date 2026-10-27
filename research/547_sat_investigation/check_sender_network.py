import csv
import json
from collections import defaultdict
from pathlib import Path

OUT = Path("research/547_sat_investigation")
SOURCE = OUT / "547_input_provenance.csv"

with SOURCE.open(encoding="utf-8", newline="") as f:
    rows = list(csv.DictReader(f))

if len(rows) != 46:
    raise SystemExit(f"STOP: expected 46 rows, got {len(rows)}")

# The 40 transactions that created the 547-sat outputs.
senders = {r["parent_txid"] for r in rows}

if len(senders) != 40:
    raise SystemExit(f"STOP: expected 40 sender transactions, got {len(senders)}")

# Directed edges: A -> B means B spent an output created by A.
edges = set()

for row in rows:
    child = row["parent_txid"]
    funding = json.loads(row["funding_outpoints_json"])

    for item in funding:
        parent = item.get("txid")
        vout = item.get("vout")

        if parent in senders:
            edges.add((parent, child, vout))

# Undirected connectivity for grouping.
graph = defaultdict(set)

for parent, child, vout in edges:
    graph[parent].add(child)
    graph[child].add(parent)

visited = set()
components = []

for node in sorted(senders):
    if node in visited:
        continue

    stack = [node]
    group = set()

    while stack:
        current = stack.pop()
        if current in visited:
            continue
        visited.add(current)
        group.add(current)
        stack.extend(graph[current] - visited)

    components.append(sorted(group))

components.sort(key=lambda x: (-len(x), x[0]))

connected = [c for c in components if len(c) > 1]
isolated = [c[0] for c in components if len(c) == 1]

report = {
    "scope": "Exact direct UTXO links among 40 identified sender transactions",
    "sender_transactions": len(senders),
    "direct_utxo_links": len(edges),
    "connected_groups": len(connected),
    "transactions_in_connected_groups": sum(map(len, connected)),
    "isolated_transactions": len(isolated),
    "edges": [
        {"from_txid": a, "to_txid": b, "spent_vout": v}
        for a, b, v in sorted(edges)
    ],
    "connected_groups_detail": connected,
    "isolated_txids": isolated,
    "limitations": (
        "Only direct links between the 40 identified transactions are tested. "
        "Shared ancestors through other transactions are not tested. "
        "Connections do not establish beneficial ownership."
    ),
}

path = OUT / "sender_network_v1.json"
path.write_text(json.dumps(report, indent=2), encoding="utf-8")

print("\n=== 547 SAT SENDER NETWORK ===")
print("Sender transactions:", len(senders))
print("Direct UTXO links:", len(edges))
print("Connected groups:", len(connected))
print("Transactions in connected groups:", sum(map(len, connected)))
print("Isolated transactions:", len(isolated))

print("\n=== VERIFIED DIRECT LINKS ===")
for a, b, v in sorted(edges):
    print(f"{a}:{v} -> {b}")

print("\n=== CONNECTED GROUPS ===")
for i, group in enumerate(connected, 1):
    print(f"\nGroup {i}: {len(group)} transactions")
    for txid in group:
        print(" ", txid)

print("\nSaved:", path)
