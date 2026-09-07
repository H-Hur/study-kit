---
description: Begin a new course of study — from learner intake to standing up the project skeleton
---

Read the [runtime notes](../docs/runtime.md) once per task before following this procedure.


Open a new study project. Follow this order.

1. Read the kit's method (`${CLAUDE_PLUGIN_ROOT}/docs/method.md`) to confirm the whole
   sequence. Kit files are always addressed through `${CLAUDE_PLUGIN_ROOT}` — a bare
   `docs/` here would mean the study project's own `docs/`, which is a different folder.
2. **Ask the learner directly** with the `learner-intake` skill. Do not skip this stage or
   delegate it to an agent. For items the learner already answered in their first message,
   lay out what was understood and ask only for what is missing.
3. Write `docs/learner-profile.md` and get it confirmed by the learner. Mark the boundary as
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
