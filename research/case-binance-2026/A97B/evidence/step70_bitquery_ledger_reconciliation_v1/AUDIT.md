# A97B STEP70–Bitquery Reconciliation

## Result

The captured Bitquery response contains 1,274 outgoing transfer rows. Against the 1,186 STEP70 ledger rows, normalization by transaction hash, asset contract (with native ETH represented as `native`), raw amount, and recipient yields 1,184 matching distinct keys and 90 Bitquery-only keys. STEP70 contains two additional occurrences of keys already present once in Bitquery; they are duplicate ledger rows, not two missing on-chain transfers.

The 90 Bitquery-only keys correspond to 90 distinct transaction hashes. All are later than the ledger's actual last row at block 26,304,617: 67 have positive raw amounts and are later than the audit's declared end block 26,309,096; 23 have raw amount zero, of which 8 fall within the declared block interval and 15 are later than it. No positive-amount Bitquery-only row falls within the declared interval. The cause of the 8 zero-amount rows within that interval is not established.

## Inputs and query scope

- `bitquery_a97b_outgoing.json` is the actual columnar response captured from `bitquery-eth_transfers_out`, not a reconstruction.
- The original query was for A97B, after `2026-10-29 22:39:35`, all assets, `include_internal=1`, `limit=10000`, newest first, `format=columnar`. It had no explicit `before_time`, block bound, or token filter.
- The response has 1,274 rows, 1,274 distinct transaction hashes, blocks 26,302,230–26,330,268, and times 2026-10-30T01:17:47Z–2026-11-02T23:05:23Z. It is below the requested 10,000-row limit. Every returned row has `Internal=0`.
- The response schema does not include a sender field. The CSV therefore records the A97B address as the query scope and leaves the sender as `NOT_RETURNED`; it does not claim that a sender value was directly returned by Bitquery.
- The historical later-time and older-cursor follow-ups reportedly returned no rows, but their raw responses were not preserved. Both follow-up requests used `include_internal=0`, unlike the primary query's `include_internal=1`; they are not treated as proof of complete pagination for the primary query. See `query_conditions.json`.

## STEP70 coverage and unmatched records

The STEP70 audit declares blocks 26,301,444–26,309,096 and `pagination_complete=true`. Its 1,186 ledger rows actually span blocks 26,302,230–26,304,617, 2026-10-30T01:17:47Z–2026-10-30T09:16:35Z. The captured Bitquery response extends beyond that actual last row.

The two repeated STEP70 records are:

| Transaction | Asset contract | Raw amount | Recipient | Repeated STEP70 unique IDs |
|---|---|---:|---|---|
| `0x4dae9089b113b4dfeb2a30926c23342e83143f781028a876fc4a6934289cf26c` | `0x152649ea73beab28c5b49b26eb48f7ead6d4c898` | `19991280659376130122422` | `0x517f451b0a9e1b87dc0ae98a05ee033c3310f046` | log 37 and log 421 |
| `0x791e4ba4d7a78079fe8d83d7e8ed93a4515d794809a4c47ac3e8df234f717d7c` | `0x0f5d2fb29fb7d3cfee444a200298f468908cc942` | `323796184738087318345142` | `0x8661ae7918c0115af9e3691662f605e9c550ddc9` | log 41 and log 432 |

`transfer_reconciliation.csv` includes each Bitquery row and the repeated STEP70 ledger occurrence as a separate row, preserving the original row identifiers and classification. The Bitquery response's `Amount_Raw` is used for exact token-unit comparisons; display amounts are not used as equality keys.

## Native ETH and token-symbol handling

There are 20 native ETH rows, identified by an empty `Contract` field and the `ETH` currency label. Four crosswalk transactions have corresponding rows that match STEP70 by transaction, recipient, and exact raw amount; the other 16 are after block 26,309,096. All 20 have `Internal=0`.

An `ETH` currency symbol alone is not treated as native ETH: contract-addressed tokens remain separate assets. The normalized CSV retains each contract and the non-ASCII-symbol flag. Amounts of different tokens are never summed.

## Zero-value rows, routing, and attribution

All 23 zero-raw-amount unmatched rows are explicitly identified in the CSV; the 8 within the declared block interval are `UNEXPLAINED_ZERO_RAW_IN_DECLARED_RANGE`. Their cause is unknown, and they are not represented as positive-value movements. The 15 zero rows after the declared interval are classified as outside that bound.

The two repeated ledger entries are token-transfer records associated with transactions whose transaction-level transfer output also shows router, WETH, and ETH legs. These are separate legs of transaction activity, not amounts to add together as independent incident proceeds. The supporting transaction responses are preserved separately. The two WETH `Withdrawal` event values are raw wei; the `eth_tx_transfers` amounts are displayed to eight decimal places and are therefore `PRECISION_LIMITED`, not exact equality evidence. Co-occurrence in one transaction does not by itself establish the incident provenance of funds or a complete causal attribution.

## Limitations and status

- `EXPLAINED`: the 90 positive-amount Bitquery-only records are after STEP70's declared end block; the 23 zero-amount records are separately classified, including the 8 whose cause is unknown.
- `EXPLAINED`: the two STEP70-only occurrences are duplicate ledger rows, not distinct missing transfers.
- `EXPLAINED`: 16 native ETH rows are outside the declared STEP70 block bound; four match the existing crosswalk.
- `DATA_LIMITATION`: the historical follow-up raw responses are unavailable, and the follow-up requests did not use the primary query's `include_internal` setting. The captured response did not reach its 10,000-row limit, but the available evidence does not establish an unbounded or fully paginated history beyond the captured result.
- `UNKNOWN`: why the eight zero-amount rows within the declared block interval were omitted from the STEP70 ledger.
- `UNKNOWN`: incident-fund fraction, ownership of counterparties, and any complete conservation or causal path. No transaction is attributed to the Binance incident merely by amount, timing, or address reuse.

## Source integrity

The source ledger, STEP70 audit, and their pages were read only and were not copied over or modified. Their existing manifest records the ledger SHA-256 as `0939350402418eb636c3105a9cf9891061af85e4e57947fc97793006dfa5ac45`. The primary Bitquery response SHA-256 is recorded in `query_conditions.json`; `SHA256SUMS` covers the files in this evidence directory.
