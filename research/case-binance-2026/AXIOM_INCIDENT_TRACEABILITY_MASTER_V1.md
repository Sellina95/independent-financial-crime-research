# AXIOM — Binance 2026 Incident Traceability Master

Status: ACTIVE RESEARCH / NOT PUBLICATION APPROVED
Baseline commit: 0285742
Branch: research/case-binance-2026

## 1. Research Mission

Independently reconstruct the reported Binance 2026
incident using reproducible public evidence.

Determine:
- Where funds originated.
- Which transactions can be verified.
- Where paths split, converge or transform.
- Where traceability or incident attribution breaks.
- Which gaps remain unresolved in public investigations.
- What the evidence reveals about financial controls.

Do not assume an institution overlooked information
merely because it was not publicly disclosed.

## 2. Final Research Deliverables

### A. Incident Timeline
UTC chronological reconstruction of:
- Initial reported asset outflows
- On-chain transactions
- Subsequent movements
- Blacklist and restriction events
- Balance checkpoints
- Verified control actions

### B. Fund Flow Network
For every verified edge:
- Chain and token
- Sender and recipient
- Exact amount
- Transaction hash and log index
- Block and UTC timestamp
- Protocol or intermediary role
- Evidence reference

### C. Asset Reconciliation
Reconcile:
- Candidate initial outflows
- Subsequent distributions
- Intermediate balances
- Restricted balances
- Post-restriction inflows
- Recovery, if independently established

Never double-count intermediary or bridge movements.

### D. Evidence & Confidence Audit
Classifications:
OBSERVED
REPORTED_BY_SOURCE
INFERRED
UNKNOWN
DISPROVEN
ACCESS_LIMITATION

Preserve raw evidence, SHA256 and source provenance.

## 3. Final Report Questions

1. What happened?
2. How did funds move?
3. What was restricted?
4. Has this pattern appeared before?
5. What does this reveal about financial infrastructure?
6. What remains unknown, and why?

Historical comparisons require independent source verification.

## 4. Verified Research Checkpoints

### Ethereum Initial Movement
Binance14 -> Central
1,615,409,498.973240 USDT

Transaction transfer documented.
Independent incident attribution remains qualified.

Reference:
GATE_3_T03_TO_700M_LINKAGE_AUDIT_V1.md

### Central Distribution
Central -> 500M branch
Central -> 200M branch

700M selected first-hop total.

20 second-hop Transfer events.
13 unique transactions.
13 archived receipts.
Scoped reconciliation PASS.

Reference:
700M_FIRST_HOP_DISTRIBUTION_AUDIT_V1.md

### Existing Follow-on Research
175M path: existing evidence
190M/130M/80M/30M paths: existing evidence
USDT blacklist checkpoints: existing evidence

Do not repeat completed transaction verification.

### Aave Attribution Correction
Previous 60M Supply -> A 25M withdrawal
direct attribution hypothesis rejected.

The 25M withdrawal was supported by
a pre-existing aUSDT position.

Incident attribution: UNKNOWN.
Do not reopen without new independent evidence.

Reference:
EG08_AAVE_POSITION_ATTRIBUTION_CORRECTION_V1.md

### Plasma 28M
Cross-chain delivery independently documented.
Incident attribution: UNKNOWN.

Stop attribution tracing absent a new source anchor.

## 5. Existing Major Branch Candidates

From the verified 500M distribution:

175M: previously investigated
145M: incoming transfers verified
100M: incoming transfer verified
50M: incoming transfer verified
28.600454M: incoming transfer verified
Remaining smaller distributions: existing ledger

Current research issue:
Determine whether any material branch is genuinely
unexplained after accounting for DEX settlement,
protocol operations, liquidity pools and published reports.

No criminal ownership inference from recipient addresses.

## 6. Priority Research Gates

P0 — Incident source authentication
Compare exact initial transactions and source addresses
against official and independent public evidence.

P1 — Full traceability boundary map
Reuse existing transaction evidence.
Identify covered, partially traced and unverified edges.

P2 — Public institutional crosswalk
Compare Binance, Bitquery, Crystal, TRM and other
relevant sources using exact claims and timestamps.

P3 — Material unresolved flows
Investigate only previously untested, decision-relevant
branches with an explicit falsification test.

P4 — Restriction and control reconciliation
Check historical blacklist states, balances and
asset-preservation implications without overclaiming.

P5 — Historical comparison and final synthesis
Compare independently verified mechanisms and controls.

## 7. Finding Categories

HIGH PRIORITY:
Independently verified, material new movement or connection.

INSTITUTIONAL:
Evidence useful for asset preservation,
investigation, issuer controls or recovery.

