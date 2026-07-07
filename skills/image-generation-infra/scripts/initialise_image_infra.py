#!/usr/bin/env python3
"""Scaffold the image-generation infrastructure in a target project.

Idempotent: creates missing directories and state files, never overwrites
anything that already exists. Optionally copies the fill-in templates for the
global design files with --copy-templates (still never overwriting).

Usage:
    python initialise_image_infra.py <project-root> [--copy-templates]
"""

import argparse
import json
import shutil
import sys
from pathlib import Path

CATEGORIES = ["characters", "objects", "environments", "ui", "branding"]

DESIGN_DIRS = (
    ["design/image-generation/references/global"]
    + [f"design/image-generation/references/{c}" for c in CATEGORIES]
    + [f"design/image-generation/{c}" for c in CATEGORIES]
)

OUTPUT_DIRS = [f"generated-assets/{d}" for d in CATEGORIES + ["drafts", "rejected", "contact-sheets"]]

STATE_FILES = {
    "image-generation/generation-queue.json": json.dumps({"built_at": None, "queue": []}, indent=2) + "\n",
    "image-generation/completed-assets.json": json.dumps({"assets": []}, indent=2) + "\n",
    "image-generation/failed-assets.json": json.dumps({"assets": []}, indent=2) + "\n",
    "image-generation/retry-assets.yaml": "# Assets prepared for another generation attempt.\nassets: []\n",
    "image-generation/asset-generation-log.md": "# Asset Generation Log\n\nAppend-only. One dated entry per generation event.\n",
}

TEMPLATE_TARGETS = {
    "style.template.md": "design/image-generation/style.md",
    "palette.template.md": "design/image-generation/palette.md",
    "negative-prompt-rules.template.md": "design/image-generation/negative-prompt-rules.md",
    "prompt-templates.template.md": "design/image-generation/prompt-templates.md",
    "qa-checklist.template.md": "design/image-generation/qa-checklist.md",
    "assets.template.yaml": "design/assets.yaml",
}

REFERENCES_README = """# Reference Images

One folder per category. Filenames are meaningful: `<subject>-<role>-reference.<ext>`
(e.g. `skinny-skeleton-master-reference.png`). Never `image1.png` or
`reference-final-final.png`.

- `global/` — style and mood boards that apply project-wide.
- `characters/`, `objects/`, `environments/`, `ui/`, `branding/` — per-subject references.

Exactly one image per subject is the authoritative "master" reference; note it
on the subject's design sheet. Move obsolete references to an `archive/`
subfolder inside their category — never delete them.

The manifest (`design/assets.yaml`) lists the specific reference files each
asset uses. Do not assume every reference applies to every asset.
"""

IG_README = """# Image Generation Design Files

- `style.md`, `palette.md`, `negative-prompt-rules.md`, `prompt-templates.md`,
  `qa-checklist.md` — global design files. Human edits here are authoritative;
  generation tooling must not rewrite them.
- `references/` — reference images by category (see its README).
- `characters/`, `objects/`, `environments/`, `ui/`, `branding/` — one design
  sheet per reusable subject; sheets describe identity, the manifest describes
  individual assets.
- `../assets.yaml` — the asset manifest: the source of truth for planned assets.
"""


def create_file(path: Path, content: str, created: list, skipped: list) -> None:
    if path.exists():
        skipped.append(path)
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    created.append(path)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project_root", type=Path)
    parser.add_argument("--copy-templates", action="store_true",
                        help="copy fill-in templates for the global design files (never overwrites)")
    args = parser.parse_args()

    root = args.project_root.resolve()
    if not root.is_dir():
        print(f"error: project root does not exist: {root}", file=sys.stderr)
        return 1

    created, skipped = [], []

    for rel in DESIGN_DIRS + OUTPUT_DIRS:
        directory = root / rel
        if not directory.exists():
            directory.mkdir(parents=True)
            created.append(directory)
        gitkeep = directory / ".gitkeep"
        if not any(p.name != ".gitkeep" for p in directory.iterdir()) and not gitkeep.exists():
            gitkeep.touch()

    for rel, content in STATE_FILES.items():
        create_file(root / rel, content, created, skipped)

    create_file(root / "design/image-generation/README.md", IG_README, created, skipped)
    create_file(root / "design/image-generation/references/README.md", REFERENCES_README, created, skipped)

    if args.copy_templates:
        templates_dir = Path(__file__).resolve().parent.parent / "assets" / "templates"
        for template_name, target_rel in TEMPLATE_TARGETS.items():
            source = templates_dir / template_name
            target = root / target_rel
            if target.exists():
                skipped.append(target)
                continue
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source, target)
            created.append(target)
        schema_source = Path(__file__).resolve().parent.parent / "assets" / "schemas" / "assets.schema.json"
        schema_target = root / "design/assets.schema.json"
        if schema_target.exists():
            skipped.append(schema_target)
        else:
            shutil.copyfile(schema_source, schema_target)
            created.append(schema_target)

    print(f"created {len(created)} path(s), left {len(skipped)} existing path(s) untouched")
    for path in created:
        print(f"  + {path.relative_to(root)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
