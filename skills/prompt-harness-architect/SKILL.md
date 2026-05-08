---
name: prompt-harness-architect
description: Design, critique, and improve production LLM prompts, chatbot system prompts, and task harnesses. Use when an AI agent needs to create or refine prompts with task context, stable and dynamic context separation, prompt caching, tool or API behavior, examples, output formats, response prefill, hallucination controls, uncertainty handling, conversation history, extended-thinking or reasoning-trace diagnosis, and evaluation cases.
---

# Prompt Harness Architect

Use this skill to design prompts as production harnesses, not one-off chatbot messages. Keep the output practical: a revised prompt or harness, a short rationale, and eval cases when the task has real behavioral risk.

## Workflow

### 1. Contract

Define the task before writing the prompt:

- Who the model helps.
- What job the model must do.
- What it must not do.
- What success looks like.
- Whether the answer is for a human, an API, a database, or another agent.
- What uncertainty behavior is required.

For high-stakes or ambiguous tasks, explicitly tell the model when to refuse, ask for missing information, escalate to a human, or say it cannot determine the answer.

### 2. Structure

Separate the prompt into stable context, dynamic input, runtime controls, and output requirements.

Stable context includes schemas, policies, rubrics, examples, product rules, and domain definitions. It is usually the best candidate for prompt caching when the runtime supports caching.

Dynamic input includes the user's request, current document, retrieved snippets, images, current tool results, and conversation state.

Use labeled sections with Markdown headings or XML-style tags. Prefer one clear structure over clever prose.

For a fill-in scaffold, read `references/prompt-harness-template.md`.

### 3. Steer

Add only the steering the task actually needs:

- Procedure order: tell the model what to inspect first, compare second, and conclude last.
- Evidence rules: require factual claims to be grounded in provided input when useful.
- Examples: add few-shot examples for hard, ambiguous, or repeatedly failing cases.
- Conversation state: for chatbots, include relevant recent turns, user preferences, summarized state, and important tool results. Do not blindly append the full conversation forever.
- Final reminders: restate the few constraints that matter most near the end.

### 4. Format

Choose the output shape based on the consumer:

- Human reader: concise prose or Markdown.
- API/database: strict JSON schema.
- XML parser: tagged final block.
- Mixed use: short human summary plus a strict structured block.

If the runtime supports response prefill, use it as a separate lever from output instructions: `{` for JSON objects, `[` for JSON arrays, or a tag such as `<final_verdict>` when the application only needs a final block.

For runtime-specific capability notes, read `references/harness-runtime-notes.md`.

### 5. Evaluate

Create eval cases before calling the prompt good:

- Happy path.
- Ambiguous input.
- Missing information.
- Conflicting evidence.
- Irrelevant or adversarial input.
- Output-format compliance.
- Conversation-history or stale-context case for chatbots.
- Known prior failures.

When reasoning traces, extended thinking, scratchpads, logs, or prior model outputs are available, use them as diagnostic material. Find where the model misunderstood, skipped evidence, guessed, or used the wrong order; then convert that observation into clearer instructions, examples, references, or eval cases. Do not expose hidden reasoning to end users.

For an eval template, read `references/eval-case-template.md`.

## Expected Output

When improving a prompt, usually return:

1. A short diagnosis of the current prompt.
2. A revised prompt or harness.
3. Key design choices, briefly.
4. Eval cases for the revised harness.
5. Any unresolved ambiguity or missing domain context.

For small prompt edits, skip the long explanation and provide the revised prompt directly.

## Source Notes

This skill is original synthesis inspired by public prompting guidance and production prompt-harness patterns. For provenance and attribution guidance, read `references/source-notes.md`.
