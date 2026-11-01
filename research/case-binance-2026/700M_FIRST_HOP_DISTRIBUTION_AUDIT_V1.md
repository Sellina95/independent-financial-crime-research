# 700M USDT — First-Hop Distribution Audit V1

## Scope

Ethereum USDT transfers from two addresses that received
500M and 200M USDT, respectively, from the central address.

This audit covers the preserved second-hop transfer evidence.
It does not establish Binance incident attribution.

## Evidence

- evidence/second_hop_usdt_v1/transfer_logs.json
- evidence/second_hop_receipts_v1/manifest.json
- 13 archived transaction receipts

Preserved transfer log SHA256:
7b8e0b68f6cabebe2c9789e5b4a76437a0b44b7c8f85a81925e2054a894d2300

## Reconciliation

| Source address | Known inflow | Observed outflow | Difference |
|---|---:|---:|---:|
| 0x9749292d74fd460982d0912ea9515ea24736c762 | 500,000,000 | 500,000,000 | 0 |
| 0x0ddf0480016e6bcb2c1f5d190d221fba1320697e | 200,000,000 | 200,000,000 | 0 |
| Total | 700,000,000 | 700,000,000 | 0 |

All amounts are USDT.

## Verification

- Transfer events: 20
- Unique transactions: 13
- Archived receipts: 13
- Missing receipts: 0
- Duplicate transaction/log-index pairs: 0
- Receipt SHA256 checks: PASS
- Transaction status checks: PASS
- Transfer log versus receipt checks: PASS
- Reconciliation difference: 0 USDT

## Observed

The preserved transfer events reconcile exactly to the
two known incoming amounts.

The 200M branch distributed 190M USDT in one transfer
and 10M USDT across eight other transfer events.

The 500M branch distributed 500M USDT across
eleven transfer events.

## Limitations

- The audit validates the preserved evidence set.
- Independent completeness of all on-chain movements
  over the interval has not been established.
- Additional inflows outside the examined evidence
  are not ruled out.
- Downstream recipient balances are not reconciled here.
- Exclusive economic provenance is not established.
- Address ownership and criminal attribution are unknown.
- Binance incident linkage is not established.
- Blacklisted balances are not equivalent to recovered assets.

## Next Research Gate

Classify downstream recipients into:

1. VERIFIED — follow-on movements supported by archived evidence.
2. PARTIALLY TRACED — some movements verified, incomplete coverage.
3. UNEXPLORED — no validated follow-on research yet.

Prioritize unresolved material flows and avoid repeating
already verified first-hop work.
