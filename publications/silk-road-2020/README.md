# CASE-003 — Silk Road / Individual X
## Final Research Findings

**Status:** PARTIALLY VERIFIED  
**Research Type:** Retrospective On-Chain Reconstruction & DOJ Evidence Review

### 1. Research Objective

Reconstruct publicly observable Bitcoin fund movements associated with the 2020 Silk Road / Individual X forfeiture case and distinguish blockchain evidence from investigative attribution.

### 2. Verified On-Chain Transactions

**Transaction A — May 6, 2012**

- TXID: `b5fbb7ff3aafe2353418974e36da3786dafaa7b061fb506e50c09adc6dbecd1c`
- Multiple inputs, predominantly approximately 20–40 BTC
- Output: 2,500 BTC
- Recipient: `1BBqjKsYuLEUE9Y5WzdbzCtYzCiQgHqtPN`
- Classification: OBSERVED

**Transaction B — April 10, 2013**

- TXID: `5d9ef693d41cb3bb4c6d98e70ea8b2cc91be29a804245a06ec8761d9cddc103c`
- Multiple inputs from two previously identified addresses
- Output: 69,471.082201 BTC
- Recipient: `1HQ3Go3ggs8pFnXuHVHRytPCq5fGG8Hbhx`
- Classification: OBSERVED

Transaction A's 2,500 BTC output was spent as an input in Transaction B.

**Transaction C — November 4, 2020**

- TXID: `3f036ff88bb851b57a1e28780dbce35a6457a8b57995c095b55b3b0cf48ba9fd`
- Input: 69,369.16716000 BTC
- Output: 69,369.16628020 BTC
- Classification: OBSERVED

The complete transaction chain between 2013 and 2020 has not been reconstructed.

### 3. DOJ Investigative Evidence

According to the November 5, 2020 civil forfeiture complaint:

- Investigators identified 54 allegedly unauthorized Silk Road withdrawals totaling 70,411.46 BTC.
- Ten withdrawals involved exactly 2,500 BTC.
- The withdrawals were unusually large compared with typical Silk Road user withdrawals.
- Corresponding legitimate vendor or employee withdrawal records were absent from the Silk Road database.
- Investigators subsequently linked the funds to Individual X.

**Classification:** OFFICIAL ALLEGATIONS — documented in the DOJ complaint, not independently reproduced in full.

### 4. Evidence Assessment

**OBSERVED**
- Multiple UTXOs were consolidated into a 2,500 BTC output in 2012.
- That output was later spent in the 2013 consolidation.
- The 2013 consolidation created a 69,471.082201 BTC output.

**INFERRED**
- The reconstructed transactions are consistent with the fund-movement pattern described by DOJ.

**UNKNOWN**
- Whether the specific 2012 TXID is one of DOJ's 54 identified withdrawals.
- Whether the 2012 transaction represents an original unauthorized withdrawal or a subsequent movement.
- The precise investigative methods used to identify Individual X.
- The complete intervening transaction chain from 2013 to 2020.
- Independent proof of beneficial ownership from blockchain data alone.

**DISPROVEN**
- No formally tested hypothesis has been disproven.

### 5. Final Research Conclusion

Public blockchain data permits partial reconstruction of the Bitcoin fund movements described in the DOJ complaint.

The complaint provides additional investigative context through transaction attribution, withdrawal-pattern analysis, internal Silk Road records, and further investigation of Individual X.

However, the publicly available evidence reviewed does not independently reproduce the complete identity-attribution process.

**Final Status: PARTIALLY VERIFIED / IDENTITY ATTRIBUTION NOT REPRODUCIBLE**

### 6. Research Lessons

1. Transaction tracing does not independently establish beneficial ownership.
2. An unusual transaction pattern is not proof of criminal activity.
3. Internal records and independent evidence can distinguish authorized from unauthorized transfers.
4. Retrospective reconstruction must not be confused with prospective crime detection.
5. Unavailable investigative evidence must remain classified as UNKNOWN.

### 7. Sources

DOJ Civil Forfeiture Complaint, November 5, 2020:  
https://www.justice.gov/usao-ndca/press-release/file/1334771/dl?inline=

2012 transaction:  
https://mempool.space/tx/b5fbb7ff3aafe2353418974e36da3786dafaa7b061fb506e50c09adc6dbecd1c

2013 transaction:  
https://mempool.space/tx/5d9ef693d41cb3bb4c6d98e70ea8b2cc91be29a804245a06ec8761d9cddc103c

2020 transaction:  
https://mempool.space/tx/3f036ff88bb851b57a1e28780dbce35a6457a8b57995c095b55b3b0cf48ba9fd
