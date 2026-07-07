# Negative Prompt Rules

Reusable exclusions, layered from global to project-specific. Asset-specific
poses and one-off exclusions belong in the asset's `qa.must_not_have` in
`assets.yaml`, not here. If the same exclusion keeps appearing on assets,
promote it to this file.

## Global exclusions

- no watermark
- no signature
- no unexpected border or frame
- no unreadable or garbled text
- TODO

## Anatomy and character exclusions

- no extra limbs, fingers, or heads
- no character redesign (features must match the design sheet)
- TODO

## Composition exclusions

- no cropped subject unless the asset explicitly requests it
- no duplicate subjects unless declared
- TODO

## Text and typography exclusions

- no baked-in text unless the asset declares exact `text_content`
- no pseudo-lettering or gibberish glyphs
- TODO

## Technical output exclusions

- no opaque background when transparency is declared
- no visible checkerboard "transparency" pattern
- no compression artifacts or noise
- TODO

## Genre-specific exclusions

- TODO (e.g. no realistic horror for a cute cartoon project,
  no modern objects in a medieval setting)

## Project-specific exclusions

- TODO
