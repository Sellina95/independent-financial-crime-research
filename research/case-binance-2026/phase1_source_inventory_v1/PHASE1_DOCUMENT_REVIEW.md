# Phase 1 — Document & Unsupported Format Review

Source commit: `bba74a5c89f830193999d8aef051349161dccf4e`
Files inspected: 102

## Preliminary roles

- EVIDENCE_RELATED_DOCUMENT_CANDIDATE: 54
- RESEARCH_REPORT_CANDIDATE: 9
- CODE_OR_CONFIG_CANDIDATE: 8
- UNRESOLVED_DOCUMENT_ROLE: 8
- IMAGE_OR_FIGURE: 8
- INTEGRITY_OR_METADATA_CANDIDATE: 7
- PRESENTATION_OR_EMBEDDED_DATA: 5
- PDF_DOCUMENT: 3

## Files requiring semantic review

- `research/case-binance-2026/700M_FIRST_HOP_DISTRIBUTION_AUDIT_V1.md` | EVIDENCE_RELATED_DOCUMENT_CANDIDATE | TX mentions: 0 | Embedded dataset: False | Errors: []
- `research/case-binance-2026/A97B/A97B_RESEARCH_MASTER.md` | EVIDENCE_RELATED_DOCUMENT_CANDIDATE | TX mentions: 0 | Embedded dataset: False | Errors: []
- `research/case-binance-2026/A97B/A97B_RESEARCH_REPORT.md` | EVIDENCE_RELATED_DOCUMENT_CANDIDATE | TX mentions: 10 | Embedded dataset: False | Errors: []
- `research/case-binance-2026/A97B/bitquery_withdrawal_crosswalk_v1/BITQUERY_WITHDRAWAL_CROSSWALK_V1.md` | EVIDENCE_RELATED_DOCUMENT_CANDIDATE | TX mentions: 0 | Embedded dataset: False | Errors: []
- `research/case-binance-2026/A97B/evidence/EXTERNAL_ATTRIBUTION_V1.md` | EVIDENCE_RELATED_DOCUMENT_CANDIDATE | TX mentions: 2 | Embedded dataset: False | Errors: []
- `research/case-binance-2026/A97B/evidence/SOURCE_SNAPSHOT_SHA256_V1.txt` | INTEGRITY_OR_METADATA_CANDIDATE | TX mentions: 0 | Embedded dataset: False | Errors: []
- `research/case-binance-2026/A97B/evidence/binance_official.pdf` | PDF_DOCUMENT | TX mentions: 0 | Embedded dataset: False | Errors: ['PDF_TEXT_EXTRACTOR_UNAVAILABLE']
- `research/case-binance-2026/A97B/evidence/bitquery_independent_audit_v1/README.md` | EVIDENCE_RELATED_DOCUMENT_CANDIDATE | TX mentions: 0 | Embedded dataset: False | Errors: []
- `research/case-binance-2026/A97B/evidence/bitquery_independent_audit_v1/a97b_batch_audit_full.mjs` | CODE_OR_CONFIG_CANDIDATE | TX mentions: 1 | Embedded dataset: False | Errors: []
- `research/case-binance-2026/A97B/evidence/bitquery_independent_audit_v1/a97b_integrity_audit_v2.py` | CODE_OR_CONFIG_CANDIDATE | TX mentions: 1 | Embedded dataset: False | Errors: []
- `research/case-binance-2026/A97B/evidence/bitquery_independent_crosscheck_v2/AUDIT.md` | EVIDENCE_RELATED_DOCUMENT_CANDIDATE | TX mentions: 1 | Embedded dataset: False | Errors: []
- `research/case-binance-2026/A97B/evidence/bitquery_independent_crosscheck_v2/SHA256SUMS` | INTEGRITY_OR_METADATA_CANDIDATE | TX mentions: 0 | Embedded dataset: False | Errors: []
- `research/case-binance-2026/A97B/evidence/chainward_analysis.pdf` | PDF_DOCUMENT | TX mentions: 0 | Embedded dataset: False | Errors: ['PDF_TEXT_EXTRACTOR_UNAVAILABLE']
- `research/case-binance-2026/A97B/evidence/fbi_alert.pdf` | PDF_DOCUMENT | TX mentions: 0 | Embedded dataset: False | Errors: ['PDF_TEXT_EXTRACTOR_UNAVAILABLE']
- `research/case-binance-2026/A97B/evidence/step70_bitquery_ledger_reconciliation_v1/AUDIT.md` | EVIDENCE_RELATED_DOCUMENT_CANDIDATE | TX mentions: 2 | Embedded dataset: False | Errors: []
- `research/case-binance-2026/A97B/evidence/step70_bitquery_ledger_reconciliation_v1/SHA256SUMS` | INTEGRITY_OR_METADATA_CANDIDATE | TX mentions: 0 | Embedded dataset: False | Errors: []
- `research/case-binance-2026/A97B/institutional_research_packet_v1/A97B_TIMELINE_TECHNICAL_REPORT_V1.md` | EVIDENCE_RELATED_DOCUMENT_CANDIDATE | TX mentions: 5 | Embedded dataset: False | Errors: []
- `research/case-binance-2026/A97B/institutional_research_packet_v1/HISTORICAL_PATTERN_RESEARCH_V1.md` | EVIDENCE_RELATED_DOCUMENT_CANDIDATE | TX mentions: 0 | Embedded dataset: False | Errors: []
- `research/case-binance-2026/AXIOM_BINANCE_2026_FIXED_RESEARCH_MAP_V1.md` | EVIDENCE_RELATED_DOCUMENT_CANDIDATE | TX mentions: 0 | Embedded dataset: False | Errors: []
- `research/case-binance-2026/AXIOM_EVIDENCE_DIFFERENCE_PROTOCOL_V1.md` | EVIDENCE_RELATED_DOCUMENT_CANDIDATE | TX mentions: 0 | Embedded dataset: False | Errors: []
- `research/case-binance-2026/AXIOM_INCIDENT_TRACEABILITY_MASTER_V1.md` | EVIDENCE_RELATED_DOCUMENT_CANDIDATE | TX mentions: 24 | Embedded dataset: False | Errors: []
- `research/case-binance-2026/AXIOM_INCIDENT_TRACEABILITY_MASTER_V2.md` | EVIDENCE_RELATED_DOCUMENT_CANDIDATE | TX mentions: 0 | Embedded dataset: False | Errors: []
- `research/case-binance-2026/AXIOM_PUBLICATION_CLAIMS_AUDIT_V1.md` | EVIDENCE_RELATED_DOCUMENT_CANDIDATE | TX mentions: 0 | Embedded dataset: False | Errors: []
- `research/case-binance-2026/BINANCE_2026_DELEGATED_WALLET_DRAIN_CASE_STUDY.md` | EVIDENCE_RELATED_DOCUMENT_CANDIDATE | TX mentions: 3 | Embedded dataset: False | Errors: []
- `research/case-binance-2026/BINANCE_2026_DELEGATED_WALLET_DRAIN_CASE_STUDY_DRAFT_V1.md` | EVIDENCE_RELATED_DOCUMENT_CANDIDATE | TX mentions: 3 | Embedded dataset: False | Errors: []
- `research/case-binance-2026/BINANCE_2026_DELEGATED_WALLET_DRAIN_CASE_STUDY_DRAFT_V2.md` | EVIDENCE_RELATED_DOCUMENT_CANDIDATE | TX mentions: 3 | Embedded dataset: False | Errors: []
- `research/case-binance-2026/BINANCE_2026_DELEGATED_WALLET_DRAIN_CASE_STUDY_DRAFT_V3.md` | EVIDENCE_RELATED_DOCUMENT_CANDIDATE | TX mentions: 3 | Embedded dataset: False | Errors: []
- `research/case-binance-2026/BLACKLIST_175M_CASE_AUDIT_V1.md` | EVIDENCE_RELATED_DOCUMENT_CANDIDATE | TX mentions: 3 | Embedded dataset: False | Errors: []
- `research/case-binance-2026/EG01_EXECUTION_TIME_AUDIT_V1.md` | EVIDENCE_RELATED_DOCUMENT_CANDIDATE | TX mentions: 0 | Embedded dataset: False | Errors: []
- `research/case-binance-2026/EG08_AAVE_POSITION_ATTRIBUTION_CORRECTION_V1.md` | UNRESOLVED_DOCUMENT_ROLE | TX mentions: 0 | Embedded dataset: False | Errors: []
- `research/case-binance-2026/EVIDENCE_CHECKPOINT_V1.md` | EVIDENCE_RELATED_DOCUMENT_CANDIDATE | TX mentions: 6 | Embedded dataset: False | Errors: []
- `research/case-binance-2026/EVIDENCE_GAP_REPORT.md` | EVIDENCE_RELATED_DOCUMENT_CANDIDATE | TX mentions: 7 | Embedded dataset: False | Errors: []
- `research/case-binance-2026/GATE_1_COMPLETENESS_REVIEW_V1.md` | EVIDENCE_RELATED_DOCUMENT_CANDIDATE | TX mentions: 0 | Embedded dataset: False | Errors: []
- `research/case-binance-2026/GATE_2_175M_PATH_CONTINUITY_AUDIT_V1.md` | EVIDENCE_RELATED_DOCUMENT_CANDIDATE | TX mentions: 2 | Embedded dataset: False | Errors: []
- `research/case-binance-2026/GATE_2_ADDITIONAL_SOURCE_ROLE_REVIEW_V1.md` | UNRESOLVED_DOCUMENT_ROLE | TX mentions: 14 | Embedded dataset: False | Errors: []
- `research/case-binance-2026/GATE_2_BITCOIN_11TX_AUDIT_V1.md` | RESEARCH_REPORT_CANDIDATE | TX mentions: 0 | Embedded dataset: False | Errors: []
- `research/case-binance-2026/GATE_2_BTC_ATTRIBUTION_ASSESSMENT_V1.md` | EVIDENCE_RELATED_DOCUMENT_CANDIDATE | TX mentions: 0 | Embedded dataset: False | Errors: []
- `research/case-binance-2026/GATE_2_ERC20_TRANSFER_AUDIT_V1.md` | EVIDENCE_RELATED_DOCUMENT_CANDIDATE | TX mentions: 6 | Embedded dataset: False | Errors: []
- `research/case-binance-2026/GATE_2_ETH_DELEGATION_CONTRACT_LINK_V1.md` | EVIDENCE_RELATED_DOCUMENT_CANDIDATE | TX mentions: 3 | Embedded dataset: False | Errors: []
- `research/case-binance-2026/GATE_2_ETH_EXTERNAL_INCIDENT_LINK_V1.md` | EVIDENCE_RELATED_DOCUMENT_CANDIDATE | TX mentions: 1 | Embedded dataset: False | Errors: []
- `research/case-binance-2026/GATE_2_ETH_HISTORICAL_RECONCILIATION_V1.md` | EVIDENCE_RELATED_DOCUMENT_CANDIDATE | TX mentions: 0 | Embedded dataset: False | Errors: []
- `research/case-binance-2026/GATE_2_ETH_T02_T03_MECHANISM_REVIEW_V1.md` | EVIDENCE_RELATED_DOCUMENT_CANDIDATE | TX mentions: 3 | Embedded dataset: False | Errors: []
- `research/case-binance-2026/GATE_2_ETH_T03_CALLER_RESTRICTION_V1.md` | UNRESOLVED_DOCUMENT_ROLE | TX mentions: 1 | Embedded dataset: False | Errors: []
- `research/case-binance-2026/GATE_2_ETH_TECHNICAL_EVIDENCE_ASSESSMENT_V1.md` | EVIDENCE_RELATED_DOCUMENT_CANDIDATE | TX mentions: 0 | Embedded dataset: False | Errors: []
- `research/case-binance-2026/GATE_2_EXPANSION_AUDIT_V1.md` | EVIDENCE_RELATED_DOCUMENT_CANDIDATE | TX mentions: 0 | Embedded dataset: False | Errors: []
- `research/case-binance-2026/GATE_2_EXTERNAL_TXID_CROSSCHECK_V1.md` | EVIDENCE_RELATED_DOCUMENT_CANDIDATE | TX mentions: 9 | Embedded dataset: False | Errors: []
- `research/case-binance-2026/GATE_2_INCIDENT_ATTRIBUTION_REVIEW_V1.md` | UNRESOLVED_DOCUMENT_ROLE | TX mentions: 0 | Embedded dataset: False | Errors: []
- `research/case-binance-2026/GATE_2_INITIAL_ATTRIBUTION_AUDIT_V1.md` | EVIDENCE_RELATED_DOCUMENT_CANDIDATE | TX mentions: 11 | Embedded dataset: False | Errors: []
- `research/case-binance-2026/GATE_2_MULTICHAIN_DISCOVERY_AUDIT_V1.md` | EVIDENCE_RELATED_DOCUMENT_CANDIDATE | TX mentions: 0 | Embedded dataset: False | Errors: []
- `research/case-binance-2026/GATE_2_POR_OWNERSHIP_AUDIT_V1.md` | RESEARCH_REPORT_CANDIDATE | TX mentions: 0 | Embedded dataset: False | Errors: []
- `research/case-binance-2026/GATE_2_PREINCIDENT_OWNERSHIP_AUDIT_V1.md` | RESEARCH_REPORT_CANDIDATE | TX mentions: 0 | Embedded dataset: False | Errors: []
- `research/case-binance-2026/GATE_2_TRON_NATIVE_TX_AUDIT_V1.md` | RESEARCH_REPORT_CANDIDATE | TX mentions: 0 | Embedded dataset: False | Errors: []
- `research/case-binance-2026/GATE_2_TX_CONTEXT_REVIEW_V1.md` | EVIDENCE_RELATED_DOCUMENT_CANDIDATE | TX mentions: 0 | Embedded dataset: False | Errors: []
- `research/case-binance-2026/GATE_2_XRPL_FIVE_SOURCE_AUDIT_V1.md` | EVIDENCE_RELATED_DOCUMENT_CANDIDATE | TX mentions: 0 | Embedded dataset: False | Errors: []
- `research/case-binance-2026/GATE_3_T03_TO_700M_LINKAGE_AUDIT_V1.md` | EVIDENCE_RELATED_DOCUMENT_CANDIDATE | TX mentions: 1 | Embedded dataset: False | Errors: []
- `research/case-binance-2026/INCIDENT_FUND_ATTRIBUTION_CHECKPOINT_2026-11-05.md` | EVIDENCE_RELATED_DOCUMENT_CANDIDATE | TX mentions: 0 | Embedded dataset: False | Errors: []
- `research/case-binance-2026/INCIDENT_WIDE_RESEARCH_FRAMEWORK_V1.md` | EVIDENCE_RELATED_DOCUMENT_CANDIDATE | TX mentions: 1 | Embedded dataset: False | Errors: []
- `research/case-binance-2026/INTERIM_TIMELINE_V1.md` | EVIDENCE_RELATED_DOCUMENT_CANDIDATE | TX mentions: 0 | Embedded dataset: False | Errors: []
- `research/case-binance-2026/INTERIM_TIMELINE_V2.md` | EVIDENCE_RELATED_DOCUMENT_CANDIDATE | TX mentions: 1 | Embedded dataset: False | Errors: []
- `research/case-binance-2026/OFFICIAL_SOURCE_VERIFICATION_V1.md` | EVIDENCE_RELATED_DOCUMENT_CANDIDATE | TX mentions: 0 | Embedded dataset: False | Errors: []
- `research/case-binance-2026/USDT_FREEZE_BALANCE_AUDIT_V3.md` | EVIDENCE_RELATED_DOCUMENT_CANDIDATE | TX mentions: 6 | Embedded dataset: False | Errors: []
- `research/case-binance-2026/USDT_FREEZE_TIMELINE_CHECKPOINT_V4.md` | EVIDENCE_RELATED_DOCUMENT_CANDIDATE | TX mentions: 5 | Embedded dataset: False | Errors: []
- `research/case-binance-2026/USDT_FUND_FLOW_AND_FREEZE_V2.md` | EVIDENCE_RELATED_DOCUMENT_CANDIDATE | TX mentions: 10 | Embedded dataset: False | Errors: []
- `research/case-binance-2026/analysis/master_timeline_v0/BINANCE14_INSTITUTIONAL_TIMELINE_V1.html` | PRESENTATION_OR_EMBEDDED_DATA | TX mentions: 2938 | Embedded dataset: False | Errors: []
- `research/case-binance-2026/analysis/master_timeline_v0/BINANCE14_MASTER_FLOW_MAP_V1.html` | PRESENTATION_OR_EMBEDDED_DATA | TX mentions: 2114 | Embedded dataset: True | Errors: []
- `research/case-binance-2026/analysis/master_timeline_v0/BINANCE14_TIMELINE_V0.html` | PRESENTATION_OR_EMBEDDED_DATA | TX mentions: 2114 | Embedded dataset: False | Errors: []
- `research/case-binance-2026/build_asset_inventory.py` | CODE_OR_CONFIG_CANDIDATE | TX mentions: 2 | Embedded dataset: False | Errors: []
- `research/case-binance-2026/evidence/binance14_all_receivers_census_v1/README.md` | UNRESOLVED_DOCUMENT_ROLE | TX mentions: 0 | Embedded dataset: False | Errors: []
- `research/case-binance-2026/evidence/binance14_all_receivers_census_v1/step66_receiver_identity_rpc_audit_v1/audit.md` | EVIDENCE_RELATED_DOCUMENT_CANDIDATE | TX mentions: 0 | Embedded dataset: False | Errors: []
- `research/case-binance-2026/evidence/binance14_all_receivers_census_v1/step83_official_attribution_crosswalk_v1/CROSSWALK_AUDIT_V1.md` | RESEARCH_REPORT_CANDIDATE | TX mentions: 0 | Embedded dataset: False | Errors: []
- `research/case-binance-2026/evidence/binance14_all_receivers_census_v1/step83_official_attribution_crosswalk_v1/source_snapshots/elliptic_source.txt` | UNRESOLVED_DOCUMENT_ROLE | TX mentions: 0 | Embedded dataset: False | Errors: []
- `research/case-binance-2026/evidence/binance14_all_receivers_census_v1/step83_official_attribution_crosswalk_v1/source_snapshots/fbi_eth_addresses.txt` | UNRESOLVED_DOCUMENT_ROLE | TX mentions: 0 | Embedded dataset: False | Errors: []
- `research/case-binance-2026/evidence/binance14_all_receivers_census_v1/step84_a97b_erc20_exception_audit_v1/ERC20_EXCEPTION_AUDIT_V1.md` | RESEARCH_REPORT_CANDIDATE | TX mentions: 0 | Embedded dataset: False | Errors: []
- `research/case-binance-2026/evidence/binance14_all_receivers_census_v1/step85_a97b_final_event_audit_v1/A97B_FINAL_EVENT_AUDIT_V1.md` | EVIDENCE_RELATED_DOCUMENT_CANDIDATE | TX mentions: 0 | Embedded dataset: False | Errors: []
- `research/case-binance-2026/evidence/eg05_kite_historical_pause_v1/audit.md` | EVIDENCE_RELATED_DOCUMENT_CANDIDATE | TX mentions: 0 | Embedded dataset: False | Errors: []
- `research/case-binance-2026/evidence/eg05_kite_pause_origin_v1/audit.md` | RESEARCH_REPORT_CANDIDATE | TX mentions: 0 | Embedded dataset: False | Errors: []
- `research/case-binance-2026/evidence/eg08_plasma_post_delivery_v1/step06f_withdrawal_revert_diagnostics_v1/anvil.log` | UNRESOLVED_DOCUMENT_ROLE | TX mentions: 0 | Embedded dataset: False | Errors: []
- `research/case-binance-2026/evidence/exploiter16_token_provenance_v1/STEP07B_12_AUDIT_CHECKPOINT.md` | EVIDENCE_RELATED_DOCUMENT_CANDIDATE | TX mentions: 3 | Embedded dataset: False | Errors: []
- `research/case-binance-2026/evidence/exploiter16_token_provenance_v1/step16_receipt_evidence_v1/SHA256SUMS` | INTEGRITY_OR_METADATA_CANDIDATE | TX mentions: 0 | Embedded dataset: False | Errors: []
- `research/case-binance-2026/evidence/exploiter16_token_provenance_v1/step18g_four_route_evidence_v1/SHA256SUMS` | INTEGRITY_OR_METADATA_CANDIDATE | TX mentions: 0 | Embedded dataset: False | Errors: []
- `research/case-binance-2026/evidence/exploiter16_token_provenance_v1/step19f_middle_hop_receipts_v1/SHA256SUMS` | INTEGRITY_OR_METADATA_CANDIDATE | TX mentions: 0 | Embedded dataset: False | Errors: []
- `research/case-binance-2026/evidence/official_announcements/BINANCE_OFFICIAL_UPDATE_1_BROWSER_CAPTURE.txt` | EVIDENCE_RELATED_DOCUMENT_CANDIDATE | TX mentions: 0 | Embedded dataset: False | Errors: []
- `research/case-binance-2026/evidence/official_announcements/BINANCE_OFFICIAL_UPDATE_2_BROWSER_CAPTURE.txt` | EVIDENCE_RELATED_DOCUMENT_CANDIDATE | TX mentions: 0 | Embedded dataset: False | Errors: []
- `research/case-binance-2026/evidence/official_announcements/EVIDENCE_MANIFEST_V1.md` | INTEGRITY_OR_METADATA_CANDIDATE | TX mentions: 0 | Embedded dataset: False | Errors: []
- `research/case-binance-2026/evidence/step72_external_attribution_v1/BITQUERY.html` | PRESENTATION_OR_EMBEDDED_DATA | TX mentions: 56 | Embedded dataset: False | Errors: []
- `research/case-binance-2026/evidence/step72_external_attribution_v1/IMD.html` | PRESENTATION_OR_EMBEDDED_DATA | TX mentions: 4 | Embedded dataset: False | Errors: []
- `research/case-binance-2026/evidence/step73_preincident_graphsense_v1/historical_source.yaml` | CODE_OR_CONFIG_CANDIDATE | TX mentions: 0 | Embedded dataset: False | Errors: []
- `research/case-binance-2026/evidence/step75a_official_report_crosswalk_v1/STEP75A_REPORT.md` | RESEARCH_REPORT_CANDIDATE | TX mentions: 0 | Embedded dataset: False | Errors: []
- `research/case-binance-2026/evidence/step75a_official_report_crosswalk_v1/official_report_excerpt.txt` | RESEARCH_REPORT_CANDIDATE | TX mentions: 0 | Embedded dataset: False | Errors: []
- `research/case-binance-2026/figures/figure_01_execution_sequence.png` | IMAGE_OR_FIGURE | TX mentions: 0 | Embedded dataset: False | Errors: []
- `research/case-binance-2026/figures/figure_02_authorization_nonce.png` | IMAGE_OR_FIGURE | TX mentions: 0 | Embedded dataset: False | Errors: []
- `research/case-binance-2026/figures/figure_03_delegated_transfer.png` | IMAGE_OR_FIGURE | TX mentions: 0 | Embedded dataset: False | Errors: []
- `research/case-binance-2026/figures/figure_04_failure_tolerance.png` | IMAGE_OR_FIGURE | TX mentions: 0 | Embedded dataset: False | Errors: []
- `research/case-binance-2026/figures/figure_05_usdt_reconciliation.png` | IMAGE_OR_FIGURE | TX mentions: 0 | Embedded dataset: False | Errors: []
- `research/case-binance-2026/investigation_workspace_v1/research_app.py` | CODE_OR_CONFIG_CANDIDATE | TX mentions: 0 | Embedded dataset: True | Errors: []
- `research/case-binance-2026/investigation_workspace_v1/test_workspace.py` | CODE_OR_CONFIG_CANDIDATE | TX mentions: 0 | Embedded dataset: True | Errors: []
- `research/case-binance-2026/investigation_workspace_v1/tx_lookup.py` | CODE_OR_CONFIG_CANDIDATE | TX mentions: 0 | Embedded dataset: False | Errors: []
- `research/case-binance-2026/investigation_workspace_v1/weth_eth_context.py` | CODE_OR_CONFIG_CANDIDATE | TX mentions: 0 | Embedded dataset: False | Errors: []
- `research/case-binance-2026/publication_staging/a97b-visual-report/README.md` | EVIDENCE_RELATED_DOCUMENT_CANDIDATE | TX mentions: 0 | Embedded dataset: False | Errors: []
- `research/case-binance-2026/publication_staging/a97b-visual-report/figures/01-a97b-eth-flow-overview.png` | IMAGE_OR_FIGURE | TX mentions: 0 | Embedded dataset: False | Errors: []
- `research/case-binance-2026/publication_staging/a97b-visual-report/figures/02-a97b-dex-weth-settlement.png` | IMAGE_OR_FIGURE | TX mentions: 0 | Embedded dataset: False | Errors: []
- `research/case-binance-2026/publication_staging/a97b-visual-report/figures/03-historical-crypto-theft-comparison.png` | IMAGE_OR_FIGURE | TX mentions: 0 | Embedded dataset: False | Errors: []

## Important limitations

- File roles are preliminary.
- TX mentions do not establish a transfer.
- Embedded HTML data is not independent evidence.
- PDF/image content may remain unreviewed.
- No event-level deduplication performed.
- No final transfer or graph connection count.

PHASE 1 is not complete.
