---
name: study-start
description: Begin a new course of study — from learner intake to standing up the project skeleton
---

Read the [runtime notes](../../docs/codex-runtime.md) once per task before following this procedure.


Open a new study project. Follow this order.

1. Read the kit's [method](../../docs/method.md) to confirm the whole sequence.
   Resolve this link from this installed skill. Choose a separate study project
   before writing any learner artifacts; never write them into the kit or its cache.
2. **Ask the learner directly** with the [`learner-intake`](../learner-intake/SKILL.md) skill. Do not skip this stage or
   delegate it to an agent. For items the learner already answered in their first message,
   lay out what was understood and ask only for what is missing.
3. Write `docs/learner-profile.md` and get it confirmed by the learner. Mark the boundary as
   a **hypothesis**.
4. Stand up the project skeleton from the bundled
   [project instructions](../../templates/PROJECT-AGENTS.md),
   [work log](../../templates/worklog.md),
   [toolbox log](../../templates/toolbox-log.md), and
   [inbox README](../../templates/inbox-README.md). Fill them in as `AGENTS.md`,
   `docs/worklog.md`, `docs/toolbox-log.md`, and `docs/inbox/README.md` in the
   study project. Copy the [style rules](../textbook-authoring/references/style-rules.md)
   to `docs/study-kit-style-rules.md`. Create `docs/notes/` and `docs/reports/` there.
5. If sources are needed, build the index with the [`source-index`](../source-index/SKILL.md) skill and the
   [`source-scout`](../source-scout/SKILL.md) agent.
6. Lay out the plan with the [`curriculum-design`](../curriculum-design/SKILL.md) skill, and for items that need a decision,
   **spell out the options** and have the learner settle them.

If a subject was given as an argument, use it as the starting point for "what do you want to
learn" in ②, but ask the other four items regardless. Do not build a plan from a subject alone.
