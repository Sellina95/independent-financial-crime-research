# PHASE 1 — Coverage Triage

Source commit: `bba74a5c89f830193999d8aef051349161dccf4e`

## Reconciliation

- Source files: 3,105
- Structured files: 3003
- Non-structured files: 102
- Top-level schema families: 355
- Families with nested signature variation: 22
- Families with sampling-limited members: 43
- Priority schema review groups: 51
- Document exceptions: 70

## Priority schema review

- `c59b37e963fa3c09a78f` | files=2241 | nested_variants=5 | limited_files=15 | example=`research/case-binance-2026/evidence/binance14_all_receivers_census_v1/step72_a97b_pattern_funding_audit_v1/rpc_cache/balance_26301443.json`
- `1485ca01a3e37dfcf221` | files=149 | nested_variants=2 | limited_files=10 | example=`research/case-binance-2026/A97B/integrated_event_audit_v1/recovered_receipts/0x0003cf5d3cffc1fde2a370f577571230112177a8a38da8bcd312b4525b6e4253.json`
- `9d4220dec04a9cef0e22` | files=30 | nested_variants=7 | limited_files=1 | example=`research/case-binance-2026/evidence/eg03_two_address_consolidation_v1/balance_A_26306503.json`
- `550daf37753235a3af66` | files=24 | nested_variants=23 | limited_files=0 | example=`research/case-binance-2026/evidence/eg08_plasma_post_delivery_v1/step06b_issuer_control_simulation_v1/manifest.json`
- `70897b228dc129d6a0d9` | files=23 | nested_variants=7 | limited_files=4 | example=`research/case-binance-2026/evidence/central_blacklist_audit_v1/balance_block_26300953.json`
- `c8b20c0308a921c00a99` | files=23 | nested_variants=6 | limited_files=23 | example=`research/case-binance-2026/A97B/eth_address_receipts_v1/pages/page_0001.json`
- `2dff4c4b25493fa7ffb2` | files=22 | nested_variants=2 | limited_files=7 | example=`research/case-binance-2026/evidence/binance14_all_receivers_census_v1/step69_noncentral_receiver_forward_screen_v1/raw/0x139b920004360b08a1e285ba3859771eb0470ce9.json`
- `24692d235b0ec9a64ecb` | files=21 | nested_variants=1 | limited_files=21 | example=`research/case-binance-2026/A97B/evidence/bitquery_independent_audit_v1/batch_001.json`
- `21f44ce4b60e14b8d9bb` | files=12 | nested_variants=11 | limited_files=4 | example=`research/case-binance-2026/evidence/eg08_source_attribution_v1/step08o_multichain_funding_window_v1/chain_events.json`
- `f620ee3efc63fc043ebd` | files=12 | nested_variants=3 | limited_files=12 | example=`research/case-binance-2026/evidence/binance14_all_receivers_census_v1/step72_a97b_pattern_funding_audit_v1/rpc_cache/incoming_eth_page_0001.json`
- `309b4d086e7fd4a1f72d` | files=12 | nested_variants=2 | limited_files=12 | example=`research/case-binance-2026/evidence/binance14_all_receivers_census_v1/step70_a97b_forward_census_v1/pages/page_0001.json`
- `f7b82dc469849c9602cd` | files=9 | nested_variants=1 | limited_files=1 | example=`research/case-binance-2026/A97B/evidence/bitquery_independent_crosscheck_v1/ETH_TX_EVENTS_BATCH5_RAW_V1.json`
- `b595830007221f4e7ec0` | files=6 | nested_variants=2 | limited_files=6 | example=`research/case-binance-2026/evidence/binance14_all_receivers_census_v1/step80_a97b_full_dex_census_v1/batches/batch_0001.json`
- `1eaf24eaf19cf4db9536` | files=5 | nested_variants=4 | limited_files=4 | example=`research/case-binance-2026/evidence/binance14_all_receivers_census_v1/step67_internal_eth_trace_audit_v1/blockscout_crosscheck_v1/transactions/0x31c4c9fe287d54fb9d3b79980477a8c793a11f774b98d0a9a92de1dad888a91d.json`
- `31f1657957a388a00ee2` | files=4 | nested_variants=1 | limited_files=4 | example=`research/case-binance-2026/evidence/exploiter16_token_provenance_v1/step18g_four_route_evidence_v1/aave_main.json`
- `51a7018d1ae663b919c8` | files=3 | nested_variants=3 | limited_files=0 | example=`research/case-binance-2026/evidence/eg08_plasma_post_delivery_v1/step06b_issuer_control_simulation_v1/blocklist_current_state.json`
- `da49d1e9bee43da5662b` | files=3 | nested_variants=3 | limited_files=0 | example=`research/case-binance-2026/evidence/eg08_plasma_post_delivery_v1/step05b_atoken_identity_reconciliation_v1/historical_balances.json`
- `e45381e3ff854d8915ce` | files=3 | nested_variants=3 | limited_files=0 | example=`research/case-binance-2026/evidence/binance14_all_receivers_census_v1/step68_elliptic_address_crosswalk_v1/manifest.json`
- `ea12db414f853e5b3e0c` | files=3 | nested_variants=3 | limited_files=0 | example=`research/case-binance-2026/evidence/eg08_plasma_post_delivery_v1/manifest.json`
- `806be9ab4b17c3f29e48` | files=3 | nested_variants=2 | limited_files=1 | example=`research/case-binance-2026/evidence/eg08_plasma_post_delivery_v1/step05a_withdrawal_anomaly_reconciliation_v1/withdrawal_block.json`
- `7a5080f54daf16cd6b03` | files=3 | nested_variants=1 | limited_files=1 | example=`research/case-binance-2026/evidence/binance14_all_receivers_census_v1/standard_transfer_logs_raw.json`
- `381b6b67d3ac9bef1e20` | files=2 | nested_variants=2 | limited_files=0 | example=`research/case-binance-2026/evidence/eg08_plasma_post_delivery_v1/step06f_withdrawal_revert_diagnostics_v1/comparison.json`
- `74e4873948a5ba59fb3a` | files=2 | nested_variants=2 | limited_files=0 | example=`research/case-binance-2026/evidence/eg08_source_attribution_v1/step08m_source_message_lookup_v1/api_raw_responses.json`
- `de9968f3349f198d864f` | files=2 | nested_variants=2 | limited_files=1 | example=`research/case-binance-2026/analysis/master_flow_map_v1/EDGE_REGISTER_V1.csv`
- `ecb98c5df4e30840026d` | files=2 | nested_variants=2 | limited_files=0 | example=`research/case-binance-2026/evidence/eg02_central_post_blacklist_ledger_v1/manifest.json`
- `f5f1484ce507b70f9882` | files=2 | nested_variants=2 | limited_files=1 | example=`research/case-binance-2026/evidence/binance14_all_receivers_census_v1/step66_receiver_identity_rpc_audit_v1/RECEIVER_IDENTITY_REGISTER_V1.csv`
- `3059040a4a50ed51392b` | files=2 | nested_variants=1 | limited_files=1 | example=`research/case-binance-2026/A97B/evidence/bitquery_independent_crosscheck_v1/ETH_TX_TRANSFERS_BATCH5_RAW_V1.json`
- `382c0c5ba13fe766cbfa` | files=2 | nested_variants=1 | limited_files=2 | example=`research/case-binance-2026/evidence/eg08_source_attribution_v1/step08j_address_a_complete_window_v1/a_events.json`
- `6c927a770131fc1944c3` | files=2 | nested_variants=1 | limited_files=1 | example=`research/case-binance-2026/A97B/evidence/step70_bitquery_ledger_reconciliation_v1/bitquery_a97b_outgoing.json`
- `d908c7c167d77f031228` | files=2 | nested_variants=1 | limited_files=2 | example=`research/case-binance-2026/evidence/eg08_source_attribution_v1/step08f_earlier_10000_blocks_v1/scan_coverage.json`
- `f5078a337cab6a5fdcab` | files=2 | nested_variants=1 | limited_files=2 | example=`research/case-binance-2026/evidence/exploiter16_token_provenance_v1/step16_receipt_evidence_v1/e16_aave.json`
- `030b85ef7589a13255f8` | files=1 | nested_variants=1 | limited_files=1 | example=`research/case-binance-2026/A97B/evidence/bitquery_independent_audit_v1/FINAL_INTEGRITY_AUDIT_V2.json`
- `040a9963c3a9ff6d3e38` | files=1 | nested_variants=1 | limited_files=1 | example=`research/case-binance-2026/evidence/step71_55m_source_audit_v1/por_crosswalk_matches.json`
- `39511f836226822562ea` | files=1 | nested_variants=1 | limited_files=1 | example=`research/case-binance-2026/evidence/binance14_all_receivers_census_v1/step66_receiver_identity_rpc_audit_v1/transaction_receipt_block_evidence.json`
- `3b5588f15276e85313fa` | files=1 | nested_variants=1 | limited_files=1 | example=`research/case-binance-2026/evidence/eg08_plasma_post_delivery_v1/step07d_final_evidence_consistency_audit_v1/summary.json`
- `4b0b149b6bb27d0c8f79` | files=1 | nested_variants=1 | limited_files=1 | example=`research/case-binance-2026/A97B/evidence/bitquery_independent_audit_v1/manifest.json`
- `4dbd768d802cf4d4451a` | files=1 | nested_variants=1 | limited_files=1 | example=`research/case-binance-2026/GATE_2_ETH_T02_AUTHORIZATION_REPLAY_V1.json`
- `4f80d0d6bcfcca5e1146` | files=1 | nested_variants=1 | limited_files=1 | example=`research/case-binance-2026/evidence/second_hop_receipts_v1/manifest.json`
- `6758bfec0c58d55e5e3a` | files=1 | nested_variants=1 | limited_files=1 | example=`research/case-binance-2026/evidence/binance14_all_receivers_census_v1/step72_a97b_pattern_funding_audit_v1/repeat_destination_patterns.json`
- `6f542bbc14c2be044eb8` | files=1 | nested_variants=1 | limited_files=1 | example=`research/case-binance-2026/evidence/binance14_all_receivers_census_v1/step79_a97b_repeat_swap_validation_v1/sample_results.json`
- `76ccffac8d641f2a36a8` | files=1 | nested_variants=1 | limited_files=1 | example=`research/case-binance-2026/evidence/binance14_all_receivers_census_v1/alchemy_asset_transfers_raw.json`
- `83465f3a3d8b482ab6cc` | files=1 | nested_variants=1 | limited_files=1 | example=`research/case-binance-2026/evidence/eg08_plasma_post_delivery_v1/step06b_aave_withdraw_callpath_v1/withdrawal_call_trace.json`
- `8866b4c9e03e4e14ab96` | files=1 | nested_variants=1 | limited_files=1 | example=`research/case-binance-2026/evidence/binance14_all_receivers_census_v1/step73_a97b_execution_conservation_v1/execution_pattern_samples.json`
- `8bcbf0367971cee14d9d` | files=1 | nested_variants=1 | limited_files=1 | example=`research/case-binance-2026/evidence/binance14_all_receivers_census_v1/step85_a97b_final_event_audit_v1/summary.json`
- `9147fb68e4bd6a37295c` | files=1 | nested_variants=1 | limited_files=1 | example=`research/case-binance-2026/evidence/second_hop_usdt_v1/transfer_logs.json`
- `91d554b6b7ae68b51268` | files=1 | nested_variants=1 | limited_files=1 | example=`research/case-binance-2026/GATE_2_ETH_T03_TRANSFER_EVENT_AUDIT_V1.json`
- `976b350c1411a2dc8515` | files=1 | nested_variants=1 | limited_files=1 | example=`research/case-binance-2026/evidence/eg08_source_attribution_v1/step08k_adapter_inbound_receipts_v1/raw_rpc_evidence.json`
- `b75159830bcf37cd1795` | files=1 | nested_variants=1 | limited_files=1 | example=`research/case-binance-2026/evidence/eg08_source_attribution_v1/step08w_incident_attribution_crosswalk_v1/existing_evidence_index.json`
- `e8b3ca23d8a6ff63f056` | files=1 | nested_variants=1 | limited_files=1 | example=`research/case-binance-2026/evidence/eg08_plasma_post_delivery_v1/step06a_issuer_freeze_capability_audit_v1/event_scan_summary.json`
- `ee8de910d08a066789e2` | files=1 | nested_variants=1 | limited_files=1 | example=`research/case-binance-2026/GATE_2_ETH_T02_SIGNATURE_RECOVERY_V1.json`
- `f33e281502bff84ee87d` | files=1 | nested_variants=1 | limited_files=1 | example=`research/case-binance-2026/evidence/initial_tx_v1/call_trace.json`

