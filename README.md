# AI Agent Skills

Cross-harness open-source skills for AI coding agents and chatbot-building workflows.

This repo is designed as a multi-skill collection: one repository, one folder per skill, and thin adapters for each agent harness. It currently ships one skill, with more planned. The canonical skill source lives under `skills/<skill-name>/`; Codex, Claude Code, Cursor, OpenCode, and future harnesses should load or copy from that same source instead of maintaining forks.

## Skills

| Skill | Status | Description |
|---|---|---|
| [`prompt-harness-architect`](skills/prompt-harness-architect/SKILL.md) | v0.1 | Design, critique, and improve production LLM prompts, chatbot system prompts, multimodal document/image review harnesses, structured outputs, and eval cases. |

## Install

### Quick Install (Recommended)

Use the open agent skills CLI:

```bash
# List available skills
npx skills add evanwhl508/ai-agent-skills --list

# Install one skill
npx skills add evanwhl508/ai-agent-skills --skill prompt-harness-architect

# Install all skills in the collection
npx skills add evanwhl508/ai-agent-skills --skill '*'
```

`--skill '*'` means "select every skill from this repo." `--all` means "install every skill to every detected agent and skip prompts" because it is shorthand for `--skill '*' --agent '*' -y`.

### Target-Specific Installs

```bash
npx skills add evanwhl508/ai-agent-skills --skill prompt-harness-architect -a codex
npx skills add evanwhl508/ai-agent-skills --skill prompt-harness-architect -a claude-code
npx skills add evanwhl508/ai-agent-skills --skill '*' -a codex
```

To install all skills to all detected agents without prompts:

```bash
npx skills add evanwhl508/ai-agent-skills --all
```

### From A Clone

This repo also ships a small local helper CLI. Use it from a clone when working on the repo itself:

```bash
git clone https://github.com/evanwhl508/ai-agent-skills.git
cd ai-agent-skills
node bin/ai-agent-skills.js list
node bin/ai-agent-skills.js add prompt-harness-architect --target codex
```

The upstream `npx skills` CLI installs the canonical skill folder as-is. That means Codex UI metadata such as `agents/openai.yaml` may appear in non-Codex installs, where it should be ignored. The local helper CLI applies this repo's `excludePaths` and omits Codex-only metadata for non-Codex targets.

If this package is later published to npm, the same helper can be exposed as:

```bash
npx @evanwhl508/ai-agent-skills list
npx @evanwhl508/ai-agent-skills add prompt-harness-architect
```

### Local Helper Defaults

For the local helper CLI, default target paths are:

| Target | Default install path | Override |
|---|---|---|
| `codex` | `$CODEX_HOME/skills` or `~/.codex/skills` | `--dir <path>` |
| `claude-code` | `$CLAUDE_HOME/skills` or `~/.claude/skills` | `--dir <path>` |
| `generic` | `./skills` in the current directory | `--dir <path>` |

Use `--force` to replace an existing installed skill folder.

## Manual Install

Copy the desired skill folder into your harness's skills directory:

```bash
cp -R skills/prompt-harness-architect ~/.codex/skills/
```

For non-Codex harnesses that only need `SKILL.md` and references, omit or ignore adapter-specific files such as `agents/openai.yaml`.

## Repository Layout

```text
ai-agent-skills/
|-- skills/
|   `-- prompt-harness-architect/
|       |-- SKILL.md
|       |-- agents/
|       |   `-- openai.yaml
|       `-- references/
|-- manifests/
|   |-- skills.json
|   `-- adapters.json
|-- .codex-plugin/
|   `-- plugin.json
|-- .claude-plugin/
|   `-- plugin.json
|-- .cursor/
|   `-- README.md
|-- .opencode/
|   `-- README.md
|-- bin/
|   `-- ai-agent-skills.js
`-- docs/
    `-- architecture/
        `-- harness-portability-strategy.md
```

## Design Principles

- Author once, adapt at the edge.
- Keep each canonical `SKILL.md` concise and harness-neutral.
- Put deeper examples, runtime notes, and templates in `references/`.
- Treat commands, hooks, plugin manifests, and marketplace metadata as adapters.
- Support one-by-one installs and all-in-one batch installs from the same manifest.

## Adapter Support

| Harness | Support level | Notes |
|---|---|---|
| Codex | First-class | Canonical skill + `.codex-plugin` metadata + `agents/openai.yaml`. |
| Claude Code | Initial | Canonical `SKILL.md` + `.claude-plugin` metadata; native commands/hooks are planned. |
| Cursor | Planned | Stub adapter notes only. |
| OpenCode / OpenClaw | Planned | Stub adapter notes only. |

## Development

```bash
npm test
node bin/ai-agent-skills.js list
node bin/ai-agent-skills.js add prompt-harness-architect --target generic --dir /tmp/ai-agent-skills-test --force
```

## License

MIT
