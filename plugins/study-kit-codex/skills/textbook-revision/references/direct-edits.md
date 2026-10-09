# Reconcile direct edits before making a new edition

Use at session or writing-milestone startup and before publication when editable
artifacts have been delivered or the user supplies an edited file. This is a revision
input route in both modes. Updated 2026-10-09 from issue #4.

## Establish the saved baseline and working copy

Use the exact published baseline recorded in the edition README, including hashes,
source snapshot/revision, and the editable files that were delivered. Keep a preserved
baseline separate from copies the user edits. A hash alone can detect change but cannot
reconstruct what changed. Do not rebuild a baseline and assume conversion reproduces
the same file. If no original remains, preserve the current file, report the missing
baseline, and resolve only changes that can be established from available evidence.

Compare saved files against the baseline; modification times are hints only. A changed
binary hash calls for semantic comparison, not a conclusion that all bytes represent
intentional edits. A copied or synchronized file can have misleading timestamps.
If the latest work is unsaved, request a saved copy or use an available authorized
editor snapshot. Do not treat zero extracted comments as proof that there are none.
Do not close the user's application automatically. Never overwrite a file open for editing.

## Inspect the whole artifact

Preserve the user's saved version before reconciliation. Compare the whole content,
not just the edits the user mentions: paragraphs and order, headings, tables and deleted
columns, figures/captions, references, comments, tracked changes, and relevant formatting.
For supplied slides, include shapes and speaker notes. Align sections or slides by stable
identity/content before comparing positions; deleted pages shift later page numbers.
Do not add slide production to the project solely because a slide file is supplied.

Use format-aware comparison with available tools. Inspect all relevant parts; plain-text
extraction alone misses comments, tracked deletions, and other document structures.
If full inspection is unavailable, state what could not be compared and do not claim a
complete merge. Register each semantic difference in the revision queue with baseline
and edited locations, before/after text or structural change, provenance, and disposition.
Comments are requests to evaluate; they are not automatically approved content changes.

## Reconcile into the authoritative source

Preserve intentional edits and deletions. Do not regenerate removed material from an
older master. If an edit appears mistaken, contradicts a source, or conflicts with a
concurrent master change, record a question and preserve both versions while resolving
it; do not silently accept or revert it. Reuse clear instructions already supplied.

Read the project's source-authority contract. By default, reconcile accepted edits into
`docs/textbook.html` at the publication trigger, or earlier if explicitly requested.
If the user designates Word or another format as the master, record that decision and
use it as the basis of the next edition. Document which HTML-only features or round-trip
conversions are unavailable; do not convert from a stale HTML file because it is the
usual path. A format change alone does not authorize changing the master.

Record each applied edit so retries do not apply it twice. Keep unresolved conflicts
visible and do not publish affected content as verified. Produce the next edition from
the reconciled source under the immutable-directory publication rules; retain the saved
user copy and baseline. Reading and registering edits at startup does not itself trigger
master revision or publication.
