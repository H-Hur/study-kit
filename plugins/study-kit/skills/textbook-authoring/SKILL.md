---
name: textbook-authoring
description: The procedure for writing a dual-audience textbook (HTML) from the learner profile and the curriculum, and managing its editions. Use it for requests like "make me a textbook", "write the preview material", or "write the next chapter". It covers the dual-audience technique of isolating fundamentals into groundwork boxes, the standard skeleton of a chapter, the prose style rules, designing interactive figures so they become still frames in print, edition labelling, and the finished textbook template.
---

Read the [runtime notes](../../docs/runtime.md) once per task before following this procedure.


# Textbook authoring — writing for two audiences

The textbook consists of chapters corresponding to the sessions of the curriculum. One
session is one chapter. Before starting, read `docs/learner-profile.md` and
`docs/curriculum.md`. **Subject, boundary, depth, and style all come from those two
documents.**

## The dual-audience convention — the center of this procedure

A textbook fitted to one person alone fills up with sentences that presume that person's
background and becomes a thing that cannot be reused. But writing everything from the
fundamentals makes it padding for the learner. The solution is **isolation**.

- Fundamentals the learner already knows are pulled out of the body into a **"groundwork"
  box** (`aside.basics`). The learner skips it; a first-time reader reads it. The same
  textbook satisfies two audiences.
- Fundamentals that remain after all that gathering go into a **chapter 0, "Preparations"**.
  State explicitly that this chapter may be skipped.
- Write the body as **self-standing prose.** Do not presume a particular learner or the
  internal circumstances of a particular project. Sentences like "this is your specialty so
  it is omitted" or "like that code in our project" close the textbook.

The boundary comes from the profile. When the boundary in the profile is corrected, the
contents of the groundwork boxes move with it.

## The standard skeleton of a chapter

[`templates/textbook-template.html`](templates/textbook-template.html) is the finished
form. One chapter goes in this order.

1. **Head** — the chapter number (which session) and the title.
2. **Opening paragraph** — why this chapter's question became necessary now. Join it to the
   previous chapter in prose.
3. **Sections (h3)** — write section titles as **assertions**, not nouns ("How the same data
   is held decides how fast the answer comes"). Reading only the titles should carry the
   argument.
4. **Groundwork boxes** — wherever needed.
5. **Figures** — see the "Visuals" section below.
6. **Three key sentences** (`.keybox`) — exactly one per chapter. Write them as **complete
   sentences.** Ending on a noun phrase ("the understanding of ~", "the importance of ~")
   makes a table of contents, not a summary.
7. **Review questions** (`details`) — three. Answers go in `.ans`. This collapsing structure
   is itself the principle behind issuing two editions
   ([`textbook-publish`](../textbook-publish/SKILL.md)).

Make the review questions **demand a judgment**, not confirm knowledge. Designing them can
be delegated to the [`drill-designer`](../../agents/drill-designer.md) agent.

## Style

The detailed clauses are in [`references/style-rules.md`](references/style-rules.md). Read
them before writing. The core, transcribed:

- **Write continuous explanation, not lists of words.** Terms and items laid out as bullets
  do not become study material. Work out in sentences why this concept became necessary, how
  it joins what came before, and what it leads to next. Use tables and lists **only to
  summarize what has already been explained.**
- **Do not bury definitions in prose; give the table first.** Where several symbols appear,
  put a definition table ahead of the prose. That gives the learner somewhere to look back to.
- **Equations: results only.** If the depth contract says "as far as the concept," do not put
  in derivations. Give the result in one line, the meaning of the symbols, and the picture
  that equation describes, in prose.
- Do not write translationese. Where a settled term exists in the target language, use it and
  give the original alongside on first appearance.

## Visuals

A figure earns the most when it shows **what moves when you move a handle**. Build
interactive figures with sliders, but hold to the following.

- Use only theme tokens for color (`var(--accent)`, `var(--accent-2)`, `var(--muted)`).
  Hard-coded colors disappear in the dark theme.
- **The controls are hidden in print.** So the figure must be a still frame whose meaning
  carries from the initial state alone. Always call the draw routine once at the end of the
  script to establish that initial state.
- Attach `role="img"` and a description to every figure.

## Imagery and metaphor

An **established image** that runs through the whole textbook — a metaphor whose meaning is
declared at the outset and used with the same meaning to the end — is a teaching device, so
keep it. A **decorative metaphor** used once and dropped should be removed. What separates
them is: is this metaphor used again later, and was its meaning defined somewhere? Applying
the "restrain metaphor" clause mechanically erases the teaching devices too, so make this
distinction first.

## Managing editions

- The textbook carries an **edition label** from the start (`.pill` in the head). Raise it
  with every correction.
- Gather pending revisions in the document belonging to
  [`textbook-revision`](../textbook-revision/SKILL.md), and when issuing a new edition, open
  that document first and fold in every waiting item.
- The master file is fixed at `docs/textbook.html`. Published editions (PDF and so on) derive
  from it.
- Do not delete the revision notice in the footer — it is where the learner learns when and
  how the next edition arrives and where to leave a question, and that is what brings them
  into the loop.

## Writing the whole thing up front versus incrementally

If the time budget is short and the curriculum is settled, **writing the whole thing up front
is better.** The learner can read ahead as preview, questions arrive earlier, and the
revision loop turns that much sooner. Measured, writing the whole textbook up front drew out
eight revision items before the study had even begun.

That said, practice results and review items can only be written after a session, so leave
their place empty in each chapter and fill them in the revised edition after the session.

## After writing

Check for violations of the conventions, the style, and self-standing prose with the
[`textbook-auditor`](../../agents/textbook-auditor.md) agent. Clause-by-clause collation is
more accurate than a person reading it through again.
