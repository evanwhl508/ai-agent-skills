# AI Agent Skills

Cross-harness open-source skills for AI coding agents and chatbot-building workflows.

This repo is a multi-skill collection: one repository, one folder per skill, and thin adapters for each agent harness. The canonical skill source lives under `skills/<skill-name>/`; Codex, Claude Code, Cursor, OpenCode, and future harnesses should load or copy from that same source instead of maintaining forks.

## Skills

| Skill | Status | Description |
|---|---|---|
| [`prompt-harness-architect`](skills/prompt-harness-architect/SKILL.md) | v0.1 | Design, critique, and improve production LLM prompts, chatbot system prompts, task harnesses, structured outputs, and eval cases. |

## Install

Preferred npm UX after the package is published:

```bash
# List available skills
npx @evan/ai-agent-skills list

# Install one skill
npx @evan/ai-agent-skills add prompt-harness-architect

# Install all skills in the collection
npx @evan/ai-agent-skills add all
```

Target-specific installs:

```bash
npx @evan/ai-agent-skills add prompt-harness-architect --target codex
npx @evan/ai-agent-skills add prompt-harness-architect --target claude-code
npx @evan/ai-agent-skills add all --target codex
```

Until the npm package is published, run from a local clone:

```bash
git clone https://github.com/evanwhl508/ai-agent-skills.git
cd ai-agent-skills
node bin/ai-agent-skills.js list
node bin/ai-agent-skills.js add prompt-harness-architect --target codex
```

By default, target paths are:

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

For harnesses that only need `SKILL.md` and references, copy the same folder and ignore adapter-specific files such as `agents/openai.yaml`.

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

## Development

```bash
npm test
node bin/ai-agent-skills.js list
node bin/ai-agent-skills.js add prompt-harness-architect --target generic --dir /tmp/ai-agent-skills-test --force
```

## License

MIT
