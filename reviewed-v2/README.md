# Sovereign reviewed known-incident registry

This v2 channel requires a Sovereign client supporting `sovereign-reviewed`.
The legacy root feed is unchanged. Client downloads are opt-in.

15 exact chain/address pairs on 8 networks: Ethereum, Optimism, BNB Smart Chain,
Polygon, Base, Arbitrum, Base Sepolia and Ethereum Sepolia. All 13 previous
records are retained. The two testnet entries identify malware command infrastructure
reported by SafeDep, not a claim that a transfer directly steals funds.
This manual list is not exhaustive; an unlisted address is not thereby safe.

Only `threat-feed.json` is a client update, signed by the existing Ed25519 identity.
Evidence and review documents are not trust anchors or independent approval.
No private key is hosted here. The scope-review binds the previous and current
journal hashes and the exact added chains. Corrections require explicit events.

Review: 2026-11-20 14:39:19 UTC. Expiry: 2026-12-04 14:39:19 UTC.
Rebuilding or signing does not renew freshness. Signing and updates are manual.
Selected 0xCERT facts retain CC BY 4.0 attribution; additional factual source:
https://safedep.io/blog/mathmain-encrypted-loader . See NOTICE.txt.
