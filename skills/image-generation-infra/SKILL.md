---
name: image-generation-infra
description: Prepare or update the reusable infrastructure for AI image generation in an app, game, website, or creative project. Use this skill whenever the user wants to create asset manifests, visual style guides, reference-image structures, prompt templates, image QA rules, output folders, retry logs, or batch-generation workflows — including requests like "prepare image generation for this project", "create assets.yaml", "organise my image references and prompts", or "make this project ready for bulk image generation". This skill sets up and audits the generation pipeline; it does not generate the final images itself.
---

# Image Generation Infra

Use this skill to prepare the complete infrastructure for consistent, repeatable, and resumable AI image generation in a software, mobile app, game, website, or creative project.

This skill does not primarily generate images. It creates and maintains the asset manifest, style documentation, subject design sheets, reference structures, prompt templates, QA rules, and generation state files that a separate image-generation skill consumes. Keeping setup separate from execution is what makes both reusable: one skill that does setup, generation, QA, and retry at once becomes overly complex and impossible to resume safely.

The infrastructure must support both interactive generation inside an agent session and automated batch workflows, and it must be resumable: it must always be safe to stop a run and continue later without regenerating approved assets.

## Core Principles

- **Style is discovered, never assumed.** If the project has a codebase, existing assets, or design docs, derive the style guide from that evidence and cite it. If it has none, interview the user until the style and vibe are explicitly confirmed. Never invent a style silently — a style guide that contradicts the product poisons every asset generated from it.
- **`assets.yaml` is the source of truth.** Every planned asset lives in the manifest with a stable ID, status, design-sheet path, references, output path, and QA rules. Nothing is "done" because a file exists on disk.
- **Identity lives in design sheets; poses live in the manifest.** A character sheet describes what never changes about the subject. The manifest entry describes this asset's pose, size, and output. Never duplicate full subject descriptions into `style.md`.
- **Prompts are composed, not stored.** Final prompts are assembled from manifest fields in a deterministic order defined by `prompt-templates.md`. Hand-writing every final prompt defeats consistency and reuse.
- **QA splits deterministic from visual.** Scripts check files, formats, dimensions, and paths. Model or human judgement checks identity, style, and composition. Auto-retry obvious failures; never claim subjective visual consistency is guaranteed.
- **State files make runs resumable.** Queue, completed, failed, and retry files track every asset's lifecycle. Never infer completion from an output filename existing.

## Operating Modes

Decide the mode before touching files:

- **Initialise** — create the infrastructure for a project that has none.
- **Extend** — add new asset categories, subjects, references, or manifest entries to an existing setup.
- **Audit** — inspect existing infrastructure and report inconsistencies, missing files, and manifest violations without changing anything.
- **Migrate** — convert unstructured prompts and loose reference files into the standard structure. Back up or diff existing manifests first; delete nothing.
- **Queue** — build or update the list of assets ready for generation.
- **Retry** — prepare failed assets for another attempt without touching approved files.

## Workflow

### 1. Inspect the project

Before creating any files:

1. Inspect the repository and understand the product.
2. Identify existing visual assets, theme files, and design documentation.
3. Search for existing image-generation infrastructure; reuse and extend it rather than overwrite. Preserve human edits to style and design files.
4. Reuse existing naming conventions where sensible.
5. Identify likely asset categories for this project type: characters, animation states, enemies, objects, props, backgrounds, environments, UI, icons, app-store graphics, marketing, branding, screenshots, tutorial illustrations.
6. Ask for clarification only when a missing detail would make the infrastructure unusable; otherwise create sensible placeholders marked `TODO`.

### 2. Discover the style

This step is mandatory and gates everything downstream. Read `references/style-discovery.md` for the full playbook.

**Project has usable visual signal** (existing sprites, icons, mockups, CSS/theme files, brand colors, screenshots, store listings, design docs): analyze those sources and draft `style.md` and `palette.md` from the evidence — extract hex values from theme files, infer genre and rendering style from existing art, read tone from copy. Present the derived summary to the user for confirmation, citing what each conclusion was based on, and mark low-confidence inferences as `TODO`.

**Project has no usable visual signal** (empty repo, idea-stage project): do not invent a style. Interview the user — visual genre, mood, shape language, rendering style, lighting, proportions, level of detail, palette direction, prohibited characteristics — until the style and vibe are explicitly confirmed. Offer concrete options with short descriptions rather than open-ended questions where possible. Only write `style.md` and `palette.md` after confirmation.

### 3. Create the project structure

Scaffold the standard layout (full annotated version in `references/project-structure.md`):

```text
design/
|-- image-generation/
|   |-- README.md, style.md, palette.md, negative-prompt-rules.md,
|   |   prompt-templates.md, qa-checklist.md
|   |-- references/{global,characters,objects,environments,ui,branding}/
|   `-- characters/ objects/ environments/ ui/ branding/   (design sheets)
|-- assets.yaml
`-- assets.schema.json

generated-assets/{characters,objects,environments,ui,branding,drafts,rejected,contact-sheets}/

image-generation/
|-- generation-queue.json, asset-generation-log.md,
|-- completed-assets.json, failed-assets.json, retry-assets.yaml
```

`scripts/initialise_image_infra.py` scaffolds this idempotently — it never overwrites existing files. Fill-in templates for every global file live in `assets/templates/`.

### 4. Create the global design files

