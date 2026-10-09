---
description: Prepare the next session — review the questions received, the briefing, the scaffolding
argument-hint: "[session number]"
---

Read the [runtime notes](../docs/runtime.md) once per task before following this procedure.

Read the recorded project mode and apply the [mode contract](../docs/project-modes.md).
Authoring adaptations take precedence over learner-only steps below.


Before either mode's preparation, check delivered working copies using
[direct-edit reconciliation](../skills/textbook-revision/references/direct-edits.md).
Register changes without automatically applying the queue or publishing.

In authoring mode, prepare the next agreed writing/review milestone from the content
plan and revision queue. Report pending editorial decisions and prepared material;
skip the learner-specific sequence below unless a taught session is actually in scope.

This is the preparation the conductor does between sessions. Finish all of it here, so that
the session time goes only to understanding and diagnosis.

1. If anything has been recovered into `docs/inbox/`, read it first and move handled files to
   the archive.
2. Run the `comprehension-auditor` agent to find concepts not understood from what was asked
   back. Move items in the report worth reflecting in the textbook into
   `docs/textbook-revisions.md`.
3. Confirm from `docs/curriculum.md` what should be doable when this session ends.
4. Prepare the concept briefing — include the review items from the audit report **from a
   different angle than before.** Repeating the same explanation is not review.
5. Prepare the practice scaffolding and any slow computations in advance.
6. If there is no diagnostic drill yet, build one with the `drill-designer` agent.
7. Check that the drill's criterion — what the answer must name to count as correct — is
   written down **before** the session. Carry it over from `docs/curriculum.md` if it is
   there; write it now if it is not. Never after the answer has been heard.

When preparation is done, report in one paragraph what was prepared.
