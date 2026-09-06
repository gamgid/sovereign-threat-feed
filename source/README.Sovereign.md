# Scam Sniffer data attribution and modification notice

Source: https://github.com/scamsniffer/scam-database

Upstream copyright and license: see the unmodified `LICENSE` (GPL-3.0)
and `README.upstream.md` included here. This directory contains public threat
intelligence, not wallet/user data. No upstream executable code is used.

Snapshot: `blacklist/all.json`, revision
`1bc0b0354537dc7c3511f3d26ca03d2e7504b67e`, updated 2026-09-06 10:45:56 UTC.
The original file is included as `all.json`; SHA-256:
`1bad69f5c56f983a2e2c7243b31bb046ee77c922563f594813575a8799062552`.

Modifications made by the Sovereign project on 2026-09-06:

- Extract only the `address` array (4,607 input entries).
- Keep only exact `0x` + 40 hexadecimal character EVM addresses.
- Convert to lowercase, deduplicate, and sort (4,598 unique entries).
- Exclude 9 non-EVM/malformed entries, retained in `excluded-records.json`.
- Wrap the normalized data with source provenance and an explicit EVM reputation
  scope in `normalized-payload.json`.
- Sign a package of that payload using the Sovereign publisher key.

This signature is **by Sovereign, not Scam Sniffer**. It authenticates the
packaging/publisher, not the truth of every upstream label. The original source,
modification notice, license and normalization/publishing scripts are retained
in this project. This source directory is also included in the application bundle.

Upstream describes a seven-day delay for the public feed. A recent commit does
not remove that delay. An EVM reputation match does not prove malicious activity
on Sepolia; absence of a match does not establish safety. No domain filtering,
contract analysis or transaction simulation is provided by this dataset.
