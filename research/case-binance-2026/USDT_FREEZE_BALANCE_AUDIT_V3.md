# Binance Security Incident 2026
## USDT Freeze Balance Audit — V3

Research date: 2026-10-30
Network: Ethereum Mainnet
Status: ON-CHAIN AUDIT PASS / SOURCE ARTIFACTS PENDING

This audit is based on user-executed Ethereum JSON-RPC
queries and reported terminal outputs.

No real-world identity attribution is attempted.

## 1. Scope

Research question:

What USDT balance existed immediately before the
blacklist transaction, and can the balance change
be reconciled with actual ERC-20 Transfer events?

Token:
Tether USD (USDT)

Contract:
0xdAC17F958D2ee523a2206206994597C13D831ec7

Target:
0xaa246bf639586a6ba46762d378ce50ca4fc654a0

## 2. Initial Receipt

Transaction:
0xb6d7d3ffcbdd0465e1ab743a8d943218176cac7b15edefa7b7bcd5e853e4266f

Block: 26300988

Transaction index: 58
Log index: 429

From:
0x811f15855476156ebf86ba3b84fafb8ceaa4e84c

To:
0xaa246bf639586a6ba46762d378ce50ca4fc654a0

Amount:
175,000,000 USDT

Evidence:
Ethereum RPC ERC-20 Transfer log.

## 3. Pre-Freeze Outgoing Transfer

Transaction:
0x11be88b460501b4652e760c41e08cc1f18575e14b6c6ffbb3383e043c2decf34

Block: 26301011

Transaction index: 87
Log index: 288

From:
0xaa246bf639586a6ba46762d378ce50ca4fc654a0

To:
0xe3478b0bb1a5084567c319096437924948be1964

Amount:
127.672480 USDT

Evidence:
Ethereum RPC ERC-20 Transfer log.

The outgoing transfer occurred before
the verified blacklist transaction.

Purpose and final destination are unknown.

## 4. Historical Balance Verification

Method:
USDT balanceOf(address) via Ethereum eth_call.

Block 26300987:
0.000000 USDT

Block 26300988:
175,000,000.000000 USDT

Block 26301020:
174,999,872.327520 USDT

Block 26301021:
174,999,872.327520 USDT

All values were returned by the user's
Ethereum RPC historical state queries.

The balances represent end-of-block state.

## 5. Blacklist Event Verification

Transaction:
0x0c07a5e428ce233a3bcb40f257ad899594421341d63ce94016822063362707bf

Block:
26301021

Transaction index:
199

Receipt status:
SUCCESS

Token contract:
0xdac17f958d2ee523a2206206994597c13d831ec7

Event:
AddedBlackList(address)

Decoded event address:
0xaa246bf639586a6ba46762d378ce50ca4fc654a0

Result:
FREEZE_EVENT_VERIFIED: PASS

The transaction receipt, event signature,
emitting contract, and target address matched.

The target's isBlackListed(address) query
was independently reported as true.

The third-party event tracker reported:
2026-10-29 21:15:03 UTC.

The timestamp remains attributed to the tracker
until independently matched to the block timestamp.

## 6. Balance Reconciliation

Total observed incoming:
175,000,000.000000 USDT

Total observed outgoing:
127.672480 USDT

Net observed transfers:
174,999,872.327520 USDT

Historical balance at end of freeze block:
174,999,872.327520 USDT

Result:
RECONCILIATION PASS

The observed transfer-log net exactly matched
the historical token balance.

No token balance difference was observed between
block 26301020 and block 26301021.

The blacklist transaction was at transaction
index 199 within block 26301021.

The exact intra-block balance is supported by
the matching end-of-block balances and transfer
log reconciliation, conditional on complete logs
and absence of non-Transfer balance adjustments.

A transaction-level state trace has not
independently established the precise balance
at the execution instant.

## 7. Later Balance Difference

A later Etherscan display reported:

174,999,872.327620 USDT

Freeze-block ending balance:

174,999,872.327520 USDT

Difference:

0.000100 USDT

The cause and transaction hash of this later
balance change have not been verified.

Do not classify it as recovered or escaped funds.

## 8. Evidence Classification

OBSERVED FROM USER-EXECUTED RPC:
- Successful blacklist transaction receipt.
- Matching AddedBlackList event.
- Initial 175M USDT Transfer event.
- Pre-blacklist 127.672480 USDT Transfer event.
- Historical balances at four blocks.
- Exact balance and Transfer-log reconciliation.

INFERRED:
- Approximately 174.999872M USDT was subject
  to the verified address blacklist at execution,
  subject to intra-block state verification.

UNKNOWN:
- Precise intra-transaction balance trace.
- Cause of later 0.000100 USDT increase.
- Purpose of 127.672480 USDT transfer.
- Actual controlling individuals.
- Further movements of transferred 127.672480 USDT.
- Complete incident-wide frozen asset total.

## 9. Research Boundaries

- Address labels do not prove identity.
- Blacklisting is not the same as recovery.
- Frozen balances must not be added to total losses.
- Intermediary transfers must not be double-counted.
- No original RPC response files have been
  independently archived in this checkpoint.
- Preserve prior Bitcoin 547-sat research.
- Keep this CASE on a separate research branch.

## 10. Next Research

1. Independently verify freeze block timestamp.
2. Archive receipt and token logs with hashes.
3. Verify intra-block balance assumptions.
4. Trace the later 0.000100 USDT difference.
5. Investigate the 127.672480 USDT destination
   only if relevant to the incident-wide objective.

## Evidence Links

Initial receipt:
https://etherscan.io/tx/0xb6d7d3ffcbdd0465e1ab743a8d943218176cac7b15edefa7b7bcd5e853e4266f

Pre-freeze outgoing transfer:
https://etherscan.io/tx/0x11be88b460501b4652e760c41e08cc1f18575e14b6c6ffbb3383e043c2decf34

Blacklist transaction:
https://etherscan.io/tx/0x0c07a5e428ce233a3bcb40f257ad899594421341d63ce94016822063362707bf

Recipient:
https://etherscan.io/address/0xaa246bf639586a6ba46762d378ce50ca4fc654a0
