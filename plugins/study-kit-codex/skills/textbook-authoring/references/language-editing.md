# A recorded language-editing policy

Updated 2026-10-09 from issue #10. Apply in both learning and authoring modes, using
the document language and intended readers; keep surrounding conversation in its
recorded language.

## Selected grammar and style roles

Let the user choose **njjenkins's `proofreader` or Daniel Rosehill's `proofreader`**
for English grammar checking; present the [candidate definitions and differences](editing-tools.md).
Do not preselect one. Record the owner, exact source URL, availability, and
**American English (en-US)** in project instructions. Reuse that selection on later
passes. Sentence style uses the recommended Strunk-based
**`writing-clearly-and-concisely` skill from The Elements of Style**.
Keep grammar and style scopes and execution results separate. Do not substitute
another editor without the user's choice.

Give the selected grammar agent the manuscript, intended reader level, terminology references,
project style guide, en-US setting, and scope of the requested pass. Ask for grammar, spelling,
punctuation, and usage findings with locations and proposed corrections. Keep it from
silently changing technical meaning or the authoritative manuscript: collect a report
from njjenkins, or give Daniel Rosehill a separate working copy and review its diff.
The main session integrates accepted corrections under the recorded publication trigger.
Preserve quotation spellings, proper names, official titles, and technical conventions. Resolve the actual installed agent and follow the
active host's delegation rules; a named role alone does not establish availability.

Recommend installing the Strunk-based `writing-clearly-and-concisely` skill from
[obra/the-elements-of-style](https://github.com/obra/the-elements-of-style) if it is
absent; installation remains a separate user choice. Use the installed skill for
sentence clarity, concision, and composition.
Follow its guidance subject to project-specific terminology, required explanations,
heading/caption/numbering rules, and the learner's depth contract. Retain necessary
qualifications rather than mechanically shortening every sentence.

Check availability before a requested pass. If the named agent or skill is missing,
report exactly which dependency is unavailable and do not claim it ran, silently
replace it, or invent its instructions. The [tool reference](editing-tools.md) provides
the upstream links for both grammar candidates and Elements of Style. These are optional
external dependencies, not bundled Study Kit agents or skills. Ordinary authoring and
mandatory numbering/citation checks can continue while a missing editing pass is
recorded as incomplete.

At project start, reuse these roles and record the project style guide, terminology,
intended readers, and timing: on request or an explicitly agreed schedule. Grammar and
English polishing are not mandatory at every edition. If timing is unset, use on-request
editing with the three-skipped-edition recommendation below. Naming these tools does
not authorize installing them or running a full pass on every edition.

Aim for accurate, natural, readable prose at the readers' level. Project-specific style
and terminology take priority over generic advice. Preserve established teaching imagery,
necessary detail, equations, quotations, and the agreed depth. Check definitions in
nearby prose, tables, captions, and earlier sections before accepting an "undefined term"
suggestion. Inspect each proposed change rather than trusting a proofreader's report.

The standard correction order is **content corrections →
`writing-clearly-and-concisely` sentence-style pass → user-selected `proofreader`
grammar pass (American English) → final audit**. Finish and integrate the style pass
before giving its resulting manuscript to the grammar agent. Do not run the two
passes in parallel or proofread the pre-style draft. Respect an explicit request
limited to one pass; otherwise use this sequence when language correction is authorized. If grammar fixes change sentence style, recheck the affected passages
without restarting an unlimited whole-manuscript loop. Verify
non-grammar suggestions against the manuscript and sources. Recheck every claim in a
rewritten factual sentence, including retained claims and qualifications, using the
[claim verification rules](../../../docs/evidence-verification.md). A smoother sentence
must not strengthen a claim beyond its source or erase its assumptions. Preserve the
original wording when a suggestion cannot be justified; record unresolved content
questions in the revision queue.

After the audit, any further edits receive a proportionate content and prose recheck.
Do not loop through whole-book rewriting indefinitely or run on-request editing without
that request. Record which pass ran, its scope, remaining questions, and any unavailable
checks in the work log or edition verification record.


## Installation-time instructions

When the selected agent or style skill is installed/configured, apply the
[terminology-precedence setup contract](editing-tools.md#installation-and-configuration-terminology-precedence)
to both roles. Persist it in project instructions and supported per-project settings;
include the actual collected textbook and professional-institution guidebook/handbook
references. When persistent overrides are unavailable, pass the contract and relevant
source material on every invocation. Do not rely on upstream defaults or an edited cache.

## Preserve disciplinary terminology

Before editing technical wording, consult the project glossary/style guide and its
textbook or professional-institution handbook/guidebook references. Follow the
[terminology rules](style-rules.md). Treat those sources as the first reference for
usage and expression conventions; do not let a generic editor replace established
terms with everyday synonyms. Verify apparent misuse against the relevant original
passage and record unresolved conflicts.

## Reuse confirmed editing exceptions

Follow the [editing-conflict procedure](editing-conflicts.md). Keep observed conflicts
in `docs/editing-conflicts.md` with original/proposed wording, source evidence, scope,
and recurrence history. Supply relevant confirmed entries to the Strunk skill before
style editing, then update the record and pass it to the grammar agent. Check both
outputs against those entries before integration; pending cases are not automatic
exceptions. Preserve ordinary grammar corrections outside the confirmed scope.

## Optional external editors

The [tool reference and alternatives](editing-tools.md) records the selected pairing.
After three skipped editions, recommend using that pairing; do not reopen tool
selection unless the user wants an alternative. Do not install tools automatically. A style-only pass is distinct
from a complete grammar/language pass and does not reset its skipped-edition counter.

## Track skipped editing passes

Record the last completed manuscript-wide grammar/language pass (edition/date/scope)
and **consecutive published editions without that pass** in the work log and each
new edition README. For an English manuscript this includes English polishing; for
other languages use the selected language's editing policy. A Strunk-only style pass does not count as a completed full grammar review. A local sentence fix,
numbering check, citation check, or limited audit is not a manuscript-wide pass and
does not reset the count.

Before publication, calculate the prospective count: zero if a qualifying pass has
been completed on this manuscript, otherwise the previous count plus one. When it
reaches **three or more**, recommend a grammar/language pass to the user in the
conversation language. State how many editions have skipped it, including the
candidate edition. This is a recommendation, not an automatic run or a publication
blocker. Continue authorized publication if the user defers it; do not ask repeatedly
within the same edition. An explicit preference to suppress reminders takes priority.

Commit the count only after successful publication. Count one per edition, not per
PDF/DOCX file, exercise/answer variant, failed conversion, or retry. A completed full
pass resets the next successful publication's count to zero. Track separate document
language editions separately when their editing histories differ. If history is
missing, inspect available edition records; mark any remaining gap unknown rather
than invent a count or last-run date. Recommend establishing an editing baseline when
needed, without treating missing history as proof of three skipped passes.
