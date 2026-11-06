# EG08 — Aave Position Attribution Correction V1

Status: RESEARCH / RED TEAM / NOT FOR PUBLIC ATTRIBUTION
Evidence checkpoint: STEP 08AC
Branch: research/case-binance-2026

## Verified observations

- The address previously labeled MIXED is the Ethereum
  Aave V3 aUSDT token contract, not an ordinary custody wallet.
- A separate address supplied 10M and 50M USDT through
  Aave Supply transactions.
- The 25M USDT payout to A is an Aave Withdraw.
- The Withdraw event identifies A as the position owner
  and recipient.
- A held 25,004,647.909954 aUSDT at block 26300769,
  immediately before the reported main drain block.
- A held 25,004,768.970602 aUSDT at block 26301076,
  before its 25M withdrawal.
- Complete filtered event scans for blocks 26300770–26301076
  found zero aToken transfers into or out of A, and zero
  Aave Supply events indexed to A.

## Rejected interpretation

The old MIXED-to-A 25M transfer must not be represented as
an ordinary wallet-to-wallet transfer of incident-tagged USDT.

The hypothesis that the post-incident 60M Supply created
A's right to withdraw 25M is inconsistent with the
documented pre-incident position.

STEP 65's former 0–25M conditional allocation is
NOT a valid incident attribution result under the
correct Aave protocol interpretation.

## Preserved uncertainty

Aave liquidity is pooled and fungible. Pre-existing
withdrawal entitlement does not uniquely identify the
individual USDT units used for redemption.

This audit does not prove that no incident-related units
were present in the pool or paid out.

It does not prove common ownership, collusion,
unauthorized conduct, or legal attribution.

Other inflows into A/B and the 28M Plasma bridge remain
separate attribution questions.

## Research decision

STOP repeating the 60M Supply -> 25M withdrawal
as an alleged direct incident-fund transfer.

Treat any renewed incident-attribution claim as requiring
new, independently verified evidence or an explicitly
defined and defensible pooled-liquidity tracing model.

Previous raw evidence is preserved without modification.
This memo supersedes the incompatible interpretation,
not the underlying transaction observations.
