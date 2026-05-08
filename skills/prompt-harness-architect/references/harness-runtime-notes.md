# Harness Runtime Notes

Use this when translating a prompt harness across providers, agent tools, or coding-agent shells.

## Capability Map

| Concept | What to check | Fallback |
|---|---|---|
| Stable context | Where system/developer instructions and reusable references belong. | Put stable material before dynamic input with clear labels. |
| Prompt caching | Whether the provider supports caching long stable prefixes. | Still separate stable context; caching can be added later. |
| Response prefill | Whether the runtime lets you seed the assistant's first token or content. | Use stricter output instructions and schema validation. |
| Structured output | Whether JSON schema, tool calls, or response format controls exist. | Ask for strict JSON and validate/retry outside the model. |
| Extended thinking / reasoning traces | Whether hidden reasoning, debug traces, or logs are available. | Use visible intermediate summaries or prior outputs as diagnostic material. |
| Conversation history | How prior turns, summaries, memory, and tool results are supplied. | Pass only relevant recent turns and structured state. |

## Provider-Neutral Rules

- Treat runtime features as optional. The prompt should still make sense without caching, prefill, or hidden reasoning.
- Do not expose hidden reasoning to end users.
- If a model needs to think through a complex task, ask for concise intermediate findings only when they are useful to the user or downstream system.
- Prefer external validation for strict output contracts.
- Keep harness-specific instructions out of the canonical skill unless clearly labeled.

## Install Targets

| Target | Typical install behavior |
|---|---|
| Codex | Copy the full skill folder, including `agents/openai.yaml`. |
| Claude Code | Copy `SKILL.md` and references; ignore Codex UI metadata if unsupported. |
| Cursor | Convert or reference the workflow as rules/instructions when a native skill loader is unavailable. |
| Generic | Copy `SKILL.md` and references into any folder the harness can load. |