## Document exceptions

- `research/case-binance-2026/700M_FIRST_HOP_DISTRIBUTION_AUDIT_V1.md` | CONTENT_OR_PROVENANCE_REVIEW | EVIDENCE_RELATED_DOCUMENT_CANDIDATE
- `research/case-binance-2026/A97B/A97B_RESEARCH_MASTER.md` | CONTENT_OR_PROVENANCE_REVIEW | EVIDENCE_RELATED_DOCUMENT_CANDIDATE
- `research/case-binance-2026/A97B/A97B_RESEARCH_REPORT.md` | CONTENT_OR_PROVENANCE_REVIEW | EVIDENCE_RELATED_DOCUMENT_CANDIDATE
- `research/case-binance-2026/A97B/bitquery_withdrawal_crosswalk_v1/BITQUERY_WITHDRAWAL_CROSSWALK_V1.md` | CONTENT_OR_PROVENANCE_REVIEW | EVIDENCE_RELATED_DOCUMENT_CANDIDATE
- `research/case-binance-2026/A97B/evidence/EXTERNAL_ATTRIBUTION_V1.md` | CONTENT_OR_PROVENANCE_REVIEW | EVIDENCE_RELATED_DOCUMENT_CANDIDATE
- `research/case-binance-2026/A97B/evidence/binance_official.pdf` | CONTENT_OR_PROVENANCE_REVIEW | PDF_DOCUMENT
- `research/case-binance-2026/A97B/evidence/bitquery_independent_audit_v1/README.md` | CONTENT_OR_PROVENANCE_REVIEW | EVIDENCE_RELATED_DOCUMENT_CANDIDATE
- `research/case-binance-2026/A97B/evidence/bitquery_independent_crosscheck_v2/AUDIT.md` | CONTENT_OR_PROVENANCE_REVIEW | EVIDENCE_RELATED_DOCUMENT_CANDIDATE
- `research/case-binance-2026/A97B/evidence/chainward_analysis.pdf` | CONTENT_OR_PROVENANCE_REVIEW | PDF_DOCUMENT
- `research/case-binance-2026/A97B/evidence/fbi_alert.pdf` | CONTENT_OR_PROVENANCE_REVIEW | PDF_DOCUMENT
- `research/case-binance-2026/A97B/evidence/step70_bitquery_ledger_reconciliation_v1/AUDIT.md` | CONTENT_OR_PROVENANCE_REVIEW | EVIDENCE_RELATED_DOCUMENT_CANDIDATE
- `research/case-binance-2026/A97B/institutional_research_packet_v1/A97B_TIMELINE_TECHNICAL_REPORT_V1.md` | CONTENT_OR_PROVENANCE_REVIEW | EVIDENCE_RELATED_DOCUMENT_CANDIDATE
- `research/case-binance-2026/A97B/institutional_research_packet_v1/HISTORICAL_PATTERN_RESEARCH_V1.md` | CONTENT_OR_PROVENANCE_REVIEW | EVIDENCE_RELATED_DOCUMENT_CANDIDATE
- `research/case-binance-2026/AXIOM_BINANCE_2026_FIXED_RESEARCH_MAP_V1.md` | CONTENT_OR_PROVENANCE_REVIEW | EVIDENCE_RELATED_DOCUMENT_CANDIDATE
- `research/case-binance-2026/AXIOM_EVIDENCE_DIFFERENCE_PROTOCOL_V1.md` | CONTENT_OR_PROVENANCE_REVIEW | EVIDENCE_RELATED_DOCUMENT_CANDIDATE
- `research/case-binance-2026/AXIOM_INCIDENT_TRACEABILITY_MASTER_V1.md` | CONTENT_OR_PROVENANCE_REVIEW | EVIDENCE_RELATED_DOCUMENT_CANDIDATE
- `research/case-binance-2026/AXIOM_INCIDENT_TRACEABILITY_MASTER_V2.md` | CONTENT_OR_PROVENANCE_REVIEW | EVIDENCE_RELATED_DOCUMENT_CANDIDATE
- `research/case-binance-2026/AXIOM_PUBLICATION_CLAIMS_AUDIT_V1.md` | CONTENT_OR_PROVENANCE_REVIEW | EVIDENCE_RELATED_DOCUMENT_CANDIDATE
- `research/case-binance-2026/BINANCE_2026_DELEGATED_WALLET_DRAIN_CASE_STUDY.md` | CONTENT_OR_PROVENANCE_REVIEW | EVIDENCE_RELATED_DOCUMENT_CANDIDATE
- `research/case-binance-2026/BINANCE_2026_DELEGATED_WALLET_DRAIN_CASE_STUDY_DRAFT_V1.md` | CONTENT_OR_PROVENANCE_REVIEW | EVIDENCE_RELATED_DOCUMENT_CANDIDATE
- `research/case-binance-2026/BINANCE_2026_DELEGATED_WALLET_DRAIN_CASE_STUDY_DRAFT_V2.md` | CONTENT_OR_PROVENANCE_REVIEW | EVIDENCE_RELATED_DOCUMENT_CANDIDATE
- `research/case-binance-2026/BINANCE_2026_DELEGATED_WALLET_DRAIN_CASE_STUDY_DRAFT_V3.md` | CONTENT_OR_PROVENANCE_REVIEW | EVIDENCE_RELATED_DOCUMENT_CANDIDATE
- `research/case-binance-2026/BLACKLIST_175M_CASE_AUDIT_V1.md` | CONTENT_OR_PROVENANCE_REVIEW | EVIDENCE_RELATED_DOCUMENT_CANDIDATE
- `research/case-binance-2026/EG01_EXECUTION_TIME_AUDIT_V1.md` | CONTENT_OR_PROVENANCE_REVIEW | EVIDENCE_RELATED_DOCUMENT_CANDIDATE
- `research/case-binance-2026/EG08_AAVE_POSITION_ATTRIBUTION_CORRECTION_V1.md` | UNRESOLVED_ROLE | UNRESOLVED_DOCUMENT_ROLE
- `research/case-binance-2026/EVIDENCE_CHECKPOINT_V1.md` | CONTENT_OR_PROVENANCE_REVIEW | EVIDENCE_RELATED_DOCUMENT_CANDIDATE
- `research/case-binance-2026/EVIDENCE_GAP_REPORT.md` | CONTENT_OR_PROVENANCE_REVIEW | EVIDENCE_RELATED_DOCUMENT_CANDIDATE
- `research/case-binance-2026/GATE_1_COMPLETENESS_REVIEW_V1.md` | CONTENT_OR_PROVENANCE_REVIEW | EVIDENCE_RELATED_DOCUMENT_CANDIDATE
- `research/case-binance-2026/GATE_2_175M_PATH_CONTINUITY_AUDIT_V1.md` | CONTENT_OR_PROVENANCE_REVIEW | EVIDENCE_RELATED_DOCUMENT_CANDIDATE
- `research/case-binance-2026/GATE_2_ADDITIONAL_SOURCE_ROLE_REVIEW_V1.md` | UNRESOLVED_ROLE | UNRESOLVED_DOCUMENT_ROLE
- `research/case-binance-2026/GATE_2_BTC_ATTRIBUTION_ASSESSMENT_V1.md` | CONTENT_OR_PROVENANCE_REVIEW | EVIDENCE_RELATED_DOCUMENT_CANDIDATE
- `research/case-binance-2026/GATE_2_ERC20_TRANSFER_AUDIT_V1.md` | CONTENT_OR_PROVENANCE_REVIEW | EVIDENCE_RELATED_DOCUMENT_CANDIDATE
- `research/case-binance-2026/GATE_2_ETH_DELEGATION_CONTRACT_LINK_V1.md` | CONTENT_OR_PROVENANCE_REVIEW | EVIDENCE_RELATED_DOCUMENT_CANDIDATE
- `research/case-binance-2026/GATE_2_ETH_EXTERNAL_INCIDENT_LINK_V1.md` | CONTENT_OR_PROVENANCE_REVIEW | EVIDENCE_RELATED_DOCUMENT_CANDIDATE
- `research/case-binance-2026/GATE_2_ETH_HISTORICAL_RECONCILIATION_V1.md` | CONTENT_OR_PROVENANCE_REVIEW | EVIDENCE_RELATED_DOCUMENT_CANDIDATE
- `research/case-binance-2026/GATE_2_ETH_T02_T03_MECHANISM_REVIEW_V1.md` | CONTENT_OR_PROVENANCE_REVIEW | EVIDENCE_RELATED_DOCUMENT_CANDIDATE
- `research/case-binance-2026/GATE_2_ETH_T03_CALLER_RESTRICTION_V1.md` | UNRESOLVED_ROLE | UNRESOLVED_DOCUMENT_ROLE
- `research/case-binance-2026/GATE_2_ETH_TECHNICAL_EVIDENCE_ASSESSMENT_V1.md` | CONTENT_OR_PROVENANCE_REVIEW | EVIDENCE_RELATED_DOCUMENT_CANDIDATE
- `research/case-binance-2026/GATE_2_EXPANSION_AUDIT_V1.md` | CONTENT_OR_PROVENANCE_REVIEW | EVIDENCE_RELATED_DOCUMENT_CANDIDATE
- `research/case-binance-2026/GATE_2_EXTERNAL_TXID_CROSSCHECK_V1.md` | CONTENT_OR_PROVENANCE_REVIEW | EVIDENCE_RELATED_DOCUMENT_CANDIDATE
- `research/case-binance-2026/GATE_2_INCIDENT_ATTRIBUTION_REVIEW_V1.md` | UNRESOLVED_ROLE | UNRESOLVED_DOCUMENT_ROLE
- `research/case-binance-2026/GATE_2_INITIAL_ATTRIBUTION_AUDIT_V1.md` | CONTENT_OR_PROVENANCE_REVIEW | EVIDENCE_RELATED_DOCUMENT_CANDIDATE
- `research/case-binance-2026/GATE_2_MULTICHAIN_DISCOVERY_AUDIT_V1.md` | CONTENT_OR_PROVENANCE_REVIEW | EVIDENCE_RELATED_DOCUMENT_CANDIDATE
- `research/case-binance-2026/GATE_2_TX_CONTEXT_REVIEW_V1.md` | CONTENT_OR_PROVENANCE_REVIEW | EVIDENCE_RELATED_DOCUMENT_CANDIDATE
- `research/case-binance-2026/GATE_2_XRPL_FIVE_SOURCE_AUDIT_V1.md` | CONTENT_OR_PROVENANCE_REVIEW | EVIDENCE_RELATED_DOCUMENT_CANDIDATE
- `research/case-binance-2026/GATE_3_T03_TO_700M_LINKAGE_AUDIT_V1.md` | CONTENT_OR_PROVENANCE_REVIEW | EVIDENCE_RELATED_DOCUMENT_CANDIDATE
- `research/case-binance-2026/INCIDENT_FUND_ATTRIBUTION_CHECKPOINT_2026-11-05.md` | CONTENT_OR_PROVENANCE_REVIEW | EVIDENCE_RELATED_DOCUMENT_CANDIDATE
- `research/case-binance-2026/INCIDENT_WIDE_RESEARCH_FRAMEWORK_V1.md` | CONTENT_OR_PROVENANCE_REVIEW | EVIDENCE_RELATED_DOCUMENT_CANDIDATE
- `research/case-binance-2026/INTERIM_TIMELINE_V1.md` | CONTENT_OR_PROVENANCE_REVIEW | EVIDENCE_RELATED_DOCUMENT_CANDIDATE
- `research/case-binance-2026/INTERIM_TIMELINE_V2.md` | CONTENT_OR_PROVENANCE_REVIEW | EVIDENCE_RELATED_DOCUMENT_CANDIDATE
- `research/case-binance-2026/OFFICIAL_SOURCE_VERIFICATION_V1.md` | CONTENT_OR_PROVENANCE_REVIEW | EVIDENCE_RELATED_DOCUMENT_CANDIDATE
- `research/case-binance-2026/USDT_FREEZE_BALANCE_AUDIT_V3.md` | CONTENT_OR_PROVENANCE_REVIEW | EVIDENCE_RELATED_DOCUMENT_CANDIDATE
- `research/case-binance-2026/USDT_FREEZE_TIMELINE_CHECKPOINT_V4.md` | CONTENT_OR_PROVENANCE_REVIEW | EVIDENCE_RELATED_DOCUMENT_CANDIDATE
- `research/case-binance-2026/USDT_FUND_FLOW_AND_FREEZE_V2.md` | CONTENT_OR_PROVENANCE_REVIEW | EVIDENCE_RELATED_DOCUMENT_CANDIDATE
- `research/case-binance-2026/analysis/master_timeline_v0/BINANCE14_INSTITUTIONAL_TIMELINE_V1.html` | CONTENT_OR_PROVENANCE_REVIEW | PRESENTATION_OR_EMBEDDED_DATA
- `research/case-binance-2026/analysis/master_timeline_v0/BINANCE14_MASTER_FLOW_MAP_V1.html` | CONTENT_OR_PROVENANCE_REVIEW | PRESENTATION_OR_EMBEDDED_DATA
- `research/case-binance-2026/analysis/master_timeline_v0/BINANCE14_TIMELINE_V0.html` | CONTENT_OR_PROVENANCE_REVIEW | PRESENTATION_OR_EMBEDDED_DATA
- `research/case-binance-2026/evidence/binance14_all_receivers_census_v1/README.md` | UNRESOLVED_ROLE | UNRESOLVED_DOCUMENT_ROLE
- `research/case-binance-2026/evidence/binance14_all_receivers_census_v1/step66_receiver_identity_rpc_audit_v1/audit.md` | CONTENT_OR_PROVENANCE_REVIEW | EVIDENCE_RELATED_DOCUMENT_CANDIDATE
- `research/case-binance-2026/evidence/binance14_all_receivers_census_v1/step83_official_attribution_crosswalk_v1/source_snapshots/elliptic_source.txt` | UNRESOLVED_ROLE | UNRESOLVED_DOCUMENT_ROLE
- `research/case-binance-2026/evidence/binance14_all_receivers_census_v1/step83_official_attribution_crosswalk_v1/source_snapshots/fbi_eth_addresses.txt` | UNRESOLVED_ROLE | UNRESOLVED_DOCUMENT_ROLE
- `research/case-binance-2026/evidence/binance14_all_receivers_census_v1/step85_a97b_final_event_audit_v1/A97B_FINAL_EVENT_AUDIT_V1.md` | CONTENT_OR_PROVENANCE_REVIEW | EVIDENCE_RELATED_DOCUMENT_CANDIDATE
- `research/case-binance-2026/evidence/eg05_kite_historical_pause_v1/audit.md` | CONTENT_OR_PROVENANCE_REVIEW | EVIDENCE_RELATED_DOCUMENT_CANDIDATE
- `research/case-binance-2026/evidence/eg08_plasma_post_delivery_v1/step06f_withdrawal_revert_diagnostics_v1/anvil.log` | UNRESOLVED_ROLE | UNRESOLVED_DOCUMENT_ROLE
- `research/case-binance-2026/evidence/exploiter16_token_provenance_v1/STEP07B_12_AUDIT_CHECKPOINT.md` | CONTENT_OR_PROVENANCE_REVIEW | EVIDENCE_RELATED_DOCUMENT_CANDIDATE
- `research/case-binance-2026/evidence/official_announcements/BINANCE_OFFICIAL_UPDATE_1_BROWSER_CAPTURE.txt` | CONTENT_OR_PROVENANCE_REVIEW | EVIDENCE_RELATED_DOCUMENT_CANDIDATE
- `research/case-binance-2026/evidence/official_announcements/BINANCE_OFFICIAL_UPDATE_2_BROWSER_CAPTURE.txt` | CONTENT_OR_PROVENANCE_REVIEW | EVIDENCE_RELATED_DOCUMENT_CANDIDATE
- `research/case-binance-2026/evidence/step72_external_attribution_v1/BITQUERY.html` | CONTENT_OR_PROVENANCE_REVIEW | PRESENTATION_OR_EMBEDDED_DATA
- `research/case-binance-2026/evidence/step72_external_attribution_v1/IMD.html` | CONTENT_OR_PROVENANCE_REVIEW | PRESENTATION_OR_EMBEDDED_DATA
- `research/case-binance-2026/publication_staging/a97b-visual-report/README.md` | CONTENT_OR_PROVENANCE_REVIEW | EVIDENCE_RELATED_DOCUMENT_CANDIDATE

## Limitations

- Signature variation is a review signal, not proof of distinct transfer schemas.
- Identical sampled signatures do not prove exhaustive equivalence.
- Source roles remain provisional.
- All files are accounted for in the inventory, but full semantic coverage is not yet verified.
- Phase 1 is not complete.
