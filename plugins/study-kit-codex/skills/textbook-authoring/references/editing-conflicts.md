# Remember recurring terminology-editing conflicts

Updated 2026-10-09. Use in both project modes and for both the Strunk style pass and
the selected grammar agent. Keep actual disciplinary examples in the study project,
not in the reusable kit or a global plugin cache.

## Project record

Create `docs/editing-conflicts.md` from the [template](../templates/editing-conflicts.md)
at project setup, or on the first editing pass in an existing project. It contains a
compact index of confirmed exceptions and an evidence/occurrence log. The main session
owns this record; editing agents report proposed entries rather than concurrently
rewriting it. Use the document language for example text and the project's recorded
report language for explanations.

Record a conflict when a style or grammar suggestion would replace a technical term,
remove a meaningful distinction, or contradict the expression convention supported
by the collected textbooks or professional-institution handbooks/guidebooks. Capture
the original wording, suggested wording, context, editor identity/version if available,
and source edition/page/section. Check the actual source before confirming an exception;
frequency of suggestion or rejection is not evidence of correctness.

## Resolve once, reuse within scope

Use statuses **pending**, **confirmed**, and **retired**. A pending case needs source
checking or a decision; it must not become an automatic exemption. Confirm a narrow
rule when the source and context establish it, reusing the user's existing terminology
choices. Ask only when ambiguity or conflicting conventions require a user decision.
Leave doubtful substitutions unapplied and retain the original pending resolution;
that does not certify the original as correct.

A confirmed entry records the preferred form, the rejected transformation, why it is
wrong here, and exactly where the exception applies. Include a counterexample or
exclusion showing where ordinary grammar/style correction is still appropriate.
For example, do not protect every occurrence of a word when only its use inside one
technical phrase has a special meaning. Preserve surrounding grammar corrections.
Do not put the whole source sentence on a global 'never edit' list.

Merge repeated occurrences into the same entry only when the expression, meaning,
source convention, and scope match. Give each observation a key formed from editing
pass ID, manuscript location, editor, and proposed transformation. Do not count a
retry or the same report copied between files twice. Two distinct observed occurrences
may be marked recurring for prioritization; recurrence does not itself confirm a rule.
Keep separate entries for different meanings. Record first/last seen and counts from
the occurrence log; never invent historical counts.

## Supply both editors before they act

Before the style pass, read the record and give `writing-clearly-and-concisely` the
confirmed entries relevant to the manuscript, with their source evidence and scope.
Pending cases are warnings to examine, not accepted rules. Ask it to cite an entry ID
when retaining an expression and to report any proposed exception conflict.

Review the style output, integrate accepted changes, and update confirmed findings in
the record. Then pass the updated relevant entries and the style-edited manuscript to
the selected grammar agent. A delegated agent must receive accessible paths or actual
excerpts; do not assume it saw the main session's context. If a tool cannot accept these
instructions, review its suggestions manually against the record before applying them.
Do not claim automatic enforcement by an external editor.

Review each editor's report/diff for recurrence of rejected transformations. Keep the
source-supported expression when the confirmed scope applies, while allowing unrelated
corrections. Log genuinely new occurrences and unresolved conflicts. Do not repeatedly
ask the user to decide an already resolved case unless the context or evidence changes.

## Keep exceptions current

At final audit, compare affected technical expressions against the confirmed entries
and report any regression by entry ID. If a definition, source edition, terminology
choice, or relevant context changes, revalidate affected entries; mark obsolete ones
retired and retain their history and replacement ID. An exception is not permanent
proof that every future use is correct. Tool updates should retain the project record
and reload it, not erase it or patch managed caches.

Record new/recurring cases and unresolved items in the editing report or edition README.
This ledger review is not a full grammar pass and does not reset the skipped-editing
counter. It runs with authorized editing/review work and does not schedule extra passes.
