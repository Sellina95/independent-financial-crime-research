# CASE-002 — Ronin Network Hack
## Anchor Evidence V0.1

**Research Series:** Following the Money  
**Status:** INITIAL ANCHOR IDENTIFIED  
**Research Type:** Retrospective On-Chain Fund Flow Reconstruction

### 1. Research Question

How far can publicly accessible blockchain evidence reconstruct the movement of assets associated with the March 2022 Ronin Bridge exploit?

### 2. Case Context

The Ronin Bridge exploit involved the unauthorized withdrawal of approximately 173,600 ETH and 25,500,000 USDC.

The transactions occurred on March 23, 2022. The incident was publicly disclosed on March 29, 2022.

The distinction between transaction time and public disclosure time must be preserved throughout this research.

### 3. Identified Addresses

**Ronin Bridge contract**

`0x1A2a1c938CE3eC39b6D47113c7955bAa9DD454F2`

**OFAC-identified address**

`0x098B716B8Aaf21512996dC57EB0615e2383E2f96`

The second address has been identified in official sanctions materials. Its connection to the exploit must be evaluated using both official documentation and blockchain evidence.

### 4. Anchor Transaction A — ETH

Transaction hash:

`0xc28fad5e8d5e0ce6a2eaf67b6687be5d58113e16be590824d6cfa1a94467d0b7`

- Block: 14442835
- Status: Success
- Transaction initiator: OFAC-identified address
- Interacted contract: Ronin Bridge
- Top-level transaction value: 0 ETH
- Internal transfer from Ronin Bridge to identified address: 173,600 ETH

**Classification:** OBSERVED — Etherscan transaction and internal transfer records.

The internal transfer must not be confused with the top-level transaction value.

Source: https://etherscan.io/tx/0xc28fad5e8d5e0ce6a2eaf67b6687be5d58113e16be590824d6cfa1a94467d0b7

### 5. Anchor Transaction B — USDC

Transaction hash:

`0xed2c72ef1a552ddaec6dd1f5cddf0b59a8f37f82bdda5257d9c7c37db7bb9b08`

- Block: 14442840
- Status: Success
- Transaction initiator: OFAC-identified address
- Interacted contract: Ronin Bridge
- ERC-20 transfer: 25,500,000 USDC
- Token movement: Ronin Bridge to identified address

**Classification:** OBSERVED — Etherscan ERC-20 transfer records.

Source: https://etherscan.io/tx/0xed2c72ef1a552ddaec6dd1f5cddf0b59a8f37f82bdda5257d9c7c37db7bb9b08

### 6. Evidence Assessment

**OBSERVED**
- Both transactions were successfully recorded on Ethereum.
- Both transactions involved the same identified address.
- The ETH transaction contains an internal transfer of 173,600 ETH.
- The USDC transaction contains an ERC-20 transfer of 25,500,000 USDC.

**OFFICIALLY ATTRIBUTED**
- The identified address has been associated with the Ronin incident in official U.S. sanctions materials.

**UNKNOWN**
- The complete subsequent movement of the assets.
- The beneficial ownership of downstream addresses.
- The identity and role of individual downstream recipients.
- Whether subsequent transactions involved independent counterparties or addresses under common control.

### 7. Research Boundary

The two transactions form the initial event-linked tracing anchors.

On-chain connectivity alone does not establish downstream criminal liability, beneficial ownership, or knowledge of illicit origin.

Subsequent tracing must distinguish direct asset transfers, intermediary contracts, token swaps, and unsupported ownership inferences.

### 8. Next Research Step

Reconstruct the first outgoing transfers from the identified address, separately for ETH and USDC.

Record transaction hashes, timestamps, asset amounts, recipient addresses, and evidence limitations before extending the tracing path.

No automated risk scoring or criminal attribution will be introduced at this stage.
