#!/usr/bin/env python3
"""Build image-generation/generation-queue.json from manifest statuses.

Queues every asset whose status is pending or retry_pending, skipping assets
whose depends_on are not yet approved (reported as blocked). Orders by
priority (ascending, missing priority last), then batch_group, then manifest
order. Approved, rejected, and generated assets are never queued.

Usage:
    python build_generation_queue.py <project-root> [--manifest design/assets.yaml]
        [--queue image-generation/generation-queue.json] [--dry-run]

Requires PyYAML (pip install pyyaml).
"""

import argparse
import datetime
import json
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("error: PyYAML is required — pip install pyyaml", file=sys.stderr)
    sys.exit(2)

QUEUEABLE = {"pending", "retry_pending"}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project_root", type=Path)
    parser.add_argument("--manifest", default="design/assets.yaml")
    parser.add_argument("--queue", default="image-generation/generation-queue.json")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    root = args.project_root.resolve()
    manifest_path = root / args.manifest
    if not manifest_path.is_file():
        print(f"error: manifest not found: {manifest_path}", file=sys.stderr)
        return 1

    with open(manifest_path, encoding="utf-8") as handle:
        manifest = yaml.safe_load(handle) or {}

    assets = manifest.get("assets") or []
    approved = {a.get("id") for a in assets if a.get("status") == "approved"}

    queue, blocked = [], []
    for index, asset in enumerate(assets):
        if asset.get("status") not in QUEUEABLE:
            continue
        unmet = [dep for dep in asset.get("depends_on") or [] if dep not in approved]
        if unmet:
            blocked.append((asset.get("id"), unmet))
            continue
        queue.append({
            "id": asset.get("id"),
            "status": "queued",
            "attempts": 0,
            "retry": asset.get("status") == "retry_pending",
            "retry_reason": asset.get("retry_reason"),
            "priority": asset.get("priority"),
            "batch_group": asset.get("batch_group"),
            "_order": (asset.get("priority") if asset.get("priority") is not None else 10**9,
                       asset.get("batch_group") or "", index),
        })

    queue.sort(key=lambda entry: entry.pop("_order"))
    for entry in queue:
        if entry["retry_reason"] is None:
            del entry["retry_reason"]

    payload = {
        "built_at": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
        "queue": queue,
    }

    print(f"{len(queue)} asset(s) queued, {len(blocked)} blocked on dependencies, "
          f"{sum(1 for a in assets if a.get('status') == 'approved')} approved (untouched)")
    for asset_id, unmet in blocked:
        print(f"  blocked: {asset_id} waiting on {', '.join(unmet)}")

    if args.dry_run:
        print(json.dumps(payload, indent=2))
        return 0

    queue_path = root / args.queue
    queue_path.parent.mkdir(parents=True, exist_ok=True)
    queue_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {queue_path.relative_to(root)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
