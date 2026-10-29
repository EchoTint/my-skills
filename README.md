# my-skills

Personal Agent Skills maintained by [EchoTint](https://github.com/EchoTint).
Each skill is self-contained: its instructions, references, and helper scripts
live together under `skills/`.

[English](README.md) | [简体中文](README.zh-CN.md) | [Changelog](CHANGELOG.md)

## Skills

| Skill | Purpose |
| --- | --- |
| [reading-study-coach](skills/reading-study-coach/) | Guided book and paper study, multi-source topic reading, adaptive learning routes, practice, mastery checks, and spaced review. |

## Install

With Node.js available, the [Skills CLI](https://github.com/vercel-labs/skills)
can discover the skills in this repository:

```bash
# List available skills without installing one.
npx skills add EchoTint/my-skills --list

# Install the reading coach into the current project.
npx skills add EchoTint/my-skills --skill reading-study-coach

# Install at user scope instead.
npx skills add EchoTint/my-skills --skill reading-study-coach -g
```

Alternatively, give your agent this repository URL and ask it to read
`skills/reading-study-coach/SKILL.md`. For manual installation, place the entire
skill folder in a supported skill directory, not just `SKILL.md`. In Magpie,
add the skill's local folder through Library and select the intended agents.
Check for an existing installation before creating another copy.

## Reading Study Coach

The coach chooses a learning route from the user's goal, the book's actual
dependencies, and demonstrated knowledge. It does not assume that chapter order
must be learning order. It can work across several sources around shared questions.

In systematic study, explanation, independent assessment, and verified practice
are separate from merely reading a chapter. The coach tracks pending work and
review dates in a workspace-local `book-wiki/`; those personal records do not
belong in this repository.

Example requests in a supporting agent:

```text
Use $reading-study-coach to help me learn this book.
Use $reading-study-coach to build an overview of this topic across these books.
Use $reading-study-coach to check my understanding of this paper's evidence.
```

The core workflow is text instructions. Optional PDF helpers use Python 3.10+
with `pypdf` (or `PyPDF2` for text intake) and Pillow for embedded-image handling.
OCR additionally needs a suitable Windows OCR environment, or Poppler and
Tesseract with the required language data. These tools are not bundled or
installed automatically. Image preparation alone is not completed OCR.

## Repository Layout

```text
my-skills/
  README.md
  README.zh-CN.md
  CHANGELOG.md
  .github/workflows/validate.yml
  tools/validate_skills.py
  skills/
    reading-study-coach/
      SKILL.md
      THIRD_PARTY_NOTICES.md
      agents/openai.yaml
      references/
      scripts/
```

New independent capabilities get a new folder under `skills/`. Keep detailed
conditional guidance in references and load it only when needed. Keep packaging,
tests, and repository maintenance outside the installed skill folder.

Run the dependency-free structural validator from the repository root:

```bash
python tools/validate_skills.py
```

It checks skill identity, bundled local references, unsafe symlinks, and Python
syntax. It does not evaluate teaching quality or prove that optional OCR works.

## Sources And Licensing

The reading coach combines original integration work with adapted workflows and
utilities from other skills. Preserve its
[third-party notices](skills/reading-study-coach/THIRD_PARTY_NOTICES.md).
Some upstream licensing remains unconfirmed; this repository does not grant a
blanket MIT license or imply that all included material is freely redistributable.
Review the notices and upstream terms before redistribution.

Repository organization takes inspiration from
[JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design): a skill catalog,
bilingual entry documents, self-contained skill directories, and separate
maintenance tooling. No design skill or editor code was copied from that project.
