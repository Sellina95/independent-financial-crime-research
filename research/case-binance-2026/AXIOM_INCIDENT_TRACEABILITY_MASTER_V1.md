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

## 14. Fund Flow Network — 700M Scoped Ledger

**Status: OBSERVED / SCOPED RECONCILIATION PASS**

Network: Ethereum Mainnet
Token: USDT (6 decimals)
Scope: Two first-hop recipients of Central.

### Evidence provenance

- Raw source: `evidence/second_hop_usdt_v1/transfer_logs.json`
- SHA256: `7b8e0b68f6cabebe2c9789e5b4a76437a0b44b7c8f85a81925e2054a894d2300`
- Identity key: `(transactionHash, logIndex)`.
- Amount arithmetic: exact integer token units.

### Verified distribution table

| Sender | Recipient | USDT | Events |
|---|---|---:|---:|
| `0x9749292d74fd460982d0912ea9515ea24736c762` | `0x811f15855476156ebf86ba3b84fafb8ceaa4e84c` | 175,000,000.000000 | 1 |
| `0x9749292d74fd460982d0912ea9515ea24736c762` | `0xbeef02961503351625926ea9a11ae13b29f5c555` | 144,999,999.999999 | 4 |
| `0x9749292d74fd460982d0912ea9515ea24736c762` | `0x0000000000be226afde21672a5e4adc45692e69d` | 100,000,000.000000 | 1 |
| `0x9749292d74fd460982d0912ea9515ea24736c762` | `0x74edc79fea13bdf1f7841570227127cec493bdd9` | 50,000,000.000000 | 1 |
| `0x9749292d74fd460982d0912ea9515ea24736c762` | `0x9b1303ebf09bc51b7fac376c9e421e8daae63b82` | 28,600,454.367187 | 1 |
| `0x9749292d74fd460982d0912ea9515ea24736c762` | `0xec4fb7e7c35c241e1138a2d8cfbb09f3ad1ccb22` | 1,399,545.632814 | 2 |
| `0x9749292d74fd460982d0912ea9515ea24736c762` | `0x8477f676e781ffbca3c3cb853b09fe1c33b57f20` | 0.000000 | 1 |

**Branch `0x9749292d74fd460982d0912ea9515ea24736c762` reconciliation:**
500,000,000.000000 expected; 500,000,000.000000 observed; 0.000000 USDT difference.

| `0x0ddf0480016e6bcb2c1f5d190d221fba1320697e` | `0x8d53903625b8e839b9df4bd28b0efb1cd6b8639a` | 190,000,000.000000 | 1 |
| `0x0ddf0480016e6bcb2c1f5d190d221fba1320697e` | `0x000000000004444c5dc75cb358380d2e3de08a90` | 4,120,000.000000 | 1 |
| `0x0ddf0480016e6bcb2c1f5d190d221fba1320697e` | `0x4e68ccd3e89f51c3074ca5072bbac773960dfa36` | 3,390,000.000000 | 1 |
| `0x0ddf0480016e6bcb2c1f5d190d221fba1320697e` | `0x56534741cd8b152df6d48adf7ac51f75169a83b2` | 1,390,000.000000 | 1 |
| `0x0ddf0480016e6bcb2c1f5d190d221fba1320697e` | `0x9db9e0e53058c89e5b94e29621a205198648425b` | 500,000.000000 | 1 |
| `0x0ddf0480016e6bcb2c1f5d190d221fba1320697e` | `0x11b815efb8f581194ae79006d24e0d814b7697f6` | 330,000.000000 | 1 |
| `0x0ddf0480016e6bcb2c1f5d190d221fba1320697e` | `0x0d4a11d5eeaac28ec3f61d100daf4d40471f1852` | 110,000.000000 | 1 |
| `0x0ddf0480016e6bcb2c1f5d190d221fba1320697e` | `0xc7bbec68d12a0d1830360f8ec58fa599ba1b0e9b` | 100,000.000000 | 1 |
| `0x0ddf0480016e6bcb2c1f5d190d221fba1320697e` | `0x3416cf6c708da44db2624d63ea0aaef7113527c6` | 60,000.000000 | 1 |

**Branch `0x0ddf0480016e6bcb2c1f5d190d221fba1320697e` reconciliation:**
200,000,000.000000 expected; 200,000,000.000000 observed; 0.000000 USDT difference.

### Scope and limitations

- Selected branch inflows: 700,000,000.000000 USDT.
- Selected branch outflows: 700,000,000.000000 USDT.
- Reconciliation difference: 0.000000 USDT.
- Unique transaction hashes: 13.
- Unique Transfer events: 20.
- Distinct recorded recipient addresses: 16.
- One recipient has a zero-value Transfer event.
- Zero-value events do not increase transferred value.
- These are recipient addresses, not 16 proven owners.
- Later swaps, protocol interactions and pooled liquidity
  must not be interpreted as direct actor-controlled custody.
