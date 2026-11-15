import json
import os
import re
import urllib.request
from datetime import datetime, timezone
from decimal import Decimal

TX_RE = re.compile(r"^0x[0-9a-fA-F]{64}$")

TRANSFER_TOPIC = (
    "0xddf252ad1be2c89b69c2b068fc378daa"
    "952ba7f163c4a11628f55a4df523b3ef"
)

def rpc(method, params):
    url = os.environ.get("ALCHEMY_RPC_URL", "")
    if not url.startswith("https://"):
        raise ValueError("HTTPS Ethereum RPC is required")

    payload = json.dumps({
        "jsonrpc": "2.0",
        "id": 1,
        "method": method,
        "params": params
    }).encode()

    req = urllib.request.Request(
        url,
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST"
    )

    try:
        with urllib.request.urlopen(req, timeout=15) as response:
            data = json.load(response)
    except Exception:
        raise ValueError("Ethereum RPC request failed") from None

    if data.get("error"):
        raise ValueError("Ethereum RPC returned an error")

    return data.get("result")


def token_decimals(contract, block):
    try:
        result = rpc("eth_call", [
            {"to": contract, "data": "0x313ce567"},
            block
        ])
        decimals = int(result, 16)
        if not 0 <= decimals <= 36:
            return None
        return decimals
    except (ValueError, TypeError, OverflowError):
        return None


def token_symbol(contract, block):
    try:
        result = rpc("eth_call", [
            {"to": contract, "data": "0x95d89b41"},
            block
        ])
        if not result or result == "0x":
            return "ERC20"

        raw = bytes.fromhex(result[2:])

        # Standard ABI-encoded dynamic string
        if len(raw) >= 96 and int.from_bytes(raw[:32], "big") == 32:
            size = int.from_bytes(raw[32:64], "big")
            if 0 < size <= 64 and len(raw) >= 64 + size:
                symbol = raw[64:64 + size].decode("utf-8")
                if symbol.isprintable() and 1 <= len(symbol) <= 30:
                    return symbol

        # Legacy bytes32 string
        if len(raw) == 32:
            symbol = raw.rstrip(b"\x00").decode("utf-8")
            if symbol.isprintable() and 1 <= len(symbol) <= 30:
                return symbol
    except (ValueError, UnicodeError, TypeError, OverflowError):
        pass

    return "ERC20"


def display_amount(raw, decimals):
    value = Decimal(raw) / (Decimal(10) ** decimals)
    return format(value, "f")


def lookup_transaction(tx_hash):
    if not TX_RE.fullmatch(tx_hash):
        raise ValueError("Invalid Ethereum transaction hash")

    tx_hash = tx_hash.lower()

    if rpc("eth_chainId", []) != "0x1":
        raise ValueError("STOP: RPC is not Ethereum Mainnet")

    tx = rpc("eth_getTransactionByHash", [tx_hash])
    receipt = rpc("eth_getTransactionReceipt", [tx_hash])

    if not tx or not receipt:
        raise ValueError("Transaction or receipt not found")

    if not tx.get("blockNumber") or not receipt.get("blockNumber"):
        raise ValueError("Transaction is not confirmed")

    if tx["blockHash"] != receipt.get("blockHash"):
        raise ValueError("Transaction/receipt block mismatch")

    if tx["blockNumber"] != receipt["blockNumber"]:
        raise ValueError("Transaction/receipt height mismatch")

    if receipt.get("status") != "0x1":
        raise ValueError("Transaction did not succeed")

    block = rpc(
        "eth_getBlockByNumber",
        [tx["blockNumber"], False]
    )

    if not block or block.get("hash") != tx["blockHash"]:
        raise ValueError("Block verification failed")

    block_number = int(tx["blockNumber"], 16)

    stamp = datetime.fromtimestamp(
        int(block["timestamp"], 16),
        tz=timezone.utc
    ).strftime("%Y-%m-%dT%H:%M:%S")

    candidates = []

    # Only top-level native ETH transfer.
    # Internal ETH transfers require a separate trace.
    native_value = int(tx.get("value", "0x0"), 16)

    if native_value > 0 and tx.get("to"):
        candidates.append({
            "kind": "NATIVE_ETH",
            "log_index": None,
            "from": tx["from"].lower(),
            "to": tx["to"].lower(),
            "asset": "ETH",
            "contract": "",
            "amount": display_amount(native_value, 18),
            "raw_amount": str(native_value),
            "decimals_verified": True
        })

    metadata_cache = {}

    for log in receipt.get("logs", []):
        topics = log.get("topics", [])

        if len(topics) != 3:
            continue

        if topics[0].lower() != TRANSFER_TOPIC:
            continue

        if len(topics[1]) != 66 or len(topics[2]) != 66:
            continue

        contract = log["address"].lower()

        if contract not in metadata_cache:
            metadata_cache[contract] = (
                token_decimals(contract, tx["blockNumber"]),
                token_symbol(contract, tx["blockNumber"])
            )

        decimals, symbol = metadata_cache[contract]
        raw_amount = int(log["data"], 16)

        candidates.append({
            "kind": "ERC20_TRANSFER",
            "log_index": int(log["logIndex"], 16),
            "from": "0x" + topics[1][-40:].lower(),
            "to": "0x" + topics[2][-40:].lower(),
            "asset": symbol,
            "contract": contract,
            "amount": (
                display_amount(raw_amount, decimals)
                if decimals is not None else None
            ),
            "raw_amount": str(raw_amount),
            "decimals_verified": decimals is not None
        })

    # Existing DRAFT schema cannot distinguish repeated identical
    # Transfer logs. Block ambiguous candidates from auto-fill.
    identities = {}

    for item in candidates:
        identity = (
            item["from"],
            item["to"],
            item["contract"] or "ETH",
            item["raw_amount"]
        )
        identities[identity] = identities.get(identity, 0) + 1

    for item in candidates:
        identity = (
            item["from"],
            item["to"],
            item["contract"] or "ETH",
            item["raw_amount"]
        )
        item["selectable"] = (
            item["decimals_verified"]
            and identities[identity] == 1
            and item["amount"] is not None
            and Decimal(item["amount"]) > 0
        )

    return {
        "tx_hash": tx_hash,
        "chain_id": 1,
        "block": block_number,
        "utc": stamp,
        "receipt_status": "SUCCESS",
        "incident_attribution": "UNKNOWN",
        "internal_eth_covered": False,
        "transfers": candidates
    }
