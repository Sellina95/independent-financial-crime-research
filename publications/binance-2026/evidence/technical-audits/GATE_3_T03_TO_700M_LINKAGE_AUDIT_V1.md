# AXIOM — T03 to 700M USDT Linkage Audit V1

## Objective

Test whether the previously audited T03 asset movement
and subsequent 700M USDT distribution share a verifiable
on-chain address and chronological sequence.

This is a scoped evidence reconciliation, not a complete
transaction-level conservation proof.

## 1. Verified observations

### T03 — Source to central recipient

- Transaction: `0x53bd38b816c23e74134786c29a8c18d792777998a3b9326047b583100e88e2f3`
- Block: 26300770
- Source: `0x28c6c06298d514db089934071355e5743bf21d60`
- Recipient: `0x5227f603c1ee34ce3c06efe6477003bdfccb2f8c`
- USDT block-end balance difference at source:
  -1,615,409,498.973240 USDT
- USDT block-end balance difference at recipient:
  +1,615,409,498.973240 USDT

Evidence:
- OUTFLOW_TRANSACTION_LEDGER_V1.csv
- GATE_2_ETH_T03_HISTORICAL_BALANCE_AUDIT_V1.json

### Subsequent 700M distribution

| Block | USDT outgoing |
|---|---:|
| 26300799 | 500,000,000 |
| 26300815 | 200,000,000 |
| Total | 700,000,000.000000 |

Both transfers originate from the same central address.

Evidence:
- FOLLOW_ON_FLOW_LEDGER_V1.csv
- 700M_FIRST_HOP_DISTRIBUTION_AUDIT_V1.md
- INTERIM_TIMELINE_V2.md

## 2. Chronological and arithmetic comparison

- T03 block: 26300770
- First 500M outflow block: 26300799
- Second 200M outflow block: 26300815
- Observed initial USDT block-end increase:
  1,615,409,498.973240 USDT
- Observed later distribution:
  700,000,000.000000 USDT
- Arithmetic difference:
  915,409,498.973240 USDT

The difference is NOT a confirmed remaining balance.
Other inflows, outflows and changes are not fully
reconciled in this scoped comparison.

## 3. Linkage assessment

ADDRESS CONTINUITY: VERIFIED IN PRESERVED RECORDS

CHRONOLOGICAL ORDER: VERIFIED

700M FIRST-HOP DISTRIBUTION:
PREVIOUSLY AUDITED

EXCLUSIVE SOURCE-OF-FUNDS PROVENANCE:
NOT ESTABLISHED

INCIDENT-WIDE CONSERVATION:
NOT ESTABLISHED

OFFICIAL BINANCE TRANSACTION ATTRIBUTION:
OPEN

CORPORATE AUTHORIZATION:
UNKNOWN

The data establishes that the same address received
a T03-associated USDT balance increase and later sent
700M USDT.

It does NOT prove that the 700M consists exclusively
of the particular units transferred in T03.

## 4. Freeze research boundary

The separate 175M and 30M paths are downstream
research segments.

They must not be added to the 700M first-hop
outflows when calculating total moved funds.

Blacklist-time balances are not equivalent to
actual recovered assets.

Evidence:
- INTERIM_TIMELINE_V2.md
- USDT_FREEZE_BALANCE_AUDIT_V3.md

## 5. Evidence limitations

1. The current calculation uses block-end historical
   balance differences, not transaction-isolated
   prestate and poststate.
2. The central address may have additional inflows
   and outflows within the study interval.
3. Address-level continuity does not establish
   exclusive economic provenance.
4. Transaction status, logs and receipts were
   previously audited; this script does not fetch
   or independently re-verify raw blockchain data.
5. Actual authorization, identity, incident-wide
   losses and recovery remain unresolved.

## 6. Decision

RESULT: ADDRESS_AND_TIME_LINKAGE_CORROBORATED

NO EXCLUSIVE_PROVENANCE CLAIM.

Gate 2 remains OPEN.
Gates 3–5 remain PARTIAL.
FIXED RESEARCH MAP V1 remains unchanged.

## 7. Next publication task

Build a consolidated evidence inventory
with source paths, claim boundaries, verification
methods and outstanding blockers.
