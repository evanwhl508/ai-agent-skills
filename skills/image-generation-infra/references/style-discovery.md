# Style Discovery Playbook

The style guide gates everything downstream: every prompt is composed from it, every QA judgement is made against it. A wrong style guide poisons every generated asset. So the rule is absolute: **derive the style from evidence when evidence exists; interview the user when it does not; never invent a style silently.**

## Step 1: Hunt for visual signal

Search the project for anything that encodes visual decisions. Typical sources by project type:

| Source | What it tells you |
|---|---|
| Existing art (`assets/`, `sprites/`, `images/`, `Assets.xcassets`, `res/drawable*`, `public/`) | Genre, rendering style, line treatment, proportions, level of detail, background handling |
| Theme/style code (`theme.dart`, `tailwind.config.*`, CSS custom properties, `colors.xml`, SwiftUI/Compose theme files, design tokens) | Exact palette hex values, semantic color roles, dark/light variants |
| App icon, logo, favicon | Brand shape language, core colors, mood |
| Design docs, READMEs, specs, wireframes | Intended genre, mood, audience, references the team already agreed on |
| Store listings, marketing pages, screenshots | The style already shipped to users |
| Fonts and typography config | Playful vs formal register, era, energy |
| Copywriting tone (onboarding text, button labels) | Vibe: cozy, snarky, clinical, epic |

Read broadly before concluding. Three sprites and a theme file outweigh one old mockup.

## Step 2: Derive and cite

Draft `style.md` and `palette.md` from the evidence. Every substantive conclusion carries its source:

```markdown
- Rendering style: flat shading with thick dark outlines
  (evidence: all 14 sprites in assets/sprites/ use 3px #2B2B2B outlines, no gradients)
- Primary palette: #FFB347, #6BCB77, #4D96FF
  (evidence: theme.dart lines 12-18, also dominant in app icon)
- Mood: cozy, gently comic (evidence: onboarding copy in strings.json, rounded shape language throughout)
```

Rules for derivation:

- Extract hex values programmatically from theme files where possible; do not eyeball colors that are written down somewhere.
- Distinguish what the evidence proves from what it merely suggests. Suggestive inferences get `TODO: confirm` markers, not confident prose.
- If sources conflict (old mockups vs shipped assets), prefer what shipped, note the conflict, and ask.
- Never pad thin evidence into a full style guide. Gaps stay as explicit `TODO` items or interview questions.

Then present the derived summary to the user for confirmation before locking it in. The presentation should be short: conclusions, evidence, open questions. Proceed once confirmed (or after applying corrections).

## Step 3: Interview when there is no signal

For an empty repo or idea-stage project, do not write `style.md` at all until the user has confirmed the style. Interview in two or three short rounds rather than one wall of questions, and offer concrete options instead of open-ended prompts — most people recognize a style faster than they can describe one.

Round 1 — the big shape:

- Visual genre: pick or describe — flat vector / pixel art / painterly / cel-shaded / claymation-look / hand-drawn sketch / 3D-render look / photographic.
- Mood, in a few words: cozy, epic, spooky-cute, clinical, chaotic, minimal, luxurious…
- One or two existing products, games, or films whose look feels right (as inspiration for genre and mood — describe what qualities to borrow, never instruct the generator to copy a specific living artist's style).

Round 2 — the rules that generation actually needs:

- Line style: outlines or no outlines? Thick or thin? Colored or dark?
- Shading: flat, soft, cel bands, painterly?
- Proportions for characters: realistic, chibi, tall-stylized?
- Level of detail: minimal shapes vs dense texture?
- Background treatment: transparent subjects, flat color, full scenes?
- Palette direction: bright/saturated, muted/earthy, dark/neon…? Any brand colors that already exist anywhere (even a napkin sketch)?

Round 3 — the guardrails:

- Anything the style must never include (realistic gore in a kids' game, text baked into images, gradients, photorealism…)?
- How much stylistic variation is acceptable between assets?

Reflect the answers back as a draft style summary and get an explicit yes before writing `style.md` and `palette.md`. "Sounds good" on a concrete summary counts; silence does not.

## Step 4: Record how the style was established

At the top of `style.md`, record the provenance so future runs (and future humans) know how much to trust it:

```markdown
> Provenance: derived from existing assets and theme.dart on 2026-07-07,
> confirmed by the user. Open items are marked TODO.
```

or

```markdown
> Provenance: no existing visual assets; established via user interview
> on 2026-07-07 and explicitly confirmed.
```

## Anti-patterns

- Writing a plausible-sounding style guide for an empty project without asking. This is the failure mode this whole playbook exists to prevent.
- Asking the user questions the codebase already answers ("what are your brand colors?" when `theme.dart` lists them).
- Confusing decorativeness with fidelity: a beautiful style guide that does not match the shipped product is worse than a plain one that does.
- Copying a named living artist's style. Describe genre, technique, and mood instead.
