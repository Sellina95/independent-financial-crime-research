# AXIOM — Gate 2 Additional Token Source Role Review V1

## Scope
- Ten ERC20 Transfer-shaped events from seven Ethereum transactions.
- No wallet ownership or criminal attribution inferred.
- Report context is third-party interpretation, not on-chain proof.
- Amounts are raw token units; no USD valuation.
- Existing 700M USDT evidence is not changed.

## Address-level evidence

### 1. `0x0729e2a4716d9f7dd17858d5d504426d228697f7`
- Transaction: `0x9a3dbf99edd0c063171d61130d82f1e6edd7cb409af5e7f2f95acd89e9584d8a`
- Token contract: `0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48`
- Destination: `0x8f10b468b06c6fd214b65f87778827f7d113f996`
- Raw amount: `14866823298`
- Transaction caller: `0xa5a5491bca93dd4c076e4906e79e7673f4a5a142`
- Prior text-based classification: OTHER_OR_UNRESOLVED
- External context: FSiRzmJNSEBAFmrDbLkQ672iPN8H TRON contract the hacker passed 57M TRX through, 31 Oct TNhpfKq83wufEKGjBhQFnT7jnxYmyBzH6F Payout address that used it 55abdfbd684ad3f49323390964297098692ac189874a6ee6fe9b0b00de816070 A Relay deposit, 15:22 UTC on 31 Oct 0x9a3dbf99edd0c063171d61130d82f1e6edd7cb409af5e7f2
- Token contract/decimals: NOT VERIFIED
- Role: PENDING_INDEPENDENT_CLASSIFICATION
- Binance ownership: UNKNOWN
- Incident attribution: UNKNOWN

### 2. `0x4d5f47fa6a74757f35c14fd3a6ef8e3c9bc514e8`
- Transaction: `0xa85ad4807b33ad63ba2b2ffbac63d913285eefe44d7e56495a4856e6374d9d5f`
- Token contract: `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2`
- Destination: `0xd01607c3c5ecaba394d8be377a08590149325722`
- Raw amount: `16490986805666272665132`
- Transaction caller: `0x8d53903625b8e839b9df4bd28b0efb1cd6b8639a`
- Prior text-based classification: OTHER_OR_UNRESOLVED
- External context: f9ed91d41453d371493fae8d10 Second receiver 0x8d53903625b8e839b9df4bd28b0efb1cd6b8639a Wallet with the Aave loan, frozen by Tether at 21:02:47 0x65bd82f19985a569ef87b3926dd5f2247ba7bd06640141060f1b2d9ddedec3f6 Its 50M USDT deposit into Aave, 21:00:11 0xa85ad4807b33ad63ba2b2ffbac63d913285eefe44d7e5649
- Token contract/decimals: NOT VERIFIED
- Role: PENDING_INDEPENDENT_CLASSIFICATION
- Binance ownership: UNKNOWN
- Incident attribution: UNKNOWN

### 3. `0x544bd38c20a08db40deb6cf51be37b28d300af85`
- Transaction: `0x38546f9087ba0eb8444965711eb64a89fe9f53e80cd6d416317c847308219164`
- Token contract: `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2`
- Destination: `0x7a250d5630b4cf539739df2c5dacb4c659f2488d`
- Raw amount: `31560305220751795`
- Transaction caller: `0x5227f603c1ee34ce3c06efe6477003bdfccb2f8c`
- Prior text-based classification: OTHER_OR_UNRESOLVED
- External context: 642ab4593 ZAMA sale wallet, emptied into a stash on 31 Oct 0x11861b31b97c5c6550d49b03b1eed1a105774084 Wallet that sold the Base VIRTUAL and bridged the ETH 0x6b1bae59d09fccbddb6c6cceb07b7279367c4e3b The hacker's OP, moved to a new wallet on Optimism 0x38546f9087ba0eb8444965711eb64a89fe9f53e80cd6d416
- Token contract/decimals: NOT VERIFIED
- Role: PENDING_INDEPENDENT_CLASSIFICATION
- Binance ownership: UNKNOWN
- Incident attribution: UNKNOWN

