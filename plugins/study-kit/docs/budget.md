# Estimating the work and judging the budget

This document decides, before a piece of work starts, whether to do it now, split it, or
schedule it. Read it before any large piece of work — writing a textbook, a round of deep
research, normalizing a batch of sources.

The figures below are historical estimates from one Claude Code course using Opus
at high reasoning. They describe that run, not a current model benchmark, price,
context capacity, or output limit in either host. The six stages are in
[the method](method.md). Read the [runtime notes](runtime.md) for the active host
before applying these notes.

## The premise — this work is done with a high-capability model

**The learner came to study because they do not know the field.** They cannot catch a
wrong citation, a number that does not match, or the point at which an explanation
started to go astray. Cost saved here becomes an error the learner cannot verify, the
error stays in the textbook, and the textbook becomes the learner's understanding.

So **judging sources, setting the boundary, writing the textbook, and drafting revisions
use the quality-focused model guidance in the [runtime notes](runtime.md).**
The only things a lower model may take on are
things that never needed the model's judgment: mechanical conversion, file tidying,
format checking. When delegating to a subagent, do not lower the model for the judging
and writing work either. **The purpose of delegation is not to cut cost but to spare the
conductor's context.**

All the estimates below come from the original Claude Code course (Opus, high
reasoning). They remain attributed to that environment in both editions.

## Historical cost accounting — three paths in the original run

- **Reading** — the cost of bringing files, search results, and web documents into
  context. Once in, it is re-sent every turn for the rest of the session.
- **Writing** — the cost of producing the artifact. Roughly the size of the artifact.
- **Reasoning** — at high reasoning, each judgment adds **2–8k per turn**. So the number
  of turns is itself a cost. If several files must be read, read them in one batch; do
  not split confirmation questions across several exchanges.

## Measured sizes (from the artifacts of one prior course of study · Korean documents)

| Work | Artifact size | Estimated tokens |
|---|---|---|
| **One round of deep research (mapping a field)** | 10 KB out | **100–350k** ↓see below |
| Acquiring one source (search, download, citation check) | — | 5–15k |
| Normalizing one source — **mechanical conversion** (pdftotext) | 37–100 KB | **0–1k** ↓see below |
| Normalizing one source — **model transcription** | 37–100 KB | **25–70k** |
| **Reading** one normalized source | 37–100 KB | 10–27k |
| Writing the source index | 6 KB | 2k |
| Writing the learner profile | 2–3 KB | 1–2k |
| Standing up the project skeleton (filling 4 templates) | 15 KB | 6–8k |
| Writing the study plan | 7 KB | 4k |
| **Writing one textbook chapter** | 8 KB | **3–4k** (+ 2–8k reasoning) |
| **Writing the whole textbook (12 chapters)** | 82 KB | **35k** (+ 30–90k reasoning) |
| Reading the whole textbook (before revision or audit) | 82 KB | 35k |
| Pending-revisions document (8 items, with drafted text) | 14 KB | 8k |
| Reading the whole kit (its own documents) | 57 KB | 30k |

Estimates assume 1.1 Korean characters per token and 3.7 characters per token for code
and ASCII. They are for a sense of magnitude, not precise values.

## Deep research — estimating from the artifact size will be badly wrong

In the prior course of study, deep research produced an **artifact of 10.8k tokens** (a
candidate list of 5 books and 13 papers, with a reading order). But producing that 10k
costs **ten to thirty times** as much. Research is work you read and throw away.

Broken out, one round looks like this.

| Component | Rounds | Per round | Subtotal |
|---|---|---|---|
| Search queries and result lists | 6–12 | 1–2k | 10–20k |
| Opening candidate documents (abstract, contents, citation) | 10–20 | 3–15k | **40–200k** |
| Judging and comparing (high reasoning) | 15–25 turns | 2–8k | **40–150k** |
| Drafting the index and the reading order | — | — | 5–10k |

The dominant items are **opening candidates** and **judgment reasoning**. So hold to the
following.

- **Do deep research once, at the very front.** Once there is a map, switch to targeted
  search. Reinvest only when a new subtopic opens, and when questions the textbook cannot
  answer pile up in one place.
- **Delegate bounded research when the host supports it.** Keep noisy acquisition
  work out of the main conversation by handing it to `source-scout` and recovering
  the index lines and the basis for each judgment. Follow the runtime notes for
  dispatch and result collection. When delegation is unavailable, perform that
  procedure directly in manageable batches.
- **Do not read full texts.** What the research stage needs is "what does this source
  answer," not its content. Look only as far as the abstract, contents, and citation.
  Reading the full text waits until the source is actually used.
- Using an outside LLM consultation as seeds can push much of this cost outside. But the
  result is **entirely secondary material**, so the cost of checking against the
  originals (5–15k per source) attaches instead.

## Transcription — always separate mechanical conversion from model transcription

Normalized storage means putting sources into markdown, and **who does the putting
splits the cost between zero and tens of thousands of tokens.**

- **Mechanical conversion** — `pdftotext -layout` and the like drop file to file without
  passing through the model. The model never reads the content, so **it costs almost no
  tokens.** In the prior course of study, 5 papers totalling **106k tokens of normalized
  text were produced this way at effectively zero.**
