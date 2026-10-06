# Gunadarma Informatics PI skill

A skill for writing and auditing *Penulisan Ilmiah* (PI) against the Informatics Program's 2025 handbook. The skill is in Indonesian and works with Claude Code, Codex, and Hermes Agent.

[Read the skill](SKILL.md) · [Download the official PDF](https://drive.google.com/file/d/1PJt6gNmPIAneWNRWJ77XT3Lz-gTEb07o/view) · [Check sample conflicts](references/konflik-visual-lampiran.md)

## Install

Clone the repo, then set `DEST` to the directory for your agent. Copy the skill and its references together.

```sh
git clone https://github.com/azrahudaya/skill-pi-informatika-gunadarma.git
cd skill-pi-informatika-gunadarma
SKILL=pedoman-pi-informatika-gunadarma-2025
DEST="$HOME/.claude/skills/$SKILL"  # Claude Code
# DEST="$HOME/.agents/skills/$SKILL"  # Codex
# DEST="$HOME/.hermes/skills/productivity/$SKILL"  # Hermes Agent
mkdir -p "$DEST/references"
cp SKILL.md "$DEST/"
cp -R references/. "$DEST/references/"
```

Start a new session after installation. The handbook PDF is not bundled; provide it alongside a manuscript for an exact audit. Confirm current submission procedures with the program. This is an independent skill, not an official university publication.

Package checks: `python3 scripts/validate.py` and `python3 -m unittest discover -s tests -v`. The authored skill remains proprietary pending a reuse-license decision; the university PDF is linked, not relicensed here.

## Contributor

<a href="https://github.com/azrahudaya"><img src="https://avatars.githubusercontent.com/u/95754136?v=4" width="48" height="48" alt="Azra Hudaya's GitHub avatar"><br>Azra Hudaya (@azrahudaya)</a>
