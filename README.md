# Gunadarma Informatics PI Skill

A writing and review skill for the 2025 *Penulisan Ilmiah* (PI) guide issued by the Informatics Program, Faculty of Industrial Technology, Universitas Gunadarma. The skill itself is in Indonesian, matching the guide and the documents it is intended to check. This repository is an independent study aid, not a university publication.

The guide covers topic selection, manuscript structure, formatting, citations, supervision, the examination, revisions, presentation, and final submission. `SKILL.md` identifies requirements by PDF page and printed page. `references/contoh-dan-lampiran.md` indexes the guide's fourteen example topic groups and ten appendices; `references/cakupan-halaman.md` maps all 36 PDF pages to the relevant skill sections. The skill distinguishes stated requirements from illustrations and records contradictions rather than silently resolving them.

## Install

Clone the repository, then copy both `SKILL.md` and `references/` into a skill directory. The relative path to `references/` must remain intact. The commands below are for a Unix shell; on Windows, use the equivalent copy operation or WSL. The folder name matches the skill's `name` field.

```sh
git clone https://github.com/azrahudaya/skill-pi-informatika-gunadarma.git
cd skill-pi-informatika-gunadarma
SKILL_NAME=pedoman-pi-informatika-gunadarma-2025
```

### Claude Code

```sh
mkdir -p "$HOME/.claude/skills/$SKILL_NAME/references"
cp SKILL.md "$HOME/.claude/skills/$SKILL_NAME/"
cp -R references/. "$HOME/.claude/skills/$SKILL_NAME/references/"
```

Start a new Claude Code session. Ask it to use `/pedoman-pi-informatika-gunadarma-2025` when reviewing an Informatics PI, or let it select the skill from your request. For one project only, place the same folder under that project's `.claude/skills/` instead of your home directory. [Claude Code skill locations](https://code.claude.com/docs/en/skills).

### Codex

```sh
mkdir -p "$HOME/.agents/skills/$SKILL_NAME/references"
cp SKILL.md "$HOME/.agents/skills/$SKILL_NAME/"
cp -R references/. "$HOME/.agents/skills/$SKILL_NAME/references/"
```

Restart Codex if the skill does not appear. Invoke it as `$pedoman-pi-informatika-gunadarma-2025` or describe the PI task and let Codex select it. For project-only use, place the folder under the project's `.agents/skills/`. [Codex skill locations](https://developers.openai.com/codex/skills).

### Hermes Agent

```sh
mkdir -p "$HOME/.hermes/skills/productivity/$SKILL_NAME/references"
cp SKILL.md "$HOME/.hermes/skills/productivity/$SKILL_NAME/"
cp -R references/. "$HOME/.hermes/skills/productivity/$SKILL_NAME/references/"
```

Start a new Hermes session or run `/reload-skills` in an existing one. Check with `hermes skills list`, then load explicitly with `/skill pedoman-pi-informatika-gunadarma-2025` if needed. If you use a named Hermes profile, install into that profile's skills directory instead. [Hermes documentation](https://hermes-agent.nousresearch.com/docs).

## Use and limits

Supply the original 2025 PDF and the PI manuscript when asking for an exact audit. The original document is needed to inspect the cover, logo, placement, signatures, and any wording the skill summarizes. The PDF and a full text transcription are not redistributed here.

Ask the agent to report each finding with the rule, evidence in the manuscript, the guide page, and a proposed fix. It must distinguish noncompliance from an untestable condition or an ambiguity in the guide. Do not treat appendix sample names, page counts, or titles as required values. Confirm time-sensitive examination and submission instructions with the Informatics Program before sending documents.

Source guide: [Informatics Program PI information](https://fti.gunadarma.ac.id/informatika/?page_id=563). This repository does not replace the applicable official guide or a supervisor's verified instructions.
