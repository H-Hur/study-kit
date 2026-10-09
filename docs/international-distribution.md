# International distribution

## Listing copy

**Name:** Study Kit  
**Short description:** Study and create textbooks

Create a focused textbook for your own learning or teaching materials for other
learners. Learning mode starts from your level and skips familiar material.
Authoring mode records instructor and learner levels, then supports material within
the instructor's knowledge or a bounded researched extension. Both modes verify
sources, design curricula, revise explanations, and prepare PDF/DOCX editions using
available conversion and layout tools.

Available for noncommercial use: code uses PolyForm Noncommercial 1.0.0; documents
and prompts use CC BY-NC-SA 4.0. See the repository LICENSE for component scope.
Host subscriptions, model usage, and optional conversion tools are separate.
There is no public demo at present.

- Repository: https://github.com/H-Hur/study-kit
- Releases: https://github.com/H-Hur/study-kit/releases
- Help and feedback: https://github.com/H-Hur/study-kit/issues
- Claude Code package folder: `plugins/study-kit`
- Codex package folder: `plugins/study-kit-codex`
- Codex upload: `dist/study-kit-codex-2.1.1.zip`

## Directory routes

A GitHub release is directly installable through the repository marketplace. It is
not evidence of acceptance into either host's official directory.

- [OpenAI submission portal](https://platform.openai.com/plugins): upload the Codex
  ZIP, resolve automated checks, complete the publisher/listing requirements, and
  submit for review. Follow [the official guide](https://developers.openai.com/plugins/deploy/submission).
- [Claude developer portal](https://claude.ai/directory/manage): submit a plugin
  bundle pointing to the public repository and Claude package folder. The earlier
  submission shortcut now redirects to [directory documentation](https://claude.com/docs/directory/publish).
  The portal requires a paid Claude account and the applicable organization role.

Do not claim approval or a catalog listing until the portal confirms it. Required
publisher declarations and any directory terms must be reviewed by the publisher.

## Reviewer scenarios

These are proposed manual checks, not a claim that end-to-end review has run.
Use a separate scratch study project and synthetic inputs, with no learner records.

| Prompt or condition | Expected behavior |
|---|---|
| Start a new study project without specifying a mode | Ask personal learning versus authoring first |
| Personal learning selected | Ask learner level, without requiring a separate instructor level |
| Teaching materials selected | Ask instructor and learner levels and settle research scope |
| Source citation cannot be verified | Record the gap; do not present it as verified |
| Publish an updated edition | Check numbering/citations and use a new edition directory |
| Three editions skipped grammar review | Recommend a review; do not claim it was performed |
| No converter is available | Return source and report missing output verification |
| A request concerns an unrelated task | Do not force the study workflow |

## Community outreach

Use the README and first-use guide as the current entry points. Delay demo-led
announcements until a working example exists. A directory submission and a
community post are separate actions. Do not generate or post a Hacker News
submission for the publisher: its [guidelines](https://news.ycombinator.com/newsguidelines.html)
exclude generated or AI-edited text. The publisher should write that post personally.

The [skills.sh CLI](https://github.com/vercel-labs/skills) is a separate skill
installation route. This repository contains two host editions with overlapping
skill names; use the documented plugin marketplace route until standalone skill
installation and its shared-file dependencies have been validated.
