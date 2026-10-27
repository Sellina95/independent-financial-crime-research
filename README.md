# Independent Financial Crime & Illicit Finance Research

**Following the Money — An Independent, Evidence-Based Research Project**

## 1. Research Mission

This project investigates how financial crime and illicit financial flows can be studied through publicly accessible evidence.

The objective is not to identify or accuse individuals of criminal conduct. Instead, the research seeks to reconstruct documented financial transactions, examine observable fund movements, and identify the evidentiary limits of public financial data.

**Core Research Question**

*How far can publicly available evidence trace financial flows associated with documented financial crime, and where does that evidence stop?*

## 2. Research Scope

The project begins with publicly documented financial crime cases involving blockchain transactions, with potential future expansion into broader illicit finance research.

Research activities include:

- Reconstructing transactions linked to officially documented cases.
- Examining fund movements through publicly accessible blockchain explorers.
- Comparing transaction evidence with official regulatory and judicial records.
- Distinguishing observable transaction activity from claims about ownership, intent, or criminal liability.
- Documenting technical, legal, institutional, and evidentiary limitations.

## 3. Evidence Classification

Every material finding should be classified as:

| Classification | Definition |
|---|---|
| **OBSERVED** | Directly supported by identifiable, reproducible evidence. |
| **INFERRED** | A reasoned interpretation supported by evidence but not directly established. |
| **UNKNOWN** | Information that available evidence cannot establish. |
| **DISPROVEN** | A hypothesis contradicted by reliable evidence. |

A blockchain transaction alone does not establish criminal intent, beneficial ownership, or participation in illicit activity.

## 4. Research Principles

1. **Evidence before interpretation.** Findings must be traceable to identifiable sources.
2. **No guilt by association.** Transaction proximity to a sanctioned or investigated address does not establish criminal conduct.
3. **Separate transaction time from knowledge time.** Record when an event occurred and when relevant information became publicly available.
4. **Distinguish reconstruction from detection.** Retrospective analysis must not be presented as evidence of prospective detection capability.
5. **Preserve uncertainty.** Unknown information must remain explicitly unknown.
6. **Prioritize reproducibility.** Public findings should include sufficient references for independent verification.
7. **Protect individuals.** Do not publish unsupported allegations or unnecessary personal information.

## 5. Initial Research Case

### CASE-001 — Blender.io: Bitcoin Fund Flow Reconstruction

**Research objective:** Reconstruct a limited set of Bitcoin transactions involving an address identified in official U.S. sanctions materials, and assess what the publicly observable transaction record does and does not establish.

**Primary source:** U.S. Department of the Treasury, Office of Foreign Assets Control (OFAC), May 6, 2022.

Official reference: https://ofac.treasury.gov/recent-actions/20220506

Initial blockchain explorer: https://mempool.space/

**Initial research status:** Transaction reconstruction in progress. No independent determination of criminal liability.

## 6. Current Research

Bitcoin UTXO Provenance & Transaction Network Analysis

Status: Active independent research
Evidence baseline: October 27, 2026

This research examines the provenance and subsequent spending of 547-satoshi Bitcoin outputs, focusing on observable transaction relationships, funding networks, and the limitations of common-input ownership heuristics.

Research Questions

What funding sources supported the repeated distribution of 547-satoshi outputs?

Can the source transactions be connected through verifiable UTXO relationships?

Do these funding sources share any historical relationship with high-value Bitcoin transactions?

How frequently were 547-satoshi outputs subsequently spent alongside substantially larger Bitcoin inputs?

Verified Findings

A Bitcoin transaction dated April 23, 2022, containing approximately 1,500.726 BTC in total input value, provides the initial investigation reference.

Evidence

Result

Inputs in reference transaction

78

Inputs valued at exactly 547 satoshis

46

Other inputs

32

Distinct source transactions for the 46 outputs

40

Verified direct UTXO links among the 40 source transactions

1

Total 547-satoshi outputs across those transactions

17,182

Outputs subsequently spent

11,415

Distinct spending transactions

6,975

An exploratory analysis of 100 spending transactions identified nine transactions containing at least 100 BTC in additional, non-547-satoshi inputs.

Sampling limitation: These 100 transactions were selected by sorted transaction ID, not random sampling. Their characteristics cannot be generalized to the complete population of 6,975 spending transactions.

Evidence Boundaries

OBSERVED: Transaction inputs, outputs, values, timestamps, and verifiable UTXO spending relationships.

INFERRED: Potential operational relationships among recurring funding transactions, subject to further validation.

UNKNOWN: Actual sender identity, underlying motivation, common beneficial ownership, and any historical relationship between the 547-satoshi senders and the high-value Bitcoin funding sources.

The presence of dust-sized outputs or joint spending with high-value inputs does not independently establish malicious dusting, illicit finance, or common ownership.

Next Investigation

Compare high-value spending transactions involving the identified 547-satoshi outputs, examine recurring funding patterns, and test whether the approximately 1,500 BTC reference transaction is unusual within the observed network.

Detailed evidence, code, and the frozen investigation baseline are maintained under:

cases/CASE-003-silk-road/

Research principle: Follow transaction evidence without confusing fund movement, wallet control, beneficial ownership, or criminal intent.

## 7. Long-Term Research Direction

The research may eventually explore:

- Transaction tracing and its limitations.
- Anti-Money Laundering (AML) investigative methodologies.
- Sanctions-related financial networks.
- Financial crime typologies and transaction patterns.
- The difference between observable warning indicators and defensible investigative conclusions.

Expansion will depend on the quality of available evidence rather than the complexity of potential analytical tools.

---

**Research philosophy:** Follow the evidence. Document the uncertainty. Never turn an inference into a fact.
