# AXIOM — Evidence Gap Report
## Binance 2026 | Independent Financial Crime & Fund-Preservation Research

**Status:** ACTIVE RESEARCH CHARTER — NOT A COMPLETED FORENSIC FINDING  
**Evidence cutoff:** 2026-11-05
**Working branch:** `research/case-binance-2026`  
**Publication gate:** No changes to `main` or the existing public report without explicit approval after audit.

> **North-star question:** What remains materially unexplained or independently unverified in the public account of the 2026 Binance incident, and can public evidence resolve that gap in a way useful to asset preservation, financial-crime investigation, or security controls?

## 1. Mission and boundaries

We are not repeating institutional announcements, maximizing transaction counts, or attempting to identify people behind wallets. We are producing **independently reproducible evidence, explicit gaps, and actionable but cautiously scoped research findings**. A published institutional claim is not automatically ground truth; a difference from it is not evidence of an omission unless source scope, cutoff, asset, chain, definitions, and valuation basis match.

Use `OBSERVED`, `REPORTED_BY_SOURCE`, `INFERRED`, `UNKNOWN`, `DISPROVEN` on every material claim. Separate **address designation, enforceable transfer restriction, execution-time balance, block-end balance, post-blacklist inflows, interception, recovery, and loss**. Never infer real-world ownership from address labels. Never count repeated intermediaries as new stolen funds.

Use lawful public evidence and read-only analysis. No exploit replication or unsupported actor attribution.

## 2. Existing evidence checkpoint (not a new discovery)

| Case | Blacklist block | Recorded USDT at block end | Status |
|---|---:|---:|---|
| Central `0x5227f603c1ee34ce3c06efe6477003bdfccb2f8c` | 26300954 | 971,149,299.483240 | Saved receipt/event/balance and SHA256 local consistency PASS; independent archive replay pending |
| 175M branch `0xaa246bf639586a6ba46762d378ce50ca4fc654a0` | 26301021 | 174,999,872.327520 | Saved event and historical balances; execution-instant trace pending |
| 30M branch `0xb171ca86f82070282138352ff7111b494060c8c3` | 26301041 | 30,000,000.000000 | Saved event/balances; independent replay pending |

**Arithmetic sum: 1,176,149,171.810760 USDT. This is not the incident-wide frozen total, not recovered value, and not a globally de-duplicated same-time estimate.** These snapshots come from three different blocks.

Preserved flow evidence includes Central → 500M → 175M branch and Central → 200M → 190M → 130M → 80M → 30M branch. The 190M transfer's original receipt was checked: `0xc0fab33d0ec562d3feef6b23946402b1af80dade21ab4f5fbea7384cc4615183`, block 26300911, status 1. Further path-level conservation is pending. PublicNode and 1RPC returned HTTP 403 from the working environment: label `RPC_ACCESS_BLOCKED`, not blockchain contradiction. Etherscan **Total Supply** cannot verify a wallet-specific historical balance.

Existing source directories: `evidence/central_blacklist_audit_v1/`, `evidence/blacklist_balance_175m_v1/`, `evidence/blacklist_event_175m_v1/`, `evidence/30m_blacklist_audit_v1/`, `evidence/root_usdt_outflows_v1/`, `evidence/second_hop_receipts_v1/`, `evidence/30m_upstream_bridge_v1/`. Key reports: `USDT_FREEZE_TIMELINE_CHECKPOINT_V4.md`, `BLACKLIST_175M_CASE_AUDIT_V1.md`. Raw original evidence takes precedence over older narrative claims when they conflict; do not silently edit the older document.

## EG-01 — Blacklist Execution-Time Balance Audit

**Status: SUBSTANTIALLY VERIFIED**
**Evidence classification: OBSERVED + STRONGLY INFERRED**

### Verification results

| Address | Blacklist block | TX index | USDT balance | Result |
|---|---:|---:|---:|---|
| Central | 26300954 | 88 | 971,149,299.483240 | PASS |
| 175M recipient | 26301021 | 199 | 174,999,872.327520 | PASS |
| 30M recipient | 26301041 | 13 | 30,000,000.000000 | PASS |

All three addresses passed:

- Successful blacklist transaction receipt.
- Matching USDT blacklist event.
- Identical previous-block and blacklist-block ending balances.
- Zero target-related USDT Transfer events in blacklist block.
- Block-level balance reconciliation PASS.

**OBSERVED:** Historical balances, transaction receipts,
blacklist events and block-wide Transfer logs.

**STRONGLY INFERRED:** Execution-instant USDT balances matched
the corresponding block-end balances.

**REMAINING LIMITATION:** Direct intra-transaction state
reconstruction and independent provider confirmation.

**CRITICAL:** These balances were observed at different blocks.
Their sum must not be represented as an incident-wide frozen
or recovered total without EG-03 conservation analysis.

Evidence:
`evidence/eg01_execution_time_v1/manifest.json`

Detailed audit:
`EG01_EXECUTION_TIME_AUDIT_V1.md`

