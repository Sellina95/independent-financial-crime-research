# AXIOM — Publication Claims Audit V1

## Scope

Automated consistency audit against existing committed
research evidence. No live blockchain RPC calls.

## Results

- Inventory evidence files checked: 15
- Inventory SHA256 matches: 15
- Structured claim checks: 9
- Checks passed: 9
- Checks failed: 0

## Automated checks

| Claim | Result |
|---|---|
| 50 EIP-7702 signatures recovered | PASS |
| One nonce-applicable authorization | PASS |
| Historical delegation lifecycle | PASS |
| T03 calldata and 64 token attempts | PASS |
| T03 failed token call and continuation | PASS |
| USDT historical balance reconciliation | PASS |
| Failed-token balances unchanged | PASS |
| 700M USDT subsequent distribution | PASS |
| Incident attribution is not overstated | PASS |

## Publication restrictions

1. Do not assert that Binance corporately approved or
   did not approve the EIP-7702 authorizations.
2. Do not claim that signing-key compromise is proven.
3. Do not identify real-world perpetrators.
4. Do not equate third-party incident attribution with
   official Binance transaction-level confirmation.
5. Do not equate block-end balance differences with
   transaction-isolated state changes.
6. Do not treat the 700M downstream distribution as
   exclusively sourced from T03.
7. Do not double-count intermediary transfers.
8. Do not equate blacklist registration with recovered funds.
9. Do not claim that a finding is original merely because
   it was absent from reviewed publications.
10. Do not describe this as a full reconstruction
    of the Binance incident.

## Human review still required

- Confirm live source authenticity and publication provenance.
- Review the original transaction/trace/receipt artifacts.
- Verify that local calculations are reproducible by others.
- Check citation quality and public-source comparisons.
- Check report wording against evidence limitations.
- Review raw evidence availability in the public repository.
- Confirm that no private credentials or sensitive
  operational data are included in published files.

## Decision

AUTOMATED_CONSISTENCY:
PASS

PUBLICATION_APPROVED: NO

Reason: Automated checks cannot replace independent
raw-evidence verification and editorial review.

FIXED RESEARCH MAP V1: UNCHANGED.
Gate 2: OPEN.
Gates 3–5: PARTIAL.
