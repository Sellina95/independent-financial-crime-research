# 2023 BTC Branch Fan-Out Verification V1

Date: 2026-10-28
Status: VERIFIED / NO OWNERSHIP ATTRIBUTION

## Objective

Trace the confirmed downstream UTXO branches
of the 2022 approximately 1,500 BTC consolidation.

Reference TXID:
64a87c3d7540876516d0bf274fcc4773c0d59d07e960287b1d1ddbf690335b08

## June 20, 2023 — First Branch

TXID:
39c4b92cd0ae0b74a9e88d7a37745b4920a8f47427d1750e7ea05bee8781999b

Outputs:
- vout 0: 10.29832430 BTC
- vout 1: 1,490.52764575 BTC

The 1,490.52764575 BTC UTXO was spent in:
acec271e3e5099d48441e0dbf1bb2498c8b0ac8688996fb5db37eca3fe121e63

That transaction had two inputs, including
another 0.39988087 BTC, and created:
- vout 0: 665.00000000 BTC
- vout 1: 825.92744720 BTC

## Small Branch — 10.29832430 BTC

Spending TXID:
2a56fcbeb4927de94bd09427fd8d944befe38ec83995743ce1c9a6dbe022288e

Confirmed UTC: 2023-06-20T19:44:56Z

- Inputs: 14
- Outputs: 47
- Other input value: 239.52238376 BTC
- Total output value: 249.81988034 BTC
- Fee: 82,772 sat

Individual output attribution is not possible
from this mixed-input transaction alone.

## 665 BTC Branch

Spending TXID:
9042f3fb20de4dd69ce3e34ebca9e0cba85918aa6c60ff8e76d690680e0f4fcc

Confirmed UTC: 2023-06-22T14:44:05Z

- Inputs: 1
- Outputs: 84
- Other inputs: 0 BTC
- Total outputs: 664.99889349 BTC
- Fee: 110,651 sat
- Largest output: 146.25735489 BTC

## 825 BTC Branch

825.92744720 BTC was spent in:
97bfc4976d8c4d3990701450db9192782c528d12e78c543901988610ead9c8a2

That transaction used one input and created
one output of 825.92740280 BTC.

Destination:
3KfzraCDBMfKMJL4QaTDigMc5m6B2AqgEG

Next spending TXID:
ce56f969f85622f1182d34c8f5afd46962527c3bf9121de07b7e6c811bc40119

Confirmed UTC: 2023-06-22T16:36:15Z

- Inputs: 1
- Outputs: 91
- Other inputs: 0 BTC
- Total outputs: 825.92621900 BTC
- Fee: 118,380 sat
- Largest output: 192.08000000 BTC

## Repeated Destination

Address:
3KfzraCDBMfKMJL4QaTDigMc5m6B2AqgEG

This address received distinct UTXOs valued:
- 10.29832430 BTC
- 665.00000000 BTC
- 825.92740280 BTC

The three UTXOs were not observed to be
co-spent in a single immediate transaction.

## OBSERVED

- Exact parent TXID:vout spending links verified.
- 665 BTC and 825.92740280 BTC were each
  consumed in separate single-input transactions.
- These created 84 and 91 outputs respectively.
- Repeated destination address verified.

## UNKNOWN

- Common beneficial ownership.
- Reason for the output distributions.
- Whether downstream outputs later reconverge.
- Ultimate destination of the funds.
- Any criminal association.

## Limitations

- Public mempool.space API verification.
- No independent Bitcoin node validation.
- Address reuse does not establish identity.
- No downstream ownership attribution.
- No claim of illicit activity.

## Next Research Question

Do the 84-output and 91-output transactions
share distinctive distribution patterns
or common destination scripts?

Compare exact output amounts and scripts
before expanding further downstream.

Preserve existing research artifacts.