---

## EG-03 — Time-Indexed Conservation and Double-Counting Audit

**Status: PARTIAL PASS — scope-limited conservation verified**

### Synchronized USDT snapshots

| Address | Block 26301041 | Block 26301167 |
|---|---:|---:|
| Central | 975,066,939.251167 | 1,175,464,711.075362 |
| 175M recipient | 174,999,872.327520 | 174,999,872.327520 |
| 30M recipient | 30,000,000.000000 | 30,000,000.000000 |
| **Three-address total** | **1,180,066,811.578687** | **1,380,464,583.402882** |

All snapshots are Ethereum USDT end-of-block balances.
These totals are NOT incident-wide frozen or recovered assets.

### Verified intermediate distribution

| Wallet | Verified incoming | Verified outgoing | End balance at block 26301041 |
|---|---:|---:|---:|
| 190M receiver | 190M | 10M + 50M + 130M = 190M | 0 |
| 130M receiver | 130M | 50M distributed + 80M = 130M | 0 |
| 80M receiver | 80M | 50M distributed + 30M = 80M | 0 |

The three intermediate wallets do not retain the previously
suspected 160M USDT at either synchronized snapshot.

**OBSERVED:** Corresponding USDT Transfer logs, successful
saved receipts for the previously traced path, and historical
balances for the three intermediate wallets.

**RECONCILED:** The specified upstream inflows and the queried
outgoing Transfer events account for the 190M, 130M, and 80M
intermediate distributions through block 26301041.

**NOT ESTABLISHED:** Final destination, restriction status,
recovery, or ownership of the distributed funds; incident-wide
conservation or completeness across every affected wallet.

### EG-03 recipient blacklist checkpoint

Historical Ethereum USDT `isBlackListed(address)` at block 26301167.
These are address restrictions, NOT recovered-asset amounts.

| Receiving address | Branch inflow | Blacklist status |
|---|---:|---|
| `0x56534741cd8b152df6d48adf7ac51f75169a83b2` | 13.54M USDT | NOT BLACKLISTED |
| `0x9db9e0e53058c89e5b94e29621a205198648425b` | 7.52M USDT | NOT BLACKLISTED |
| `0x11b815efb8f581194ae79006d24e0d814b7697f6` | 4.15M USDT | NOT BLACKLISTED |
| `0xc7bbec68d12a0d1830360f8ec58fa599ba1b0e9b` | 1.96M USDT | NOT BLACKLISTED |
| `0x0d4a11d5eeaac28ec3f61d100daf4d40471f1852` | 1.61M USDT | NOT BLACKLISTED |
| `0x3416cf6c708da44db2624d63ea0aaef7113527c6` | 0.93M USDT | NOT BLACKLISTED |
| `0x3041cbd36888becc7bbcbc0045e3b1f144466f5f` | 0.33M USDT | NOT BLACKLISTED |
| `0xc5af84701f98fa483ece78af83f11b6c38aca71d` | 0.15M USDT | NOT BLACKLISTED |

The three largest recipients (60M, 37.74M, 32.07M USDT)
were separately checked at this block and were NOT BLACKLISTED.
Central was BLACKLISTED and served as a positive control.

**LIMITATION:** No claim that received tokens remained in these
addresses, were recoverable, or were attributable to one owner.
Source: `evidence/eg03_recipient_blacklist_v1.json`.

### Next acceptance tests

1. Deduplicate Transfer events by transaction hash and log index.
2. Trace recipient overlap and later movements of distributed funds.
3. Verify blacklist state for relevant terminal addresses.
4. Compare synchronized, scope-defined balances without adding
   historical transfer amounts to current holdings.
5. Preserve original RPC responses and evidence hashes for the
   new queries before institutional submission.

---

## 3. Research gap register — prioritized

