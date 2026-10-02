# Contributing to Simplish

Improve Simplish by starting with a concrete reading or learning problem. An example that is difficult to follow, changes the source meaning, skips a prerequisite, or ignores the requested depth is more useful than a general request to make the skill “smarter.”

## Propose a focused change

1. Open an issue or describe the problem in a pull request. Include a minimal prompt, the relevant response, and what the reader should have been able to understand or do.
2. Remove personal, confidential, and machine-specific information. Use a fictional example when the original cannot be shared safely.
3. Check whether an existing instruction already covers the problem. Prefer clarifying a rule or adding a useful example over accumulating overlapping rules.
4. Make the smallest change that addresses the underlying issue. Keep the main skill concise; put detailed learning guidance and supporting evidence in the reference file.
5. Review the result against representative prompts and explain the observed improvement and any tradeoff.

Preserve the user's requested detail and format. Simple wording must retain technical meaning, exceptions, uncertainty, and useful reasoning. Do not make every response follow a fixed template or require practice when the user only asked for an answer or rewrite.

## Preserve evidence boundaries

The skill combines writing and teaching choices. Research supporting a component technique does not validate this particular skill or establish that it improves learning for every reader and subject.

When adding a learning claim, cite a relevant source in `references/learning-and-memory.md` and state what the study or guidance supports, its context, and its limits. Prefer original research or authoritative guidance. Distinguish practical design choices, such as the number of examples, from measured findings.

Avoid guarantees about attention or retention, fixed attention spans, universal memory limits, unsupported neuroscience, and learning-style diagnoses. Respect stated preferences and accessibility needs without inferring a biological learning type. Do not claim formal ASD-STE100 compliance.

Keep source attribution intact. If adapting material from elsewhere, check its license and preserve any required notices.

## Validate and review

From the repository root, run:

```sh
python3 scripts/validate.py
```

This structural check does not assess response accuracy or teaching quality. Review generated responses with the outcome-based rubric in [the evaluation cases](evals/cases.md). Run cases affected by a narrow change; use the full set when changing general writing or teaching behavior. Add a regression case when an existing case does not cover the problem.

For comparisons within one assistant, keep the prompt and model consistent and record the assistant and version, model, date, and skill revision. For portability changes, review affected cases in each supported assistant and report which were actually tested. Check for lost information as well as easier reading. A shorter or more fluent answer is not automatically a better answer.

## Submit a reviewable pull request

Describe the reader's problem, the resulting behavior, and the evidence from validation and response review. Include unresolved limitations when relevant. Report structural checks and human response reviews separately; neither is an automated test of memory or learning effectiveness.

Claims about learning or retention would require an appropriate study with learners, an assessment aligned with the goal, and delayed assessment for retention. Do not infer those outcomes from rubric scores alone.
