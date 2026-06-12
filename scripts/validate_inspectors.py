#!/usr/bin/env python3
"""Validate fixed reference inspector configuration."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "inspectors" / "reference-projects.json"


def main() -> int:
    data = json.loads(CONFIG.read_text(encoding="utf-8"))
    if data.get("schema_version") != "reference-inspectors.v1":
        raise SystemExit("Bad schema_version in inspectors/reference-projects.json")

    inspectors = data.get("inspectors", [])
    if not inspectors:
        raise SystemExit("No inspectors configured")

    ids = set()
    github_count = 0
    for inspector in inspectors:
        for key in ("id", "name", "priority", "sources", "watch_for", "node_relevance"):
            if key not in inspector:
                raise SystemExit(f"Missing {key} in inspector {inspector}")
        if inspector["id"] in ids:
            raise SystemExit(f"Duplicate inspector id: {inspector['id']}")
        ids.add(inspector["id"])
        if not inspector["sources"]:
            raise SystemExit(f"Inspector has no sources: {inspector['id']}")
        for source in inspector["sources"]:
            if "type" not in source or "name" not in source or "url" not in source:
                raise SystemExit(f"Bad source in inspector {inspector['id']}: {source}")
            if source["type"] == "github":
                github_count += 1
                if "repo" not in source:
                    raise SystemExit(
                        f"GitHub source missing repo in inspector {inspector['id']}"
                    )

    print(f"OK: {len(inspectors)} inspectors, {github_count} GitHub sources.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
