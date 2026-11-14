# Independent Financial Crime & Illicit Finance Research

**Following the Money — Independent, Evidence-Based Investigations**

An independent research project examining how far publicly accessible financial and blockchain evidence can reconstruct transactions, asset movements, and investigative mechanisms.

The objective is to distinguish **what the evidence establishes, what can reasonably be inferred, and what remains unknown**. Findings are documented with source references, reproducible checks, and explicit evidentiary limitations.

## Published Research

### 01 — [Binance 2026: Anatomy of a Delegated Wallet Drain](publications/binance-2026/README.md)

*Independent Reconstruction of EIP-7702 Execution and DEX/WETH Settlement*

**Network:** Ethereum

**Research status:** Two completed, scope-limited technical reconstructions

This investigation examines selected Ethereum transactions associated with the October 2026 Binance security incident. It reconstructs observable transaction activity while separating verified on-chain evidence from unresolved questions about incident-fund provenance, authorization, and beneficial ownership.

#### Part I — EIP-7702 Delegated Wallet Execution

- Recovered **50 EIP-7702 authorization signatures** to the same wallet address, with **one nonce-applicable authorization** identified in a nonce-only replay.
- Reconstructed approximately **167,464 ETH** in delegated asset movement, alongside **64 ERC-20 transfer attempts** and **63 matching Transfer events**.
- Identified a reverted **27th token-transfer call**, followed by **37 subsequent calls** without recorded call errors; the parent transaction succeeded.
- Audited historical USDT block-end balance changes of **1,615,409,498.97324 USDT** and two later transfers totaling **700 million USDT**, without establishing exclusive provenance.

[Read Part I — Master Investigation](publications/binance-2026/README.md)

#### Part II — A97B DEX/WETH Settlement

- Reconstructed **1,015 transactions** with matched WETH Withdrawal events and direct native ETH returns.
- Reconciled approximately **6,829.200 ETH** in gross direct returns.
- Documented **four separate direct ETH outflows totaling 10,647.2 ETH**.

[Read Part II — Transaction-Level Technical Report](publications/binance-2026/a97b-settlement/README.md) · [View Visual Report](publications/binance-2026/a97b-settlement/visual-report/README.md)

#### Independent Verification — Bitquery MCP

A subsequent independent-provider audit cross-checked the WETH Withdrawal events and amounts associated with the 1,015 reconciled transactions.

**Result: 1,015 / 1,015 PASS · 0 requiring review**

The audit preserved **21 raw response batches** and passed SHA-256 integrity checks. This cross-provider verification does not independently establish every native ETH return path or the provenance of the funds.

> **Evidence boundary:** These are completed, scope-limited reconstructions, not a complete independent verification of the Binance incident. Incident-wide fund conservation, transaction-level incident attribution, internal authorization, and beneficial ownership remain unresolved.

---

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
