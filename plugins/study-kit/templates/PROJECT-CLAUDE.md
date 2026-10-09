# {{project name}} — a course of study in {{field}}

- **Project mode**: {{learning / authoring}}

{{Template adaptation: the text below defaults to learning mode. For authoring mode,
replace the purpose with producing a manuscript for the intended readers, and use
reader capabilities rather than the author's expertise in the boundary section.
Replace study working rules and session progress with writing/review milestones and
manuscript acceptance criteria. Keep shared language, source, and publication rules.
Fill in the authoring contract below only in authoring mode; remove it otherwise.}}

### Authoring contract (authoring mode only)

- Instructor level and role: {{concepts, methods, practical capabilities; separate from learner level}}.
- Learner level: {{capabilities and boundary; details in the intended reader profile}}.
- Content approach: {{support within instructor knowledge / bounded researched extension}}.
- Extension bounds: {{authorized topics and depth, or none}}. Research beyond these
  bounds requires a scope decision; research within them does not need repeated approval.
- Reader profile: `docs/learner-profile.md`; content plan: `docs/curriculum.md`.
- Supplied draft and authoritative source: {{path and owner's instructions}}.
- Scope authority: {{who decides contents; existing authorization}}.
- Publication authority: {{who decides publication; existing authorization}}.
- Scope and deadline: {{agreed manuscript boundaries and writing milestones}}.
- A supplied draft and authorized extension define the scope. Additions outside that
  scope are proposed extensions for the scope owner.
- Editorial questions are revision input, not evidence of the author's comprehension.
- Completion means the agreed manuscript and publication checks are satisfied.

## 0. What this project is — read this before anything else

**This is a study project.** The primary artifact is not working code but **the learner's
understanding**; code, experiments, and study notes are the evidence of it.

**Final goal**: {{capability sentence — when this is over I must be able to ___}}
And to understand the principles that requires, {{depth contract — e.g. conceptually rather
than mathematically}}.

### The learner profile and the boundary of explanation (strict)

The whole of it is in [`docs/learner-profile.md`](docs/learner-profile.md). In summary:

- The learner is an **expert in {{field}}**. {{capabilities already familiar}} are already
  familiar, so explaining at that level is wasted page and discourtesy.
- But the boundary is not drawn by the name of a field. **{{the subordinate area being
  studied}} is the same field, yet it is precisely what the learner came to learn.** Even
  where a familiar concept is used as material, all of it is the subject of study.
- Subjects of study — explained fully on first appearance: {{list of topics}}.
  **Explanations are given {{depth contract}}.**
- This boundary is a **hypothesis.** When the learner corrects it, amend the profile and leave
  a record of the correction.

### Style of explanation (strict)

- **Write continuous explanation, not lists of words.** Work out in sentences why the concept
  became necessary, how it joins what came before, and what it leads to next. Use tables and
  lists only to summarize what has already been explained.
- **Do not write translationese.** Where a settled term exists, use it and give the original
  alongside on first appearance.
- The detailed clauses are in `${CLAUDE_PLUGIN_ROOT}/skills/textbook-authoring/references/style-rules.md`.

### Terminology references

Use original textbooks and professional institutions' handbooks/guidebooks first for
technical terminology, usage, and customary expressions. Record chosen terms and
source edition/page/section in the project glossary or style guide. Preserve these
conventions during grammar and English editing; resolve conflicting source usage
explicitly. Verify factual claims separately against appropriate sources.

When configuring `writing-clearly-and-concisely` and the chosen grammar `proofreader`,
apply this same terminology precedence to both roles. Record the source-index,
glossary/style-guide, and original textbook/guidebook/handbook paths and relevant
edition/page/section. Use supported project-level settings; if no override is available,
pass the rule and relevant sources in every invocation. Do not edit managed plugin
caches or assume a delegated agent has inherited the references. Check this configuration
after tool updates and review technical substitutions against the cited conventions.

### Document editing rules

- Use title phrases, not sentence-form headings. Number the content hierarchy `1.`,
  `1.1.`, `1.1.1.`, with a trailing period and one space before the title.
- Put figure numbers/captions below figures and table numbers/captions above tables.
- Leave one body-text line of space between each complete figure/table-plus-caption
  block and surrounding prose, using consistent paragraph/block spacing.
- Prefix table header cells `(A) `, `(B) `, etc., and leftmost data cells `(1) `,
  `(2) `, etc. Row numbering starts at the second row and excludes the header.
  Use exactly one space after each closing parenthesis.

- Number standalone display equations `(1)`, `(2)`, etc., at the far right of their
  equation row. Do not number inline mathematics within sentences or paragraphs.
  Keep equation numbering separate from heading, figure, and table numbering.

### Working rules in study mode

- **When introducing a new method**: explain first what it assumes, where it holds, and where
  it breaks, and only then go to implementation. No black boxes that emit only results.
- **Implementation is {{with an agent / by the learner}}**, and the learner concentrates on
  concepts, design decisions, and diagnosis. There is no need to implement every internal by
  hand, but **do not leave what an agent built as a black box** — get an explanation of what
  it assumed and where it breaks. A subject is finished only when the learner can name
  candidate causes themselves when a result looks wrong.
- **Time budget**: {{total}}. Prepare a {{briefing length}} concept summary before each
  session and spend the rest on implementation, experiment, and diagnosis. The plan is in
  [`docs/curriculum.md`](docs/curriculum.md).
- **When reviewing what the learner built**: do not overwrite it with the right answer; put
  defects and improvements first.
- Documents, conversation, and reports are in {{language}}.
  {{When the profile specifies a split, replace the line above with the following
  two rules, fill them in, and remove these drafting instructions:}}
  - **Conversation language (strict)**: {{language}}. Use it for questions, reports,
    explanations, and short status messages, even when skills or edited files use
    another language.
  - **Document language(s)**: {{language and artifact mapping}}. This governs the
    artifact text, not the surrounding conversation.

## 1. Verification strategy — do not attempt a higher layer on something that has not passed a lower one

{{Fill in to suit the field. e.g. analytic comparison → reproducing a published benchmark →
cross-comparison of fidelity → verifying the applied result}}

## 2. Recording rules

- **Daily record** — accumulate chronologically in the single file
  [`docs/worklog.md`](docs/worklog.md). At the end of each session: "date / what was done /
  decisions / what comes next". **Facts of the work only.**
- **Study record** — files by topic under `docs/notes/`. "What was understood, what intuition
  formed, and what is still unclear (remaining questions)."
- **Pending textbook revisions** — [`docs/textbook-revisions.md`](docs/textbook-revisions.md).
  Register the learner's questions **with the revised wording written out.**
- **Toolbox record** — [`docs/toolbox-log.md`](docs/toolbox-log.md). Whenever a new tool is
  used or an effect or trap is established.
- Keep experiments in units of `experiments/NNN_topic/` with inputs, scripts, results, and
  remarks together. **An unrecorded experiment counts as an experiment not run.**
- Save every artifact in the project folder. An artifact that exists only in scratch is not an
  artifact.

## 3. Rules for adopting sources

Priority for adopting a basis: ① standard textbooks ② original papers and specifications
③ journal articles and technical reports ④ primary library source.

**Not adoptable**: figures, coefficients, or conventions from blog posts or LLM recall. Use
them only as hints and confirm the value in a primary source. Confirmed sources are listed in
[`REFERENCES.md`](REFERENCES.md) with their grade.

## 4. Progress

- Current session: {{N}} / {{total}}
- What comes next: see the end of [`docs/worklog.md`](docs/worklog.md)

## 5. Textbook publication policy

- **Trigger**: {{reuse the user's existing instruction; otherwise default to an
  explicit request to publish. Record a standing automatic trigger only if the
  user has authorized it, including its scope.}}
- **Formats and variants**: {{PDF / DOCX / both; exercise / answer / both}}.
- **Page setup**: {{paper size, margins, fonts, and reference document if applicable}}.
- **Edition directory**: `output/<edition>_<YYYYMMDD_hhmmss>/`, using local time;
  record the timezone in its README. Published directories are immutable.
- Questions and corrections first enter `docs/textbook-revisions.md` with complete
  replacement wording and its source or reasoning. Do not change the master merely
  because a correction was reported. Apply the queue when the trigger is met, or
  follow an explicit instruction to edit the master earlier.
- Reuse authorization within the recorded trigger; do not ask again on every revision.
  Publishing files does not by itself authorize external messages or public hosting.
- Put the edition identifier, date, changes, and verification results in the edition
  README. Keep changeable edition labels out of the textbook body and footer.

## 6. Editorial safeguards

- **Language editing**: {{document language, intended readers, project style guide,
  grammar agent: {{user-selected njjenkins/proofreader or Daniel Rosehill/proofreader;
  exact GitHub source URL and availability}}; variety: American English (en-US);
  sentence-style skill: Strunk-based
  `writing-clearly-and-concisely` (The Elements of Style); timing: on request or an
  explicitly agreed schedule}}. A full grammar/English pass is not required every
  edition. When run, use this order: content corrections →
  `writing-clearly-and-concisely` → selected `proofreader` (en-US) → final audit.
  The grammar agent checks the style-edited manuscript; do not run both in parallel.
- **Editing history**: {{last completed full pass: edition/date/scope; consecutive
  editions published without one, or unknown}}. Recommend a pass when the candidate
  edition brings the count to three or more. A recommendation does not block publication
  or authorize automatic editing. Recommend the selected agent/skill pairing, not
  a new tool search. Record missing dependencies honestly. Update once per successfully published edition;
  reset after a full pass, not after local fixes. No plugin installation is required.
- **Before every updated edition**: check numbering, cross-references, citations, and
  quotation/source support in the final source and outputs, regardless of editing cadence.
- Project terminology and style override generic editing suggestions. Check definitions
  in nearby prose, tables, and captions. Recheck every claim in a rewritten factual
  sentence, including unchanged claims and qualifications.
- **Editable working copies and publication baseline**: {{paths, exact baseline files,
  hashes, and authoritative source}}. At session/milestone startup and before issuing
  an edition, compare saved working copies with the baseline. Preserve and reconcile
  all user edits before conversion; timestamps alone are not a change detector.
- Preserve user deletions. Record ambiguous or contradictory edits for resolution;
  do not silently restore them or overwrite an open document.


### Recurring editing conflicts

Keep `docs/editing-conflicts.md` as the project record of original wording, proposed
mis-edits, source edition/page/section, scoped decisions, and distinct occurrences.
Before sentence-style editing, supply relevant confirmed exceptions to the Strunk
skill. Update findings before the grammar pass and supply the same record to the
selected proofreader. The main session reviews both reports/diffs and owns updates.
Pending entries are not automatic exemptions; repeated suggestions alone establish
no rule. Preserve surrounding grammar corrections, and revalidate exceptions when
their source, meaning, or project convention changes. Retain retired entries' history.
Do not patch plugin caches or export this project's terminology into the reusable kit.
