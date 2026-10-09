---
name: textbook-revision
description: The procedure for turning the learner's questions into drafted textbook revisions, stacking them, and folding them into a new edition. Use it whenever the learner asks about the textbook's content or asks something back, and for requests like "explain this part again" or "let's put out a revised edition". It covers tracing a question back to the defect in the textbook, why the actual revised wording is written in advance, the specification of the pending-revisions document, and the procedure for bumping an edition.
---

Read the [runtime notes](../../docs/codex-runtime.md) once per task before following this procedure.

Read the recorded project mode and apply the [mode contract](../../docs/project-modes.md).
Authoring adaptations take precedence over learner-only steps below.


# The revision loop — turning questions back into the textbook

In authoring mode, treat requester questions and corrections as editorial input. Use
the same trace-back and queue process, without diagnosing the author's understanding.
The learner-evidence interpretation below applies to learning mode.

## A question back is not a shortfall in the learner but a defect in the textbook

If the learner asks something back, the earlier explanation did not reach them. Stop at
answering the question and that signal disappears, and the same misunderstanding is
reproduced for the next reader unchanged.

So whenever a question arrives, do two things. **Answer, and trace back.**

## Procedure

### 1. Answer — at the depth of conversation

An answer in conversation is not bound by the textbook's depth contract. If the learner
asks for the equation, answer with the equation. The textbook and the conversation have
different readers.

### 2. Trace back — "which sentence in the textbook produced this misunderstanding"

This is the core labor of the loop. Do not transcribe the question; find the place in the
textbook that produced the misunderstanding. It is usually one of the following.

- **An unstated premise** — it was never said which reference, coordinate system, unit, or
  condition the statement holds under. This is the most common cause.
- **A term used without definition** — a word appearing for the first time was used without
  explanation.
- **A compressed expression** — two steps were folded into one sentence and the middle
  vanished.
- **One word, two meanings** — a term the field uses for two different things was not
  disambiguated.

If nothing is found, classify it as "content that was never in the textbook at all." That
is a defect too.

### 3. Register it with the revised wording written out

Create an item in `docs/textbook-revisions.md`. **Write out the sentence that will actually
go into the textbook.** With the wording written, the revision work ends in assembly alone;
write only "reflect later" and the item is either rewritten from scratch at revision time
or quietly disappears.

What goes into one item: the date registered and its status, the trigger (a quotation of
the learner's own words), where it is to be reflected, the substance of the answer, **a
draft of the revised wording**, and the attendant corrections (other places arising from
the same cause), and the source or reasoning supporting the correction. Link a
verified source and location for factual changes; record uncertainty when unresolved.
Apply the [claim verification rules](../../docs/evidence-verification.md) to every
claim in a rewritten factual sentence, including unchanged claims.
Register first: a question or correction alone does not authorize changing the master
or publishing it. An explicit request to edit the master can override this queue default.

Do not skip the attendant corrections. If the misunderstanding came from an unstated
premise, the same premise is usually missing in several places in the textbook.

### 4. Reconcile direct edits, then bump the edition

Before applying the queue, follow [direct-edit reconciliation](references/direct-edits.md)
for any delivered working copies or user-edited artifacts. Register the full semantic
changes, preserve user deletions, and reconcile with the recorded authoritative source.
Do not regenerate from an older master over the user's saved work. If figures or tables
are inserted, deleted, or reordered, use [safe renumbering](references/renumbering.md);
range-first replacements alone do not prevent double changes.


Read the publication trigger in the project instructions. Reuse the user's existing
authorization; do not ask again within an authorized standing trigger. If none exists,
default to an explicit request to publish and record that policy once. Before the
trigger is met, keep revised wording in the queue.

When the trigger is met, **open the pending-revisions document first** and fold in every
waiting item within the authorized scope. Record which items were applied to the master.
Only after the requested artifacts pass publication checks, change their status to
`reflected (edition N)` and move them to the reflection history. A failed conversion
leaves the edition unpublished and the items applied-but-unpublished, not reflected;
a retry must not apply their changes a second time.

- A large item (a full pass over the style, say) may be split across rounds. When splitting,
  say so in the item.
- If the learner designates "just this one first," mark it as partially reflected and leave
  the rest waiting.
- Once the edition is bumped, publish with [`textbook-publish`](../textbook-publish/SKILL.md).

## Other input routes

Questions do not arrive only in conversation. Gather the following into the same document.

- **Direct edits, comments, and tracked changes in delivered files** — use
  [direct-edit reconciliation](references/direct-edits.md), including whole-content
  comparison and the authoritative-source decision.

- **Exchanges recovered from the secondary track** — questions the learner left in the
  scraps-of-time channel.
- **[`comprehension-auditor`](../comprehension-auditor/SKILL.md) reports** — among the
  concepts mechanically identified as not grasped from the conversation record, those worth
  reflecting in the textbook.
- **Errors in the textbook exposed during practice** — where a figure or an explanation in
  the textbook differed from reality.
- **Improvements the author promised** — anything said to be "strengthened in the next
  edition."

## Do not

- Do not answer a question and move on. The moment you have answered is the best moment to
  trace back.
- Do not write a waiting item as a summary. Without the wording, it has not been registered.
- Do not paraphrase the learner's utterance instead of quoting it. The basis for revisiting
  the judgment later disappears.
