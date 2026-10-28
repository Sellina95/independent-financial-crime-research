# 1,500 BTC Consolidation & Forward Flow — Verified V1

Date: 2026-10-28
Status: ON-CHAIN VERIFIED / NO OWNERSHIP ATTRIBUTION

## 1. Research Objective

Reconstruct the observed consolidation of 547-sat
UTXOs with high-value BTC inputs, and trace the
resulting output to its next confirmed spending
transaction.

Scope is limited to observable Bitcoin transactions.
Sender identity, beneficial ownership, and intent
remain unknown.

## 2. Reference Transaction

TXID:
64a87c3d7540876516d0bf274fcc4773c0d59d07e960287b1d1ddbf690335b08

Confirmed UTC: 2022-04-22T21:18:11Z

- Total inputs: 78
- Total outputs: 1
- Total input value: 1,500.72709382 BTC
- Total output value: 1,500.72603880 BTC
- Mining fee: 105,502 sat

Input composition:

- 46 inputs of exactly 547 sat
- Combined dust value: 0.00025162 BTC
- 32 non-547-sat inputs
- Combined non-dust value: 1,500.72684220 BTC

All 46 dust inputs were verified against the
original 40 creation transactions.

## 3. Shared Input Scripts

Exact scriptPubKey comparison found:

- Shared input scripts: 22
- Dust inputs at those scripts: 38
- Non-547 inputs at those scripts: 23
- Non-547 value at shared scripts:
  1,237.47524195 BTC

This establishes observable address/script reuse
between dust and non-dust UTXOs consumed in the
same reference transaction.

It does not prove that the original dust sender
controlled the high-value BTC.

## 4. Consolidated Output

Output index: 0

Amount: 1,500.72603880 BTC

Destination:
bc1qzd8c8h8dcgwuy5zdafdzdce2ap0nayf8v3xrez

Script type: v0_p2wpkh

The reference transaction consumed 78 inputs
and created one new output.

## 5. Verified Forward Spending

The reference output was subsequently spent.

Next TXID:
39c4b92cd0ae0b74a9e88d7a37745b4920a8f47427d1750e7ea05bee8781999b

Confirmed UTC: 2023-06-20T19:36:49Z

- Reference output consumed at input index: 1
- Total transaction inputs: 2
- Total transaction outputs: 2
- Total input value: 1,500.82603066 BTC
- Total output value: 1,500.82597005 BTC
- Mining fee: 6,061 sat

Output 0:
- 10.29832430 BTC
- 3KfzraCDBMfKMJL4QaTDigMc5m6B2AqgEG

Output 1:
- 1,490.52764575 BTC
- bc1qa7rc5skutrhrq4vktuswhu6rr4fpjje8rh9axc

The next transaction contained another input
of 0.09999186 BTC.

## 6. Evidence Classification

OBSERVED:

- The 46 dust UTXOs and 32 non-dust UTXOs
  were jointly consumed in the reference TX.
- 22 exact input scripts appeared in both groups.
- The reference TX created one output.
- That output was spent in the 2023 transaction.
- The 2023 transaction created two outputs.

UNKNOWN:

- Identity of the dust sender.
- Identity of the high-value BTC controller.
- Whether the original funding sources shared
  a beneficial owner.
- Purpose of the consolidation.
- Final ownership and destination of the funds.
- Any connection to criminal conduct.

## 7. Critical Interpretation Boundary

Co-spending is not proof of common origin.

A Bitcoin transaction combines inputs into
new outputs. Individual satoshis cannot be
uniquely assigned to particular outputs using
this transaction evidence alone.

The 1,490.52764575 BTC output must not be
described as exclusively originating from
the reference transaction's funds because
the 2023 transaction also consumed another input.

## 8. Sources

Reference:
https://mempool.space/tx/64a87c3d7540876516d0bf274fcc4773c0d59d07e960287b1d1ddbf690335b08

Forward spending:
https://mempool.space/tx/39c4b92cd0ae0b74a9e88d7a37745b4920a8f47427d1750e7ea05bee8781999b

Public data provider: mempool.space API

Verification performed using transaction inputs,
prevout scripts, output values, exact UTXO references,
and outspend records.

Independent Bitcoin node verification not performed.

## 9. Next Research Priority

Trace the two outputs of the 2023 transaction,
with priority on the 1,490.52764575 BTC output.

Maintain exact TXID:vout provenance.

Do not infer ownership, intent, or illicit activity
without additional independent evidence.

Preserve existing frozen research artifacts.
