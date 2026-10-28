# Shared Funding Paths — Depth-2 Verification V1

Date: 2026-10-28
Status: ON-CHAIN VERIFIED / NO OWNERSHIP ATTRIBUTION

## Objective

Verify exact UTXO relationships among the
previously identified 547-sat creation transactions.

## Verification

Provider: mempool.space public transaction API

- Exact UTXO edges verified: 5
- Unique transactions checked: 7
- Verification status: PASS
- Original 547-sat creation transactions connected: 4
- Identified connected groups: 2

## Group A — Shared Parent

1d4e3c27cba7006c1ae93a61cd7e4f96c39c19f618ad10dca9bd4127d009a833:324
->
d7af4972d79e0b89c11a089320fd025446c9c567c4f75b19f8d73bffe7fda4ce

Funding value: 22,176,250 sat

The parent transaction then supplied:

Output 261 — 9,088,600 sat
->
de3178c6167aac05cfe47c841c566300debda028b64c6dfa3a8d908f353b5fe1

Output 262 — 7,897,692 sat
->
f71e2f979d577e2b0a84eec3c1c9b7b542e52c8db56cb7a2d9aa7e2de4ae759d

These child transactions created 228 and 363
outputs valued exactly 547 sat, respectively.

## Group B — Sequential Funding

b8b3e7e154c190e090327d469fa8b5e4d2cbf5e3b94e7b47e55ed502cb505a77:607
->
cd83a6cba2c78b0c5feb7ad249b8ca290aaa58ea4ebaaea05933e1c757663e39

Funding value: 1,802,789,781 sat

cd83a6cba2c78b0c5feb7ad249b8ca290aaa58ea4ebaaea05933e1c757663e39:607
->
5e0bcf53b9e51d68fc91b622ceb87ca77efd32e631392f9e893ff6eb36d4b015

Funding value: 1,802,117,344 sat

## OBSERVED

All five parent-output to child-input references
were verified using exact TXID, vout and value.

## UNKNOWN

- Common operator or beneficial ownership.
- Whether groups A and B share a funding source.
- Whether dust funding and high-value BTC funding
  share a common historical source.
- Purpose or criminal intent.

## Limitations

Transaction-level UTXO relationships do not
prove common ownership or identity.

Where transactions have multiple inputs, the
individual satoshis cannot be uniquely attributed
to particular outputs using these edges alone.

Verification used one public API provider.
No independent Bitcoin node verification yet.

## Next Step

Analyze the original 40 creation transactions
for repeated funding and distribution structures.

Preserve all previously frozen evidence.
