import csv
from decimal import Decimal
from pathlib import Path

WETH = "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2"

WITHDRAWAL_TOPIC = (
    "0x7fcf532c15f0a6db0bd6d0e038bea71d"
    "30d808c7d98cb3bf7268a95bf5081b65"
)

EVIDENCE = (
    Path(__file__).resolve().parent.parent
    / "A97B"
    / "evidence"
    / "bitquery_independent_crosscheck_v1"
    / "A97B_BITQUERY_CROSSCHECK_V1.csv"
)

def build(receipt, tx_hash):
    """
    Separate WETH unwrapping from ETH delivery.

    WETH withdrawal logs prove that the WETH contract
    emitted an unwrapping event. They do NOT independently
    prove the final ETH recipient.

    Existing Bitquery crosschecks are supplementary evidence,
    not substitutes for exact call traces.
    """
    withdrawals = []
    deliveries = []

    for log in receipt.get("logs", []):
        if str(log.get("address", "")).lower() != WETH:
            continue

        topics = log.get("topics", [])

        if len(topics) != 2:
            continue

        if str(topics[0]).lower() != WITHDRAWAL_TOPIC:
            continue

        if len(topics[1]) != 66:
            continue

        amount_hex = log.get("data", "")

        if not isinstance(amount_hex, str):
            continue

        if not amount_hex.startswith("0x"):
            continue

        raw = int(amount_hex, 16)
        withdrawer = "0x" + topics[1][-40:].lower()

        withdrawals.append({
            "kind": "WETH_WITHDRAWAL",
            "log_index": int(log["logIndex"], 16),
            "withdrawer": withdrawer,
            "weth_contract": WETH,
            "amount_wei": str(raw),
            "amount_eth": format(
                Decimal(raw) / Decimal(10**18), "f"
            ),
            "verification": "ETHEREUM_RECEIPT_LOG",
            "count_as_new_external_inflow": False
        })

    # Supplement with already-preserved A97B evidence.
    # No new chain attribution is inferred.
    if withdrawals and EVIDENCE.is_file():
        with EVIDENCE.open(
            encoding="utf-8-sig", newline=""
        ) as handle:
            for row in csv.DictReader(handle):
                if row.get("tx_hash", "").lower() != tx_hash.lower():
                    continue

                router = row.get(
                    "router_to_a97b_sender", ""
                ).lower()

                recipient = row.get(
                    "router_to_a97b_receiver", ""
                ).lower()

                if not any(
                    w["withdrawer"] == router
                    for w in withdrawals
                ):
                    continue

                deliveries.append({
                    "kind": "INTERNAL_ETH_REPORTED",
                    "sender": router,
                    "receiver": recipient,
                    "amount_display": row.get(
                        "router_to_a97b_eth_display", ""
                    ),
                    "precision": row.get(
                        "eth_transfer_precision",
                        "NOT_ASSESSED"
                    ),
                    "relationship": row.get(
                        "call_relationship",
                        "NOT_ASSESSED"
                    ),
                    "incident_attribution": row.get(
                        "incident_attribution",
                        "NOT_ESTABLISHED"
                    ),
                    "evidence_source": (
                        "A97B_BITQUERY_CROSSCHECK_V1.csv"
                    ),
                    "exact_internal_wei_verified": False,
                    "selectable": False
                })

    return {
        "weth_withdrawals": withdrawals,
        "reported_internal_eth": deliveries,
        "internal_trace_complete": False,
        "auto_save_internal_eth": False,
        "incident_attribution": "NOT_ESTABLISHED",
        "double_count_warning": (
            "WETH unwrapping and subsequent ETH delivery "
            "must not be counted as independent inflows."
        )
    }
