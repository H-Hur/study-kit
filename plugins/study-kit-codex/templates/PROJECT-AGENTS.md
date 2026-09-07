# {{project name}} — a course of study in {{field}}

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
- The detailed clauses are in `docs/study-kit-style-rules.md` (copied from the kit when the project was created).

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

## Study Kit in Codex

Use the installed Study Kit skills for study-start, study-session,
study-review, and study-publish. Read the runtime notes linked from
the installed skill before work; do not guess an old cache path.
Keep intake and learner decisions in the main conversation. Delegate
bounded specialist work through available subagent tools with the
role procedure, study directory, inputs, write scope, and expected
report. Collect the result before integrating it. If delegation is
unavailable, execute that procedure directly in manageable batches.