- **Model transcription** — the model reads the original and writes it out again. Both
  reading and writing attach, so it is **25–70k per source.** Use it only when mechanical
  conversion does not work: scanned PDFs, documents whose tables are badly broken, web
  pages drawn by script.

So the principle of normalization is one line. **Let the machine move what a machine can
move; the model attaches the header and verifies a sample.**

```bash
pdftotext -layout original.pdf - > references/md/name.md   # the model does not read it
wc -c references/md/name.md                               # compare size (a few hundred tokens)
grep -c "<a distinctive phrase found only in the original>" references/md/name.md   # sample check
```

Do not skip the verification. **Work that changes format quietly loses content** — in the
prior course of study a single regular expression silently deleted 8.5 KB of body text,
and without a size comparison it would have gone straight into the index. The
verification itself costs a few hundred tokens.

If mechanical conversion fails and model transcription is unavoidable, **do not move the
whole thing; move only the passage you will use.** Transcribing an entire source is done
only after deciding to make it a basis for the textbook.

## Rules for current work

1. Use limits actually reported by the current host. Context capacity, per-response
   output limits, account allowance, and a user-specified task budget are different
   quantities. Do not infer any of them by subtracting historical file sizes.
2. Keep each writing unit bounded and save it to the study project. A chapter or
   section is a useful unit; use the actual host limits when choosing its size.
   An unknown token budget alone is not a reason to stop authorized work. Continue
   in saved, manageable units until the agreed scope is complete or a real limit
   requires a pause; record the next action if that happens.
3. Use scripts for mechanical conversion, then verify the result. Delegate bounded
   research and audits according to the runtime notes when supported. Keep profile
   decisions and integration of findings in the main conversation.
4. Batch independent reads and avoid replaying unnecessary source text. Observe the
   host's actual context and compaction behavior rather than assuming every earlier
   file remains in full in every turn or incurs the same cost.
5. Use background execution only when supported and collect its completion result.
   Schedule a future run only when requested by the learner and supported by the
   host. Otherwise leave the next action in the work log. Never claim that a future
   run exists without a confirming tool result.

## Historical operating rules — preserved for context

The following is an archival quotation of the original run's rules and rationale.
It preserves the 8k, three-times, and 150k thresholds and their examples so the
original decisions remain understandable. These are not instructions or fixed
limits for a new Claude Code or Codex session. Use the current-work rules above.

> ## How to check the remaining budget
>
> If the session reports remaining budget, use that figure. If there is no such display,
> **estimate from what has been read in so far** — reading this whole folder is 30k, the
> whole textbook is 35k, and those are re-sent every turn until the session ends. After
> reading a large file, treat the budget as reduced by that much and re-measure the size of
> the next piece of work.
>
> If the remaining budget is unknown, **do not start a large piece of work.** Building only
> the skeleton and pushing the rest to the next round is always better than leaving a
> textbook cut off halfway.
>
> ## Rules of judgment
>
> **① Keep the artifact written in one response under 8k tokens.** Do not try to write the
> whole textbook at once. Split by chapter (3–4k) and each chapter fits in one response;
> if it is cut off partway, the earlier chapters survive.
>
> **② Do not start unless the remaining budget is at least three times the expected spend.**
> If it breaks off mid-build, everything read up to that point is thrown away. The factor
> of three is because reading, editing, and verification during the work, plus per-turn
> reasoning at high effort, add about twice the expectation.
>
> - Writing the whole textbook (35k + reasoning) → attempt it in one session only with
>   **150k or more** left.
> - Deep research (100–350k) → **the conductor does not do this directly.** Delegated, the
>   conductor's side drops to around 10k (instructing and recovering).
> - Normalizing 5 sources → under 5k with mechanical conversion, over 150k with model
>   transcription. **The point where the judgment splits is whether mechanical conversion
>   works.** Test one with `pdftotext` before committing.
>
> **③ Always delegate work that is heavy on reading.** A normalized source is 10–27k each,
> so reading five directly ends the session by itself. `source-scout`, `textbook-auditor`,
> and `comprehension-auditor` read and **return only the conclusion**. Do not lower the
> model when delegating.
>
> **④ Cut the number of turns.** At high reasoning, reasoning attaches to every turn, so
> read several files in one batch and send independent pieces of work out together. Batch
> confirmation questions too, rather than splitting them item by item.
>
> **⑤ Schedule work that must cross sessions.**
> - Long calculations and conversions — run them in the background and take only the result.
> - Regularly repeating work (periodic comprehension audits, sending material at a set
>   time) — put it on a schedule.
> - Large writing that cannot finish today for want of budget — do **only the skeleton and
>   the first chapter** today and name the rest explicitly in the work log for the next
>   round.
>
> **⑥ Decide first what will be left behind.** When the budget is tight, leave **files**
> rather than conversation. Conversation disappears when the session ends; files remain.
> Writing the actual revised wording into the pending-revisions document matters more the
> smaller the budget is — the next round then ends in assembly alone.

## The one-line check before starting

> What bounded artifact comes next → what limits does this host actually report →
> can a script handle the mechanical part → is delegation available and useful →
> where will the result and any unfinished next action be saved?

Runtime portability update — 2026-09-06: historical measurements are retained;
current execution follows host capabilities. This is a packaging adaptation, not
newly measured learning guidance.
