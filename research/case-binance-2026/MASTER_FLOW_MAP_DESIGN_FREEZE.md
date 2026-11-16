# Binance 2026 — Master Flow Map Design Freeze

Status: APPROVED DESIGN / IMPLEMENTATION PENDING
Date: 2026-11-16

Repository: Sellina95/independent-financial-crime-research

Research branch: research/case-binance-2026

Baseline commit:
bba74a5c89f830193999d8aef051349161dccf4e

This document is the authoritative design and
implementation checklist for the Binance 2026 map.

Do not change the approved design without user approval.

---

## 1. FINAL OBJECTIVE

Reconstruct all evidence-supported fund movements
available in the pinned GitHub research snapshot.

Create one canonical dataset:

MASTER_FLOW_DATA.json

Use this dataset for:

- Master Flow Map
- Transaction Timeline
- Research Inspector
- Evidence and Audit

Preserve verified facts, inferred routes,
uncertainties and original evidence.

Do not assume every extracted record is a transfer.

Do not assume every observed transfer belongs
to the Binance incident.

---

## 2. WEBSITE DESIGN — FROZEN

KEEP THE CURRENT PUBLIC WEBSITE DESIGN.

Main website:
https://sellina95.github.io/independent-financial-crime-research/

Transaction Timeline:
https://sellina95.github.io/independent-financial-crime-research/timeline.html

Preserve:

- Independent On-Chain Research header
- Binance 14 · Master Flow Map
- Existing dark visual theme
- Existing fonts and colors
- Existing graph and arrows
- Existing node appearance
- Existing search and filters
- Existing Research Inspector
- Existing navigation
- Existing Transaction Timeline design

Add research features within the existing UI.

Do NOT replace the website with the previously
generated alternative dashboard mockup.

The failed STEP 40 research map is abandoned.

Do NOT use STEP 40 preview connections
as authoritative source evidence.

---

## 3. MASTER FLOW MAP REQUIREMENTS

Show:

- Ethereum Mainnet / Chain ID 1
- Plasma / Chain ID 9745
- ERC-20 transfers
- USDT and USDT0
- WETH
- Native ETH
- Internal ETH transfers
- DEX swaps
- Deposits and withdrawals
- Bridge activity
- Verified fund movements
- Unverified candidate routes

Visual distinction:

Verified transfers: solid arrows

Candidate routes: dotted arrows

DEX conversions: conversion annotations

Cross-chain activity: chain-aware links

Blacklist/freeze: node incident markers

Official actions: documented incident markers

A node may have multiple chronological incidents.

All eligible records must remain discoverable,
even when only a local neighborhood is displayed.

---

## 4. RESEARCH INSPECTOR REQUIREMENTS

Clicking a node should show:

- Chain and wallet address
- Wallet / contract classification
- Research label and provenance
- Incoming fund movements
- Outgoing fund movements
- Token contract and asset
- Raw amount and verified decimals
- Transaction hash
- Block number and event timestamp
- DEX swaps and WETH conversions
- Bridge activity
- Blacklist events
- Freeze / unfreeze events
- Relevant official FBI references
- Relevant OFAC designations
- Other verified official actions
- Evidence verification status
- Original source file and record location
- Research coverage and uncertainty

Do not conflate:

Blacklist != Freeze

Freeze != Recovery

Balance decrease != Recovery

FBI mention != OFAC designation

Official designation != Proof of criminal ownership

UNKNOWN != NOT LISTED

Every claim needs supporting evidence.

---

## 5. TRANSACTION TIMELINE

Keep the existing Transaction Timeline page.

Show chronological:

- Transfers
- DEX conversions
- WETH deposits and withdrawals
- Bridge activity
- Blacklist / freeze / unfreeze
- Verified official actions
- Research observations and hypotheses

Separate:

1. On-chain occurrence timestamp
2. Official announcement / effective timestamp
3. Research observation / verification timestamp

Timeline events must link to Master Flow Map
nodes and transactions using stable IDs.

Desired feature:

Time-based incident replay.

Later discoveries must not appear as facts
already known at earlier times.

---

## 6. REQUIRED SOURCE EXTRACTION

Extract when supported:

01. Source repository and Git commit
02. Original file path and SHA256
03. Original row / JSON pointer
04. Chain ID
05. TX hash
06. Block number
07. Timestamp
08. From address
09. To address
10. Token contract
11. Asset symbol
12. Decimals
13. Raw amount
14. Verified display amount
15. Log index
16. Internal trace identifier
17. Event type
18. Wallet / contract identity
19. Blacklist / freeze / designation records
20. Evidence verification status
21. Investigation block coverage
22. RPC failures and unresolved gaps

Never invent missing information.

---

## 7. CANONICAL DATA MODEL

MASTER_FLOW_DATA.json must contain:

- metadata
- nodes
- events
- candidate_routes
- node_incidents
- entity_claims
- source_references
- duplicate_groups
- audit

The file must preserve original evidence links.

Chain-aware address identity is mandatory.

Candidate routes must not be promoted
to verified movements without evidence.

Official identity claims require sourcing.

---

## 8. EVENT DEDUPLICATION

For ERC-20 transfer logs:

chain_id + tx_hash + log_index

Validate contract and event context.

For internal ETH:

chain_id + tx_hash + verified trace identifier

TX + from + to alone is NOT enough.

Different events inside one TX remain separate.

Transaction envelopes are not automatically
independent transfer events.

Preserve multiple supporting observations.

