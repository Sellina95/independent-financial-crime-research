# Interim Forensic Timeline V2

## Scope
Ethereum USDT fund-flow research.
Research branch only. No criminal attribution established.

## Chronological observations

| Block | Event | Evidence |
|---|---|---|
| 26300770 onward | Candidate movements toward central address 0x5227f603c1ee34ce3c06efe6477003bdfccb2f8c | Initial ledger; varying verification levels |
| 26300799 | Central address sends 500,000,000 USDT to 0x9749292d74fd460982d0912ea9515ea24736c762 | Verified transaction and receipt |
| 26300815 | Central address sends 200,000,000 USDT to 0x0ddf0480016e6bcb2c1f5d190d221fba1320697e | Verified transaction and receipt |
| 26300911 | 200M branch sends 190,000,000 USDT to 0x8d53903625b8e839b9df4bd28b0efb1cd6b8639a | Verified second-hop evidence |
| 26300942 | 500M branch sends 175,000,000 USDT to 0x811f15855476156ebf86ba3b84fafb8ceaa4e84c | Verified second-hop evidence |
| 26300988 | 175,000,000 USDT enters 0xaa246bf639586a6ba46762d378ce50ca4fc654a0 | Receipt verified |
| 26301011 | 127.672480 USDT leaves that address | Receipt verified |
| 26301020 | Historical USDT balance: 174,999,872.327520 | Balance audit PASS |
| 26301021 | Tether AddedBlackList event; block-end balance unchanged | Event and receipt audit PASS |
| 26301027 | 30,000,000 USDT enters 0xb171ca86f82070282138352ff7111b494060c8c3 from 0xccbef95633adb5cd2b5038db5a38d77e726ca263 | Transfer receipt PASS; upstream chain evidence archived |
| 26301041 | Prior research reports blacklist registration for the 30M receiver | Blacklist event, receipt and historical balances PASS |

## Confirmed reconciliation
175,000,000 - 127.672480 = 174,999,872.327520 USDT.

## Anti-double-counting
- 500M + 200M = 700M USDT transferred onward.
- The 175M belongs to a downstream branch of that 700M.
- Do not add 175M again to the 700M.
- The 30M receiving address is linked through verified transactions to the 200M branch of the 700M network. Exclusive fund provenance remains unproven.
- Blacklisted account balances are not necessarily recovered assets.
- Ownership and incident attribution remain unverified.

## Evidence authority
1. Raw blockchain transactions, receipts and logs
2. Historical token balance snapshots
3. Reconciled ledgers and audited reports
4. Terminal-only observations (not yet archived)
5. Hypotheses requiring verification


## 30M USDT upstream chain — verified

| Block | Transfer | USDT |
|---|---|---:|
| 26300911 | 200M branch -> 0x8d539... | 190,000,000 |
| 26300956 | 0x8d539... -> 0x77edef... | 130,000,000 |
| 26300980 | 0x77edef... -> 0x7aa4... | 80,000,000 |
| 26301002 | 0x7aa4... -> 0xccbef... | 30,000,000 |
| 26301027 | 0xccbef... -> 0xb171... | 30,000,000 |
| 26301041 | Tether AddedBlackList for 0xb171... | Balance: 30,000,000 |

Recipient full address:
`0xb171ca86f82070282138352ff7111b494060c8c3`

Blacklist TX:
`0x3445389c8aceb50fe1c155a1208f7289cc8f7f5950139e21dc405333d1aedc93`

## 30M balance audit

- Before 30M inflow: 0 USDT
- Immediately preceding blacklist block: 30,000,000 USDT
- Blacklist block-end: 30,000,000 USDT
- Historical balance: PASS
- Blacklist event and receipt: PASS
- Actual asset recovery: NOT ESTABLISHED
- Continued current blacklist status: NOT TESTED

## Reconciliation rules

- 175M and 30M are separate downstream branches of the observed 700M network.
- Do NOT add downstream transfer amounts to the original 700M.
- Do NOT call a blacklist-time balance a recovered amount.
- A connected address graph does NOT prove exclusive economic provenance.
- No criminal attribution or Binance ownership is established by these transfers.

## New evidence

- evidence/30m_upstream_bridge_v1/manifest.json
- evidence/30m_upstream_bridge_v1/ (4 transactions + 4 receipts)
- evidence/30m_blacklist_audit_v1/balance_snapshots.json
- evidence/30m_blacklist_audit_v1/blacklist_event.json
- evidence/30m_blacklist_audit_v1/blacklist_receipt.json

## Next research gates

1. Audit other 700M downstream branches for missing movements.
2. Verify blacklist-time balances of the remaining relevant addresses.
3. Produce canonical event ledger with UTC, block, transaction index and log index.
4. Reconcile all independently blacklisted balances without double counting.
5. Maintain separate evidence for third-party incident and wallet attribution.

## Version history

- V1: Initial interim timeline and pending 30M path.
- V2: Verified 30M upstream connection and blacklist balance audit.
