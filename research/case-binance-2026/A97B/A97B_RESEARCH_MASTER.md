# A97B — Independent On-Chain Forensic Case Study

**Case:** Binance 2026 — A97B Non-Central Route  
**Address:** `0xa97bf7836f8a08f9ed91d41453d371493fae8d10`  
**Research branch:** `research/case-binance-2026`  
**Baseline commit:** `4f341da`  
**Status:** Research in progress — not approved for publication

---

## 0. Research Mission

Reconstruct the observed movement of assets involving A97B,
evaluate the strength of the incident-attribution evidence,
and examine the timing and effectiveness of relevant
address designations and asset restrictions.

The final objective is an evidence-based LinkedIn research
publication understandable to non-specialists and reviewable
by financial crime investigators.

### Research boundaries

- Separate on-chain observations from external attribution.
- Do not assume all A97B assets originated from the incident.
- Distinguish address listing from actual token freezing.
- Do not equate ERC-20 Transfer logs with verified balance changes.
- Do not infer ownership from transaction patterns alone.
- Record unresolved questions as UNKNOWN.
- No publication without final evidence review and approval.

---

# PART I — RESEARCH AUDIT

## 1. Incident Attribution

**Status: IN PROGRESS**

### Research question

Which observed A97B inflows and outflows can be attributed
to the Binance incident, and where does the evidence stop?

### Existing evidence

- Binance 14 is an observed direct source of A97B Transfer events.
- STEP 65 identified 124 ledger rows mentioning A97B.
- These are event records, not 124 independently verified
  economically meaningful transfers.
- A97B also received funds from other sources.
- A97B's 10,647.2 ETH direct outflows are verified transactions,
  but full incident-fund provenance is not established.
- A97B appears in the supplied Elliptic address list.
- Elliptic listing is an external attribution, not independent
  proof that all assets at the address were stolen.

### Required verification

- [ ] Verify the earliest relevant Binance 14 → A97B inflow.
- [ ] Separate reliable asset movements from nonstandard events.
- [ ] Reconstruct other identified inflow sources and coverage.
- [ ] Review temporal ordering of inflows and outflows.
- [ ] Evaluate mixed-fund attribution limits.
- [ ] Document confirmed, inferred and unknown incident links.

### Evidence references

- `evidence/binance14_all_receivers_census_v1/step65_direct_receiver_route_register_v1/`
- `evidence/binance14_all_receivers_census_v1/step72_a97b_pattern_funding_audit_v1/`
- `evidence/binance14_all_receivers_census_v1/step83_official_attribution_crosswalk_v1/`
- `GATE_2_INCIDENT_ATTRIBUTION_MATRIX_V2.csv`

---

## 2. Restriction Timeline

**Status: NOT VERIFIED FOR A97B**

### Research question

When were relevant addresses designated, listed or restricted,
and what technical restrictions actually applied?

### Distinctions required

1. FBI public incident-related address designation
2. Elliptic risk/blocklist inclusion
3. Exchange or service-level restrictions
4. Token issuer on-chain blacklist or freeze
5. Actual asset balance and transferability

These are separate evidence categories.

### Required verification

- [ ] Record FBI publication timestamp and source.
- [ ] Determine whether address-specific listing time is available.
- [ ] Record Elliptic snapshot time and provenance.
- [ ] Identify any applicable token issuer freeze transactions.
- [ ] Verify the targeted address, token, block and transaction.
- [ ] Record balances where technically verifiable.
- [ ] Mark unavailable listing timestamps as UNKNOWN.

### Existing external-list observations

- A97B: Elliptic direct listing
- 3,000 ETH recipient: Elliptic direct listing
- 7,647 ETH recipient: FBI and Elliptic direct listing
- These listings do NOT establish token freezes.

### Evidence references

- `evidence/binance14_all_receivers_census_v1/step83_official_attribution_crosswalk_v1/`
- `OFFICIAL_INCIDENT_EVIDENCE_REGISTER_V1.csv`
- `USDT_FREEZE_TIMELINE_CHECKPOINT_V4.md`

Existing freeze research for other addresses must not be
automatically attributed to A97B.

---

## 3. Post-Restriction Activity

**Status: NOT STARTED**

### Research question

Did A97B or the relevant receiving addresses show additional
asset inflows or outflows following a verified restriction?

### Required verification

- [ ] Define restriction events and exact time boundaries.
- [ ] Separate listing date from actual execution time.
- [ ] Check incoming events after each relevant boundary.
- [ ] Check outgoing events after each relevant boundary.
- [ ] Match token contract and chain.
- [ ] Check transaction index within the same block.
- [ ] Separate native ETH movements from ERC-20 logs.
- [ ] Verify balances where possible.
- [ ] Distinguish continued activity from restriction failure.

### Known scope limitation

The existing A97B outgoing ledger covers recorded events
from 2026-10-30 01:17:47 UTC through 09:16:35 UTC.

This does not establish complete later activity or prove
absence of subsequent transfers.

### Evidence references

