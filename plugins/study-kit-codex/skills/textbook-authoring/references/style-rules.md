# Textbook style rules

The clauses used in common by authoring, revision, and auditing. Where the "preferred style
of explanation" in the learner profile conflicts with a clause here, **the profile wins.**
What is here is the default when the profile says nothing.

The clauses below were written for a Korean-language textbook. For another language, clauses
1, 2, 6, 7, and 8 apply as written, while 3, 4, and 5 are rewritten to suit that language's
grammar.

## 1. Write in prose (the most frequently broken clause)

Terms and items laid out as bullets are a summary, not study material. Work out in sentences
why the concept became necessary, how it joins what came before, and what it leads to next.

- Use tables and lists **only to summarize what has already been explained.**
- If a section consists of two lists, that section has not been written yet.

## 2. Title-style headings and hierarchical numbering

Use concise title phrases, not full-sentence assertions, for document and section
headings: "Data structures" or "Performance comparison", not "How the same data is
held decides how fast the answer comes". This changes headings, not the requirement
for explanatory body prose or the chapter's three complete key sentences.

Number content headings by hierarchy: `1. Title`, `1.1. Subtitle`,
`1.1.1. Subsection`, `1.1.2. Subsection`, `1.2. Subtitle`, `1.2.1. Subsection`.
Use a trailing period and one space before the title. Restart subordinate counters
under each parent; do not skip a parent level. The document's cover title is unnumbered.
Heading numbers express document structure; record session numbers separately rather
than forcing preparatory material or front matter to have chapter number zero.

## Document layout rules (2026-10-09)

Apply these rules to HTML, PDF, DOCX, and other document outputs. Preserve them through
conversion; do not assume HTML CSS alone determines the final Word layout.

- **Figure number and caption below the figure.** Keep the number and caption together
  and associated with their figure, including across page breaks.
- **Table number and caption above the table.** In HTML, put `caption` before `colgroup`
  and row groups; in Word, place the caption paragraph before the table and keep it
  with the first table row.
- **One body-text line of space** between surrounding prose and each figure/table
  block, including its caption, on both sides where adjacent prose exists. Apply this
  outside the complete block, not between its caption and object. Use paragraph/block
  spacing equal to the configured body line height; avoid accumulated blank paragraphs
  or doubled spacing. Check the rendered result, especially at page boundaries.
- **Column labels in the header row**: prefix the existing header text left to right
  with `(A) `, `(B) `, `(C) `, continuing `(Z) `, `(AA) ` if needed.
- **Row labels in the leftmost cells**: prefix existing first-column content with
  `(1) `, `(2) `, `(3) ` starting at the second physical row (the first data row).
  Exclude the header row from row numbering. Do not add a separate index column by
  default. After every closing parenthesis, write exactly one ordinary space before
  the cell text. Restart row and column labels in each table; repeated headers on
  later pages retain their column labels and do not advance row numbering.

For merged or multirow headers, normalize to a single clearly labeled header row when
that preserves meaning. If it does not, determine the logical row/column mapping and
record the necessary exception rather than silently duplicating labels or changing
meaning. Row-spanning data cells need a layout that gives every data row its own label.
Materialize labels as text so export cannot lose CSS-generated numbering. Avoid duplicate
prefixes when editing an already numbered table. Structural edits require rechecking
all row/column labels and references to them.

Example (the caption appears above this table):

Table 1. Comparison

| (A) Item | (B) Description | (C) Result |
|---|---|---|
| (1) First item | Description | Result |
| (2) Second item | Description | Result |

## 3. Do not write translationese

Use the word order and vocabulary of the target language rather than carrying English
sentence structure across. Where a settled native term exists for a technical word, use it
and **give the original alongside on first appearance.** Keep the original word as-is only
for terms that have no settled translation.

Signs of translationese to watch for, in any language: passive constructions where the actor
is known, nominalized verbs where a verb would do, "it is possible to X" for "X can", and
chains of prepositional phrases that a single clause would carry.

### Technical terminology and disciplinary usage

When writing the textbook, first consult the original source material's textbooks
and handbooks/guidebooks issued by professional institutions for technical terms,
their meanings, customary phrasing, and usage conventions. Prefer relevant passages
in those originals over general dictionaries, generic prose advice, or model recall.
Use sources appropriate to the subject, intended audience, document language, and
edition; do not assume a newer or similarly named source uses the same convention.