- This is NOT incident-wide transfer completeness.
- This is NOT proof of stolen-funds attribution.
- These downstream movements are NOT additional losses.
- This checkpoint records existing observations;
  it does not claim a newly discovered transaction path.

### Next research boundary

Cross-reference saved downstream evidence and public
institutional reports before any new branch tracing.
Prioritize a genuinely unresolved mechanism or control
question rather than repeating documented movements.

## 15. Preserved 175M and 190M Follow-on Audit

**Status: SCOPED RECEIPT VERIFICATION PASS**

| Block | From | To | USDT | TXID |
|---:|---|---|---:|---|
| 26300936 | `0x8d53903625b8e839b9df4bd28b0efb1cd6b8639a` | `0x23878914efe38d27c4d67ab83ed1b93a74d4086a` | 10,000,000.000000 | `0x420e74015336a44f3056c00bf5a1313889a7f6ed30a053ad59832d4a4a1f14eb` |
| 26300947 | `0x8d53903625b8e839b9df4bd28b0efb1cd6b8639a` | `0x23878914efe38d27c4d67ab83ed1b93a74d4086a` | 50,000,000.000000 | `0x65bd82f19985a569ef87b3926dd5f2247ba7bd06640141060f1b2d9ddedec3f6` |
| 26300956 | `0x8d53903625b8e839b9df4bd28b0efb1cd6b8639a` | `0x77edef23fbd05921c26fe29fcc3a65e14d2ac3eb` | 130,000,000.000000 | `0xd2e7e5e6ee32a3552de469d97e90d83b707d314ffe7b8747786de92daa3fc3d8` |
| 26300988 | `0x811f15855476156ebf86ba3b84fafb8ceaa4e84c` | `0xaa246bf639586a6ba46762d378ce50ca4fc654a0` | 175,000,000.000000 | `0xb6d7d3ffcbdd0465e1ab743a8d943218176cac7b15edefa7b7bcd5e853e4266f` |

### Scoped reconciliation

- 175M intermediary: 175M observed outgoing; difference 0.
- 190M intermediary: 10M + 50M + 130M = 190M.
- Both checks cover preserved receipts only.
- Zero scoped difference does NOT prove complete history.
- These are downstream movements, not additional incident losses.

### Protocol and attribution boundary

- The 10M and 50M transfers reach an Aave-associated address.
- No direct 60M Supply -> 25M withdrawal attribution is supported.
- The pre-existing aUSDT position correction remains controlling.
- Wallet ownership and incident-specific attribution: UNKNOWN.
- Do not re-open the discredited 25M attribution path.

### Original evidence SHA256

- `evidence/blacklist_flow_175m_v1/inflow_receipt.json` — `5a7dcf937bba60abb091d43884013b6882a7beba9b47b863184a11fbf3042aa4`
- `evidence/30m_upstream_bridge_v1/130m_receipt.json` — `f69ff4b030582007513a308a260837adc6b54863c004322190eddc3d3c704603`
- `evidence/eg08_source_attribution_v1/step08y_forward_edge_preservation_v1/raw_intermediate_receipts.json` — `1129314e62d6c2d334053c262c99fa041d9e4bf698a68f2e7ca9eb3f291c6568`

### Research decision

Mark these two intermediary distributions as
SCOPED RECONCILIATION PASS, not FINAL TRACE COMPLETE.
Link existing 130M and blacklist studies without
re-running their original transaction investigations.

## 16. 130M Path and Blacklist Control Checkpoint

Status: SCOPED RECEIPT AUDIT / CONTROL CHECKPOINT

### A. Preserved 130M -> 80M -> 30M route

| Block | Sender | Recipient | USDT | TXID | Log index |
|---:|---|---|---:|---|---:|
| 26300956 | `0x8d53903625b8e839b9df4bd28b0efb1cd6b8639a` | `0x77edef23fbd05921c26fe29fcc3a65e14d2ac3eb` | 130,000,000.000000 | `0xd2e7e5e6ee32a3552de469d97e90d83b707d314ffe7b8747786de92daa3fc3d8` | 382 |
| 26300980 | `0x77edef23fbd05921c26fe29fcc3a65e14d2ac3eb` | `0x7aa4d3029e4c6a8e916300014ad95b6d6c03bfd1` | 80,000,000.000000 | `0x279d12e9a7f594eeaf0eb83fe649f7f2cdf82ced156a82f85014dc56369b36d8` | 701 |
| 26301002 | `0x7aa4d3029e4c6a8e916300014ad95b6d6c03bfd1` | `0xccbef95633adb5cd2b5038db5a38d77e726ca263` | 30,000,000.000000 | `0x9a7645882a20445c5a731a15f34e1757f0b6c52e8f51a4ddb8c09cdc424295ce` | 424 |
| 26301027 | `0xccbef95633adb5cd2b5038db5a38d77e726ca263` | `0xb171ca86f82070282138352ff7111b494060c8c3` | 30,000,000.000000 | `0x1e6f851d072ae0ad448dca2446552cbb4e76516029b34980d5189e4353aae7a7` | 132 |

