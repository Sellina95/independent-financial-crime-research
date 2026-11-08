# A97B — External Incident Attribution Evidence V1

Status: RESEARCH / NOT APPROVED FOR PUBLICATION
Research date: 2026-11-08
Address: 0xa97bf7836f8a08f9ed91d41453d371493fae8d10

## 1. Research Question

How strongly can the observed Binance 14 → A97B
ETH inflows be linked to the reported incident?

This audit separates:

- Official incident statements
- Independent external analysis
- Preserved on-chain observations
- Address-level external attribution
- Unresolved individual fund provenance

## 2. Binance Official Statement

Source:
https://www.binance.com/en-NG/blog/community/3229153443759566763

Source type: Primary corporate incident statement
Reported publication date: 2026-11-03

Relevant reported facts:

- Binance Hot Wallet 14 was compromised through
  unauthorized EIP-7702 delegation.
- Binance reported a final unauthorized ETH outflow
  of approximately 2,961.9 ETH.
- The final outflow was reported around
  2026-10-29 23:56 UTC.
- Binance reported revocation of the malicious
  delegation at 2026-10-30 00:10 UTC.

Assessment:

OFFICIALLY REPORTED INCIDENT CONTEXT.

This is a corporate account of the incident.
An exact transaction-hash match to the official
article is not established in this record.

## 3. ChainWard Independent Analysis

Source:
https://chainward.ai/decodes/binance-7702-delegation

Source type: Independent blockchain incident analysis
Reported publication date: 2026-10-30

Relevant reported movements:

Movement 1:
- Block: 26301444
- Time: 2026-10-29 22:39:35 UTC
- Approximate amount: 128.4911 ETH

Movement 2:
- Block: 26301828
- Time: 2026-10-29 23:56:47 UTC
- Approximate amount: 2961.910821 ETH

Preserved local A97B observations:

Movement 1:
- TX: 0x4a4aed833556814c16fe176fc8abc70ce124eadc73da3bcdf42a67ef44f9ad6b
- Exact decoded Alchemy value:
  128.491139212075057017 ETH

Movement 2:
- TX: 0x4395d51dc3f3c51230329efc3548f74edbced353ff3f795c517cc57fa650f89b
- Exact decoded Alchemy value:
  2961.910820938285094748 ETH

Combined observed amount:
3090.401960150360151765 ETH

Assessment:

STRONGLY CORROBORATED INCIDENT ASSOCIATION.

The reported block numbers, timestamps and
approximate amounts correspond to the preserved
A97B movements.

Independent exact-TX-hash confirmation in the
cited external publication remains unverified.

## 4. FBI Address Attribution

Source:
https://www.fbi.gov/investigate/cyber/alerts/2026/north-korea-responsible-for-6-billion-binance-attack

Source type: Law-enforcement public address listing
Reported publication date: 2026-10-31

Relevant listed address:

0x54401f80da97893a15d43566184635b6674bc942

Preserved A97B transaction evidence:

- 0.1 ETH directly transferred to this address.
- 7647 ETH directly transferred to this address.

Assessment:

EXTERNAL ADDRESS-LEVEL INCIDENT ATTRIBUTION.

Address inclusion does not independently establish
the exact incident-origin fraction of its balance.

## 5. Elliptic Address Attribution

Previously preserved source snapshot:

research/case-binance-2026/evidence/binance14_all_receivers_census_v1/step83_official_attribution_crosswalk_v1/source_snapshots/elliptic_source.txt

Previously preserved crosswalk:

research/case-binance-2026/evidence/binance14_all_receivers_census_v1/step83_official_attribution_crosswalk_v1/address_attribution_crosswalk.csv

Relevant observations:

- A97B is present in the Elliptic incident list.
- Multiple A97B direct recipients are also listed.
- The 7647 ETH recipient appears in both
  preserved FBI and Elliptic lists.

First-added address listing timestamps:
UNKNOWN.

Assessment:

PRESERVED EXTERNAL ADDRESS ASSOCIATION.

## 6. Attribution Decision Matrix

CONFIRMED WITHIN PRESERVED EVIDENCE:

- Two Binance 14 → A97B ETH movement records exist.
- Their Alchemy raw-value decoding totals
  3090.401960150360151765 ETH.
- A97B directly sent 10647.2 ETH
  across four transactions to three recipients.
- Preserved Elliptic/FBI lists match relevant
  addresses as documented in STEP 83.

OFFICIALLY REPORTED:

- Unauthorized Binance 14 sweep activity.
- A final approximately 2961.9 ETH unauthorized
  movement around 23:56 UTC.

STRONGLY CORROBORATED:

- The two observed Binance 14 → A97B inflows
  correspond in time, block and approximate
  amount to externally reported sweep activity.

UNKNOWN / NOT ESTABLISHED:

- Exact-TX-hash identity in the cited public reports.
- Complete economic attribution of the 10647.2 ETH outflows.
- Beneficial ownership of A97B or downstream recipients.
- A97B-specific issuer blacklist or freeze.
- Post-freeze flows without a verified freeze boundary.
- Complete balance-based fund conservation.

## 7. Publication Boundaries

Acceptable:

An independently reconstructed A97B route with
strong external incident corroboration.

Not acceptable:

- Claiming all 10647.2 ETH were stolen funds.
- Claiming FBI directly listed A97B.
- Claiming address listing equals freezing.
- Claiming all ERC20 event logs are economic transfers.
- Claiming post-freeze activity without temporal evidence.

## 8. Source Preservation

This document records external source URLs
and the researcher's evidence assessment.

It does not contain downloaded copies of the
external webpages or their SHA256 fingerprints.

The existing STEP 65–85 raw evidence is
preserved in its original location.

Publication approval: REQUIRED.
