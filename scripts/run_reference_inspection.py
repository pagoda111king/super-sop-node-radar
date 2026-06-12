#!/usr/bin/env python3
"""Generate reference project inspector reports.

The script creates a metadata-first inspection snapshot. It does not claim deep
approval; human or agent review should add code/docs/forum interpretation.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import date
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "inspectors" / "reference-projects.json"


def run(cmd: list[str]) -> tuple[int, str]:
    proc = subprocess.run(cmd, capture_output=True, text=True, check=False)
    output = proc.stdout.strip() if proc.stdout.strip() else proc.stderr.strip()
    return proc.returncode, output


def gh_repo_view(repo: str) -> dict[str, Any]:
    fields = ",".join(
        [
            "nameWithOwner",
            "description",
            "url",
            "stargazerCount",
            "forkCount",
            "latestRelease",
            "pushedAt",
            "licenseInfo",
            "repositoryTopics",
            "isArchived",
        ]
    )
    code, output = run(["gh", "repo", "view", repo, "--json", fields])
    if code != 0:
        return {"repo": repo, "error": output}
    try:
        return json.loads(output)
    except json.JSONDecodeError:
        return {"repo": repo, "error": output}


def format_release(meta: dict[str, Any]) -> str:
    release = meta.get("latestRelease")
    if not release:
        return "-"
    tag = release.get("tagName") or release.get("name") or "-"
    published = release.get("publishedAt") or "-"
    url = release.get("url") or ""
    if url:
        return f"[{tag}]({url}) · {published}"
    return f"{tag} · {published}"


def write_project_report(
    run_dir: Path,
    inspector: dict[str, Any],
    github_meta: list[tuple[dict[str, Any], dict[str, Any]]],
    today: str,
) -> Path:
    path = run_dir / f"{inspector['id']}.md"
    lines = [
        f"# Project Inspector Report · {today}",
        "",
        f"## Inspector",
        "",
        f"- id: `{inspector['id']}`",
        f"- name: {inspector['name']}",
        f"- priority: `{inspector['priority']}`",
        "",
        "## Sources Checked",
        "",
        "| Type | Source | URL | Automated Status |",
        "|---|---|---|---|",
    ]

    for source in inspector["sources"]:
        status = "manual_review_needed"
        if source["type"] == "github":
            status = "github_metadata_checked"
        lines.append(
            f"| {source['type']} | {source['name']} | {source['url']} | {status} |"
        )

    lines.extend(
        [
            "",
            "## GitHub Metadata Snapshot",
            "",
            "| Repo | Stars | Forks | Pushed At | Latest Release | License | Archived |",
            "|---|---:|---:|---|---|---|---|",
        ]
    )

    for source, meta in github_meta:
        if "error" in meta:
            lines.append(
                f"| `{source['repo']}` | - | - | - | - | - | error: {meta['error']} |"
            )
            continue
        license_name = (meta.get("licenseInfo") or {}).get("name") or "-"
        lines.append(
            "| "
            f"[`{meta.get('nameWithOwner', source['repo'])}`]({meta.get('url', source['url'])}) "
            f"| {meta.get('stargazerCount', '-')} "
            f"| {meta.get('forkCount', '-')} "
            f"| {meta.get('pushedAt', '-')} "
            f"| {format_release(meta)} "
            f"| {license_name} "
            f"| {meta.get('isArchived', '-')} |"
        )

    lines.extend(
        [
            "",
            "## Watch Questions",
            "",
        ]
    )
    for item in inspector["watch_for"]:
        lines.append(f"- {item}")

    lines.extend(
        [
            "",
            "## Node / Rail Relevance",
            "",
        ]
    )
    for item in inspector["node_relevance"]:
        lines.append(f"- `{item}`")

    lines.extend(
        [
            "",
            "## Inspector Interpretation",
            "",
            "Automated metadata snapshot complete. Deep code, docs, forum, issue, and release-note review should be added by the scheduled inspector run before recommending node changes.",
            "",
            "## Recommendation",
            "",
            "Decision: `watch`",
            "",
            "Reason: metadata checked; no deep impact judgment recorded yet.",
            "",
            "Next test: inspect recent releases/docs/issues and map any substantial change to node/rail impact.",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")
    return path


def write_chief_report(
    report_dir: Path,
    inspectors: list[dict[str, Any]],
    project_reports: list[Path],
    today: str,
) -> Path:
    path = report_dir / f"{today}-reference-inspection.md"
    lines = [
        f"# Chief Inspector Proposal · {today}",
        "",
        "## Executive Decision",
        "",
        "Decision: `watch`",
        "",
        "Confidence: `low_to_medium`",
        "",
        "This automated pass created a metadata-first snapshot for the fixed reference project inspectors. It should be followed by targeted deep review before any node or rail optimization is accepted.",
        "",
        "## Inspectors Covered",
        "",
        "| Inspector | Priority | Related Nodes / Rails | Report |",
        "|---|---|---|---|",
    ]

    by_name = {path.stem: path for path in project_reports}
    for inspector in inspectors:
        report = by_name.get(inspector["id"])
        rel = report.relative_to(ROOT) if report else ""
        nodes = ", ".join(f"`{item}`" for item in inspector["node_relevance"])
        lines.append(
            f"| {inspector['name']} | `{inspector['priority']}` | {nodes} | `{rel}` |"
        )

    lines.extend(
        [
            "",
            "## Proposed Changes",
            "",
            "### Accept Now",
            "",
            "- None. This pass should not directly change the 6-layer / 14-node taxonomy.",
            "",
            "### Watch",
            "",
            "- Watch all P0 inspectors for architecture-level shifts in tools, handoffs, evaluation, tracing, durable execution, and skill/plugin packaging.",
            "",
            "### Reject / Ignore",
            "",
            "- Ignore popularity-only movement unless it is tied to released, documented, or testable behavior.",
            "",
            "## User Decision Needed",
            "",
            "Choose whether the next deep review should focus on P0 runtime architecture, evaluation/trace systems, or enterprise interoperability.",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")
    return path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", default=date.today().isoformat())
    args = parser.parse_args()

    config = json.loads(CONFIG.read_text(encoding="utf-8"))
    run_dir = ROOT / "inspectors" / "runs" / args.date
    chief_dir = ROOT / "chief-inspector" / "reports"
    run_dir.mkdir(parents=True, exist_ok=True)
    chief_dir.mkdir(parents=True, exist_ok=True)

    reports = []
    for inspector in config["inspectors"]:
        github_meta = []
        for source in inspector["sources"]:
            if source["type"] == "github":
                github_meta.append((source, gh_repo_view(source["repo"])))
        reports.append(write_project_report(run_dir, inspector, github_meta, args.date))

    chief = write_chief_report(chief_dir, config["inspectors"], reports, args.date)
    print(f"OK: wrote {len(reports)} inspector reports and {chief.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
