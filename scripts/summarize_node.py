#!/usr/bin/env python3
"""Summarize one node capability map."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python3 scripts/summarize_node.py <node-map-id>")
        return 2

    node_map_id = sys.argv[1]
    node_map_path = ROOT / "registry" / "node-maps" / f"{node_map_id}.json"
    if not node_map_path.exists():
        print(f"Node map not found: {node_map_path}")
        return 1

    node_map = json.loads(node_map_path.read_text(encoding="utf-8"))
    projects = {}
    for path in sorted((ROOT / "registry" / "projects").glob("*.json")):
        obj = json.loads(path.read_text(encoding="utf-8"))
        projects[obj["id"]] = obj

    print(f"# {node_map['id']}")
    print()
    print(node_map["purpose"])
    print()
    print("| Capability | Project | State | Note |")
    print("|---|---|---|---|")
    for ref in node_map["project_refs"]:
        project = projects.get(ref["project_id"], {})
        name = project.get("name", ref["project_id"])
        print(
            f"| {ref['capability_type']} | {name} | "
            f"{ref['review_state']} | {ref.get('note', '')} |"
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
