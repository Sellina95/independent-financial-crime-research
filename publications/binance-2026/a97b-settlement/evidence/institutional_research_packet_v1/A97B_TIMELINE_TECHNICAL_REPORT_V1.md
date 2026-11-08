# A97B — Ethereum Token Conversion and ETH Return Timeline

## Scope

Independent transaction-level reconstruction of A97B activity.
This is a gross-flow audit, not a determination of stolen-fund ownership.

## Verified observations

- Address: `0xa97bf7836f8a08f9ed91d41453d371493fae8d10`
- Integrated outbound event records: **1,186**.
- DEX/WETH-classified outbound events: **1,126**, across **1,124 distinct transactions**.
- Matched WETH unwrap and native ETH direct-return transactions: **1,015**.
- Gross ETH directly returned to A97B: **6829.199984950999210044 ETH**.
- Matched direct-return interval: **2026-10-30 01:22:11 UTC to 2026-10-30 06:20:23 UTC**.
- Recovered and event-matched receipts: **109/109 transactions**, separately classified.
- Previously audited exception events: **60** (audit present, not automatically conclusively attributed).
- Direct native ETH outflows: **4 transactions; 10647.2 ETH gross**.

## Observed ETH outflow timeline

### 2026-10-30 01:17:47 UTC — 3000.0 ETH
- Transaction: `0x04989db7e722b99d966b134e2152510c96e1b2855485a179002f8b7120dab14e`
- From: `0xa97bf7836f8a08f9ed91d41453d371493fae8d10`
- To: `0xc2096a12ebe0944f4d39e59979f485afd92d850a`
- Classification: direct native ETH outflow.
- Provenance and beneficial owner: not established.

### 2026-10-30 04:28:59 UTC — 0.1 ETH
- Transaction: `0xb472fe82656347e3f665bb3a1c429afffe3e9f5c0e540d80c8dd939efbf0cb95`
- From: `0xa97bf7836f8a08f9ed91d41453d371493fae8d10`
- To: `0xa3b3dee870f01560fdbe5af659c9c9135748886f`
- Classification: direct native ETH outflow.
- Provenance and beneficial owner: not established.

### 2026-10-30 06:34:59 UTC — 0.1 ETH
- Transaction: `0xc07ba7a343bf4059f157d1a9f5078e9439ebea94df3aa1c46743f6b7812816cc`
- From: `0xa97bf7836f8a08f9ed91d41453d371493fae8d10`
- To: `0x54401f80da97893a15d43566184635b6674bc942`
- Classification: direct native ETH outflow.
- Provenance and beneficial owner: not established.

### 2026-10-30 06:36:11 UTC — 7647.0 ETH
- Transaction: `0x16a76cdb8e480358041d9607407599828c42f7fbe20ecb59fb3216fdce91d7de`
- From: `0xa97bf7836f8a08f9ed91d41453d371493fae8d10`
- To: `0x54401f80da97893a15d43566184635b6674bc942`
- Classification: direct native ETH outflow.
- Provenance and beneficial owner: not established.

## DEX settlement mechanism

Within each of the 1,015 matched transactions, the existing audit
pairs WETH transfer and Withdrawal events with an equivalent direct
native ETH payment to A97B from the unwrap router.
This does not by itself establish the economic path of every token
sent by A97B or show that the ETH was entirely stolen.

## Public-report crosswalk

- Bitquery lists A97B as `Second receiver`.
- Bitquery describes an ETH move to a stash at 06:36 UTC on October 30.
- Our single minute-matching candidate: `0x16a76cdb8e480358041d9607407599828c42f7fbe20ecb59fb3216fdce91d7de`.
- Candidate amount: 7647.0 ETH.
- Candidate destination: `0x54401f80da97893a15d43566184635b6674bc942`.
- Exact transaction cross-identification by Bitquery: not verified.
- The eight scanned public HTML pages did not show our 1,015
  exact TX hashes or exact gross return total; this is not proof
  that the organizations lacked this information.

## Material audit limitations

- The 1,126 DEX-classified event rows are not 1,126 confirmed swaps.
- The 1,015 transactions are not the same unit as 1,017 matched event rows.
- The 109 recovered receipts prove event reconciliation only;
  matching ETH return for these transactions is not established.
- The returned ETH and direct ETH outflows must not be netted together
  without a time-specific balance and asset-inventory reconciliation.
- A97B may have mixed incident-related and unrelated inventory.
- This record cannot identify the controller or final beneficiary.
- Two methods using Blockscout are not fully independent providers.

## Evidence files

- `A97B_ETH_TRANSACTION_TIMELINE_V1.csv`
- `A97B_HOURLY_FLOW_SUMMARY_V1.csv`
- `HISTORICAL_CASE_MECHANISM_CROSSWALK_V1.csv`
