---
name: textbook-authoring
description: The procedure for writing a dual-audience textbook (HTML) from the learner profile and the curriculum, and managing its editions. Use it for requests like "make me a textbook", "write the preview material", or "write the next chapter". It covers the dual-audience technique of isolating fundamentals into groundwork boxes, the standard skeleton of a chapter, the prose style rules, designing interactive figures so they become still frames in print, edition records, and the finished textbook template.
---

Read the [runtime notes](../../docs/codex-runtime.md) once per task before following this procedure.

Read the recorded project mode and apply the [mode contract](../../docs/project-modes.md).
Authoring adaptations take precedence over learner-only steps below.


# Textbook authoring — writing for two audiences

In learning mode, chapters correspond to curriculum sessions: one session is one
chapter. In authoring mode, chapters follow the agreed reader-oriented content plan;
a personal study-session schedule is not required. Before starting, read `docs/learner-profile.md` and
`docs/curriculum.md`. **Subject, boundary, depth, and style all come from those two
documents.**

## The dual-audience convention — the center of this procedure

A textbook fitted to one person alone fills up with sentences that presume that person's
background and becomes a thing that cannot be reused. But writing everything from the
fundamentals makes it padding for the learner. The solution is **isolation**.

- Fundamentals the learner already knows are pulled out of the body into a **"groundwork"
  box** (`aside.basics`). The learner skips it; a first-time reader reads it. The same
  textbook satisfies two audiences.
- Fundamentals that remain after all that gathering go into a **preparatory chapter, "Preparations"**.
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
3. **Sections (h3, then h4)** — use concise title phrases and hierarchical numbers
   such as `1.`, `1.1.`, `1.1.1.`, with one space before the title. Keep document
   numbering separate from session numbering; do not use sentence-form headings.
4. **Groundwork boxes** — wherever needed.
5. **Figures** — see the "Visuals" section below.
6. **Three key sentences** (`.keybox`) — exactly one per chapter. Write them as **complete
   sentences.** Ending on a noun phrase ("the understanding of ~", "the importance of ~")
   makes a table of contents, not a summary.
7. **Review questions** (`details`) — three. Answers go in `.ans`. This collapsing structure
   supports exercise and answer variants for PDF; DOCX uses explicit content filtering
   ([`textbook-publish`](../textbook-publish/SKILL.md)).

Make the review questions **demand a judgment**, not confirm knowledge. Designing them can
be delegated to the [`drill-designer`](../drill-designer/SKILL.md) agent.

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

## Terminology sources

For technical terminology, usage, and customary expressions, consult the original
source collection's textbooks and professional institutions' handbooks/guidebooks
first. Follow the [terminology rules](references/style-rules.md), record source
locations and selected conventions in the project glossary/style guide, and use them
consistently. General language editing must preserve those disciplinary conventions.

## Document layout

Apply the heading, caption, spacing, and table-label rules in
[style rules](references/style-rules.md). Put figure numbers/captions below figures,
table numbers/captions above tables, and one body-text line of space between the
complete object/caption block and surrounding prose. Prefix header cells `(A) `,
`(B) `, etc.; prefix first-column data cells `(1) `, `(2) `, etc., excluding the
header row. Keep labels as real text and verify the converted output.
Number standalone display equations only, with `(1)`, `(2)`, etc. at the far right
of the equation row. Inline mathematics remains unnumbered.

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

- Keep edition identifiers and publication dates in the edition directory name and
  README, not in the textbook body or footer. A correction becomes a new edition
  at the recorded publication trigger, not at every conversational question.
- Gather pending revisions in the document belonging to
  [`textbook-revision`](../textbook-revision/SKILL.md), and when issuing a new edition, open
  that document first and fold in every waiting item.
- The default master is `docs/textbook.html`. Published editions derive from the
  reconciled authoritative source recorded in the project; see Source authority below.
- Keep a stable feedback notice in the footer: where to leave a question and how to
  obtain updates. Put edition-specific coverage and changes in the edition README.
- Follow the immutable output directory and selected-format rules in
  [`textbook-publish`](../textbook-publish/SKILL.md).

## Writing the whole thing up front versus incrementally

If the time budget is short and the curriculum is settled, **writing the whole thing up front
is better.** The learner can read ahead as preview, questions arrive earlier, and the
revision loop turns that much sooner. Measured, writing the whole textbook up front drew out
eight revision items before the study had even begun.

That said, practice results and review items can only be written after a session, so leave
their place empty in each chapter and fill them in the revised edition after the session.

## Source authority and editorial checks

HTML at `docs/textbook.html` is the default master. Before using an existing project,
read its source-authority contract and reconcile user edits through
[direct-edit reconciliation](../textbook-revision/references/direct-edits.md). If the
user has designated another format as authoritative, work from it and record the
limits of HTML conversion instead of overwriting it from a stale HTML copy.

Follow the [claim verification rules](../../docs/evidence-verification.md) when
writing or rewriting factual sentences. Use [safe renumbering](../textbook-revision/references/renumbering.md)
when target numbers or order change.

## After writing

Run the project's [language-editing policy](references/language-editing.md) when due:
content corrections first, prose editing next, textbook audit last. Recheck factual
rewrites and any content changes made after this pass.


Check for violations of the conventions, the style, and self-standing prose with the
[`textbook-auditor`](../textbook-auditor/SKILL.md) agent. Clause-by-clause collation is
more accurate than a person reading it through again.
