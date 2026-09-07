---
name: source-index
description: The procedure for gathering study sources in four beats — seed collection, lawful acquisition, checking against the original, graded index — and building REFERENCES.md and the references/ store. Use it for requests like "gather the sources", "which papers should I read", or "organize this literature". It covers the quarantine rule for secondary material, when to spend deep research, the two-form storage specification (original plus markdown normalization), and the quantitative verification that catches content lost during conversion.
---

Read the [runtime notes](../../docs/runtime.md) once per task before following this procedure.


# Source collection and the graded index

The artifact of this stage is not a pile of files but **an index whose grades have been
judged.** Quality is not how many sources there are; it is whether it is clear which ones
can be used as a basis and which are only hints.

## The four beats

### ① Seeds — get a map of the field

Without a map of the field you do not even know what to search for. At that point deep
research (an outside LLM consultation, a research agent, following survey papers) gives a
first draft of the terrain. What to ask for: the standard textbooks, the classics counted
as originals, the current directions, and a reading order.

**When to spend it**
- **Once**, at the very front. Once there is a map, switch to targeted search (locating a
  public copy of a particular source, confirming a particular figure against its
  original). Deep research is a map-making tool, not a standing tool.
- There are only two occasions to reinvest — when a new subtopic opens and there is no map
  of that sub-terrain, and when questions the textbook cannot answer pile up in the
  feedback loop (a hole in the textbook is a hole in the map).

### ② Acquire — lawful routes only

Take only public originals (author or institutional copies, preprint servers, libraries).
**Do not circumvent paywalls; record only the route of acquisition in the index.** For
sites that block automated collection (403, bot blocks), record the manual download route
so the learner can fetch it directly when needed.

### ③ Verify — check against the original

Every citation that came from a seed is **secondary information**. Author, year, volume,
and DOI contain plausible things that are wrong. **Compare an acquired source against its
own first page**, correct the citation, and promote it to primary. Mark citations that
could not be compared as "unverified" in the index.

This quarantine rule is the most important thing in the procedure. Without it, unverified
information seeps into the index and the textbook as fact, and afterwards there is no
telling the verified from the guessed.

### ④ Index — list with the grade

Put [`templates/REFERENCES.md`](templates/REFERENCES.md) at the project root and fill it
in one line at a time.

- **Primary** — the original work, a textbook, a specification, library source. Usable as
  the basis for figures, definitions, and conventions.
- **Secondary** — a summary, an LLM digest, a blog post. Use **only as a hint about where
  to look.**

## Two-form storage — the original and the normalization

Keep an acquired source in two forms.

- `references/originals/` — PDFs and the like. **The basis for an equation, a table, or a
  figure is always this side.**
- `references/md/` — the markdown normalization. The working memory an agent can read and
  search at any time without tools.

Always put the **citation, source URL, date acquired, and grade** at the top of the
normalization as a header, along with a note that the extraction is for searching and the
original is the basis. A PDF cannot be read without a dedicated tool and a web page
disappears, so a source is only actually used if a normalization exists.

```bash
# PDF → markdown (layout preserved)
pdftotext -layout original.pdf - > references/md/name.md
```

## Attach quantitative verification to every conversion

**Work that changes format quietly loses content.** Measured, a single regular expression
meant to strip citation markers silently deleted 8.5 KB of body text, and without a length
comparison it would have gone straight into the index.

Always check after converting.

```bash
# size comparison — has it shrunk implausibly against the original
wc -c extracted.txt normalized.md
# sample comparison — does an arbitrary passage of the original survive in the result
grep -c "a distinctive phrase found only in the original" normalized.md
```

If a web page is drawn by script and the body cannot be captured, decode the data embedded
in the page and restore it. Attach the same verification there too.

## Cost — historical observations for planning

The quantities in this section are estimates from the original Claude Code course
using Opus at high reasoning. They are not current limits or Codex benchmarks.
Use the [budget notes](../../docs/budget.md) and host runtime for present-day
chunking, model selection, and delegation.

**① Research costs ten to thirty times its artifact.** The seed list itself is a little
over 10k tokens, but opening and judging dozens of candidate documents to produce it costs
100–350k in that run. **Delegate bounded research to `source-scout` when supported,
and recover only the index lines and the basis for the judgments.** Otherwise run
its procedure directly in batches. At the research stage, look only as far as the
abstract, contents, and citation — reading the full text waits until the source is
actually used.

**② Normalization is effectively free by machine and 25–70k per source by model.**
`pdftotext` drops file to file without passing through the model, so it costs almost no
tokens (measured: 5 papers, 106k tokens of material in total, done this way at zero).
Model transcription — the model reading and rewriting — is for scanned PDFs, documents
with broken tables, and other cases where machine conversion fails, and even then move
**only the passage to be used, not the whole thing.** Before committing, test one source
with `pdftotext` to see which case you are in.

Meanwhile, **do not lower the model for grading sources or checking citations.** The
learner came to study because they do not know the field, and they cannot catch a wrong
citation or a figure that does not match. Cost saved here remains as an error the learner
cannot verify.

## Do not

- Do not put a citation or a figure the LLM produced into the index or the textbook
  without confirming the original.
- Do not circumvent paywalls.
- Do not keep an extraction without its original.
- Do not gather sources and leave them ungraded. An index without grades is not an index.
