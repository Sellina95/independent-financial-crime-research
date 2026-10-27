# 547-sat Sender Provenance Investigation — V1

Date: 2026-10-27
Status: IN PROGRESS

## Objective
Identify the funding sources behind the 547-sat transfers
and test whether they have a historical funding relationship
with the high-value BTC inputs in the 2022 consolidation.

## Consolidation Transaction
TXID:
64a87c3d7540876516d0bf274fcc4773c0d59d07e960287b1d1ddbf690335b08

OBSERVED:
- 78 inputs total
- 46 inputs of exactly 547 sats
- 32 other inputs
- Approximately 1,500.726 BTC total input value

## Sender Provenance
OBSERVED:
- 46 dust inputs originate from 40 distinct transactions.
- 49 distinct funding input addresses identified.
- Direct address overlap with high-value inputs: 0.
- Limited historical ancestor TXID overlap: 0.

## Sender Network
OBSERVED:
- 40 source transactions examined.
- 1 direct UTXO link identified.
- 2 source transactions form one connected component.
- 38 source transactions have no direct links to
  other transactions within the examined set.

Verified link:
cd83a6cba2c78b0c5feb7ad249b8ca290aaa58ea4ebaaea05933e1c757663e39:607
->
5e0bcf53b9e51d68fc91b622ceb87ca77efd32e631392f9e893ff6eb36d4b015

## Interpretation
OBSERVED:
The two transactions share an exact UTXO spending relationship.

UNKNOWN:
- Identity of the actual sender(s).
- Whether the source transactions share an operator.
- Sender motivation.
- Historical funding relationship with the high-value BTC.
- Whether additional connections exist through intermediate transactions.

No criminal attribution or ownership conclusion is supported.

## Next Step
Trace non-547-sat outputs and intermediate transactions
between the 40 source transactions.

Reconstruct connected funding chains using exact outpoints.

Then compare these reconstructed funding paths against
the ancestry of the 32 high-value inputs.

Do not modify unrelated research or GCF.
