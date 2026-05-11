# Harness Portability Strategy

## Goal

Make every skill in this collection easy to adopt from multiple AI-agent harnesses: Codex, Claude Code, Cursor, OpenCode, OpenClaw-style installers, and future tools.

The repo follows the same broad practice as Everything Claude Code: keep durable workflows in shared source files, then adapt loading, metadata, commands, hooks, and marketplace packaging at the harness edge.

## Core Principle

Author once. Adapt at the edge.

Canonical behavior belongs in:

```text
skills/<skill-name>/SKILL.md
skills/<skill-name>/references/
skills/<skill-name>/assets/
skills/<skill-name>/scripts/
```

Harness-specific files should only explain how shared skills are loaded or exposed.

If the same workflow text has to be edited in several harness-specific places, the structure is wrong. Move durable behavior back into `skills/<skill-name>/`.

## Installer UX

Preferred command:

```bash
npx skills add evanwhl508/ai-agent-skills --skill prompt-harness-architect
```

The CLI must support both single-skill and all-skills installation:

```bash
npx skills add evanwhl508/ai-agent-skills --list
npx skills add evanwhl508/ai-agent-skills --skill prompt-harness-architect
npx skills add evanwhl508/ai-agent-skills --skill '*'
npx skills add evanwhl508/ai-agent-skills --skill prompt-harness-architect -a codex
npx skills add evanwhl508/ai-agent-skills --skill '*' -a claude-code
npx skills add evanwhl508/ai-agent-skills --all
```

`--skill '*'` selects every skill in the repo for the chosen agent target. `--all` is broader: it expands to every skill and every agent, with prompts skipped.

The repo may also ship a custom helper CLI as a local development and fallback path, but public docs should lead with `npx skills`.

The upstream `npx skills` CLI copies the canonical skill folder as-is. Harness-specific pruning such as dropping `agents/` for non-Codex targets is a feature of this repo's local helper CLI, not the upstream installer.

## Adapter Rules

- Keep `SKILL.md` plain Markdown with simple YAML frontmatter.
- Use only `name` and `description` in canonical skill frontmatter.
- Put display names, marketplace fields, and UI metadata in adapter manifests.
- Treat hooks, commands, agents, and MCP configs as optional adapters.
- Keep adapter manifests thin; do not duplicate the workflow.
- Support manual copy into a generic skills folder.

## Current Adapter Matrix

| Harness | Support level | Notes |
|---|---|---|
| Codex | First-class | Canonical skill + `.codex-plugin` metadata + `agents/openai.yaml`. |
| Claude Code | Initial | Canonical skill + `.claude-plugin` metadata; native commands/hooks are planned. |
| Cursor | Planned | Stub adapter notes only. |
| OpenCode / OpenClaw | Planned | Stub adapter notes only. |

## Reference Practice

This strategy is informed by:

- https://github.com/affaan-m/everything-claude-code
- https://github.com/affaan-m/everything-claude-code/blob/main/docs/architecture/cross-harness.md

Borrow the architecture pattern, not the exact content.
