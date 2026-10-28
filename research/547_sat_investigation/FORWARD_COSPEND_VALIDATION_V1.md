# 547-Sat Forward Co-Spend Validation V1

Date: 2026-10-28
Status: VERIFIED SCREEN / NO OWNERSHIP ATTRIBUTION

## Source Inventory
- Original creation transactions: 40
- Recorded 547-sat outputs: 17,182
- Recorded spent outputs: 11,415
- Distinct spending transactions: 6,975

## Exploratory Sample
- Selection: First 100 spending TXIDs in lexical order
- Transactions with >=100 BTC other inputs: 9
- Not a representative or random sample

## Live On-Chain Verification
- Selected transactions verified: 9
- Total 547-sat inputs: 78
- Inputs matching original tracked inventory: 9
- Other 547-sat inputs: 69
- Distinct creation TXIDs for other inputs: 60
- Creation TXIDs appearing more than once: 5

## Evidence Boundary
OBSERVED:
- Counts match the committed CSV inventory.
- Selected nine transactions were rechecked against
  the public mempool.space transaction API.

UNKNOWN:
- Whether the 60 additional creation transactions
  share an operator with the original 40.
- Whether dust funding and high-value BTC funding
  share historical ancestry.
- Sender identity, intent and beneficial ownership.

## Limitations
- The full historical inventory was not independently
  re-fetched in this validation.
- No inference about the full 6,975 transaction
  population follows from the 100-TX sample.
- Co-spending does not prove common ownership.

## Next Priority
Return to the original 40 creation transactions
and the 32 non-547-sat inputs of the reference
1,500 BTC transaction.

Test historical funding connections using exact
UTXO paths and bounded backward tracing.

Preserve frozen investigation map V1.
