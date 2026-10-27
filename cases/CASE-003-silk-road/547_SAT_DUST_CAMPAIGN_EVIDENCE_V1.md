# CASE-003 — 547-Satoshi Message Campaign
## Evidence Freeze V1 — Interim Findings

Status: INTERIM / NOT FINAL
Evidence scope: Bitcoin on-chain transaction reconstruction
Freeze date: 2026-10-27

---

## 1. Research Question

Why did 46 separate 547-satoshi UTXOs originating from
transactions containing the same anonymity-message fingerprint
appear together in a single high-value Bitcoin transaction
on 2022-04-23?

This investigation examines observable transaction behavior.
It does not assume criminal intent, common ownership,
or a connection to the Silk Road criminal case.

---

## 2. Primary Transaction Anchors

### 2.1 Message transaction — 2020-11-25

TXID:
3995be87d959d28c8d845806ccf2bd27c61cc72bf18aa46f7bf37a2a07c092cd

Observed:
- 267 outputs valued at exactly 547 satoshis.
- Seven specially constructed output addresses collectively
  encode an anonymity-related message referencing memo.sv.
- One specific 547-sat output, vout 175, was later consumed
  by the 2022 consolidation transaction.

Exact outpoint:
3995be87d959d28c8d845806ccf2bd27c61cc72bf18aa46f7bf37a2a07c092cd:175

Recipient address:
bc1q95h6vkehyvnss820w85uz60pnv6qyfuhvtckw8

### 2.2 Consolidation transaction — 2022-04-23

TXID:
64a87c3d7540876516d0bf274fcc4773c0d59d07e960287b1d1ddbf690335b08

Observed:
- 78 total inputs.
- 46 inputs valued at exactly 547 satoshis.
- 32 non-547-satoshi inputs.
- Total input value: 1,500.72709382 BTC.
- Previously observed main output: 1,500.72603880 BTC.
- The original 2020 message UTXO was consumed at input 14.

The exact outpoint match establishes transaction-level
lineage, not real-world ownership.

---

## 3. Message Fingerprint Verification

All 46 of the 547-sat inputs originated from
40 distinct previous transactions.

Each of those 40 transactions contained all seven
predefined message-address markers.

Classification results:

- FULL_MESSAGE_MATCH: 40 source transactions / 46 inputs
- PARTIAL_MESSAGE_MATCH: 0
- NO_MESSAGE_MATCH: 0
- FETCH_FAILED: 0

This is an exact predefined message-address fingerprint
match, not proof that all 40 transactions had one sender.

The repeated 547-sat denomination and shared message
fingerprint establish a coherent observable transaction
pattern.

---

## 4. Recipient Address Structure

Among the 46 dust inputs:

- Unique recipient addresses: 28.
- Addresses also appearing among the 32 non-dust
  inputs in the same consolidation transaction: 22.
- Unique addresses among non-dust inputs: 31.

Therefore, 22 of the 28 dust-recipient addresses
also contributed at least one non-dust UTXO to
the same transaction.

Example:

Address:
3DXmrrHdLNz16WqbVEvFr5fuw8bjHpDUFU

Observed:
- At least one 547-sat input.
- One 127.85575170 BTC input.
- Both spent in the same 2022 consolidation transaction.

This establishes same-address co-spending,
not necessarily the identity of the wallet operator.

---

## 5. Value Reconciliation

547-sat inputs:

46 x 547 = 25,162 satoshis
= 0.00025162 BTC

Non-547-sat inputs:

1,500.72684220 BTC

Combined inputs:

1,500.72709382 BTC

Previously observed main output:

1,500.72603880 BTC

Difference between total inputs and this output:

0.00105502 BTC

This difference must NOT automatically be labeled
a miner fee without checking the full output list
and transaction fee field.

---

## 6. Evidence Classification

### OBSERVED

O1. One exact 2020 message-transaction outpoint
    was consumed by the 2022 consolidation.

O2. All 46 dust inputs trace to 40 source transactions
    containing the same seven message-address markers.

O3. The 46 dust inputs span 28 distinct recipient addresses.

O4. Twenty-two recipient addresses also provided
    non-dust inputs to the same transaction.

O5. The consolidation combines dust and substantial
    non-dust Bitcoin values.

### INFERRED / HYPOTHESES

H1. Wallet UTXO consolidation or cleanup.

H2. Custodial or multi-address wallet operation.

H3. A more specialized operational pattern.

These are competing hypotheses.
None has yet been established.

### UNKNOWN

U1. Identity of the message-campaign sender or senders.

U2. Whether the 40 source transactions shared
    a common funding entity.

U3. Whether the 28 recipient addresses shared
    one real-world owner.

U4. Why the 46 dust UTXOs were selected for spending.

U5. The operational meaning of the memo.sv reference.

U6. Whether any of these transactions relate
    to criminal activity.

U7. Whether the addresses had independent
    pre-2022 transaction relationships.

### DISPROVEN

No hypothesis is currently classified as disproven.

---

## 7. Methodology

Public Bitcoin transaction data was queried through:

https://mempool.space/api/tx/{txid}

UTXO lineage was established using exact:

(previous_txid, previous_vout)

The message classification compared the presence of
seven predefined output addresses in each funding
transaction.

Recipient-address overlap was calculated using
the prevout scriptpubkey_address values in the
2022 consolidation transaction.

Results are reproducible but have not yet been
independently cross-verified against a second
Bitcoin data provider or a locally operated node.

---

## 8. Next Investigation

STEP 5 — Historical Address Relationships

1. Reconstruct the creation dates of the 40
   message-bearing funding transactions.

2. Compare their funding inputs and transaction structure.

3. Examine historical relationships among the 28
   recipient addresses before April 2022.

4. Investigate the provenance of the 32 non-dust inputs.

5. Test wallet consolidation versus custodial
   aggregation versus other operational hypotheses.

6. Verify the complete consolidation output list
   and actual transaction fee.

Do not infer a criminal connection from co-spending,
message content, or large Bitcoin values alone.

---

## 9. Research Boundary

This artifact documents an independent on-chain
investigation discovered during CASE-003 research.

Its location in the CASE-003 Silk Road directory
does not establish an evidentiary connection
to Silk Road, James Zhong, or any DOJ prosecution.

V0 remains unchanged.

Evidence Freeze V1 preserves the current findings.
It does not close the investigation.
