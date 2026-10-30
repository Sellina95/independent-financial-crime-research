# USDT Freeze Timeline & Coverage Audit — V4

Research date: 2026-10-30
Network: Ethereum Mainnet
Branch: research/case-binance-2026

Status: INTERIM EVIDENCE CHECKPOINT

## Scope

This checkpoint records user-executed JSON-RPC
queries and reported on-chain verification results.

It is not a complete incident-wide loss,
recovery, or freeze-coverage estimate.

Token: Ethereum USDT
Contract:
0xdAC17F958D2ee523a2206206994597C13D831ec7

Blacklist discovery window:
Blocks 26300770–26301050

## 1. Blacklist Event Discovery

Eight AddedBlackList events were observed
in the specified window.

Three addresses had positive balances
at their respective blacklist blocks.

Five addresses had zero USDT balances
at their respective blacklist block boundaries.

The event count is specific to this
contract and block window.

## 2. Positive-Balance Blacklist Cases

### Case A — Root recipient

Address:
0x5227f603c1ee34ce3c06efe6477003bdfccb2f8c

Blacklist block: 26300954
Transaction index: 88

Blacklist TX:
0x7baba482077843514d9c72bac0110ba0916b0814288a72917e2c3bb27a9d8659

Balance immediately before block:
971,149,299.483240 USDT

Balance at block end:
971,149,299.483240 USDT

Transfer-based intra-block reconciliation:
PASS

### Case B — 175M branch

Address:
0xaa246bf639586a6ba46762d378ce50ca4fc654a0

Blacklist block: 26301021
Transaction index: 199

Blacklist TX:
0x0c07a5e428ce233a3bcb40f257ad899594421341d63ce94016822063362707bf

Transfer-based balance at blacklist:
174,999,872.327520 USDT

Prior outgoing:
127.672480 USDT

Outgoing TX:
0x11be88b460501b4652e760c41e08cc1f18575e14b6c6ffbb3383e043c2decf34

Reconciliation:
PASS

### Case C — Newly identified 30M branch

Address:
0xb171ca86f82070282138352ff7111b494060c8c3

Blacklist block: 26301041
Transaction index: 13

Blacklist TX:
0x3445389c8aceb50fe1c155a1208f7289cc8f7f5950139e21dc405333d1aedc93

USDT balance before block:
30,000,000.000000

USDT balance after block:
30,000,000.000000

Transfer-based balance at blacklist:
30,000,000.000000 USDT

Intra-block reconciliation:
PASS

Incoming source:
0xccbef95633adb5cd2b5038db5a38d77e726ca263

Incoming block: 26301027

Incoming TX:
0x1e6f851d072ae0ad448dca2446552cbb4e76516029b34980d5189e4353aae7a7

Earlier identified upstream transfer:
0x7aa4d3029e4c6a8e916300014ad95b6d6c03bfd1
to
0xccbef95633adb5cd2b5038db5a38d77e726ca263

Upstream block: 26301002
Amount: 30,000,000 USDT

## 3. Combined Balance

Case A:   971,149,299.483240 USDT
Case B:   174,999,872.327520 USDT
Case C:    30,000,000.000000 USDT

Total: 1,176,149,171.810760 USDT

Classification:
Transfer-reconciled blacklist-time
balances for three distinct addresses.

NOT classified as:
- Incident-wide frozen total
- Recovered assets
- Final financial loss
- A percentage of the initial theft

## 4. Zero-Balance Blacklist Cases

The following addresses had zero USDT
at both boundaries of their blacklist blocks:

0x9749292d74fd460982d0912ea9515ea24736c762
0x0ddf0480016e6bcb2c1f5d190d221fba1320697e
0x8d53903625b8e839b9df4bd28b0efb1cd6b8639a
0x7aa4d3029e4c6a8e916300014ad95b6d6c03bfd1
0xccbef95633adb5cd2b5038db5a38d77e726ca263

Their intra-block state has not been
individually established in this checkpoint.

Do not count the amounts that previously
passed through them as frozen balances.

## 5. Other Verified Flow Evidence

Root direct outflow in initial audit window:
500,000,000 + 200,000,000 USDT

The 200M branch subsequently distributed
its entire observed receipt.

The 190M intermediary sent:
60,000,000 USDT to an Aave-associated
aToken contract
and 130,000,000 USDT to another address.

Two receipts showed corresponding
aEthUSDT mint events.

Borrowing ETH has NOT yet been verified.

The 130M and subsequent 80M branches
were further subdivided, with multiple
recipient addresses recurring.

Avoid double-counting intermediate flows.

## 6. Evidence Classification

OBSERVED FROM USER-EXECUTED RPC:
- Eight blacklist events in the window
- Three positive-balance blacklist cases
- Successful blacklist transaction receipts
- Relevant historical USDT balances
- Transfer-based intra-block reconciliations
- Source transfer into the 30M recipient
- Aave-associated USDT transfer and
  corresponding aToken mint events

INFERRED:
- The three listed balances were subject to
  USDT blacklist transfer restrictions,
  conditional on contract semantics and
  the transfer-based reconciliation.

UNKNOWN / PENDING:
- Incident-wide initial loss by asset
- Full asset provenance and attribution
- Other or later blacklist events
- Other frozen addresses and amounts
- Internal state-trace verification
- Aave debt and borrowed-asset movements
- Final destination of remaining branches
- Amount recovered, if any

## 7. Next Steps

1. Build a deduplicated USDT flow ledger.
2. Continue tracing major unclassified branches.
3. Verify Aave supply and borrow mechanisms.
4. Extend blacklist discovery beyond this window.
5. Reconcile all distinct asset origins.
6. Repeat for ETH and other affected assets.
7. Reconstruct a source-cited UTC timeline.
8. Prepare a cautious LinkedIn research report.

Do not make criminal identity attributions
from address labels alone.

This file summarizes terminal-observed results;
raw RPC responses have not yet been archived.