LINKEDIN:
Reproducible public-interest research with clear limitations.

STOP / RED TEAM:
Incorrect attribution, double counting,
unverified mechanism or alternative explanation.

NO NEW EVIDENCE:
Document the boundary and stop low-value exploration.

## 8. Permanent Protection

Only research/case-binance-2026 may contain ongoing work.

Never modify main without explicit approval.

Do not overwrite original evidence or prior reports.
The EVIDENCE_GAP_REPORT.md remains the research charter.

All findings require exact evidence references.
No invented links, ownership or criminal allegations.

Blocked RPC access is not blockchain evidence.
Do not repeatedly query inaccessible historical providers.

## 9. Publication Acceptance

- [ ] Incident timeline reconstructed and audited
- [ ] Fund flow network with evidence-linked edges
- [ ] Asset conservation and duplicate checks
- [ ] Blacklist-time balances correctly classified
- [ ] Public institutional source crosswalk
- [ ] Known false attribution claims explicitly corrected
- [ ] Traceability boundaries documented
- [ ] High-value unresolved gaps evaluated
- [ ] Independent replay where materially necessary
- [ ] Historical mechanism comparison
- [ ] Red-team review completed
- [ ] Final human review and publication approval

## 10. Research Session Log

Baseline: 0285742

STEP 01-07:
Existing evidence inventory and selected 700M
distribution review completed.

STEP 08-09:
145M recipient historical contract-code verification
not completed due to RPC and explorer access limits.

Current next step:
Build a source-linked incident-wide traceability
and institutional-publication crosswalk.

Do not repeat Aave 25M / Plasma 28M attribution chase.

## 11. Next Finding Template

UTC:
Source commit:
Research question:
Previously available evidence:
New verification:
OBSERVED:
REPORTED_BY_SOURCE:
INFERRED:
UNKNOWN:
DISPROVEN:
Conservation checks:
Competing explanations:
Institutional source comparison:
Novelty assessment:
Classification:
Next decisive test:
Stopping condition:


## 12. Incident Timeline — Audited Checkpoint

Status: PARTIAL — existing evidence only.

| Block | UTC | Event | USDT amount |
|---:|---|---|---:|
| 26300770 | 2026-10-29 20:24:23 UTC | Initial Binance14 → Central | 1,615,409,498.973240 |
| 26300799 | 2026-10-29 20:30:11 UTC | Central → 500M branch | 500,000,000 |
| 26300815 | 2026-10-29 20:33:23 UTC | Central → 200M branch | 200,000,000 |
| 26300942 | 2026-10-29 20:59:11 UTC | 500M branch → 175M recipient | 175,000,000 |
| 26300954 | 2026-10-29 21:01:35 UTC | Central blacklist event | 971,149,299.483240 |
| 26300988 | 2026-10-29 21:08:23 UTC | 175M recipient → terminal address | 175,000,000 |
| 26301011 | 2026-10-29 21:12:59 UTC | Terminal address outgoing | 127.672480 |
| 26301021 | 2026-10-29 21:14:59 UTC | 175M terminal blacklist event | 174,999,872.327520 |
| 26301041 | 2026-10-29 21:18:59 UTC | 30M terminal blacklist event | 30,000,000 |

### Evidence boundaries

- Initial transfer timestamp: USDT_FUND_FLOW_AND_FREEZE_V2.md.
- Second-hop timestamps: archived transfer_logs.json where available.
- Other event ordering: preserved block numbers, not invented UTC times.
- Blacklist amounts are historical address-balance checkpoints.
- Blacklist registration is not proof of asset recovery.
- Initial and downstream amounts must not be summed as separate losses.

### RED TEAM — historical report correction

The older USDT_FUND_FLOW_AND_FREEZE_V2.md recorded
a 127.672380 USDT discrepancy.
The later BLACKLIST_175M_CASE_AUDIT_V1.md reconciled
the 127.672480 USDT outgoing transfer and
174,999,872.327520 USDT historical remaining balance.
The later verified reconciliation takes precedence.
Original documents remain unchanged.

Incident-specific attribution remains UNKNOWN where
independent source authentication is unavailable.

## 13. Transaction Evidence Crosswalk

Status: REPORT-LINKED / RAW RECEIPT REPLAY PENDING

