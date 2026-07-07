#!/usr/bin/env python3
"""Diff the manifest against disk and generation state — without ever treating
a file's existence as completion.

Reports:
  - assets recorded complete (approved/generated) whose output file is missing;
  - assets still pending/queued whose output path is already occupied
    (overwrite risk);
  - files under output_root that no manifest entry claims (orphans).

Usage:
    python find_missing_assets.py <project-root> [--manifest design/assets.yaml]

Requires PyYAML (pip install pyyaml).
"""

import argparse
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("error: PyYAML is required — pip install pyyaml", file=sys.stderr)
    sys.exit(2)

DONE_STATUSES = {"generated", "approved"}
NOT_STARTED_STATUSES = {"pending", "queued", "blocked"}
IGNORED_DIRS = {"drafts", "rejected", "contact-sheets"}
IGNORED_NAMES = {".gitkeep", ".DS_Store"}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project_root", type=Path)
    parser.add_argument("--manifest", default="design/assets.yaml")
    args = parser.parse_args()

    root = args.project_root.resolve()
    manifest_path = root / args.manifest
    if not manifest_path.is_file():
        print(f"error: manifest not found: {manifest_path}", file=sys.stderr)
        return 1

    with open(manifest_path, encoding="utf-8") as handle:
        manifest = yaml.safe_load(handle) or {}

    assets = manifest.get("assets") or []
    output_root = root / str((manifest.get("project") or {}).get("output_root", "generated-assets"))

    missing, overwrite_risk = [], []
    claimed = set()

    for asset in assets:
        asset_id = asset.get("id", "?")
        status = asset.get("status")
        out = (asset.get("output") or {}).get("path")
        if not out:
            continue
        out_path = root / out
        claimed.add(out_path.resolve())
        if status in DONE_STATUSES and not out_path.is_file():
            missing.append((asset_id, status, out))
        if status in NOT_STARTED_STATUSES and out_path.is_file():
            overwrite_risk.append((asset_id, status, out))

    orphans = []
    if output_root.is_dir():
        for path in sorted(output_root.rglob("*")):
            if not path.is_file() or path.name in IGNORED_NAMES:
                continue
            relative_parts = path.relative_to(output_root).parts
            if relative_parts and relative_parts[0] in IGNORED_DIRS:
                continue
            if path.resolve() not in claimed:
                orphans.append(path.relative_to(root))

    print(f"checked {len(assets)} asset(s) against {output_root.relative_to(root)}/")
    if missing:
        print(f"\n{len(missing)} asset(s) recorded complete but file MISSING:")
        for asset_id, status, out in missing:
            print(f"  {asset_id} [{status}] -> {out}")
    if overwrite_risk:
        print(f"\n{len(overwrite_risk)} not-started asset(s) whose output path is already occupied (overwrite risk):")
        for asset_id, status, out in overwrite_risk:
            print(f"  {asset_id} [{status}] -> {out}")
    if orphans:
        print(f"\n{len(orphans)} file(s) on disk not claimed by any manifest entry:")
        for path in orphans:
            print(f"  {path}")
    if not (missing or overwrite_risk or orphans):
        print("no discrepancies found")
    return 1 if missing else 0


if __name__ == "__main__":
    sys.exit(main())
