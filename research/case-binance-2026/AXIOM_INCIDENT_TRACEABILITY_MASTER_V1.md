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
