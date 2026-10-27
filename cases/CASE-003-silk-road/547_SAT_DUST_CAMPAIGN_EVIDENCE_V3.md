# CASE-003 — 547-Satoshi Message Campaign
## Evidence Freeze V3 — Historical Distribution Structure

Date: 2026-10-27
Status: INTERIM EVIDENCE / NOT FINAL ATTRIBUTION
Scope: STEP 5D
Previous evidence: V0, V1, V2 preserved.

## Research Question

Did the historical high-value Bitcoin transactions
share observable distribution structures or direct
transaction-to-transaction funding relationships?

## Scope

Consolidation transaction:
64a87c3d7540876516d0bf274fcc4773c0d59d07e960287b1d1ddbf690335b08

- Overlapping non-dust inputs: 23
- Historical origin transactions: 22
- Historical origin period: 2017-08 to 2019-08
- Data source: mempool.space public transaction API

## OBSERVED — Transaction Structures

22 historical transactions exhibited 11 distinct
input/output count structures.

Most common structures:

- 3 inputs / 13 outputs: 7 transactions
- 3 inputs / 14 outputs: 3 transactions
- 3 inputs / 8 outputs: 3 transactions
- 1 input / 1 output: 2 transactions

Other structures occurred once each.

The repetition is an observed structural similarity,
not proof of automation, common ownership, or custody.

## OBSERVED — Repeated Funding Addresses

Seven upstream input addresses appeared in more
than one historical origin transaction.

Address | Origin transaction count

- 3JjPf13Rd8g6WAyvg8yiPnrsdjJt1NP4FC | 9
- 378p3u4RN1HTEWFkiTK27zuBWbx6eLSX6p | 8
- 3DLRBj8bqGMgB6vcKgWeQLqSV4eDUMvDGw | 6
- 1Ej4Jm8J83tKG4wUAbikNF3rQoGckH4Emp | 5
- 1Dk7S7v3hDBVcS93LPPKWpCSGbL63Ewwn | 3
- 3HMS9df28gpPkRggoGJuQ6sJ1GtKxeDMCb | 3
- 1JcNS4m5ME4JZAZcQ5Z5sSQ5UnaRcSHUwR | 2

Counts refer to origin transactions, not unique
recipients or independent operators.

## OBSERVED — Direct Transaction Chains

Four parent outpoints were consumed by another
transaction within the 22-transaction sample.

Link 1:
19b52d15c37af195b5dcd865aa1ed58a53eecace2a4c373a1ce0560786fbd41b:8
->
40ab7625cf4290692a43d864d8c319c7a400975fb7c588ed75a995927cab406e

Links 2 and 3:
4a9f4a51f7262d78eb62a10b2dbf963444c488906cd5cb0a70d44037c39bda28:3
4a9f4a51f7262d78eb62a10b2dbf963444c488906cd5cb0a70d44037c39bda28:6
->
bc3df415342ec1a568b0aa672a68839f203be3ef5f1268a7c42c9f27f62ff2c9

Link 4:
4a9f4a51f7262d78eb62a10b2dbf963444c488906cd5cb0a70d44037c39bda28:7
->
8aafef602724fdb9a46b36255db5d06556bf568669b1e06003b9532dbf6aa3bd

These are four UTXO links across three
distinct parent-child transaction pairs.

## OBSERVED — Same-Block Groups

Block 488259:
- 09f0357c6a6f95d78dd235001b38b6421690b7625a6aea4b68cc10c354bfe8ce
- bc3df415342ec1a568b0aa672a68839f203be3ef5f1268a7c42c9f27f62ff2c9

Block 490361:
- 40ab7625cf4290692a43d864d8c319c7a400975fb7c588ed75a995927cab406e
- e89639c1a412ef763481d224a1172b6b093f25c19afa020b9dd0d2c78e318c69

Same-block inclusion does not prove
common ownership or coordination.

## INFERRED

- Some historical transactions were connected
  through direct UTXO spending relationships.
- Repeated funding addresses and transaction
  structures warrant further investigation.
- These observations are compatible with multiple
  wallet-management and custody explanations.

The evidence types may overlap and must not
be counted as independent confirmations.

## UNKNOWN

- Whether the transactions had one operator.
- Whether they belonged to an exchange or custodian.
- Whether they reflect automated wallet operations.
- The identity of any real-world owner.
- Whether the 547-sat sender controlled the
  high-value funds.
- Whether any funds were connected to a crime.
- Whether the activity relates to Silk Road
  or any named individual.

## DISPROVEN

No ownership, custody, or criminal hypothesis
has been disproven by STEP 5D.

## Limitations

- One public API provider was used.
- The sample covers selected historical origins,
  not complete wallet history.
- Input/output counts alone are not attribution.
- Shared input addresses do not prove one owner.
- Direct UTXO links establish transaction-level
  movement, not real-world identity.
- No independent node verification yet.

## Next Step — STEP 5E

Compare competing explanations for the observed
2017 distribution and 2022 consolidation:

H1: Single wallet/operator UTXO management.
H2: Exchange or custodial wallet management.
H3: Other multi-party or specialized transaction structure.

Assess what evidence supports, weakens, or
cannot distinguish each hypothesis.

Do not assign criminal attribution without
independent corroborating evidence.

## Freeze Boundary

V3 records historical transaction structure
observations only.

V0, V1, V2 remain unchanged.
