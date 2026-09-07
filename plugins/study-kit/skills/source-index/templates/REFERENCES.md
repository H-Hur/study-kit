# Source index

Originals that have been obtained are in `references/`, and markdown normalizations (for
searching) in `references/md/`. For sources not obtained, the citation and the route of
acquisition are recorded instead.

**Always distinguish the grade of a source.**

- **Primary** — the original work, a textbook, a specification, library source. Usable as
  the basis for figures, definitions, and conventions.
- **Secondary** — a summary, an LLM digest, a blog post. Use **only as a hint about where
  to look.**

If the selection of a source came from secondary material, say so, and **check the
citation of anything obtained against the original.** Citations of sources not obtained
need confirmation against the original before they are cited.

---

## Originals obtained (primary — citation checked against the original: {{done/not done}})

| Citation | Original / normalization | What it is good for here |
|---|---|---|
| {{author, "title", source (year), DOI}} | [`original`](references/{{file}}) · [`md`](references/md/{{file}}) | {{when, and for what, it is opened}} |

## Not obtained (citation from a secondary source — check against the original when obtained)

| Citation | Route of acquisition | Why it is needed |
|---|---|---|
| {{citation}} | {{paywalled, library, author's public copy, etc.}} | {{its role}} |

## Textbooks

| Citation | Role |
|---|---|
| {{citation}} | {{main text / reference / optional}} |

## Secondary material kept

| Title | Path | Summary |
|---|---|---|
| {{title}} | {{path}} | {{what it was a seed for}} |

---

## When adding a source

1. Put the public original in `references/` and build a markdown normalization in
   `references/md/`, with the **citation, source URL, date acquired, and grade** at the top.
2. **Always check the citation against the first page of the original.** Mark anything
   from a secondary source as such until it has been verified.
3. Add one line to the relevant table in this file. For sources not obtained, write the
   route and the reason they are needed.
4. Do not circumvent paywalls.
