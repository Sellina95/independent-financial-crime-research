# Independent Financial Crime & Illicit Finance Research

**Following the Money — Independent, Evidence-Based Investigations**

An independent research project examining how far publicly accessible financial and blockchain evidence can reconstruct transactions, asset movements, and investigative mechanisms.

The objective is to distinguish **what the evidence establishes, what can reasonably be inferred, and what remains unknown**. Findings are documented with source references, reproducible checks, and explicit evidentiary limitations.

## Published Research

### 01 — [Binance 2026: Anatomy of a Delegated Wallet Drain](publications/binance-2026/README.md)

*An Independent Reconstruction of EIP-7702 Authorization, Batch Execution, and Asset Movements*

**Network:** Ethereum · **Research status:** Completed, scope-limited technical reconstruction

This investigation examines selected Ethereum transactions associated with the October 2026 Binance security incident by named external investigators. It reconstructs an EIP-7702 authorization sequence, delegated asset movement, and the subsequent removal of delegation, without claiming to independently establish corporate authorization or the full incident-wide flow of funds.

**Selected findings:**

- **50** EIP-7702 authorization signatures recovering to the same wallet address; **one** nonce-applicable authorization identified in a nonce-only replay.
- Approximately **167,464 ETH** moved in the audited execution, alongside **64 ERC-20 transfer attempts** and **63 matching Transfer events**.
- The **27th token-transfer call reverted**; **37 subsequent calls continued** without recorded call errors, while the parent transaction succeeded.
- Historical USDT balances showed corresponding **1,615,409,498.97324 USDT** block-end changes. Two later transfers totaling **700 million USDT** were audited, without establishing exclusive provenance from the earlier transaction.

**[Read the Full Investigation](publications/binance-2026/README.md)**

**Part II — A97B DEX Settlement and ETH Return:** [Read the transaction-level reconstruction](publications/binance-2026/a97b-settlement/README.md). The scope-limited audit documents 1,015 ETH-return transactions and subsequent direct ETH outflows. Incident-fund provenance and ultimate ownership remain unresolved. · [Figures & Supporting Evidence](publications/binance-2026/)

> **Evidence boundary:** This is a bounded reconstruction of selected transactions, not an independent verification of the entire reported incident. Transaction-level incident attribution, internal approval, beneficial ownership, and complete fund conservation remain unresolved.

### 02 — [Bitcoin: Silk Road / Individual X (2020)](publications/silk-road-2020/README.md)

*Retrospective Bitcoin Transaction Reconstruction & DOJ Evidence Review*

**Network:** Bitcoin · **Research status:** Completed, scope-limited review · **Final finding:** PARTIALLY VERIFIED

This case compares observable Bitcoin transaction links with the U.S. Department of Justice's publicly documented Silk Road / Individual X forfeiture case.

**Selected findings:**

- Reconstructed a documented link between a **2,500 BTC output in 2012** and a **69,471.082201 BTC consolidation in 2013**.
- Examined a separate **2020 transaction** and DOJ allegations as distinct categories of evidence.
- Identified the evidentiary gap: the complete intervening transaction path and independent identity-attribution process were **not** reproduced.

**[Read the Full Bitcoin Investigation](publications/silk-road-2020/README.md)**

> **Evidence boundary:** The research supports a partial on-chain reconstruction. It does not independently establish the complete transaction history, beneficial ownership, or the DOJ's identity-attribution process.

## Research Methodology

Every material finding is assessed using explicit evidence classifications:

| Classification | Meaning |
|---|---|
| **OBSERVED** | Directly supported by identifiable, checkable evidence |
| **INFERRED** | An interpretation supported by evidence but not independently established |
| **UNKNOWN** | Not established by the available evidence |
| **DISPROVEN** | A hypothesis contradicted by reliable evidence |

The research distinguishes **transaction time from information availability**, **retrospective reconstruction from real-time detection**, and **on-chain connectivity from real-world identity or criminal responsibility**.

## Research in Progress

Ongoing investigations and intermediate working files are maintained on separate research branches. Only scope-defined, reviewed findings are selected for presentation on `main`. Branch separation is for organization and **does not make research branches private** in this public repository.

## Research Philosophy

**Follow the evidence. Document the uncertainty. Never turn an inference into a fact.**

*Independent research, not an official investigation or a finding of criminal responsibility.*
