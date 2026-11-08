# Historical Mechanism Comparison — A97B

## Research question

Which documented mechanisms of historical exploit-related
token-to-ETH conversion resemble observed A97B transactions?

## Evidence standard

Mechanism resemblance is not common actor, control, illicit origin,
criminal intent or transaction-level equality.

| Case | Documented mechanism | Comparison | Boundary |
|---|---|---|---|
| Harmony Horizon Bridge (2022) | Stolen Ethereum-chain tokens exchanged via Uniswap into ETH, followed by Tornado Cash deposits | DEX token-to-ETH conversion | Mixer route documented; not established for A97B |
| FTX Unauthorized Transfers (2022) | Majority of stolen tokens converted into ETH using DEXs | Multi-token conversion to ETH | No published 1015-TX A97B settlement crosswalk in this historical case |
| WazirX Breach (2024) | Multiple stolen assets exchanged for ETH through decentralized services | Token-to-ETH conversion | Identical unwrap and return-to-sender behavior not established |
| Binance A97B Public Crosswalk (2026) | Bitquery identifies A97B as second receiver and documents ETH movement around 06:36 UTC on Oct 30 | Address and minute-level outflow match with our reconstruction | Bitquery exact transaction hash and full settlement-level overlap unverified |

## Primary publicly available research references

- Harmony Horizon Bridge: https://www.elliptic.co/insights/the-top-crypto-hacks-of-2022/
- FTX Unauthorized Transfers: https://www.elliptic.co/insights/477-million-in-unauthorized-transfers-from-ftx/
- WazirX Breach: https://www.elliptic.co/insights/235-million-lost-by-wazirx-in-north-korea-linked-breach/
- Binance A97B Public Crosswalk: https://www.bitquery.io/investigations/binance-hack

## Unanswered institutional questions

1. Is the detailed unwrap-return pattern unusual relative to normal router execution?
2. Does the pattern persist in a matched normal-DEX control sample?
3. Can every token input be linked to verified event-time incident funds?
4. Are settlement signatures or router paths repeated across historical cases?
5. Does any institution disclose this same 1,015-transaction reconstruction?

All historical transaction-level comparisons: NOT TESTED.
