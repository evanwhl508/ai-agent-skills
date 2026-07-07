# Prompt Templates

Every generation prompt is composed in this fixed order (see the skill's
`references/prompt-composition.md` for a worked example):

1. Project and intended use
2. Global style (from `style.md` + `palette.md`)
3. Subject identity (invariants from the subject's design sheet)
4. Asset-specific action or composition (from `assets.yaml` `generation.description`)
5. Camera and orientation
6. Consistency constraints
7. Technical output requirements
8. Relevant negative rules (from `negative-prompt-rules.md` + asset `must_not_have`)
9. Reference-image instructions

Fill in the bracketed slots below per project. Keep asset-specific wording in
the manifest, not here.

## Single character sprite

```text
[1] {asset type} for "{project name}", {one-line product description}.
[2] {style summary from style.md}. Palette: {relevant palette entries}.
[3] {subject invariants from the design sheet}. These features are canonical
    and must not change.
[4] {generation.description}
[5] {generation.orientation}; full body in frame; {camera convention}.
[6] Must read as the exact same subject as the master reference; identical
    proportions and features.
[7] {size} {format}, {background rule}{, baseline/safe-area rules}.
    {variants} variant(s).
[8] Exclude: {applicable negative rules + asset must_not_have}.
[9] Reference "{master reference filename}" is authoritative for identity
    and proportions; do not copy its pose.
```

## Sprite sheet

As single sprite, plus in [7]: "{frames} frames in a {frame_layout} grid,
uniform cell size, consistent baseline and spacing per cell" and in [8]:
"no frame numbers or grid lines baked into the image".

## Object / prop

As single sprite, with [3] from the object's sheet (materials, scale cues)
and [8] including "no hands or characters holding the object" unless declared.

## Background / environment

[4] describes the scene; [5] camera and horizon; [7] opaque full-bleed at
{size}; note where gameplay/UI space must stay uncluttered; [8] includes
"no characters" unless declared.

## UI icon

[4] the concept; [7] exact canvas {size}, {padding/corner-radius convention},
must read clearly at {smallest display size}; [8] includes "no fine detail
that disappears at small sizes".

## Marketing image

[4] focal subject and composition for {aspect_ratio}; [7] reserve
{copy space area} for overlaid text (text composited later, not generated)
unless `text_content` is declared.

## App-store graphic

[7] platform dimensions {per store requirements}, safe areas
{per store requirements}; device-frame convention: TODO.

## Portrait / card artwork

[5] tighter camera ({framing}); [4] expression from the permitted list in
the design sheet; [7] card-frame safe area: TODO.
