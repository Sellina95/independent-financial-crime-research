# Phase 1 — Structural Evidence Review

Source commit: `bba74a5c89f830193999d8aef051349161dccf4e`
Files reviewed: 3105

## Preliminary evidence roles

- TRANSACTION_ENVELOPE_CANDIDATE: 1281
- TRANSFER_SHAPED_CANDIDATE: 1254
- UNKNOWN_DATA_ROLE: 179
- AUDIT_OR_DERIVED_CANDIDATE: 176
- MANIFEST_OR_INTEGRITY: 85
- DOCUMENT_OR_PRESENTATION: 78
- RAW_SOURCE_CANDIDATE: 33
- DOCUMENT_OR_MEDIA: 11
- CODE_OR_CONFIGURATION: 8

## Largest top-level schema families

- c59b37e963fa3c09a78f | 2241 files | AUDIT_OR_DERIVED_CANDIDATE | example: `research/case-binance-2026/evidence/binance14_all_receivers_census_v1/step72_a97b_pattern_funding_audit_v1/rpc_cache/balance_26301443.json`
- 1485ca01a3e37dfcf221 | 149 files | TRANSACTION_ENVELOPE_CANDIDATE | example: `research/case-binance-2026/A97B/integrated_event_audit_v1/recovered_receipts/0x0003cf5d3cffc1fde2a370f577571230112177a8a38da8bcd312b4525b6e4253.json`
- 9d4220dec04a9cef0e22 | 30 files | UNKNOWN_DATA_ROLE | example: `research/case-binance-2026/evidence/eg03_two_address_consolidation_v1/balance_A_26306503.json`
- 550daf37753235a3af66 | 24 files | MANIFEST_OR_INTEGRITY | example: `research/case-binance-2026/evidence/eg08_plasma_post_delivery_v1/step06b_issuer_control_simulation_v1/manifest.json`
- c8b20c0308a921c00a99 | 23 files | TRANSFER_SHAPED_CANDIDATE | example: `research/case-binance-2026/A97B/eth_address_receipts_v1/pages/page_0001.json`
- 70897b228dc129d6a0d9 | 23 files | AUDIT_OR_DERIVED_CANDIDATE | example: `research/case-binance-2026/evidence/central_blacklist_audit_v1/balance_block_26300953.json`
- 2dff4c4b25493fa7ffb2 | 22 files | TRANSFER_SHAPED_CANDIDATE | example: `research/case-binance-2026/evidence/binance14_all_receivers_census_v1/step69_noncentral_receiver_forward_screen_v1/raw/0x139b920004360b08a1e285ba3859771eb0470ce9.json`
- 24692d235b0ec9a64ecb | 21 files | AUDIT_OR_DERIVED_CANDIDATE | example: `research/case-binance-2026/A97B/evidence/bitquery_independent_audit_v1/batch_001.json`
- 9b01d174809ea9feeeb8 | 20 files | TRANSFER_SHAPED_CANDIDATE | example: `research/case-binance-2026/evidence/30m_upstream_bridge_v1/130m_transaction.json`
- 309b4d086e7fd4a1f72d | 12 files | TRANSFER_SHAPED_CANDIDATE | example: `research/case-binance-2026/evidence/binance14_all_receivers_census_v1/step70_a97b_forward_census_v1/pages/page_0001.json`
- f620ee3efc63fc043ebd | 12 files | TRANSFER_SHAPED_CANDIDATE | example: `research/case-binance-2026/evidence/binance14_all_receivers_census_v1/step72_a97b_pattern_funding_audit_v1/rpc_cache/incoming_eth_page_0001.json`
- 21f44ce4b60e14b8d9bb | 12 files | TRANSFER_SHAPED_CANDIDATE | example: `research/case-binance-2026/evidence/eg08_source_attribution_v1/step08o_multichain_funding_window_v1/chain_events.json`
- 3c186caf63b51c59b923 | 10 files | UNKNOWN_DATA_ROLE | example: `research/case-binance-2026/evidence/step76_preincident_inbound_v1/chunks/chunk_26250512_26250611.json`
- f7b82dc469849c9602cd | 9 files | RAW_SOURCE_CANDIDATE | example: `research/case-binance-2026/A97B/evidence/bitquery_independent_crosscheck_v1/ETH_TX_EVENTS_BATCH5_RAW_V1.json`
- b595830007221f4e7ec0 | 6 files | UNKNOWN_DATA_ROLE | example: `research/case-binance-2026/evidence/binance14_all_receivers_census_v1/step80_a97b_full_dex_census_v1/batches/batch_0001.json`
- cb92dd8102afa7783fd9 | 6 files | AUDIT_OR_DERIVED_CANDIDATE | example: `research/case-binance-2026/evidence/eg08_plasma_post_delivery_v1/step06a_issuer_freeze_capability_audit_v1/raw_event_logs.jsonl`
- 1eaf24eaf19cf4db9536 | 5 files | TRANSFER_SHAPED_CANDIDATE | example: `research/case-binance-2026/evidence/binance14_all_receivers_census_v1/step67_internal_eth_trace_audit_v1/blockscout_crosscheck_v1/transactions/0x31c4c9fe287d54fb9d3b79980477a8c793a11f774b98d0a9a92de1dad888a91d.json`
- 31f1657957a388a00ee2 | 4 files | TRANSFER_SHAPED_CANDIDATE | example: `research/case-binance-2026/evidence/exploiter16_token_provenance_v1/step18g_four_route_evidence_v1/aave_main.json`
- 7a5080f54daf16cd6b03 | 3 files | RAW_SOURCE_CANDIDATE | example: `research/case-binance-2026/evidence/binance14_all_receivers_census_v1/standard_transfer_logs_raw.json`
- e45381e3ff854d8915ce | 3 files | MANIFEST_OR_INTEGRITY | example: `research/case-binance-2026/evidence/binance14_all_receivers_census_v1/step68_elliptic_address_crosswalk_v1/manifest.json`
- ea12db414f853e5b3e0c | 3 files | MANIFEST_OR_INTEGRITY | example: `research/case-binance-2026/evidence/eg08_plasma_post_delivery_v1/manifest.json`
- 2644190dc6f8fe8ac2ee | 3 files | RAW_SOURCE_CANDIDATE | example: `research/case-binance-2026/evidence/eg08_plasma_post_delivery_v1/step02_transfer_ledger_v1/raw_incoming_logs.jsonl`
- 806be9ab4b17c3f29e48 | 3 files | TRANSACTION_ENVELOPE_CANDIDATE | example: `research/case-binance-2026/evidence/eg08_plasma_post_delivery_v1/step05a_withdrawal_anomaly_reconciliation_v1/withdrawal_block.json`
- da49d1e9bee43da5662b | 3 files | UNKNOWN_DATA_ROLE | example: `research/case-binance-2026/evidence/eg08_plasma_post_delivery_v1/step05b_atoken_identity_reconciliation_v1/historical_balances.json`
- 51a7018d1ae663b919c8 | 3 files | UNKNOWN_DATA_ROLE | example: `research/case-binance-2026/evidence/eg08_plasma_post_delivery_v1/step06b_issuer_control_simulation_v1/blocklist_current_state.json`
- 1124bc32e43178adfdbc | 3 files | TRANSFER_SHAPED_CANDIDATE | example: `research/case-binance-2026/evidence/exploiter16_token_provenance_v1/step19f_middle_hop_receipts_v1/01_central_to_hop1.json`
- 54590a21eb7a522bf479 | 2 files | AUDIT_OR_DERIVED_CANDIDATE | example: `research/case-binance-2026/A97B/dex_transfer_sequence_audit_v1/SEQUENCE_EXCEPTIONS_V1.csv`
- 86ab8d8c02cd7472e536 | 2 files | RAW_SOURCE_CANDIDATE | example: `research/case-binance-2026/A97B/eth_address_receipts_v1/A97B_ADDRESS_ETH_RETURN_V1.csv`
- 3059040a4a50ed51392b | 2 files | RAW_SOURCE_CANDIDATE | example: `research/case-binance-2026/A97B/evidence/bitquery_independent_crosscheck_v1/ETH_TX_TRANSFERS_BATCH5_RAW_V1.json`
- 6c927a770131fc1944c3 | 2 files | UNKNOWN_DATA_ROLE | example: `research/case-binance-2026/A97B/evidence/step70_bitquery_ledger_reconciliation_v1/bitquery_a97b_outgoing.json`
- ada8e57edbf37b33763f | 2 files | TRANSFER_SHAPED_CANDIDATE | example: `research/case-binance-2026/A97B/integrated_event_audit_v1/A97B_INTEGRATED_EVENT_LEDGER_V1.csv`
- 699a9ac37d30d6ee18bd | 2 files | UNKNOWN_DATA_ROLE | example: `research/case-binance-2026/AXIOM_EVIDENCE_DIFFERENCE_REGISTER_V1.csv`
- 475598b9617d605693e6 | 2 files | UNKNOWN_DATA_ROLE | example: `research/case-binance-2026/GATE_2_INCIDENT_ATTRIBUTION_MATRIX_V1.csv`
- cc4e28254c3a1fe7d43e | 2 files | UNKNOWN_DATA_ROLE | example: `research/case-binance-2026/INCIDENT_ENTRY_POINT_REGISTER_V1.csv`
- de9968f3349f198d864f | 2 files | TRANSFER_SHAPED_CANDIDATE | example: `research/case-binance-2026/analysis/master_flow_map_v1/EDGE_REGISTER_V1.csv`
- 56dd4f419ede856e52d3 | 2 files | AUDIT_OR_DERIVED_CANDIDATE | example: `research/case-binance-2026/evidence/30m_blacklist_audit_v1/blacklist_event.json`
- f5f1484ce507b70f9882 | 2 files | AUDIT_OR_DERIVED_CANDIDATE | example: `research/case-binance-2026/evidence/binance14_all_receivers_census_v1/step66_receiver_identity_rpc_audit_v1/RECEIVER_IDENTITY_REGISTER_V1.csv`
- 0417f5841b1ebf837469 | 2 files | TRANSFER_SHAPED_CANDIDATE | example: `research/case-binance-2026/evidence/binance14_all_receivers_census_v1/step84_a97b_erc20_exception_audit_v1/erc20_53_event_register.csv`
- ecb98c5df4e30840026d | 2 files | MANIFEST_OR_INTEGRITY | example: `research/case-binance-2026/evidence/eg02_central_post_blacklist_ledger_v1/manifest.json`
- 36e65029784cc833af1d | 2 files | AUDIT_OR_DERIVED_CANDIDATE | example: `research/case-binance-2026/evidence/eg08_plasma_post_delivery_v1/step05_withdrawal_audit_v1/existing_supply_receipts.json`
- 381b6b67d3ac9bef1e20 | 2 files | RAW_SOURCE_CANDIDATE | example: `research/case-binance-2026/evidence/eg08_plasma_post_delivery_v1/step06f_withdrawal_revert_diagnostics_v1/comparison.json`
- 0702d2e66f8e87c4848b | 2 files | TRANSFER_SHAPED_CANDIDATE | example: `research/case-binance-2026/evidence/eg08_source_attribution_v1/step08e_upstream_3000_blocks_v1/events.json`
- 97f76a93674921113786 | 2 files | UNKNOWN_DATA_ROLE | example: `research/case-binance-2026/evidence/eg08_source_attribution_v1/step08f_earlier_10000_blocks_v1/inbound_sources.json`
- d908c7c167d77f031228 | 2 files | UNKNOWN_DATA_ROLE | example: `research/case-binance-2026/evidence/eg08_source_attribution_v1/step08f_earlier_10000_blocks_v1/scan_coverage.json`
- 382c0c5ba13fe766cbfa | 2 files | TRANSFER_SHAPED_CANDIDATE | example: `research/case-binance-2026/evidence/eg08_source_attribution_v1/step08j_address_a_complete_window_v1/a_events.json`
- 74e4873948a5ba59fb3a | 2 files | RAW_SOURCE_CANDIDATE | example: `research/case-binance-2026/evidence/eg08_source_attribution_v1/step08m_source_message_lookup_v1/api_raw_responses.json`
- f5078a337cab6a5fdcab | 2 files | TRANSFER_SHAPED_CANDIDATE | example: `research/case-binance-2026/evidence/exploiter16_token_provenance_v1/step16_receipt_evidence_v1/e16_aave.json`
- e369aedb967d9fa2b89e | 1 files | RAW_SOURCE_CANDIDATE | example: `research/case-binance-2026/A97B/bitquery_withdrawal_crosswalk_v1/A97B_DIRECT_ETH_WITHDRAWAL_CROSSWALK_V1.csv`
- 84ed7911201bfc694879 | 1 files | AUDIT_OR_DERIVED_CANDIDATE | example: `research/case-binance-2026/A97B/bitquery_withdrawal_crosswalk_v1/AUDIT_V1.json`
- b001f98c1d6e62f48701 | 1 files | AUDIT_OR_DERIVED_CANDIDATE | example: `research/case-binance-2026/A97B/dex_execution_reconstruction_v1/AUDIT_V1.json`
- 7f8579d3062f85d30a3f | 1 files | UNKNOWN_DATA_ROLE | example: `research/case-binance-2026/A97B/dex_execution_reconstruction_v1/DEX_EXECUTION_TIMELINE_V1.csv`
- 2f24a3427f90f7cd238f | 1 files | AUDIT_OR_DERIVED_CANDIDATE | example: `research/case-binance-2026/A97B/dex_external_screening_v1/AUDIT_V1.json`
- b9c4c7cfab7e296c6e30 | 1 files | UNKNOWN_DATA_ROLE | example: `research/case-binance-2026/A97B/dex_external_screening_v1/DEX_ADDRESS_EXTERNAL_LISTING_V1.csv`
- f828dc4fd752e0b43141 | 1 files | AUDIT_OR_DERIVED_CANDIDATE | example: `research/case-binance-2026/A97B/dex_internal_trace_v1/AUDIT_V1.json`
- 83e3da375dbd10c65f7c | 1 files | TRANSFER_SHAPED_CANDIDATE | example: `research/case-binance-2026/A97B/dex_internal_trace_v1/DEX_ALL_TOKEN_TRANSFERS_V1.csv`
- 251cb3f9ca81ecac2bdc | 1 files | UNKNOWN_DATA_ROLE | example: `research/case-binance-2026/A97B/dex_internal_trace_v1/DEX_SWAP_EVENT_CANDIDATES_V1.csv`
- ac8e7ab6022d0c41be17 | 1 files | AUDIT_OR_DERIVED_CANDIDATE | example: `research/case-binance-2026/A97B/dex_internal_trace_v1/DEX_TRANSACTION_TRACE_SUMMARY_V1.csv`
- b4a927e0b23828fccca1 | 1 files | AUDIT_OR_DERIVED_CANDIDATE | example: `research/case-binance-2026/A97B/dex_route_mechanism_v1/AUDIT_V1.json`
- 5b45350a5fa4f6657594 | 1 files | UNKNOWN_DATA_ROLE | example: `research/case-binance-2026/A97B/dex_route_mechanism_v1/DEX_MECHANISM_TIMELINE_V1.csv`
- ede65d168cf306cf692b | 1 files | UNKNOWN_DATA_ROLE | example: `research/case-binance-2026/A97B/dex_route_mechanism_v1/WETH_RECEIVER_RANKING_V1.csv`

## Audit limitations

- Roles are structurally inferred, not source-verified.
- Top-level schemas are grouped; nested coverage is not proven.
- Sampled nested schemas still require targeted inspection.
- Unsupported documents/media require separate review.
- No atomic transfer or final graph-edge count is claimed.

## Next verification gates

- [ ] Verify source-provider provenance
- [ ] Verify raw versus derived lineage
- [ ] Analyze relevant nested schema variants
- [ ] Complete document and unsupported-format review
- [ ] Confirm per-file final dispositions
