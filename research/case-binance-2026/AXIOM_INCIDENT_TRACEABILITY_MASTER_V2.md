# AXIOM — Binance 2026 Incident Research Master Map

**Status:** ACTIVE RESEARCH / NOT PUBLICATION APPROVED
**Last status review:** 2026-11-08
**Branch:** `research/case-binance-2026`

## PURPOSE

This is the fixed, incident-wide research map.

- V1: detailed investigation, evidence, findings and audit history.
- V2: latest status, acceptance gates and next decisions.
- Raw evidence: preserved in existing research files.
- Final case study: separate, audited, publication-approved deliverable.

Do not append numbered research steps to V2.
Update existing rows as evidence changes.

## FINAL RESEARCH OBJECTIVE

Reconstruct the reported incident and distinguish:

1. What happened, based on authenticated evidence.
2. How wallet authorization and execution operated.
3. How funds moved across assets, wallets and protocols.
4. Which controls restricted which assets, and when.
5. What was restricted, preserved or actually recovered.
6. Where source attribution and traceability break.
7. Which independent findings materially differ from
   published investigations.
8. What institutions can learn, without unsupported
   attribution or novelty claims.

## MASTER PROGRESS MAP

Status definitions:
- DONE_SCOPED: Acceptance test passed within explicit boundaries.
- CORROBORATED: Multiple sources support a mechanism,
  but a causal verification boundary remains.
- PARTIAL: Some requirements passed; others remain open.
- OPEN: Material evidence or reconciliation missing.
- DEFERRED: Not currently worth further investigation.
- STOP: Do not repeat absent material new evidence.

| Gate | Research objective | Current status | Acceptance requirement | Next decision |
|---|---|---|---|---|
| G01 | Authenticate incident source and initial unauthorized outflows | PARTIAL | Primary incident claims, chain-specific origin transactions and authorization boundaries independently crosswalked | Complete only material source gaps |
| G02 | Reconstruct EIP-7702 delegation, execution and removal | DONE_SCOPED | T02 signatures, T03 execution, historical delegation states and T17 block-end status documented | STOP repeated technical checks; internal compromise remains unknown |
| G03 | Explain ERC-20 failure behavior and KITE restriction | CORROBORATED | Safe pause-origin, historical paused state, revert, receipt and failure-handler evidence connected | STOP unless contrary evidence warrants opcode replay |
| G04 | Build evidence-linked fund-flow network | PARTIAL | 700M first-hop distributions and selected 175M/190M/130M/80M/30M continuations audited; full recipient coverage remains open | Review archived follow-on evidence for the 145M, 100M, 50M and 28.6M recipients before any new RPC |
| G05 | Reconcile assets and eliminate duplicate counting | PARTIAL | Scoped 500M/200M distributions reconcile; incident-wide provenance and transformed-asset conservation remain open | Preserve fungible-source uncertainty and stop counting repeated hops as new losses |
| G06 | Determine asset-level restriction and freeze effects | PARTIAL | Historical blacklist events, asset-specific coverage and time-specific balances reconciled | Separate restricted balances from recovered funds |
| G07 | Assess institutional response and delegation controls | PARTIAL | Authenticated suspension-effective time, qualifying movements and delegation-state timeline compared | If internal cutoff unavailable, retain UNKNOWN |
| G08 | Reproduce selected cross-chain or protocol mechanisms | PARTIAL | One or more material routes with event-level conservation and explicit attribution boundary | Reopen only on material new source anchor |
| G09 | Compare institutional public claims | PARTIAL | Claims normalized by exact source, population, asset, UTC and definition | Test only material discrepancies |
| G10 | Complete independent red-team and publication audit | OPEN | Counterexamples, provenance, conservation, limitations, review and explicit publication approval | Remain on research branch |

## COMPLETED OR STOPPED INVESTIGATIONS

| Investigation | Established outcome | Limit / stopping condition |
|---|---|---|
| T02 authorization | Existing audit recovers 50/50 signatures to Binance 14 | Does not explain internal signing compromise |
| T03 delegated batch | 64 ERC-20 calls, 63 matching Transfer events, one reverted child call | No-error calls are not automatically proven transfers |
| T17 delegation removal | Archived historical code empty at block-end 26301896 | Exact intra-block mutation not independently replayed |
| KITE pause origin | 2026-08-05 Safe-compatible pause execution and state transition | Administrative motive UNKNOWN |
| KITE failed transfer | Incident-adjacent pause and EnforcedPause-matching revert | Strongly corroborated, not complete opcode replay |
| 700M distribution | Scoped first-hop and second-hop reconciliation | Not complete incident conservation |
| 175M / 190M / 130M / 80M / 30M | Selected receipt-linked paths audited | No automatic downstream ownership attribution |
| Central USDT blacklist | Historical designation and balance checkpoints | Not equivalent to recovery |
| Central later USDT inflow | Scoped 204,315,411.592122 USDT reconciled | Wider population not proven |
| Aave 25M | Claimed direct supply-to-withdraw link rejected | Incident attribution UNKNOWN |
| Plasma 28M | Selected cross-chain delivery independently documented | Incident attribution UNKNOWN |

