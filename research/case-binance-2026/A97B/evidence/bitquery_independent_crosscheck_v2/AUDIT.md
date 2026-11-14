# A97B Bitquery Independent Crosscheck v2 — Pilot Stage

## Scope

- Baseline: `eth_address_receipts_v1/A97B_ADDRESS_ETH_RETURN_V1.csv` (1,015 rows).
- Existing Bitquery checks excluded from the new-target set: 6 prior checks plus 10 pilot transactions re-queried here.
- New transactions queried in this stage: the first 50 of the remaining 999, in baseline order.
- This stage does not complete the remaining 949 transactions.

## Query conditions

- MCP tool: `bitquery-eth_tx_events`
- `event`: `Withdrawal`
- `only_successful`: `1`
- `format`: `rows`
- `limit`: `1000`
- Network: Ethereum mainnet
- WETH emitter: `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2`
- Expected event: `Withdrawal(address,uint256)`
- Expected topic0: `0x7fcf532c15f0a6db0bd6d0e038bea71d30d808c7d98cb3bf7268a95bf5081b65`

The 10 pilot transactions were re-read in one successful call. The 50 new transactions were queried in five successful batches of 10. Four earlier attempts were rejected by MCP parameter validation because of malformed transaction-hash strings; those attempts returned no chain data and are not counted as missing transactions. All 50 intended hashes were subsequently queried successfully.

## Completeness and reconciliation

- Pilot re-query: 10 requested hashes, 10 returned event rows, 10 distinct hashes.
- New-target pilot: 50 requested hashes, 50 returned event rows, 50 distinct hashes.
- All 60 returned rows identify the expected WETH emitter and Withdrawal signature.
- No duplicate transaction hashes or duplicate event rows were observed.
- Each returned row had `TxSuccess=1`, `CallSuccess=1`, `Reverted=0`, `Removed=0`, and `Parsed=1`.
- The decimal-string `wad` argument equals the unsigned integer decoded from the 32-byte raw `Data`.
- All 60 raw wei values equal the Blockscout ETH quantity converted to wei exactly.
- Batch response sizes were 10 rows, well below the configured 1,000-row limit; no response was limit-capped.
- Results: 60 MATCH, 0 MISMATCH, 0 UNVERIFIED.

No hash was absent from the successful responses. A missing hash in a future response must be recorded as UNVERIFIED unless a separate complete event-log response resolves it; absence from an event-filtered response alone is not evidence that the event did not occur.

## Evidence files

- `request_manifest.json`: exact requested hashes, effective query parameters, source hashes, and call/validation outcomes.
- `pilot10_events.json`: raw event rows from the pilot re-query.
- `batch_001_events.json` through `batch_005_events.json`: raw rows for the first 50 new transactions.
- `excluded_existing_16.csv`: the prior six and pilot ten excluded from the new-target set.
- `reconciliation.csv`: one comparison row per re-queried or newly queried transaction.
- `unverified.csv`: header-only register; no transactions were UNVERIFIED in this stage.
- `SHA256SUMS`: hashes for the v2 evidence files, excluding the checksum file itself.

The six earlier checks and their prior evidence were not modified. No other research files or pre-existing untracked directories were changed.
