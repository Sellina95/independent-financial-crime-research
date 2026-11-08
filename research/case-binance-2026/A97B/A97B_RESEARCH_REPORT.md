# A97B — Transaction-Level Reconstruction of DEX Settlement and ETH Movements

**Independent Financial Crime Research | Research version 1.0**

**Status:** Evidence-backed reconstruction; incident-fund provenance and beneficial ownership remain unresolved.

> This report distinguishes observed on-chain transactions, external reporting, and unresolved attribution. It does not identify an attacker or establish that all observed ETH originated from the incident.

## Executive summary

Ethereum address `0xa97bf7836f8a08f9ed91d41453d371493fae8d10` is discussed in public reporting concerning the October 2026 Binance incident.

Our preserved research reconstructs **1,186 outbound transfer-event records**, including **1,126 DEX/WETH-classified event records** across **1,124 distinct transactions**.

Within **1,015 distinct transactions**, WETH withdrawal activity and matching direct native ETH payments to A97B were reconciled. Gross direct ETH receipts total **6829.199984950999210044 ETH**.

Separately, **109 transaction receipts** were recovered and their relevant transfer events matched. These 109 transactions are not included in the 1,015 confirmed ETH-return transactions.

Four direct native ETH outflows from A97B total **10647.2 ETH**, including a **7,647 ETH** transfer at **2026-10-30 06:36:11 UTC**.

**The gross DEX receipts and direct outflows must not be treated as a conserved, incident-attributed fund balance without an event-time asset inventory.**

---

## 1. Incident context and event chronology

Earlier research identified two direct native ETH transfers from Binance14 to A97B:

