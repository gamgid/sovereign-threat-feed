# Sovereign reviewed known-incident registry

This separate v2 channel requires an updated Sovereign client supporting
`sovereign-reviewed`. The legacy root feed remains unchanged for older clients.

Initial release: 13 primary-reviewed exact chain/address pairs on Ethereum,
Optimism, BNB Smart Chain, Polygon, Base and Arbitrum. This is a manually
maintained known-incident registry, not an exhaustive list of malicious addresses
or a verdict that an unlisted address is safe. Testnets are not covered.

Only `threat-feed.json` is a client update: an Ed25519-signed envelope verified
against the application's existing trust key. Other files are review evidence,
not alternative trust anchors. No private key is hosted here.

`registry.json` is the append-only review journal. Corrections are explicit
withdrawal events; rebuilding does not renew review timestamps. Source review:
2026-11-12 11:26:15 UTC; this package expires 2026-11-26 11:26:15 UTC.
Updates and signing are manual. Client downloads are opt-in.

Attribution: selected and normalized 0xCERT data, CC BY 4.0. See NOTICE.txt and
the journal's primary-source links and evidence hashes.