- `evidence/binance14_all_receivers_census_v1/step70_a97b_forward_census_v1/`
- `evidence/binance14_all_receivers_census_v1/step81_a97b_remaining_60_audit_v1/`

---

## 4. Conservation & Evidence Closure

**Status: STRUCTURAL AUDIT PASS / PROVENANCE OPEN**

### Established event reconciliation

| Event structure | Count |
|---|---:|
| DEX/WETH-compatible events | 1,126 |
| Direct native ETH transfers | 4 |
| Other DEX router patterns | 3 |
| ERC-20 exceptions | 53 |
| Total indexed events | 1,186 |

STEP 80 reports 1,184 distinct outer transaction hashes.
Event counts and transaction counts are not interchangeable.

### ERC-20 exception subgroups

| Structure | Events |
|---|---:|
| Direct transfer structure | 28 |
| External caller / transfer selector | 17 |
| Other function selectors | 8 |
| Total | 53 |

All 53 have matching cached receipt events.

Some nonstandard token events lack independently verified
balance changes. No unsupported economic-flow claims.

### Direct ETH evidence

Four direct native ETH transactions:

- 3,000 ETH → `0xc2096a12ebe0944f4d39e59979f485afd92d850a`
- 0.1 ETH → `0xa3b3dee870f01560fdbe5af659c9c9135748886f`
- 0.1 ETH → `0x54401f80da97893a15d43566184635b6674bc942`
- 7,647 ETH → `0x54401f80da97893a15d43566184635b6674bc942`

Total: **10,647.2 ETH**, three immediate recipients.

This total is NOT an independently proven stolen-fund amount.

### Closure checklist

- [x] Indexed outgoing event-count reconciliation
- [x] Direct native ETH transaction matching
- [x] ERC-20 exception receipt matching
- [x] FBI / Elliptic address-level crosswalk
- [ ] Incident-specific source attribution
- [ ] Restriction-event and timeline crosswalk
- [ ] Post-restriction inflow/outflow review
- [ ] Final asset-level conservation assessment
- [ ] Explicit UNKNOWN register
- [ ] Publication claim audit

### Evidence references

- `evidence/binance14_all_receivers_census_v1/step80_a97b_full_dex_census_v1/`
- `evidence/binance14_all_receivers_census_v1/step84_a97b_erc20_exception_audit_v1/`
- `evidence/binance14_all_receivers_census_v1/step85_a97b_final_event_audit_v1/`

---

# PART II — LINKEDIN RESEARCH STORYBOARD

**Publication status: DRAFT FRAMEWORK — NOT APPROVED**

## 01 — What happened?

Explain the broader incident context and locate A97B
within the independently observed Binance 14 route.

Separate overall incident figures from the A97B
research dataset.

**Evidence gate:** official source verification and
incident-specific linkage.

## 02 — How did funds move?

Create an accessible transaction network showing:

- Binance 14 → A97B observed connection
- A97B's mixed-source funding
- 1,126 DEX/WETH-compatible events
- 10,647.2 ETH in direct native transfers
- Repeat recipients and execution patterns
- Known and unknown economic-flow boundaries

**Evidence gate:** source-to-outflow attribution
must not exceed what the data supports.

## 03 — What was restricted, and what happened afterward?

Create a time-ordered comparison of:

- Official address designation
- Private risk-list inclusion
- Actual token issuer restriction
- Verified inflows and outflows
- Balances and transaction-order evidence

**Evidence gate:** avoid calling a listing a freeze.

## 04 — Has this pattern appeared before?

Compare one or two earlier documented incidents.

Evaluate similarities and differences in:

- Flow concentration
- DEX interaction
- Repeated address usage
- Address-based restrictions
- Observed post-restriction activity

**Status: DEFERRED**

Do not select comparisons solely because
they visually resemble this case.

## 05 — What does this reveal about financial infrastructure?

Evaluate evidence-supported implications for:

- Address-based transaction monitoring
- Token issuer restrictions
- Smart-contract and DEX observability
- Mixed-fund attribution limitations
- Operational response timing

Distinguish verified control outcomes
from hypotheses and recommendations.

---

# PART III — CLAIM REGISTER

| Proposed claim | Status |
|---|---|
| 1,186 indexed A97B movement events reconciled | CONFIRMED WITHIN DATASET |
| 1,126 events match DEX/WETH patterns | PATTERN-BASED |
| 10,647.2 ETH directly transferred | CONFIRMED |
| All 10,647.2 ETH attributable to incident | UNKNOWN |
| A97B appears in Elliptic supplied list | CONFIRMED IN SNAPSHOT |
| 7,647 ETH recipient appears in FBI/Elliptic lists | CONFIRMED IN SNAPSHOTS |
| A97B assets were frozen | NOT VERIFIED |
| Relevant transfers occurred after a verified freeze | NOT VERIFIED |
| All ERC-20 events represent real balance changes | NOT ESTABLISHED |

---

# PART IV — NEXT RESEARCH ACTION

**STEP 86B — A97B Inflow & Incident Attribution Audit**

Priority:

