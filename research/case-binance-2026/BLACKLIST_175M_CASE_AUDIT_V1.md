# CASE AUDIT — 175M USDT Blacklist Path

## Scope
Ethereum USDT address `0xaa246bf639586a6ba46762d378ce50ca4fc654a0`.
This audit concerns one observed fund-flow path, not the entire incident.

## Verified chronological evidence
1. Block 26300987: historical USDT balance = 0.
2. Block 26300988: incoming 175,000,000 USDT.
   - TX: `0xb6d7d3ffcbdd0465e1ab743a8d943218176cac7b15edefa7b7bcd5e853e4266f`
   - Source: `0x811f15855476156ebf86ba3b84fafb8ceaa4e84c`
3. Block 26301011: outgoing 127.672480 USDT.
   - TX: `0x11be88b460501b4652e760c41e08cc1f18575e14b6c6ffbb3383e043c2decf34`
   - Destination: `0xe3478b0bb1a5084567c319096437924948be1964`
4. Block 26301020: historical balance = 174,999,872.327520 USDT.
5. Block 26301021: Tether AddedBlackList event for this address.
   - TX: `0x0c07a5e428ce233a3bcb40f257ad899594421341d63ce94016822063362707bf`
   - Historical block-end balance = 174,999,872.327520 USDT.

## Reconciliation
175,000,000 - 127.672480 = **174,999,872.327520 USDT**

Historical balance snapshots and transfer receipts agree.

## Evidence standard
- Transfer events and successful receipts: VERIFIED
- Historical balanceOf results: VERIFIED
- Tether blacklist event and receipt: VERIFIED
- Owner identity / criminal attribution: NOT ESTABLISHED
- Asset recovery or redemption: NOT ESTABLISHED
- Current blacklist status or current balance: NOT TESTED

The blacklist event establishes registration at that block,
not recovery of funds or a complete incident-wide freeze total.

## Preserved evidence
- `evidence/blacklist_balance_175m_v1/balance_snapshots.json` — SHA256 `5f87f125a413be985daad792d589f4ab8f97b30dbff2edbe0198553e0e78cab3`
- `evidence/blacklist_event_175m_v1/blacklist_event.json` — SHA256 `4a62a337d3a475134ac85830d55756de4840f1cbc163f536a1d997a5ecaf02cf`
- `evidence/blacklist_event_175m_v1/blacklist_receipt.json` — SHA256 `a1bacad49a9c1b21e04a7928e63bccaac4140018ff2d53f3d4038d9c975ad58b`
- `evidence/blacklist_flow_175m_v1/inflow_receipt.json` — SHA256 `5a7dcf937bba60abb091d43884013b6882a7beba9b47b863184a11fbf3042aa4`
- `evidence/blacklist_flow_175m_v1/outflow_receipt.json` — SHA256 `225fbef95746ec5e7f43d2cbba20fa5273c3fedb1ed14dafb430db9558e1fe35`