| ID | Research question | Current evidence | Acceptance test | Priority |
|---|---|---|---|---|
| EG-01 | How much USDT was actually present **at each blacklist execution instant**? | **SUBSTANTIALLY VERIFIED** — three addresses: blacklist receipts/events, block-wide Transfer reconciliation, adjacent-block balances PASS; execution-instant balances strongly inferred, not directly traced | Same chain/token/address/receipt; intra-block ordering; full Transfer reconciliation and trace where needed; distinguish inferred vs observed execution-time balance | **P0** |
| EG-02 | What **post-blacklist inflows** changed later restricted balance? Is restricted value distinct from initial balance and recovered assets? | **SCOPED RECONCILIATION PASS** — Central, blocks 26300955–26301167: 204,315,411.592122 USDT inbound, zero outgoing Transfer events, ending balance 1,175,464,711.075362 USDT; difference 0; evidence committed in `eg02_central_post_blacklist_ledger_v1/` | Independent second-provider replay; execution-time rather than block-end state; wider address/chain coverage; distinguish balance increase from recovery | **P0** |
| EG-03 | Are three event-time address balances double counted or incomparable because of asynchronous snapshots? | **PARTIAL PASS** — synchronized balances and three intermediate-wallet distributions reconciled; downstream recipient coverage and restriction status remain open | Time-indexed conservation, synchronized snapshots where possible, recipient-identity and transfer-link checks; report scope-specific estimate only | **P0** |
| EG-04 | Does a genuine discrepancy persist against institutional freeze numbers after basis normalization? | Not established | Normalize UTC cutoff, chain, token, pricing, frozen/intercepted/recovered definitions; verify underlying receipt evidence and alternative explanations | P1 |
| EG-05 | What do **64 attempts / 37 failures** refer to, and why did they fail? | **Population and denominator unverified** | Locate original claim/dataset; classify external tx vs internal call vs batch item, status, revert, nonce, gas, execution environment; compare with officially reported 50 signing transactions without equating counts | **P1** |
| EG-06 | Did delegated execution or asset movement continue after Binance's withdrawal suspension became effective? | **PARTIAL — CURRENT PRIORITY**. T02/T03/T17 technical linkage is documented; TechCrunch reports public confirmation by 22:27 UTC; Binance retrospectively reports a final 2,961.9 ETH transfer finalized at 23:56 UTC and delegation removal at 00:10 UTC. The 22:39:35 UTC candidate remains explorer-reported and not independently replayed. Exact internal suspension cutoff is UNKNOWN. | Authenticate the actual suspension cutoff; independently retrieve candidate transaction, receipt, trace and historical delegation state from two providers; compare broadcast, inclusion and finalization separately | **P0** |
| EG-07 | Can a TRM-reported **TRON pool / self-minted-token / receipt-token value transfer** be reproduced independently? | TRM's public account, not independently reproduced | One bounded route, raw pool/token events, liquidity, mint/sell/redeem, accounting and falsification test | P2 |
| EG-08 | Can chained **cross-chain bridge** value links be established rather than guessed from amount/time similarity? | Not reproduced | Bridge IDs, deposit/withdrawal events, token changes, fees, plausible competing matches; uncertainty labels | P2 |

**Updated sequence (2026-11-05):** EG-01–03 now have scoped checkpoints, with EG-02 at SCOPED RECONCILIATION PASS and EG-03 still PARTIAL. EG-06 is the immediate priority because the internal withdrawal-suspension cutoff remains UNKNOWN. EG-05's external 64/37 population remains open. EG-04, EG-07 and EG-08 remain deferred behind a decisive EG-06 test and bounded reconciliation work. Unavailable archive-RPC access must be recorded, not endlessly retried and not declared PASS.

## 4. Public-source comparison ledger — cutoff 2026-11-05

- **Binance, November 3, 2026:** reported a compromise involving wallet-signing service, EIP-7702 delegation, 50 signing transactions, MPC-related complexity in revocation, final unauthorized transfer confirmation at 23:56 UTC on October 29 and removal of delegation at 00:10 UTC October 30. Reported figures and causal account remain attributed to Binance until independently verified. Source: https://www.binance.com/fr-AF/blog/community/3229153443759566763
- **TRM Labs, November 3, 2026:** described self-minted TRON tokens, liquidity pools, lending receipt tokens and chained bridges as economic-value transfer patterns. Independently reproduce one bounded case before treating specific inferred wallet linkages as facts. Source: https://www.trmlabs.com/resources/blog/binance-hack-update-north-korea-launders-proceeds-through-self-minted-tokens-and-chained-bridges
- **FBI, Elliptic, Bitquery and additional sources:** register each exact source URL, publication timestamp, asset/chain/time cutoff, confidence and quoted claim before comparison; do not allege that an institution missed something without a supported like-for-like discrepancy. An institution's lack of public disclosure does not establish lack of internal investigation.

## 5. Required audit template for each research question

1. **Decision relevance:** How could the answer change asset preservation, investigation, or security controls?
2. **Claim and source:** direct URL, publisher, publication UTC, collection UTC, chain/token/block/tx/log index and file hashes.
3. **Population and temporal basis:** explicit inclusions, exclusions, block-end vs execution instant, currency units and token decimals.
4. **Raw observation:** immutable transaction, receipt, event and historical-state evidence; capture RPC errors as evidence of availability, not of blockchain state.
5. **Classification:** `OBSERVED` / `REPORTED_BY_SOURCE` / `INFERRED` / `UNKNOWN` / `DISPROVEN`.
6. **Conservation and red-team:** check repeated hops, token transformations, loan receipts, bridge payouts, fees, alternatives, false address matches and missing sources.
7. **Verdict:** `CONFIRMED_EXISTING`, `OPEN_GAP`, `MATERIAL_DISCREPANCY_REPLICATED`, `DISPROVEN`, or `STOP_LOW_VALUE`.
8. **Next cheapest decisive test and stopping rule:** do not spend more time on already validated arithmetic.

## 6. Research gates and stopping conditions

