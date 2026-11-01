# AXIOM — Gate 2 External TXID Crosscheck V1

Checked UTC: 2026-11-01T04:12:47.251299+00:00

## Method
- Compare exact Ethereum-format TXID strings.
- Extract only complete hashes from visible text and hyperlinks.
- No blockchain receipt or incident attribution verification.
- NEW means absent from the local register, not confirmed stolen funds.
- UNRESOLVED means no exact external TXID match found.
- A report may describe transactions without printing full TXIDs.

## Source snapshots
### Bitquery
- URL: https://bitquery.io/investigations/binance-hack
- HTTP: 200
- Retrieved HTML SHA256: `09bbfe9280ebd5a80ab484fdf4ceae8393708b3c723515bc9aa7d6ad399edfe8`
- Explicit full TXIDs: 10

### GCSA
- URL: https://media.gcsa.com/en-US/news-3730400
- HTTP: 200
- Retrieved HTML SHA256: `eb813da2f78145965a7cff506ad82d0d59c7542818c9a11e2beb26bf5ead097b`
- Explicit full TXIDs: 19

## Comparison
- Local unique TXIDs: 11
- MATCH: 2
- NEW: 24
- UNRESOLVED local TXIDs: 9

## Unresolved local TXIDs
- `0x2c45d7874dd60a5f1fa6e400933378efbc96b66abb988b8e3ed9bc010e6f260b`
- `0x2e1001627db976a77c5ce2feddef516f2c729b1de101c25d0d5af7699e5ffeb3`
- `0x51f263fa50966df6bbd7f8c6e6e99e3791c94444f7c4343b2fef1ee2d62fd39f`
- `0x9f21e145a0720fab80451c90f5590c9eeb7634022ab648da836bad4fa532ecf2`
- `0xa87c6a03fb9269975d32b3522784a4f286f98413bd78a1b404195674bef55653`
- `0xb1f99ca5c9472cf4bc3c1125f0aafca4a6392e6471e68c71630efaafd800f295`
- `0xcb5bb7c01c571998ddbbaedf4b89e1b7660babc4a6e9166940989193d72accfe`
- `0xd4e08d3ef0cb02a75922913c61984fbf7fe4bbc4b95324735ef27f908fd6c49c`
- `0xe07f61ff02643b25fa91075704febd2f075a50edfcd79de4f7232be58ddf2b52`

## Decision
- Gate 2 remains OPEN.
- No victim wallet is confirmed by string matching alone.
- Next: inspect source context and verify new transaction candidates.
