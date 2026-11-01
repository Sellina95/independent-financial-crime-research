# AXIOM — Evidence Difference Protocol V1

## Mission
Track disagreements, missing disclosures, new paths and
verification blockers without treating suspicion as proof.

## Categories
- CONTRADICTION: Two verified sources make incompatible claims
  about the same event, unit, scope and timestamp.
- COVERAGE_GAP: A published source omits information needed
  for independent comparison.
- NEW_LEAD: A previously unassessed path, address, event
  or mechanism merits investigation.
- ACCESS_BLOCKED: Rate limit, HTTP 403, unavailable RPC or
  otherwise inaccessible underlying evidence.
- RESOLVED: A previously recorded difference has been
  reconciled with documented evidence.

## Mandatory controls
1. Preserve exact source URLs, publication times, hashes
   and observation times when available.
2. Distinguish Binance OFFICIAL, THIRD_PARTY and
   AXIOM_ONCHAIN_OBSERVED evidence.
3. Do not call omission a contradiction.
4. Do not attribute wallets to attackers without evidence.
5. Separate event time, blockchain inclusion time,
   announcement time and freeze execution time.
6. Preserve asset units and prevent double counting.
7. Record competing explanations and a falsification test.
8. Never silently delete historical entries.
   Update status and link to resolution evidence.
9. Keep research-only evidence on the research branch.
10. Do not publish a new lead as an established crime.

## Next research priorities
- Incident-specific transaction IDs and official attribution
- Additional first-hop routes not covered by published reports
- Freeze request versus on-chain execution timestamp
- Cross-chain asset conservation and duplicate counting
- EIP-7702 authorization and execution linkage

## Current status
Gate 2 remains OPEN.
The initial register contains no verified CONTRADICTION.
