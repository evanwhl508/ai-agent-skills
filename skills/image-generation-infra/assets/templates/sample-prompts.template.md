# Sample Composed Prompts

> Pre-flight artifact. These are full prompts composed BY HAND from real
> `assets.yaml` entries, before any batch run. Two jobs:
>   1. Let a human eyeball the composition and fix the design files before
>      spending generation credits at scale.
>   2. Give the execution skill few-shot examples of a correctly composed
>      prompt, so it only has to add model-specific syntax on top.
>
> Keep these model-neutral: the nine composition layers, no Midjourney
> suffixes or ComfyUI nodes — that translation is the execution skill's job.
> Regenerate whenever style.md, the design sheets, or the templates change
> materially. Cover different asset types (a character, an object, a
> background, a UI icon) so the executor sees the range.

The composition order (see `prompt-templates.md`): project & use → global
style → subject identity → asset-specific action → camera & orientation →
consistency constraints → technical output → negative rules → reference
instructions.

---

## Sample: `TODO_asset_id` (type: TODO)

Manifest entry composed:

```text
TODO — paste the composed prompt here, assembling the nine layers from:
- project.* pointers (style, palette, negative rules)
- this asset's subject sheet (identity invariants)
- this asset's generation.description, orientation, size, background
- this asset's qa.must_not_have (as exclusions)
- this asset's subject.references (which is authoritative, and for what)
```

Negative prompt (if the target model separates it):

```text
TODO — the exclusion layer, phrased for a negative-prompt field.
```

Notes for the executor:

- Reference `TODO-master-reference.png` is authoritative for identity; do not copy its pose.
- TODO — any per-asset gotcha worth flagging.

---

## Sample: `TODO_asset_id_2` (type: TODO)

TODO — repeat for a second, different asset type.
