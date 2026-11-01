# AXIOM — Gate 2 Initial Attribution Audit V1

Audit date (UTC): 2026-11-01T04:09:32.680914+00:00

## Research question
Can existing source-wallet candidates be independently linked to the Binance incident and its initial unauthorized withdrawals?

## Scope and method
- Read-only review of existing local CSV registers.
- No live blockchain queries performed.
- No wallet ownership inferred from transaction proximity.
- No changes to existing 700M USDT tracing evidence.

## Input inventory
- Entry-point records: 11
- Source-wallet records: 3
- Unique Ethereum-format addresses in entry register: 23
- Unique Ethereum-format addresses in wallet register: 3
- Unique transaction hashes in entry register: 11

### Entry-point CSV columns
- `chain`
- `source_address`
- `destination_address`
- `transaction_hash`
- `block`
- `observed_assets`
- `verification_status`
- `evidence`

### Source-wallet CSV columns
- `chain`
- `source_address`
- `observed_transaction_count`
- `ownership_status`

## Candidate transaction inventory
- `0x2c45d7874dd60a5f1fa6e400933378efbc96b66abb988b8e3ed9bc010e6f260b`
- `0x2e1001627db976a77c5ce2feddef516f2c729b1de101c25d0d5af7699e5ffeb3`
- `0x51f263fa50966df6bbd7f8c6e6e99e3791c94444f7c4343b2fef1ee2d62fd39f`
- `0x53bd38b816c23e74134786c29a8c18d792777998a3b9326047b583100e88e2f3`
- `0x9f21e145a0720fab80451c90f5590c9eeb7634022ab648da836bad4fa532ecf2`
- `0xa87c6a03fb9269975d32b3522784a4f286f98413bd78a1b404195674bef55653`
- `0xb1f99ca5c9472cf4bc3c1125f0aafca4a6392e6471e68c71630efaafd800f295`
- `0xcb5bb7c01c571998ddbbaedf4b89e1b7660babc4a6e9166940989193d72accfe`
- `0xd4e08d3ef0cb02a75922913c61984fbf7fe4bbc4b95324735ef27f908fd6c49c`
- `0xdc102dd89dded5a83f1008906883ffb7c81ff3b7d7965d8c7277d170b5e17481`
- `0xe07f61ff02643b25fa91075704febd2f075a50edfcd79de4f7232be58ddf2b52`

## Evidence assessment
- OBSERVED: Existing research registers contain candidate addresses and transaction references.
- NOT REVERIFIED: Transaction existence, amounts, timestamps, and receipts were not independently checked in this audit.
- UNKNOWN: Whether candidate source addresses belong to Binance.
- UNKNOWN: Whether candidate transactions were unauthorized.
- UNKNOWN: Whether the audited 700M USDT path originated from the reported incident.

## Attribution requirements
- Obtain an independently attributable incident wallet or transaction reference from a reliable source.
- Verify chain, transaction hash, block timestamp, sender, recipient, token contract, and amount.
- Compare the transaction against the official incident timeline.
- Separate confirmed on-chain movement from incident attribution.

## Gate 2 decision
- Status: OPEN — INCIDENT ATTRIBUTION NOT ESTABLISHED.
- Existing candidates remain research leads only.
- Do not promote candidate wallets to confirmed victim wallets.
- Do not label the 700M USDT path as confirmed stolen funds.
