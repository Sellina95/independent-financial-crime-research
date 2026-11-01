# AXIOM — Bitcoin 11-TX Input/Output Audit V1

## Scope
- 11 previously observed Bitcoin transactions.
- Reported source address: `bc1qm34lsc65zpw79lxes69zkqmk6ee3ewf0j77s3h`
- Reported receiving address: `bc1q0mtc2f5agpkvlq6hhahmfr3hlr55kyfjhl2mnm`
- Data: mempool.space Bitcoin transaction API.

## On-chain results
- Receiver outputs: 18,270.20000000 BTC
- Inputs from source address: 18,333.70635832 BTC
- Inputs from other addresses: 0.00000000 BTC
- Other outputs: 63.50277682 BTC
- Transaction fees: 0.00358150 BTC
- Unique spent input outpoints: 513
- Distinct block hashes: 1
- Distinct block timestamps: 1
- Per-transaction conservation: PASS
- Aggregate conservation: PASS
- Duplicate input outpoint check: PASS

## Interpretation limits
- Receiver outputs are observed transfers, not confirmed losses.
- Inputs from the source address do not automatically
  establish the economic origin of each receiver output.
- Other outputs cannot automatically be labeled change.
- A shared block timestamp is not exact transaction creation time.
- Binance ownership is not independently verified.
- Unauthorized withdrawal status remains UNVERIFIED.
- No victim loss amount is certified by this audit.

## Decision
- Gate 2: OPEN.
- Bitcoin source-to-receiver transaction structure audited.
- Next: independent wallet ownership and incident attribution.
