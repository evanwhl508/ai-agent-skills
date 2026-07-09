# Asset Manifest Schema (`design/assets.yaml`)

The manifest is the source of truth for planned image assets. Generation tools read it; state files record progress against it; QA validates outputs against it. If an asset is not in the manifest, it does not exist as far as the pipeline is concerned.

A machine-validatable JSON Schema ships alongside this skill at `assets/schemas/assets.schema.json`; copy it into the project as `design/assets.schema.json` and run `scripts/validate_manifest.py` against the manifest.

**This document describes the Full-tier manifest.** For a Lite-tier project (a handful of recurring subjects, occasional bursts), most of these fields are ceremony you will not use. A Lite manifest is a flat, human-readable list — enough to know what to generate, from which reference, to where:

```yaml
project:
  name: My Game
  style: design/image-generation/style.md
assets:
  - id: skinny_skeleton_idle
    references: [design/image-generation/references/characters/skinny-skeleton-master-reference.png]
    description: Idle pose, sword resting on shoulder, side view facing right.
    output: generated-assets/characters/skinny_skeleton_idle.png
    must_not_have: [opaque background, extra weapons]
```

Skip the schema, statuses, and state files until asset volume actually justifies them, then escalate to the Full structure below via the **Extend** mode. Do not start here for a dozen assets.

## Top level

```yaml
version: 1

project:
  name: Example Project
  output_root: generated-assets
  global_style: design/image-generation/style.md
  palette: design/image-generation/palette.md
  negative_rules: design/image-generation/negative-prompt-rules.md
  prompt_templates: design/image-generation/prompt-templates.md
  qa_checklist: design/image-generation/qa-checklist.md

defaults:
  format: png
  quality: high
  background: transparent
  overwrite: false
  max_attempts: 2

assets: []
```

- `version` — manifest schema version. Currently `1`.
- `project.*` — paths to the global design files. Generation reads these before every asset. All paths in the manifest are project-root-relative.
- `defaults.*` — inherited by every asset unless the asset overrides the field. `overwrite: false` is the safety default: approved outputs are never replaced silently.

## Asset entries

```yaml
assets:
  - id: skinny_skeleton_idle          # required, stable, unique, snake_case
    category: characters              # required: characters|objects|environments|ui|branding|...
    type: single_sprite               # required: single_sprite|sprite_sheet|object|background|
                                      #           ui_icon|marketing|app_store|portrait|...
    status: pending                   # required, see lifecycle below

    subject:
      sheet: design/image-generation/characters/skinny-skeleton.md   # required for subjects
      references:                     # specific files, not "everything in the folder"
        - design/image-generation/references/characters/skinny-skeleton-master-reference.png

    generation:
      description: Idle pose with a subtle ribcage bob and sword resting on shoulder.
      orientation: side view facing right
      size: 1024x1024                 # or aspect_ratio: "16:9"
      background: transparent         # overrides defaults when present
      variants: 1

    output:
      path: generated-assets/characters/skinny-skeleton/skinny_skeleton_idle.png

    qa:
      must_have:
        - feet aligned to the expected baseline
        - complete character visible
        - same proportions as the canonical reference
      must_not_have:
        - additional weapons
        - cropped feet
        - opaque background

    max_attempts: 2                   # optional override of defaults
    depends_on: []                    # optional: asset IDs that must be approved first
```

### Required fields per asset

`id`, `category`, `type`, `status`, `generation.description`, `output.path`. For assets with a reusable subject, `subject.sheet` is required; pure one-offs (e.g. an abstract background) may omit `subject`.

### Optional fields

| Field | Meaning |
|---|---|
| `generation.frames`, `generation.frame_layout` | Sprite-sheet frame count and grid, e.g. `8` and `4x2` |
| `generation.baseline`, `generation.safe_area` | Alignment line and area that must stay uncropped |
| `generation.text_content`, `generation.locale` | Exact text to render and its localisation |
| `generation.seed` | Seed, where the model supports it |
| `platform` | e.g. `ios`, `android`, `web` — for store/marketing assets |
| `priority` | Lower number = generated earlier |
| `batch_group` | Free-form label for generating related assets together |
| `parent` | Asset ID this one derives from (e.g. recolor of a base sprite) |
| `retry_reason` | Why the last attempt failed; consumed on the next attempt |

### Rules the validator enforces

- Asset IDs unique across the manifest.
- Output paths unique, inside `project.output_root`, no `..` traversal.
- Filename stem of `output.path` matches the asset `id` (keeps deterministic QA trivial).
- Every `subject.sheet` and every path under `project.*` exists on disk.
- Every listed reference image exists, or the asset carries `references_missing: true` to mark the gap explicitly.
- `status` is one of the lifecycle values below.
- `depends_on` names existing asset IDs, acyclic.

## Status lifecycle

```text
pending        planned, not yet queued
queued         selected for the next generation run
generating     attempt in progress
generated      output exists, awaiting QA / review
qa_failed      failed deterministic or visual QA
retry_pending  cleared for another attempt (respecting max_attempts)
approved       accepted; never regenerated without explicit instruction
rejected       given up on; kept for the record
blocked        cannot proceed (unmet dependency, missing required reference)
```

Only the generation workflow moves assets between statuses, and it updates the manifest and the state files together after each asset — never one without the other.
