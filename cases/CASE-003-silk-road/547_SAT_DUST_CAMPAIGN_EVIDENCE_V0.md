# CASE-003 — 547-Sat Dust Campaign
## Evidence Record V0 | 2026-10-27

Status: OPEN INVESTIGATION
Scope: Bitcoin on-chain transaction reconstruction
Evidence standard: OBSERVED / INFERRED / UNKNOWN

This document records a 547-satoshi message campaign
encountered during CASE-003 Silk Road research.

The campaign's relationship to the Silk Road theft,
James Zhong, or any criminal actor is NOT established.

This is an investigative lead, not a criminal allegation.

---

## 1. Initial Discovery — 10,000 BTC Split

Date: 2020-11-24

TXID:
481aa062147384e1511925f7b5bc1c22bdd0f6fdf1664ff2db134ef9b2263516

Source:
https://mempool.space/tx/481aa062147384e1511925f7b5bc1c22bdd0f6fdf1664ff2db134ef9b2263516

OBSERVED:
- A roughly 10,000 BTC input was spent.
- The transaction generated ten outputs of
  approximately 1,000 BTC each.
- Additional small inputs were present.

Ten receiving addresses:

1. bc1qfj4trvfnute2kkdfxssymq2p6ztj63r68j5d3t
2. bc1qam27vpg8ve5sd6m7xpz93eexwwm0c4yly9c7u3
3. bc1q9hv8dx3f5flg3gqc0uprel097yevkvklwzvcvt
4. bc1q95h6vkehyvnss820w85uz60pnv6qyfuhvtckw8
5. bc1qkq4clu886qkgq5rtegesa7jt2lrp7yyujvl96t
6. bc1qh8srqerlu8m05za0949605fvfttknc9qrp23l4
7. bc1qwtdggnya06g68vnkyjf7l0lzt7nqz609cq7vt2
8. bc1qq7rnxtywgqjs0x57gv38y5al0tcanqg0nrj7zx
9. bc1qc6he83h5v0n6znh95detfnv093jftw3vquzgk8
10. bc1qnd8zru8xjukvnylv6aj7vjy7ltpzuept93eff2

---

## 2. Message Distribution Transaction

Date: 2020-11-25 16:41:54

TXID:
3995be87d959d28c8d845806ccf2bd27c61cc72bf18aa46f7bf37a2a07c092cd

Source:
https://mempool.space/tx/3995be87d959d28c8d845806ccf2bd27c61cc72bf18aa46f7bf37a2a07c092cd

OBSERVED:
- One input of 0.00529162 BTC.
- Input address:
  bc1qqzsr4czpu42lz7ma5ahhzae0rnny9w7yyzdhay
- Hundreds of outputs, many exactly 547 sats.
- Transaction fee: 81,117 sats.
- Seven consecutive specially constructed addresses
  encode a readable message.

Message:

"Lets use full power of anonymity.
 See memo dot sv topic hmwyda."

Encoded address sequence:

1Lets1xxxx1use1xxxxxxxxxxxy2EaMkJ
1fuLL1xxxx1power1xxxxxxxxxxzatvCK
1of1xxxxx1anonymity1xxxxxxxz9JzFN
1See1xxxx1memo1xxxxxxxxxxxxxBuhPF
1dot1xxxxx1sv1xxxxxxxxxxxxxwYqEEt
1topic1xxx1hmwyda1xxxxxxxxxvo8wMn
1xxxxxxxxxxxxxxxxxxxxxxxxxy1kmdGr

IMPORTANT:
The message is encoded in transaction output
addresses. It is not an individual message
attached separately to every recipient.

---

## 3. Recipient Overlap

Comparison:
2020-11-24 split transaction
vs.
2020-11-25 message transaction

OBSERVED FROM PROVIDED TRANSACTION RECORDS:

Six of the ten 1,000 BTC receiving addresses
also appear as 547-sat recipients.

Matched:

bc1qam27vpg8ve5sd6m7xpz93eexwwm0c4yly9c7u3
bc1q95h6vkehyvnss820w85uz60pnv6qyfuhvtckw8
bc1qkq4clu886qkgq5rtegesa7jt2lrp7yyujvl96t
bc1qwtdggnya06g68vnkyjf7l0lzt7nqz609cq7vt2
bc1qq7rnxtywgqjs0x57gv38y5al0tcanqg0nrj7zx
bc1qnd8zru8xjukvnylv6aj7vjy7ltpzuept93eff2

Observed overlap: 6 / 10.

UNKNOWN:
- Why these six addresses were selected.
- Whether the remaining four received dust
  in other transactions.
- Whether selection depended on transaction
  recency, value, address activity, or other factors.

