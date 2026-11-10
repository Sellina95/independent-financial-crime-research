# AXIOM — Binance 2026 | FIXED RESEARCH MAP V1

**Status: FIXED — user-approved research roadmap**  
**Repository:** `Sellina95/independent-financial-crime-research`  
**Branch:** `research/case-binance-2026`  
**Rule:** This file is the authoritative roadmap for this case. Do not silently replace or redesign it in a new chat.

## Objective

Reconstruct the documented incident from the earliest verifiable victim-wallet outflows, and determine whether those flows connect by verifiable transactions to the already-audited 700M USDT subpath. Never assume that connection.

## Fixed map

### ① Official incident evidence — NOT COMPLETE
Establish the incident date and time, affected networks, assets, reported loss, and any officially disclosed victim wallet addresses. Record source, publication date, and what remains unknown. Distinguish official claims from third-party reporting.

### ② Victim wallets and initial unauthorized outflows — NOT COMPLETE
Identify candidate victim wallets and verify their initial outflow transactions, amounts, chains, timestamps, and evidence supporting incident attribution. An on-chain transfer alone does not establish that it was unauthorized.

### ③ Forward tracing — PARTIAL (700M SUBPATH ONLY)
Trace verified incident outflows through recipients, splits, exchanges, bridges, and subsequent destinations. **Existing 700M path:** central address `0x5227f603c1ee34ce3c06efe6477003bdfccb2f8c` sent 500M + 200M USDT to two addresses; preserved second-hop evidence includes 20 transfer events across 13 transactions. The first distribution was audited. **Its connection to the Binance incident is UNKNOWN.** Do not call this the full tracing of incident funds.

### ④ Blacklist / freeze comparison — PARTIAL
Compare traced addresses against blacklist and freeze events, event times, and point-in-time balances. Prior research includes A/B/C blacklist-address observations and partial 175M / 30M downstream paths. Blacklist registration is not proof of Binance involvement, actual recovery, or ownership.

### ⑤ Conservation and evidence audit — PARTIAL (700M SUBPATH AUDIT COMPLETE)
Verify logs against receipts, hashes, transfer amounts, point-in-time balances, gaps, and double counting. Previously audited 700M preserved outflows reconcile with a zero difference. Do not count the same funds again when they move to later hops.

## Where the completed 700M work belongs

- **Verified:** the on-chain 500M + 200M first distribution from the central address, and the preserved next-hop transfer evidence.
- **Verified:** 20 USDT Transfer events, 13 transaction receipts, receipt/manifest integrity checks, and 700M observed-outflow reconciliation.
- **Audit file:** `research/case-binance-2026/700M_FIRST_HOP_DISTRIBUTION_AUDIT_V1.md`
- **Audit commit:** `686d2db`
- **NOT verified:** that the central address was a Binance victim wallet, that the 700M was stolen in the Binance incident, or that all downstream destinations have been traced.
- **Decision:** preserve this evidence; only attach it to the incident after Gates ① and ② establish a defensible transaction-level connection.

## Fixed next action

**Start with ①.** Build an evidence register of official incident statements and explicitly identified victim addresses. Then verify the initial outflow transactions under ②. **Do not expand the 700M downstream branches yet.** New addresses or leads are parked until the relevant gate.

## Rules for every new ChatGPT session

1. Read this exact map first. Treat it as the controlling roadmap, not a suggestion.
2. Keep the order **① → ② → ③ → ④ → ⑤**. Verification/audit checks can occur within each stage, but the investigative priority does not change.
3. State the active stage and what is already complete before proposing work.
4. Preserve the 700M audit; do not redo it without contradictory evidence.
5. Distinguish **OBSERVED / INFERRED / UNKNOWN / DISPROVEN**; never equate blacklisting or repeated addresses with incident attribution.
6. Give one terminal command at a time when needed; wait for the output. Use the research branch; protect `main`.
7. Do not change this map without explicitly explaining why and receiving the user's approval. New evidence may change findings, not silently change the map.

## New-session message

> AXIOM — Binance 2026 이어가자. 첨부한 `AXIOM_BINANCE_2026_FIXED_RESEARCH_MAP_V1.md`가 고정 조사 지도야. 먼저 읽고 ①→②→③→④→⑤ 순서를 유지해. 700M 경로는 분배 감사만 완료했고 사건 연결은 미확인이야. 현재 ①부터 이어가자. 지도를 임의로 바꾸지 마.
