# study-kit — a study support bundle

## 0. What this folder is — read this before anything else

This folder is **not study material. It is a tool for building a course of study.** It
holds the whole procedure for bringing an expert up to working speed in an adjacent
field in a short time: asking the learner, gathering sources, laying out a plan, writing
a textbook for that person, and correcting the textbook from what they ask back.

**It contains no field of study.** What to teach is settled by the kit asking the
learner. That is the first rule, and all the rest come out of it. The moment field
knowledge enters the kit, the kit becomes a thing you use once and throw away.

### The second rule — the studying does not happen here

This folder is **the side that gets read**, not a workshop. When a new course of study
begins, the study project is created in a **separate folder** (`~/Projects/<name>/`) and
only the templates and the procedure are carried over from the kit. Study artifacts —
profile, plan, textbook, records — are never created inside this folder.

The only work done here is work on the kit itself.

## 1. What to do first when this folder is opened

**If `RESUME.md` is present, read it first.** It carries the state of work on the kit
itself and what is queued next. Write one when work on the kit has to be carried across
sessions, and **delete it once that queue is empty** — what was done is the git log's job,
not a handover note's, and a note that has turned into a changelog is worse than none.

Then sort the user's first request into one of three.

- **They want to begin a course of study** → go to section 2. Start with intake.
- **They want to change the kit** → work under the rules in section 6.
- **They want to see what this is** → explain from `README.md` and
  `plugins/study-kit/docs/method.md`. There is no need to read every file in this folder
  (see section 5).

If the sorting is unclear, ask. Guessing and creating a study project is the harder one
to undo.

## 2. Beginning a course of study — the opening questions

**Do not wait for the learner to volunteer their background. Ask first.** The detailed
procedure is in `plugins/study-kit/skills/learner-intake/SKILL.md`; what is written here
is only the opening questions actually to be put.

Do not pour out all five at once. **Ask ① and ② first, and move on to ③④⑤ after the
answers come back** — the later questions change depending on the earlier answers. For
items already answered in the first message, lay out what was understood and ask only
for what is missing.

> **① What field are you an expert in, and what specifically do you handle well?**
> Say also how far your knowledge reaches into what borders the field you want to learn.
>
> **② What do you want to learn? State the goal in the form "when this is over I must be
> able to ___."**

Once those answers are in, go on to ask the rest. For items whose options are obvious,
do not ask in open prose — **lay out concrete options and have the learner choose.**
Spelling out the decision in detail and having them pick is what settled the plan
fastest, measured.

> **③ How much time can you spend?** (total, cadence, length of one sitting) **And how
> deep do you want to go?** (as far as the mathematical derivation / as far as concept
> and intuition) **Will you implement things yourself, or work with an agent?**
>
> **④ Do you have odd scraps of time?** (commuting and the like — length and character)
> **What device and conditions will you receive material on?** (must it open without a
> login, will you read offline) **Do you already have tools or assets?**
>
> **⑤ How do you like explanations?** (continuous prose / bulleted points, language,
> visuals, phrasing to avoid)

**Take the answer to ① as a hypothesis, not a settled fact.** Learners do not know the
boundary of their own knowledge precisely either. Measured, this boundary was corrected
twice after the study had begun. Write it into the profile as a hypothesis and redraw it
when the first questions come back.

## 3. Structure

```
study-kit/
├── CLAUDE.md                     ← this file
├── README.md                     install and a summary of the parts
└── plugins/study-kit/
    ├── docs/method.md            the method — the six stages in full (read before working)
    ├── docs/budget.md            what a piece of work costs, and whether to start it now
    ├── skills/                   work that requires exchange with the learner (the conductor does it)
    │   ├── learner-intake/       ask five things and write the profile (+ profile template)
    │   ├── source-index/         seed → acquire → check against the original → graded index (+ index template)
    │   ├── curriculum-design/    work backward from the target capability to sessions (+ plan template)
    │   ├── textbook-authoring/   the dual-audience textbook (+ textbook master HTML, style rules)
    │   ├── textbook-revision/    turn questions into drafted revisions (+ pending-revisions template)
    │   └── textbook-publish/     issue two editions, exercise and answer
    ├── agents/                   work with a lot to read where only the conclusion is needed (delegate)
    │   ├── source-scout          acquire, verify, normalize, and list sources
    │   ├── drill-designer        design review questions and diagnostic drills
    │   ├── textbook-auditor      check the textbook against the conventions and style rules
    │   └── comprehension-auditor identify concepts not grasped, from the conversation record
    ├── commands/                 study-start · study-session · study-publish · study-review
    └── templates/                skeleton of a new study project (CLAUDE.md · work log · toolbox log · mailbox)
```

