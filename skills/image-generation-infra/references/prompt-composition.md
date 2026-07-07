# Prompt Composition

Final generation prompts are assembled, not hand-written. Every prompt for every asset is composed from the same sources in the same order, so consistency comes from the structure rather than from an author remembering to repeat themselves.

## The composition order

Assemble every prompt in this order:

1. **Project and intended use** — what product this is for and what the image is (game sprite, app icon, store screenshot). Sets the generator's frame before any detail.
2. **Global style** — the relevant rules from `style.md` (genre, rendering, line style, lighting, proportions) and palette guidance from `palette.md`.
3. **Subject identity** — the invariants from the subject's design sheet: canonical description, silhouette, colors, materials, the things that must never change.
4. **Asset-specific action or composition** — this asset's `generation.description` from the manifest: the pose, the moment, the arrangement.
5. **Camera and orientation** — `generation.orientation`, perspective, framing.
6. **Consistency constraints** — "same character as the reference", "identical proportions to the master reference", frame-to-frame coherence for sheets.
7. **Technical output requirements** — size or aspect ratio, background/transparency, format, variant count, baseline and safe area when declared.
8. **Relevant negative rules** — the applicable layers from `negative-prompt-rules.md` plus the asset's `qa.must_not_have` items, phrased as exclusions.
9. **Reference-image instructions** — which attached references are authoritative and what to take from each (identity from the master reference, lighting from the lighting reference).

Earlier layers are stable across the whole project; later layers narrow to this one asset. When a generator has separate fields (prompt vs negative prompt vs reference attachments), map layers 1–7 to the prompt, layer 8 to the negative prompt, layer 9 to the attachments — same content, same order, different slots.

## Worked example

Given the manifest entry `skinny_skeleton_idle` (see `asset-manifest-schema.md`), a composed prompt looks like:

```text
[1] Game sprite for "Graveyard Lane", a cute-spooky tower-defense mobile game.
[2] Cute cartoon style, flat shading, thick dark outlines (3px, near-black),
    minimal texture, soft top-left lighting. Palette: bone white #F5F0E6,
    moss green #6BCB77, night blue #2B2D42; avoid saturated reds.
[3] Skinny Skeleton: small lanky skeleton, oversized round skull, one loose
    tooth, chipped left eye socket, holds a short bone sword. Proportions
    2.5 heads tall. These features are canonical and must not change.
[4] Idle pose with a subtle ribcage bob and the sword resting on the shoulder.
[5] Side view facing right, full body in frame, orthographic game-sprite camera.
[6] Must read as the exact same character as the master reference; identical
    proportions and features.
[7] 1024x1024 PNG, fully transparent background, feet on the horizontal
    baseline at 90% height, whole character inside the safe area. 1 variant.
[8] Exclude: extra limbs, extra weapons, redesigned features, cropped feet,
    opaque or patterned background, embedded text, watermark, realistic horror.
[9] Reference "skinny-skeleton-master-reference.png" is authoritative for
    identity and proportions; do not copy its pose.
```

The bracketed numbers are for this document only — omit them in real prompts.

## Per-asset-type template skeletons

`prompt-templates.md` in the target project holds the filled-in versions of these. Each keeps the nine-layer order and varies what layers 4–7 emphasize:

- **Single character sprite** — pose readability, full body, baseline, transparency.
- **Sprite sheet** — frame count and layout grid, identical identity across frames, consistent baseline and spacing per cell, no frame numbering baked into the image.
- **Object / prop** — material and scale cues, orientation, transparency, no hands or characters holding it unless declared.
- **Background / environment** — camera and horizon, where gameplay/UI space must stay uncluttered, no characters unless declared, opaque full-bleed output.
- **UI icon** — reads at small size, strong silhouette, declared corner radius/padding conventions, exact canvas size.
- **Marketing image** — composition for the declared aspect ratio, focal subject, space reserved for copy (but text itself usually composited later, not generated).
- **App-store graphic** — platform dimension requirements, safe areas, device-frame conventions if used.
- **Portrait / card artwork** — tighter camera, expression from the permitted list in the design sheet, card-frame safe area.

## Rules

- Never paste a full design sheet into a prompt; extract the invariants (layer 3) and let the reference image carry the rest.
- Never restate style rules ad hoc; quote them from `style.md` so a style edit propagates to every future prompt.
- Keep asset-specific wording in the manifest's `generation.description`, not in `prompt-templates.md`, so templates stay reusable.
- When a prompt needs something no layer provides, that is a signal a design file is missing information — fix the file, then compose.
