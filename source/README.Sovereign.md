# Scam Sniffer data attribution and modification notice

Source: https://github.com/scamsniffer/scam-database

Upstream copyright and license: see the unmodified `LICENSE` (GPL-3.0)
and `README.upstream.md` included here. This directory contains public threat
intelligence, not wallet/user data. No upstream executable code is used.

Snapshot and exact transformation counts: see PROVENANCE.json and excluded-records.json.
Transformation: extract address; retain 0x + 40 hex; lowercase, deduplicate, sort.
Source date is NOT package issuance date. Public feed delay: seven days.
Signature is by Sovereign, not Scam Sniffer; absence does not establish safety.