**Phase 1 — Fund preservation / EG-01–03:** Scoped checkpoints now exist. EG-01 is substantially verified with execution-instant state still inferred; EG-02 has a scoped Central post-blacklist ledger reconciliation pass; EG-03 has scoped conservation checkpoints but attribution and downstream coverage remain unresolved. Independent replay and wider-population completeness remain open. Do not call the incident-wide freeze figure verified.

**Phase 2 — Control failure / EG-05–06:** T02/T03/T17 technical work is already documented and must not be repeated. EG-06 now concerns the independently defensible internal withdrawal-suspension cutoff and whether any relevant delegated asset movement occurred after it. EG-05 remains open only for the external `64 attempts / 37 failures` population and denominator. Treat the 50 official signing transactions as a **different population until proven otherwise**. Never infer causes of failed operations from a single `status` flag.

**Phase 3 — TRON / cross-chain value transfer / EG-07–08:** Select one public, high-confidence, falsifiable example. Require a full value-conservation narrative and distinguish identity-free economic linkage from proven wallet control. Stop if amount and timing are the only evidence.

**Opportunity-cost gate:** Any proposed extension must state new information expected, how it might alter a decision, effort, and a stop rule. Reproducing an already established result with no incremental validation value is lower priority than resolving a material gap.

## 7. External-use deliverables

**Forensic Evidence Package:** immutable raw evidence, method, queries, checksums, exact UTC points, linked transactions, source registry, ledger, limitations, red-team tests.

**Institutional Research Brief (1–2 pages):** what was public, what was independently reproduced, what's unresolved or materially different, practical decision relevance and one precise follow-up; include direct reproducible sources.

**Route by type of result:** a new actionable, verifiable investigative lead → appropriate official law-enforcement tip channel; method/reproducibility finding → blockchain-intelligence research team; defensible incident-control insight → affected security/incident-response contact. Do not send generic bulk outreach or imply a discovery that has not passed the audit. External response/use is never guaranteed.

## 8. GitHub publication protection — mandatory

- Commit unfinished audit work only to `research/case-binance-2026`, after checking branch and worktree.
- Never push ongoing research directly to `main`; `main` accepts only **completed, audited, explicitly approved** work.
- Do not edit the existing public report or `publication/binance-2026-v1` without separate explicit approval.
- Store new evidence as versioned additions with SHA256 and manifests; do not overwrite raw evidence.
- The charter is stable. Change its mission, ordering or verification gates only with a documented reason and explicit approval. Findings belong in separate evidence/checkpoint files.

## 9. Immediate next actions — updated 2026-11-05

1. **EG-06 (P0):** establish an authenticated, UTC-normalized withdrawal-suspension cutoff. Separate public announcement, internal suspension, transaction broadcast, block inclusion and final asset movement. Independently replay the 22:39:35 UTC candidate before drawing any post-suspension conclusion.
2. **EG-03 (P1):** reproduce STEP 60–66 from archived/raw RPC evidence and resolve the differing accounting boundaries; do not merge the two conditional models.
3. **STEP 76 (P1):** decide whether the 114,589.789942 USDT counterparty match warrants a bounded extension of the pre-incident scan. The current 1,000-block result remains partial, not a seven-day audit.
4. **EG-05 (P1):** identify the original source and denominator for the external 64 attempts / 37 failures claim. Keep it separate from the observed 64 ERC-20 calls / 63 Transfer events / one reverted child call.
5. Defer EG-04 normalization and broad EG-07/08 expansion until a decisive test or material new evidence justifies the effort.

**Success is not finding more wallets. Success is resolving a material evidence gap with a result another investigator can verify, challenge, and use.**

### EG-01 audit checkpoint

**SUBSTANTIALLY VERIFIED** — three blacklist addresses.
Block-level receipt, Transfer-log and historical balance checks PASS.
Execution-instant balances remain strongly inferred rather than
directly observed through intra-transaction tracing.

See `EG01_EXECUTION_TIME_AUDIT_V1.md` and
`evidence/eg01_execution_time_v1/manifest.json`.

### EG-03 · Two-Address Consolidation Audit (Research Checkpoint)

**Scope:** A `0xb8734a14fbd4aa2d44e6aa830405ffc861ba313c`
and B `0x1c3b25019ed4e4876e7af7903cc3e1e23287c337`.

**Period:** Ethereum blocks 26306503–26311867.

**OBSERVED / independently rechecked in this checkpoint**
- Combined USDT balance at baseline: 80,265,235.424359.
- Combined USDT balance at end: 265,245.424479.
- B → A: 50,000,000 and 28,000,000 USDT, verified in receipts.
- A → `0x6c96de32cea08842dcc4058c14d3aaad7fa41dee`:
  28,000,000 USDT, confirmed in USDT Transfer log.
- Earlier A → B transfer of 25,000,000 USDT: receipt rechecked.

