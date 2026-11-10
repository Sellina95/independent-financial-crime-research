# AXIOM — T03 Delegated Contract Caller Evidence V1

## Source provenance
- Network: Ethereum Mainnet
- Provider: Alchemy historical JSON-RPC
- Method: eth_getCode, eth_getTransactionByHash
- Historical state block: 26300769 (block-end)
- Delegated implementation: `0x63e842b054bd624a465454d533c33f573e9c6fae`
- T03 transaction: `0x53bd38b816c23e74134786c29a8c18d792777998a3b9326047b583100e88e2f3`
- Implementation bytecode: 1674 bytes
- Bytecode SHA256: `7235599d1e4088edcc48d2461f987475c3130897dea39c87ea1757603673bd56`

## OBSERVED
1. T03 is directed to `0x28c6c06298d514db089934071355e5743bf21d60`.
2. T03 sender is `0x7c8601d4645b93cea45f71e118a729332e6b5ca0`.
3. T03 calldata selector is `0x8a179be4`.
4. Implementation dispatcher at PC `0x0042` compares this selector and conditionally branches to PC `0x0087`.
5. Implementation bytecode at PC `0x00e2` contains the exact T03 sender address.
6. The code uses `CALLER`, `SUB`, and conditional `JUMPI` to PC `0x02e7`, consistent with a caller-equality check.

## INFERRED
- The selected function contains a caller-specific execution condition.
- T03 sender matches the hardcoded address.
- Combined with separately audited EIP-7702 historical delegation, this supports an execution-mechanism hypothesis.

## UNKNOWN
- Transaction-level instruction trace confirming this exact branch was taken.
- Full asset-transfer semantics of this function.
- Whether other contract paths permit other callers.
- Identity, control, or authorization of the signer.
- Whether the transaction was corporately authorized.

## Classification
TECHNICAL CORROBORATION / NEW_LEAD.
Not proof of perpetrator identity or unauthorized corporate approval.
