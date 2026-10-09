# Renumber references without changing them twice

Use when figures, tables, or their order change. Updated 2026-10-09 from issue #8.

Build a mapping from each original target identity to its final number before editing
references. Keep figure and table namespaces separate. Prefer stable element IDs and
structured cross-references. Otherwise identify reference spans in the original text
and replace them once; do not rescan generated replacement numbers as old references.
If a tool requires multiple passes, first use unique protected placeholders whose
absence in the source has been checked, then replace those with final labels.

Replacing ranges before single references is not sufficient: a later pass may match
the newly numbered range. Resolve ranges against the original targets. A deletion or
reordering may make a range non-contiguous, reverse its order, or remove a target;
rebuild the reference from the intended surviving targets or flag it for resolution.
Do not guess a replacement for a deleted target, or replace unrelated numbers globally.

After final numbering, check the surrounding grammar, including particles whose form
depends on the pronunciation of the new number. Diff and read every changed caption
and reference. Verify unique numbering, existing targets, intended range membership,
and no leftover placeholders. Include colliding mappings such as 12→13 and 13→14 in
verification, mixed single/range references, deleted targets, and reordered figures.
