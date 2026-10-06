# Gunadarma Informatics PI skill

A cross-agent guide to the Informatics Program's 2025 *Penulisan Ilmiah* (PI) handbook. The skill is in Indonesian; this README is in English. Independent work, not an official Universitas Gunadarma publication.

`SKILL.md` covers the manuscript, formatting, citations, supervision, defense, revisions, and submission. Its references index all 36 PDF pages, 14 example topic groups, and 10 appendices. The [visual conflict notes](references/konflik-visual-lampiran.md) distinguish written rules from inconsistent samples. Consult the original handbook for exact wording and artwork; neither the PDF nor its full transcript is distributed here.

## Install

Clone once, then copy the whole skill folder to the agent you use. These commands use a Unix shell (or WSL on Windows).

```sh
git clone https://github.com/azrahudaya/skill-pi-informatika-gunadarma.git
cd skill-pi-informatika-gunadarma
SKILL_NAME=pedoman-pi-informatika-gunadarma-2025
```

| Agent | Personal skill directory | Explicit invocation |
| --- | --- | --- |
| Claude Code | `~/.claude/skills/$SKILL_NAME/` | `/pedoman-pi-informatika-gunadarma-2025` |
| Codex | `~/.agents/skills/$SKILL_NAME/` | `$pedoman-pi-informatika-gunadarma-2025` |
| Hermes Agent | `~/.hermes/skills/productivity/$SKILL_NAME/` | `/skill pedoman-pi-informatika-gunadarma-2025` |

For Claude Code:

```sh
DEST="$HOME/.claude/skills/$SKILL_NAME"
mkdir -p "$DEST/references"
cp SKILL.md "$DEST/"
cp -R references/. "$DEST/references/"
```

For Codex:

```sh
DEST="$HOME/.agents/skills/$SKILL_NAME"
mkdir -p "$DEST/references"
cp SKILL.md "$DEST/"
cp -R references/. "$DEST/references/"
```

For Hermes Agent:

```sh
DEST="$HOME/.hermes/skills/productivity/$SKILL_NAME"
mkdir -p "$DEST/references"
cp SKILL.md "$DEST/"
cp -R references/. "$DEST/references/"
```

Start a new agent session after installation. Hermes also supports `/reload-skills`. For project-only installation, use `.claude/skills/` or `.agents/skills/` under that project. For a named Hermes profile, install under that profile's `skills/` directory. See the [Claude Code](https://code.claude.com/docs/en/skills), [Codex](https://developers.openai.com/codex/skills), and [Hermes](https://hermes-agent.nousresearch.com/docs) documentation for current skill locations.

## Use

Provide the handbook PDF and the latest PI manuscript when requesting an exact audit. For example: “Audit this PI against the 2025 Informatics handbook. Report the rule, manuscript evidence, handbook page, and required correction. Mark unresolved conflicts as ambiguous.” Do not infer compliance from the page index alone. Confirm current administrative instructions with the program before sending files or printing a final copy.

Check the package with `python3 scripts/validate.py` and `python3 -m unittest discover -s tests -v`. GitHub Actions runs both on pushes and pull requests. These checks cover packaging and traceability, not whether a student's manuscript complies with the handbook.

The source handbook is linked from the [Informatics Program's PI page](https://fti.gunadarma.ac.id/informatika/?page_id=563). The authored skill is marked proprietary pending a separate reuse-license decision; the original handbook is not licensed by this repository.
