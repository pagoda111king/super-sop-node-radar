#!/usr/bin/env python3
"""Validate fixed reference inspector configuration."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "inspectors" / "reference-projects.json"
CONTRACTS = ROOT / "inspectors" / "understanding-contracts.json"


def require_keys(obj: dict, keys: tuple[str, ...], label: str) -> None:
    for key in keys:
        if key not in obj:
            raise SystemExit(f"Missing {key} in {label}")


def main() -> int:
    data = json.loads(CONFIG.read_text(encoding="utf-8"))
    if data.get("schema_version") != "reference-inspectors.v1":
        raise SystemExit("Bad schema_version in inspectors/reference-projects.json")
    contracts = json.loads(CONTRACTS.read_text(encoding="utf-8"))
    if contracts.get("schema_version") != "inspector-understanding-contracts.v1":
        raise SystemExit("Bad schema_version in inspectors/understanding-contracts.json")

    inspectors = data.get("inspectors", [])
    if not inspectors:
        raise SystemExit("No inspectors configured")
    contract_items = contracts.get("contracts", [])
    if not contract_items:
        raise SystemExit("No understanding contracts configured")

    ids = set()
    github_count = 0
    for inspector in inspectors:
        require_keys(
            inspector,
            ("id", "name", "priority", "sources", "watch_for", "node_relevance"),
            f"inspector {inspector}",
        )
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

    contract_ids = set()
    for contract in contract_items:
        require_keys(
            contract,
            (
                "inspector_id",
                "logic_focus",
                "must_read_surfaces",
                "tracking_surfaces",
                "architecture_questions",
                "sediment_targets",
            ),
            f"understanding contract {contract}",
        )
        contract_id = contract["inspector_id"]
        if contract_id in contract_ids:
            raise SystemExit(f"Duplicate understanding contract: {contract_id}")
        contract_ids.add(contract_id)
        for list_key in (
            "must_read_surfaces",
            "tracking_surfaces",
            "architecture_questions",
            "sediment_targets",
        ):
            if not contract[list_key]:
                raise SystemExit(f"Empty {list_key} in contract {contract_id}")

    missing_contracts = ids - contract_ids
    extra_contracts = contract_ids - ids
    if missing_contracts:
        raise SystemExit(f"Missing contracts for inspectors: {sorted(missing_contracts)}")
    if extra_contracts:
        raise SystemExit(f"Contracts without inspectors: {sorted(extra_contracts)}")

    print(
        f"OK: {len(inspectors)} inspectors, {github_count} GitHub sources, "
        f"{len(contract_items)} understanding contracts."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
