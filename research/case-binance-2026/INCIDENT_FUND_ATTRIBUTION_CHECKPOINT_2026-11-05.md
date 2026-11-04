# AXIOM — Incident Fund Attribution Checkpoint

Date: 2026-11-05
Branch: research/case-binance-2026
Status: RESEARCH / NOT FINAL ATTRIBUTION

## 1. Research question

What amount of the 28,000,000 USDT bridged to
Plasma can be defensibly attributed to the
reported Binance incident?

Distinguish:
- Observed transactions and balances
- Conditional source accounting
- Incident attribution
- Legal ownership and unauthorized conduct

## 2. Existing incident evidence

Existing Gate-2 research documents:
- T02: 50 EIP-7702 signature recoveries
- T03: Binance14 source wallet transfer
- T17: subsequent delegation revocation
- External incident TXID cross-references

Important:
Cryptographic signature recovery does not
establish voluntary corporate authorization.
The existing incident attribution matrix
remains UNRESOLVED pending sufficient
independent incident attribution evidence.

## 3. Source-to-branch path

Ethereum USDT:
Binance14 -> Central -> 200M -> 190M -> 60M

STEP 60:
- HOP2 opening balance: 0 USDT
- Source inflow: 190,000,000 USDT
- Outflows to mixed wallet: 10M + 50M
- Other inflows and outflows: 0
- End balance: 130M
- Reconciliation: PASS
- Conditional 190M-source attribution of
  the 60M outgoing: 60M / 60M

STEP 61:
- HOP1 opening balance: 0 USDT
- Central inflow: 200M
- Other outflows: 10M
- Next-hop outflow: 190M
- End balance: 0
- Reconciliation: PASS
- Conditional 200M-source attribution of
  the 190M outgoing: 190M / 190M

STEP 62:
- Central opening balance: 0 USDT
- Binance14 inflow: 1,615,409,498.973240
- Other inflows: 55,739,800.510000
- Other outflows: 500,000,000
- Target outflow: 200,000,000
- Closing balance: 971,149,299.483240
- Reconciliation: PASS
- Conditional Binance14-source allocation
  of target 200M: 144,260,199.490000
  to 200,000,000 USDT

These are conditional, fungible-balance
accounting bounds, not legal taint findings.

## 4. Additional Central inflow

STEP 63:
- 55,739,800.500000 USDT arrived from
  0xdfd5293d8e347dfe59e90efd55b2956a1343963d
- Another 0.010000 USDT arrived separately.

STEP 64:
- Source wallet baseline:
  56,452,803.864299 USDT
- No new incoming USDT in examined interval
- 55,739,800.500000 transferred to Central
- Source wallet provenance prior to baseline
  is not established.

Do NOT classify this source as incident-related
solely because it transferred to Central.

## 5. Mixed wallet

Wallet:
0x23878914efe38d27c4d67ab83ed1b93a74d4086a

STEP 65:
- Baseline: 195,865,280.403528 USDT
- Known branch inflow: 60,000,000
- Other inflows: 35,868,038.335205
- Other inflow addresses: 45
- Other outflows: 25,165,689.154604
- Target outflow: 25,000,000
- End balance: 241,567,629.584129
- Reconciliation: PASS

Under the prior single-tag, fungible-balance
model, attribution of the 25M target outflow
to the 60M tagged inflow remains 0 to 25M.

The baseline and additional incoming sources
are NOT classified as incident funds.

## 6. A/B group through Plasma bridge

Wallet A:
0xb8734a14fbd4aa2d44e6aa830405ffc861ba313c

Wallet B:
0x1c3b25019ed4e4876e7af7903cc3e1e23287c337

STEP 66:
- Baseline combined: 1,178,547.506043
- External inflows: 81,300,997.522314
- External outflows: 82,214,299.603998
- Internal transfer volume: 157,301,000
- Final combined balance: 265,245.424359
- Reconciliation: PASS
- Plasma bridge outflow: 28,000,000
- Tagged 25M contribution to bridge:
  conditional model range 0 to 25M

IMPORTANT:
This is a pooled A/B accounting model.
It does not enforce all per-address
custody constraints.
It does not establish shared ownership.
It does not evaluate all possible
incident-related incoming sources.
The 0-to-25M range applies specifically
to the designated 25M tagged source;
it is NOT a bound on all incident funds
potentially present in the 28M bridge.

EG-08 separately preserves Ethereum-to-Plasma
delivery evidence. Aave deposit transactions
were examined read-only, but their complete
evidence bundle is not yet preserved here.

## 7. Evidence limitations

STEP 60-66 were terminal-based RPC audits.
Full RPC request/response bundles and
reproducible source scripts for these steps
are not archived by this checkpoint.

Results here are reported observations from
terminal audit outputs, not a replacement
for raw evidence and independent replay.

No claim that 28M is confirmed stolen funds.
No claim of an Aave freeze failure.
No identification of wallet owners.

## 8. Next research decision

PRIORITY 1:
Preserve reproducible raw evidence for the
material attribution checkpoints and
address-specific A/B event ledger.

PRIORITY 2:
Determine whether independent incident
evidence links other inflows or historical
balances to the same incident.

PRIORITY 3:
Recalculate attribution using explicit
per-address constraints and compare
alternative defensible tracing conventions.

STOP RULE:
Do not recursively trace every unrelated
source wallet without a material reason to
expect attribution uncertainty to shrink.

## 9. Publication status

RESEARCH CHECKPOINT ONLY.
Not a final forensic opinion or accusation.
