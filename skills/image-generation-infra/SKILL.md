---
name: image-generation-infra
description: Prepare or update the reusable infrastructure for AI image generation in an app, game, website, or creative project. Use this skill whenever the user wants to create asset manifests, visual style guides, reference-image structures, prompt templates, image QA rules, output folders, retry logs, or batch-generation workflows — including requests like "prepare image generation for this project", "create assets.yaml", "organise my image references and prompts", or "make this project ready for bulk image generation". This skill sets up and audits the generation pipeline; it does not generate the final images itself.
---

# Image Generation Infra

Use this skill to prepare the complete infrastructure for consistent, repeatable, and resumable AI image generation in a software, mobile app, game, website, or creative project.

This skill does not primarily generate images. It creates and maintains the asset manifest, style documentation, subject design sheets, reference structures, prompt templates, QA rules, and generation state files that a separate image-generation skill consumes. Keeping setup separate from execution is what makes both reusable: one skill that does setup, generation, QA, and retry at once becomes overly complex and impossible to resume safely.

The infrastructure must support both interactive generation inside an agent session and automated batch workflows, and it must be resumable: it must always be safe to stop a run and continue later without regenerating approved assets.

## Core Principles

- **Consistency comes from reference images, not prose.** This is the most important principle, and the easiest to get wrong. The single strongest lever for keeping a character or object looking the same across generations is feeding the generator a *locked master reference image* — via image-to-image, an IP-Adapter or reference-conditioning input, or a fine-tune/LoRA trained on the subject. The text stack (style guide, design sheet, composed prompt) is essential supporting context, but text alone cannot hold identity stable; diffusion models drift no matter how precise the words. So for every recurring subject, establish and lock one canonical master reference *early*, and make every asset of that subject condition on it. Treat the design sheet as the description *of* that reference, not a substitute for it.
- **Style is discovered, never assumed.** If the project has a codebase, existing assets, or design docs, derive the style guide from that evidence and cite it. If it has none, interview the user until the style and vibe are explicitly confirmed. Never invent a style silently — a style guide that contradicts the product poisons every asset generated from it.
- **Identity lives in design sheets; poses live in the manifest.** A design sheet describes what never changes about the subject and points at its master reference. The manifest entry describes this asset's pose, size, and output. Never duplicate full subject descriptions into `style.md`.
- **The manifest is the source of truth.** Every planned asset lives in the manifest (`assets.yaml`) with a stable ID, its subject's references, an output path, and QA notes. Nothing is "done" because a file exists on disk.
- **Prompts are composed, not stored.** The composed prompt is assembled in a deterministic order from the design files — it supplies framing, pose, and technical requirements around the reference image. Hand-writing every final prompt from memory invites drift.
- **QA splits deterministic from visual.** Scripts check files, formats, dimensions, and paths. Model or human judgement checks identity, style, and composition. Auto-retry obvious failures; never claim subjective visual consistency is guaranteed.
- **Right-size the ceremony.** Most projects have a handful of recurring subjects, not thousands of assets. Default to the Lite tier below; only stand up the full manifest schema, state files, and validation scripts when asset volume actually justifies them. Building a batch pipeline for a dozen assets is its own failure mode.

## Choose the tier first

Before anything else, decide how much infrastructure the project actually warrants. The tiers share the same shape — reference images carry identity, a style guide sets the look, a manifest lists the work — they differ only in ceremony.

**Lite (default).** For a solo project or anything up to roughly 20–30 recurring subjects generated in occasional bursts. The generation loop here is tight and visual — generate, look, nudge, regenerate — so keep friction low:

- `design/image-generation/style.md` (palette folded in unless it is large)
- `design/image-generation/references/` with a **locked master reference per recurring subject** — this is where the real consistency lives
- a design sheet per recurring subject (skip for one-off assets)
- a flat `design/assets.yaml` — a simple list of assets, no schema ceremony, no state files
- `sample-prompts.md` and the generation command

Run the workflow below but **skip steps 9 (state files) and 10 (validation scripts)**, keep step 8 a flat list, and drop the standalone `negative-prompt-rules.md`/`qa-checklist.md` and the schema. Everything else — inspect, style, structure, references, design sheets, prompt templates, the image-gen skill, sample prompts, the command — still applies.

**Full (opt-in, for scale).** Escalate when the project has many assets (sprite sheets, large icon sets, localized variants), an ongoing cadence, or multiple people needing an auditable pipeline. Adds to Lite:

- `negative-prompt-rules.md` and `qa-checklist.md` as standalone files
- the full `assets.yaml` schema + `assets.schema.json`
- state files (queue, completed, failed, retry, log) for resumable batch runs
- the validation/queue/diff scripts

All 13 steps. Start Lite and migrate up with the **Extend** mode when volume grows — never the reverse.

Whichever tier, the reference-image work and the style guide are non-negotiable; the manifest/state machinery is what scales.

Note: even for a project that never runs a batch, the design sheets, style guide, and locked references have standalone value as a design bible — a handoff artifact and a single source of visual truth.

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
|   |   prompt-templates.md, qa-checklist.md, sample-prompts.md
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

### 5. Establish and lock the master references

This is the load-bearing step for consistency (see the first core principle), not a folder-creation chore. For every recurring subject, the project needs one **locked master reference image** that every future asset of that subject will condition on.

Create the category folders under `design/image-generation/references/` with a README covering what belongs where, which image is authoritative, and how obsolete references are archived (never deleted). Filenames must be meaningful (`skinny-skeleton-master-reference.png`, `graveyard-lighting-reference.png`) — never `image1.png` or `reference-final-final.png`.

Then, for each recurring subject, secure its master reference:

