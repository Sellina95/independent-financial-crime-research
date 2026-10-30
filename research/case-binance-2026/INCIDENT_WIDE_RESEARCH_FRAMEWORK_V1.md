# Incident-Wide Asset Tracing — Research Framework V1

## Research Objective

Reconstruct the observable asset movements associated
with the reported October 2026 Binance incident.

The investigation covers all identified assets,
not only USDT.

Research questions:

1. Which assets moved from the identified source?
2. What is the verified origin of those assets?
3. Where were the assets transferred?
4. Were assets swapped, bridged, supplied or borrowed?
5. Which assets were restricted or frozen, and when?
6. How much remains verified, unresolved or unknown?

## Research Workflow

| Stage | Research Area | Objective |
|---|---|---|
| 1 | Asset Inventory | Identify ETH and all token contracts, symbols, decimals and amounts associated with the initial transaction |
| 2 | Provenance | Verify source addresses, source transactions and the evidence supporting Binance attribution |
| 3 | Fund Flow | Reconstruct major asset movements and recipient branches |
| 4 | Transformation | Verify swaps, bridges, lending deposits, borrowing and other asset conversions |
| 5 | Containment | Verify blacklist events, token restrictions, balances and timing |
| 6 | Reconciliation | Reconcile distinct asset origins, movements, balances and unresolved amounts without double-counting |

## Evidence Standards

Every research finding must be classified as:

- OBSERVED: Directly supported by verified transaction,
  event, contract state or primary-source evidence.
- INFERRED: An interpretation supported by observations
  but not independently proven.
- UNKNOWN: Information not established by available evidence.

Additional rules:

- Never infer criminal identity from wallet labels.
- Do not treat blacklist registration as asset recovery.
- Do not equate transferred value with final financial loss.
- Do not double-count funds moving through intermediaries.
- Distinguish token amounts from USD-equivalent values.
- Preserve exact block numbers, transaction hashes,
  contract addresses and observation timestamps.
- Use a defined investigation cutoff for balances.
- Record incomplete paths explicitly.
- Avoid claiming incident-wide completeness without
  verifying the full initial asset and transaction scope.

## Initial Scope

Start from the identified Ethereum transaction:

0x53bd38b816c23e74134786c29a8c18d792777998a3b9326047b583100e88e2f3

This is an investigation anchor, not proof that
the entire incident is represented by this transaction.

Expand the scope only when supported by evidence.

## Existing Evidence

Prior USDT research checkpoints:
- V1: Initial evidence checkpoint
- V2: USDT movement and blacklist evidence
- V3: Historical balance and transfer reconciliation
- V4: Blacklist timeline and balance coverage

These checkpoints remain unchanged.

## Research Deliverables

1. Incident-wide asset inventory
2. Source and provenance evidence register
3. Deduplicated transaction and fund-flow ledger
4. Asset transformation and DeFi exposure register
5. Freeze and containment timeline
6. Asset-by-asset reconciliation
7. UTC incident chronology
8. Evidence-based public research summary

## Publication Boundary

A future LinkedIn report must distinguish
verified facts, interpretations and unknowns.

Do not publish an incident-wide total until
its source coverage and valuation methodology
have been validated.