## CONTROL TIMELINE CHECKPOINTS

| UTC | Control / event | Status |
|---|---|---|
| 2026-08-05 20:39:35 | Old KITE paused via Safe-compatible execution | OBSERVED |
| 2026-10-29 20:20:59 | T02 EIP-7702 delegation established | EXISTING ON-CHAIN AUDIT |
| 2026-10-29 20:24:23 | T03 delegated asset movement | OBSERVED |
| 2026-10-29 21:01:35 | Central USDT blacklist event | OBSERVED IN PRIOR AUDIT |
| 2026-10-29 23:56 | Last unauthorized ETH transfer per Binance | REPORTED_BY_SOURCE |
| 2026-10-30 00:10:35 | T17-associated transaction; empty delegation code at block-end | BLOCK-END VERIFIED |

Unknown:
- Actual internal withdrawal-suspension-effective time.
- Exact internal compromise and signing-approval path.
- Incident-wide recovered asset value.
- Complete cross-chain incident attribution.

Do not substitute public announcement time for internal
control-effective time.

## ACTIVE DECISION QUEUE

| Priority | Research question | Next action | Stop rule |
|---|---|---|---|
| P0 | Can the internal suspension-effective time be authenticated? | Review preserved official evidence and any material new primary disclosure | Retain UNKNOWN if inaccessible |
| P1 | Which important fund-flow edges remain open? | Compare existing ledgers and mark unsupported links | Do not revisit completed routes |
| P1 | How do frozen, restricted and recovered values compare? | Normalize chain, token, time and accounting definitions | No incident-wide total without compatible evidence |
| P1 | Is any public institutional discrepancy material? | Source-to-claim crosswalk | No novelty inferred from non-disclosure |
| P2 | Is a TRON/bridge/receipt-token mechanism reproducible? | One bounded case with raw event verification | Stop if only time/amount coincidence |
| FINAL | Is the report ready for external review? | Independent conservation and red-team assessment | Explicit human approval required |

## EVIDENCE NAVIGATION

- Detailed research history:
  `AXIOM_INCIDENT_TRACEABILITY_MASTER_V1.md`
- Research charter and original gaps:
  `EVIDENCE_GAP_REPORT.md`
- Delegation state:
  `GATE_2_ETH_HISTORICAL_CODE_AUDIT_V1.json`
- Ethereum historical synthesis:
  `GATE_2_ETH_HISTORICAL_RECONCILIATION_V1.md`
- Initial transaction audit:
  `GATE_2_INITIAL_TX_ONCHAIN_VALIDATION_V1.csv`
- T03 raw call trace and receipt:
  `evidence/initial_tx_v1/`
- KITE incident-adjacent state:
  `evidence/eg05_kite_historical_pause_v1/`
- KITE pause-origin records:
  `evidence/eg05_kite_pause_origin_v1/`
- Central post-blacklist ledger:
  `evidence/eg02_central_post_blacklist_ledger_v1/`
- Aave attribution correction:
  `EG08_AAVE_POSITION_ATTRIBUTION_CORRECTION_V1.md`

Evidence reference does not imply every file was
independently revalidated in this status update.

## FIXED MAINTENANCE RULES

1. V1 retains detailed, append-only research updates.
2. V2 remains the fixed map; update rows in place.
3. Each new result must map to an existing gate.
4. Update status only after an explicit acceptance test.
5. Record which evidence supports each changed decision.
6. Preserve historical UNKNOWN statements in source files.
7. Distinguish OBSERVED, REPORTED_BY_SOURCE,
   INFERRED, UNKNOWN and DISPROVEN.
8. Do not reopen completed work without material reason.
9. Never equate frozen, restricted and recovered assets.
10. Keep main and public reports unchanged until
    explicit publication approval.

**Current next action:** G04 archived-evidence continuation review, starting with the 145M USDT recipient. Check existing reports and raw receipts before any new RPC. G07 internal suspension cutoff remains UNKNOWN unless new primary evidence emerges.
