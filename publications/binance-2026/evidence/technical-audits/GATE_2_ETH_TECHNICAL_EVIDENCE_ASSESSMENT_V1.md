# AXIOM — Ethereum Gate ② Technical Evidence Assessment V1

## Assessment
**Technical mechanism: STRONGLY CORROBORATED**

**Official incident attribution and unauthorized status: OPEN**

This assessment concerns the technical reconstruction of T02/T03/T17.
It does not establish who controlled the signing key or whether Binance
corporately authorized any transaction.

## OBSERVED — Independently tested evidence

1. T02: 50 EIP-7702 authorization signatures all recover to Binance 14.
2. T02: Nonce-only replay accepts one authorization at index 15.
3. Historical code: Binance 14 had no code before T02, then the
   expected delegation code after T02 and before T03's block.
4. T03 block: no preceding Type-4 transactions.
5. Delegated implementation: T03 selector matches its dispatcher,
   and T03 sender matches the embedded caller restriction.
6. T03 calldata: one recipient and 65 address entries comprising
   the zero address plus 64 token contracts.
7. Runtime: 64 ERC-20 transfer calls to that recipient; 63 matching
   Transfer events and one reverted call.
8. Failure handling: failed call at position 27, followed by 37
   further non-error token calls; matching custom event exists.
9. Historical balances: USDT decreased by 1,615,409,498.97324
   at Binance 14 and increased by the same amount at the recipient.
10. Failed-token historical balances remained unchanged.
11. T17: delegation code was absent at the checked block-end state.

## INFERRED — Mechanism interpretation

- The evidence strongly supports a delegated batch asset-transfer
  mechanism involving ETH and ERC-20 tokens.
- The contract's observed behavior is consistent with continuing
  after an individual token transfer revert.
- The zero address in calldata likely represents native ETH.

## UNKNOWN — Unresolved evidentiary gates

- Whether Binance authorized the EIP-7702 signatures internally.
- How the signatures were obtained or the signing key was controlled.
- Whether the incident was unauthorized under corporate records.
- Beneficial ownership of downstream addresses.
- Full instruction-level replay of T03.
- Transaction-level balance deltas independent of other block activity.
- Official transaction-by-transaction mapping to the incident.

## Evidence classification

- Historical delegation state: VERIFIED BLOCK-END STATE
- Authorization signer recovery: VERIFIED CRYPTOGRAPHIC RECOVERY
- Authorization processing: NONCE-ONLY REPLAY
- Selector and caller checks: VERIFIED STATIC CODE
- Asset calls and events: VERIFIED AGAINST LOCAL TRACE / RECEIPT
- Selected historical balances: VERIFIED BLOCK-END DIFFERENCES
- Actual corporate authorization: UNKNOWN

## Audit boundary

No perpetrator identity, motive, internal compromise mechanism,
or legal conclusion is asserted.

Do not merge this assessment into an allegation of proven theft.
Keep original evidence files and research branch intact.
