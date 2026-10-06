#!/usr/bin/env python3
"""Check the published skill package without requiring the source PDF."""

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
NAME = "pedoman-pi-informatika-gunadarma-2025"


def check(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def numbered_entries(text: str) -> list[int]:
    return [int(n) for n in re.findall(r"(?m)^(\d+)\. ", text)]


def main() -> None:
    skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    examples = (ROOT / "references/contoh-dan-lampiran.md").read_text(encoding="utf-8")
    coverage = (ROOT / "references/cakupan-halaman.md").read_text(encoding="utf-8")
    visual = (ROOT / "references/konflik-visual-lampiran.md").read_text(encoding="utf-8")

    check(skill.startswith("---\n"), "SKILL.md must start with YAML frontmatter")
    check("\n---\n" in skill[4:], "SKILL.md frontmatter needs a closing --- line")
    frontmatter, body = skill[4:].split("\n---\n", 1)
    check(bool(body.strip()), "SKILL.md needs a body after frontmatter")
    fields = dict(re.findall(r"(?m)^(name|description):\s*(.+)$", frontmatter))
    check(fields.get("name") == NAME, "skill name mismatch")
    check(bool(fields.get("description")), "missing description")

    topics, appendices = examples.split("## Lampiran resmi", 1)
    check(numbered_entries(topics) == list(range(1, 15)), "expected 14 ordered topics")
    check(numbered_entries(appendices) == list(range(1, 11)), "expected 10 ordered appendices")
    pages = [int(n) for n in re.findall(r"(?m)^\| (\d+) \|", coverage)]
    check(pages == list(range(1, 37)), "expected an ordered index of all 36 PDF pages")

    references = set(re.findall(r"`(references/[^`]+\.md)`", skill))
    check(references == {
        "references/cakupan-halaman.md",
        "references/contoh-dan-lampiran.md",
        "references/konflik-visual-lampiran.md",
    }, "SKILL.md must reference every packaged reference")
    for relative in references:
        check((ROOT / relative).is_file(), f"missing reference: {relative}")
    for text in (skill, readme, examples, coverage, visual):
        check("\u2014" not in text, "em dash found")
    published_text = "\n".join((skill, readme, examples, coverage, visual))
    check(re.search(r"(?:/home/[^/\s]+/|C:\\Users\\[^\\\s]+\\)", published_text) is None, "local path leaked")
    check(not list(ROOT.rglob("*.pdf")), "source PDF must not be included in this package")
    print("PASS: skill metadata, 14 topics, 10 appendices, 36-page index, references, public-file checks")


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc
