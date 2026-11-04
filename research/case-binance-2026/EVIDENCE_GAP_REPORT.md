# AXIOM — Evidence Gap Report
## Binance 2026 | Independent Financial Crime & Fund-Preservation Research

**Status:** ACTIVE RESEARCH CHARTER — NOT A COMPLETED FORENSIC FINDING  
**Evidence cutoff:** 2026-11-04  
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
| EG-02 | What **post-blacklist inflows** changed later restricted balance? Is restricted value distinct from initial balance and recovered assets? | Incomplete post-event ledger; mechanism discussed publicly | Time-stamped address/token ledger, inflows/outflows, blacklist state, token semantics, recoveries and redemptions kept separately | **P0** |
| EG-03 | Are three event-time address balances double counted or incomparable because of asynchronous snapshots? | **PARTIAL PASS** — synchronized balances and three intermediate-wallet distributions reconciled; downstream recipient coverage and restriction status remain open | Time-indexed conservation, synchronized snapshots where possible, recipient-identity and transfer-link checks; report scope-specific estimate only | **P0** |
| EG-04 | Does a genuine discrepancy persist against institutional freeze numbers after basis normalization? | Not established | Normalize UTC cutoff, chain, token, pricing, frozen/intercepted/recovered definitions; verify underlying receipt evidence and alternative explanations | P1 |
| EG-05 | What do **64 attempts / 37 failures** refer to, and why did they fail? | **Population and denominator unverified** | Locate original claim/dataset; classify external tx vs internal call vs batch item, status, revert, nonce, gas, execution environment; compare with officially reported 50 signing transactions without equating counts | **P1** |
| EG-06 | Do Binance's EIP-7702 account, authorization revocation, and **T02/T03/T17** align chronologically? | Official November 3 narrative available, T02/T03/T17 meaning not yet recovered from original case evidence | Resolve ID definitions first; compare broadcast vs confirmation times, UTC, blocks, indexes, execution privileges and revocation | P1 |
| EG-07 | Can a TRM-reported **TRON pool / self-minted-token / receipt-token value transfer** be reproduced independently? | TRM's public account, not independently reproduced | One bounded route, raw pool/token events, liquidity, mint/sell/redeem, accounting and falsification test | P2 |
| EG-08 | Can chained **cross-chain bridge** value links be established rather than guessed from amount/time similarity? | Not reproduced | Bridge IDs, deposit/withdrawal events, token changes, fees, plausible competing matches; uncertainty labels | P2 |

**Sequence:** Close EG-01–03 to a scoped PASS / FAIL / OPEN WITH LIMIT verdict; then prioritize EG-05–06 based on source definability; only then run a small EG-07/08 pilot. Unavailable archive-RPC access must be recorded, not endlessly retried and not declared PASS.

## 4. Public-source comparison ledger — cutoff 2026-11-04

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

**Phase 1 — Fund preservation / EG-01–03:** Record exact blacklist events and state basis, pre/post movements, time-aware conservation, uncertain claims and independent archive replay status. If independent historical access is blocked, leave that element `OPEN_GAP` and conclude the narrower verified checkpoint; do not call the entire incident-wide freeze figure verified.

**Phase 2 — Control failure / EG-05–06:** Before coding, recover evidence defining `64`, `37`, `T02`, `T03`, `T17`. Treat 50 official signing transactions as a **different population until proven otherwise**. Never infer causes of failed operations from a single `status` flag.

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

## 9. Immediate next actions

1. Close the three-address USDT freeze checkpoint with its **limited** claim and explicitly list remaining independent verification gaps.
2. Perform **one targeted post-blacklist inflow and same-time conservation audit** from preserved receipts, not another simple sum.
3. Inventory the exact source defining **64/37** and the IDs **T02/T03/T17**; mark `UNKNOWN` if unrecoverable rather than inventing causes.
4. Choose **one** falsifiable TRM mechanism pilot only after the earlier gates.

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
