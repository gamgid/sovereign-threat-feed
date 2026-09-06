#!/usr/bin/env python3
"""Read-only upstream acquisition. Creates a NEW review directory, never publishes.

Usage: python3 Scripts/prepare-threat-feed.py COMMIT NEW_OUTPUT_DIRECTORY
Then review provenance, exclusions and the address diff before local signing.
Only Python standard library; no npm, package installation or executable download.
"""
import datetime
import hashlib
import json
from pathlib import Path
import re
import sys
import urllib.request

REPOSITORY = "scamsniffer/scam-database"
DATA_PATH = "blacklist/all.json"


def fetch(url, limit):
    request = urllib.request.Request(url, headers={"User-Agent": "Sovereign-threat-feed-review"})
    with urllib.request.urlopen(request, timeout=25) as response:
        if response.url != url:
            raise ValueError("Unexpected upstream redirect")
        data = response.read(limit + 1)
    if len(data) > limit:
        raise ValueError("Upstream size limit exceeded")
    return data


def main():
    if len(sys.argv) != 3 or not re.fullmatch(r"[0-9a-f]{40}", sys.argv[1]):
        raise ValueError("Supply a pinned commit and a new output directory")
    requested = sys.argv[1]
    out = Path(sys.argv[2])
    if out.exists():
        raise ValueError("Output already exists; use a new review directory")
    api = f"https://api.github.com/repos/{REPOSITORY}/commits?path={DATA_PATH}&sha={requested}&per_page=1"
    commit = json.loads(fetch(api, 256_000))[0]
    revision = commit["sha"]
    if not re.fullmatch(r"[0-9a-f]{40}", revision):
        raise ValueError("Invalid source revision")
    updated = datetime.datetime.fromisoformat(commit["commit"]["committer"]["date"].replace("Z", "+00:00"))
    now = datetime.datetime.now(datetime.timezone.utc)
    if not datetime.timedelta(0) <= now - updated < datetime.timedelta(days=14):
        raise ValueError("Source is stale or from the future; do not relabel it as fresh")
    base = f"https://raw.githubusercontent.com/{REPOSITORY}/{revision}/"
    raw = fetch(base + DATA_PATH, 16_000_000)
    source = json.loads(raw)
    values = source["address"]
    if not isinstance(values, list) or len(values) > 100_000:
        raise ValueError("Unexpected source structure")
    valid = [x.lower() for x in values if isinstance(x, str) and re.fullmatch(r"0x[0-9a-fA-F]{40}", x)]
    addresses = sorted(set(valid))
    if not 1 <= len(addresses) <= 25_000:
        raise ValueError("Unexpected address count")
    excluded = [x for x in values if not isinstance(x, str) or not re.fullmatch(r"0x[0-9a-fA-F]{40}", x)]
    digest = hashlib.sha256(raw).hexdigest()
    payload = {"channel": "sovereign.evm-address-reputation.v1", "schema": 1,
               "scope": "evm-address-reputation", "issuedAt": int(now.timestamp() * 1000),
               "sourceUpdatedAt": int(updated.timestamp() * 1000), "sourceCommit": revision,
               "sourceSHA256": digest, "addresses": addresses}
    provenance = {"repository": f"https://github.com/{REPOSITORY}", "requestedCommit": requested,
                  "commit": revision, "sourceUpdatedAt": updated.isoformat(), "sourceSHA256": digest,
                  "license": "GPL-3.0", "upstreamDelayDays": 7, "inputAddresses": len(values),
                  "validUniqueEVMAddresses": len(addresses), "excludedNonEVMOrMalformed": len(excluded),
                  "duplicates": len(valid) - len(addresses)}
    license_data = fetch(base + "LICENSE", 100_000)
    readme = fetch(base + "README.md", 100_000)
    out.mkdir(parents=True, exist_ok=False)
    (out / "all.json").write_bytes(raw)
    (out / "LICENSE").write_bytes(license_data)
    (out / "README.upstream.md").write_bytes(readme)
    (out / "PROVENANCE.json").write_text(json.dumps(provenance, indent=2) + "\n")
    (out / "excluded-records.json").write_text(json.dumps(excluded, indent=2) + "\n")
    (out / "normalized-payload.json").write_text(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print(json.dumps(provenance))


if __name__ == "__main__":
    main()
