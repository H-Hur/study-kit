---
description: Revise and publish the textbook, and send it to the learner
---

Read the [runtime notes](../docs/runtime.md) once per task before following this procedure.

Read the recorded project mode and apply the [mode contract](../docs/project-modes.md).
Authoring adaptations take precedence over learner-only steps below.


1. Check the recorded publication trigger and existing user authorization. This explicit
   publish request can satisfy the trigger; do not ask for redundant approval.
   Check saved working copies against the preserved publication baseline using
   [direct-edit reconciliation](../skills/textbook-revision/references/direct-edits.md).
   **Open `docs/textbook-revisions.md` first.** Fold in waiting items within scope;
   do not reapply items already recorded as applied but unpublished. If a large item
   must be split, tell the learner and settle the scope of this edition.
2. Amend the reconciled authoritative source (by default `docs/textbook.html`) under
   the conventions of the `textbook-authoring` skill and
   assign the next edition identifier to a fresh output directory and its README,
   without adding an edition label to the textbook body.
3. Run the recorded [language-editing pass](../skills/textbook-authoring/references/language-editing.md)
   only when requested or scheduled, after content fixes: first use
   `writing-clearly-and-concisely`, then give the resulting manuscript to the
   user-selected `proofreader` for American English grammar. Run these sequentially.
   If the candidate edition
   would be the third or later consecutive edition without a full pass, recommend one;
   this does not block publication or authorize running it. Verify factual rewrites.
   Check document conventions and figures with the `textbook-auditor` agent; a full
   grammar/English rewrite is not part of the mandatory audit. Fold the findings
   into this edition or return them to the pending list.
4. Use the `textbook-publish` skill to produce the selected formats (PDF, DOCX, or both)
   and exercise/answer variants. Verify content separation and rendered layout, record
   page counts and checks in the edition README. Always complete the
   [numbering and citation checks](../skills/textbook-publish/references/numbering-and-citations.md)
   before marking the directory published. Record the updated skipped-editing count
   once for the successful edition, not once per output file.
   Do not declare publication complete when required checks remain unavailable.
5. Return the files in the current conversation by default. Send them externally only
   when the learner has authorized that delivery and a suitable tool is available.
   Otherwise state that they have not been sent. Do not expose target identifiers or tokens.
6. Change the status of each reflected item to `reflected (edition N)`, move it to the
   reflection history, and record the publication in `docs/worklog.md`.
