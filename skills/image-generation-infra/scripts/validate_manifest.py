#!/usr/bin/env python3
"""Validate design/assets.yaml before generation.

Checks: unique asset IDs, required fields, valid statuses, output paths unique
and contained in output_root, filename stems matching asset IDs, referenced
files existing (design sheets, reference images, global project files), and
acyclic depends_on references.

Exit code 0 with warnings allowed; non-zero when any error is found.

Usage:
    python validate_manifest.py <project-root> [--manifest design/assets.yaml]

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

STATUSES = {"pending", "queued", "generating", "generated", "qa_failed",
            "retry_pending", "approved", "rejected", "blocked"}
REQUIRED_PROJECT_FIELDS = ["name", "output_root", "global_style", "palette",
                           "negative_rules", "prompt_templates", "qa_checklist"]


def contained(root: Path, candidate: Path) -> bool:
    try:
        candidate.resolve().relative_to(root.resolve())
        return True
    except ValueError:
        return False


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project_root", type=Path)
    parser.add_argument("--manifest", default="design/assets.yaml")
    args = parser.parse_args()

    root = args.project_root.resolve()
    manifest_path = root / args.manifest
    errors, warnings = [], []

    if not manifest_path.is_file():
        print(f"error: manifest not found: {manifest_path}", file=sys.stderr)
        return 1

    with open(manifest_path, encoding="utf-8") as handle:
        manifest = yaml.safe_load(handle)

    if not isinstance(manifest, dict):
        print("error: manifest is not a mapping", file=sys.stderr)
        return 1

    if manifest.get("version") != 1:
        errors.append(f"version must be 1, got {manifest.get('version')!r}")

    project = manifest.get("project") or {}
    for field in REQUIRED_PROJECT_FIELDS:
        if not project.get(field):
            errors.append(f"project.{field} is missing")
    for field in REQUIRED_PROJECT_FIELDS[2:]:
        rel = project.get(field)
        if rel and not (root / rel).is_file():
            errors.append(f"project.{field} does not exist: {rel}")

    output_root = root / str(project.get("output_root", "generated-assets"))

    assets = manifest.get("assets") or []
    seen_ids, seen_outputs = {}, {}
    ids = set()

    for index, asset in enumerate(assets):
        label = asset.get("id") or f"assets[{index}]"
        asset_id = asset.get("id")

        if not asset_id:
            errors.append(f"{label}: missing id")
        elif asset_id in seen_ids:
            errors.append(f"duplicate asset id: {asset_id}")
        else:
            seen_ids[asset_id] = index
            ids.add(asset_id)

        for field in ("category", "type"):
            if not asset.get(field):
                errors.append(f"{label}: missing {field}")

        status = asset.get("status")
        if status not in STATUSES:
            errors.append(f"{label}: invalid status {status!r}")

        generation = asset.get("generation") or {}
        if not generation.get("description"):
            errors.append(f"{label}: missing generation.description")
        frames = generation.get("frames")
        layout = generation.get("frame_layout")
        if layout:
            try:
                cols, rows = (int(part) for part in str(layout).split("x"))
                if frames and frames > cols * rows:
                    errors.append(f"{label}: {frames} frames do not fit frame_layout {layout}")
            except ValueError:
                errors.append(f"{label}: unparsable frame_layout {layout!r}")

        out = (asset.get("output") or {}).get("path")
        if not out:
            errors.append(f"{label}: missing output.path")
        else:
            if out in seen_outputs:
                errors.append(f"{label}: output path also used by {seen_outputs[out]}: {out}")
            seen_outputs[out] = label
            if not contained(output_root, root / out):
                errors.append(f"{label}: output path escapes output_root: {out}")
            if asset_id and Path(out).stem.split("_v")[0] != asset_id:
                warnings.append(f"{label}: output filename stem does not match asset id: {out}")

        subject = asset.get("subject") or {}
        sheet = subject.get("sheet")
        if sheet and not (root / sheet).is_file():
            errors.append(f"{label}: design sheet does not exist: {sheet}")
        for reference in subject.get("references") or []:
            if not (root / reference).is_file():
                if asset.get("references_missing"):
                    warnings.append(f"{label}: reference marked missing: {reference}")
                else:
                    errors.append(f"{label}: reference image does not exist "
                                  f"(add references_missing: true to acknowledge): {reference}")

    for asset in assets:
        for dependency in asset.get("depends_on") or []:
            if dependency not in ids:
                errors.append(f"{asset.get('id')}: depends_on unknown asset: {dependency}")

    # dependency cycle check
    graph = {a.get("id"): list(a.get("depends_on") or []) for a in assets if a.get("id")}
    state = {}

    def has_cycle(node: str) -> bool:
        if state.get(node) == "done":
            return False
        if state.get(node) == "visiting":
            return True
        state[node] = "visiting"
        cyclic = any(has_cycle(dep) for dep in graph.get(node, []) if dep in graph)
        state[node] = "done"
        return cyclic

    for node in graph:
        if has_cycle(node):
            errors.append(f"dependency cycle involving: {node}")
            break

    print(f"validated {len(assets)} asset(s): {len(errors)} error(s), {len(warnings)} warning(s)")
    for message in errors:
        print(f"  ERROR: {message}")
    for message in warnings:
        print(f"  warn:  {message}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
