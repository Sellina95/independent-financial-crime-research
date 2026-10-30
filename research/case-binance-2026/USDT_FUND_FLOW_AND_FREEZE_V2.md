# Binance Security Incident 2026
## USDT Fund Flow & Freeze Evidence — V2

Status: EVIDENCE CHECKPOINT
Research date: 2026-10-30
Network: Ethereum Mainnet
Token: USDT
Contract: 0xdAC17F958D2ee523a2206206994597C13D831ec7

This research reconstructs public fund movements.
It does not attribute criminal identity or ownership.

## 1. Initial USDT Movement

Transaction:
0x53bd38b816c23e74134786c29a8c18d792777998a3b9326047b583100e88e2f3

Block: 26300770
Time: 2026-10-29 20:24:23 UTC

From:
0x28C6c06298d514Db089934071355E5743bf21d60

To:
0x5227f603C1eE34CE3C06eFe6477003BDfCCB2f8c

Amount: 1,615,409,498.97324 USDT

Evidence: User-captured Etherscan ERC-20 transfer.

## 2. First Distribution

Transaction:
0x68d7d69deaeb9750c38020b4f8d3728146ca8d2267eba1e38cf9b56722ad659a

Block: 26300799

From:
0x5227f603C1eE34CE3C06eFe6477003BDfCCB2f8c

To:
0x9749292d74fd460982d0912ea9515ea24736c762

Amount: 500,000,000 USDT

Evidence: User-provided ERC-20 transfer records.

## 3. Subsequent Transfer

Transaction:
0x1fb992f92a45afec23d7d5740c7958a644fb90ef0cba19ca39bd2c6534fb670b

Block: 26300942

From:
0x9749292d74fd460982d0912ea9515ea24736c762

To:
0x811f15855476156ebf86ba3b84fafb8ceaa4e84c

Amount: 175,000,000 USDT

Status: Success
Evidence: User-captured Etherscan transaction.

## 4. Final Observed Transfer

Transaction:
0xb6d7d3ffcbdd0465e1ab743a8d943218176cac7b15edefa7b7bcd5e853e4266f

Block: 26300988

From:
0x811f15855476156ebf86ba3b84fafb8ceaa4e84c

To:
0xAa246BF639586a6Ba46762D378CE50cA4fc654a0

Amount: 175,000,000 USDT
Status: Success

Evidence: User-captured Etherscan transaction
and ERC-20 transfer.

## 5. Recipient Balance Observation

Address:
0xAa246BF639586a6Ba46762D378CE50cA4fc654a0

User-observed Etherscan balance:
174,999,872.327620 USDT

Difference from observed 175M inflow:
127.672380 USDT

The difference is not yet reconciled
against all token balance changes.

The balance is a snapshot, not historical
proof of the amount at freeze execution.

## 6. Blacklist State

User queried the official USDT contract:

isBlackListed(
0xAa246BF639586a6Ba46762D378CE50cA4fc654a0
)

Reported response: true

OBSERVED:
User-reported contract read confirms the address
was blacklisted at the time of the query.

It does not by itself establish the exact
blacklist activation time.

## 7. Reported Blacklist Event

Third-party event tracker: cryptoalert.report

Reported event: Ban
Reported timestamp: 2026-10-29 21:15:03 UTC
Reported block: 26301021

Reported transaction:
0x0c07a5e428ce233a3bcb40f257ad899594421341d63ce94016822063362707bf

Source:
https://cryptoalert.report/address/0xAa246BF639586a6Ba46762D378CE50cA4fc654a0

Status: REPORTED / ORIGINAL LOG VERIFICATION PENDING

The AddedBlackList event and indexed address
have not been independently checked against
the original Etherscan transaction log.

The blacklist event itself does not encode
the number of USDT held by the address.

## 8. Evidence Classification

OBSERVED:
- Initial 1.615B USDT transfer recorded.
- Subsequent 500M USDT transfer recorded.
- 175M USDT transferred to Exploiter 20.
- 175M USDT transferred to Exploiter 21.
- Final recipient balance observed on Etherscan.
- User-reported isBlackListed response: true.

REPORTED:
- Blacklist transaction and activation time.
- Third-party frozen balance estimate.

INFERRED:
- The observed transfer chain represents a
  traceable subset of the original outflow.
- The blacklist likely restricted subsequent
  USDT transfers from the final recipient.

UNKNOWN:
- Exact balance at blacklist activation.
- Full original blacklist event log.
- Cause of 127.672380 USDT balance difference.
- Complete distribution of the other USDT.
- Final financial loss or recovery.
- Real-world wallet ownership.
- Other-chain movements and total freezes.

## 9. Verification Rules

- Do not sum intermediary transfers as losses.
- Do not treat blacklist state as proof of
  the historical frozen amount.
- Do not treat labels as proof of identity.
- Keep reported and verified evidence separate.
- Do not merge this research into production.
- Preserve all existing Bitcoin research.

## 10. Next Investigation

1. Verify AddedBlackList event in original logs.
2. Reconstruct recipient balance at freeze block.
3. Reconcile the 127.672380 USDT difference.
4. Investigate remaining 500M USDT branches.
5. Verify freeze status of other recipient wallets.

## Transaction Sources

https://etherscan.io/tx/0x53bd38b816c23e74134786c29a8c18d792777998a3b9326047b583100e88e2f3

https://etherscan.io/tx/0x68d7d69deaeb9750c38020b4f8d3728146ca8d2267eba1e38cf9b56722ad659a

https://etherscan.io/tx/0x1fb992f92a45afec23d7d5740c7958a644fb90ef0cba19ca39bd2c6534fb670b

https://etherscan.io/tx/0xb6d7d3ffcbdd0465e1ab743a8d943218176cac7b15edefa7b7bcd5e853e4266f

https://etherscan.io/tx/0x0c07a5e428ce233a3bcb40f257ad899594421341d63ce94016822063362707bf
