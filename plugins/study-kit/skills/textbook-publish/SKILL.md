---
name: textbook-publish
description: Publish a textbook as PDF, DOCX, or both, with the requested exercise and answer variants. Use for requests to send a textbook, make a PDF or Word document, or issue a revised edition. Covers the publication trigger, immutable edition folders, conversion, content and layout checks, and authorized delivery.
---

Read the [runtime notes](../../docs/runtime.md) once per task before following this procedure.

Read the recorded project mode and apply the [mode contract](../../docs/project-modes.md).
Authoring adaptations take precedence over learner-only steps below.


# Publishing the textbook — formats, answer variants, and delivery

The default master is `docs/textbook.html`; use the authoritative source recorded
in the project. Before conversion, follow [direct-edit reconciliation](../textbook-revision/references/direct-edits.md)
for delivered working copies. Every edition derives from that reconciled source, and
conversion does not modify it. If another format is authoritative, use a compatible
conversion workflow and record any unsupported HTML features; the HTML examples below
apply only to a current, reconciled HTML source. Revision of the master is governed by
[`textbook-revision`](../textbook-revision/SKILL.md) and the recorded publication trigger.

## Choose the format and answer variants

Use the format already requested or recorded in the project: **PDF, DOCX, or both**.
DOCX-only delivery is valid; a PDF used internally for layout verification need not be
a deliverable. Ask only if the format is unresolved and matters to the task.

Exercise and answer are variants of the same numbered edition. For browser PDF
conversion, review answers collapsed inside `<details>` provide the separation.

- **Exercise variant** — convert a copy with review answers collapsed. Collapsed answers are not printed, so
  only the questions appear. For working through alone in scraps of time.
- **Answer variant** — expand the `<details>` in a copy, then convert. The answers appear too.
  For checking in a focused sitting.

Honor explicitly requested variants. Otherwise, if the learner has only one kind of
time, issue only the appropriate variant; use the "scraps of time" item in the profile
as the basis for that judgment.

## Reserve an edition before conversion

Confirm the project publication trigger is met; an explicit request to publish counts.
Reuse standing authorization within its scope. Reserve a new directory such as
`output/3_20261009_213000/` (edition identifier and local `YYYYMMDD_hhmmss`). Record
its timezone/UTC offset in `README.md`. Create it exclusively: if it already exists,
choose a fresh timestamp; never reuse it silently. Until checks pass, its README
must say **draft / unpublished**. Conversion intermediates live in a separate staging
folder, and source-relative assets must remain resolvable in every staged copy.

After verification, mark it published. Published directories are immutable. Corrections
normally make a new edition. An explicit replacement request is the only exception:
first compare the target with the originally published copy or recorded hashes to check
for user edits. If that cannot be established, preserve it and use a new directory or
resolve the conflict with the user. Never overwrite an open Word file.

Use the [edition README template](templates/edition-README.md) to record scope,
changes, source snapshot/revision, artifact hashes, tools, and verification. Preserve
the exact publication baseline separately from editable working copies, and record
both paths. A hash detects changes but cannot replace the original for comparison.
Keep the
edition label and date there and in the directory name, out of the textbook body,
appendices, and footer. Give delivered files edition-qualified names if detached from
the folder, so an attachment cannot silently replace an earlier edition.

## PDF procedure

Use an available host workflow that preserves answer separation and verifies layout.
On Windows, or without Poppler, read the [platform notes](../../docs/platform-tools.md).
The following is a POSIX example, not a Windows command. Locate the actual browser
and obey the host's tool policy; this package supplies no converter.

Prepare `exercise.html` and `answer.html` in staging using an HTML parser. In review
question `details` elements, remove the `open` attribute for exercise and add it for
answer. Handle attributes and nesting; literal substitution of `<details>` alone misses
`<details class="...">`. Keep question text in both. Preserve relative assets by copying
them with their relative layout or resolving their URLs against the original source.
Inspect the resulting pages before printing. Do not rely on a `file://` query toggle.

```bash
# Set CHROME to a discovered executable; STAGE to the prepared copies;
# OUT to the newly reserved edition directory (absolute paths for both).
"$CHROME" --headless=new --disable-gpu --no-pdf-header-footer \
  --virtual-time-budget=4000 \
  --print-to-pdf="$OUT/textbook-drill.pdf" "file://$STAGE/exercise.html"
"$CHROME" --headless=new --disable-gpu --no-pdf-header-footer \
  --virtual-time-budget=4000 \
  --print-to-pdf="$OUT/textbook.pdf" "file://$STAGE/answer.html"

pdfinfo "$OUT/textbook.pdf" | grep '^Pages'
pdftotext "$OUT/textbook-drill.pdf" "$STAGE/exercise.txt"
pdftotext "$OUT/textbook.pdf" "$STAGE/answer.txt"
# Choose a real answer-only phrase: exercise must yield 0 matches, answer at least 1.
grep -F -c -- '<answer-only phrase>' "$STAGE/exercise.txt"
grep -F -c -- '<answer-only phrase>' "$STAGE/answer.txt"
```