- **`style.md`** — visual genre, mood, shape language, line style, rendering style, lighting, texture, perspective, camera angle, composition, character proportions, level of detail, background treatment, transparency rules, consistency requirements, acceptable stylistic variation, prohibited visual characteristics. Permanent style rules only.
- **`palette.md`** — primary, secondary, accent, background, and semantic UI colors; character-specific colors where relevant; hex values when available; rules for highlights, shadows, outlines, and contrast; colors that must not be introduced. The palette is guidance, not merely a list of colors.
- **`negative-prompt-rules.md`** — layered exclusions: global, anatomy and character, composition, text and typography, technical output, genre-specific, project-specific. Reusable rules only; asset-specific poses do not belong here.
- **`qa-checklist.md`** — deterministic checks separated from visual checks. Read `references/qa-guidelines.md` for the split and its rationale.

### 5. Create reference infrastructure

Create the category folders under `design/image-generation/references/` and a README that explains what belongs in each folder, which images are authoritative, and how obsolete references are handled. Filenames must be meaningful (`skinny-skeleton-master-reference.png`, `graveyard-lighting-reference.png`) — never `image1.png` or `reference-final-final.png`. The manifest points at specific reference files; never assume every reference applies to every asset.

### 6. Create subject design sheets

One Markdown sheet per reusable visual subject (`characters/skinny-skeleton.md`, `objects/bone-sword.md`, `environments/graveyard-lane.md`, `ui/unit-card.md`). Capture, where applicable: canonical description, silhouette, proportions, facial features, clothing, equipment, colors, materials, orientation, scale, permitted expressions and poses, invariants that must never change, associated references, subject-specific negative rules. Use `assets/templates/character-sheet.template.md` as the starting point.

### 7. Create prompt templates

`prompt-templates.md` defines the deterministic composition order — project and intended use, global style, subject identity, asset-specific action, camera and orientation, consistency constraints, technical output requirements, negative rules, reference-image instructions — plus per-asset-type templates (single sprite, sprite sheet, object, background, UI icon, marketing image, app-store graphic, portrait/card art). Read `references/prompt-composition.md` for worked examples.

### 8. Create the asset manifest

Create `design/assets.yaml` from `assets/templates/assets.template.yaml`. Every asset needs a stable ID, category, type, status, design-sheet path, reference paths, description, orientation, dimensions, background rule, output path, variants, QA requirements, and max attempts. Read `references/asset-manifest-schema.md` for field-by-field documentation and the status lifecycle. Copy `assets/schemas/assets.schema.json` into the project as `design/assets.schema.json`.

### 9. Create generation state files

`generation-queue.json`, `completed-assets.json`, `failed-assets.json`, `retry-assets.yaml`, and `asset-generation-log.md`. Track at least: asset ID, status, attempt count, timestamp, output paths, failure reason, retry decision, review status, selected variant.

### 10. Validate

Run `scripts/validate_manifest.py <project-root>` before declaring setup complete. It checks unique IDs, unique and contained output paths, required fields, valid statuses, and that every referenced file exists or is explicitly marked missing. `scripts/find_missing_assets.py` diffs the manifest against disk without trusting filenames as completion; `scripts/build_generation_queue.py` builds the queue from manifest statuses. Produce a concise validation report.

### 11. Prepare the image-generation skill

Check whether a suitable image-generation skill is already installed. If yes: identify its invocation name, document how this infrastructure calls it, and do not duplicate it. If no: create or install one via the harness's skill-creation mechanism, keep generation behavior separate from this skill, and document required API keys, dependencies, models, and permissions. Never place secrets in the repository.

### 12. Produce the final generation command

Output a ready-to-run instruction for the target harness, using paths that actually exist in the project:

```text
Use the image-generation skill.

Read design/assets.yaml and process every asset whose status is
pending or retry_pending.

Before generating each asset:

1. Read the global files referenced under project.
2. Read the asset's subject sheet.
3. Read only the reference images listed by that asset.
4. Compose the prompt using design/image-generation/prompt-templates.md.
5. Generate the declared number of variants.
6. Save outputs exactly to the declared output path.
7. Run deterministic QA checks.
8. Evaluate the visual QA requirements.
9. Retry failed assets up to max_attempts.
10. Update the manifest status and all generation state files after each asset.

Do not overwrite approved assets.
Do not silently skip failures.
Resume from existing generation state.
Stop only when every processable asset is approved, rejected, or blocked.
```

## Safety and File Handling

- Never delete original references automatically.
- Never overwrite approved generated assets unless explicitly instructed.
- Never store API keys or secrets in Markdown, YAML, logs, or scripts.
- Preserve human edits to style and subject design files.
- Back up or diff existing manifests before major migrations.
- Clearly mark inferred project details as `TODO` when uncertain.
- Do not claim that image identity or visual consistency can be perfectly guaranteed.
- Keep the infrastructure independent of a particular image model where possible.

## Completion Criteria

Setup is complete only when:

1. the folder structure exists;
2. the global design files exist and the style was either derived from evidence or confirmed by the user;
3. `assets.yaml` passes validation;
4. asset output paths are defined;
5. reference folders and naming rules are documented;
6. QA rules exist;
7. progress and retry files exist;
8. the actual image-generation skill is identified or created;
9. a ready-to-run generation instruction is produced;
10. unresolved requirements are clearly listed.

## Expected Output

At the end of a run, report: the mode executed, how the style was established (evidence-derived with citations, or user-confirmed via interview), what was created or changed, the validation result, the identified image-generation skill, the ready-to-run generation command, and an explicit list of unresolved `TODO`s.
