# AXIOM — 175M USDT Path Continuity Audit V1

## Observed transfer sequence
1. `0x9749292d74fd460982d0912ea9515ea24736c762` -> `0x811f15855476156ebf86ba3b84fafb8ceaa4e84c`
   - TX: `0x1fb992f92a45afec23d7d5740c7958a644fb90ef0cba19ca39bd2c6534fb670b`
   - Block: 26300942
   - Amount: 175,000,000 USDT (reference decimals: 6)
2. `0x811f15855476156ebf86ba3b84fafb8ceaa4e84c` -> `0xaa246bf639586a6ba46762d378ce50ca4fc654a0`
   - TX: `0xb6d7d3ffcbdd0465e1ab743a8d943218176cac7b15edefa7b7bcd5e853e4266f`
   - Block: 26300988
   - Amount: 175,000,000 USDT (reference decimals: 6)

## Audit checks
- Address continuity: PASS
- Token contract equality: PASS
- Raw amount equality: PASS
- Event chronological ordering: PASS
- Both events previously extracted from RPC receipts.
- Token contract identity and decimals use reference mappings.

## Limitations
- Two sequential 175M transfers are not 350M in independent losses.
- This does not prove complete wallet-level fund conservation.
- Other intervening transactions have not been excluded.
- Ownership of these wallets is not independently verified.
- Incident attribution is UNKNOWN.
- Classification is provisional.

## Gate decision
- Gate 2: OPEN.
- Additional confirmed victim wallets: 0.