`--virtual-time-budget` allows scripts to draw interactive figures; also inspect their
printed still frames. Use absolute output paths and properly encoded file URLs when
paths contain special characters. Check page counts for every produced variant, render
and inspect pages for clipping or lost content, and compare figures, equations, tables,
citations, and footnotes against the master. A single answer phrase is a smoke check:
verify all answer blocks are absent/present as intended and all questions survive.

## DOCX procedure

For DOCX or mixed output, read [Word conversion and verification](references/docx.md).
Collapsed HTML is not a reliable DOCX answer filter. Remove answer content explicitly
from the exercise copy; include it explicitly in the answer copy before conversion.
Perform the same separation and content checks as for PDF, plus actual Word layout
verification where available. Keep unverified artifacts marked draft and state exactly
which checks could not be run. If a required converter is unavailable, return the
available source/draft and name the missing dependency; do not claim publication.

## Measured traps

1. **Collapsed `<details>` does not print its content.** Exploiting that property is what
   makes two editions possible; not knowing it leaves the answer edition without answers.
   Always convert the answer variant from the expanded copy. Every time you publish,
   **confirm answer separation as described above** — a substitution can fail
   silently and the file sizes still come out similar, so the eye will not catch it.
2. **Splitting editions by a JS branch on the `file://` URL query is unreliable.** The branch
   is sometimes not applied at the moment of headless conversion. Using a prepared copy
   is the certain way.
3. **Choose the page-count tool with care.** macOS `mdls` depends on the Spotlight index and
   returns `(null)` for paths that are not indexed (temporary folders and the like) —
   measured, it came back empty even inside the project folder. The page count reported by
   `file(1)` reads the declared value in the page tree and can be wrong. **Prefer `pdfinfo`
   (Poppler), or PyMuPDF's document page count when Poppler is unavailable.** Text
   page separators are a cross-check only when extraction preserves one per page;
   see the platform notes.
4. **The sending tool may restrict which folders it can read.** Messenger integrations
   sometimes refuse to attach files outside a designated working folder. Copy the files into
   the permitted folder before sending.

## Delivery

Return files in the current conversation by default. External delivery requires
the learner's authorization and an available tool, as described in the runtime
notes. A preferred channel in the curriculum does not itself grant sending access.

The channel was settled at the planning stage (`docs/curriculum.md`). If it has not been
settled, do the channel test in
[`curriculum-design`](../curriculum-design/SKILL.md) first — **does it open without a
login, does it open directly on the learner's device, is it readable offline.**

A channel that attaches the file directly (a messenger document attachment, say) is the most
robust. A link drops out the moment it demands authentication.

```bash
# Sending through a messenger CLI (tool and target are configured to the installation)
cp "$OUT/textbook-drill.pdf" "$SEND_DIR/textbook-${EDITION}-drill.pdf"
"$SEND_CLI" message send --channel "$CHANNEL" --target "$TARGET" \
  --media "$SEND_DIR/textbook-${EDITION}-drill.pdf" --force-document \
  -m "[exercise edition] {{one line on what was updated}}"
```

**Never leave the values of target identifiers or tokens on screen, in logs, or in
documents.** Inject them as environment variables, and do not read or print a configuration
file wholesale.

If the delivery channel has a resident agent, register the path of the latest published
edition so it can resend on the learner's request. Re-verify the registration with a
confirming question — trusting the "registered" reply alone means missing a silent failure.

## Required checks and optional language editing

Before marking an edition published, complete the
[numbering and citation checks](references/numbering-and-citations.md) on the final
source and delivered outputs. Run them for every updated edition regardless of the
language-editing schedule. Recheck affected targets after late changes.

Grammar/English polishing is optional unless requested or scheduled. Follow the
[editing policy](../textbook-authoring/references/language-editing.md): track consecutive
published editions without a full pass and recommend one when the prospective count
reaches three or more. Do not turn that recommendation into automatic editing or a
publication blocker. Record the count only after successful publication.

## After publishing

- Record the date, edition directory, formats, verification, and actual delivery result
  in the work log. Mark queued revisions reflected only after publication checks pass.
  A failed external delivery is recorded separately from successful local publication.
- Keeping a web edition alongside preserves the interactive figures. But a web edition that
  requires authentication stays **secondary** and is never made the main channel.
