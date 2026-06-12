#!/usr/bin/env python3
"""Validate Super SOP Node Radar registry files.

This script intentionally uses only the Python standard library so the registry
can be checked in lightweight agent environments.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROJECT_DIR = ROOT / "registry" / "projects"
NODE_MAP_DIR = ROOT / "registry" / "node-maps"

PROJECT_STATES = {
    "candidate",
    "metadata_triaged",
    "docs_reviewed",
    "code_reviewed",
    "tested",
    "benchmarked",
    "approved",
    "deprecated",
}


def load_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:  # pragma: no cover - CLI guard
        raise SystemExit(f"Invalid JSON: {path}: {exc}") from exc


def require(obj: dict, path: Path, keys: list[str]) -> None:
    missing = [key for key in keys if key not in obj]
    if missing:
        raise SystemExit(f"Missing keys in {path}: {', '.join(missing)}")


def validate_project(path: Path) -> str:
    obj = load_json(path)
    require(
        obj,
        path,
        [
            "schema_version",
            "id",
            "name",
            "repo",
            "review_state",
            "measured_at",
            "node_fit",
            "evidence",
            "risks",
            "next_review_tasks",
        ],
    )
    if obj["schema_version"] != "project-entry.v1":
        raise SystemExit(f"Bad schema_version in {path}: {obj['schema_version']}")
    if obj["review_state"] not in PROJECT_STATES:
        raise SystemExit(f"Bad review_state in {path}: {obj['review_state']}")
    if not obj["node_fit"]:
        raise SystemExit(f"Project has no node_fit: {path}")
    if not obj["evidence"]:
        raise SystemExit(f"Project has no evidence: {path}")
    require(obj["repo"], path, ["owner", "name", "url"])
    return obj["id"]


def validate_node_map(path: Path, project_ids: set[str]) -> None:
    obj = load_json(path)
    require(
        obj,
        path,
        [
            "schema_version",
            "id",
            "node",
            "capability_family",
            "purpose",
            "capability_types",
            "project_refs",
        ],
    )
    if obj["schema_version"] != "node-capability.v1":
        raise SystemExit(f"Bad schema_version in {path}: {obj['schema_version']}")
    capability_ids = {item["id"] for item in obj["capability_types"]}
    for ref in obj["project_refs"]:
        missing_project = ref["project_id"] not in project_ids
        missing_capability = ref["capability_type"] not in capability_ids
        if missing_project:
            raise SystemExit(f"Unknown project_id in {path}: {ref['project_id']}")
        if missing_capability:
            raise SystemExit(
                f"Unknown capability_type in {path}: {ref['capability_type']}"
            )
        if ref["review_state"] not in PROJECT_STATES:
            raise SystemExit(f"Bad review_state in {path}: {ref['review_state']}")


def main() -> int:
    project_paths = sorted(PROJECT_DIR.glob("*.json"))
    node_map_paths = sorted(NODE_MAP_DIR.glob("*.json"))
    if not project_paths:
        raise SystemExit("No project entries found.")
    if not node_map_paths:
        raise SystemExit("No node maps found.")

    project_ids = {validate_project(path) for path in project_paths}
    for path in node_map_paths:
        validate_node_map(path, project_ids)

    print(
        f"OK: {len(project_paths)} project entries, "
        f"{len(node_map_paths)} node maps."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
