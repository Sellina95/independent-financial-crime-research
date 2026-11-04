# EG-01 — Blacklist Execution-Time Balance Audit

**Status: SUBSTANTIALLY VERIFIED / direct intra-transaction state pending**

## Verified observations

| Address | Block | TX index | Balance (USDT) | Target Transfers |
|---|---:|---:|---:|---:|
| Central (`0x5227f603c1ee34ce3c06efe6477003bdfccb2f8c`) | 26300954 | 88 | 971149299.483240 | 0 |
| 175M (`0xaa246bf639586a6ba46762d378ce50ca4fc654a0`) | 26301021 | 199 | 174999872.327520 | 0 |
| 30M (`0xb171ca86f82070282138352ff7111b494060c8c3`) | 26301041 | 13 | 30000000.000000 | 0 |

For all three addresses:

- Blacklist transaction receipt status: SUCCESS.
- Matching blacklist event: verified.
- Previous-block and blacklist-block end balances: identical.
- Target USDT Transfer logs within blacklist block: zero.
- Block-level balance reconciliation: PASS.

## Evidence classification

**OBSERVED:** Blacklist receipt/event, block-wide Transfer logs,
historical block-end balances from eth.drpc.org.

**STRONGLY INFERRED:** The execution-instant balance matched
the adjacent block-end balances for each address.

**NOT DIRECTLY VERIFIED:** Intra-transaction balance state;
absence of non-Transfer balance mutations; independent RPC
provider reproduction.

The three snapshots occur in DIFFERENT blocks. Their sum
is NOT an incident-wide frozen or recovered amount.

## Evidence

`evidence/eg01_execution_time_v1/manifest.json`

## Next research

EG-02: post-blacklist value changes and recovery semantics.
EG-03: synchronized conservation and double-count prevention.