1. Review STEP 65's 124 A97B-related event rows.
2. Reuse STEP 72 funding evidence.
3. Identify verified inflow origins and time ordering.
4. Distinguish event-only records from validated asset movement.
5. Establish the strongest defensible incident-attribution claim.

No existing evidence should be moved, overwritten or recreated.

Update this master file only after verified new findings.

**Publication gate:** Explicit approval required.
**Main branch:** Protected.


---

## A97B Evidence Closure Checkpoint — 2026-11-08

### 1. Incident Attribution

**Status: EXTERNAL ADDRESS LINK CONFIRMED / FUND PROVENANCE UNKNOWN**

- A97B appears in the preserved Elliptic incident-address snapshot.
- The FBI source snapshot does not directly list A97B.
- Binance 14 → A97B: two Alchemy-recorded internal ETH movements,
  totaling 3,090.401960150360151765 ETH by raw-value decoding.
- These internal ETH movements have not been independently
  revalidated in this checkpoint.
- A97B has mixed-source funding.
- No claim that the entire 10,647.2 ETH of observed direct outflows
  is attributable to the incident.

### 2. Restriction Timeline

**Status: ADDRESS LISTING VERIFIED / ACTUAL FREEZE NOT VERIFIED**

- Elliptic direct address-list match: confirmed in preserved snapshot.
- First-added listing timestamp: UNKNOWN.
- A97B-specific issuer blacklist or freeze transaction: NOT VERIFIED.
- Relevant ETH recipient address listings are not evidence of freezing.
- Existing USDT freeze research for other wallets cannot be applied
  to A97B without address-specific transaction evidence.

### 3. Post-Restriction Activity

**Status: UNKNOWN**

- Existing A97B outgoing ledger spans
  2026-10-30 01:17:47 UTC to 09:16:35 UTC.
- 1,186 indexed outgoing movement events were reconciled.
- A verified A97B restriction execution timestamp is unavailable.
- Later wallet coverage has not been established.
- Post-listing or post-freeze movements cannot be inferred
  from the current dataset.

### 4. Conservation & Evidence Closure

**Status: STRUCTURAL PASS / ECONOMIC PROVENANCE OPEN**

- Outgoing event reconciliation: 1,186 / 1,186.
- DEX/WETH-compatible patterns: 1,126 events.
- Direct native ETH transfers: 4 transactions / 10,647.2 ETH.
- Other router patterns: 3 events.
- ERC-20 exceptions: 53 events.
- Address-level external listing crosswalk: 6 of 124 research
  addresses matched at least one preserved external list.
- Full asset-level inflow/outflow conservation: NOT ESTABLISHED.
- Actual balance effects of selected nonstandard ERC-20 events:
  NOT ESTABLISHED.
- Specific incident-fund attribution: UNKNOWN.

### Publication Claim Boundary

**Supported for a research report:**
- Observed transaction structure and reconciled event counts.
- Direct ETH transfer amounts and immediate recipients.
- Elliptic/FBI address-list matches, with source attribution.
- Evidence gaps in fund provenance and restriction verification.

**Not supported:**
- All A97B transfers were stolen incident funds.
- A97B assets were frozen.
- Transfers continued after a verified A97B freeze.
- Address-listing proves wallet ownership.
- A97B demonstrates failure of issuer freeze controls.

### Next Reporting Action

Prepare the five-section LinkedIn research report:

1. What happened?
2. How did funds move?
3. What was restricted — and what happened afterward?
4. Has this pattern appeared before?
5. What does this reveal about financial infrastructure?

Section 4 requires separately verified historical comparisons.
The other sections must distinguish observations,
external attribution, inference and unknowns.

**Research status: EVIDENCE-BOUNDED CHECKPOINT**
**Publication status: NOT APPROVED**

---

## External Incident Attribution Update — 2026-11-08

This update supersedes the earlier blanket UNKNOWN
classification for the Binance 14 → A97B incident link.
Earlier text is retained as an audit trail.

### Updated findings

- Binance 14 compromise: OFFICIALLY REPORTED.
- Binance 14 → A97B ETH inflows:
  STRONGLY CORROBORATED INCIDENT ASSOCIATION.
- Two observed inflows:
  128.491139212075057017 ETH and
  2961.910820938285094748 ETH.
- Combined observed inflow:
  **3090.401960150360151765 ETH**.
- A97B Elliptic incident-list inclusion:
  CONFIRMED IN PRESERVED SNAPSHOT.
- The 7647 ETH recipient:
  FBI AND ELLIPTIC ADDRESS-LIST MATCH.
- All 10647.2 ETH outflows as stolen funds:
  NOT ESTABLISHED.
- A97B-specific freeze:
  NOT VERIFIED.
- Post-freeze movement:
  UNKNOWN.

### New evidence register

`research/case-binance-2026/A97B/evidence/EXTERNAL_ATTRIBUTION_V1.md`

The incident link is supported by official
reporting and independent external corroboration.

Exact source-fund allocation through mixed
ETH balances remains unresolved.

Publication: NOT APPROVED.
