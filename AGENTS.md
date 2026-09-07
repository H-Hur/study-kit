# Working on study-kit

Read `CLAUDE.md` for the kit's purpose and maintenance rules. This repository holds
the reusable kit; learner profiles, courses, textbooks, and study records belong in
a separate study project. Kit documents are maintained in English.

Claude Code and Codex ship from the same repository and release version. Maintain
the learning procedures in `plugins/study-kit/`. The Codex package at
`plugins/study-kit-codex/` is generated; do not edit it directly.

For Codex packaging changes, edit `scripts/build_codex.py` or the files in `codex/`,
then run `python3 scripts/build_codex.py`. Read `docs/distribution.md` for the
installation and release workflow. Run `python3 scripts/build_codex.py --check`
before handing back a change. Raise the source plugin version whenever either
distributed package changes; the generator uses that version for Codex too.

Claude-specific paths and model names in `CLAUDE.md` describe the original runtime.
The Codex equivalents are documented in `codex/runtime.md`; do not assume Claude
environment variables or conversation storage exist in Codex.

When maintaining this repository in Codex, use `codex/runtime.md` for execution
even when a shared source document links to the Claude edition's runtime notes.
Historical budget figures are not Codex limits or reasons to halt bounded work.
