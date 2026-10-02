#!/usr/bin/env python3
"""Check skill structure and local inline Markdown file links; no network access."""

from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

try:
    import yaml
except ImportError:
    sys.exit("Install validation dependencies: python3 -m pip install -r requirements-dev.txt")


ROOT = Path(__file__).resolve().parents[1]
REQUIRED = (
    "SKILL.md",
    "references/learning-and-memory.md",
    "README.md",
    "CONTRIBUTING.md",
    "evals/cases.md",
    "CHANGELOG.md",
)


def validate(root: Path) -> list[str]:
    errors = []
    for relative in REQUIRED:
        if not (root / relative).is_file():
            errors.append(f"Missing required file: {relative}")

    skill = root / "SKILL.md"
    if skill.is_file():
        text = skill.read_text(encoding="utf-8")
        match = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)", text, re.DOTALL)
        if not match:
            errors.append("SKILL.md needs YAML frontmatter at the start.")
        else:
            try:
                metadata = yaml.safe_load(match.group(1))
            except yaml.YAMLError as error:
                errors.append(f"Invalid YAML frontmatter: {error}")
            else:
                if not isinstance(metadata, dict):
                    errors.append("Skill frontmatter must be a mapping.")
                else:
                    if metadata.get("name") != "simplish":
                        errors.append("Skill name must be simplish.")
                    description = metadata.get("description")
                    if not isinstance(description, str) or not description.strip():
                        errors.append("Skill description must be a nonempty string.")
                    elif len(description) > 1024:
                        errors.append("Skill description must be at most 1024 characters.")
        if not text[match.end() if match else 0:].strip():
            errors.append("SKILL.md needs instructions after the frontmatter.")

    markdown_files = [*root.glob("*.md"), *root.glob("references/**/*.md"), *root.glob("evals/**/*.md")]
    for path in markdown_files:
        text = path.read_text(encoding="utf-8")
        # Ignore fenced examples. This checks inline file links, not anchors or remote URLs.
        text = re.sub(r"^```[^\n]*\n.*?^```\s*$", "", text, flags=re.MULTILINE | re.DOTALL)
        for raw_target in re.findall(r"\[[^\]\n]*\]\(([^)\n]+)\)", text):
            target = raw_target.strip().strip("<>")
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            resolved = (path.parent / unquote(parsed.path)).resolve()
            if not resolved.is_relative_to(root.resolve()):
                errors.append(f"{path.relative_to(root)}: link leaves repository: {target}")
            elif not resolved.exists():
                errors.append(f"{path.relative_to(root)}: missing link target: {target}")
    return errors


if __name__ == "__main__":
    failures = validate(ROOT)
    if failures:
        print("Validation failed:")
        print("\n".join(f"- {failure}" for failure in failures))
        sys.exit(1)
    print("Simplish metadata, required files, and local Markdown file links are valid.")