**RECONCILED FROM EARLIER TERMINAL AUDIT**
- Internal transfers during the consolidation period: 78,000,000 USDT.
- External inflows: 0.000120 USDT.
- External outflows: 79,999,990.000000 USDT.
- Group net movement: -79,999,989.999880 USDT.
- Balance reconciliation difference: 0 USDT.
- Earlier full audit reported 14 unique Transfer events.
- The complete 14-event population was not independently re-fetched
  or archived by this preservation checkpoint.

**INFERRED**
- Counting A ↔ B transfers as new external movement would
  double-count flows within the selected analytical boundary.

**UNKNOWN / NOT CLAIMED**
- Common ownership or control of A and B.
- Exact attribution of the 80M external outflow to incident funds.
- Whether the new 28M recipient was subject to later restrictions.
- Whether any institutional actor overlooked a freeze opportunity.
- This does not establish laundering, recovery, or control failure.

**Evidence directory:**
`research/case-binance-2026/evidence/eg03_two_address_consolidation_v1/`

**Status:** PARTIAL PASS — address-group conservation verified;
incident-fund attribution and downstream restriction status unresolved.

### EG-08 — Verified Ethereum-to-Plasma Delivery

**Status:** CROSS-CHAIN DELIVERY VERIFIED (incident attribution unresolved).

**OBSERVED — Ethereum**
- Source transaction: `0xbb2744d79ded511ce6bfdf85792fd4d8794ed6cae681f95fdc7de844c05c4f7a`; block `26307046`.
- 28,000,000 USDT transferred to Ethereum USDT0 adapter `0x6c96de32cea08842dcc4058c14d3aaad7fa41dee`.
- `OFTSent` event GUID: `0xdb41c20c03f2591813b8a6714c5eccff01fc00b9b393b36f5cafb1f82fe0655f`.
- Destination LayerZero EID: `30383` (Plasma).

**OBSERVED — Plasma**
- Destination transaction: `0xa2e90c60008700b31605275112d9a3ec17fe96dc3582391a5e781cc340218029`; block `36440003`, status success.
- Plasma chain ID: `9745`.
- `OFTReceived` event GUID matches Ethereum `OFTSent`.
- Destination OFT contract: `0x02ca37966753bdddf11216b73b16c1de756a7cf9`.
- Receiver: `0xb8734a14fbd4aa2d44e6aa830405ffc861ba313c`.
- Amount received: **28,000,000 USDT0**.
- LayerZero Scan reports `DELIVERED` and destination `SUCCEEDED`.
- Ethereum and Plasma raw receipts independently checked against RPCs.

**RECONCILIATION**
- Ethereum 28M USDT and Plasma 28M USDT0 represent linked
  cross-chain legs, **not 56M of separate incident funds**.
- GUID, recipient, chain, and amount checks: PASS.

**UNKNOWN / NOT CLAIMED**
- Whether the entire 28M is attributable to the original incident;
  upstream wallets had commingled balances.
- Subsequent movements on Plasma.
- Whether these funds were frozen, recovered, or should have been
  designated by a particular institution.
- Common ownership of addresses on different chains.

**Raw evidence:** `research/case-binance-2026/evidence/eg08_plasma_delivery_v1/`

**Next test:** Plasma recipient's subsequent USDT0 balance and
Transfer events, with contract and time-basis validation.


---

## 2026-11-05 Research Progress Update

This section consolidates the latest research evidence.
Earlier historical research and original methodology are preserved.

### 1. Overall Research Status

| Area | Status | Remaining gap |
|---|---|---|
| Gate 1 | COMPLETE_WITH_LIMITATIONS | Independent incident-wide reconciliation |
| Gate 2 | OPEN | Victim-wallet ownership and unauthorized outflows |
| Gate 3 | PARTIAL | Source provenance and downstream disposition |
| EG-01 | SUBSTANTIALLY VERIFIED | Independent replay and execution-time state |
| EG-02 | SCOPED RECONCILIATION PASS | Second-provider replay and disposition |
| EG-03 | PARTIAL | Reconcile accounting boundaries |
| EG-04 | OPEN | Normalize institutional freeze figures |
| EG-05 | TECHNICAL RESULT DOCUMENTED | External 64/37 claim population |
| EG-06 | PARTIAL — CURRENT PRIORITY | Suspension cutoff and independent transaction replay |
| EG-07 | OPEN | Bounded TRON mechanism reproduction |
| EG-08 | DELIVERY VERIFIED | Attribution and subsequent disposition |

### 2. Gate 2 — Transaction Verification

**Bitcoin**

Reference: `GATE_2_BITCOIN_11TX_AUDIT_V1.md`

- 11 transactions examined.
- Receiver outputs: 18,270.20000000 BTC.
- Inputs from reported source: 18,333.70635832 BTC.
- Other outputs: 63.50277682 BTC.
- Fees: 0.00358150 BTC.
- 513 unique spent input outpoints.
- Conservation and duplicate checks: PASS.

**TRON**

Reference: `GATE_2_TRON_NATIVE_TX_AUDIT_V1.md`

- Two native TRX transfers.
- Total: 46,394,098 TRX.
- Source, receiver, amount, block and timestamp matched.
- Both transactions SUCCESS.
- TRC-20 coverage excluded.

**XRP Ledger**

Reference: `GATE_2_XRPL_FIVE_SOURCE_AUDIT_V1.md`

- Five source accounts.
- Total: 233,461,943.1 XRP.
- Ledger inclusion, success, amount and duplicate checks PASS.

**STEP 75A official crosswalk**

- Official rounded aggregate: 233.46M XRP.
- Reported time: 20:05:00–20:09:20 UTC.
- Amount/time/address crosswalk PASS.

**Proof of Reserves**

Reference: `GATE_2_POR_OWNERSHIP_AUDIT_V1.md`

- 11/11 chain-and-address matches.
- 98 asset-level rows, not 98 separate wallets.
- Three addresses also appear in Binance's 2022 disclosure.
- Original CSV provenance and incident-time control remain unverified.

Gate 2 remains OPEN. Transaction verification does not establish
victim-wallet ownership or unauthorized conduct.

### 3. Gate 3 — T03 and 700M First-Hop Distribution

References:

- `GATE_3_T03_TO_700M_LINKAGE_AUDIT_V1.md`
- `700M_FIRST_HOP_DISTRIBUTION_AUDIT_V1.md`

T03 initial USDT sweep: 1,615,409,498.973240 USDT.

Examined first-hop distribution:

500M + 200M = 700M USDT.

- 20 Transfer events.
- 13 unique transactions.
- 13 archived receipts.
- Zero missing receipts.
- Zero duplicate transaction/log-index pairs.
- Receipt SHA256 and Transfer-log matching PASS.
- Reconciliation difference: 0 USDT.

The 175M and 30M paths are downstream branches.
Do not add them again to the 700M first-hop total.

Exclusive provenance, recipient ownership and incident-wide
conservation remain unestablished.

### 4. EG-01 — Blacklist-Time Balance Audit

References:

- `USDT_FREEZE_TIMELINE_CHECKPOINT_V4.md`
- `EG01_EXECUTION_TIME_AUDIT_V1.md`

Eight AddedBlackList events were observed in the examined window.

Three addresses had positive balances at their respective
blacklist block boundaries:

| Address | Block | USDT |
|---|---:|---:|
| Central | 26300954 | 971,149,299.483240 |
| 175M branch | 26301021 | 174,999,872.327520 |
| 30M branch | 26301041 | 30,000,000.000000 |

Five other examined addresses had zero balances at their
respective blacklist block boundaries.

These are asynchronous address-specific observations,
not an incident-wide frozen or recovered total.

### 5. EG-02 — Central Post-Blacklist Ledger

**SCOPED RECONCILIATION PASS — committed in 022f516.**

Evidence:
`evidence/eg02_central_post_blacklist_ledger_v1/`

Interval: blocks 26300955–26301167.

| Item | USDT |
|---|---:|
| Opening balance | 971,149,299.483240 |
| Inflow, block 26300968 | 3,917,639.767927 |
| Inflow, block 26301167 | 200,397,771.824195 |
| Total inbound | 204,315,411.592122 |
| Outgoing Transfer events | 0 |
| Ending balance | 1,175,464,711.075362 |
| Reconciliation difference | 0 |

Both incoming Transfer events identify Binance 14 as token sender.

Transactions:

1. `0x31c4c9fe287d54fb9d3b79980477a8c793a11f774b98d0a9a92de1dad888a91d`
2. `0x55ba4dabc41b468e580751373ad31acdee6f5ba398682df2c93e5a8340870556`

Four evidence files preserved:
- audit.json
- manifest.json
- raw_logs.json
- transfer_ledger.json

SHA256 integrity PASS.

Limitations:
- Block-end rather than execution-instant balances.
- One address and Ethereum USDT only.
- No independent second-provider replay.
- No proof of recovery or ultimate ownership.

The balance increase must not be described as recovered assets.

### 6. EG-03 — Conditional Source Accounting, STEP 60–66

Reference:
`INCIDENT_FUND_ATTRIBUTION_CHECKPOINT_2026-11-05.md`

Status: PARTIAL — conditional fungible-balance accounting.

- STEP 60: 190M source branch; 60M outflow and 130M ending balance reconciled.
- STEP 61: 200M inflow, 190M onward and 10M other outflow reconciled.
- STEP 62: conditional Binance 14 allocation of 144,260,199.490000 USDT.
- STEP 63–64: 55,739,800.500000 USDT plus 0.010000 USDT from another source; pre-baseline provenance UNKNOWN.
- STEP 65: 35,868,038.335205 USDT of other inflows from 45 addresses; conditional allocation of target 25M to designated source: 0–25M.
- STEP 66: pooled A/B model; 28M bridge outflow; conditional contribution from designated 25M source: 0–25M.

These are conditional fungible-balance calculations,
not legal taint, ownership or exclusive incident provenance.

The 0–25M range applies only to the designated tagged source.

The earlier two-address checkpoint and STEP 66 pooled checkpoint
have different reported baselines and flow totals.
Their accounting boundaries have not been demonstrated identical.

Do not merge these accounting models.

STEP 60–66 raw RPC bundles and reproducible scripts
are not archived in the checkpoint.

### 7. Attribution Research — STEP 71–73

**STEP 71 — On-chain source transfer**

Evidence:
`evidence/step71_55m_source_audit_v1/`

- Source: `0xdfd5293d8e347dfe59e90efd55b2956a1343963d`
- Recipient: Central.
- Amount: 55,739,800.500000 USDT.
- Block: 26300772.

The saved audit records the transfer and block-level evidence.

**STEP 72 — External attribution cross-check**

Evidence:
`evidence/step72_external_attribution_v1/`

- Bitquery: address present; amount absent.
- IMD: address and amount present.
- On-chain transfer: OBSERVED.
- Incident linkage: REPORTED_BY_SOURCES.
- Independent proof of unauthorized transfer: NOT ESTABLISHED.
- Official Binance transaction-level confirmation: NOT ESTABLISHED.
- Independence of external sources: UNKNOWN.

This corroborates an incident-link hypothesis,
not unauthorized intent or exclusive provenance.

**STEP 73 — Historical GraphSense listing**

Evidence:
`evidence/step73_preincident_graphsense_v1/`

The source address appears in GraphSense's Binance exchange-wallet
tagpack at commit:

`4291546db584a40c03d77af32e27ac7ad6e90bac`

Date: 2023-02-24.

This is a historical third-party listing,
not a direct Binance attestation or proof of incident-time control.

### 8. STEP 75A — Official Report Crosswalk

Evidence:
`evidence/step75a_official_report_crosswalk_v1/`

XRP:
- Five transactions.
- 233,461,943.1 XRP.
- Official rounded aggregate: 233.46M XRP.
- Reported time: 20:05:00–20:09:20 UTC.
- Crosswalk PASS.

USDT:
- Individual official confirmation of the 55.74M source: NOT DISCLOSED.
- Individual official confirmation of the 195M mixed wallet: NOT DISCLOSED.
- Incident attribution: UNRESOLVED.

Raw HTML was not captured due to AWS WAF.
The preserved excerpt documents the source and retrieval limitation.

Do not extend aggregate XRP corroboration to individual USDT attribution.

### 9. STEP 76 — Pre-Incident Inbound Scan

Evidence:
`evidence/step76_preincident_inbound_v1/`

Audit timestamp: 2026-11-05 11:12:40 UTC.

- Blocks: 26250512–26251511.
- Coverage: 1,000 blocks across ten chunks.
- Unique inbound events: 53.
- Total inbound: 1,616,374.401633 USDT.
- Distinct senders: 31.
- Counterparty match:
  `0x5aae4d2f360e156de3416936049837a7bb685588`
- Matching transfer: 114,589.789942 USDT at block 26251021.
- Next block: 26251512.

Status: PARTIAL_AUDIT_PASS.

Not a complete seven-day scan.
RPC data was not independently re-queried.
No outbound balance reconciliation was performed.
Incident attribution remains UNRESOLVED.

Do not describe this as a completed pre-incident funding audit.

### 10. EG-05 — T03 Failure-Tolerance Mechanism

Status: TECHNICAL RESULT DOCUMENTED; EXTERNAL CLAIM POPULATION OPEN.

Observed:
- 64 ERC-20 transfer calls.
- 63 matching Transfer events.
- One child token call reverted at position 27.
- 37 subsequent calls continued without recorded call errors.
- Parent transaction receipt succeeded.

The 37 subsequent non-error calls are not 37 failures.

The separate external 64 attempts / 37 failures claim
has not been linked to this technical population.

### 11. EG-06 — Withdrawal Suspension Versus Delegated Execution

**CURRENT RESEARCH PRIORITY.**

Completed technical research — DO NOT REPEAT:

T02:
- Block 26300753.
- Type-4 EIP-7702 transaction.
- 50 authorization entries examined.
- Authority recovery identified Binance 14.
- Matching authorization nonce resolved.

T03:
- Block 26300770.
- Delegated execution documented.
- Initial USDT sweep: 1,615,409,498.973240 USDT.

T17:
- Block 26301896.
- Delegation-removal checkpoint documented.

Existing case study:
`BINANCE_2026_DELEGATED_WALLET_DRAIN_CASE_STUDY.md`

**TechCrunch — October 29, 2026**

https://techcrunch.com/2026/10/29/binance-pauses-withdrawals-as-hackers-suspected-of-stealing-billions-in-crypto/

Publication time: 22:27 UTC.

Reported that a Binance spokesperson confirmed temporary
withdrawal suspension across multiple networks.

Classification: REPORTED_BY_SOURCE.

This establishes public confirmation by 22:27 UTC,
not the exact internal suspension timestamp.

**Binance retrospective — November 3**

https://www.binance.com/en-IN/blog/community/3229153443759566763