### 4. `0x811f15855476156ebf86ba3b84fafb8ceaa4e84c`
- Transaction: `0xb6d7d3ffcbdd0465e1ab743a8d943218176cac7b15edefa7b7bcd5e853e4266f`
- Token contract: `0xdac17f958d2ee523a2206206994597c13d831ec7`
- Destination: `0xaa246bf639586a6ba46762d378ce50ca4fc654a0`
- Raw amount: `175000000000000`
- Transaction caller: `0x811f15855476156ebf86ba3b84fafb8ceaa4e84c`
- Prior text-based classification: OTHER_OR_UNRESOLVED
- External context:  175 million USDT UTC 10-29 20:59:11 | Block 26300942 | Index 117 | Status 0x1 0x1fb992f92a45afec23d7d5740c7958a644fb90ef0cba19ca39bd2c6534fb670b T07 target wallet received 175 million USDT UTC 10-29 21:08:23 | Block 26300988 | Index 58 | Status 0x1 0xb6d7d3ffcbdd0465e1ab743a8d943218176cac7b15edefa7
- Token contract/decimals: NOT VERIFIED
- Role: PENDING_INDEPENDENT_CLASSIFICATION
- Binance ownership: UNKNOWN
- Incident attribution: UNKNOWN

### 5. `0x8d53903625b8e839b9df4bd28b0efb1cd6b8639a`
- Transaction: `0x65bd82f19985a569ef87b3926dd5f2247ba7bd06640141060f1b2d9ddedec3f6`
- Token contract: `0xdac17f958d2ee523a2206206994597c13d831ec7`
- Destination: `0x23878914efe38d27c4d67ab83ed1b93a74d4086a`
- Raw amount: `50000000000000`
- Transaction caller: `0x8d53903625b8e839b9df4bd28b0efb1cd6b8639a`
- Prior text-based classification: OTHER_OR_UNRESOLVED
- External context: 0:35 0x5227f603c1ee34ce3c06efe6477003bdfccb2f8c Main receiver, holds the frozen stablecoins 0xa97bf7836f8a08f9ed91d41453d371493fae8d10 Second receiver 0x8d53903625b8e839b9df4bd28b0efb1cd6b8639a Wallet with the Aave loan, frozen by Tether at 21:02:47 0x65bd82f19985a569ef87b3926dd5f2247ba7bd0664014106
- Token contract/decimals: NOT VERIFIED
- Role: PENDING_INDEPENDENT_CLASSIFICATION
- Binance ownership: UNKNOWN
- Incident attribution: UNKNOWN

### 6. `0x8f10b468b06c6fd214b65f87778827f7d113f996`
- Transaction: `0x9a3dbf99edd0c063171d61130d82f1e6edd7cb409af5e7f2f95acd89e9584d8a`
- Token contract: `0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48`
- Destination: `0xd661623947ef2ead12d577b47021c167d163b0c5`
- Raw amount: `14866823298`
- Transaction caller: `0xa5a5491bca93dd4c076e4906e79e7673f4a5a142`
- Prior text-based classification: OTHER_OR_UNRESOLVED
- External context: FSiRzmJNSEBAFmrDbLkQ672iPN8H TRON contract the hacker passed 57M TRX through, 31 Oct TNhpfKq83wufEKGjBhQFnT7jnxYmyBzH6F Payout address that used it 55abdfbd684ad3f49323390964297098692ac189874a6ee6fe9b0b00de816070 A Relay deposit, 15:22 UTC on 31 Oct 0x9a3dbf99edd0c063171d61130d82f1e6edd7cb409af5e7f2
- Token contract/decimals: NOT VERIFIED
- Role: PENDING_INDEPENDENT_CLASSIFICATION
- Binance ownership: UNKNOWN
- Incident attribution: UNKNOWN

### 7. `0x9749292d74fd460982d0912ea9515ea24736c762`
- Transaction: `0x1fb992f92a45afec23d7d5740c7958a644fb90ef0cba19ca39bd2c6534fb670b`
- Token contract: `0xdac17f958d2ee523a2206206994597c13d831ec7`
- Destination: `0x811f15855476156ebf86ba3b84fafb8ceaa4e84c`
- Raw amount: `175000000000000`
- Transaction caller: `0x9749292d74fd460982d0912ea9515ea24736c762`
- Prior text-based classification: OTHER_OR_UNRESOLVED
- External context: C transfer via T05 Hot Wallet 34 UTC 10-29 20:41:23 | Block 26300855 | Index 26 | Status 0x1 0xdc102dd89dded5a83f1008906883ffb7c81ff3b7d7965d8c7277d170b5e17481 T06 transit 175 million USDT UTC 10-29 20:59:11 | Block 26300942 | Index 117 | Status 0x1 0x1fb992f92a45afec23d7d5740c7958a644fb90ef0cba19ca
- Token contract/decimals: NOT VERIFIED
- Role: PENDING_INDEPENDENT_CLASSIFICATION
- Binance ownership: UNKNOWN
- Incident attribution: UNKNOWN

