# AXIOM — Gate 2 ERC-20 Transfer Evidence Audit V1

## Scope
- Ethereum mainnet, six previously validated transactions.
- Exact receipt log extraction; no inference of victim ownership.
- Only standard three-topic Transfer-shaped logs decoded.
- Token contracts and decimals not independently checked.
- Internal ETH movements and nonstandard token events excluded.
- Receipt hashes cover RPC JSON representations, not authenticated provenance.

## Results
- Transactions inspected: 6
- Total receipt logs: 67
- Transfer-shaped logs: 66
- Distinct token source addresses: 3
- Distinct token destination addresses: 3

## Token source addresses
- `0x28c6c06298d514db089934071355e5743bf21d60`: 63 events
- `0xee7ae85f2fe2239e27d9c1e23fffe168d63b4055`: 2 events
- `0x5227f603c1ee34ce3c06efe6477003bdfccb2f8c`: 1 events

## Receipt response hashes
- `0x53bd38b816c23e74134786c29a8c18d792777998a3b9326047b583100e88e2f3`: `4d0943f240a942e5af22b89e86992a2b46203c82ed175abde1e151529ff458f6`
- `0xdc102dd89dded5a83f1008906883ffb7c81ff3b7d7965d8c7277d170b5e17481`: `9a35647221183da6eb373b3801b75bc021304caed63be4a8d44f508a952208dd`
- `0xad99264d5532ae0dd04b2004eebda05f25657e70dacb764f7ac8d4ccd051298b`: `5535a43bc5f07f790367ef5e87df5da659a19a2c2fa9aacae9357b532b8432fd`
- `0x68d7d69deaeb9750c38020b4f8d3728146ca8d2267eba1e38cf9b56722ad659a`: `faabca7960e10495e1801fdcbb624ff5e74d72efff69a839eddea8f8b08b52b9`
- `0xafbf94c92a8d749988411669fa14d4f8866d9b4420b4ebd299f28e958dac7209`: `675dc55fcb525f67442c6ac35c2ea0201190d1f4e7691f6929668405f2e01c15`
- `0xca63641eaeb49779d80ba11ce4fe894d635f2e98c032e9efd5bb4ce304ae56da`: `6abf9665774471ff0c5172c33777d1fd00b42866d73b26cf64eabf760ac9c70f`

## Evidence limitations
- A token Transfer event shows recorded token movement, not unauthorized intent.
- Zero-address mint/burn events require separate interpretation.
- EIP-7702 delegation and contract calls require independent analysis.
- Binance wallet ownership remains unverified.
- The three original wallet candidates remain unconfirmed.
- No asset conservation or loss total established by this extraction.

## Gate decision
- Gate 2: OPEN.
- Next: verify token contracts and distinguish original source wallets
  from intermediaries, receivers, and transaction callers.