| Time (UTC) | ETH | Transaction |
|---|---:|---|
| 2026-10-29 22:39:35 UTC | 128.491139212075057017 | [`0x4a4aed8335…`](https://etherscan.io/tx/0x4a4aed833556814c16fe176fc8abc70ce124eadc73da3bcdf42a67ef44f9ad6b) |
| 2026-10-29 23:56:47 UTC | 2961.910820938285094748 | [`0x4395d51dc3…`](https://etherscan.io/tx/0x4395d51dc3f3c51230329efc3548f74edbced353ff3f795c517cc57fa650f89b) |

Combined direct native ETH inflows in these two transactions: **3090.401960150360151765 ETH**.

These observations establish the documented direct-transfer path, not the provenance of every token or ETH amount subsequently handled by A97B.

### Key timestamps

- **2026-10-29 22:39:35 UTC:** 128.491139212075057017 ETH direct inflow from Binance14.
- **2026-10-29 23:56:47 UTC:** 2961.910820938285094748 ETH direct inflow from Binance14.
- **2026-10-30 01:17:47 UTC:** first listed direct native ETH outflow of 3000.0 ETH.
- **2026-10-30 01:22:11 UTC–2026-10-30 06:20:23 UTC:** window of the 1,015 matched DEX-related ETH direct-return transactions.
- **2026-10-30 06:36:11 UTC:** 7,647 ETH direct transfer to [`0x54401f80da…4bc942`](https://etherscan.io/address/0x54401f80da97893a15d43566184635b6674bc942).

These entries are chronological observations, not a complete balance-conservation ledger.

## 2. DEX execution structure

The audited population contains:

- **1,126 DEX/WETH-classified outbound event records** across **1,124 distinct transaction hashes**.
- **1,015 distinct transactions** with reconciled WETH withdrawal and native ETH direct-return observations.
- **109 distinct transactions** whose previously missing receipts were recovered and matched to corresponding transfer events.
- **60 additional outbound event records** carrying previous exception-audit classifications.

Classification as DEX/WETH-related does not independently prove that every event is a completed economic swap.

### Transaction-level sequence established for 1,015 transactions

```text
A97B-related ERC-20 transfer activity
           |
           v
DEX / intermediary token and WETH movement
           |
           v
WETH transfer into an unwrap router
           |
           v
WETH Withdrawal event
           |
           v
Native ETH payment directly back to A97B
```

Individual smart-contract execution may contain additional intermediate steps. The diagram summarizes audited legs and is not a complete call trace.

## 3. WETH unwrap and native ETH direct returns

**Matched transactions:** 1,015
**Gross direct return:** 6829.199984950999210044 ETH
**First matched return:** 2026-10-30 01:22:11 UTC
**Last matched return:** 2026-10-30 06:20:23 UTC

The ETH amount received by A97B was reconciled against the corresponding WETH withdrawal amount at transaction level.

Original address-centric Blockscout records were preserved, and the research also compared overlapping records against earlier transaction-centric Blockscout retrievals. These are consistency checks within the same provider, not independent-provider corroboration.

### Representative transactions

| Time (UTC) | Direct ETH return | Transaction |
|---|---:|---|
| 2026-10-30 01:22:11 UTC | 1.986430199284161679 | [`0xd0bf6957d5…`](https://etherscan.io/tx/0xd0bf6957d547142e3701929dde1e6816a4b035c7d6aba01a5e9ec0f912bea856) |
| 2026-10-30 03:49:47 UTC | 100.648880344946284816 | [`0x8c3f2b7b49…`](https://etherscan.io/tx/0x8c3f2b7b490c9187adeb9a6bed1ac3972599a54d901431030396015717b74003) |
| 2026-10-30 06:20:23 UTC | 17.572749103025391488 | [`0x5aaabda6db…`](https://etherscan.io/tx/0x5aaabda6db62c5c2af7ccf42954e0df338004459db7d5cbdbafb77d27ce3b968) |

### Hourly settlement activity

| UTC hour | Activity | Transactions | Gross ETH |
|---|---|---:|---:|
| 2026-10-30 01:00 UTC | DEX_WETH_ETH_DIRECT_RETURN | 117 | 1266.327747581200891148 |
| 2026-10-30 01:00 UTC | DIRECT_NATIVE_ETH_OUTFLOW | 1 | 3000.0 |
| 2026-10-30 02:00 UTC | DEX_WETH_ETH_DIRECT_RETURN | 274 | 1207.366367706810386794 |
| 2026-10-30 03:00 UTC | DEX_WETH_ETH_DIRECT_RETURN | 160 | 1220.233276988872719574 |
| 2026-10-30 04:00 UTC | DEX_WETH_ETH_DIRECT_RETURN | 149 | 759.734608979193234972 |
| 2026-10-30 04:00 UTC | DIRECT_NATIVE_ETH_OUTFLOW | 1 | 0.1 |
| 2026-10-30 05:00 UTC | DEX_WETH_ETH_DIRECT_RETURN | 221 | 1399.678660589728572059 |
| 2026-10-30 06:00 UTC | DEX_WETH_ETH_DIRECT_RETURN | 94 | 975.859323105193405497 |
| 2026-10-30 06:00 UTC | DIRECT_NATIVE_ETH_OUTFLOW | 2 | 7647.1 |

**Interpretation boundary:** 6,829.199984950999210044 ETH is gross observed direct receipt, not proven stolen value, realized profit, or recovered assets.

## 4. Subsequent native ETH outflows

| Time (UTC) | ETH sent | Destination | Transaction |
|---|---:|---|---|
| 2026-10-30 01:17:47 UTC | 3000.0 | [`0xc2096a12eb…2d850a`](https://etherscan.io/address/0xc2096a12ebe0944f4d39e59979f485afd92d850a) | [`0x04989db7e7…`](https://etherscan.io/tx/0x04989db7e722b99d966b134e2152510c96e1b2855485a179002f8b7120dab14e) |
| 2026-10-30 04:28:59 UTC | 0.1 | [`0xa3b3dee870…48886f`](https://etherscan.io/address/0xa3b3dee870f01560fdbe5af659c9c9135748886f) | [`0xb472fe8265…`](https://etherscan.io/tx/0xb472fe82656347e3f665bb3a1c429afffe3e9f5c0e540d80c8dd939efbf0cb95) |
| 2026-10-30 06:34:59 UTC | 0.1 | [`0x54401f80da…4bc942`](https://etherscan.io/address/0x54401f80da97893a15d43566184635b6674bc942) | [`0xc07ba7a343…`](https://etherscan.io/tx/0xc07ba7a343bf4059f157d1a9f5078e9439ebea94df3aa1c46743f6b7812816cc) |
| 2026-10-30 06:36:11 UTC | 7647.0 | [`0x54401f80da…4bc942`](https://etherscan.io/address/0x54401f80da97893a15d43566184635b6674bc942) | [`0x16a76cdb8e…`](https://etherscan.io/tx/0x16a76cdb8e480358041d9607407599828c42f7fbe20ecb59fb3216fdce91d7de) |

**Gross direct native ETH outflows:** 10647.2 ETH across four transactions.

At 06:34:59 UTC, a 0.1 ETH transaction went to the same destination later receiving 7,647 ETH at 06:36:11 UTC: `0x54401f80da97893a15d43566184635b6674bc942`.

This temporal sequence is observed; describing the smaller transaction as a test payment would be a hypothesis, not a verified fact.

Because A97B could contain mixed inventory, the 7,647 ETH outflow cannot automatically be assigned to the preceding 6,829 ETH DEX returns.

## 5. Crosswalk against institutional public reporting

Bitquery's public investigation identifies A97B as a second receiver and describes an ETH movement to a stash at approximately 06:36 UTC on October 30.

The uniquely minute-matching candidate in our direct-outflow register is [`0x16a76cdb8e…`](https://etherscan.io/tx/0x16a76cdb8e480358041d9607407599828c42f7fbe20ecb59fb3216fdce91d7de), at 06:36:11 UTC, for 7,647 ETH.

**Matching publication time is not proof that Bitquery disclosed or independently verified this exact transaction hash.**

The prior automated public-page screen covered eight HTML pages across Binance, Chainalysis, Elliptic and Bitquery. It found no exact match to the 1,015 return transaction hashes or the precise 6,829.199984950999210044 ETH amount in those retrieved pages.

One Bitquery HTML page contained the A97B address. This limits novelty claims: the address and broad flow were already publicly discussed.

The screen did not exhaust charts, downloadable records, client-only intelligence, unpublished investigations, or all available publications.

### Public report references

- [Bitquery — Binance investigation](https://www.bitquery.io/investigations/binance-hack)
- [Elliptic — public research](https://www.elliptic.co/insights/)
- [Chainalysis — public blog](https://www.chainalysis.com/blog/)
- [Binance — official website](https://www.binance.com/)

## 6. Comparison with historical incidents

These are **qualitative, literature-based comparisons**, not independently reconstructed historical transaction graphs or statistical behavioral matches.

| Historical case | Reported mechanism | Relevant similarity | Key limitation |
|---|---|---|---|
| Harmony Horizon Bridge (2022) | Stolen Ethereum-chain tokens exchanged via Uniswap into ETH, followed by Tornado Cash deposits | DEX token-to-ETH conversion | Mixer route documented; not established for A97B |
| FTX Unauthorized Transfers (2022) | Majority of stolen tokens converted into ETH using DEXs | Multi-token conversion to ETH | No published 1015-TX A97B settlement crosswalk in this historical case |
| WazirX Breach (2024) | Multiple stolen assets exchanged for ETH through decentralized services | Token-to-ETH conversion | Identical unwrap and return-to-sender behavior not established |
| Binance A97B Public Crosswalk (2026) | Bitquery identifies A97B as second receiver and documents ETH movement around 06:36 UTC on Oct 30 | Address and minute-level outflow match with our reconstruction | Bitquery exact transaction hash and full settlement-level overlap unverified |

Historical research sources carried forward for verification:

- **Harmony Horizon Bridge:** https://www.elliptic.co/insights/the-top-crypto-hacks-of-2022/
- **FTX Unauthorized Transfers:** https://www.elliptic.co/insights/477-million-in-unauthorized-transfers-from-ftx/
- **WazirX Breach:** https://www.elliptic.co/insights/235-million-lost-by-wazirx-in-north-korea-linked-breach/
- **Binance A97B Public Crosswalk:** https://www.bitquery.io/investigations/binance-hack

**No common-actor inference is supported.** Token-to-ETH conversion and routing through public DEX infrastructure are not by themselves unique indicators of illicit behavior.

## 7. Limitations and unresolved questions

1. **Incident attribution:** The source of every ERC-20 token position and every ETH receipt has not been independently attributed to the Binance incident.
2. **Mixed balances:** No complete time-specific inventory conservation analysis is established here.
3. **Counting units:** 1,186 and 1,126 refer to event records; 1,124, 1,015 and 109 refer to distinct transactions.
4. **Recovered receipts:** The 109 recovered receipts support transfer-event matching, not confirmed ETH direct-return amounts.
5. **External publication overlap:** Public HTML screening is not a complete institutional intelligence comparison.
6. **Identity:** Blockchain address interaction does not prove shared ownership, actor identity or criminal intent.
7. **Historical analogies:** Historical cases were not transaction-by-transaction reproduced in this research packet.
8. **Provider independence:** Two Blockscout retrieval routes do not constitute independent provider corroboration.
9. **Withdrawals:** Downstream custody, beneficiary, and subsequent disposition require separate verification.

## 8. Reproducibility and evidence index

### Transaction ledgers

- [Combined ETH-return and direct-outflow transaction timeline](institutional_research_packet_v1/A97B_ETH_TRANSACTION_TIMELINE_V1.csv)
- [Hourly ETH-flow summary](institutional_research_packet_v1/A97B_HOURLY_FLOW_SUMMARY_V1.csv)
- [1,015 transaction ETH-return ledger](eth_address_receipts_v1/A97B_ADDRESS_ETH_RETURN_V1.csv)
- [Four direct native ETH outflows](bitquery_withdrawal_crosswalk_v1/A97B_DIRECT_ETH_WITHDRAWAL_CROSSWALK_V1.csv)

### Audit evidence

- [1,186-record integrated event ledger](integrated_event_audit_v1/A97B_INTEGRATED_EVENT_LEDGER_V1.csv)
- [109 recovered receipt verification register](integrated_event_audit_v1/RECOVERED_109_RECEIPT_AUDIT_V1.csv)
- [WETH first-recipient audit ledger](eth_first_recipient_audit_v1/ETH_FIRST_RECIPIENT_LEDGER_V1.csv)
- [STEP 86 reconciliation metadata](integrated_event_audit_v1/AUDIT_V1.json)
- [Research packet SHA-256 manifest](institutional_research_packet_v1/SHA256_MANIFEST_V1.json)

### Historical and public-source crosswalk

- [Historical literature comparison ledger](institutional_research_packet_v1/HISTORICAL_CASE_MECHANISM_CROSSWALK_V1.csv)
- [Eight-page public HTML overlap register](public_report_overlap_v1/PUBLIC_REPORT_SOURCE_CROSSWALK_V1.csv)

### Selected source-file checksums

| Source | SHA-256 |
|---|---|
| `A97B_ADDRESS_ETH_RETURN_V1.csv` | `4f2c27670a1e155506f70f3f850151340293a890c626b5f4baaeb38845fe4eef` |
| `A97B_INTEGRATED_EVENT_LEDGER_V1.csv` | `eaf5350c5cdb37ba18708fec7c55f46d0f769b916187e16b57cc9a7660c9d2fc` |
| `RECOVERED_109_RECEIPT_AUDIT_V1.csv` | `c46fcf1596c1f187799932d1c0bc80a4fd46dbb5150f69d0fe089fe4231df558` |
| `A97B_DIRECT_ETH_WITHDRAWAL_CROSSWALK_V1.csv` | `277c588a0a39e8db58c415770cbf17fba57a7f05d1afabd1dac7d2e921a797f9` |

## 9. Research conclusion

Within the specific A97B dataset, the transaction-level evidence supports a consistent direct ETH return following WETH withdrawal in 1,015 transactions, totaling 6,829.199984950999210044 ETH gross.

Four separate direct native ETH outflows were identified, including the 7,647 ETH payment at 06:36:11 UTC on October 30. This timestamp aligns with Bitquery's published minute-level description, subject to exact transaction cross-identification.

The incremental public contribution is a reproducible, fine-grained settlement audit for a previously identified address—not discovery of a new attacker or definitive tracing of stolen-fund ownership.

**Publication gate:** Research branch only. External release and incident-fund attribution require explicit review.
