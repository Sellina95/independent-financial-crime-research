# AXIOM — Ethereum Historical Evidence Reconciliation V1

## Purpose

Reconcile earlier Ethereum research checkpoints with later
independently verified on-chain evidence.

This document supplements earlier reports without rewriting
their historical observations.

## 1. Superseded technical uncertainties

| Earlier uncertainty | Current evidence | Updated status |
|---|---|---|
| T02 raw authorization list unverified | T02 signature recovery V1 | VERIFIED |
| EIP-7702 signer identity unknown at address level | 50/50 signatures recover to Binance 14 | VERIFIED ADDRESS RECOVERY |
| Which T02 nonce applied | Nonce-only replay, index 15 | CORROBORATED |
| Historical wallet delegation code unknown | Historical code audit V1 | VERIFIED BLOCK-END STATE |
| Delegation persistence before T03 unknown | Block 26300769 and block-order audit | STRONGLY CORROBORATED |
| T03 token-transfer outcomes incomplete | Transfer event audit V1 | 63 MATCHES / 1 REVERT |
| Failed-call continuation unknown | Failure tolerance audit V1 | OBSERVED |
| Selected token balance deltas unknown | Historical balance audit V1 | VERIFIED BLOCK-END DIFFERENCES |

## 2. Reconstructed technical sequence

1. T02: Fifty EIP-7702 authorization signatures recover
   to Binance 14.
2. A nonce-only replay identifies index 15 as the
   applicable authorization.
3. The wallet delegation code appears after T02.
4. The same delegation pointer exists at the end of
   the block preceding T03.
5. No Type-4 transactions precede T03 within its block.
6. T03 calldata and runtime evidence identify one
   recipient and 64 token-transfer attempts.
7. Sixty-three matching ERC-20 Transfer events were found.
8. The 27th token-transfer call reverted.
9. Thirty-seven subsequent calls continued without
   recorded call errors.
10. USDT historical balance differences reconcile
    between source and recipient.
11. The failed token's checked balances did not change.
12. The delegation code is absent after T17.

## 3. Evidence hierarchy

VERIFIED:
- Signature address recovery
- Historical block-end delegation state
- Transaction and calldata fields
- Runtime calls, receipt events and selected balances

CORROBORATED / INFERRED:
- T02-to-T03 delegated batch execution mechanism
- The zero-address entry represents native ETH
- Failure-tolerant processing design

NOT ESTABLISHED:
- Instruction-level trace proving each delegated opcode
- Transaction-level pre/post balances independent
  of other transactions within the block
- Binance corporate authorization or lack of consent
- Signing-key compromise mechanism
- Actual controller of recipient wallets
- Official Binance transaction-specific attribution
- Full incident-wide funds conservation

## 4. Original documents preserved

- EVIDENCE_CHECKPOINT_V1.md
- GATE_2_ETH_T02_T03_MECHANISM_REVIEW_V1.md
- GATE_2_ETH_DELEGATION_CONTRACT_LINK_V1.md

Their original UNKNOWN statements were accurate
at the time of writing. Later evidence supersedes
the specified technical uncertainties.

## 5. Publication boundary

Suitable for an independently reconstructed
Ethereum EIP-7702 case study, subject to final
publication audit.

Not suitable for declaring the full Binance
incident reconstructed or criminal responsibility proven.

## 6. Research map

The FIXED RESEARCH MAP V1 remains unchanged.

Gate 1: COMPLETE_WITH_LIMITATIONS.
Gate 2: OPEN.
Gates 3–5: PARTIAL.

This reconciliation does not close any incident-wide gate.
