# STEP 85 — A97B Outgoing Event Audit V1

## Research scope

A97B: `0xa97bf7836f8a08f9ed91d41453d371493fae8d10`

This report reconciles the previously indexed outgoing movement
events from A97B. It does not claim a complete historical reconstruction
of all funds controlled by the address.

## Event reconciliation

| Event structure | Count |
|---|---:|
| DEX/WETH-compatible pattern | 1,126 |
| Direct native ETH transaction | 4 |
| Other DEX router pattern | 3 |
| ERC-20 exceptions | 53 |
| **Total** | **1,186** |

Event-count conservation: **PASS**

STEP 80 reports 1,184 distinct outer transaction hashes.
Events and outer transactions must not be treated as interchangeable.

## ERC-20 exception audit

| Structure | Events |
|---|---:|
| Direct transfer structure match | 28 |
| External caller, transfer selector | 17 |
| Other function selectors | 8 |
| **Total** | **53** |

All 53 source ERC-20 events were matched against cached receipts.

For the 28 direct transfer structures, the outer call target, recipient
and amount matched the relevant Transfer event.

The 17 external-caller events show recurring contract execution.
Large Transfer-log volumes, failed standard balanceOf calls,
and non-standard selector observations warrant caution.
These findings do not independently prove artificial events,
address poisoning, or a real decrease in A97B token balances.

The remaining eight events comprise two zero-address events,
three mass-event transactions, two multicall-selector transactions,
and one other contract execution.

A zero-address Transfer event is not by itself definitive proof
of an economically meaningful token burn.

## Direct native ETH transactions

Four separately matched native ETH transactions total
**10647.2 ETH** across three immediate recipient addresses.

This is an observed transaction total, not an independently proven
total of stolen or incident-attributable ETH.

## External attribution crosswalk

- Research universe: 124 unique addresses
- Direct FBI and Elliptic listing: 1
- Elliptic-only listing: 5
- Neither list: 118

External address listings do not establish freezes, ownership
or exact incident-fund provenance.

## Evidence limitations

**Observed:** transaction records, receipt logs, directly matched
ETH transfers, indexed event counts and external-list membership.

**Inferred / pattern-based:** DEX/WETH-compatible event structures.

**Unknown:** actual balance effects of relevant non-standard ERC-20
events, complete swaps and settlement, final beneficiaries,
ownership and specific stolen-fund attribution.

## Audit status

**Indexed-event structural reconciliation: PASS**

**Full economic fund-flow reconstruction: NOT ESTABLISHED**

This is a research-branch audit artifact, not a publication-ready
claim of exhaustive forensic coverage.