- If an authoritative image already exists (existing sprite, approved concept art), designate it the master and record it.
- If none exists, the *first* generation job for that subject is to produce and lock its master reference — a clean, canonical, front-or-three-quarter view. Every subsequent asset of that subject references it (image-to-image / reference-conditioning) rather than re-rolling identity from text. Flag this ordering in the manifest via `depends_on` so pose assets wait for their master.
- Record which model input the reference feeds (image-to-image, IP-Adapter, style/character reference, or training a LoRA) so the execution skill knows how to use it, not just that it exists.

The manifest points at specific reference files per asset; never assume every reference applies to every asset.

### 6. Create subject design sheets

One Markdown sheet per reusable visual subject (`characters/skinny-skeleton.md`, `objects/bone-sword.md`, `environments/graveyard-lane.md`, `ui/unit-card.md`). Capture, where applicable: canonical description, silhouette, proportions, facial features, clothing, equipment, colors, materials, orientation, scale, permitted expressions and poses, invariants that must never change, associated references, subject-specific negative rules. Use `assets/templates/character-sheet.template.md` as the starting point.

### 7. Create prompt templates

`prompt-templates.md` defines the deterministic composition order — project and intended use, global style, subject identity, asset-specific action, camera and orientation, consistency constraints, technical output requirements, negative rules, reference-image instructions — plus per-asset-type templates (single sprite, sprite sheet, object, background, UI icon, marketing image, app-store graphic, portrait/card art). Read `references/prompt-composition.md` for worked examples.

### 8. Create the asset manifest

Create `design/assets.yaml` from `assets/templates/assets.template.yaml`. Every asset needs a stable ID, its subject's reference paths, an asset-specific description, orientation, dimensions, background rule, output path, and QA notes.

**Lite tier:** keep it a flat list — ID, references, description, output path, must-have/must-not-have. Skip status lifecycle, schema, and per-asset ceremony you will not use. A short manifest a human can read at a glance is the point.

**Full tier:** add category, type, status, variants, max attempts, and dependencies; read `references/asset-manifest-schema.md` for field-by-field documentation and the status lifecycle; copy `assets/schemas/assets.schema.json` into the project as `design/assets.schema.json`.

### 9. Create generation state files *(Full tier)*

Skip for Lite. For resumable batch runs, create `generation-queue.json`, `completed-assets.json`, `failed-assets.json`, `retry-assets.yaml`, and `asset-generation-log.md`. Track at least: asset ID, status, attempt count, timestamp, output paths, failure reason, retry decision, review status, selected variant.

### 10. Validate *(Full tier)*

Skip for Lite (a flat manifest is eyeballed, not validated). For Full-tier setups, run `scripts/validate_manifest.py <project-root>` before declaring setup complete. It checks unique IDs, unique and contained output paths, required fields, valid statuses, and that every referenced file exists or is explicitly marked missing. `scripts/find_missing_assets.py` diffs the manifest against disk without trusting filenames as completion; `scripts/build_generation_queue.py` builds the queue from manifest statuses. Produce a concise validation report.

### 11. Prepare the image-generation skill

Check whether a suitable image-generation skill is already installed. If yes: identify its invocation name, document how this infrastructure calls it, and do not duplicate it. If no: create or install one via the harness's skill-creation mechanism, keep generation behavior separate from this skill, and document required API keys, dependencies, models, and permissions. Never place secrets in the repository.

### 12. Compose sample prompts

The hand-off to the execution skill is the weakest joint in the pipeline: "compose the prompt from the templates" is one line of instruction, but the executor still has to map manifest fields into the target model's actual syntax. De-risk it before any generation runs.

Pick one to three representative manifest entries (ideally covering different asset types) and compose their full prompts by hand, walking the complete composition order against the real style guide, design sheets, and negative rules. Save them to `design/image-generation/sample-prompts.md`, labelled with their asset IDs. This buys two things: the user can eyeball the composed output and fix the design files before burning generation credits, and the execution skill gets few-shot examples of a correctly composed prompt so it only has to add model-specific syntax on top. Regenerate the samples whenever the style guide or templates change materially.

### 13. Produce the final generation command

Output a ready-to-run instruction for the target harness, using paths that actually exist in the project:

```text
Use the image-generation skill.

Read design/assets.yaml and process every asset whose status is
pending or retry_pending.

Before generating each asset:

1. Read the global files referenced under project.
2. Read the asset's subject sheet.
3. Load the master reference image(s) listed by that asset and feed them to
   the model as conditioning input (image-to-image / reference / IP-Adapter) —
   this is what holds identity stable, not the prompt text alone.
4. Compose the prompt using design/image-generation/prompt-templates.md,
   following the worked examples in design/image-generation/sample-prompts.md.
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

Setup is complete only when (Full tier — for Lite, items 3, 7, and the validation half of 6 are optional):

1. the folder structure exists;
2. the style guide exists and the style was either derived from evidence or confirmed by the user;
3. every recurring subject has a locked master reference recorded (or its master-reference job is queued as the first asset);
4. the manifest lists each asset with its references and output path;
5. asset output paths are defined and reference naming rules are documented;
6. QA notes exist (Full tier: `assets.yaml` also passes validation);
7. progress and retry state files exist (Full tier only);
8. the actual image-generation skill is identified or created, and how references feed it is documented;
9. sample composed prompts exist for representative assets;
10. a ready-to-run generation instruction is produced;
11. unresolved requirements are clearly listed.

## Expected Output

At the end of a run, report: the tier chosen (Lite/Full) and why, the mode executed, how the style was established (evidence-derived with citations, or user-confirmed via interview), the master-reference status per recurring subject (locked, or first-job-queued), what was created or changed, the validation result (Full tier), the identified image-generation skill and how references feed it, a pointer to the sample composed prompts, the ready-to-run generation command, and an explicit list of unresolved `TODO`s.
