---
name: textbook-revision
description: The procedure for turning the learner's questions into drafted textbook revisions, stacking them, and folding them into a new edition. Use it whenever the learner asks about the textbook's content or asks something back, and for requests like "explain this part again" or "let's put out a revised edition". It covers tracing a question back to the defect in the textbook, why the actual revised wording is written in advance, the specification of the pending-revisions document, and the procedure for bumping an edition.
---

Read the [runtime notes](../../docs/runtime.md) once per task before following this procedure.


# The revision loop — turning questions back into the textbook

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
the same cause).

Do not skip the attendant corrections. If the misunderstanding came from an unstated
premise, the same premise is usually missing in several places in the textbook.

### 4. Bump the edition

When issuing a new edition, **open the pending-revisions document first** and fold in every
waiting item. Change the status of each reflected item to `reflected (edition N)` and move
it to the reflection history at the end.

- A large item (a full pass over the style, say) may be split across rounds. When splitting,
  say so in the item.
- If the learner designates "just this one first," mark it as partially reflected and leave
  the rest waiting.
- Once the edition is bumped, publish with [`textbook-publish`](../textbook-publish/SKILL.md).

## Other input routes

Questions do not arrive only in conversation. Gather the following into the same document.

- **Exchanges recovered from the secondary track** — questions the learner left in the
  scraps-of-time channel.
- **[`comprehension-auditor`](../../agents/comprehension-auditor.md) reports** — among the
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
