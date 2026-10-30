# Binance Security Incident 2026
## Evidence Checkpoint V1

Research status: INITIAL ON-CHAIN RECONSTRUCTION
Evidence level: USER-CAPTURED ETHERSCAN + CSV CROSS-CHECK
Research date: 2026-10-30

## Research Question

Can public on-chain evidence reconstruct the Binance
security incident and subsequent fund movements?

No attribution of real-world identity is attempted.

## 1. Initial Transaction

Network: Ethereum Mainnet
Block: 26300770
Timestamp: 2026-10-29 20:24:23 UTC

Transaction:
0x53bd38b816c23e74134786c29a8c18d792777998a3b9326047b583100e88e2f3

Transaction caller:
0x7C8601d4645b93cea45F71e118A729332e6B5CA0

Interacted with:
0x28C6c06298d514Db089934071355E5743bf21d60

ETH recipient:
0x5227f603C1eE34CE3C06eFe6477003BDfCCB2f8c

Observed internal ETH transfer:
167,464.247856558836135296 ETH

Etherscan status: Success

Additional ERC-20 transfers reported in the same
transaction, including approximately 1.615B USDT.

Note:
The transaction caller and asset sender are different.
Execution traces and authorization mechanisms have
not yet been independently validated.

## 2. Major Subsequent ETH Transfer

Transaction:
0x551d7961652e6d9835b11988908adf86ebe480badb4ce2d7d52193b2b1b02c76

Block: 26300842
Timestamp: 2026-10-29 20:38:47 UTC

From:
0x5227f603C1eE34CE3C06eFe6477003BDfCCB2f8c

To:
0x8532FA14ACAf483729C449b8458aedDb900543D4

Value: 195,460 ETH
Etherscan status: Success

## 3. Additional ETH Transfer

Transaction:
0x48186565bdd78b13e516cf5deaf8431d839eed211205718aa90cdb44ae64e84a

Timestamp: 2026-10-30 01:14:11 UTC

From:
0x5227f603C1eE34CE3C06eFe6477003BDfCCB2f8c

To:
0x8532FA14ACAf483729C449b8458aedDb900543D4

CSV-recorded value: 2,000 ETH

Transaction status requires independent confirmation.

## 4. Recipient Wallet Observation

Address:
0x8532FA14ACAf483729C449b8458aedDb900543D4

User-provided Etherscan CSV:
55 incoming transactions.
0 outgoing normal transactions.

CSV total incoming:
197,460.004859337646469657 ETH

User-observed Etherscan balance:
197,460.004859337646469657 ETH

CSV time coverage:
2026-10-29 20:38:47 UTC
through 2026-10-30 05:58:47 UTC

The balance observation is not proof of freezing,
permanent custody, or absence of internal transfers.

## 5. Evidence Classification

OBSERVED:
- Transaction records reproduced from user-supplied
  Etherscan pages and exports.
- Successful 195,460 ETH transfer reported by Etherscan.
- Recipient wallet balance matching CSV receipts
  at the captured observation point.

INFERRED:
- Funds from the initial sweep likely contributed
  to the subsequent large ETH transfer.
- The two ETH inflows may represent consolidation.

UNKNOWN:
- Complete incident origin and authorization path.
- Full internal transaction traces.
- Complete ERC-20 fund movement graph.
- Token-level freeze contracts and balances.
- Actual controller of each wallet.
- Complete multi-chain losses.
- Any subsequent movement after observation.

## 6. Research Restrictions

- Etherscan address labels are third-party attribution.
- Address labels do not prove criminal identity.
- USD valuations are observation-time estimates.
- Do not infer causality from amount similarity alone.
- Ethereum account balances do not provide UTXO
  provenance for individual ETH units.
- No production findings or criminal allegations.
- Bitcoin 547-sat research remains independent.

## 7. Next Verification

Priority:
Validate the initial USDT transfer using Ethereum
ERC-20 event logs and the token contract.

Then inspect freeze-related contract calls separately.

Only verified transaction hashes and contract events
may support confirmed movement or freeze claims.

## Sources

Initial transaction:
https://etherscan.io/tx/0x53bd38b816c23e74134786c29a8c18d792777998a3b9326047b583100e88e2f3

Major subsequent transaction:
https://etherscan.io/tx/0x551d7961652e6d9835b11988908adf86ebe480badb4ce2d7d52193b2b1b02c76

Additional transaction:
https://etherscan.io/tx/0x48186565bdd78b13e516cf5deaf8431d839eed211205718aa90cdb44ae64e84a

Exploiter 8:
https://etherscan.io/address/0x8532FA14ACAf483729C449b8458aedDb900543D4

These URLs are source pointers, not independent
node-level verification.
