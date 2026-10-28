# 547-Sat Funding Ancestry — Depth-2 Screen V1

Date: 2026-10-28
Status: SCREEN COMPLETE / NO ATTRIBUTION

## Research Question

Do the funding sources of the original 547-sat
transfers and the high-value BTC inputs share
observable transaction ancestry?

## Scope

Reference TXID:
64a87c3d7540876516d0bf274fcc4773c0d59d07e960287b1d1ddbf690335b08

- Dust funding root outpoints: 51
- High-value funding root outpoints: 32
- Additional backward depth: 2 hops
- API transactions fetched: 212

## Results

DUST:
- Hop 1 observed ancestor TXIDs: 110
- Hop 2 observed ancestor TXIDs: 178

LARGE BTC:
- Hop 1 observed ancestor TXIDs: 101
- Hop 2 observed ancestor TXIDs: 681

Shared ancestor TXIDs: 0

## Evidence Classification

OBSERVED:
No shared ancestor TXID was identified within
the bounded investigation.

UNKNOWN:
- Whether deeper ancestry contains a common source.
- Whether the two funding groups share an operator.
- Sender identity or beneficial ownership.
- Intent or criminal involvement.

## Limitations

- Public mempool.space API was used.
- No independent Bitcoin node validation.
- TXID-level ancestry screening is not a complete
  outpoint-level proof of common fund ownership.
- The tracing implementation retains representative
  paths by TXID, not every alternative outpoint path.
- No match within this depth does not establish
  that funding sources are independent.

## Next Research Priority

Examine the original 40 dust creation transactions
for repeated funding patterns, exact UTXO links,
and potential shared funding structures.

Do not expand backward tracing without a
specific hypothesis and bounded research budget.

Frozen investigation map V1 remains unchanged.