**The basis for splitting the tools**: work that requires exchange with the learner is a
skill (the conductor does it directly); work with a lot to read where only the
conclusion is needed is an agent. A subagent cannot speak to the learner, so intake,
converging on a plan, and question-and-answer cannot be delegated.

## 4. Opening work — the order for starting a new course of study

Once intake is done, go in this order. The basis for each judgment is in
`docs/method.md`.

1. **Settle the profile** — write `<study folder>/docs/learner-profile.md` and show it to
   the learner for confirmation. Have the target capability sentence and the boundary
   corrected in the learner's own words.
2. **Project skeleton** — take `PROJECT-CLAUDE.md` · `worklog.md` · `toolbox-log.md` ·
   `inbox-README.md` from `templates/`, fill them in, and create `docs/notes/` and
   `docs/reports/`.
3. **Source index** — if there is no map of the field, get seeds from deep research, then
   hand acquisition, verification, and normalization to `source-scout` and build
   `REFERENCES.md`. Every citation that came from a seed is secondary information, so
   **do not use it as fact before checking it against the original.**
4. **Plan** — work backward from the target capability to sessions and plant a diagnostic
   drill in each. Test delivery channels starting with "does it open without a login."
   For items that need a decision, lay out options and get them settled.
5. **Textbook** — once the curriculum is settled, writing the whole thing up front is
   better. For judging length, see section 5.
6. **Publish** — produce two editions, exercise and answer, and send them to the channel.

That much is the preparation before study begins. After that the loop runs each session:
`study-session` → session → `study-review` → `study-publish`.

## 5. Estimating the work and judging the budget

The whole of it lives in **`plugins/study-kit/docs/budget.md`** — host-specific model guidance, the historical sizes of artifacts, how to delegate
bounded research when supported, the split between mechanical conversion and model
transcription, the current-work rules, and the one-line check
before starting. **Read it before starting any large piece of work.** It sits inside the
plugin, so an installed copy carries it too; work on the kit itself is judged by the same
rules as work on a course of study.

Two figures belong to this folder rather than to a course of study: reading this whole
folder is about 30k, and the kit's own documents come to about 116 KB in all.

## 6. When changing the kit

- **Check every time that no field vocabulary has crept in.** One example sentence drawn
  from a particular field costs that document its reusability. Sweep the whole tree after
  editing.

  ```bash
  grep -rniE '\b(<list the field vocabulary of the study you worked on>)\b' --include='*.md' --include='*.html' .
  ```

  **Use word boundaries in the pattern.** Short tokens match inside ordinary English words
  and bury the real hits under a page of false positives.

- **If a feature requires the learning to be measured, suspect that it is assuming a
  teacher.** The kit is used by a learner studying alone. Measuring the effect of study is
  what an instructor needs in order to grade; a lone learner needs only enough to judge for
  themselves whether it landed, and to know which part of the material to fix. A criterion
  that exists so the learner can check alone — and so that a miss names a defect in the
  material — is in scope. Anything that only makes sense with someone standing on the other
  side keeping score is not. If a learner decides for themselves that they need to measure,
  that reaches the kit as a method they submit, not as a feature invented here.
- **Do not add a procedure that has not been measured.** The worth of each document is
  not in "do it this way" but in "we did it this way and it broke here." Do not invent
  traps that were never hit.
- **Do not compress the documents.** Removing the examples from a clause damages its
  intent. Do not shorten because it is long; remove an entire item that is not needed.
- When adding a skill or an agent, apply the split criterion in section 3. If it requires
  exchanging words with the learner, do not make it an agent.
