# Contributing

Contributions are welcome, but the collection should stay small, portable, and useful.

## Skill Rules

- Put canonical skill content in `skills/<skill-name>/`.
- Keep `SKILL.md` concise and harness-neutral.
- Use only `name` and `description` in canonical skill frontmatter.
- Put detailed examples, templates, and runtime-specific notes in `references/`.
- Do not copy third-party transcripts, docs, or course material unless the license clearly allows redistribution.
- Prefer original synthesis, attribution, and small quoted snippets only when needed.
- Add or update `manifests/skills.json` for every installable skill.
- Keep adapter files thin. They should point to canonical skill source instead of duplicating workflow text.

## Validation

Run:

```bash
npm test
```

Before opening a pull request, manually test at least one install:

```bash
node bin/ai-agent-skills.js add <skill-name> --target generic --dir /tmp/ai-agent-skills-test --force
```

Also verify compatibility with the public `skills` CLI when possible:

```bash
npx skills add . --list
npx skills add . --skill <skill-name> -a codex --copy -y
```

If you are testing from a fork or branch before merge, use a local path or full git URL rather than `evanwhl508/ai-agent-skills`.
