---
description: Begin a new course of study — from learner intake to standing up the project skeleton
---

Read the [runtime notes](../docs/runtime.md) once per task before following this procedure.

Read the recorded project mode and apply the [mode contract](../docs/project-modes.md).
Authoring adaptations take precedence over learner-only steps below.


Open a new study project. Follow this order.

1. Read the kit's method (`${CLAUDE_PLUGIN_ROOT}/docs/method.md`) to confirm the whole
   sequence. Kit files are always addressed through `${CLAUDE_PLUGIN_ROOT}` — a bare
   `docs/` here would mean the study project's own `docs/`, which is a different folder.
2. First ask whether this is personal learning or teaching material for other learners.
   In learning mode ask only the learner's level. In authoring mode ask both instructor
   and learner levels, then choose support within the instructor's knowledge or a
   bounded researched extension, following the mode contract. **Ask directly** with the `learner-intake` skill. Do not skip this stage or
   delegate it to an agent. For items the learner already answered in their first message,
   lay out what was understood and ask only for what is missing.
3. Write `docs/learner-profile.md` (the intended reader profile in authoring mode) and
   get it confirmed by the requester. Mark the boundary as
   a **hypothesis**.
4. Stand up the project skeleton — take `PROJECT-CLAUDE.md`, `worklog.md`, and
   `toolbox-log.md` from `${CLAUDE_PLUGIN_ROOT}/templates/`, fill them in, and create
   `docs/notes/` and `docs/reports/` (these two in the study project, not in the kit).
5. If sources are needed, build the index with the `source-index` skill and the
   `source-scout` agent.
6. Lay out the plan with the `curriculum-design` skill, and for items that need a decision,
   **spell out the options** and have the learner settle them.

If a subject was given as an argument, use it as the starting point for "what do you want to
learn" in ②, but ask the other four items regardless. Do not build a plan from a subject alone.

When filling the project instructions, carry over any conversation/document language
split from the profile. Set the publication trigger once from existing authorization;
if unspecified, use explicit publication requests as the default. Record the requested
output formats (including DOCX only), answer variants, and page setup under environment
and delivery decisions. Ask only for decisions needed for the requested output.

During the existing style discussion, settle and record the
[language-editing policy](../skills/textbook-authoring/references/language-editing.md).
Ask the user to choose njjenkins's `proofreader` or Daniel Rosehill's `proofreader`
for grammar, presenting the GitHub links and differences in the editing-tool reference.
Record the owner, source URL, and American English (en-US); reuse a prior explicit
choice. Recommend Strunk-based `writing-clearly-and-concisely` for sentence style
and verify availability before use.
If that style skill is absent, recommend installation from
[obra/the-elements-of-style](https://github.com/obra/the-elements-of-style), following
the recorded recommendation in the editing-tool reference. Do not install automatically.
Reuse the user's timing. If unset,
use on-request editing with a recommendation after three consecutive editions without
a full pass. Record the initial editing history; do not invent a past pass or count.

The [editing-tool reference](../skills/textbook-authoring/references/editing-tools.md)
records the selected pairing and alternatives. Offer alternatives only if requested;
do not replace a missing named tool silently or claim it is installed.

When installation/configuration of the selected editing tools is authorized, apply the
[terminology-precedence contract](../skills/textbook-authoring/references/editing-tools.md#installation-and-configuration-terminology-precedence)
to both the style skill and grammar agent. Save it in project instructions, with the
collected textbook and professional-institution guidebook/handbook references, and
verify the tools receive it. If collection is pending, record and complete that setup
when the terminology references become available.

Create `docs/editing-conflicts.md` from the
[editing-conflict template](../skills/textbook-authoring/templates/editing-conflicts.md)
in the study project, preserving an existing record. It starts without confirmed
exceptions; populate it only from observed, source-checked editing conflicts. Wire it
into both editing roles using the [procedure](../skills/textbook-authoring/references/editing-conflicts.md).