Record selected terms, definitions, customary expressions, and source locations in
the project glossary or style guide. Apply them consistently in headings, body text,
figures, tables, and captions. If authoritative sources differ, record the distinction
and choose the convention that fits the subject and reader context; do not silently
merge different meanings. If the preferred sources are unavailable, use another
verified primary source and identify the unresolved convention rather than invent it.

A project-specific terminology decision takes precedence when explicitly given. Flag
conflicts with source usage for resolution. Generic grammar/style suggestions must not
replace an established technical expression merely because an everyday alternative
sounds simpler. This priority concerns terminology and expression conventions; factual
claims still require their own appropriate source verification.

## 4. Do not let punctuation stand in for sentences

Dashes and parentheses are places for an aside, not for joining logic. Several dashes in one
paragraph mean sentences have been left unfinished. Convert as follows.

- A dash that unpacks what precedes it → a comma, or a new sentence
- A dash that joins a reason → "because", "so"
- A dash that contrasts → "whereas", "but"
- A dash carrying an aside → parentheses, or deletion

## 5. Endings and address

- Keep the body of the textbook in one register. Where addressing the learner (guidance,
  review questions) mixes with exposition, settle on one side.
- Do not address the learner specifically ("as a professor, you...", "you, an expert in X,
  ..."). This is the most common route to breaking self-standing prose.

## 6. Metaphor — separate established imagery from decoration

- **Established imagery**: a metaphor whose meaning is declared at the outset and repeated
  with the same meaning throughout the textbook. It is a teaching device that makes a concept
  graspable, so **keep it.**
- **Decorative metaphor**: rhetoric used once and dropped. Figures drawn from death, war, and
  money in particular blur the concept and only make the sentence loud. **Remove them.**

There is one test: is this metaphor used again later, and was its meaning defined somewhere?

## 7. Equations and symbols

- Number standalone display equations only. Inline mathematics within a sentence or
  paragraph has no equation number. Number displays in document order `(1)`, `(2)`,
  etc., independently of headings, figures, and tables, unless the project specifies
  another sequence. Put the parenthesized number at the far right of the display's
  text area, on the same equation row, not immediately after the formula or on a
  separate line. Keep it with its equation across page breaks.
- Keep numbers as real text or native fields, not CSS-only generated content. Check
  alignment and reference targets after conversion, insertion, or deletion. A multiline
  display treated as one equation receives one number; distinct displayed equations
  receive their own numbers. Explain symbols in the following prose, outside the
  equation row, so commentary does not displace the right-aligned number.


- If the depth contract says "as far as the concept," **do not put in derivations.** Give the
  result in one line, the meaning of the symbols, and the picture the equation describes, in
  prose.
- Where three or more symbols appear, **put the definition table first** and the prose after.
  A definition buried in a sentence cannot be looked back to.
- When using a figure, say where the value came from. If it can be checked, give the check
  alongside.

## 8. Self-standing prose (the dual-audience convention)

The textbook must hold for a reader who reads only the textbook.

- Do not presume a particular learner's background ("this is your specialty so it is
  omitted").
- Do not presume the files, tools, or circumstances of a particular project. Where necessary,
  rewrite with a generic name.
- Do not use for the first time, without explanation, a term not yet explained in another
  chapter. A term appearing for the first time is unpacked in the body or sent to a groundwork
  box or a glossary.

## How to check

Clause-by-clause collation is more accurate than a person reading it through. Count what can
be counted first.

```bash
grep -o '—' textbook.html | wc -l              # dash frequency (clause 4)
grep -c '<li>' textbook.html                   # signs of list overuse (clause 1)
sed -n '/<main>/,$p' textbook.html | grep -o '#[0-9A-Fa-f]\{6\}' | wc -l   # hard-coded color in the body
```

Clauses that counting cannot catch (1, 2, 6, 8) go to the
[`textbook-auditor`](../../textbook-auditor/SKILL.md) agent.

## Applying a language-editing pass

Use the project's recorded [editing policy](language-editing.md). Apply content fixes
before prose editing, then audit. The project guide and terminology govern suggestions;
check adjacent tables and captions for definitions. Do not strengthen factual claims
or discard qualifications to make sentences smoother. Recheck rewritten claims against
their sources, including unchanged claims in those sentences.