This overlap alone does not prove targeting
based on criminal association.

---

## 4. Spent vs Unspent Outputs

OBSERVED FROM USER EXPLORER INSPECTION:

- Some ordinary 547-sat outputs were spent.
- Some ordinary 547-sat outputs remained unspent.
- The seven message-encoding outputs appeared unspent.

Interpretation:

The message-encoding outputs may function as
publicly visible text carriers.

Ordinary dust recipients may later spend their
547-sat outputs.

Neither observation establishes malicious intent.

---

## 5. Large Consolidation Transaction

Date: 2022-04-23 06:18:11

TXID:
64a87c3d7540876516d0bf274fcc4773c0d59d07e960287b1d1ddbf690335b08

Source:
https://mempool.space/tx/64a87c3d7540876516d0bf274fcc4773c0d59d07e960287b1d1ddbf690335b08

OBSERVED FROM PROVIDED EXPLORER RECORD:

- Numerous inputs worth exactly 547 sats.
- Multiple large BTC inputs.
- One output of 1,500.72603880 BTC.
- Transaction fee: 105,502 sats.
- The transaction is a consolidation.

A 547-sat input appears from:

bc1q95h6vkehyvnss820w85uz60pnv6qyfuhvtckw8

This address also appeared in the
2020-11-24 split and 2020-11-25 message transactions.

CRITICAL VERIFICATION BOUNDARY:

The 2022 input has not yet been matched to
the precise 2020 message output using
previous TXID + vout.

Therefore, the exact UTXO lineage remains PENDING.

---

## 6. Dusting and Address Clustering

OBSERVED:
- Many small UTXOs were consumed together
  with large BTC UTXOs.
- A single consolidated output was created.

INFERRED:
- Common-input analysis could expose
  additional address relationships.
- The transaction is consistent with ordinary
  wallet consolidation.
- It is also consistent with an outcome that
  a dust-based tracking actor could observe.

UNKNOWN:
- Whether the original sender monitored
  later recipient spending.
- Whether the sender intended to deanonymize
  recipients.
- Whether the sender and consolidation operator
  were related.
- Whether all input addresses had common ownership.

Common-input heuristics are not proof of
common ownership.

Sending dust does not grant control over
the recipient's UTXO.

---

## 7. Competing Hypotheses

H1 — Advertising / message distribution

The sender distributed a public message
to many Bitcoin addresses.

H2 — Automated address collection

The sender selected recently active addresses
from public blockchain data.

H3 — High-value targeting

The sender preferentially selected addresses
associated with large Bitcoin transactions.

H4 — Dust-based observation

The sender may have monitored whether
recipients later consolidated dust UTXOs
with other funds.

H5 — Shared operational control

The message campaign and later consolidation
may have involved related operators.

H5 has no direct supporting evidence at present.

These hypotheses are not mutually exclusive.

---

## 8. Sender-Side Evidence

2020-11-25 transaction input:

bc1qqzsr4czpu42lz7ma5ahhzae0rnny9w7yyzdhay

Amount:
0.00529162 BTC

OBSERVED:
The message distribution transaction was
funded and broadcast by an actor or actors.

UNKNOWN:
- Identity of the transaction creator.
- Funding source beyond the observed input.
- Whether the same actor operated other
  547-sat message transactions.
- Whether subsequent recipient activity
  was monitored.

The funding address is not automatically
the sender's complete wallet or identity.

---

## 9. Research Boundaries

This evidence record does NOT establish:

- A link between the dust sender and James Zhong.
- A link between the dust sender and Mt. Gox theft.
- Criminal intent by any recipient.
- Malicious intent by the message sender.
- Actual deanonymization by the sender.
- Common ownership of all consolidated inputs.
- Exact lineage between the 2020 and 2022 dust UTXOs.

Historical community reports of similar messages
are contextual leads, not independent proof of
a shared sender or criminal connection.

---

## 10. Next Verification Tasks

Priority 1:
Resolve the exact TXID + vout for the 2020
547-sat outputs.

Priority 2:
Match each 2022 consolidation input to its
original funding transaction and output index.

Priority 3:
Determine how many 2022 dust inputs originated
from the same message campaign.

Priority 4:
Trace the funding input of the 2020 message
distribution transaction.

Priority 5:
Compare recipient selection against
non-recipient control addresses.

No additional conclusion is authorized
until the corresponding evidence is obtained.

---

## Evidence Freeze Declaration

Freeze version: V0
Date: 2026-10-27

Basis:
User-provided transaction records and
direct blockchain explorer inspection.

Independent complete raw-transaction
verification remains pending.

Purpose:
Preserve the investigation's current evidence
without retroactively converting hypotheses
into established facts.
