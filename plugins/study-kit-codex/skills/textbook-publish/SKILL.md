---
name: textbook-publish
description: The procedure for turning the textbook HTML into two PDF editions, exercise and answer, and sending them to the learner's channel. Use it for requests like "send me the textbook", "make it a PDF", or "ship the revised edition". It covers the two-edition principle that exploits collapsed answers, the headless Chrome conversion commands, page-count verification, and four measured traps including the one where collapsed content vanishes in print.
---

Read the [runtime notes](../../docs/codex-runtime.md) once per task before following this procedure.


# Publishing the textbook — making two editions and sending them

The master is a single file, `docs/textbook.html`. Every published edition derives from it,
and the master is not modified.

## The principle of two editions

It uses, as is, the property that the review questions are collapsed inside `<details>`.

- **Exercise edition** — convert the master unchanged. Collapsed answers are not printed, so
  only the questions appear. For working through alone in scraps of time.
- **Answer edition** — expand the `<details>` in a copy, then convert. The answers appear too.
  For checking in a focused sitting.

If the learner has only one kind of time, issue only one edition. The "scraps of time" item
in the profile is the basis for that judgment.

## Procedure

Use the available host PDF workflow when it can preserve both editions and verify
answer separation. The following commands are a local example; locate the actual
executables and obey the host's browser/tool policy before using them. This package
supplies no browser or converter. If conversion is unavailable, return the HTML
master and identify the missing dependency without claiming PDF publication.

```bash
SRC=docs/textbook.html
TMP="$(mktemp -d)"
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"   # adjust to the install path

# ① Exercise edition — answers hidden (master unchanged)
"$CHROME" --headless=new --disable-gpu --no-pdf-header-footer \
  --virtual-time-budget=4000 \
  --print-to-pdf="$PWD/docs/textbook-drill.pdf" "file://$PWD/$SRC"

# ② Answer edition — answers expanded (substituted in a copy)
sed 's/<details>/<details open>/g' "$SRC" > "$TMP/print.html"
"$CHROME" --headless=new --disable-gpu --no-pdf-header-footer \
  --virtual-time-budget=4000 \
  --print-to-pdf="$PWD/docs/textbook.pdf" "file://$TMP/print.html"

# ③ Page-count verification
pdfinfo docs/textbook.pdf | grep '^Pages'                    # this one if poppler is available
pdftotext docs/textbook.pdf - | grep -c $'\f'                # otherwise count the page separators

# ④ Confirm the two editions actually differ — an answer-only phrase must be absent from
#    the exercise edition and present in the answer edition
pdftotext docs/textbook-drill.pdf - | grep -c '<a phrase that appears only in an answer>'   # must be 0
pdftotext docs/textbook.pdf       - | grep -c '<a phrase that appears only in an answer>'   # must be 1 or more
```

`--virtual-time-budget` gives scripts time to draw the figures. Include it whenever there
are interactive figures. Give the output path as an **absolute path**.

## Measured traps

1. **Collapsed `<details>` does not print its content.** Exploiting that property is what
   makes two editions possible; not knowing it leaves the answer edition without answers.
   Always convert the answer edition from the substituted copy. Every time you publish,
   **confirm with ④ above that the two editions actually differ** — a substitution can fail
   silently and the file sizes still come out similar, so the eye will not catch it.
2. **Splitting editions by a JS branch on the `file://` URL query is unreliable.** The branch
   is sometimes not applied at the moment of headless conversion. Using a substituted copy
   is the certain way.
3. **Choose the page-count tool with care.** macOS `mdls` depends on the Spotlight index and
   returns `(null)` for paths that are not indexed (temporary folders and the like) —
   measured, it came back empty even inside the project folder. The page count reported by
   `file(1)` reads the declared value in the page tree and can be wrong. **Prefer `pdfinfo`
   (poppler); if it is unavailable, count page separators with `pdftotext`.**
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
cp docs/textbook.pdf docs/textbook-drill.pdf "$SEND_DIR/"
"$SEND_CLI" message send --channel "$CHANNEL" --target "$TARGET" \
  --media "$SEND_DIR/textbook-drill.pdf" --force-document \
  -m "[exercise edition] {{one line on what was updated}}"
```

**Never leave the values of target identifiers or tokens on screen, in logs, or in
documents.** Inject them as environment variables, and do not read or print a configuration
file wholesale.

If the delivery channel has a resident agent, register the path of the latest published
edition so it can resend on the learner's request. Re-verify the registration with a
confirming question — trusting the "registered" reply alone means missing a silent failure.

## After publishing

- Record the date, the edition, and the recipient in the work log.
- Keeping a web edition alongside preserves the interactive figures. But a web edition that
  requires authentication stays **secondary** and is never made the main channel.
