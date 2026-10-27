# CASE-003 — DOJ Evidence Review V1

## Research Question

How did U.S. investigators connect the 69,370 BTC to the Silk Road theft?

## Primary Source

U.S. Department of Justice, Complaint for Forfeiture, filed November 5, 2020.

Case No. 3:20-cv-07811-VC

https://www.justice.gov/usao-ndca/press-release/file/1334771/dl?inline=

## Finding 1 — Transaction Attribution

**Source:** Complaint §15, page 4

DOJ alleges that investigators used a third-party Bitcoin attribution company to identify 54 transactions from Silk Road-controlled addresses to two receiving addresses.

Total: 70,411.46 BTC.

**Classification:** OBSERVED — official allegation documented; underlying attribution data not independently reproduced.

## Finding 2 — Abnormal Withdrawal Pattern

**Source:** Complaint §16, page 4

DOJ identified:

- Round-number Bitcoin transfers
- Transfers clustered closely in time
- Ten transfers of exactly 2,500 BTC
- Amounts substantially larger than typical Silk Road user withdrawals
- No corresponding vendor or employee withdrawal entries in the Silk Road database

**Classification:** OBSERVED — documented DOJ allegations.

**Interpretation:** The combination of abnormal transaction patterns and missing internal records supported the theft hypothesis.

**Classification:** INFERRED — interpretation of the cited evidence.

## Finding 3 — Consolidation

**Source:** Complaint §17, page 4

DOJ alleges that the two receiving addresses transferred 69,471.082201 BTC to:

`1HQ3Go3ggs8pFnXuHVHRytPCq5fGG8Hbhx`

The complaint describes the transfer as occurring approximately April 9, 2013.

Our explorer observation records the transaction on April 10, 2013. The date discrepancy remains unresolved and may involve timezone conventions.

**Classification:** OBSERVED — source statements and explorer record, with date reconciliation pending.

## Finding 4 — Subsequent Movement

**Source:** Complaint §18–19, page 5

DOJ alleges that 101 BTC was transferred to BTC-e in April 2015, while the majority of the funds remained associated with the 1HQ3 address.

The exact 2015 transaction has not yet been independently reconstructed.

**Classification:** OBSERVED — DOJ allegation.

## Finding 5 — Attribution and Seizure

**Source:** Complaint §21–24, pages 5–6

DOJ alleges that:

- Individual X was linked to a transaction associated with 1HQ3.
- Investigators determined that Individual X had moved the cryptocurrency from Silk Road.
- Individual X signed a forfeiture consent agreement on November 3, 2020.
- The United States took custody of the property on November 3, 2020.

**Classification:** OBSERVED — statements in the official complaint.

**UNKNOWN:** The complete underlying evidence used to identify Individual X and establish wallet control.

## Preliminary Conclusion

The DOJ case was not based solely on observing large Bitcoin transfers.

The complaint describes a combination of blockchain attribution, unusual withdrawal patterns, comparison against Silk Road internal records, further investigation of an individual, and a forfeiture agreement.

This establishes the investigative logic alleged in the complaint, but does not independently reproduce the underlying investigative evidence.

## Next Research Question

Can the 54 allegedly unauthorized Silk Road withdrawals be independently reconstructed using public blockchain data, and which parts of the DOJ attribution require unavailable internal records?
