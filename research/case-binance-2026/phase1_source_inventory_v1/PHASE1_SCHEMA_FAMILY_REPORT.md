# Phase 1 — Schema Family Inspection

Source commit: `bba74a5c89f830193999d8aef051349161dccf4e`
Total source files: 3105
Top-level schema families: 355

This is representative inspection, not exhaustive validation.
A top-level schema match does not guarantee identical nested records.

## Schema families

### c59b37e963fa3c09a78f — 2241 files
- Representative: `research/case-binance-2026/evidence/binance14_all_receivers_census_v1/step72_a97b_pattern_funding_audit_v1/rpc_cache/balance_26301443.json`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 17, 'TRANSFER_SHAPED_CANDIDATE': 1112, 'TRANSACTION_ENVELOPE_CANDIDATE': 1112}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 3
- Evidence role verified: NO

### 1485ca01a3e37dfcf221 — 149 files
- Representative: `research/case-binance-2026/A97B/integrated_event_audit_v1/recovered_receipts/0x0003cf5d3cffc1fde2a370f577571230112177a8a38da8bcd312b4525b6e4253.json`
- Candidate roles: {'TRANSACTION_ENVELOPE_CANDIDATE': 149}
- Field hints: {'tx_hash': True, 'from': True, 'to': True, 'amount': False, 'log_index': True, 'trace': False, 'token': False, 'events': True}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 24
- Evidence role verified: NO

### 9d4220dec04a9cef0e22 — 30 files
- Representative: `research/case-binance-2026/evidence/eg03_two_address_consolidation_v1/balance_A_26306503.json`
- Candidate roles: {'UNKNOWN_DATA_ROLE': 16, 'TRANSACTION_ENVELOPE_CANDIDATE': 10, 'TRANSFER_SHAPED_CANDIDATE': 4}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 3
- Evidence role verified: NO

### 550daf37753235a3af66 — 24 files
- Representative: `research/case-binance-2026/evidence/eg08_plasma_post_delivery_v1/step06b_issuer_control_simulation_v1/manifest.json`
- Candidate roles: {'MANIFEST_OR_INTEGRITY': 24}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 8
- Evidence role verified: NO

