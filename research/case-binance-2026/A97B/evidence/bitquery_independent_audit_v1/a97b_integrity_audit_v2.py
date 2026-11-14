import csv
import json
import hashlib
from pathlib import Path
from collections import Counter, defaultdict
from decimal import Decimal

ROOT = Path("a97b_batch_audit_full_1015_v1")
SOURCE = Path("A97B_ADDRESS_ETH_RETURN_V1.csv")
INPUT = Path("reconciliation_full_1015.csv")
MANIFEST = ROOT / "manifest.json"
RESULT = ROOT / "audit_results.csv"
OUT = ROOT / "FINAL_INTEGRITY_AUDIT_V2.json"

WETH = "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2"
TOPIC = "0x7fcf532c15f0a6db0bd6d0e038bea71d30d808c7d98cb3bf7268a95bf5081b65"

def sha(data):
    return hashlib.sha256(data).hexdigest()

def stop(reason):
    raise SystemExit("STOP: " + reason)

def read_csv(path):
    with path.open(newline="") as f:
        return list(csv.DictReader(f))

def norm(tx):
    return str(tx).strip().lower()

def flag(value, expected):
    if isinstance(value, bool):
        return value is expected
    if isinstance(value, int):
        return value == int(expected)
    if isinstance(value, str):
        return value.lower() in (
            ("true", "1") if expected else ("false", "0")
        )
    return False

if OUT.exists():
    stop("V2 report already exists; refusing overwrite")

source = read_csv(SOURCE)
converted = read_csv(INPUT)
old_results = read_csv(RESULT)
manifest = json.loads(MANIFEST.read_text())

expected = {}
for row in source:
    tx = norm(row["tx_hash"])
    amount = Decimal(row["expected_unwrap_eth"]) * Decimal(10**18)

    if tx in expected:
        stop("Duplicate source transaction")
    if amount != amount.to_integral_value():
        stop("Fractional wei")

    expected[tx] = int(amount)

converted_map = {
    norm(r["tx_hash"]): int(r["expected_wei"])
    for r in converted
}

if len(source) != 1015 or len(converted_map) != 1015:
    stop("Input census invalid")

if expected != converted_map:
    stop("Source and converted wei mismatch")

if sha(INPUT.read_bytes()) != manifest["input_sha256"]:
    stop("Input SHA256 mismatch")

if sha(RESULT.read_bytes()) != manifest["results_sha256"]:
    stop("Results SHA256 mismatch")

batches = manifest["batches"]

if len(batches) != 21:
    stop("Batch count mismatch")

requested = []
events = defaultdict(list)
raw_event_count = 0

for index, batch in enumerate(batches, 1):
    path = Path(batch["file"])

    if not path.exists():
        stop(f"Missing batch file: {path}")

    if sha(path.read_bytes()) != batch["sha256"]:
        stop(f"Batch SHA256 mismatch: {path}")

    saved = json.loads(path.read_text())

    txs = [norm(x) for x in saved["requested_txs"]]
    requested.extend(txs)

    response = saved["response"]

    if response.get("isError"):
        stop(f"API error in batch {index}")

    if not isinstance(response.get("content"), list):
        stop(f"Missing response content in batch {index}")

    for item in response["content"]:
        if item.get("type") != "text":
            continue

        parsed = json.loads(item["text"])

        if isinstance(parsed, list):
            records = parsed
        elif isinstance(parsed, dict) and isinstance(parsed.get("rows"), list):
            columns = parsed.get("columns")
            if not isinstance(columns, list):
                stop(f"Invalid columnar response: batch {index}")
            records = [
                dict(zip(columns, values))
                for values in parsed["rows"]
            ]
        elif isinstance(parsed, dict):
            records = [parsed]
        else:
            stop(f"Unknown response format: batch {index}")

        for event in records:
            tx = norm(event.get("Tx", ""))
            events[tx].append(event)
            raw_event_count += 1

# Census check: use normalized transaction hashes.
if Counter(requested) != Counter(expected.keys()):
    missing = list((Counter(expected.keys()) - Counter(requested)).elements())
    extra = list((Counter(requested) - Counter(expected.keys())).elements())
    stop(f"Census mismatch: missing={missing[:3]}, extra={extra[:3]}")

if set(events) - set(expected):
    stop("Unexpected event transaction hashes")

if len(old_results) != 1015:
    stop("Previous audit result count mismatch")

previous = {norm(r["tx_hash"]): r for r in old_results}

if len(previous) != 1015 or set(previous) != set(expected):
    stop("Previous audit transaction census mismatch")

failures = []
checks = []

for tx, expected_wei in expected.items():
    tx_events = events.get(tx, [])

    qualifying = [
        e for e in tx_events
        if norm(e.get("Emitter")) == WETH
        and norm(e.get("Topic0")) == TOPIC
        and e.get("Signature") == "Withdrawal(address,uint256)"
        and flag(e.get("TxSuccess"), True)
        and flag(e.get("CallSuccess"), True)
        and flag(e.get("Reverted"), False)
        and flag(e.get("Removed"), False)
    ]

    reasons = []

    if len(qualifying) != 1:
        reasons.append(f"Qualifying event count={len(qualifying)}")
    else:
        event = qualifying[0]
        data = event.get("Data", "")

        try:
            if not isinstance(data, str) or len(data) != 66:
                raise ValueError("Invalid Data length")

            raw_wei = int(data, 16)

            if raw_wei != expected_wei:
                reasons.append("Raw wei mismatch")

            args = event.get("Arguments", [])
            wad = [
                a.get("Value")
                for a in args
                if isinstance(a, dict) and a.get("Name") == "wad"
            ]

            if len(wad) != 1 or int(wad[0]) != raw_wei:
                reasons.append("Decoded wad mismatch")

        except (ValueError, TypeError):
            reasons.append("Malformed event data")

    if previous[tx].get("verdict") != "MATCH":
        reasons.append("Previous result not MATCH")

    record = {
        "tx_hash": tx,
        "expected_wei": str(expected_wei),
        "raw_events": len(tx_events),
        "qualifying_events": len(qualifying),
        "status": "PASS" if not reasons else "REVIEW_REQUIRED",
        "reasons": reasons,
    }

    checks.append(record)

    if reasons:
        failures.append(record)

summary = {
    "source_transactions": len(expected),
    "requested_transactions": len(requested),
    "unique_requested": len(set(requested)),
    "batch_count": len(batches),
    "raw_event_rows": raw_event_count,
    "pass": len(checks) - len(failures),
    "review_required": len(failures),
    "all_pass": len(failures) == 0,
    "incident_provenance": "NOT_ESTABLISHED",
}

report = {
    "summary": summary,
    "source_sha256": sha(SOURCE.read_bytes()),
    "input_sha256": sha(INPUT.read_bytes()),
    "manifest_sha256": sha(MANIFEST.read_bytes()),
    "previous_results_sha256": sha(RESULT.read_bytes()),
    "failures": failures,
    "checks": checks,
}

OUT.write_text(json.dumps(report, indent=2) + "\n")

print("\n===== A97B INTEGRITY AUDIT V2 =====")
for key, value in summary.items():
    print(f"{key.upper()}: {value}")

print("REPORT:", OUT)
print("REPORT_SHA256:", sha(OUT.read_bytes()))
