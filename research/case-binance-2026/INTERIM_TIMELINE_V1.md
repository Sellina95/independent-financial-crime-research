# Interim Forensic Timeline V1

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
| 26301027 | 30,000,000 USDT enters 0xb171ca86f82070282138352ff7111b494060c8c3 from 0xccbef95633adb5cd2b5038db5a38d77e726ca263 | RPC scan observed; receipt pending |
| 26301041 | Prior research reports blacklist registration for the 30M receiver | Dedicated audit pending |

## Confirmed reconciliation
175,000,000 - 127.672480 = 174,999,872.327520 USDT.

## Anti-double-counting
- 500M + 200M = 700M USDT transferred onward.
- The 175M belongs to a downstream branch of that 700M.
- Do not add 175M again to the 700M.
- The 30M source is NOT YET LINKED to the 700M branches.
- Blacklisted account balances are not necessarily recovered assets.
- Ownership and incident attribution remain unverified.

## Evidence authority
1. Raw blockchain transactions, receipts and logs
2. Historical token balance snapshots
3. Reconciled ledgers and audited reports
4. Terminal-only observations (not yet archived)
5. Hypotheses requiring verification

## Next investigation
1. Verify and archive the 30M transaction receipt.
2. Trace USDT entering 0xccbef95633adb5cd2b5038db5a38d77e726ca263.
3. Compare its incoming path against both 700M branches.
4. Verify 30M recipient historical balance and blacklist event.
5. Add UTC timestamps, transaction indices and log indices.
6. Reconcile event-level flows without double counting.

## Primary evidence
- OUTFLOW_TRANSACTION_LEDGER_V1.csv
- FOLLOW_ON_FLOW_LEDGER_V1.csv
- evidence/root_usdt_outflows_v1/
- evidence/second_hop_usdt_v1/
- evidence/second_hop_receipts_v1/
- BLACKLIST_175M_CASE_AUDIT_V1.md
- evidence/blacklist_balance_175m_v1/
- evidence/blacklist_event_175m_v1/
- evidence/blacklist_flow_175m_v1/
