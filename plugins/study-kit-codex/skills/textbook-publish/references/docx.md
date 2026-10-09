# Word output from the HTML master

Read this when DOCX is selected, including DOCX-only delivery. These safeguards respond
to the failures reported in [issue #6](https://github.com/H-Hur/study-kit/issues/6);
they are conversion checks, not a claim that every converter version has those defects.

## Prepare and convert

1. Use the recorded page setup. Prepare a project `reference.docx` with explicit page
   size, margins, and styles for body, headings, captions, tables, and footnotes. If A4
   was requested, set A4 explicitly; do not accept a default Letter page. Specify fonts
   in the styles rather than relying on the current Word theme. Pandoc uses styles and
   document properties from its [reference document](https://pandoc.org/MANUAL.html#option--reference-doc).
2. Prepare separate HTML copies with an HTML parser. For exercise, remove `.ans` and
   other answer-only content while retaining each question; for answer, include the
   answer blocks in normal flow. Do not trust collapsed `details` to hide DOCX content.
3. Materialize essential CSS-generated content (labels, numbers, spacing) as real text.
   Put a table's `caption` before `colgroup` and row groups. In the reported workflow,
   the reverse order lost a table: count tables and inspect their content after conversion.
4. Preserve original SVGs. If the target Word/converter combination loses them, render
   PNG fallback copies at adequate resolution, point only staged HTML to them, and
   check labels and sharpness in the result. Preserve relative image paths.
5. Preserve verbatim quotation characters. Check `pandoc --list-extensions=html` for
   the installed reader; disable `smart` only if supported/enabled, and also check any
   intermediate Markdown reader. Do not apply an unsupported reader option. Compare
   quoted passages with the source after conversion.

With prepared copies and a validated reference document, an example is:

```text
pandoc staging/answer.docx-source.html --from=html --to=docx --reference-doc=reference.docx --output=output/EDITION_TIMESTAMP/textbook.docx
pandoc staging/exercise.docx-source.html --from=html --to=docx --reference-doc=reference.docx --output=output/EDITION_TIMESTAMP/textbook-drill.docx
```

Replace the illustrative paths with the reserved unpublished edition folder. Run with
asset paths resolved from the original master. Select only the variants requested.
Never overwrite a document open in Word; write a new draft path and retain the open file.

## Preserve document editing rules

Apply the shared [style rules](../../textbook-authoring/references/style-rules.md).
Use title phrases and a coherent heading hierarchy (`1.`, `1.1.`, `1.1.1.`).
Map content hierarchy to Word heading styles. Choose either native multilevel numbering
or materialized number text; never combine both and produce duplicate numbers. If the
HTML cover title is removed during conversion, account for its level when mapping headings.

Place figure caption paragraphs below images; keep the image paragraph with its caption.
Place table captions above tables and keep them with the table's first row. Set spacing
before and after the complete object/caption block to one configured body-text line.
Do not put that blank-line gap between the caption and the object, or rely on empty
paragraphs that accumulate on repeated conversion. Check Word layout for orphaned captions.

Prefix header cell text `(A) `, `(B) `, etc., and first-column data cell text `(1) `,
`(2) `, etc. Start row numbering at physical row two and exclude the header. Preserve
exactly one ordinary space after `)`. Keep these prefixes as actual text through
conversion; repeated header rows retain column labels. Check all tables, including
glossaries and symbol definitions, for missing, duplicated, or shifted labels.

For equations, leave inline mathematics unnumbered. Put `(1)`, `(2)`, etc. at the
far right of each standalone display equation row, using native equation/paragraph
alignment or another layout that survives conversion. Avoid padding with spaces.
If a borderless layout table is necessary, treat it as equation layout, not a data
table: do not add a table caption or row/column labels. Keep equation numbers as
text or native fields and verify they remain beside their equations in rendered
Word/PDF output, without wrapping, clipping, or separation at a page break.

## Verify the delivered document

Compare the master with each DOCX: questions and answers, equations (including symbols),
figures, tables, citations, quotations, and footnotes. Record expected and observed
counts plus discrepancies; a count alone does not prove preservation. Inspect representative
content and every element that changed representation. Render all pages using Word or
an available compatible layout engine and inspect page breaks, clipping, font substitution,
figure placement, table splits, and footnote layout. Record the renderer: a substitute
renderer does not prove identical layout in the recipient's Word version.

Obtain page count from actual layout, not cached `docProps/app.xml` metadata. ZIP/XML
inspection can establish structural presence but cannot verify pagination or visual layout.
If no renderer is available, state that limitation and return a draft rather than claim
layout verification. An internal PDF render may support these checks without adding PDF
to the requested deliverables.

On Windows, use the [platform notes](../../../docs/platform-tools.md) for missing Python
libraries and safe Word COM execution. A hanging COM call must not lead to killing all
Word processes or closing a user's open documents.