| Block | Event | TXID | UTC | Source | Type |
|---:|---|---|---|---|---|
| 26300770 | Initial USDT transfer | `0x53bd38b816c23e74134786c29a8c18d792777998a3b9326047b583100e88e2f3` | 2026-10-29 20:24:23 UTC | `USDT_FUND_FLOW_AND_FREEZE_V2.md` | TRANSFER |
| 26300799 | Central 500M distribution | `0x68d7d69deaeb9750c38020b4f8d3728146ca8d2267eba1e38cf9b56722ad659a` | 2026-10-29 20:30:11 UTC | `USDT_FUND_FLOW_AND_FREEZE_V2.md` | TRANSFER |
| 26300815 | Central 200M distribution | `0x1fc0ef33a767132edad434834a5555b30fcb5a171206c03b86175ef6dafac81c` | 2026-10-29 20:33:23 UTC | `GATE_3_T03_TO_700M_LINKAGE_AUDIT_V1.md` | TRANSFER |
| 26300942 | 175M transfer | `0x1fb992f92a45afec23d7d5740c7958a644fb90ef0cba19ca39bd2c6534fb670b` | 2026-10-29 20:59:11 UTC | `GATE_2_175M_PATH_CONTINUITY_AUDIT_V1.md` | TRANSFER |
| 26300954 | Central blacklist | `0x7baba482077843514d9c72bac0110ba0916b0814288a72917e2c3bb27a9d8659` | 2026-10-29 21:01:35 UTC | `USDT_FREEZE_TIMELINE_CHECKPOINT_V4.md` | BLACKLIST |
| 26300988 | 175M onward transfer | `0xb6d7d3ffcbdd0465e1ab743a8d943218176cac7b15edefa7b7bcd5e853e4266f` | 2026-10-29 21:08:23 UTC | `BLACKLIST_175M_CASE_AUDIT_V1.md` | TRANSFER |
| 26301011 | 127.672480 transfer | `0x11be88b460501b4652e760c41e08cc1f18575e14b6c6ffbb3383e043c2decf34` | 2026-10-29 21:12:59 UTC | `BLACKLIST_175M_CASE_AUDIT_V1.md` | TRANSFER |
| 26301021 | 175M recipient blacklist | `0x0c07a5e428ce233a3bcb40f257ad899594421341d63ce94016822063362707bf` | 2026-10-29 21:14:59 UTC | `USDT_FREEZE_TIMELINE_CHECKPOINT_V4.md` | BLACKLIST |
| 26301041 | 30M recipient blacklist | `0x3445389c8aceb50fe1c155a1208f7289cc8f7f5950139e21dc405333d1aedc93` | 2026-10-29 21:18:59 UTC | `USDT_FREEZE_TIMELINE_CHECKPOINT_V4.md` | BLACKLIST |

### Verification boundaries

- TXID/block associations were checked against nearby report text.
- This is NOT an independent replay of all original receipts.
- The 200M TXID remains unlinked in the selected evidence.
- UTC entries come from existing observations or external reports.
- Missing UTC values must not be inferred from nearby blocks.
- BLACKLIST amounts in Section 12 are address balance
  checkpoints, not transaction transfer amounts.
- Evidence confidence may be upgraded only after raw-artifact
  matching and appropriate independent validation.

### Reconciliation caution

The older 175M snapshot discrepancy of 127.672380 USDT
was superseded by the receipt-reconciled 127.672480 USDT
outflow documented in BLACKLIST_175M_CASE_AUDIT_V1.md.

Next: verify the 200M TXID and missing event timestamps
from existing archived records before attempting new RPC calls.

### STEP 18 — 200M original receipt verification

- Transaction: `0x1fc0ef33a767132edad434834a5555b30fcb5a171206c03b86175ef6dafac81c`
- Block: `26300815`
- USDT amount: `200,000,000.000000`
- Receipt status: SUCCESS
- Transfer log index: `0x394`
- Source: Central address
- Destination: 200M branch address
- Two preserved receipt files independently matched.
- Classification: OBSERVED, ARCHIVED RECEIPT CROSS-CHECK PASS.
- UTC timestamp: NOT YET PINNED.
- Incident-specific unauthorized transfer attribution: UNKNOWN.

### STEP 20-21 — Historical UTC provenance audit

All nine event rows now carry UTC timestamps
matched to their own block numbers in archived JSON.

Classification:
OBSERVED IN SAVED BLOCK/RECEIPT METADATA.
Not a fresh independent RPC replay.

RED TEAM — 175M blacklist timestamp:
- On-chain block timestamp: 2026-10-29 21:14:59 UTC.
- Older third-party report: 2026-10-29 21:15:03 UTC.
- Difference: 4 seconds.
- Cause: UNKNOWN.
- Timeline uses the archived on-chain block time.

These times are block timestamps, not a precise
wall-clock timestamp for each individual transaction.
Transaction index determines order within a block.

Original evidence and earlier reports remain unchanged.