- When a new trap or effect is established, write it into the relevant document on the
  spot. Written later, it disappears.

### What ships, and how a change reaches an installed copy

Three things that reading the tree does not tell you. Each had already gone wrong once when
the kit was installed for the first time.

- **Each host publishes its plugin subtree.** Claude Code uses `plugins/study-kit/`;
  Codex uses `plugins/study-kit-codex/`, generated from the same procedures. The files at the top of this folder —
  `CLAUDE.md`, `README.md`, `CONTRIBUTING.md` — are not part of the plugin. So nothing an
  installer needs may live only up here. The budget rules did, and nobody who installed the
  kit received them until they were moved into `plugins/study-kit/docs/budget.md`.
- **Address the kit's own files as `${CLAUDE_PLUGIN_ROOT}/...`.** After install, the
  commands and skills run in the learner's study project, where a bare `docs/` or
  `templates/` is the learner's own folder — so a relative path to a kit file either fails
  or quietly reads the wrong file. This was hit twice, in `study-start` and in the
  `PROJECT-CLAUDE.md` template. Paths in those same documents that mean the study project's
  own files stay relative; they are meant to resolve there.
  This variable applies to Claude Code. The Codex generator converts package references
  to links resolved from the installed skill and supplies a `PROJECT-AGENTS.md` template.
- **A change that does not raise the version does not travel.** The plugin cache is keyed by
  version. Editing a published version in place and refreshing the marketplace left an
  installed copy untouched — the fix reached nobody. Raise the version whenever the change
  ships inside the plugin.

## 7. Records for this folder

Record changes to the kit in the relevant document with the date, and raise the version in
`plugins/study-kit/.claude-plugin/plugin.json` whenever the change ships inside the plugin —
section 6 says why it does not reach anyone otherwise.
The same version is used by the generated Codex package. After changing either edition,
run `python3 scripts/build_codex.py` and check in the result. See
`docs/distribution.md` for the shared release workflow.

**The kit's own documents are written in English.** File names and identifiers are also
English. This governs the language of maintaining the kit; it says nothing about the
language of a course of study. **The language of the profile, the plan, the textbook, and
the conversation with the learner comes from `docs/learner-profile.md`**, which is
settled by asking the learner in intake. An English kit produces a Korean textbook for a
learner who wants one.

### Parked, with reasons

Directions that were considered and set down. The reason matters more than the item — it is
what stops the same idea being picked up again without the objection.

- **Delayed review.** The kit has no retention mechanism, and understanding something during
  a session is not the same as being able to use it two weeks later. Parked because every
  design drafted for it ended in measuring the effect of the study, and **measurement is what
  a teacher needs.** This kit is used by someone studying alone. A lone learner needs enough
  to judge for themselves whether it landed, and to know which part of the material to fix —
  not a record of how they scored over time. If retention is taken up again, it comes back
  through the feedback route: a learner who decided for themselves that they needed to
  measure, reporting how they did it.
- **A mastery-state ladder** (exposed → guided → independent → transferable → durable). The
  direction is right — the kit tracks what is known versus what is to be learned, but not how
  well. Parked because maintaining a five-state value per concept is a real burden for a
  one-person tool, and delayed review buys more for less.

### Distribution update — 2026-09-06

Codex packaging and Claude migration requirements have now been checked against official
OpenAI documentation, linked in `docs/distribution.md`. Both editions ship from one
repository and version. The generated Codex edition converts commands and specialist
roles to skills; the original study measurements remain attributed to their original
runtime. This is a packaging adaptation, not a newly measured teaching procedure.

### Runtime coexistence update — 2026-09-06

Version 1.3.0 provides separate runtime instructions: Claude Code reads
`plugins/study-kit/docs/runtime.md`; Codex reads `codex/runtime.md` (shipped as
`docs/codex-runtime.md`). Shared procedures defer to the active host for model
selection, delegation, evidence access, limits, and delivery. Both packages remain
in the repository. Historical budget rules and measurements are retained as
attributed records, with separate current-work guidance. Codex specialist skills
now specify dispatch, input and write boundaries, completion handling, and direct
execution fallback. These are runtime adaptations, not new learning measurements.
