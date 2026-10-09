# Review of feedback issues 4, 7, 8, and 10

Reviewed — 2026-10-09. The user approved implementation of all four revised proposals. They are now
incorporated in the current 2.1.0 release. The rationale below records why
the implementation differs from some issue wording.

## #4 — Direct edits to published files

[Issue](https://github.com/H-Hur/study-kit/issues/4). Recommend adoption with a stronger
baseline and explicit source authority. This is particularly important after DOCX output
and authoring mode: the current HTML-master rule and a user's edited Word file can diverge.

Modification time is a useful hint, not the test of whether content changed. Copying,
syncing, or saving can change timestamps without content changes, or preserve timestamps
despite changed content. Compare a saved working copy against the exact published
baseline and recorded hash from the edition directory. Do not rebuild the baseline as
if conversion were guaranteed to reproduce an identical file. Preserve the user's file
before reconciliation; a changed binary hash triggers semantic inspection, not a claim
that every change was intentional text editing.

Diff the whole document, including paragraph order, tables, removed content, comments,
and tracked changes. Include speaker notes and shape content when a supplied slide
artifact is in scope; this does not require adding a slide-authoring feature. Align
sections/slides by identity or content before interpreting positional references, since
insertions and deletions shift them. If only an incomplete extraction is possible, state
that limit rather than claim a full reconciliation. Read a saved snapshot; unsaved or
unavailable comments are not evidence that no comments exist. Closing the editor is
needed when safe access cannot otherwise be established, not a reason to close user work.

Preserve intentional edits and deletions. Flag doubtful changes or source contradictions
for resolution; do not silently restore deleted material or silently accept a suspected
error. Record every semantic change with its location, provenance, and disposition.
Use existing user instructions to decide the authoritative source. If Word remains a
working copy, reconcile into the HTML master before conversion. If the user designates
Word as authoritative, explicitly record that change and the limitations of any HTML
round-trip. Do not unconditionally switch masters merely because one artifact was edited.
Publish a new edition from the reconciled authoritative source.

Touch points: revision inputs, session/milestone startup, pre-publication checks, edition
README baseline, project source-authority contract. Verify with reordered paragraphs,
a deleted column, an unreported edit, and unchanged or misleading timestamps.

## #7 — Source evidence versus tool summaries and calculations

[Issue](https://github.com/H-Hur/study-kit/issues/7). Recommend adoption with revised
wording. The report establishes failures in the tools used in those projects; it does
not establish that all web-fetch tools return model summaries, or that a quotation in a
summary is necessarily faithful.

Distinguish an original page/PDF, extracted text, and a generated summary. Check critical
numbers, dates, equations, and institutional attribution against the original passage,
with a page/section and preserved source where available. A citation's first page can
verify bibliographic identity; it cannot verify a claim elsewhere in the work. If source
access is unavailable, mark the claim unverified rather than promote a summary or quote.
When rewriting a factual sentence, check its retained claims as well as the edited words
and keep any qualifying assumptions and uncertainty.

Separate sourced facts from explicitly derived results. A calculation can establish a
mathematical result under stated assumptions, test units, reproduce a number, or check
transcription. It cannot independently establish that an empirical input or reported
measurement is true. Retain the auditor's computational figure checks, but name what
those checks do and do not establish. Do not replace the current wording with a blanket
ban on calculations as evidence.

Touch points: source-index verification, source-scout, textbook-auditor, and revision
basis. Verify with a correct derivation using an unsupported input, a summary whose
quote differs from the original, and an unchanged false claim inside a rewritten sentence.

## #8 — Renumbering figures, tables, and references

[Issue](https://github.com/H-Hur/study-kit/issues/8). Adopt the problem report, replace
the proposed algorithm. Range-first followed by single-number replacement can still
match already changed text; replacement order alone does not prevent double shifting.

Build a mapping from original figure/table identity to final number. Resolve references
against the original text and write replacements once, using structured reference IDs
where available or a single pass over original spans. If a tool requires multiple
passes, use protected unique placeholders so generated numbers cannot match later
rules. Treat ranges as references to original targets, not merely two numeric endpoints:
a deletion or reorder can require splitting a range or reporting a missing target.
Keep figure and table namespaces distinct. Do not replace unrelated numbers globally.

After numbering is final, adjust number-dependent particles and surrounding grammar for
the document language. Diff and read every changed caption/reference; verify all targets
exist, numbering is unique, and ranges still refer to the intended items. Test colliding
mappings (12→13 and 13→14), mixed single/range references, deleted targets, reordered
items, and language-dependent particles.

Touch points: revision trap note and cross-reference verification during audit. No new
plugin or standalone agent is needed for this bounded procedure.

## #10 — Language-editing pass at project start

[Issue](https://github.com/H-Hur/study-kit/issues/10). Recommend an optional project
editing policy, not a mandatory dependency or automatic plugin installation. Build on
the existing style preference question and reuse any chosen editor or skill. If none is
available, the main agent can perform a focused prose pass with the project style guide.

Record document language, intended readers, style guide, selected tool if any, and timing
(final draft before publication, every draft, or on request). For an unset policy,
recommend a final-draft pass after content corrections and before the textbook audit;
do not reopen that decision every edition. A request for natural prose does not
justify changing technical meaning, removing necessary detail, or expanding claims.

Project-specific style and terminology take priority over generic editing advice.
Check adjacent definitions, tables, and captions before accepting an "undefined term"
finding. Verify non-grammar suggestions against the manuscript and sources. Any change
to a factual sentence receives the claim-level check proposed in #7, including retained
qualifications. Changes requested after final editing receive a proportionate content
and prose recheck, not an automatic whole-book rewrite.

Touch points: existing intake style item, project template, authoring style rules, and
publication ordering. Verify with a term defined in a nearby table and an edit that
turns a qualified claim into an absolute one.

## Suggested implementation order

First #4 (protect user edits and establish the authoritative manuscript), then #7
(evidence rules shared with editing), #8 (safe reference updates), and #10 (editing
policy using those safeguards). None requires a new product plugin or duplicated
production workflow. These four procedures are implemented in the shared source and generated Codex package.


## Implemented procedure locations

- #4: [direct edits](../plugins/study-kit/skills/textbook-revision/references/direct-edits.md),
  linked from startup of sessions/milestones and publication, with baseline/source fields.
- #7: [claim verification](../plugins/study-kit/docs/evidence-verification.md), linked
  from source indexing, scouting, authoring, revision, editing, and audit.
- #8: [safe renumbering](../plugins/study-kit/skills/textbook-revision/references/renumbering.md),
  linked from revision, authoring, and audit.
- #10: [language editing](../plugins/study-kit/skills/textbook-authoring/references/language-editing.md),
  selected during the existing style discussion and placed before publication audit.

Validation checks packaging and link integrity. This update defines agent procedures;
it does not claim a live Word merge or behavioral execution of every listed scenario.
