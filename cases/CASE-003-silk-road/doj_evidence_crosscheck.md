# CASE-003 — Silk Road Bitcoin Theft
## DOJ Evidence Crosscheck V0.1

**Research Series:** Following the Money  
**Status:** ON-CHAIN RECONSTRUCTION / DOJ EVIDENCE REVIEW PENDING  
**Research Type:** Retrospective Bitcoin Fund Flow Reconstruction

### 1. Research Question

How far can publicly observable Bitcoin transactions reconstruct the movement of funds associated with the Silk Road theft case, and what additional evidence did U.S. investigators require to establish criminal provenance and control?

### 2. Official Case Reference

U.S. Department of Justice — 2020 Silk Road Bitcoin seizure.

Primary source (civil forfeiture complaint):

https://www.justice.gov/usao-ndca/press-release/file/1334771/dl?inline=

The complaint's specific factual allegations and evidentiary methods remain subject to detailed review.

### 3. Transaction A — 2013 Consolidation

**Date:** 2013-04-10  
**TXID:** `5d9ef693d41cb3bb4c6d98e70ea8b2cc91be29a804245a06ec8761d9cddc103c`

Repeated input addresses:

- `1BADznNF3W1gi47R65MQs754KB7zTaGuYZ`
- `1BBqjKsYuLEUE9Y5WzdbzCtYzCiQgHqtPN`

Output address:

`1HQ3Go3ggs8pFnXuHVHRytPCq5fGG8Hbhx`

**Output amount:** 69,471.082201 BTC

**Classification:** OBSERVED — explorer transaction record.

### 4. Transaction B — 2020 Transfer

**Date:** 2020-11-04  
**TXID:** `3f036ff88bb851b57a1e28780dbce35a6457a8b57995c095b55b3b0cf48ba9fd`

Input:

`1HQ3Go3ggs8pFnXuHVHRytPCq5fGG8Hbhx`

69,369.16716000 BTC

Output:

`bc1qa5wkgaew2dkv56kfvj49j0av5nml45x9ek9hz6`

69,369.16628020 BTC

**Fee:** 0.00087980 BTC

**Classification:** OBSERVED — explorer transaction record.

### 5. Evidence Boundaries

**OBSERVED**
- Repeated input addresses in the 2013 consolidation
- Large Bitcoin output created in 2013
- Subsequent transfer from the same address in 2020

**INFERRED**
- Repeated input patterns may indicate coordinated control, but do not independently prove common beneficial ownership.

**UNKNOWN**
- Actual beneficial ownership based solely on blockchain records
- Purpose of the 2013 consolidation
- Investigative evidence establishing attribution to the theft
- Exact legal and custodial relationship of the 2020 receiving address

**DISPROVEN**
- No hypothesis has yet been formally disproven.

### 6. Next Research Task

Review the DOJ complaint and extract the specific evidence supporting:

1. The alleged theft and its chronology
2. Attribution of funds to Silk Road
3. Attribution of relevant addresses to the investigated actor
4. The seizure and transfer of the Bitcoin

For every finding, distinguish official allegations, independently observed transactions, reasonable inferences, and unresolved questions.

**Research principle:** A transaction pattern is not proof of criminal conduct.
