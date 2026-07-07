# Target Project Structure

The infrastructure lives in three top-level trees with distinct jobs:

- **`design/`** — human- and agent-authored inputs: the manifest, style docs, design sheets, and reference images. Everything here is source; it is edited deliberately and versioned.
- **`generated-assets/`** — machine outputs only. Nothing here is edited by hand; anything can in principle be regenerated from `design/` plus the generation state.
- **`image-generation/`** — run state. Queue, logs, completion and failure records. This is what makes batch runs resumable.

Keeping the trees separate means you can always answer: "what did we decide?" (`design/`), "what do we have?" (`generated-assets/`), and "where are we in the run?" (`image-generation/`).

## Full layout

```text
design/
|-- image-generation/
|   |-- README.md                    # what lives where, naming rules, who edits what
|   |-- style.md                     # global style guide (with provenance header)
|   |-- palette.md                   # color guidance with hex values
|   |-- negative-prompt-rules.md     # layered reusable exclusions
|   |-- prompt-templates.md          # composition order + per-asset-type templates
|   |-- qa-checklist.md              # deterministic checks + visual checks
|   |-- references/
|   |   |-- README.md                # folder purposes, naming, authority, obsolescence
|   |   |-- global/                  # style/mood boards that apply project-wide
|   |   |-- characters/
|   |   |-- objects/
|   |   |-- environments/
|   |   |-- ui/
|   |   `-- branding/
|   |-- characters/                  # one design sheet per character, e.g. skinny-skeleton.md
|   |-- objects/
|   |-- environments/
|   |-- ui/
|   `-- branding/
|-- assets.yaml                      # THE manifest: source of truth for planned assets
`-- assets.schema.json               # machine-validatable schema for assets.yaml

generated-assets/
|-- characters/                      # outputs, mirrored by category
|-- objects/
|-- environments/
|-- ui/
|-- branding/
|-- drafts/                          # variants awaiting selection
|-- rejected/                        # failed QA, kept for comparison (never auto-deleted)
`-- contact-sheets/                  # grid overviews for human review

image-generation/
|-- generation-queue.json            # assets queued for the next run
|-- asset-generation-log.md          # human-readable append-only run log
|-- completed-assets.json            # per-asset completion records
|-- failed-assets.json               # per-asset failure records with reasons
`-- retry-assets.yaml                # assets prepared for another attempt
```

## Conventions

### Reference images

- Named by subject and role: `skinny-skeleton-master-reference.png`, `skinny-skeleton-side-view-reference.png`, `graveyard-lighting-reference.png`, `main-menu-layout-reference.png`.
- Never `image1.png`, `test2.png`, `reference-final-final.png`.
- One image per subject is marked authoritative ("master") in the references README; others are supporting.
- Obsolete references are moved to an `archive/` subfolder within their category, never deleted automatically.
- The manifest lists the specific reference files each asset uses. Do not assume every reference applies to every asset.

### Design sheets

- One Markdown file per reusable subject, named in kebab-case after the subject: `characters/skinny-skeleton.md`.
- Sheets describe identity — what never changes. Poses, one-off compositions, and sizes belong in `assets.yaml`.

### Output paths

- Mirror the category: `generated-assets/<category>/<subject>/<asset_id>.png`.
- The filename stem equals the asset ID so deterministic QA can match files to manifest entries.
- Output paths are declared in the manifest and must stay inside the project's `output_root`. Path traversal (`..`) in an output path is a validation error.
- Multiple variants of one asset get `_v1`, `_v2` suffixes and land in `drafts/` until one is selected.

### State files

Minimal shapes (extend as needed, but keep these fields):

```json
// generation-queue.json
{ "built_at": "<iso8601>", "queue": [
  { "id": "skinny_skeleton_idle", "status": "queued", "attempts": 0, "priority": 1 }
] }

// completed-assets.json
{ "assets": [
  { "id": "skinny_skeleton_idle", "status": "approved", "attempts": 1,
    "completed_at": "<iso8601>", "outputs": ["generated-assets/characters/skinny-skeleton/skinny_skeleton_idle.png"],
    "selected_variant": 1, "review": "human-approved" }
] }

// failed-assets.json
{ "assets": [
  { "id": "necromancer_cast", "status": "qa_failed", "attempts": 2,
    "failed_at": "<iso8601>", "reason": "extra staff in frame; proportions drifted",
    "retry_decision": "retry_pending" }
] }
```

`retry-assets.yaml` mirrors manifest entries for assets being retried, plus a `retry_reason` and any prompt adjustments for the next attempt.

`asset-generation-log.md` is append-only, one dated entry per generation event, written for humans skimming what happened.

### Status lifecycle

```text
pending -> queued -> generating -> generated -> approved
                                |-> qa_failed -> retry_pending -> queued ...
                                |-> rejected
pending -> blocked   (unmet dependency or missing required reference)
```

Only `approved` is terminal-success. `generated` means "output exists, awaiting QA/review". Completion is never inferred from a file existing on disk — that is what `completed-assets.json` is for.
