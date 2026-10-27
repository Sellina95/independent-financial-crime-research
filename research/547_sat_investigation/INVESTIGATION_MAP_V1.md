# 547-sat Investigation — Fixed Investigation Map V1

Date: 2026-10-27
Status: BASELINE FROZEN
Scope: Observed on-chain relationships, not ownership attribution.

## Central Transaction
TXID:
64a87c3d7540876516d0bf274fcc4773c0d59d07e960287b1d1ddbf690335b08

- 78 inputs
- 46 inputs of 547 sat
- 32 non-547-sat inputs
- Approximately 1,500.726 BTC total input value

## Backward Provenance
- 46 dust UTXOs
- 40 distinct creation transactions
- 49 distinct creation-transaction funding addresses
- 1 verified direct UTXO link between 2 of the 40 transactions
- 38 transactions with no direct link found within this set
- Direct address overlap with large inputs: 0
- Limited ancestor TXID overlap: 0

## Forward Outspend Inventory
Scope: All 547-sat outputs created by the 40 transactions.

- Total outputs: 17,182
- Spent outputs: 11,415
- Unspent outputs: 5,767
- Distinct spending transactions: 6,975

## Exploratory Sample
First 100 spending TXIDs sorted lexicographically.

- 98 transactions include non-547-sat inputs
- 39 include at least 1 BTC in other inputs
- 9 include at least 100 BTC in other inputs

WARNING:
This is not a random or representative sample.
Do not generalize its rates to all 6,975 spending transactions.

## Research Questions
Q1: Who controlled the funding sources of the 547-sat transfers?
Q2: Why were these outputs distributed?
Q3: Is there any historical funding relationship between
    the senders and the approximately 1,500 BTC transaction?
Q4: How unusual is the 1,500 BTC transaction among
    the observed spending transactions?

## Evidence Boundaries
OBSERVED: On-chain UTXO transfers and spending relationships.
INFERRED: Possible shared funding operations, subject to testing.
UNKNOWN: Sender identity, motivation, ownership and attribution.

The map is the fixed V1 baseline.
Later findings must be added in separate versioned records.
