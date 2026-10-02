# Simplish

**Simple words. Clear connections. Useful practice.**

Simplish is a reusable AI skill for explaining unfamiliar or complex subjects. It helps the reader find the main idea, follow the reasoning, and practise when learning is the goal.

It combines plain-language principles inspired by ASD-STE100, response organization inspired by i-have-adhd, and research on learning. It preserves the requested depth and technical meaning. The combined skill has not been experimentally validated for attention or learning gains.

## Use it

Load [SKILL.md](SKILL.md) as instructions in your preferred assistant, then ask it to use Simplish:

```text
Use Simplish to explain how a database index works. I know basic SQL.

Use Simplish to rewrite this document in simple English. Keep every condition.

Use Simplish to teach me how fractions work with an example and optional practice.

Use Simplish: Why must a career evolve with age? Is there one age when people peak?
Give a detailed answer and distinguish evidence from general advice.
```

| Your request | How Simplish responds |
|---|---|
| Quick question | Direct answer with necessary qualifications |
| Rewrite | Clearer language that preserves the original meaning |
| Explanation | Main idea, connected reasoning, and useful examples |
| Lesson | Prerequisites, worked examples, and optional practice |
| Study plan | Practice, feedback, and later review adapted to the goal |

Simplish does not force every answer into a template. Long answers stay complete. Necessary technical terms stay in the explanation and are defined where needed.

## Install or refresh the skill

The same `SKILL.md` and `references/` files use the shared skill format supported by both tools. No separate version of the instructions is needed.

| Tool | Personal skill folder | Explicit invocation |
|---|---|---|
| Codex | `~/.agents/skills/simplish/` | `$simplish` in the CLI or IDE; select the skill in the app |
| Claude Code | `~/.claude/skills/simplish/` | `/simplish` |

The locations and invocation methods follow the [Codex skill documentation](https://learn.chatgpt.com/docs/build-skills) and [Claude Code skill documentation](https://code.claude.com/docs/en/skills). Local installation applies to the local tools; it does not upload a skill to a cloud account.

To install for both tools on macOS or Linux, run this from the repository root:

```sh
for simplish_dir in "$HOME/.agents/skills/simplish" "$HOME/.claude/skills/simplish"; do
  mkdir -p "$simplish_dir/references"
  cp SKILL.md "$simplish_dir/SKILL.md"
  cp references/learning-and-memory.md "$simplish_dir/references/learning-and-memory.md"
done
```

These commands replace the two installed files. Save separate local edits first. If Simplish is already installed in another configured skills directory, refresh that copy instead of creating a duplicate. Keep this repository as the source for future changes.

The installed package is:

```text
simplish/
├── SKILL.md
└── references/
    └── learning-and-memory.md
```

For an assistant without a skill loader, supply the instructions from `SKILL.md` and include the learning reference when asking for a lesson or study plan. Package compatibility does not guarantee identical answers across models; use the evaluation cases to review behavior in each tool.

## Improve it

Start with a response that is hard to read, loses meaning, or fails to teach the requested idea. Make a focused change, then check the result with representative prompts.

Validation requires Python 3.9 or later. The skill itself is Markdown and needs no Python dependencies.

```sh
python3 -m venv .venv
. .venv/bin/activate
python3 -m pip install -r requirements-dev.txt
python3 scripts/validate.py
```

The validator checks skill metadata, required files, and local Markdown file links. It does not judge factual accuracy, reading quality, or learning outcomes. Use the [evaluation cases](evals/cases.md) for response review and the [contribution guide](CONTRIBUTING.md) for the full workflow.

## Repository guide

| File | Purpose |
|---|---|
| [SKILL.md](SKILL.md) | Main instructions loaded by the assistant |
| [Learning and memory](references/learning-and-memory.md) | Teaching guidance, sources, and evidence limits |
| [Evaluation cases](evals/cases.md) | Six realistic prompts and a review rubric |
| [CONTRIBUTING.md](CONTRIBUTING.md) | How to propose and evaluate improvements |
| [CHANGELOG.md](CHANGELOG.md) | History of meaningful changes |

## Sources and scope

- [ASD-STE100](https://www.asd-ste100.org/STE_faq.html) informs the use of clear wording and consistent terms. Simplish does not certify formal ASD-STE100 conformity.
- [i-have-adhd](https://github.com/ayghri/i-have-adhd) informs response organization. Simplish does not assume a diagnosis or a fixed attention span.
- The [learning reference](references/learning-and-memory.md) links the research behind retrieval practice, feedback, worked examples, and spaced review, with limits for each source.

Clarity can support understanding. Lasting learning also depends on prior knowledge, practice, feedback, and later use.
