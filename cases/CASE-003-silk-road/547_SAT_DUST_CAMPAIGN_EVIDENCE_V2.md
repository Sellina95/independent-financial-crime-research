# CASE-003 — 547-Satoshi Message Campaign
## Evidence Freeze V2 — Historical Funding Linkage

Status: INTERIM / NOT FINAL
Freeze date: 2026-10-27
Scope: STEP 5A, 5B, 5C
Previous evidence: V0 and V1 remain unchanged.

## 1. Research Question

Were the Bitcoin addresses that received 547-satoshi
message outputs already linked through earlier funding
transactions before the April 2022 consolidation?

## 2. Transaction Anchor

Consolidation TXID:
64a87c3d7540876516d0bf274fcc4773c0d59d07e960287b1d1ddbf690335b08

## 3. STEP 5A — Message Transaction Timeline

OBSERVED:
- 40 distinct message-bearing source transactions fetched.
- 40/40 successfully retrieved.
- Transaction dates: 2020-08-06 through 2021-01-27 UTC.
- 49 distinct input funding addresses.
- No repeated funding address among those 40 transactions.
- Each transaction had hundreds of 547-satoshi outputs.

INTERPRETATION:
The message-bearing transactions share a previously
verified address fingerprint, but the funding addresses
are not repeated in this sample.

UNKNOWN:
Whether those 49 addresses share common ownership
or an earlier funding source.

## 4. STEP 5B — Earlier Non-Dust UTXOs

OBSERVED:
- 28 distinct dust-recipient addresses.
- 22 of those addresses also contributed non-dust
  inputs to the April 2022 consolidation.
- All 22 had a non-dust UTXO created before their
  first observed 547-satoshi UTXO in this sample.
- Those non-dust UTXOs were created in 2017–2019.
- Six dust-recipient addresses had no non-dust input
  in the consolidation transaction.

LIMITATION:
This compares UTXOs spent in the consolidation,
not complete historical address balances.
It does not establish an address's first-ever receipt,
continuous custody, or real-world ownership.

## 5. STEP 5C — Historical Funding Linkage

OBSERVED:
- 23 non-dust inputs analyzed.
- 22 distinct origin transactions.
- One origin transaction funded two analyzed addresses.
- Seven upstream funding addresses each appeared
  in transactions funding multiple analyzed addresses.
- Three upstream outpoints were associated with
  multiple analyzed recipients because the same
  transaction inputs funded multiple outputs.

### Direct shared origin transaction

TXID:
8aafef602724fdb9a46b36255db5d06556bf568669b1e06003b9532dbf6aa3bd

Date: 2017-10-04 UTC

Recipient 1:
3AdQtghXUCYxNpUTEg5sUFZwGvp3QDYNix
Value: 41.35980659 BTC

Recipient 2:
3DssfzjwSP4dcrGqU66cMMkMtrozj19oNR
Value: 45.51775073 BTC

### Selected shared upstream funding addresses

378p3u4RN1HTEWFkiTK27zuBWbx6eLSX6p
- Connected analyzed recipients: 9

3JjPf13Rd8g6WAyvg8yiPnrsdjJt1NP4FC
- Connected analyzed recipients: 8

1Ej4Jm8J83tKG4wUAbikNF3rQoGckH4Emp
- Connected analyzed recipients: 5

3DLRBj8bqGMgB6vcKgWeQLqSV4eDUMvDGw
- Connected analyzed recipients: 5

Recipient sets overlap. Counts must not be added
as if they represented distinct addresses.

The three shared parent outpoints do not provide
three independent links beyond the common source
transaction relationships.

## 6. Evidence Classification

### OBSERVED

O1. Message-bearing transactions span August 2020
    through January 2021 in the analyzed sample.

O2. All 22 overlapping addresses had earlier-created
    non-dust UTXOs.

O3. Two analyzed addresses received non-dust funds
    from the same 2017 transaction.

O4. Multiple analyzed addresses share upstream
    input funding addresses in their origin transactions.

O5. Dust and non-dust UTXOs were later consumed
    together in April 2022.

### INFERRED

I1. Some analyzed addresses had observable funding
    relationships before the dust campaign.

I2. The 2022 consolidation was not the first observable
    transaction-level relationship among every address
    in the analyzed group.

These observations are compatible with several wallet,
custody, service, and transaction-aggregation models.

### UNKNOWN

U1. Common real-world ownership.
U2. Identity of the upstream funding entities.
U3. Whether a custodial service was involved.
U4. Identity and intent of the dust sender or senders.
U5. Whether the dust campaign influenced the
    2022 consolidation.
U6. Any relationship to criminal activity.
U7. Any relationship to Silk Road or James Zhong.

### DISPROVEN

No ownership, service, or criminal hypothesis has
been disproven by this investigation.

## 7. Methodology and Limitations

Source:
https://mempool.space/api/tx/{txid}

Method:
- Exact outpoint matching for consolidation inputs.
- Historical transaction timestamp comparison.
- Shared origin TXID analysis.
- Shared upstream input-address analysis.
- Shared parent-outpoint analysis.

Data was queried from one public API.
Independent node or second-provider verification
has not yet been completed.

Shared funding addresses do not establish
common real-world ownership.

## 8. Next Step — STEP 5D

Investigate the structure of the 22 historical
funding transactions:

1. Compare input/output counts and values.
2. Identify repeated upstream transaction patterns.
3. Examine shared block timestamps and chronology.
4. Compare plausible wallet/custodial explanations.
5. Test alternative explanations and avoid
   double-counting dependent evidence.

## 9. Freeze Boundary

V2 is an interim evidence snapshot, not a final
attribution or criminal finding.

V0 and V1 must remain unchanged.
