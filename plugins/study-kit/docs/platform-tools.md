# Platform checks for conversion and verification

Use these notes before textbook conversion or PDF source extraction, especially on
Windows PowerShell 5.1. They address the environment failures reported in
[issue #9](https://github.com/H-Hur/study-kit/issues/9), with DOCX safeguards from
[issue #6](https://github.com/H-Hur/study-kit/issues/6). Check what is installed;
these are fallback routes, not bundled dependencies or permission to install software.

## Detect before selecting a route

Record the operating system, shell version, Python executable, converter, and renderer
actually available. On PowerShell, use `Get-Command python, py, pandoc, pdftotext, pdfinfo -ErrorAction SilentlyContinue`
and `$PSVersionTable.PSVersion`. Probe Python
imports independently; a working Python does not imply `pymupdf`, `docx`, `lxml`, or
`win32com` is installed. Locate Chrome/Edge only if using the permitted browser workflow;
never reuse a macOS application path on Windows.

| Need | Preferred available route | Fallback and limit |
|---|---|---|
| PDF text and page count | Poppler `pdftotext` / `pdfinfo` | PyMuPDF extraction below; preserve page boundaries and inspect reading order |
| DOCX structure | `python-docx` and XML inspection | Standard-library `zipfile` + `xml.etree.ElementTree`; no layout claim |
| DOCX conversion | Available document tool or Pandoc with a reference DOCX | Keep HTML/draft and report missing converter if neither is available |
| DOCX pagination and rendering | Word or another available layout engine | Structural inspection alone cannot verify layout; mark that check unavailable |

## UTF-8 scripts instead of nested shell strings

Write nontrivial conversion code to a `.py` file through a file-editing tool, then invoke
that file with path arguments. Avoid embedding Python with f-strings, dollar signs,
quotes, or non-ASCII text inside PowerShell command strings or interpolating here-strings.
Use explicit `encoding="utf-8"` for text and `newline="\n"` for generated text files.
Read known UTF-8 BOM inputs with `utf-8-sig` if needed; do not guess encodings silently.

Windows PowerShell 5.1 file cmdlets and redirection have differing encoding defaults.
Do not use `>` or `Out-File` to serialize Unicode artifacts without an explicit encoding.
For `.ps1` source containing non-ASCII text, use UTF-8 with BOM for PowerShell 5.1.
See Microsoft's [encoding reference](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_character_encoding?view=powershell-5.1).
After writing, reopen and compare representative non-ASCII text, symbols, and quotes;
terminal display alone does not establish file integrity.

## PDF extraction when Poppler is absent

If PyMuPDF is installed, save the following as a project helper and run it with input
PDF and a new output text path. It emits one form feed per page, including empty pages,
and verifies that delimiter count against the document's actual page count.

```python
import sys
from pathlib import Path
import pymupdf

source, target = map(Path, sys.argv[1:3])
with pymupdf.open(source) as document:
    pages = [page.get_text("text", sort=True) for page in document]
    if any("\f" in page for page in pages):
        raise ValueError("Embedded form feed: resolve before using it as a page delimiter")
    text = "".join(page + "\f" for page in pages)
    assert text.count("\f") == document.page_count
    with target.open("x", encoding="utf-8", newline="\n") as output:
        output.write(text)
    print("Pages:", document.page_count)
```

PyMuPDF documents [per-page text extraction](https://pymupdf.readthedocs.io/en/latest/recipes-text.html)
and [page counts](https://pymupdf.readthedocs.io/en/latest/document.html). Sorting text does
not recover the semantics of columns, equations, or tables; inspect them against the
original. Scans may need OCR. Empty extracted text is not evidence that a source is empty.
Add the source-index header separately and retain the raw extraction for quantitative
comparison. If neither extractor exists, report the missing dependency rather than
claim normalization or page-count verification.

## DOCX inspection without python-docx or lxml

A DOCX is a ZIP package. Read `word/document.xml` using `zipfile.ZipFile` and parse it
with `xml.etree.ElementTree`; also inspect relationships, media, styles, numbering,
and `word/footnotes.xml` when present. Use namespace-aware queries, including
`http://schemas.openxmlformats.org/wordprocessingml/2006/main` for text/tables and
`http://schemas.openxmlformats.org/officeDocument/2006/math` for equations.
Do not count every media file as a displayed figure or every footnote node as a user
footnote (separator entries exist). Compare actual references and visible content.
These checks establish structure; cached page metadata cannot replace rendering.

## Word COM: bounded execution, owned instance only

Use COM only on Windows with Word and the automation dependency available. Run it in
a separate worker process with a finite timeout controlled by the parent. Create a
separate instance (for example `win32com.client.DispatchEx("Word.Application")`),
not an attachment to the user's active instance. Track the worker's document and the
identity of the Word process it created; if exclusive ownership cannot be established,
do not perform process-level cleanup.

Open a staging copy, repaginate, obtain the layout page count, and export/render for
inspection. Close only the worker's document and quit only its own application instance
in cleanup. On timeout, stop the worker; terminate a Word process only when its identity
and exclusive ownership are proven. Never run a global `taskkill /IM WINWORD.EXE`,
close a user's documents, or overwrite an open file. Record failure and preserve the
draft if cleanup or rendering cannot be completed safely; do not retry indefinitely.

Update — 2026-10-09. These are platform fallbacks and verification safeguards, not new
claims about learning outcomes.