### 70897b228dc129d6a0d9 — 23 files
- Representative: `research/case-binance-2026/evidence/central_blacklist_audit_v1/balance_block_26300953.json`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 5, 'TRANSACTION_ENVELOPE_CANDIDATE': 5, 'TRANSFER_SHAPED_CANDIDATE': 1, 'UNKNOWN_DATA_ROLE': 12}
- Field hints: {'tx_hash': False, 'from': False, 'to': True, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 13
- Evidence role verified: NO

### c8b20c0308a921c00a99 — 23 files
- Representative: `research/case-binance-2026/A97B/eth_address_receipts_v1/pages/page_0001.json`
- Candidate roles: {'TRANSFER_SHAPED_CANDIDATE': 23}
- Field hints: {'tx_hash': True, 'from': True, 'to': True, 'amount': True, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: True
- Inspection error: None
- Nested field paths: 69
- Evidence role verified: NO

### 2dff4c4b25493fa7ffb2 — 22 files
- Representative: `research/case-binance-2026/evidence/binance14_all_receivers_census_v1/step69_noncentral_receiver_forward_screen_v1/raw/0x139b920004360b08a1e285ba3859771eb0470ce9.json`
- Candidate roles: {'TRANSFER_SHAPED_CANDIDATE': 16, 'RAW_SOURCE_CANDIDATE': 6}
- Field hints: {'tx_hash': True, 'from': True, 'to': True, 'amount': True, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: True
- Inspection error: None
- Nested field paths: 25
- Evidence role verified: NO

### 24692d235b0ec9a64ecb — 21 files
- Representative: `research/case-binance-2026/A97B/evidence/bitquery_independent_audit_v1/batch_001.json`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 21}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: True
- Inspection error: None
- Nested field paths: 5
- Evidence role verified: NO

### 9b01d174809ea9feeeb8 — 20 files
- Representative: `research/case-binance-2026/evidence/30m_upstream_bridge_v1/130m_transaction.json`
- Candidate roles: {'TRANSFER_SHAPED_CANDIDATE': 20}
- Field hints: {'tx_hash': True, 'from': True, 'to': True, 'amount': True, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 21
- Evidence role verified: NO

### 21f44ce4b60e14b8d9bb — 12 files
- Representative: `research/case-binance-2026/evidence/eg08_source_attribution_v1/step08o_multichain_funding_window_v1/chain_events.json`
- Candidate roles: {'TRANSFER_SHAPED_CANDIDATE': 3, 'UNKNOWN_DATA_ROLE': 5, 'RAW_SOURCE_CANDIDATE': 1, 'AUDIT_OR_DERIVED_CANDIDATE': 3}
- Field hints: {'tx_hash': False, 'from': True, 'to': True, 'amount': True, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 16
- Evidence role verified: NO

### 309b4d086e7fd4a1f72d — 12 files
- Representative: `research/case-binance-2026/evidence/binance14_all_receivers_census_v1/step70_a97b_forward_census_v1/pages/page_0001.json`
- Candidate roles: {'TRANSFER_SHAPED_CANDIDATE': 12}
- Field hints: {'tx_hash': True, 'from': True, 'to': True, 'amount': True, 'log_index': False, 'trace': False, 'token': False, 'events': True}
- Nested sample limited: True
- Inspection error: None
- Nested field paths: 21
- Evidence role verified: NO

### f620ee3efc63fc043ebd — 12 files
- Representative: `research/case-binance-2026/evidence/binance14_all_receivers_census_v1/step72_a97b_pattern_funding_audit_v1/rpc_cache/incoming_eth_page_0001.json`
- Candidate roles: {'TRANSFER_SHAPED_CANDIDATE': 12}
- Field hints: {'tx_hash': True, 'from': True, 'to': True, 'amount': True, 'log_index': False, 'trace': False, 'token': False, 'events': True}
- Nested sample limited: True
- Inspection error: None
- Nested field paths: 29
- Evidence role verified: NO

### 3c186caf63b51c59b923 — 10 files
- Representative: `research/case-binance-2026/evidence/step76_preincident_inbound_v1/chunks/chunk_26250512_26250611.json`
- Candidate roles: {'UNKNOWN_DATA_ROLE': 10}
- Field hints: {'tx_hash': True, 'from': False, 'to': False, 'amount': False, 'log_index': True, 'trace': False, 'token': False, 'events': True}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 14
- Evidence role verified: NO

### f7b82dc469849c9602cd — 9 files
- Representative: `research/case-binance-2026/A97B/evidence/bitquery_independent_crosscheck_v1/ETH_TX_EVENTS_BATCH5_RAW_V1.json`
- Candidate roles: {'RAW_SOURCE_CANDIDATE': 3, 'UNKNOWN_DATA_ROLE': 6}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': True, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: True
- Inspection error: None
- Nested field paths: 25
- Evidence role verified: NO

### b595830007221f4e7ec0 — 6 files
- Representative: `research/case-binance-2026/evidence/binance14_all_receivers_census_v1/step80_a97b_full_dex_census_v1/batches/batch_0001.json`
- Candidate roles: {'UNKNOWN_DATA_ROLE': 6}
- Field hints: {'tx_hash': True, 'from': True, 'to': True, 'amount': True, 'log_index': True, 'trace': False, 'token': False, 'events': True}
- Nested sample limited: True
- Inspection error: None
- Nested field paths: 48
- Evidence role verified: NO

### cb92dd8102afa7783fd9 — 6 files
- Representative: `research/case-binance-2026/evidence/eg08_plasma_post_delivery_v1/step06a_issuer_freeze_capability_audit_v1/raw_event_logs.jsonl`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 3, 'UNKNOWN_DATA_ROLE': 3}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 0
- Evidence role verified: NO

### 1eaf24eaf19cf4db9536 — 5 files
- Representative: `research/case-binance-2026/evidence/binance14_all_receivers_census_v1/step67_internal_eth_trace_audit_v1/blockscout_crosscheck_v1/transactions/0x31c4c9fe287d54fb9d3b79980477a8c793a11f774b98d0a9a92de1dad888a91d.json`
- Candidate roles: {'TRANSFER_SHAPED_CANDIDATE': 5}
- Field hints: {'tx_hash': True, 'from': True, 'to': True, 'amount': True, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: True
- Inspection error: None
- Nested field paths: 78
- Evidence role verified: NO

### 31f1657957a388a00ee2 — 4 files
- Representative: `research/case-binance-2026/evidence/exploiter16_token_provenance_v1/step18g_four_route_evidence_v1/aave_main.json`
- Candidate roles: {'TRANSFER_SHAPED_CANDIDATE': 4}
- Field hints: {'tx_hash': True, 'from': True, 'to': True, 'amount': True, 'log_index': True, 'trace': False, 'token': False, 'events': True}
- Nested sample limited: True
- Inspection error: None
- Nested field paths: 73
- Evidence role verified: NO

### 1124bc32e43178adfdbc — 3 files
- Representative: `research/case-binance-2026/evidence/exploiter16_token_provenance_v1/step19f_middle_hop_receipts_v1/01_central_to_hop1.json`
- Candidate roles: {'TRANSFER_SHAPED_CANDIDATE': 3}
- Field hints: {'tx_hash': True, 'from': True, 'to': True, 'amount': True, 'log_index': True, 'trace': False, 'token': False, 'events': True}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 69
- Evidence role verified: NO

### 2644190dc6f8fe8ac2ee — 3 files
- Representative: `research/case-binance-2026/evidence/eg08_plasma_post_delivery_v1/step02_transfer_ledger_v1/raw_incoming_logs.jsonl`
- Candidate roles: {'RAW_SOURCE_CANDIDATE': 2, 'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 6
- Evidence role verified: NO

### 51a7018d1ae663b919c8 — 3 files
- Representative: `research/case-binance-2026/evidence/eg08_plasma_post_delivery_v1/step06b_issuer_control_simulation_v1/blocklist_current_state.json`
- Candidate roles: {'UNKNOWN_DATA_ROLE': 3}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 16
- Evidence role verified: NO

### 7a5080f54daf16cd6b03 — 3 files
- Representative: `research/case-binance-2026/evidence/binance14_all_receivers_census_v1/standard_transfer_logs_raw.json`
- Candidate roles: {'RAW_SOURCE_CANDIDATE': 2, 'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': True, 'from': False, 'to': False, 'amount': False, 'log_index': True, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: True
- Inspection error: None
- Nested field paths: 10
- Evidence role verified: NO

### 806be9ab4b17c3f29e48 — 3 files
- Representative: `research/case-binance-2026/evidence/eg08_plasma_post_delivery_v1/step05a_withdrawal_anomaly_reconciliation_v1/withdrawal_block.json`
- Candidate roles: {'TRANSACTION_ENVELOPE_CANDIDATE': 3}
- Field hints: {'tx_hash': True, 'from': True, 'to': True, 'amount': True, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 47
- Evidence role verified: NO

### da49d1e9bee43da5662b — 3 files
- Representative: `research/case-binance-2026/evidence/eg08_plasma_post_delivery_v1/step05b_atoken_identity_reconciliation_v1/historical_balances.json`
- Candidate roles: {'UNKNOWN_DATA_ROLE': 3}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 38
- Evidence role verified: NO

### e45381e3ff854d8915ce — 3 files
- Representative: `research/case-binance-2026/evidence/binance14_all_receivers_census_v1/step68_elliptic_address_crosswalk_v1/manifest.json`
- Candidate roles: {'MANIFEST_OR_INTEGRITY': 3}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 5
- Evidence role verified: NO

### ea12db414f853e5b3e0c — 3 files
- Representative: `research/case-binance-2026/evidence/eg08_plasma_post_delivery_v1/manifest.json`
- Candidate roles: {'MANIFEST_OR_INTEGRITY': 3}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 14
- Evidence role verified: NO

### 0417f5841b1ebf837469 — 2 files
- Representative: `research/case-binance-2026/evidence/binance14_all_receivers_census_v1/step84_a97b_erc20_exception_audit_v1/erc20_53_event_register.csv`
- Candidate roles: {'TRANSFER_SHAPED_CANDIDATE': 2}
- Field hints: {'tx_hash': True, 'from': True, 'to': True, 'amount': True, 'log_index': False, 'trace': False, 'token': True, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 26
- Evidence role verified: NO

### 0702d2e66f8e87c4848b — 2 files
- Representative: `research/case-binance-2026/evidence/eg08_source_attribution_v1/step08e_upstream_3000_blocks_v1/events.json`
- Candidate roles: {'TRANSFER_SHAPED_CANDIDATE': 2}
- Field hints: {'tx_hash': False, 'from': True, 'to': True, 'amount': True, 'log_index': True, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 6
- Evidence role verified: NO

### 3059040a4a50ed51392b — 2 files
- Representative: `research/case-binance-2026/A97B/evidence/bitquery_independent_crosscheck_v1/ETH_TX_TRANSFERS_BATCH5_RAW_V1.json`
- Candidate roles: {'RAW_SOURCE_CANDIDATE': 2}
- Field hints: {'tx_hash': False, 'from': True, 'to': False, 'amount': True, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: True
- Inspection error: None
- Nested field paths: 7
- Evidence role verified: NO

### 36e65029784cc833af1d — 2 files
- Representative: `research/case-binance-2026/evidence/eg08_plasma_post_delivery_v1/step05_withdrawal_audit_v1/existing_supply_receipts.json`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 2}
- Field hints: {'tx_hash': True, 'from': True, 'to': True, 'amount': False, 'log_index': True, 'trace': False, 'token': False, 'events': True}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 26
- Evidence role verified: NO

### 381b6b67d3ac9bef1e20 — 2 files
- Representative: `research/case-binance-2026/evidence/eg08_plasma_post_delivery_v1/step06f_withdrawal_revert_diagnostics_v1/comparison.json`
- Candidate roles: {'RAW_SOURCE_CANDIDATE': 2}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 12
- Evidence role verified: NO

### 382c0c5ba13fe766cbfa — 2 files
- Representative: `research/case-binance-2026/evidence/eg08_source_attribution_v1/step08j_address_a_complete_window_v1/a_events.json`
- Candidate roles: {'TRANSFER_SHAPED_CANDIDATE': 2}
- Field hints: {'tx_hash': False, 'from': True, 'to': True, 'amount': True, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: True
- Inspection error: None
- Nested field paths: 6
- Evidence role verified: NO

### 475598b9617d605693e6 — 2 files
- Representative: `research/case-binance-2026/GATE_2_INCIDENT_ATTRIBUTION_MATRIX_V1.csv`
- Candidate roles: {'UNKNOWN_DATA_ROLE': 2}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 16
- Evidence role verified: NO

### 54590a21eb7a522bf479 — 2 files
- Representative: `research/case-binance-2026/A97B/dex_transfer_sequence_audit_v1/SEQUENCE_EXCEPTIONS_V1.csv`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 2}
- Field hints: {'tx_hash': True, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 12
- Evidence role verified: NO

### 56dd4f419ede856e52d3 — 2 files
- Representative: `research/case-binance-2026/evidence/30m_blacklist_audit_v1/blacklist_event.json`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1, 'UNKNOWN_DATA_ROLE': 1}
- Field hints: {'tx_hash': True, 'from': False, 'to': False, 'amount': False, 'log_index': True, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 10
- Evidence role verified: NO

### 699a9ac37d30d6ee18bd — 2 files
- Representative: `research/case-binance-2026/AXIOM_EVIDENCE_DIFFERENCE_REGISTER_V1.csv`
- Candidate roles: {'UNKNOWN_DATA_ROLE': 2}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 10
- Evidence role verified: NO

### 6c927a770131fc1944c3 — 2 files
- Representative: `research/case-binance-2026/A97B/evidence/step70_bitquery_ledger_reconciliation_v1/bitquery_a97b_outgoing.json`
- Candidate roles: {'UNKNOWN_DATA_ROLE': 2}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: True
- Inspection error: None
- Nested field paths: 2
- Evidence role verified: NO

### 74e4873948a5ba59fb3a — 2 files
- Representative: `research/case-binance-2026/evidence/eg08_source_attribution_v1/step08m_source_message_lookup_v1/api_raw_responses.json`
- Candidate roles: {'RAW_SOURCE_CANDIDATE': 1, 'TRANSFER_SHAPED_CANDIDATE': 1}
- Field hints: {'tx_hash': False, 'from': True, 'to': False, 'amount': True, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 345
- Evidence role verified: NO

### 86ab8d8c02cd7472e536 — 2 files
- Representative: `research/case-binance-2026/A97B/eth_address_receipts_v1/A97B_ADDRESS_ETH_RETURN_V1.csv`
- Candidate roles: {'RAW_SOURCE_CANDIDATE': 1, 'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': True, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 8
- Evidence role verified: NO

### 97f76a93674921113786 — 2 files
- Representative: `research/case-binance-2026/evidence/eg08_source_attribution_v1/step08f_earlier_10000_blocks_v1/inbound_sources.json`
- Candidate roles: {'UNKNOWN_DATA_ROLE': 2}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': True, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 3
- Evidence role verified: NO

### ada8e57edbf37b33763f — 2 files
- Representative: `research/case-binance-2026/A97B/integrated_event_audit_v1/A97B_INTEGRATED_EVENT_LEDGER_V1.csv`
- Candidate roles: {'TRANSFER_SHAPED_CANDIDATE': 2}
- Field hints: {'tx_hash': True, 'from': True, 'to': True, 'amount': True, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 18
- Evidence role verified: NO

### cc4e28254c3a1fe7d43e — 2 files
- Representative: `research/case-binance-2026/INCIDENT_ENTRY_POINT_REGISTER_V1.csv`
- Candidate roles: {'UNKNOWN_DATA_ROLE': 2}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 8
- Evidence role verified: NO

### d908c7c167d77f031228 — 2 files
- Representative: `research/case-binance-2026/evidence/eg08_source_attribution_v1/step08f_earlier_10000_blocks_v1/scan_coverage.json`
- Candidate roles: {'UNKNOWN_DATA_ROLE': 2}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: True
- Inspection error: None
- Nested field paths: 4
- Evidence role verified: NO

### de9968f3349f198d864f — 2 files
- Representative: `research/case-binance-2026/analysis/master_flow_map_v1/EDGE_REGISTER_V1.csv`
- Candidate roles: {'TRANSFER_SHAPED_CANDIDATE': 2}
- Field hints: {'tx_hash': True, 'from': True, 'to': True, 'amount': True, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 15
- Evidence role verified: NO

### ecb98c5df4e30840026d — 2 files
- Representative: `research/case-binance-2026/evidence/eg02_central_post_blacklist_ledger_v1/manifest.json`
- Candidate roles: {'MANIFEST_OR_INTEGRITY': 2}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 5
- Evidence role verified: NO

### f5078a337cab6a5fdcab — 2 files
- Representative: `research/case-binance-2026/evidence/exploiter16_token_provenance_v1/step16_receipt_evidence_v1/e16_aave.json`
- Candidate roles: {'TRANSFER_SHAPED_CANDIDATE': 2}
- Field hints: {'tx_hash': True, 'from': True, 'to': True, 'amount': True, 'log_index': True, 'trace': False, 'token': False, 'events': True}
- Nested sample limited: True
- Inspection error: None
- Nested field paths: 80
- Evidence role verified: NO

### f5f1484ce507b70f9882 — 2 files
- Representative: `research/case-binance-2026/evidence/binance14_all_receivers_census_v1/step66_receiver_identity_rpc_audit_v1/RECEIVER_IDENTITY_REGISTER_V1.csv`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 2}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 11
- Evidence role verified: NO

### 00e4bb1e10cd5303c964 — 1 files
- Representative: `research/case-binance-2026/GATE_2_RECEIVER_ROLE_SCREEN_V1.csv`
- Candidate roles: {'UNKNOWN_DATA_ROLE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 14
- Evidence role verified: NO

### 0170009f47d86a7f9fc7 — 1 files
- Representative: `research/case-binance-2026/GATE_2_EXTERNAL_TXID_CROSSCHECK_V1.csv`
- Candidate roles: {'UNKNOWN_DATA_ROLE': 1}
- Field hints: {'tx_hash': True, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 6
- Evidence role verified: NO

### 0194d592707c1d94de80 — 1 files
- Representative: `research/case-binance-2026/evidence/eg08_plasma_post_delivery_v1/step05b_atoken_identity_reconciliation_v1/receipt_transfer_events.json`
- Candidate roles: {'TRANSFER_SHAPED_CANDIDATE': 1}
- Field hints: {'tx_hash': True, 'from': True, 'to': True, 'amount': True, 'log_index': True, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 16
- Evidence role verified: NO

### 01c0583e7729b035ebb9 — 1 files
- Representative: `research/case-binance-2026/A97B/economic_flow_v1/A97B_ADDRESS_ROUTES_V1.csv`
- Candidate roles: {'UNKNOWN_DATA_ROLE': 1}
- Field hints: {'tx_hash': False, 'from': True, 'to': True, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 8
- Evidence role verified: NO

### 022e4293b3ae4eaa5f2e — 1 files
- Representative: `research/case-binance-2026/GATE_2_POR_EVIDENCE_MANIFEST_V1.json`
- Candidate roles: {'MANIFEST_OR_INTEGRITY': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 18
- Evidence role verified: NO

### 030b85ef7589a13255f8 — 1 files
- Representative: `research/case-binance-2026/A97B/evidence/bitquery_independent_audit_v1/FINAL_INTEGRITY_AUDIT_V2.json`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': True, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: True
- Inspection error: None
- Nested field paths: 22
- Evidence role verified: NO

### 038be39c7fd36e625a97 — 1 files
- Representative: `research/case-binance-2026/evidence/eg08_plasma_post_delivery_v1/step05_withdrawal_audit_v1/derived_aave_contracts.json`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': True, 'log_index': True, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 11
- Evidence role verified: NO

### 040a9963c3a9ff6d3e38 — 1 files
- Representative: `research/case-binance-2026/evidence/step71_55m_source_audit_v1/por_crosswalk_matches.json`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: True
- Inspection error: None
- Nested field paths: 15
- Evidence role verified: NO

### 0446dcd5f8765aecb999 — 1 files
- Representative: `research/case-binance-2026/evidence/eg08_plasma_post_delivery_v1/step07c_atoken_interest_reconciliation_v1/summary.json`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 9
- Evidence role verified: NO

### 0466b95b6443ea54098a — 1 files
- Representative: `research/case-binance-2026/evidence/eg08_source_attribution_v1/step08y_forward_edge_preservation_v1/summary.json`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 13
- Evidence role verified: NO

### 049671923413da7d1a19 — 1 files
- Representative: `research/case-binance-2026/GATE_2_XRPL_FIVE_SOURCE_TX_AUDIT_V1.csv`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': True, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 13
- Evidence role verified: NO

### 04cc4f86398e3dffe2de — 1 files
- Representative: `research/case-binance-2026/evidence/binance14_all_receivers_census_v1/step65_direct_receiver_route_register_v1/DIRECT_RECEIVER_TRANSACTION_LEDGER_V1.csv`
- Candidate roles: {'TRANSFER_SHAPED_CANDIDATE': 1}
- Field hints: {'tx_hash': True, 'from': True, 'to': True, 'amount': True, 'log_index': True, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 15
- Evidence role verified: NO

### 074018cbaa803805c777 — 1 files
- Representative: `research/case-binance-2026/A97B/institutional_research_packet_v1/SHA256_MANIFEST_V1.json`
- Candidate roles: {'MANIFEST_OR_INTEGRITY': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 6
- Evidence role verified: NO

### 0a8411da6a20a17a0ad9 — 1 files
- Representative: `research/case-binance-2026/evidence/binance14_all_receivers_census_v1/manifest.json`
- Candidate roles: {'MANIFEST_OR_INTEGRITY': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 26
- Evidence role verified: NO

### 0ac942a603e605fafdb1 — 1 files
- Representative: `research/case-binance-2026/evidence/eg08_plasma_post_delivery_v1/step07a_28m_conservation_audit_v1/provenance.json`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 6
- Evidence role verified: NO

### 0c22445fa62d5beba71e — 1 files
- Representative: `research/case-binance-2026/A97B/integrated_event_audit_v1/RECOVERED_109_RECEIPT_AUDIT_V1.csv`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': True, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 5
- Evidence role verified: NO

### 0c4e8318fb63f6be765a — 1 files
- Representative: `research/case-binance-2026/A97B/economic_flow_v1/A97B_HOURLY_ASSET_FLOW_V1.csv`
- Candidate roles: {'UNKNOWN_DATA_ROLE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 8
- Evidence role verified: NO

### 0c7b29ec8f474887cbcd — 1 files
- Representative: `research/case-binance-2026/evidence/eg08_plasma_post_delivery_v1/step05c_burn_interest_event_reconciliation_v1/summary.json`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': True, 'from': True, 'to': True, 'amount': True, 'log_index': True, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 155
- Evidence role verified: NO

### 0d88e119e6f001ef8da1 — 1 files
- Representative: `research/case-binance-2026/GATE_2_NEW_TX_TRIAGE_V1.csv`
- Candidate roles: {'UNKNOWN_DATA_ROLE': 1}
- Field hints: {'tx_hash': True, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 7
- Evidence role verified: NO

### 0f5c80dd51f588247f43 — 1 files
- Representative: `research/case-binance-2026/A97B/evidence/step70_bitquery_ledger_reconciliation_v1/query_conditions.json`
- Candidate roles: {'UNKNOWN_DATA_ROLE': 1}
- Field hints: {'tx_hash': True, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 43
- Evidence role verified: NO

### 0fd3e35921ad45f1c1b2 — 1 files
- Representative: `research/case-binance-2026/evidence/exploiter16_token_provenance_v1/step18g_four_route_evidence_v1/manifest.json`
- Candidate roles: {'MANIFEST_OR_INTEGRITY': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 12
- Evidence role verified: NO

### 11d8643b88a53ed5b8db — 1 files
- Representative: `research/case-binance-2026/evidence/binance14_all_receivers_census_v1/step85_a97b_final_event_audit_v1/manifest.json`
- Candidate roles: {'MANIFEST_OR_INTEGRITY': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 10
- Evidence role verified: NO

### 1201d8089ce605446107 — 1 files
- Representative: `research/case-binance-2026/A97B/institutional_research_packet_v1/HISTORICAL_CASE_MECHANISM_CROSSWALK_V1.csv`
- Candidate roles: {'UNKNOWN_DATA_ROLE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 7
- Evidence role verified: NO

### 12ef2c938fb9e57b99de — 1 files
- Representative: `research/case-binance-2026/evidence/eg08_plasma_post_delivery_v1/step06b_issuer_control_simulation_v1/provenance.json`
- Candidate roles: {'UNKNOWN_DATA_ROLE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 8
- Evidence role verified: NO

### 12f45e3802b0f0a2286d — 1 files
- Representative: `research/case-binance-2026/PUBLICATION_CITATION_MAP_V1.csv`
- Candidate roles: {'UNKNOWN_DATA_ROLE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 7
- Evidence role verified: NO

### 13c4d148a12da068fcc4 — 1 files
- Representative: `research/case-binance-2026/evidence/exploiter16_token_provenance_v1/step16_receipt_evidence_v1/central_to_e16_aave.json`
- Candidate roles: {'TRANSFER_SHAPED_CANDIDATE': 1}
- Field hints: {'tx_hash': True, 'from': True, 'to': True, 'amount': True, 'log_index': True, 'trace': False, 'token': False, 'events': True}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 52
- Evidence role verified: NO

### 13e687a39173e55a029c — 1 files
- Representative: `research/case-binance-2026/evidence/binance14_all_receivers_census_v1/step77_a97b_dex_swap_evidence_v1/dex_router_samples.json`
- Candidate roles: {'UNKNOWN_DATA_ROLE': 1}
- Field hints: {'tx_hash': True, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 18
- Evidence role verified: NO

### 13fb64bbb1e55d219a1d — 1 files
- Representative: `research/case-binance-2026/PR01OCT26_HotCold.csv`
- Candidate roles: {'UNKNOWN_DATA_ROLE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 6
- Evidence role verified: NO

### 1422ce6114d32b5247cf — 1 files
- Representative: `research/case-binance-2026/evidence/eg08_plasma_post_delivery_v1/step06e_scenario_accounting_reconciliation_v1/summary.json`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 40
- Evidence role verified: NO

### 14a33910c1cd736ce46f — 1 files
- Representative: `research/case-binance-2026/A97B/evidence/elliptic_blocklist.csv`
- Candidate roles: {'UNKNOWN_DATA_ROLE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 1
- Evidence role verified: NO

### 14dd2bebf312fb32ffbb — 1 files
- Representative: `research/case-binance-2026/OFFICIAL_INCIDENT_EVIDENCE_REGISTER_V1.csv`
- Candidate roles: {'UNKNOWN_DATA_ROLE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 7
- Evidence role verified: NO

### 1596d9f3250a7c0a0dfc — 1 files
- Representative: `research/case-binance-2026/evidence/eg08_plasma_post_delivery_v1/step05_withdrawal_audit_v1/atoken_user_transfer_ledger.json`
- Candidate roles: {'TRANSFER_SHAPED_CANDIDATE': 1}
- Field hints: {'tx_hash': False, 'from': True, 'to': True, 'amount': True, 'log_index': True, 'trace': False, 'token': True, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 9
- Evidence role verified: NO

### 15b61dced6593df45992 — 1 files
- Representative: `research/case-binance-2026/evidence/eg03_two_address_consolidation_v1/manifest.json`
- Candidate roles: {'MANIFEST_OR_INTEGRITY': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 12
- Evidence role verified: NO

### 163633cbeffae9bc7cf5 — 1 files
- Representative: `research/case-binance-2026/evidence/binance14_all_receivers_census_v1/step70_a97b_forward_census_v1/A97B_FORWARD_TRANSFER_LEDGER_V1.csv`
- Candidate roles: {'TRANSFER_SHAPED_CANDIDATE': 1}
- Field hints: {'tx_hash': True, 'from': True, 'to': True, 'amount': True, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 14
- Evidence role verified: NO

### 16936aec273e62e1538f — 1 files
- Representative: `research/case-binance-2026/GATE_2_EXPANDED_WALLET_CANDIDATES_V1.csv`
- Candidate roles: {'UNKNOWN_DATA_ROLE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 12
- Evidence role verified: NO

### 1810bbb96c982aeea701 — 1 files
- Representative: `research/case-binance-2026/evidence/eg08_source_attribution_v1/step08f_earlier_10000_blocks_v1/summary.json`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 19
- Evidence role verified: NO

### 1b653edfba31276fe486 — 1 files
- Representative: `research/case-binance-2026/GATE_2_MULTICHAIN_SOURCE_CANDIDATES_V1.csv`
- Candidate roles: {'UNKNOWN_DATA_ROLE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 13
- Evidence role verified: NO

### 1c7790c4ba84c6a9f132 — 1 files
- Representative: `research/case-binance-2026/evidence/eg08_plasma_post_delivery_v1/step05_withdrawal_audit_v1/withdrawal_audit_summary.json`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': True, 'from': True, 'to': True, 'amount': True, 'log_index': True, 'trace': False, 'token': True, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 49
- Evidence role verified: NO

### 1cb1330984d0d8694be0 — 1 files
- Representative: `research/case-binance-2026/evidence/eg08_source_attribution_v1/step08n_source_receipt_verification_v1/summary.json`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 10
- Evidence role verified: NO

### 1d81c1166054e17878e3 — 1 files
- Representative: `research/case-binance-2026/evidence/eg05_kite_pause_origin_v1/manifest.json`
- Candidate roles: {'MANIFEST_OR_INTEGRITY': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': True, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 54
- Evidence role verified: NO

### 1eff5d50a4281346a538 — 1 files
- Representative: `research/case-binance-2026/evidence/eg08_plasma_post_delivery_v1/step06b_issuer_control_simulation_v1/non_owner_control.json`
- Candidate roles: {'UNKNOWN_DATA_ROLE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 2
- Evidence role verified: NO

### 20a0d1f2f5e816acdc66 — 1 files
- Representative: `research/case-binance-2026/evidence/binance14_all_receivers_census_v1/step68_elliptic_address_crosswalk_v1/elliptic_blocklist_snapshot.csv`
- Candidate roles: {'UNKNOWN_DATA_ROLE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 1
- Evidence role verified: NO

### 21a7d1a822cde23a12a4 — 1 files
- Representative: `research/case-binance-2026/evidence/eg08_plasma_post_delivery_v1/step05c_burn_interest_event_reconciliation_v1/manifest.json`
- Candidate roles: {'MANIFEST_OR_INTEGRITY': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 13
- Evidence role verified: NO

### 21b431988977fce1c76f — 1 files
- Representative: `research/case-binance-2026/evidence/binance14_all_receivers_census_v1/step72_a97b_pattern_funding_audit_v1/eth_funding_screen.json`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: True
- Inspection error: None
- Nested field paths: 24
- Evidence role verified: NO

### 2220a21ca20064392abd — 1 files
- Representative: `research/case-binance-2026/evidence/binance14_all_receivers_census_v1/step69_noncentral_receiver_forward_screen_v1/NONCENTRAL_OUTGOING_LEDGER_V1.csv`
- Candidate roles: {'TRANSFER_SHAPED_CANDIDATE': 1}
- Field hints: {'tx_hash': True, 'from': True, 'to': True, 'amount': True, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 15
- Evidence role verified: NO

### 228fae668acb06965cfc — 1 files
- Representative: `research/case-binance-2026/analysis/master_timeline_v0/MASTER_TIMELINE_V0.csv`
- Candidate roles: {'TRANSFER_SHAPED_CANDIDATE': 1}
- Field hints: {'tx_hash': True, 'from': True, 'to': True, 'amount': True, 'log_index': True, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 16
- Evidence role verified: NO

### 233bf303145ba3cfaea9 — 1 files
- Representative: `research/case-binance-2026/evidence/binance14_all_receivers_census_v1/step72_a97b_pattern_funding_audit_v1/manifest.json`
- Candidate roles: {'MANIFEST_OR_INTEGRITY': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 35
- Evidence role verified: NO

### 2394a6edc687c6e34fb4 — 1 files
- Representative: `research/case-binance-2026/A97B/dex_weth_flow_audit_v1/DEX_WETH_TX_SUMMARY_V1.csv`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': True, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 8
- Evidence role verified: NO

### 245bf491354d38613ce5 — 1 files
- Representative: `research/case-binance-2026/evidence/binance14_all_receivers_census_v1/transaction_summary.csv`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 7
- Evidence role verified: NO

### 24eea93621d7995ea1a9 — 1 files
- Representative: `research/case-binance-2026/evidence/eg08_plasma_delivery_v1/verified_summary.json`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': True, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 19
- Evidence role verified: NO

### 251cb3f9ca81ecac2bdc — 1 files
- Representative: `research/case-binance-2026/A97B/dex_internal_trace_v1/DEX_SWAP_EVENT_CANDIDATES_V1.csv`
- Candidate roles: {'UNKNOWN_DATA_ROLE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 0
- Evidence role verified: NO

### 2548e9a80a90d8b972b1 — 1 files
- Representative: `research/case-binance-2026/evidence/binance14_all_receivers_census_v1/step83_official_attribution_crosswalk_v1/manifest.json`
- Candidate roles: {'MANIFEST_OR_INTEGRITY': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 10
- Evidence role verified: NO

### 27e6ee0058fc692a42ad — 1 files
- Representative: `research/case-binance-2026/evidence/eg08_plasma_post_delivery_v1/step06a_issuer_freeze_capability_audit_v1/summary.json`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: True
- Inspection error: None
- Nested field paths: 28
- Evidence role verified: NO

### 2a9752306ef676f72654 — 1 files
- Representative: `research/case-binance-2026/GATE_2_ETH_T03_COMMAND_CONSOLIDATION_V1.json`
- Candidate roles: {'UNKNOWN_DATA_ROLE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': True, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 18
- Evidence role verified: NO

### 2b7cda451cffd1e590b3 — 1 files
- Representative: `research/case-binance-2026/evidence/binance14_all_receivers_census_v1/step67_internal_eth_trace_audit_v1/blockscout_crosscheck_v1/audit.json`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 10
- Evidence role verified: NO

### 2cfaf94608def7f3d3f9 — 1 files
- Representative: `research/case-binance-2026/A97B/dex_weth_flow_audit_v1/AUDIT_V1.json`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': True}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 12
- Evidence role verified: NO

### 2d1221dd58edd8233c16 — 1 files
- Representative: `research/case-binance-2026/evidence/eg08_plasma_post_delivery_v1/step07a_28m_conservation_audit_v1/conservation_report.json`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': True, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 30
- Evidence role verified: NO

### 2de21690dadb8cdab417 — 1 files
- Representative: `research/case-binance-2026/evidence/eg02_central_post_blacklist_ledger_v1/audit.json`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 17
- Evidence role verified: NO

### 2f24a3427f90f7cd238f — 1 files
- Representative: `research/case-binance-2026/A97B/dex_external_screening_v1/AUDIT_V1.json`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 8
- Evidence role verified: NO

### 2f909010bb317edf1720 — 1 files
- Representative: `research/case-binance-2026/evidence/eg01_execution_time_v1/manifest.json`
- Candidate roles: {'MANIFEST_OR_INTEGRITY': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': True, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 25
- Evidence role verified: NO

### 315dcd3692b8a2899ed3 — 1 files
- Representative: `research/case-binance-2026/analysis/master_flow_map_v1/AUDIT_V1.json`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: True
- Inspection error: None
- Nested field paths: 27
- Evidence role verified: NO

### 31b645c6c4cd4e398544 — 1 files
- Representative: `research/case-binance-2026/evidence/step73_preincident_graphsense_v1/audit.json`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 11
- Evidence role verified: NO

### 3341194641afa3666e11 — 1 files
- Representative: `research/case-binance-2026/evidence/eg08_plasma_post_delivery_v1/step06d_aave_reserve_liquidity_reconciliation_v1/summary.json`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 16
- Evidence role verified: NO

### 35e05b8664f57013f38b — 1 files
- Representative: `research/case-binance-2026/A97B/eth_first_recipient_audit_v1/AUDIT_V1.json`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 11
- Evidence role verified: NO

### 36968707eb839e83a500 — 1 files
- Representative: `research/case-binance-2026/A97B/evidence/step70_bitquery_ledger_reconciliation_v1/transfer_reconciliation.csv`
- Candidate roles: {'UNKNOWN_DATA_ROLE': 1}
- Field hints: {'tx_hash': False, 'from': True, 'to': True, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 33
- Evidence role verified: NO

### 37ee1b329fc7cd3baf9c — 1 files
- Representative: `research/case-binance-2026/evidence/step73_preincident_graphsense_v1/manifest.json`
- Candidate roles: {'MANIFEST_OR_INTEGRITY': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 3
- Evidence role verified: NO

### 39511f836226822562ea — 1 files
- Representative: `research/case-binance-2026/evidence/binance14_all_receivers_census_v1/step66_receiver_identity_rpc_audit_v1/transaction_receipt_block_evidence.json`
- Candidate roles: {'TRANSFER_SHAPED_CANDIDATE': 1}
- Field hints: {'tx_hash': True, 'from': True, 'to': True, 'amount': True, 'log_index': True, 'trace': False, 'token': False, 'events': True}
- Nested sample limited: True
- Inspection error: None
- Nested field paths: 5496
- Evidence role verified: NO

### 39b7676b347bf4625a02 — 1 files
- Representative: `research/case-binance-2026/evidence/step71_55m_source_audit_v1/balance_and_code_audit.json`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': True, 'log_index': True, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 16
- Evidence role verified: NO

### 3a226dcbdd9e87850de4 — 1 files
- Representative: `research/case-binance-2026/evidence/eg08_plasma_post_delivery_v1/step06b_aave_withdraw_callpath_v1/runtime_code_inventory.json`
- Candidate roles: {'RAW_SOURCE_CANDIDATE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 36
- Evidence role verified: NO

### 3aed01d86909a56c8fe0 — 1 files
- Representative: `research/case-binance-2026/evidence/eg08_plasma_post_delivery_v1/step07c_atoken_interest_reconciliation_v1/provenance.json`
- Candidate roles: {'UNKNOWN_DATA_ROLE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 6
- Evidence role verified: NO

### 3b5588f15276e85313fa — 1 files
- Representative: `research/case-binance-2026/evidence/eg08_plasma_post_delivery_v1/step07d_final_evidence_consistency_audit_v1/summary.json`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: True
- Inspection error: None
- Nested field paths: 28
- Evidence role verified: NO

### 3c4b48cdff6e28636d7d — 1 files
- Representative: `research/case-binance-2026/GATE_2_TX_CONTEXT_REVIEW_V1.csv`
- Candidate roles: {'UNKNOWN_DATA_ROLE': 1}
- Field hints: {'tx_hash': True, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 10
- Evidence role verified: NO

### 3c9c3a43422a3ddbae01 — 1 files
- Representative: `research/case-binance-2026/evidence/eg08_plasma_post_delivery_v1/step06f_withdrawal_revert_diagnostics_v1/manifest.json`
- Candidate roles: {'MANIFEST_OR_INTEGRITY': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 8
- Evidence role verified: NO

### 3f2285913ac18d228e8d — 1 files
- Representative: `research/case-binance-2026/GATE_2_EXTERNAL_SOURCE_QUEUE_V1.csv`
- Candidate roles: {'UNKNOWN_DATA_ROLE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 7
- Evidence role verified: NO

### 3faaecce305704007cb5 — 1 files
- Representative: `research/case-binance-2026/evidence/eg08_plasma_post_delivery_v1/step06b_aave_withdraw_callpath_v1/withdrawal_eth_call.json`
- Candidate roles: {'TRANSFER_SHAPED_CANDIDATE': 1}
- Field hints: {'tx_hash': False, 'from': True, 'to': True, 'amount': True, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 13
- Evidence role verified: NO

### 4018bd30202daa1d754e — 1 files
- Representative: `research/case-binance-2026/evidence/binance14_all_receivers_census_v1/step72_a97b_pattern_funding_audit_v1/audit.json`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 10
- Evidence role verified: NO

### 416835cec966bcd5e30f — 1 files
- Representative: `research/case-binance-2026/AXIOM_PUBLICATION_CLAIMS_AUDIT_V1.csv`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 3
- Evidence role verified: NO

### 42a1089c8c33ee052c5d — 1 files
- Representative: `research/case-binance-2026/A97B/economic_flow_v1/A97B_ECONOMIC_FLOW_AUDIT_V1.json`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: True
- Inspection error: None
- Nested field paths: 12
- Evidence role verified: NO

### 42f017c7a239d1b4742f — 1 files
- Representative: `research/case-binance-2026/evidence/eg08_plasma_delivery_v1/manifest.json`
- Candidate roles: {'MANIFEST_OR_INTEGRITY': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 10
- Evidence role verified: NO

### 43ae2cac3784b9488253 — 1 files
- Representative: `research/case-binance-2026/evidence/30m_blacklist_audit_v1/balance_snapshots.json`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': True, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 9
- Evidence role verified: NO

### 43c65c63ebe294d34414 — 1 files
- Representative: `research/case-binance-2026/evidence/binance14_all_receivers_census_v1/step67_internal_eth_trace_audit_v1/blockscout_crosscheck_v1/crosscheck_results.json`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': True, 'from': True, 'to': True, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 15
- Evidence role verified: NO

### 44adb409e446464c35f7 — 1 files
- Representative: `research/case-binance-2026/evidence/eg08_plasma_post_delivery_v1/step06e_scenario_accounting_reconciliation_v1/scenario_accounting.json`
- Candidate roles: {'UNKNOWN_DATA_ROLE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 13
- Evidence role verified: NO

### 45114a5c50c184f296fa — 1 files
- Representative: `research/case-binance-2026/evidence/binance14_all_receivers_census_v1/step77_a97b_dex_swap_evidence_v1/audit.json`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: True
- Inspection error: None
- Nested field paths: 13
- Evidence role verified: NO

### 45911f7206b2d354730f — 1 files
- Representative: `research/case-binance-2026/evidence/eg08_source_attribution_v1/step08r_aave_mantle_receipt_audit_v1/summary.json`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 8
- Evidence role verified: NO

### 45f4b9c62fe3e9cc91a4 — 1 files
- Representative: `research/case-binance-2026/evidence/eg08_plasma_post_delivery_v1/step05b_atoken_identity_reconciliation_v1/exact_block_logs.json`
- Candidate roles: {'UNKNOWN_DATA_ROLE': 1}
- Field hints: {'tx_hash': True, 'from': False, 'to': False, 'amount': False, 'log_index': True, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 36
- Evidence role verified: NO

### 45f50149429b0fd16d45 — 1 files
- Representative: `research/case-binance-2026/A97B/economic_flow_v1/A97B_ASSET_DIRECTION_TOTALS_V1.csv`
- Candidate roles: {'UNKNOWN_DATA_ROLE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 7
- Evidence role verified: NO

### 4615c2a5098778c2f7fa — 1 files
- Representative: `research/case-binance-2026/evidence/eg08_source_attribution_v1/step08z_crystal_axiom_crosswalk_v1/crystal_source_claims.json`
- Candidate roles: {'UNKNOWN_DATA_ROLE': 1}
- Field hints: {'tx_hash': False, 'from': True, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 15
- Evidence role verified: NO

### 471d5c6da5bc47832a9e — 1 files
- Representative: `research/case-binance-2026/evidence/eg08_plasma_post_delivery_v1/step05b_atoken_identity_reconciliation_v1/token_metadata.json`
- Candidate roles: {'UNKNOWN_DATA_ROLE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 32
- Evidence role verified: NO

### 473d887e2ac7e7fa2e91 — 1 files
- Representative: `research/case-binance-2026/evidence/eg08_source_attribution_v1/step08m_source_message_lookup_v1/summary.json`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 10
- Evidence role verified: NO

### 48059d51981da905838f — 1 files
- Representative: `research/case-binance-2026/evidence/eg08_plasma_post_delivery_v1/step07b_post_ledger_gap_audit_v1/provenance.json`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 7
- Evidence role verified: NO

### 4b0b149b6bb27d0c8f79 — 1 files
- Representative: `research/case-binance-2026/A97B/evidence/bitquery_independent_audit_v1/manifest.json`
- Candidate roles: {'MANIFEST_OR_INTEGRITY': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: True
- Inspection error: None
- Nested field paths: 5
- Evidence role verified: NO

### 4b16f9b69fa269f768a7 — 1 files
- Representative: `research/case-binance-2026/A97B/dex_transaction_paths_v1/DEX_ALL_VERIFIED_TOKEN_LEGS_V1.csv`
- Candidate roles: {'TRANSFER_SHAPED_CANDIDATE': 1}
- Field hints: {'tx_hash': True, 'from': True, 'to': True, 'amount': True, 'log_index': True, 'trace': False, 'token': True, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 14
- Evidence role verified: NO

### 4bd0ed368dab3cf2bb65 — 1 files
- Representative: `research/case-binance-2026/evidence/eg05_kite_historical_pause_v1/manifest.json`
- Candidate roles: {'MANIFEST_OR_INTEGRITY': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': True, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 27
- Evidence role verified: NO

### 4c3149e9da7d6142acf6 — 1 files
- Representative: `research/case-binance-2026/evidence/eg08_source_attribution_v1/step08t_atoken_historical_position_v1/summary.json`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: True
- Inspection error: None
- Nested field paths: 48
- Evidence role verified: NO

### 4c3f8bb4579ca7984575 — 1 files
- Representative: `research/case-binance-2026/A97B/eth_address_receipts_v1/AUDIT_V1.json`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 15
- Evidence role verified: NO

### 4cb6a76742463ea91e0d — 1 files
- Representative: `research/case-binance-2026/evidence/binance14_all_receivers_census_v1/step65_direct_receiver_route_register_v1/manifest.json`
- Candidate roles: {'MANIFEST_OR_INTEGRITY': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 19
- Evidence role verified: NO

### 4dbd768d802cf4d4451a — 1 files
- Representative: `research/case-binance-2026/GATE_2_ETH_T02_AUTHORIZATION_REPLAY_V1.json`
- Candidate roles: {'UNKNOWN_DATA_ROLE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: True
- Inspection error: None
- Nested field paths: 17
- Evidence role verified: NO

### 4dd6c327d208474a4987 — 1 files
- Representative: `research/case-binance-2026/evidence/central_blacklist_audit_v1/manifest.json`
- Candidate roles: {'MANIFEST_OR_INTEGRITY': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 20
- Evidence role verified: NO

### 4e04736e5d365889ab80 — 1 files
- Representative: `research/case-binance-2026/SOURCE_WALLET_REGISTER_V1.csv`
- Candidate roles: {'UNKNOWN_DATA_ROLE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 4
- Evidence role verified: NO

### 4e2ba50a7451dd5effa7 — 1 files
- Representative: `research/case-binance-2026/evidence/binance14_all_receivers_census_v1/step81_a97b_remaining_60_audit_v1/manifest.json`
- Candidate roles: {'MANIFEST_OR_INTEGRITY': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 5
- Evidence role verified: NO

### 4e5b50ff1041179ed530 — 1 files
- Representative: `research/case-binance-2026/evidence/eg08_source_attribution_v1/step08j_address_a_complete_window_v1/summary.json`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 22
- Evidence role verified: NO

### 4e8413e7f8eb7d4e4866 — 1 files
- Representative: `research/case-binance-2026/evidence/eg08_source_attribution_v1/step08k_adapter_inbound_receipts_v1/summary.json`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 15
- Evidence role verified: NO

### 4f80d0d6bcfcca5e1146 — 1 files
- Representative: `research/case-binance-2026/evidence/second_hop_receipts_v1/manifest.json`
- Candidate roles: {'MANIFEST_OR_INTEGRITY': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: True
- Inspection error: None
- Nested field paths: 3
- Evidence role verified: NO

### 515298613f4dc23d0e2c — 1 files
- Representative: `research/case-binance-2026/analysis/master_flow_map_v1/NODE_REGISTER_V1.csv`
- Candidate roles: {'UNKNOWN_DATA_ROLE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 13
- Evidence role verified: NO

### 53133ae7dbb06cc88cc5 — 1 files
- Representative: `research/case-binance-2026/evidence/eg03_recipient_blacklist_v1.json`
- Candidate roles: {'UNKNOWN_DATA_ROLE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': True, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: True
- Inspection error: None
- Nested field paths: 20
- Evidence role verified: NO

### 532739341f8a362cfac9 — 1 files
- Representative: `research/case-binance-2026/evidence/eg08_plasma_post_delivery_v1/step06a_issuer_freeze_capability_audit_v1/capability_inventory.json`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 70
- Evidence role verified: NO

### 542127e45fc07806a195 — 1 files
- Representative: `research/case-binance-2026/A97B/evidence/bitquery_independent_audit_v1/PACKAGE_SHA256.json`
- Candidate roles: {'MANIFEST_OR_INTEGRITY': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 28
- Evidence role verified: NO

### 5474464a493be2d10d6b — 1 files
- Representative: `research/case-binance-2026/evidence/eg08_source_attribution_v1/step08n_source_receipt_verification_v1/source_oft_crosswalk.json`
- Candidate roles: {'RAW_SOURCE_CANDIDATE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 21
- Evidence role verified: NO

### 549b8a8dbdcf82a0fa37 — 1 files
- Representative: `research/case-binance-2026/evidence/binance14_all_receivers_census_v1/step73_a97b_execution_conservation_v1/eth_conservation_screen.json`
- Candidate roles: {'UNKNOWN_DATA_ROLE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 10
- Evidence role verified: NO

### 563a8746bac77f07592c — 1 files
- Representative: `research/case-binance-2026/AXIOM_PUBLICATION_EVIDENCE_INVENTORY_V1.csv`
- Candidate roles: {'UNKNOWN_DATA_ROLE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 7
- Evidence role verified: NO

### 56402384238d2356779e — 1 files
- Representative: `research/case-binance-2026/evidence/eg08_plasma_post_delivery_v1/step05c_burn_interest_event_reconciliation_v1/state_reconciliation.json`
- Candidate roles: {'UNKNOWN_DATA_ROLE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 9
- Evidence role verified: NO

### 564366d20f7214c43bbc — 1 files
- Representative: `research/case-binance-2026/evidence/binance14_all_receivers_census_v1/step67_internal_eth_trace_audit_v1/blockscout_crosscheck_v1/manifest.json`
- Candidate roles: {'MANIFEST_OR_INTEGRITY': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 10
- Evidence role verified: NO

### 578772006c9007bb905a — 1 files
- Representative: `research/case-binance-2026/evidence/eg08_plasma_post_delivery_v1/step02_transfer_ledger_v1/scan_snapshot.json`
- Candidate roles: {'UNKNOWN_DATA_ROLE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': True, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 10
- Evidence role verified: NO

### 57fc62ac9f5fda595aba — 1 files
- Representative: `research/case-binance-2026/AXIOM_EXTERNAL_PRIOR_ART_COMPARISON_V1.csv`
- Candidate roles: {'UNKNOWN_DATA_ROLE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 5
- Evidence role verified: NO

### 58dffcd919e467787013 — 1 files
- Representative: `research/case-binance-2026/A97B/integrated_event_audit_v1/AUDIT_V1.json`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: True
- Inspection error: None
- Nested field paths: 21
- Evidence role verified: NO

### 59ab1ab37e55f263a3ba — 1 files
- Representative: `research/case-binance-2026/evidence/eg08_plasma_post_delivery_v1/destination_block_recipient_transfer_logs.json`
- Candidate roles: {'UNKNOWN_DATA_ROLE': 1}
- Field hints: {'tx_hash': True, 'from': False, 'to': True, 'amount': False, 'log_index': True, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 14
- Evidence role verified: NO

### 5b13841e56e5e54d007b — 1 files
- Representative: `research/case-binance-2026/A97B/evidence/bitquery_independent_audit_v1/reconciliation_full_1015.csv`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': True, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 3
- Evidence role verified: NO

### 5b45350a5fa4f6657594 — 1 files
- Representative: `research/case-binance-2026/A97B/dex_route_mechanism_v1/DEX_MECHANISM_TIMELINE_V1.csv`
- Candidate roles: {'UNKNOWN_DATA_ROLE': 1}
- Field hints: {'tx_hash': True, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 18
- Evidence role verified: NO

### 5b5ca08d25b915ec8c5a — 1 files
- Representative: `research/case-binance-2026/evidence/binance14_all_receivers_census_v1/step81_a97b_remaining_60_audit_v1/remaining_60_event_register.csv`
- Candidate roles: {'TRANSFER_SHAPED_CANDIDATE': 1}
- Field hints: {'tx_hash': True, 'from': True, 'to': True, 'amount': True, 'log_index': False, 'trace': False, 'token': True, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 19
- Evidence role verified: NO

### 5ba044cdccd5f7674882 — 1 files
- Representative: `research/case-binance-2026/evidence/binance14_all_receivers_census_v1/step68_elliptic_address_crosswalk_v1/audit.json`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 10
- Evidence role verified: NO

### 5d7804d04c0b679a4606 — 1 files
- Representative: `research/case-binance-2026/GATE_2_ETH_T03_BLOCK_ORDER_AUDIT_V1.json`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 12
- Evidence role verified: NO

### 5fb04049be97fbc3ab3d — 1 files
- Representative: `research/case-binance-2026/evidence/binance14_all_receivers_census_v1/step69_noncentral_receiver_forward_screen_v1/audit.json`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: True
- Inspection error: None
- Nested field paths: 12
- Evidence role verified: NO

### 620c65c42f51c885a545 — 1 files
- Representative: `research/case-binance-2026/evidence/eg08_plasma_post_delivery_v1/step05a_withdrawal_anomaly_reconciliation_v1/atoken_exact_block_log_queries.json`
- Candidate roles: {'RAW_SOURCE_CANDIDATE': 1}
- Field hints: {'tx_hash': True, 'from': False, 'to': False, 'amount': False, 'log_index': True, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 36
- Evidence role verified: NO

### 631976a8f3c0991bffef — 1 files
- Representative: `research/case-binance-2026/A97B/dex_transaction_paths_v1/DEX_TRANSACTION_PATHS_V1.csv`
- Candidate roles: {'UNKNOWN_DATA_ROLE': 1}
- Field hints: {'tx_hash': True, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 17
- Evidence role verified: NO

### 6331ff3e9e83e2171cf5 — 1 files
- Representative: `research/case-binance-2026/evidence/eg08_source_attribution_v1/step08z_crystal_axiom_crosswalk_v1/claim_by_claim_comparison.json`
- Candidate roles: {'UNKNOWN_DATA_ROLE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 7
- Evidence role verified: NO

### 64be67ad73f40e6798bb — 1 files
- Representative: `research/case-binance-2026/evidence/binance14_all_receivers_census_v1/step70_a97b_forward_census_v1/manifest.json`
- Candidate roles: {'MANIFEST_OR_INTEGRITY': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 19
- Evidence role verified: NO

### 64cc9269498587eb8b0a — 1 files
- Representative: `research/case-binance-2026/A97B/dex_weth_settlement_audit_v1/WETH_WRAP_UNWRAP_EVENTS_V1.csv`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': True, 'from': False, 'to': False, 'amount': False, 'log_index': True, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 7
- Evidence role verified: NO

### 6503179750c80929907f — 1 files
- Representative: `research/case-binance-2026/evidence/eg08_plasma_post_delivery_v1/step06c_local_fork_freeze_scenarios_v1/baseline.json`
- Candidate roles: {'UNKNOWN_DATA_ROLE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 6
- Evidence role verified: NO

### 652a2fab6deb96c071ad — 1 files
- Representative: `research/case-binance-2026/evidence/eg08_plasma_post_delivery_v1/step06f_withdrawal_revert_diagnostics_v1/provenance.json`
- Candidate roles: {'RAW_SOURCE_CANDIDATE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: True
- Inspection error: None
- Nested field paths: 15
- Evidence role verified: NO

### 669626b0885bec44fcef — 1 files
- Representative: `research/case-binance-2026/evidence/eg08_plasma_post_delivery_v1/step05b_atoken_identity_reconciliation_v1/manifest.json`
- Candidate roles: {'MANIFEST_OR_INTEGRITY': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 11
- Evidence role verified: NO

### 67159c3e48d85c0c13e9 — 1 files
- Representative: `research/case-binance-2026/A97B/evidence/bitquery_independent_crosscheck_v1/A97B_BITQUERY_CROSSCHECK_V1.csv`
- Candidate roles: {'UNKNOWN_DATA_ROLE': 1}
- Field hints: {'tx_hash': True, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 15
- Evidence role verified: NO

### 6758bfec0c58d55e5e3a — 1 files
- Representative: `research/case-binance-2026/evidence/binance14_all_receivers_census_v1/step72_a97b_pattern_funding_audit_v1/repeat_destination_patterns.json`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': True}
- Nested sample limited: True
- Inspection error: None
- Nested field paths: 16
- Evidence role verified: NO

### 689f227c917d37d2ad4f — 1 files
- Representative: `research/case-binance-2026/evidence/exploiter16_token_provenance_v1/step19f_middle_hop_receipts_v1/manifest.json`
- Candidate roles: {'MANIFEST_OR_INTEGRITY': 1}
- Field hints: {'tx_hash': False, 'from': True, 'to': True, 'amount': True, 'log_index': True, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: True
- Inspection error: None
- Nested field paths: 22
- Evidence role verified: NO

### 68a628005c3188d48d46 — 1 files
- Representative: `research/case-binance-2026/A97B/dex_transaction_paths_v1/DEX_ADDRESS_SCREENING_UNIVERSE_V1.csv`
- Candidate roles: {'UNKNOWN_DATA_ROLE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 4
- Evidence role verified: NO

### 6908522f275a76027a69 — 1 files
- Representative: `research/case-binance-2026/evidence/binance14_all_receivers_census_v1/step81_a97b_remaining_60_audit_v1/summary.json`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 13
- Evidence role verified: NO

### 6a39d05fcb0c6cfc0652 — 1 files
- Representative: `research/case-binance-2026/evidence/eg08_plasma_post_delivery_v1/step06c_local_fork_freeze_scenarios_v1/destroy_blocked_funds_scenario.json`
- Candidate roles: {'UNKNOWN_DATA_ROLE': 1}
- Field hints: {'tx_hash': True, 'from': False, 'to': False, 'amount': False, 'log_index': True, 'trace': False, 'token': False, 'events': True}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 34
- Evidence role verified: NO

### 6ada2e7498993a5c6e51 — 1 files
- Representative: `research/case-binance-2026/evidence/binance14_all_receivers_census_v1/step69_noncentral_receiver_forward_screen_v1/NONCENTRAL_RECEIVER_SCREEN_V1.csv`
- Candidate roles: {'UNKNOWN_DATA_ROLE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 10
- Evidence role verified: NO

### 6cc50e31677220279453 — 1 files
- Representative: `research/case-binance-2026/evidence/eg08_source_attribution_v1/step08q_large_inflow_origin_windows_v1/summary.json`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': True, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 41
- Evidence role verified: NO

### 6d9d50519c1b9c2290af — 1 files
- Representative: `research/case-binance-2026/evidence/eg08_plasma_post_delivery_v1/step07c_atoken_interest_reconciliation_v1/supply_transaction_checks.json`
- Candidate roles: {'UNKNOWN_DATA_ROLE': 1}
- Field hints: {'tx_hash': True, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 6
- Evidence role verified: NO

### 6dbdf712f27c466b5b53 — 1 files
- Representative: `research/case-binance-2026/A97B/dex_weth_counterparty_audit_v1/WETH_TRANSACTION_ROUTES_V1.csv`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': True, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 12
- Evidence role verified: NO

### 6e512b6f45a5db6553d9 — 1 files
- Representative: `research/case-binance-2026/evidence/binance14_all_receivers_census_v1/step69_noncentral_receiver_forward_screen_v1/manifest.json`
- Candidate roles: {'MANIFEST_OR_INTEGRITY': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 30
- Evidence role verified: NO

### 6e9c67c69fd78359ddb3 — 1 files
- Representative: `research/case-binance-2026/evidence/exploiter16_token_provenance_v1/step16_receipt_evidence_v1/manifest.json`
- Candidate roles: {'MANIFEST_OR_INTEGRITY': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': True, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 14
- Evidence role verified: NO

### 6f542bbc14c2be044eb8 — 1 files
- Representative: `research/case-binance-2026/evidence/binance14_all_receivers_census_v1/step79_a97b_repeat_swap_validation_v1/sample_results.json`
- Candidate roles: {'UNKNOWN_DATA_ROLE': 1}
- Field hints: {'tx_hash': True, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: True
- Inspection error: None
- Nested field paths: 18
- Evidence role verified: NO

### 6faf181d43d8dcdc271b — 1 files
- Representative: `research/case-binance-2026/GATE_2_ERC20_TRANSFER_EVIDENCE_V1.csv`
- Candidate roles: {'UNKNOWN_DATA_ROLE': 1}
- Field hints: {'tx_hash': True, 'from': False, 'to': False, 'amount': True, 'log_index': True, 'trace': False, 'token': True, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 14
- Evidence role verified: NO

### 702ce71be035c3aa804c — 1 files
- Representative: `research/case-binance-2026/A97B/evidence/bitquery_independent_crosscheck_v2/unverified.csv`
- Candidate roles: {'UNKNOWN_DATA_ROLE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 0
- Evidence role verified: NO

### 70644e44525640407fd6 — 1 files
- Representative: `research/case-binance-2026/evidence/second_wallet_tokens_v1/manifest.json`
- Candidate roles: {'MANIFEST_OR_INTEGRITY': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': True, 'events': False}
- Nested sample limited: True
- Inspection error: None
- Nested field paths: 6
- Evidence role verified: NO

### 7169eac921425ea8b752 — 1 files
- Representative: `research/case-binance-2026/GATE_2_TRON_NATIVE_TX_VALIDATION_V1.csv`
- Candidate roles: {'UNKNOWN_DATA_ROLE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 14
- Evidence role verified: NO

### 75c5096219251dd0b2ce — 1 files
- Representative: `research/case-binance-2026/evidence/eg08_source_attribution_v1/step08z_crystal_axiom_crosswalk_v1/summary.json`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 14
- Evidence role verified: NO

### 7628d53db5d9f1b04d6f — 1 files
- Representative: `research/case-binance-2026/evidence/eg08_plasma_post_delivery_v1/step06f_withdrawal_revert_diagnostics_v1/baseline.json`
- Candidate roles: {'RAW_SOURCE_CANDIDATE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 6
- Evidence role verified: NO

### 76ccffac8d641f2a36a8 — 1 files
- Representative: `research/case-binance-2026/evidence/binance14_all_receivers_census_v1/alchemy_asset_transfers_raw.json`
- Candidate roles: {'TRANSFER_SHAPED_CANDIDATE': 1}
- Field hints: {'tx_hash': True, 'from': True, 'to': True, 'amount': True, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: True
- Inspection error: None
- Nested field paths: 17
- Evidence role verified: NO

### 777224bbc4350ce3db2a — 1 files
- Representative: `research/case-binance-2026/A97B/dex_transaction_paths_v1/AUDIT_V1.json`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': True}
- Nested sample limited: True
- Inspection error: None
- Nested field paths: 11
- Evidence role verified: NO

### 7a4480847708967b7aee — 1 files
- Representative: `research/case-binance-2026/evidence/eg08_plasma_post_delivery_v1/step06e_scenario_accounting_reconciliation_v1/provenance.json`
- Candidate roles: {'UNKNOWN_DATA_ROLE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 6
- Evidence role verified: NO

### 7a5a1d788ee05348c53e — 1 files
- Representative: `research/case-binance-2026/evidence/eg08_source_attribution_v1/step08u_recent_supply_event_audit_v1/summary.json`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: True
- Inspection error: None
- Nested field paths: 32
- Evidence role verified: NO

### 7c13034699680b7991ad — 1 files
- Representative: `research/case-binance-2026/evidence/eg08_plasma_post_delivery_v1/step06b_aave_withdraw_callpath_v1/manifest.json`
- Candidate roles: {'MANIFEST_OR_INTEGRITY': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 9
- Evidence role verified: NO

### 7c9242d23391b6618747 — 1 files
- Representative: `research/case-binance-2026/GATE_2_PREINCIDENT_OWNERSHIP_SCREEN_V1.csv`
- Candidate roles: {'UNKNOWN_DATA_ROLE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 10
- Evidence role verified: NO

### 7d77c624b034bf5c80c6 — 1 files
- Representative: `research/case-binance-2026/evidence/eg08_plasma_post_delivery_v1/step07b_post_ledger_gap_audit_v1/summary.json`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 18
- Evidence role verified: NO

### 7eb924adbeee9913a60e — 1 files
- Representative: `research/case-binance-2026/evidence/eg08_source_attribution_v1/step08z_crystal_axiom_crosswalk_v1/attribution_boundary.json`
- Candidate roles: {'UNKNOWN_DATA_ROLE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 18
- Evidence role verified: NO

### 7f8579d3062f85d30a3f — 1 files
- Representative: `research/case-binance-2026/A97B/dex_execution_reconstruction_v1/DEX_EXECUTION_TIMELINE_V1.csv`
- Candidate roles: {'UNKNOWN_DATA_ROLE': 1}
- Field hints: {'tx_hash': True, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 18
- Evidence role verified: NO

### 83465f3a3d8b482ab6cc — 1 files
- Representative: `research/case-binance-2026/evidence/eg08_plasma_post_delivery_v1/step06b_aave_withdraw_callpath_v1/withdrawal_call_trace.json`
- Candidate roles: {'TRANSFER_SHAPED_CANDIDATE': 1}
- Field hints: {'tx_hash': False, 'from': True, 'to': True, 'amount': True, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: True
- Inspection error: None
- Nested field paths: 38
- Evidence role verified: NO

### 83e3da375dbd10c65f7c — 1 files
- Representative: `research/case-binance-2026/A97B/dex_internal_trace_v1/DEX_ALL_TOKEN_TRANSFERS_V1.csv`
- Candidate roles: {'TRANSFER_SHAPED_CANDIDATE': 1}
- Field hints: {'tx_hash': True, 'from': True, 'to': True, 'amount': True, 'log_index': True, 'trace': False, 'token': True, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 9
- Evidence role verified: NO

### 84aa20867ee994f4d481 — 1 files
- Representative: `research/case-binance-2026/A97B/evidence/bitquery_independent_crosscheck_v1/AUDIT_V1.json`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': True, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 36
- Evidence role verified: NO

### 84ed7911201bfc694879 — 1 files
- Representative: `research/case-binance-2026/A97B/bitquery_withdrawal_crosswalk_v1/AUDIT_V1.json`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 16
- Evidence role verified: NO

### 852ca6ffaef39b4767ac — 1 files
- Representative: `research/case-binance-2026/evidence/eg08_plasma_post_delivery_v1/step05_withdrawal_audit_v1/manifest.json`
- Candidate roles: {'MANIFEST_OR_INTEGRITY': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 17
- Evidence role verified: NO

### 866880e4693cedd1f6c3 — 1 files
- Representative: `research/case-binance-2026/A97B/dex_weth_counterparty_audit_v1/WETH_COUNTERPARTY_TOTALS_V1.csv`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': False, 'from': True, 'to': True, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 6
- Evidence role verified: NO

### 872cb2199e7c2812e88b — 1 files
- Representative: `research/case-binance-2026/GATE_2_ADDITIONAL_SOURCE_CLASSIFICATION_V1.csv`
- Candidate roles: {'UNKNOWN_DATA_ROLE': 1}
- Field hints: {'tx_hash': True, 'from': False, 'to': False, 'amount': True, 'log_index': True, 'trace': False, 'token': True, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 15
- Evidence role verified: NO

### 8866b4c9e03e4e14ab96 — 1 files
- Representative: `research/case-binance-2026/evidence/binance14_all_receivers_census_v1/step73_a97b_execution_conservation_v1/execution_pattern_samples.json`
- Candidate roles: {'UNKNOWN_DATA_ROLE': 1}
- Field hints: {'tx_hash': True, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: True
- Inspection error: None
- Nested field paths: 22
- Evidence role verified: NO

### 8abf7d6280c640ff9a78 — 1 files
- Representative: `research/case-binance-2026/A97B/dex_weth_flow_audit_v1/DEX_WETH_EVENT_FLOW_V1.csv`
- Candidate roles: {'TRANSFER_SHAPED_CANDIDATE': 1}
- Field hints: {'tx_hash': True, 'from': True, 'to': True, 'amount': True, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 23
- Evidence role verified: NO

### 8b6a4d0aa75b6dd65175 — 1 files
- Representative: `research/case-binance-2026/evidence/eg08_plasma_post_delivery_v1/step02_transfer_ledger_v1/ledger_summary.json`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': True, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 20
- Evidence role verified: NO

### 8bcbf0367971cee14d9d — 1 files
- Representative: `research/case-binance-2026/evidence/binance14_all_receivers_census_v1/step85_a97b_final_event_audit_v1/summary.json`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: True
- Inspection error: None
- Nested field paths: 36
- Evidence role verified: NO

### 8c2b25ccd4a76a66cba7 — 1 files
- Representative: `research/case-binance-2026/A97B/eth_first_recipient_audit_v1/ETH_FIRST_RECIPIENT_LEDGER_V1.csv`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': True, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 13
- Evidence role verified: NO

### 8c59450814b7e8d813ec — 1 files
- Representative: `research/case-binance-2026/evidence/step71_55m_source_audit_v1/manifest.json`
- Candidate roles: {'MANIFEST_OR_INTEGRITY': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 13
- Evidence role verified: NO

### 8cc2833ccabdbfff5e57 — 1 files
- Representative: `research/case-binance-2026/evidence/eg08_plasma_post_delivery_v1/step05_withdrawal_audit_v1/raw_atoken_user_logs.jsonl`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': True, 'from': False, 'to': False, 'amount': False, 'log_index': True, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 17
- Evidence role verified: NO

### 8cdbefe3995c9e89accb — 1 files
- Representative: `research/case-binance-2026/evidence/eg08_plasma_post_delivery_v1/step05_withdrawal_audit_v1/existing_supply_transactions.json`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': True, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 6
- Evidence role verified: NO

### 8d4e4875bcb53c6080aa — 1 files
- Representative: `research/case-binance-2026/evidence/binance14_all_receivers_census_v1/transfer_events_normalized.csv`
- Candidate roles: {'TRANSFER_SHAPED_CANDIDATE': 1}
- Field hints: {'tx_hash': False, 'from': True, 'to': True, 'amount': True, 'log_index': True, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 14
- Evidence role verified: NO

### 8e314070db0bdc9635d7 — 1 files
- Representative: `research/case-binance-2026/GATE_2_POR_WALLET_MATCH_V1.csv`
- Candidate roles: {'UNKNOWN_DATA_ROLE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 10
- Evidence role verified: NO

### 8ee6f0dedca6089f1163 — 1 files
- Representative: `research/case-binance-2026/evidence/binance14_all_receivers_census_v1/step80_a97b_full_dex_census_v1/transaction_classification.csv`
- Candidate roles: {'UNKNOWN_DATA_ROLE': 1}
- Field hints: {'tx_hash': True, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 10
- Evidence role verified: NO

### 8f4a923dd239b93fd721 — 1 files
- Representative: `research/case-binance-2026/evidence/step76_preincident_inbound_v1/PARTIAL_AUDIT_V1.json`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': True, 'from': False, 'to': False, 'amount': False, 'log_index': True, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 29
- Evidence role verified: NO

### 8f58fca811542fbd21c9 — 1 files
- Representative: `research/case-binance-2026/evidence/eg08_plasma_post_delivery_v1/step07d_final_evidence_consistency_audit_v1/provenance.json`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 5
- Evidence role verified: NO

### 9147fb68e4bd6a37295c — 1 files
- Representative: `research/case-binance-2026/evidence/second_hop_usdt_v1/transfer_logs.json`
- Candidate roles: {'UNKNOWN_DATA_ROLE': 1}
- Field hints: {'tx_hash': True, 'from': False, 'to': False, 'amount': False, 'log_index': True, 'trace': False, 'token': True, 'events': True}
- Nested sample limited: True
- Inspection error: None
- Nested field paths: 16
- Evidence role verified: NO

### 91d554b6b7ae68b51268 — 1 files
- Representative: `research/case-binance-2026/GATE_2_ETH_T03_TRANSFER_EVENT_AUDIT_V1.json`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': True, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: True
- Inspection error: None
- Nested field paths: 19
- Evidence role verified: NO

### 9208ba7ad06ed520461c — 1 files
- Representative: `research/case-binance-2026/analysis/master_flow_map_v1/EVIDENCE_REGISTER_V1.csv`
- Candidate roles: {'UNKNOWN_DATA_ROLE': 1}
- Field hints: {'tx_hash': True, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 10
- Evidence role verified: NO

### 9229e47bd088e3fc086a — 1 files
- Representative: `research/case-binance-2026/evidence/eg08_plasma_post_delivery_v1/step06d_aave_reserve_liquidity_reconciliation_v1/provenance.json`
- Candidate roles: {'UNKNOWN_DATA_ROLE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: True
- Inspection error: None
- Nested field paths: 5
- Evidence role verified: NO

### 939031de175e9ae0f81c — 1 files
- Representative: `research/case-binance-2026/evidence/eg08_plasma_post_delivery_v1/step06a_issuer_freeze_capability_audit_v1/provenance.json`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 7
- Evidence role verified: NO

### 9447477792ed60efad9d — 1 files
- Representative: `research/case-binance-2026/evidence/eg08_source_attribution_v1/step08k_adapter_inbound_receipts_v1/decoded_receipts.json`
- Candidate roles: {'RAW_SOURCE_CANDIDATE': 1}
- Field hints: {'tx_hash': True, 'from': True, 'to': True, 'amount': True, 'log_index': True, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 22
- Evidence role verified: NO

### 945468a944d216f3b235 — 1 files
- Representative: `research/case-binance-2026/evidence/eg08_plasma_post_delivery_v1/step07c_atoken_interest_reconciliation_v1/historical_scaled_snapshots.json`
- Candidate roles: {'UNKNOWN_DATA_ROLE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 9
- Evidence role verified: NO

### 9464bdd83b3d8eb09da5 — 1 files
- Representative: `research/case-binance-2026/evidence/eg08_plasma_post_delivery_v1/step06e_scenario_accounting_reconciliation_v1/manifest.json`
- Candidate roles: {'MANIFEST_OR_INTEGRITY': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 7
- Evidence role verified: NO

### 947adcd623ed9974095e — 1 files
- Representative: `research/case-binance-2026/evidence/binance14_all_receivers_census_v1/step73_a97b_execution_conservation_v1/audit.json`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 12
- Evidence role verified: NO

### 95b83b449b05a2529003 — 1 files
- Representative: `research/case-binance-2026/evidence/eg08_plasma_post_delivery_v1/step06b_aave_withdraw_callpath_v1/source_verification_lookup.json`
- Candidate roles: {'RAW_SOURCE_CANDIDATE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 9
- Evidence role verified: NO

### 976b350c1411a2dc8515 — 1 files
- Representative: `research/case-binance-2026/evidence/eg08_source_attribution_v1/step08k_adapter_inbound_receipts_v1/raw_rpc_evidence.json`
- Candidate roles: {'TRANSFER_SHAPED_CANDIDATE': 1}
- Field hints: {'tx_hash': True, 'from': True, 'to': True, 'amount': True, 'log_index': True, 'trace': False, 'token': False, 'events': True}
- Nested sample limited: True
- Inspection error: None
- Nested field paths: 237
- Evidence role verified: NO

### 97fa2df66a6603e257ea — 1 files
- Representative: `research/case-binance-2026/A97B/public_report_overlap_v1/AUDIT_V1.json`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: True
- Inspection error: None
- Nested field paths: 10
- Evidence role verified: NO

### 98e61ad87c8499408536 — 1 files
- Representative: `research/case-binance-2026/A97B/evidence/bitquery_independent_crosscheck_v2/excluded_existing_16.csv`
- Candidate roles: {'UNKNOWN_DATA_ROLE': 1}
- Field hints: {'tx_hash': True, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 3
- Evidence role verified: NO

### 990a797d7662275cdb32 — 1 files
- Representative: `research/case-binance-2026/GATE_2_ETH_T03_HISTORICAL_BALANCE_AUDIT_V1.json`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': True, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 34
- Evidence role verified: NO

### 99e6832804af2b4374b8 — 1 files
- Representative: `research/case-binance-2026/evidence/eg08_plasma_post_delivery_v1/step05_withdrawal_audit_v1/withdrawal_events.json`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': True, 'from': True, 'to': True, 'amount': True, 'log_index': True, 'trace': False, 'token': True, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 40
- Evidence role verified: NO

### 9ad2d3458949a56016a7 — 1 files
- Representative: `research/case-binance-2026/evidence/eg08_plasma_post_delivery_v1/step02_transfer_ledger_v1/block_timestamp_index.json`
- Candidate roles: {'UNKNOWN_DATA_ROLE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 12
- Evidence role verified: NO

### 9c31168b00d5e6043837 — 1 files
- Representative: `research/case-binance-2026/evidence/eg08_plasma_post_delivery_v1/step06b_aave_withdraw_callpath_v1/implementation_slot_history.json`
- Candidate roles: {'RAW_SOURCE_CANDIDATE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 110
- Evidence role verified: NO

### 9d2ca1b838881be030dc — 1 files
- Representative: `research/case-binance-2026/evidence/binance14_all_receivers_census_v1/step83_official_attribution_crosswalk_v1/summary.json`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 27
- Evidence role verified: NO

### 9e7b0abd70343a8da1f1 — 1 files
- Representative: `research/case-binance-2026/investigation_workspace_v1/WORKSPACE_MANIFEST.json`
- Candidate roles: {'MANIFEST_OR_INTEGRITY': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 15
- Evidence role verified: NO

### 9f298840680b846cd216 — 1 files
- Representative: `research/case-binance-2026/evidence/initial_tx_v1/token_inventory.csv`
- Candidate roles: {'UNKNOWN_DATA_ROLE': 1}
- Field hints: {'tx_hash': False, 'from': True, 'to': True, 'amount': False, 'log_index': True, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 11
- Evidence role verified: NO

### 9f43f24680447b399fb1 — 1 files
- Representative: `research/case-binance-2026/evidence/eg08_plasma_post_delivery_v1/step07d_final_evidence_consistency_audit_v1/claim_classification_matrix.json`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: True
- Inspection error: None
- Nested field paths: 4
- Evidence role verified: NO

### a04dc5ed21155d65a178 — 1 files
- Representative: `research/case-binance-2026/evidence/eg08_source_attribution_v1/step08o_multichain_funding_window_v1/summary.json`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: True
- Inspection error: None
- Nested field paths: 41
- Evidence role verified: NO

### a089473be61eb6e77e3f — 1 files
- Representative: `research/case-binance-2026/A97B/evidence/bitquery_independent_audit_v1/audit_results.csv`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': True, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 5
- Evidence role verified: NO

### a1e8bd7ae1515e6c4603 — 1 files
- Representative: `research/case-binance-2026/evidence/binance14_all_receivers_census_v1/step79_a97b_repeat_swap_validation_v1/audit.json`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 8
- Evidence role verified: NO

### a1ebbd2796e5c2647c82 — 1 files
- Representative: `research/case-binance-2026/evidence/eg08_plasma_post_delivery_v1/step06d_aave_reserve_liquidity_reconciliation_v1/raw_reserve_data.json`
- Candidate roles: {'RAW_SOURCE_CANDIDATE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: True
- Inspection error: None
- Nested field paths: 3
- Evidence role verified: NO

### a59ca965d608078ddb68 — 1 files
- Representative: `research/case-binance-2026/evidence/binance14_all_receivers_census_v1/step66_receiver_identity_rpc_audit_v1/manifest.json`
- Candidate roles: {'MANIFEST_OR_INTEGRITY': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 24
- Evidence role verified: NO

### a654f13875ed36337a96 — 1 files
- Representative: `research/case-binance-2026/A97B/institutional_research_packet_v1/AUDIT_V1.json`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 19
- Evidence role verified: NO

### a6aa0c42b71f11945f0a — 1 files
- Representative: `research/case-binance-2026/GATE_2_ADDITIONAL_SOURCE_EVENT_AUDIT_V1.csv`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': True, 'from': False, 'to': False, 'amount': True, 'log_index': True, 'trace': False, 'token': True, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 13
- Evidence role verified: NO

### a710af86685e34b5753e — 1 files
- Representative: `research/case-binance-2026/evidence/eg08_plasma_post_delivery_v1/step05_withdrawal_audit_v1/other_pool_events_for_user.json`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': True, 'from': False, 'to': False, 'amount': False, 'log_index': True, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 16
- Evidence role verified: NO

### a82ba350bde84271e380 — 1 files
- Representative: `research/case-binance-2026/evidence/binance14_all_receivers_census_v1/step65_direct_receiver_route_register_v1/DIRECT_RECEIVER_REGISTER_V1.csv`
- Candidate roles: {'UNKNOWN_DATA_ROLE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 14
- Evidence role verified: NO

### a893e68970024f5ffc92 — 1 files
- Representative: `research/case-binance-2026/evidence/eg08_plasma_post_delivery_v1/step02_transfer_ledger_v1/transfer_ledger.json`
- Candidate roles: {'TRANSFER_SHAPED_CANDIDATE': 1}
- Field hints: {'tx_hash': False, 'from': True, 'to': True, 'amount': True, 'log_index': True, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 12
- Evidence role verified: NO

### aa82cb0346f49757d7a0 — 1 files
- Representative: `research/case-binance-2026/evidence/eg08_plasma_post_delivery_v1/step05c_burn_interest_event_reconciliation_v1/decoded_events.json`
- Candidate roles: {'TRANSFER_SHAPED_CANDIDATE': 1}
- Field hints: {'tx_hash': True, 'from': True, 'to': True, 'amount': True, 'log_index': True, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 26
- Evidence role verified: NO

### ab0f04ba60a7f8aefd4b — 1 files
- Representative: `research/case-binance-2026/evidence/eg08_source_attribution_v1/step08y_forward_edge_preservation_v1/outgoing_scan_coverage.json`
- Candidate roles: {'UNKNOWN_DATA_ROLE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 16
- Evidence role verified: NO

### ac6faf1ff4e0877af6c7 — 1 files
- Representative: `research/case-binance-2026/evidence/step76_preincident_inbound_v1/checkpoint.json`
- Candidate roles: {'UNKNOWN_DATA_ROLE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 10
- Evidence role verified: NO

### ac8e7ab6022d0c41be17 — 1 files
- Representative: `research/case-binance-2026/A97B/dex_internal_trace_v1/DEX_TRANSACTION_TRACE_SUMMARY_V1.csv`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': True, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 6
- Evidence role verified: NO

### acc2ab9cef348636c49c — 1 files
- Representative: `research/case-binance-2026/evidence/binance14_all_receivers_census_v1/step80_a97b_full_dex_census_v1/summary.json`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 17
- Evidence role verified: NO

### ada76555795fc9be9d28 — 1 files
- Representative: `research/case-binance-2026/evidence/eg08_plasma_delivery_v1/layerzero_message.json`
- Candidate roles: {'UNKNOWN_DATA_ROLE': 1}
- Field hints: {'tx_hash': False, 'from': True, 'to': False, 'amount': True, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 114
- Evidence role verified: NO

### ae4f0125e58f597b0816 — 1 files
- Representative: `research/case-binance-2026/A97B/evidence/bitquery_independent_crosscheck_v2/reconciliation.csv`
- Candidate roles: {'UNKNOWN_DATA_ROLE': 1}
- Field hints: {'tx_hash': True, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 19
- Evidence role verified: NO

### ae9937519699d60eec1c — 1 files
- Representative: `research/case-binance-2026/A97B/dex_weth_settlement_audit_v1/DEX_WETH_SETTLEMENT_TIMELINE_V1.csv`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': True, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 16
- Evidence role verified: NO

### aec0b3e65d4ea6da9025 — 1 files
- Representative: `research/case-binance-2026/evidence/eg08_plasma_post_delivery_v1/step06c_local_fork_freeze_scenarios_v1/fork_restoration.json`
- Candidate roles: {'UNKNOWN_DATA_ROLE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 6
- Evidence role verified: NO

### af6598e309319290c587 — 1 files
- Representative: `research/case-binance-2026/evidence/binance14_all_receivers_census_v1/audit.json`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 17
- Evidence role verified: NO

### af7bad1854e672ebe53c — 1 files
- Representative: `research/case-binance-2026/A97B/integrated_event_audit_v1/MANIFEST_V1.json`
- Candidate roles: {'MANIFEST_OR_INTEGRITY': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 115
- Evidence role verified: NO

### b001f98c1d6e62f48701 — 1 files
- Representative: `research/case-binance-2026/A97B/dex_execution_reconstruction_v1/AUDIT_V1.json`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': True}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 7
- Evidence role verified: NO

### b009bc654111c14f55f4 — 1 files
- Representative: `research/case-binance-2026/evidence/eg08_plasma_post_delivery_v1/step05c_burn_interest_event_reconciliation_v1/interest_netting_calculation.json`
- Candidate roles: {'UNKNOWN_DATA_ROLE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 14
- Evidence role verified: NO

### b3f3f20f6e8c432d0c62 — 1 files
- Representative: `research/case-binance-2026/A97B/public_report_overlap_v1/PUBLIC_REPORT_TX_HASH_MATCHES_V1.csv`
- Candidate roles: {'UNKNOWN_DATA_ROLE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 0
- Evidence role verified: NO

### b4a927e0b23828fccca1 — 1 files
- Representative: `research/case-binance-2026/A97B/dex_route_mechanism_v1/AUDIT_V1.json`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 11
- Evidence role verified: NO

### b75159830bcf37cd1795 — 1 files
- Representative: `research/case-binance-2026/evidence/eg08_source_attribution_v1/step08w_incident_attribution_crosswalk_v1/existing_evidence_index.json`
- Candidate roles: {'UNKNOWN_DATA_ROLE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: True
- Inspection error: None
- Nested field paths: 32
- Evidence role verified: NO

### b7c765f6e06eb62595b5 — 1 files
- Representative: `research/case-binance-2026/A97B/institutional_research_packet_v1/A97B_HOURLY_FLOW_SUMMARY_V1.csv`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 5
- Evidence role verified: NO

### b959df503608a4a6361e — 1 files
- Representative: `research/case-binance-2026/evidence/eg08_plasma_post_delivery_v1/step06a_issuer_freeze_capability_audit_v1/contract_code_inventory.json`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 25
- Evidence role verified: NO

### b99f19c7aa8754467715 — 1 files
- Representative: `research/case-binance-2026/A97B/institutional_research_packet_v1/A97B_ETH_TRANSACTION_TIMELINE_V1.csv`
- Candidate roles: {'UNKNOWN_DATA_ROLE': 1}
- Field hints: {'tx_hash': True, 'from': True, 'to': True, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 9
- Evidence role verified: NO

### b9c4c7cfab7e296c6e30 — 1 files
- Representative: `research/case-binance-2026/A97B/dex_external_screening_v1/DEX_ADDRESS_EXTERNAL_LISTING_V1.csv`
- Candidate roles: {'UNKNOWN_DATA_ROLE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 6
- Evidence role verified: NO

### bc0336b2bd5e7150c980 — 1 files
- Representative: `research/case-binance-2026/evidence/eg03_two_address_consolidation_v1/previous_terminal_audit_summary.json`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 11
- Evidence role verified: NO

### bcc9df9648453e7dd836 — 1 files
- Representative: `research/case-binance-2026/evidence/additional_stablecoins_v1/manifest.json`
- Candidate roles: {'MANIFEST_OR_INTEGRITY': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': True, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 9
- Evidence role verified: NO

### bda0b3f323eb120899ad — 1 files
- Representative: `research/case-binance-2026/evidence/binance14_all_receivers_census_v1/step70_a97b_forward_census_v1/audit.json`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: True
- Inspection error: None
- Nested field paths: 14
- Evidence role verified: NO

### bde4a1ccaeb9ebe9107c — 1 files
- Representative: `research/case-binance-2026/evidence/eg08_source_attribution_v1/step08w_incident_attribution_crosswalk_v1/summary.json`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 13
- Evidence role verified: NO

### be0584aa907eafe31733 — 1 files
- Representative: `research/case-binance-2026/evidence/eg08_plasma_post_delivery_v1/step06b_issuer_control_simulation_v1/owner_identity.json`
- Candidate roles: {'UNKNOWN_DATA_ROLE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 3
- Evidence role verified: NO

### be6e9b4bb6147d7bfe24 — 1 files
- Representative: `research/case-binance-2026/A97B/ledger_v1/A97B_EVENT_TIMELINE_V1.csv`
- Candidate roles: {'TRANSFER_SHAPED_CANDIDATE': 1}
- Field hints: {'tx_hash': True, 'from': True, 'to': True, 'amount': True, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 16
- Evidence role verified: NO

### beda2b2e1480ac2207fb — 1 files
- Representative: `research/case-binance-2026/evidence/binance14_all_receivers_census_v1/step83_official_attribution_crosswalk_v1/address_attribution_crosswalk.csv`
- Candidate roles: {'UNKNOWN_DATA_ROLE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 7
- Evidence role verified: NO

### bf1aecc5c8fc8b7f1721 — 1 files
- Representative: `research/case-binance-2026/evidence/eg08_source_attribution_v1/step08l_crosschain_message_decode_v1/summary.json`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 14
- Evidence role verified: NO

### c0a8d97678b13b0d2fe0 — 1 files
- Representative: `research/case-binance-2026/evidence/eg08_source_attribution_v1/step08y_forward_edge_preservation_v1/forward_candidates.json`
- Candidate roles: {'UNKNOWN_DATA_ROLE': 1}
- Field hints: {'tx_hash': False, 'from': True, 'to': True, 'amount': False, 'log_index': True, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 49
- Evidence role verified: NO

### c1ef6eaaf3d6bfdeae8e — 1 files
- Representative: `research/case-binance-2026/A97B/eth_first_recipient_audit_v1/ETH_FIRST_RECIPIENT_SUMMARY_V1.csv`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 4
- Evidence role verified: NO

### c399b3cced9686aa1b14 — 1 files
- Representative: `research/case-binance-2026/GATE_2_POR_SOURCE_MANIFEST_V1.json`
- Candidate roles: {'MANIFEST_OR_INTEGRITY': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 12
- Evidence role verified: NO

### c48c23ba4f301e3cfa69 — 1 files
- Representative: `research/case-binance-2026/FOLLOW_ON_FLOW_LEDGER_V1.csv`
- Candidate roles: {'UNKNOWN_DATA_ROLE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 9
- Evidence role verified: NO

### c579568298ba973cfa3c — 1 files
- Representative: `research/case-binance-2026/GATE_2_ETH_T03_FAILURE_TOLERANCE_V1.json`
- Candidate roles: {'UNKNOWN_DATA_ROLE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': True, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 21
- Evidence role verified: NO

### c7b96fd99c7e57fd94cc — 1 files
- Representative: `research/case-binance-2026/GATE_2_BITCOIN_11TX_INPUT_OUTPUT_AUDIT_V1.csv`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 16
- Evidence role verified: NO

### cafcde05e4ca27fc0747 — 1 files
- Representative: `research/case-binance-2026/evidence/binance14_all_receivers_census_v1/all_receivers_summary.csv`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 9
- Evidence role verified: NO

### ce1cf88a77ab20ea3c28 — 1 files
- Representative: `research/case-binance-2026/evidence/eg08_source_attribution_v1/step08ac_ethereum_atoken_position_origin_v1/position_origin_audit.json`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: True
- Inspection error: None
- Nested field paths: 38
- Evidence role verified: NO

### cf3959395545aee1e311 — 1 files
- Representative: `research/case-binance-2026/A97B/economic_flow_v1/A97B_ACTUAL_MOVEMENT_EVENTS_V1.csv`
- Candidate roles: {'TRANSFER_SHAPED_CANDIDATE': 1}
- Field hints: {'tx_hash': True, 'from': True, 'to': True, 'amount': True, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 16
- Evidence role verified: NO

### cf91c0a6c49619b352eb — 1 files
- Representative: `research/case-binance-2026/evidence/eg08_plasma_post_delivery_v1/step06a_issuer_freeze_capability_audit_v1/chain_identity.json`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 4
- Evidence role verified: NO

### cfbe0d2819ef5297ccfb — 1 files
- Representative: `research/case-binance-2026/evidence/eg08_plasma_post_delivery_v1/step07c_atoken_interest_reconciliation_v1/reconciliation.json`
- Candidate roles: {'UNKNOWN_DATA_ROLE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: True
- Inspection error: None
- Nested field paths: 23
- Evidence role verified: NO

### d1429a8eddc6be62a915 — 1 files
- Representative: `research/case-binance-2026/evidence/eg08_plasma_post_delivery_v1/step06d_aave_reserve_liquidity_reconciliation_v1/reserve_snapshots.json`
- Candidate roles: {'UNKNOWN_DATA_ROLE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: True
- Inspection error: None
- Nested field paths: 33
- Evidence role verified: NO

### d15bae8744616dbcdb31 — 1 files
- Representative: `research/case-binance-2026/evidence/eg08_plasma_post_delivery_v1/step06e_scenario_accounting_reconciliation_v1/live_state_latest.json`
- Candidate roles: {'UNKNOWN_DATA_ROLE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 27
- Evidence role verified: NO

### d2e43a1a0c04c0919252 — 1 files
- Representative: `research/case-binance-2026/A97B/eth_address_receipts_v1/CHECKPOINT_MANIFEST_V1.json`
- Candidate roles: {'MANIFEST_OR_INTEGRITY': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 36
- Evidence role verified: NO

### d2f4c23fa8b3c0a11b63 — 1 files
- Representative: `research/case-binance-2026/A97B/dex_transfer_sequence_audit_v1/AUDIT_V1.json`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 8
- Evidence role verified: NO

### d302c28ab3b02cdb2dee — 1 files
- Representative: `research/case-binance-2026/evidence/eg08_plasma_post_delivery_v1/step07a_28m_conservation_audit_v1/summary.json`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 9
- Evidence role verified: NO

### d39cf4c3414959d82cc3 — 1 files
- Representative: `research/case-binance-2026/evidence/eg08_source_attribution_v1/step08y_forward_edge_preservation_v1/raw_intermediate_receipts.json`
- Candidate roles: {'TRANSACTION_ENVELOPE_CANDIDATE': 1}
- Field hints: {'tx_hash': True, 'from': True, 'to': True, 'amount': False, 'log_index': True, 'trace': False, 'token': False, 'events': True}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 125
- Evidence role verified: NO

### d43275d3d583b53faf63 — 1 files
- Representative: `research/case-binance-2026/evidence/eg08_plasma_post_delivery_v1/step06a_issuer_freeze_capability_audit_v1/manifest.json`
- Candidate roles: {'MANIFEST_OR_INTEGRITY': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 16
- Evidence role verified: NO

### d43cf6cc9a8c9afecd96 — 1 files
- Representative: `research/case-binance-2026/analysis/master_timeline_v0/AUDIT_V0.json`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: True
- Inspection error: None
- Nested field paths: 19
- Evidence role verified: NO

### d4f35445b28b5cff88ee — 1 files
- Representative: `research/case-binance-2026/evidence/eg08_source_attribution_v1/step08r_aave_mantle_receipt_audit_v1/decoded_transaction_context.json`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': False, 'from': True, 'to': True, 'amount': True, 'log_index': True, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 25
- Evidence role verified: NO

### d609d2d3e468be8faedc — 1 files
- Representative: `research/case-binance-2026/A97B/dex_weth_flow_audit_v1/DEX_WETH_HOURLY_V1.csv`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': True}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 4
- Evidence role verified: NO

### d6efe9b1f2a7af533cf1 — 1 files
- Representative: `research/case-binance-2026/evidence/binance14_all_receivers_census_v1/step84_a97b_erc20_exception_audit_v1/manifest.json`
- Candidate roles: {'MANIFEST_OR_INTEGRITY': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 9
- Evidence role verified: NO

### d711559f2f6ea086953f — 1 files
- Representative: `research/case-binance-2026/GATE_2_INITIAL_TX_ONCHAIN_VALIDATION_V1.csv`
- Candidate roles: {'UNKNOWN_DATA_ROLE': 1}
- Field hints: {'tx_hash': True, 'from': True, 'to': True, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 18
- Evidence role verified: NO

### d71dc074e1b52ab7f523 — 1 files
- Representative: `research/case-binance-2026/A97B/evidence/bitquery_independent_crosscheck_v2/request_manifest.json`
- Candidate roles: {'MANIFEST_OR_INTEGRITY': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: True
- Inspection error: None
- Nested field paths: 36
- Evidence role verified: NO

### d76a9698ac6ed48a2f3e — 1 files
- Representative: `research/case-binance-2026/evidence/step76_preincident_inbound_v1/meta.json`
- Candidate roles: {'UNKNOWN_DATA_ROLE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 7
- Evidence role verified: NO

### d7abe59a5f255013e4d8 — 1 files
- Representative: `research/case-binance-2026/GATE_2_ETH_HISTORICAL_CODE_AUDIT_V1.json`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 25
- Evidence role verified: NO

### d7dcb746a508b5ac4b76 — 1 files
- Representative: `research/case-binance-2026/GATE_2_ETH_T02_NONCE_GAP_AUDIT_V1.json`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 15
- Evidence role verified: NO

### d9dddcd359424b6ef7b4 — 1 files
- Representative: `research/case-binance-2026/evidence/eg08_plasma_post_delivery_v1/step05a_withdrawal_anomaly_reconciliation_v1/withdrawal_receipt_transfer_decoding.json`
- Candidate roles: {'TRANSFER_SHAPED_CANDIDATE': 1}
- Field hints: {'tx_hash': False, 'from': True, 'to': True, 'amount': True, 'log_index': True, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 9
- Evidence role verified: NO

### da9974e6ffe5cb62f841 — 1 files
- Representative: `research/case-binance-2026/A97B/ledger_v1/A97B_LEDGER_AUDIT_V1.json`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 11
- Evidence role verified: NO

### db04952a324eb333d5c9 — 1 files
- Representative: `research/case-binance-2026/A97B/dex_weth_counterparty_audit_v1/AUDIT_V1.json`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 8
- Evidence role verified: NO

### dcf89add7439edf89bcb — 1 files
- Representative: `research/case-binance-2026/evidence/eg08_plasma_post_delivery_v1/step05b_atoken_identity_reconciliation_v1/summary.json`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 53
- Evidence role verified: NO

### dda9db91e5078c19a3b0 — 1 files
- Representative: `research/case-binance-2026/A97B/ledger_v1/A97B_HOURLY_EVENT_COUNTS_V1.csv`
- Candidate roles: {'UNKNOWN_DATA_ROLE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 4
- Evidence role verified: NO

### ddbb7bd1f97b584c1924 — 1 files
- Representative: `research/case-binance-2026/evidence/binance14_all_receivers_census_v1/step79_a97b_repeat_swap_validation_v1/manifest.json`
- Candidate roles: {'MANIFEST_OR_INTEGRITY': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 43
- Evidence role verified: NO

### ddc012acbe2f7e1521c6 — 1 files
- Representative: `research/case-binance-2026/A97B/evidence/bitquery_independent_crosscheck_v1/SHA256_MANIFEST_V1.json`
- Candidate roles: {'MANIFEST_OR_INTEGRITY': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 10
- Evidence role verified: NO

### dde495e42aa5dbae42eb — 1 files
- Representative: `research/case-binance-2026/evidence/binance14_all_receivers_census_v1/step77_a97b_dex_swap_evidence_v1/erc20_transfer_events.csv`
- Candidate roles: {'TRANSFER_SHAPED_CANDIDATE': 1}
- Field hints: {'tx_hash': True, 'from': True, 'to': True, 'amount': True, 'log_index': True, 'trace': False, 'token': True, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 9
- Evidence role verified: NO

### de822c05070d573a1bf1 — 1 files
- Representative: `research/case-binance-2026/evidence/eg02_historical_balances_v1/manifest.json`
- Candidate roles: {'MANIFEST_OR_INTEGRITY': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 8
- Evidence role verified: NO

### e2d6220e030e274b9c61 — 1 files
- Representative: `research/case-binance-2026/evidence/eg08_source_attribution_v1/step08w_incident_attribution_crosswalk_v1/attribution_gates.json`
- Candidate roles: {'UNKNOWN_DATA_ROLE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 3
- Evidence role verified: NO

### e310b73a3b97d014c743 — 1 files
- Representative: `research/case-binance-2026/evidence/root_usdt_outflows_v1/manifest.json`
- Candidate roles: {'MANIFEST_OR_INTEGRITY': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': True, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 10
- Evidence role verified: NO

### e369aedb967d9fa2b89e — 1 files
- Representative: `research/case-binance-2026/A97B/bitquery_withdrawal_crosswalk_v1/A97B_DIRECT_ETH_WITHDRAWAL_CROSSWALK_V1.csv`
- Candidate roles: {'RAW_SOURCE_CANDIDATE': 1}
- Field hints: {'tx_hash': True, 'from': True, 'to': True, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 10
- Evidence role verified: NO

### e389d2f5aae0548701ad — 1 files
- Representative: `research/case-binance-2026/evidence/binance14_all_receivers_census_v1/step84_a97b_erc20_exception_audit_v1/summary.json`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': True}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 12
- Evidence role verified: NO

### e42293819a8a6b583bca — 1 files
- Representative: `research/case-binance-2026/A97B/public_report_overlap_v1/PUBLIC_REPORT_SOURCE_CROSSWALK_V1.csv`
- Candidate roles: {'UNKNOWN_DATA_ROLE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 12
- Evidence role verified: NO

### e5a1eeb9a8dc52348443 — 1 files
- Representative: `research/case-binance-2026/evidence/eg08_plasma_post_delivery_v1/step05a_withdrawal_anomaly_reconciliation_v1/anomaly_reconciliation_summary.json`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': True, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 38
- Evidence role verified: NO

### e68105dd333cd69a7a13 — 1 files
- Representative: `research/case-binance-2026/A97B/dex_transaction_paths_v1/DEX_MISSING_RECEIPTS_V1.csv`
- Candidate roles: {'RAW_SOURCE_CANDIDATE': 1}
- Field hints: {'tx_hash': True, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 3
- Evidence role verified: NO

### e6a9034f92fc202ca030 — 1 files
- Representative: `research/case-binance-2026/evidence/eg08_plasma_post_delivery_v1/step05a_withdrawal_anomaly_reconciliation_v1/historical_balance_snapshots.json`
- Candidate roles: {'RAW_SOURCE_CANDIDATE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 10
- Evidence role verified: NO

### e8b3ca23d8a6ff63f056 — 1 files
- Representative: `research/case-binance-2026/evidence/eg08_plasma_post_delivery_v1/step06a_issuer_freeze_capability_audit_v1/event_scan_summary.json`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: True
- Inspection error: None
- Nested field paths: 16
- Evidence role verified: NO

### e94d3dd22f9b323131bd — 1 files
- Representative: `research/case-binance-2026/evidence/blacklist_balance_175m_v1/balance_snapshots.json`
- Candidate roles: {'UNKNOWN_DATA_ROLE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': True, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 12
- Evidence role verified: NO

### ecc92e6b5effb3b7bc0f — 1 files
- Representative: `research/case-binance-2026/evidence/eg08_plasma_post_delivery_v1/step06b_aave_withdraw_callpath_v1/provenance.json`
- Candidate roles: {'RAW_SOURCE_CANDIDATE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 17
- Evidence role verified: NO

### ed4e50676a23d829cb66 — 1 files
- Representative: `research/case-binance-2026/evidence/eg08_plasma_post_delivery_v1/step06c_local_fork_freeze_scenarios_v1/freeze_scenarios.json`
- Candidate roles: {'UNKNOWN_DATA_ROLE': 1}
- Field hints: {'tx_hash': True, 'from': False, 'to': False, 'amount': False, 'log_index': True, 'trace': False, 'token': False, 'events': True}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 34
- Evidence role verified: NO

### ede65d168cf306cf692b — 1 files
- Representative: `research/case-binance-2026/A97B/dex_route_mechanism_v1/WETH_RECEIVER_RANKING_V1.csv`
- Candidate roles: {'UNKNOWN_DATA_ROLE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 4
- Evidence role verified: NO

### edebd042f44731243066 — 1 files
- Representative: `research/case-binance-2026/evidence/eg08_plasma_post_delivery_v1/step06a_issuer_freeze_capability_audit_v1/historical_control_snapshots.json`
- Candidate roles: {'TRANSACTION_ENVELOPE_CANDIDATE': 1}
- Field hints: {'tx_hash': True, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: True
- Inspection error: None
- Nested field paths: 1407
- Evidence role verified: NO

### edf36f40accd553726c2 — 1 files
- Representative: `research/case-binance-2026/evidence/step75a_official_report_crosswalk_v1/crosswalk.json`
- Candidate roles: {'UNKNOWN_DATA_ROLE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 29
- Evidence role verified: NO

### ee4d0a35f385356e6334 — 1 files
- Representative: `research/case-binance-2026/evidence/eg08_plasma_post_delivery_v1/step02_transfer_ledger_v1/transfer_ledger.csv`
- Candidate roles: {'TRANSFER_SHAPED_CANDIDATE': 1}
- Field hints: {'tx_hash': False, 'from': True, 'to': True, 'amount': True, 'log_index': True, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 11
- Evidence role verified: NO

### ee8de910d08a066789e2 — 1 files
- Representative: `research/case-binance-2026/GATE_2_ETH_T02_SIGNATURE_RECOVERY_V1.json`
- Candidate roles: {'UNKNOWN_DATA_ROLE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: True
- Inspection error: None
- Nested field paths: 26
- Evidence role verified: NO

### ef46bfcf681b4d18d4bc — 1 files
- Representative: `research/case-binance-2026/evidence/eg08_source_attribution_v1/step08m_source_message_lookup_v1/source_message_candidates.json`
- Candidate roles: {'UNKNOWN_DATA_ROLE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': True, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: True
- Inspection error: None
- Nested field paths: 13
- Evidence role verified: NO

### efa463bf39384a6ea5a7 — 1 files
- Representative: `research/case-binance-2026/evidence/eg02_central_post_blacklist_ledger_v1/transfer_ledger.json`
- Candidate roles: {'UNKNOWN_DATA_ROLE': 1}
- Field hints: {'tx_hash': True, 'from': True, 'to': False, 'amount': False, 'log_index': True, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 6
- Evidence role verified: NO

### eff99dcf61095d127ae4 — 1 files
- Representative: `research/case-binance-2026/evidence/step72_external_attribution_v1/attribution_audit.json`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 26
- Evidence role verified: NO

### f0bede77d68e55931d0a — 1 files
- Representative: `research/case-binance-2026/GATE_2_NEW_TX_ONCHAIN_SCREEN_V1.csv`
- Candidate roles: {'UNKNOWN_DATA_ROLE': 1}
- Field hints: {'tx_hash': True, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 16
- Evidence role verified: NO

### f21b22107e5b45f25191 — 1 files
- Representative: `research/case-binance-2026/evidence/eg08_source_attribution_v1/step08v_atoken_inbound_crosscheck_v1/summary.json`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 7
- Evidence role verified: NO

### f325a9bd714919823593 — 1 files
- Representative: `research/case-binance-2026/evidence/binance14_all_receivers_census_v1/step80_a97b_full_dex_census_v1/manifest.json`
- Candidate roles: {'MANIFEST_OR_INTEGRITY': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 2139
- Evidence role verified: NO

### f3362712263f27f6280f — 1 files
- Representative: `research/case-binance-2026/evidence/eg08_source_attribution_v1/step08e_upstream_3000_blocks_v1/summary.json`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 21
- Evidence role verified: NO

### f33e281502bff84ee87d — 1 files
- Representative: `research/case-binance-2026/evidence/initial_tx_v1/call_trace.json`
- Candidate roles: {'TRANSFER_SHAPED_CANDIDATE': 1}
- Field hints: {'tx_hash': False, 'from': True, 'to': True, 'amount': True, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: True
- Inspection error: None
- Nested field paths: 25
- Evidence role verified: NO

### f3d8a7033b6ba455a17b — 1 files
- Representative: `research/case-binance-2026/evidence/binance14_all_receivers_census_v1/step68_elliptic_address_crosswalk_v1/DIRECT_RECEIVER_ELLIPTIC_CROSSWALK_V1.csv`
- Candidate roles: {'UNKNOWN_DATA_ROLE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 4
- Evidence role verified: NO

### f4030c1b0498ba4e961d — 1 files
- Representative: `research/case-binance-2026/evidence/eg08_source_attribution_v1/step08w_incident_attribution_crosswalk_v1/verified_a_to_b_receipt.json`
- Candidate roles: {'TRANSFER_SHAPED_CANDIDATE': 1}
- Field hints: {'tx_hash': True, 'from': True, 'to': True, 'amount': True, 'log_index': True, 'trace': False, 'token': False, 'events': True}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 61
- Evidence role verified: NO

### f828dc4fd752e0b43141 — 1 files
- Representative: `research/case-binance-2026/A97B/dex_internal_trace_v1/AUDIT_V1.json`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 11
- Evidence role verified: NO

### f8b6c2554aed3c3bc90d — 1 files
- Representative: `research/case-binance-2026/evidence/30m_upstream_bridge_v1/manifest.json`
- Candidate roles: {'MANIFEST_OR_INTEGRITY': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': True, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 17
- Evidence role verified: NO

### f8bab8324b775e4ce17c — 1 files
- Representative: `research/case-binance-2026/A97B/dex_weth_settlement_audit_v1/AUDIT_V1.json`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 9
- Evidence role verified: NO

### f9f24e37205adaa9cfb6 — 1 files
- Representative: `research/case-binance-2026/evidence/step72_external_attribution_v1/manifest.json`
- Candidate roles: {'MANIFEST_OR_INTEGRITY': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 5
- Evidence role verified: NO

### fa8507d0d2ce3b2e848b — 1 files
- Representative: `research/case-binance-2026/evidence/eg08_plasma_post_delivery_v1/provenance.json`
- Candidate roles: {'UNKNOWN_DATA_ROLE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': True, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 15
- Evidence role verified: NO

### fa9f409479357858f9db — 1 files
- Representative: `research/case-binance-2026/evidence/eg08_plasma_post_delivery_v1/step06c_local_fork_freeze_scenarios_v1/fork_context.json`
- Candidate roles: {'UNKNOWN_DATA_ROLE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 12
- Evidence role verified: NO

### ff386374a25ac9e545c6 — 1 files
- Representative: `research/case-binance-2026/evidence/eg08_source_attribution_v1/step08l_crosschain_message_decode_v1/decoded_crosschain_messages.json`
- Candidate roles: {'UNKNOWN_DATA_ROLE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': True, 'amount': True, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 17
- Evidence role verified: NO

### ff6648ed866d35a92c0b — 1 files
- Representative: `research/case-binance-2026/evidence/binance14_all_receivers_census_v1/step70_a97b_forward_census_v1/A97B_ASSET_SUMMARY_V1.csv`
- Candidate roles: {'AUDIT_OR_DERIVED_CANDIDATE': 1}
- Field hints: {'tx_hash': False, 'from': False, 'to': False, 'amount': False, 'log_index': False, 'trace': False, 'token': False, 'events': False}
- Nested sample limited: False
- Inspection error: None
- Nested field paths: 6
- Evidence role verified: NO
