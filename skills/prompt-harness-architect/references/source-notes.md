# Source Notes

This skill is original synthesis. It was initially inspired by an Anthropic prompting 101 transcript about building a prompt iteratively for a multimodal review workflow.

Do not redistribute the raw transcript unless the license clearly allows it. Public repo content should use paraphrase, attribution, and independent examples.

## Distilled Principles

- Prompt engineering is iterative and empirical.
- Start with task context and role.
- Separate stable context from dynamic input.
- Structure prompt sections clearly.
- Tell the model what order to inspect evidence.
- Use examples for hard or ambiguous cases.
- Repeat critical constraints near the end.
- Specify the final output format.
- Use response prefill when a runtime supports it.
- Use reasoning traces or prior model outputs to diagnose missing instructions, then encode the fix in the prompt harness.

## Originality Guidance

Strengthen this skill with:

- Public prompting docs from multiple providers.
- Personal production lessons from shipped AI apps.
- Non-insurance examples such as support triage, document extraction, research review, internal tooling, and structured data cleanup.
- Eval cases that show how the workflow behaves, not just how it is described.
