# Shared Parent Funding — Evidence V1

Date: 2026-10-28
Status: ON-CHAIN VERIFIED / NO OWNERSHIP ATTRIBUTION

## Research Question

Do separate 547-sat creation transactions
share an observable upstream funding transaction?

## Verified Common Parent

TXID:
d7af4972d79e0b89c11a089320fd025446c9c567c4f75b19f8d73bffe7fda4ce

The parent transaction contains 264 outputs.

## Verified Funding Links

Link A:
- Parent output: 261
- Funding value: 9,088,600 sat
- Child TXID:
  de3178c6167aac05cfe47c841c566300debda028b64c6dfa3a8d908f353b5fe1
- Child date UTC: 2020-09-29
- Child 547-sat outputs: 228

Link B:
- Parent output: 262
- Funding value: 7,897,692 sat
- Child TXID:
  f71e2f979d577e2b0a84eec3c1c9b7b542e52c8db56cb7a2d9aa7e2de4ae759d
- Child date UTC: 2020-09-29
- Child 547-sat outputs: 363

## OBSERVED

- Two distinct child transactions spent separate
  outputs from the same parent transaction.
- Exact TXID and vout references were verified
  against the mempool.space transaction API.
- The two children created 591 outputs valued
  exactly 547 sat in total.
- Both children belong to the original 40
  creation transactions.

## UNKNOWN

- Whether both children had the same operator.
- Ownership of the parent transaction inputs.
- Why the 547-sat outputs were created.
- Whether the high-value BTC funding sources
  share ancestry with this network.

## Evidence Boundary

A shared parent transaction establishes
an observable transaction-level relationship.

It does not establish common beneficial ownership,
intent, or financial crime.

Source: https://mempool.space/tx/d7af4972d79e0b89c11a089320fd025446c9c567c4f75b19f8d73bffe7fda4ce
