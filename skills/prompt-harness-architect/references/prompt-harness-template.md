# Prompt Harness Template

Use this when creating a new prompt harness or rewriting a rough prompt into production form.

## Compact Template

```text
<task_context>
You are helping [user/persona/team] with [task].
The goal is [success condition].
Do not [forbidden behavior].
</task_context>

<stable_reference>
[Schemas, policies, rubrics, examples, product rules, domain definitions.]
</stable_reference>

<dynamic_input>
[User request, document, retrieved context, image description, tool result, current conversation state.]
</dynamic_input>

<procedure>
1. Read the stable reference.
2. Extract facts from the dynamic input.
3. Compare facts against the rubric or task criteria.
4. Identify uncertainty, missing information, or contradictions.
5. Produce the final answer in the requested format.
</procedure>

<uncertainty_policy>
If the evidence is insufficient, say what cannot be determined.
Do not invent facts or infer beyond the available evidence.
Escalate to a human when the task is high-stakes or ambiguous.
</uncertainty_policy>

<output_format>
[Markdown, JSON schema, XML tags, or mixed human + structured output.]
</output_format>

<final_reminders>
Use only provided evidence.
Follow the output format exactly.
Keep the final answer concise.
</final_reminders>
```

## JSON Output Contract Checklist

When the output must be JSON, specify:

- Required keys.
- Allowed enum values.
- Type of each field.
- Whether null is allowed.
- What to do with unknown or missing values.
- Whether extra keys are forbidden.
- Whether the runtime should prefill `{` or `[` when supported.

## Example Domain: Support Triage

Use a non-insurance example to avoid copying the source transcript's running case.

```text
Task: Classify a support ticket.
Stable context: severity rubric, product area list, escalation rules.
Dynamic input: customer ticket text, account tier, recent incidents.
Procedure: extract facts, map to severity, decide escalation, produce JSON.
Uncertainty policy: if severity depends on unavailable logs, set confidence to "low" and request the missing log.
```