Avoid WETH / DEX economic double counting.

Do not assume matching cross-chain amounts
prove bridge-linked transfers.

Unresolved duplicates remain in the audit.

---

## 9. HISTORICAL BASELINE COUNTS

Prior research reported:

Tracked files: 3,105

Older extracted records: 13,486

Additional extracted candidates: 4,836

Combined extracted observations: 18,322

TX / from / to combinations: 5,304

Earlier research groups: 5,855

Discarded STEP 40 preview records: 11,754

NONE of these numbers is the final unique
on-chain transfer count or map connection count.

Required independently audited outputs:

- Total source files inspected
- Raw observations extracted
- Transaction envelopes
- Unique atomic transfer events
- Unresolved duplicates
- Verified transfer events
- Candidate routes
- DEX / bridge / administrative events
- Unique chain-aware addresses
- Unique directed wallet pairs
- Displayable graph connections
- Source coverage and exclusions

Unique events and displayable edges
must be counted separately.

---

# 10. IMPLEMENTATION CHECKLIST

Only mark [x] after successful verification.

Every completed phase must reference
its audit evidence and results.

## PHASE 1 — SOURCE INVENTORY

- [x] Confirm pinned source commit
- [x] Recount all tracked source files
- [x] Classify JSON / CSV / JSONL
- [x] Review documents and HTML
- [ ] Identify raw versus derived evidence
- [ ] Identify all extraction schemas
- [x] Account for unsupported source formats
- [ ] Record disposition of every file
- [x] Validate inventory coverage

Acceptance:
All source files accounted for.

## PHASE 2 — EXTRACTION

- [ ] Extract transaction metadata
- [ ] Extract ERC-20 logs
- [ ] Extract native ETH movements
- [ ] Extract internal ETH traces
- [ ] Extract Bitquery evidence
- [ ] Extract Alchemy evidence
- [ ] Extract Blockscout evidence
- [ ] Extract DEX / WETH activity
- [ ] Extract bridge / Plasma activity
- [ ] Extract blacklist / freeze records
- [ ] Extract documented official actions
- [ ] Preserve original source references
- [ ] Audit unsupported or missing fields

Acceptance:
Relevant source observations accounted for.

## PHASE 3 — NORMALIZATION

- [ ] Normalize chain IDs
- [ ] Normalize addresses by chain
- [ ] Normalize TX and block identifiers
- [ ] Normalize token contracts and amounts
- [ ] Separate TX envelopes from transfers
- [ ] Establish atomic event identity
- [ ] Reconcile provider duplicates
- [ ] Preserve distinct same-TX events
- [ ] Prevent economic double counting
- [ ] Report unresolved conflicts
- [ ] Audit unique transfer/event counts
- [ ] Audit displayable graph connection counts

Acceptance:
Event and connection totals reconciled.

## PHASE 4 — INCIDENT CONTEXT

- [ ] Attach verified address activities
- [ ] Add blacklist events
- [ ] Add freeze / unfreeze events
- [ ] Separate frozen and recovered balances
- [ ] Cross-check official FBI material
- [ ] Cross-check OFAC material
- [ ] Preserve attribution uncertainty
- [ ] Attach candidate routes separately
- [ ] Validate event and announcement times

Acceptance:
All incident claims evidence-linked.

## PHASE 5 — CANONICAL DATASET

- [ ] Generate MASTER_FLOW_DATA.json
- [ ] Validate required data sections
- [ ] Validate source reference integrity
- [ ] Validate unique event identifiers
- [ ] Validate chain separation
- [ ] Validate duplicate groups
- [ ] Validate source coverage
- [ ] Validate amount accounting
- [ ] Record final event and edge counts
- [ ] Report unresolved evidence gaps

Acceptance:
Canonical dataset passes audit.

## PHASE 6 — WEBSITE INTEGRATION

- [ ] Preserve Master Flow Map design
- [ ] Preserve Transaction Timeline design
- [ ] Preserve existing navigation
- [ ] Preserve Research Inspector styling
- [ ] Add chain and event filters
- [ ] Add blacklist / freeze annotations
- [ ] Add verified official actions
- [ ] Add original evidence drill-down
- [ ] Link map and timeline event IDs
- [ ] Verify all approved data is discoverable
- [ ] Validate large-network performance
- [ ] Perform visual regression tests
- [ ] Complete publication readiness audit
- [ ] Obtain explicit user approval to publish

Acceptance:
No unauthorized redesign or publication.

---

# 11. BRANCH AND PUBLICATION POLICY

Research branch:
research/case-binance-2026

Public website branch:
main

Never:

- Modify original research evidence without approval
- Push unfinished research to main
- Change the existing website without approval
- Treat an analysis hypothesis as verified fact
- Report unverified transfer totals as final
- Mark checklist items complete without audit evidence
- Change the frozen design without user approval

Research commits are not publication approval.

---

# 12. CURRENT STATUS

DESIGN: APPROVED

PHASE 1: NOT COMPLETED

PHASE 2: NOT COMPLETED

PHASE 3: NOT COMPLETED

PHASE 4: NOT COMPLETED

PHASE 5: NOT COMPLETED

PHASE 6: NOT COMPLETED

FINAL UNIQUE TRANSFER COUNT: UNKNOWN

FINAL UNIQUE MAP CONNECTION COUNT: UNKNOWN

PUBLICATION: NOT APPROVED

NEXT ACTION:

PHASE 1 source inventory and schema audit.
