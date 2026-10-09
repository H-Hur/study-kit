# Learning and authoring modes

Decision — 2026-10-09, issue #1. One plugin contains two modes. Source verification,
textbook writing, revision, audit, and publication have one maintained implementation.
Claude Code and Codex remain runtime packages generated from the same procedures.

## Select once, before profiling

Begin a new project by asking: **"Is this for your own learning, or are you creating
a course or teaching material for other learners?"** Make this the first intake
decision, before questions about level. If the user has already explicitly answered
it, acknowledge that answer rather than ask it again; do not silently infer the mode
from a request to make a textbook. On resuming a project, reuse its recorded decision. Record **Project mode: learning / authoring** in the
project instructions and `docs/learner-profile.md`. Existing personal study projects
remain in learning mode unless the user changes that purpose. A request to write a
textbook alone does not establish authoring mode: a learner may want their own textbook.

- **Learning**: the requester is the learner. Ask only for that learner's level,
  expressed as known concepts and practical capabilities. Do not ask for a separate
  instructor level or an instructor expansion policy. Then run the remaining intake,
  curriculum, session preparation, and comprehension feedback loop.
- **Authoring**: the requester commissions or writes material for other readers. The
  reader profile is a hypothesis about those readers, not a profile of the requester.
  Use the authoring adaptations below before learner-specific instructions elsewhere.

If the requester also studies the subject, keep author and reader evidence separate.
Ask for a mode change only when the active purpose is genuinely ambiguous. Preserve
existing records when changing mode; do not reinterpret old editorial questions as
learning evidence. Do not maintain duplicate copies of shared production procedures.

## Authoring intake and records

Keep the shared path `docs/learner-profile.md` so downstream procedures use the same
input. Title it **Intended reader profile** and record whose assumptions it represents.
Adapt the existing five intake topics rather than conducting a second full intake:

1. Ask for **both the instructor's level and the learners' level**, separately, in
   terms of concepts, methods, and practical capabilities. Establish both before
   asking how far to extend the course. Never substitute the instructor's expertise
   for the learners' background. Record the instructor level and the content approach
   below in the project instructions; keep learner level in the reader profile.
2. What the readers should be able to do after reading, and the manuscript's purpose.
3. Readers' depth and available reading time if known; separately record the author's
   deadline and production scope. Do not invent a study schedule for the author.
4. Reader delivery constraints and available material. Record whether the requester
   supplies or edits a draft, its location, and who decides scope and publication.
5. Reader-appropriate prose and document language, with the requester's conversation
   language recorded separately when they differ.

After both levels are established, ask which content approach to use:

- **Support within the instructor's knowledge**: help organize, explain, and adapt
  what the instructor knows to the learners' level. Research may verify claims or
  clarify an existing topic, but does not silently broaden the course.
- **Research a bounded extension**: include researched material slightly beyond the
  instructor's current knowledge. Set the intended extension topics and depth with
  the instructor; use verified sources, distinguish those additions in the editorial
  record, and explain them to the instructor at their level. The learner-facing
  material still follows the learners' level, not the instructor's level.

Record the selected approach and bounds. An authorized extension is standing scope,
not a reason to ask again for each addition within it. If extension bounds are not
clear enough to research, settle that missing scope first. Work outside those bounds
remains a proposed extension. The instructor can change the approach explicitly later.

Record draft ownership, the authoritative source file, scope authority, publication
authority, deadline, and supplied-draft boundary in the project instructions. A supplied
draft sets the content boundary together with the selected content approach and
authorized research extension. Propose additions outside that combined scope to
the designated scope owner rather than silently expanding it. Reuse approvals already given within
that scope. Leave unknown reader properties explicitly unknown and ask only when they
matter to the current work. The requester confirms the profile as a design assumption,
not as evidence that actual readers have mastered the material.

## Shared procedures and mode-specific behavior

| Procedure | Authoring behavior |
|---|---|
| Source index and source scout | Same verification and acquisition rules |
| Curriculum design | Work backward from reader capabilities into a chapter/reading sequence in `docs/curriculum.md`; omit session timing and secondary channels when no taught course was requested |
| Drill design | Design reader exercises and answer criteria when in scope; do not administer them to the requester or infer reader scores |
| Textbook authoring | Use reader profile and content plan; preserve the supplied draft's boundary and distinguish proposed extensions |
| Textbook revision | Treat requester questions as editorial feedback, not evidence of poor comprehension; queue changes under the same publication policy |
| Textbook audit and publication | Same content/style audit, selected formats, edition records, and authorization rules |
| [`study-session`](../skills/study-session/SKILL.md) | Prepare the next agreed writing/review milestone, pending editorial questions, and material needed; do not force a learner briefing or diagnostic session |
| [`study-review`](../skills/study-review/SKILL.md) | Review manuscript quality and pending editorial issues through the textbook auditor; do not run a comprehension audit of the author |
| Comprehension auditor | Use only when actual learner evidence is explicitly supplied for that purpose; identify its subjects and limits. Author/editor remarks are not learner evidence |

When creating project instructions from the shared template, replace the learning-only
purpose, working rules, session progress, and success criteria with this authoring
contract. Retain the shared language, source, revision, and publication rules. Judge
completion by the agreed manuscript scope and checks, not the requester's learning.
This mode introduces no classroom grading, student tracking, or inferred learning results.
