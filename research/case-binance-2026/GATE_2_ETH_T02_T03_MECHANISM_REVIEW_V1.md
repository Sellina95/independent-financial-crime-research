# AXIOM — Ethereum T02/T03 Mechanism Review V1

## T02 — Etherscan browser observations
- TXID: 0xad99264d5532ae0dd04b2004eebda05f25657e70dacb764f7ac8d4ccd051298b
- Explorer displays EIP-7702 type-4 transaction.
- Explorer Authorization tab shows 50 entries:
  1 True and 49 False.
- Valid entry nonce: 18914809.
- Explorer State tab shows wallet nonce:
  18914809 -> 18914810.
- Source: https://etherscan.io/tx/0xad99264d5532ae0dd04b2004eebda05f25657e70dacb764f7ac8d4ccd051298b
- Evidence basis: user-provided Etherscan browser capture/text.
- Raw T02 authorization list not independently replayed.

## T03 — Locally verified call trace
- TXID: 0x53bd38b816c23e74134786c29a8c18d792777998a3b9326047b583100e88e2f3
- Receipt status: SUCCESS
- Root caller: 0x7c8601d4645b93cea45f71e118a729332e6b5ca0
- Root target: 0x28c6c06298d514db089934071355e5743bf21d60
- Total calls: 192
- Calls involving target wallet: 130
- CALL: 80
- STATICCALL: 74
- DELEGATECALL: 38
- Source: evidence/initial_tx_v1/call_trace.json
- Source: evidence/initial_tx_v1/receipt.json

## Interpretation
OBSERVED: T02 explorer evidence indicates one valid authorization.
OBSERVED: T03 invokes the same wallet, which executes token calls.
INFERRED: The events are consistent with delegated execution.
UNKNOWN: Exact delegated code active at the T03 block.
UNKNOWN: Whether the authorization was unauthorized.
CAUTION: Nested DELEGATECALLs do not independently prove EIP-7702.
CAUTION: Explorer attribution labels are third-party claims.

## Decision
T02-to-T03 causal mechanism: PARTIALLY_CORROBORATED.
Unauthorized withdrawal attribution: UNRESOLVED.
Gate 2: OPEN.

## Next validation
Check the target wallet's code at T03 block
26300770 and compare its EIP-7702 delegation pointer
with the valid T02 authorization's delegated address.