### B. Reconciliation boundaries

- Verified movements: 130M -> 80M -> 30M -> 30M.
- 130M less 80M = 50M unaccounted for in this
  selected outgoing sample, NOT a verified residual balance.
- 80M less 30M = 50M likewise NOT a verified balance.
- The two successive 30M transfers are the same
  observed path, not 60M of distinct loss.
- These selected receipts do not prove full coverage.
- Incident-specific ownership/attribution: UNKNOWN.

### C. Blacklist-time balance checkpoints

| Address group | Block | USDT balance |
|---|---:|---:|
| Central | 26300954 | 971,149,299.483240 |
| 175M recipient | 26301021 | 174,999,872.327520 |
| 30M recipient | 26301041 | 30,000,000.000000 |

- Source: `EG01_EXECUTION_TIME_AUDIT_V1.md`.
- Classification: OBSERVED historical block-end balance;
  execution-instant balance STRONGLY INFERRED.
- Three checkpoints occur at different block times.
- Their arithmetic sum is NOT incident-wide frozen
  value, recovered assets or synchronized holdings.
- Transfer restriction, subsequent incoming funds,
  redemption and recovery must be kept separate.

### D. Raw receipt provenance

- `evidence/30m_upstream_bridge_v1/130m_receipt.json` SHA256 `f69ff4b030582007513a308a260837adc6b54863c004322190eddc3d3c704603`
- `evidence/30m_upstream_bridge_v1/80m_receipt.json` SHA256 `20edcee810398d3d140e4c985ff5472bb10e801672f0b70801aaea447c59a2d7`
- `evidence/30m_upstream_bridge_v1/30m_a_receipt.json` SHA256 `2f1a843b67efafa45f4b5d4c324ec28f289438a62b5e84afca896b85db131363`
- `evidence/30m_upstream_bridge_v1/30m_b_receipt.json` SHA256 `8a3c9f2e1e3ecb7872b7e730d0fa0f923b0ac85ae03d8876e91b8f4a0519c5bb`

### E. Research decision

- Existing 130M/80M/30M path: DO NOT RETRACE.
- Existing blacklist event/balance audit: REUSE.
- No new actor attribution or institutional omission claim.
- Next priority: compare source/designation evidence and
  public institutional interpretations before new tracing.

## 17. EG-06 Control-Timing Evidence Boundary

**Status: PARTIAL / CONTROL FAILURE NOT ESTABLISHED**

### Evidence register

| UTC | Event or claim | Classification |
|---|---|---|
| 2026-10-29 22:27 | Public confirmation reported by TechCrunch | REPORTED_BY_SOURCE |
| 2026-10-29 22:39:35 | Candidate transaction time in research charter | UNVERIFIED CANDIDATE |
| 2026-10-29 23:56 | Last unauthorized 2,961.9 ETH transfer, per Binance | REPORTED_BY_SOURCE |
| 2026-10-30 00:10:35 | Delegation revocation candidate, block 26301896 | INDEXED EVIDENCE / RAW REPLAY PENDING |

Revocation candidate TXID:
`0xafbf94c92a8d749988411669fa14d4f8866d9b4420b4ebd299f28e958dac7209`

### Critical unknowns

- Exact internal withdrawal-suspension effective timestamp: UNKNOWN.
- Whether the 22:39:35 candidate is a verified qualifying transaction: UNKNOWN.
- Relevant broadcast, inclusion and finalization times are not interchangeable.
- Whether a specific transaction bypassed an effective control: NOT ESTABLISHED.
- Public confirmation time is not an internal suspension timestamp.
- Cryptographic signing does not establish corporate authorization.

### Institutional interpretation

No control failure may be asserted from these timestamps alone.
The unresolved question is whether authenticated internal
control timing can be compared to independently verified
qualifying asset transfers and delegation state.

### Evidence provenance

- `EVIDENCE_GAP_REPORT.md` SHA256 `1834a50d03490fec9e1cf83b9b3f6bc90fc7e4c78cab67979ded6ce6835cefec`
- `evidence/step75a_official_report_crosswalk_v1/official_report_excerpt.txt` SHA256 `955b0061acea6b3be3f804638e568b74b1cb7cbccaf53d003cf06c42127b6630`
- `evidence/eg08_source_attribution_v1/step08w_incident_attribution_crosswalk_v1/existing_evidence_index.json` SHA256 `e280dd09a3311ee6a7c9cbf1f74982c79c7b64ad3cba23513e3718773d333eae`

### Research decision

- EG-06 remains OPEN.
- Do not repeat T02/T03/T17 technical audits.
- Do not claim an institution missed a control failure.
- Resume only with authenticated suspension timing
  or a material, independently reproducible transaction.
- Otherwise retain UNKNOWN and prioritize other gaps.
