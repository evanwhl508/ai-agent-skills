# Image QA Checklist

Two categories with different executors. Deterministic checks are automatable
and run on every output; visual checks need model or human judgement and their
verdicts are recorded per asset. See the skill's `references/qa-guidelines.md`
for the rationale and retry policy.

## Deterministic checks (run scripts)

- [ ] Output file exists at the declared `output.path`
- [ ] Filename stem matches the asset ID
- [ ] Format matches the declared format
- [ ] Dimensions match the declared size / aspect ratio
- [ ] Expected number of files exists (variants, sheet outputs)
- [ ] Alpha channel present when transparency is declared
- [ ] Output saved inside the declared output root
- [ ] Manifest entry has a valid design-sheet path
- [ ] All referenced files exist
- [ ] No duplicate asset IDs
- TODO: project-specific automatable checks

## Visual checks (model or human judgement)

- [ ] Subject matches the canonical reference
- [ ] Character proportions consistent with the design sheet
- [ ] Orientation correct
- [ ] Pose readable at intended display size
- [ ] Frame sequence coherent (sprite sheets)
- [ ] Style matches `style.md`
- [ ] Palette within the intended visual language
- [ ] No important content cropped
- [ ] Declared text exact and legible
- [ ] No prohibited elements from the negative rules
- TODO: project-specific visual checks

## Review policy

- Automatic retry on deterministic failures, up to `max_attempts`.
- `approved` status normally requires human sign-off: TODO confirm reviewer(s).
- Visual consistency is judged, never guaranteed.
