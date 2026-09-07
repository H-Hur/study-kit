---
name: study-review
description: Audit comprehension — find concepts not understood from what was asked back, and build review items
---

Read the [runtime notes](../../docs/codex-runtime.md) once per task before following this procedure.


Call the [`comprehension-auditor`](../comprehension-auditor/SKILL.md) agent to find what the learner asked back about in recent
conversation records, study notes, and material recovered from the secondary track, and take
back a report of the concepts judged not understood along with proposed re-explanations.

When the report arrives, the conductor judges the following.

- Items arising from a defect in the textbook → register them in
  `docs/textbook-revisions.md` **with the revised wording written out.**
- Items where the explanation was right but did not land → put them in the next briefing's
  review list, from a different angle.
- Items where the boundary was wrong (something said to be known was asked back about, or the
  reverse) → correct the boundary in `docs/learner-profile.md` and leave the date and the
  trigger in the record of corrections.

Do not present the audit result to the learner as a report card. The premise of this loop is
that a question back is a defect in the explanation, not a shortfall in the learner.