### 8. `0xaa246bf639586a6ba46762d378ce50ca4fc654a0`
- Transaction: `0x11be88b460501b4652e760c41e08cc1f18575e14b6c6ffbb3383e043c2decf34`
- Token contract: `0xdac17f958d2ee523a2206206994597c13d831ec7`
- Destination: `0xe3478b0bb1a5084567c319096437924948be1964`
- Raw amount: `127672480`
- Transaction caller: `0xaa246bf639586a6ba46762d378ce50ca4fc654a0`
- Prior text-based classification: OTHER_OR_UNRESOLVED
- External context: ssful. T10 USDT Unlimited Quota Authorization UTC 10-29 21:12:59 | Block 26301011 | Index 86 | Status 0x1 0x3825815ffa7d04c818f11d6708da7c87f6dc218362a501f432b7f26a651739c6 T11 USDT payment UTC 10-29 21:12:59 | Block 26301011 | Index 87 | Status 0x1 0x11be88b460501b4652e760c41e08cc1f18575e14b6c6ffbb
- Token contract/decimals: NOT VERIFIED
- Role: PENDING_INDEPENDENT_CLASSIFICATION
- Binance ownership: UNKNOWN
- Incident attribution: UNKNOWN

### 9. `0xd661623947ef2ead12d577b47021c167d163b0c5`
- Transaction: `0x9a3dbf99edd0c063171d61130d82f1e6edd7cb409af5e7f2f95acd89e9584d8a`
- Token contract: `0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2`
- Destination: `0x8f10b468b06c6fd214b65f87778827f7d113f996`
- Raw amount: `6620026585864030887`
- Transaction caller: `0xa5a5491bca93dd4c076e4906e79e7673f4a5a142`
- Prior text-based classification: OTHER_OR_UNRESOLVED
- External context: FSiRzmJNSEBAFmrDbLkQ672iPN8H TRON contract the hacker passed 57M TRX through, 31 Oct TNhpfKq83wufEKGjBhQFnT7jnxYmyBzH6F Payout address that used it 55abdfbd684ad3f49323390964297098692ac189874a6ee6fe9b0b00de816070 A Relay deposit, 15:22 UTC on 31 Oct 0x9a3dbf99edd0c063171d61130d82f1e6edd7cb409af5e7f2
- Token contract/decimals: NOT VERIFIED
- Role: PENDING_INDEPENDENT_CLASSIFICATION
- Binance ownership: UNKNOWN
- Incident attribution: UNKNOWN

### 10. `0xf70da97812cb96acdf810712aa562db8dfa3dbef`
- Transaction: `0x9a3dbf99edd0c063171d61130d82f1e6edd7cb409af5e7f2f95acd89e9584d8a`
- Token contract: `0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48`
- Destination: `0x0729e2a4716d9f7dd17858d5d504426d228697f7`
- Raw amount: `14866823298`
- Transaction caller: `0xa5a5491bca93dd4c076e4906e79e7673f4a5a142`
- Prior text-based classification: OTHER_OR_UNRESOLVED
- External context: FSiRzmJNSEBAFmrDbLkQ672iPN8H TRON contract the hacker passed 57M TRX through, 31 Oct TNhpfKq83wufEKGjBhQFnT7jnxYmyBzH6F Payout address that used it 55abdfbd684ad3f49323390964297098692ac189874a6ee6fe9b0b00de816070 A Relay deposit, 15:22 UTC on 31 Oct 0x9a3dbf99edd0c063171d61130d82f1e6edd7cb409af5e7f2
- Token contract/decimals: NOT VERIFIED
- Role: PENDING_INDEPENDENT_CLASSIFICATION
- Binance ownership: UNKNOWN
- Incident attribution: UNKNOWN

## Decision
- Ten additional token-source addresses observed.
- No additional victim wallet confirmed.
- Do not equate token source with exchange ownership.
- Next: verify asset contracts and classify transaction purpose.
- Gate 2 remains OPEN.