Binance reported:
- Final unauthorized transfer of 2,961.9 ETH finalized at 23:56 UTC on October 29.
- The transaction had been broadcast earlier and remained pending.
- Delegation removal at 00:10 UTC on October 30.

The earlier broadcast timestamp has not been independently established.

**Candidate transaction**

`0x4a4aed833556814c16fe176fc8abc70ce124eadc73da3bcdf42a67ef44f9ad6b`

Explorer-reported:
- Block 26301444.
- Timestamp 2026-10-29 22:39:35 UTC.
- Outer sender: `0x7c8601d4645b93cea45f71e118a729332e6b5ca0`.
- Target: Binance 14.
- Internal ETH transfer: 128.491139212075057017 ETH.
- Recipient: `0xa97bf7836f8a08f9ed91d41453d371493fae8d10`.

Classification: REPORTED_BY_EXPLORER; NOT INDEPENDENTLY REPLAYED.

Block inclusion is 12 minutes and 35 seconds after the TechCrunch
publication. This does not establish transaction broadcast time
or prove execution occurred after internal suspension.

**UNKNOWN**
- Exact internal withdrawal suspension timestamp.
- Candidate transaction broadcast time.
- Independent receipt and execution trace.
- Historical delegation state at candidate block.
- Whether a new instruction was submitted after suspension.
- Whether all relevant signing and delegated-execution capabilities
  were disabled by withdrawal suspension.

**Next tests**
1. Retrieve raw transaction, receipt and block from two providers.
2. Preserve execution trace and provider provenance.
3. Verify internal ETH transfer and child-call outcomes.
4. Verify historical Binance 14 delegation state at block 26301444.
5. Reconcile with Binance's reported 23:56 UTC final transfer.
6. Seek authenticated evidence of the internal suspension cutoff.
7. Keep announcement, suspension, broadcast, inclusion and final movement separate.

Do not repeat T02/T03/T17 technical research.

### 12. EG-07 — TRON Mechanism

Status: OPEN.

TRM's described self-minted-token, liquidity-pool,
receipt-token and bridge mechanism has not been independently reproduced.

If resumed, use one bounded route:
- Contract events.
- Liquidity changes.
- Mint/sell/redeem accounting.
- Bridge events.
- Competing explanations and falsification tests.

Defer broad expansion until a material testable route is identified.

### 13. EG-08 — Ethereum-to-Plasma Delivery

Status: CROSS-CHAIN DELIVERY VERIFIED; ATTRIBUTION UNKNOWN.

Evidence:
`evidence/eg08_plasma_delivery_v1/`

- Ethereum source block: 26307046.
- Plasma destination block: 36440003.
- 28M USDT sent.
- 28M USDT0 received.
- Matching LayerZero GUID.
- Successful destination execution.
- Seven SHA256 entries recorded.

This is one linked bridge transfer, not 56M of separate funds.

Subsequent Plasma movements, restriction status, recovery
and incident attribution remain UNKNOWN.

### 14. Publication Readiness

References:
- `AXIOM_PUBLICATION_CLAIMS_AUDIT_V1.md`
- `AXIOM_PUBLICATION_EVIDENCE_INVENTORY_V1.csv`

Recorded automated checks:
- 15 evidence inventory files checked.
- 15 SHA256 matches.
- Nine structured claim checks passed.
- Zero structured claim-check failures.

Automated consistency: PASS.
Publication approval: NOT GRANTED.

Human review remains required for source authenticity,
transaction and trace reproducibility, citations,
alternative explanations, claim boundaries and sensitive-material review.

Internal research is appropriate.
LinkedIn publication remains a possibility after human review.
Institutional submission is not yet ready.
No incident-wide attribution or criminal allegation is established.

### 15. Research Priorities

1. EG-06: independently replay the 22:39:35 UTC candidate and establish the suspension cutoff.
2. EG-03: reproduce STEP 60–66 and reconcile accounting boundaries.
3. STEP 76: assess whether the counterparty match justifies extending the historical scan.
4. EG-04: normalize freeze figures by chain, asset, cutoff, valuation and definition.
5. Defer unrelated tracing and broad TRON expansion.

### 16. Permanent Controls

- Preserve the fixed AXIOM methodology.
- Do not repeat completed T02/T03/T17 or 700M first-hop work.
- Distinguish OBSERVED, REPORTED_BY_SOURCE, INFERRED and UNKNOWN.
- Never infer ownership or criminal intent from wallet labels.
- Do not equate blacklisted, frozen, intercepted, replenished and recovered.
- Keep conditional fungible-balance accounting separate from ownership or legal taint.
- Do not double-count intermediary transfers or bridge legs.
- Preserve raw evidence, provenance and SHA256 manifests.
- Keep unfinished work on `research/case-binance-2026`.
- No publication to main without explicit approval.

The immediate unresolved research question remains the timing
and effectiveness of Binance's withdrawal suspension relative
to subsequent delegated-wallet execution.
