import csv
import hashlib
import json
import os
import urllib.request
from decimal import Decimal, getcontext
from pathlib import Path

getcontext().prec = 100

BASE = Path("research/case-binance-2026/evidence/initial_tx_v1")
RECEIPT = BASE / "receipt.json"
OUT = BASE / "token_inventory.csv"
TMP = BASE / "token_inventory.csv.tmp"

TX = "0x53bd38b816c23e74134786c29a8c18d792777998a3b9326047b583100e88e2f3"
SOURCE = "0x28c6c06298d514db089934071355e5743bf21d60"
TARGET = "0x5227f603c1ee34ce3c06efe6477003bdfccb2f8c"
TOPIC = "0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef"
BLOCK = 26300770
BATCH = 12

RPCS = [
    "https://ethereum.publicnode.com",
    "https://eth.drpc.org",
    "https://1rpc.io/eth"
]

FIELDS = [
    "transaction", "block", "log_index",
    "contract", "from", "to",
    "raw_amount", "symbol", "decimals",
    "quantity", "metadata_block"
]

def rpc(method, params):
    errors = []
    payload = json.dumps({
        "jsonrpc": "2.0", "id": 1,
        "method": method, "params": params
    }).encode()

    for url in RPCS:
        try:
            req = urllib.request.Request(
                url, data=payload,
                headers={
                    "Content-Type": "application/json",
                    "User-Agent": "Mozilla/5.0"
                }
            )
            with urllib.request.urlopen(req, timeout=15) as r:
                answer = json.load(r)
            if "error" in answer:
                raise RuntimeError(str(answer["error"]))
            if answer.get("result") is None:
                raise RuntimeError("Empty result")
            return answer["result"]
        except Exception as e:
            errors.append(str(e)[:70])

    raise RuntimeError(" / ".join(errors))

def call(contract, selector):
    return rpc("eth_call", [
        {"to": contract, "data": selector},
        hex(BLOCK)
    ])

def symbol_decode(raw):
    data = bytes.fromhex(raw[2:])
    if len(data) == 32:
        value = data.rstrip(b"\0")
    else:
        if len(data) < 96:
            raise ValueError("Invalid symbol data")
        offset = int.from_bytes(data[:32], "big")
        if offset + 32 > len(data):
            raise ValueError("Invalid offset")
        n = int.from_bytes(data[offset:offset+32], "big")
        if n > 256 or offset + 32 + n > len(data):
            raise ValueError("Invalid symbol length")
        value = data[offset+32:offset+32+n]
    symbol = value.decode("utf-8").strip()
    if not symbol:
        raise ValueError("Empty symbol")
    return symbol

raw_receipt = RECEIPT.read_bytes()
expected_hash = "08b5bb08e7c82a6dc32950314932bbdcebe7481c5611585f68bad500f20e4961"
assert hashlib.sha256(raw_receipt).hexdigest() == expected_hash

receipt = json.loads(raw_receipt)
assert receipt["transactionHash"].lower() == TX
assert int(receipt["blockNumber"], 16) == BLOCK
assert int(receipt["status"], 16) == 1

events = []
for log in receipt["logs"]:
    t = log["topics"]
    if len(t) != 3 or t[0].lower() != TOPIC:
        continue
    if len(log["data"]) != 66:
        continue

    src = "0x" + t[1][-40:].lower()
    dst = "0x" + t[2][-40:].lower()
    assert (src, dst) == (SOURCE, TARGET)

    events.append({
        "transaction": TX,
        "block": str(BLOCK),
        "log_index": str(int(log["logIndex"], 16)),
        "contract": log["address"].lower(),
        "from": src,
        "to": dst,
        "raw_amount": str(int(log["data"], 16))
    })

events.sort(key=lambda x: int(x["log_index"]))
assert len(events) == 63
assert len({r["contract"] for r in events}) == 63

existing = {}
if OUT.exists():
    with OUT.open(newline="") as f:
        reader = csv.DictReader(f)
        assert reader.fieldnames == FIELDS
        for row in reader:
            key = row["log_index"]
            assert key not in existing
            existing[key] = row

expected = {r["log_index"]: r for r in events}
for key, row in existing.items():
    assert key in expected
    for field, value in expected[key].items():
        assert row[field] == value
    assert row["metadata_block"] == str(BLOCK)
    assert format(
        Decimal(row["raw_amount"]) /
        (Decimal(10) ** int(row["decimals"])), "f"
    ) == row["quantity"]

print("===== ASSET LEDGER =====", flush=True)
print("Previously saved:", len(existing), "/ 63", flush=True)

processed = 0
for event in events:
    key = event["log_index"]
    if key in existing:
        continue
    if processed >= BATCH:
        break

    try:
        contract = event["contract"]
        symbol = symbol_decode(call(contract, "0x95d89b41"))
        decimals = int(call(contract, "0x313ce567"), 16)
        assert 0 <= decimals <= 77

        quantity = format(
            Decimal(event["raw_amount"]) /
            (Decimal(10) ** decimals), "f"
        )
        row = {
            **event,
            "symbol": symbol,
            "decimals": str(decimals),
            "quantity": quantity,
            "metadata_block": str(BLOCK)
        }

        existing[key] = row
        with TMP.open("w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=FIELDS)
            writer.writeheader()
            writer.writerows(
                existing[k] for k in sorted(existing, key=int)
            )
            f.flush()
            os.fsync(f.fileno())
        os.replace(TMP, OUT)

        processed += 1
        print(f"PASS {len(existing):02d}/63: {symbol} {quantity}", flush=True)

    except Exception as e:
        print("UNRESOLVED:", contract, str(e)[:100], flush=True)

print("\n===== RESULT =====")
print("Saved:", len(existing), "/ 63")
print("Remaining:", 63 - len(existing))
print("CSV:", OUT)
print("STATUS:", "COMPLETE" if len(existing) == 63 else "PARTIAL")
print("NOT COMMITTED")
