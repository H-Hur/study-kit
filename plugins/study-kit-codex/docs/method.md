# The method — building a course of study for one person

This document is the backbone of the kit. The agents and the skills are parts of the
procedure written here, and this order decides which part is used when. No field of study
appears anywhere in it. **What to teach is settled by the kit asking the learner** — this
is the first and most important rule of the kit.

## What the kit assumes and what it does not

Use it when you want to get oriented in a field quickly but do not have time to
work carefully through an entire textbook and all its exercises. Start from what
you already know, skip familiar material, and focus on what you need for your goal.
The scope and depth follow your available time and target capability; this is an
intended use, not a promise of a fixed learning speed or a substitute for practice
when the goal requires it.

It assumes one thing. **The learner is already an expert somewhere, and wants to come up
to working speed in an adjacent field in a short time.** This is not a tool for teaching
a beginner from blank. An expert already has a conceptual frame to hang new material on,
so being told again what they already know not only slows the pace, it is discourteous.
That is why the kit's procedure keeps **finding and maintaining the boundary between what
is known and what is to be learned** at its center from beginning to end.

What it does not assume is everything else. Field, goal, time, the learner's language,
the depth of explanation, whether sources even exist, the delivery channel — all of it is
filled in by asking, at stage 0. The moment knowledge of a particular field enters the
kit, the kit becomes a thing you use once and throw away.

Before starting any large piece of work, judge what it will cost:
[`budget.md`](budget.md) carries the measured sizes and the rules for deciding whether to
do it now, split it, or schedule it.

## The six stages

```
0 intake → 1 sources → 2 boundary & goal → 3 plan → 4 run & feedback loop → 5 finish & review
```

The artifact of each stage is the input of the next, and stage 4 is a loop that returns
to itself. Stages 2 and 4 rewrite each other — questions from the learner redraw the
boundary.

### Stage 0 — Intake

**Building a study plan starts with asking the learner.** A learner volunteering their
background is luck, not procedure, so the kit must ask first. There are five things to
ask. Who they are (the specifics of their expertise and the reach of their adjacent
knowledge), what they want to learn (the target field, and the goal as a capability
sentence), how much and how deep (time budget, whether as far as the mathematical
derivation or as far as the concept, whether implementing directly or in collaboration),
under what environment and constraints (whether there are scraps of time and how long,
the receiving device and its authentication constraints, tools and assets already held),
and what kind of explanation they like (style, language, visuals).

What most often goes wrong at this stage is the first question. **Learners do not know the
boundary of their own knowledge precisely either.** So take the intake answers as
hypotheses rather than settled facts, and count the procedure for redrawing the boundary
when the first questions arrive as part of intake. Measured, this boundary was corrected
twice.

Procedure: the [`learner-intake`](../skills/learner-intake/SKILL.md) skill.
Artifact: `docs/learner-profile.md`.

### Stage 1 — Sources

The artifact is not a pile of files but **an index whose grades have been judged.** It
moves in four beats: get seeds, acquire them lawfully, verify them against the originals,
and list them in the index.

Separating seeds from verification is the core of this stage. When there is no map of the
field you do not even know what to search for, so deep research (an outside LLM
consultation or a research agent) gives a first draft of the terrain — and the citations,
figures, and years obtained that way contain plausible things that are wrong. So
**quarantine the entire research result as secondary material** and do not use it as fact
before confirming the original. Without this quarantine rule, unverified information
seeps into the index and the textbook as fact, and afterwards there is no telling the
verified from the guessed.

Deep research is a map-making tool, not a standing tool. Use it once at the very front,
and switch to targeted search once there is a map. There are two occasions to reinvest —
when a new subtopic opens and there is no map of that sub-terrain, and when questions the
textbook cannot answer pile up in the feedback loop (a hole in the textbook is usually a
hole in the map).

Acquired sources are **kept in two forms.** The original is the basis for equations and
tables; the markdown normalization is the working memory an agent can read and search at
any time without tools. Put the citation, source URL, date acquired, and grade at the top
of the normalization. Do not circumvent paywalls; record only the route of acquisition.

Procedure: the [`source-index`](../skills/source-index/SKILL.md) skill, the [`source-scout`](../skills/source-scout/SKILL.md) agent.
Artifacts: `references/` (originals and normalizations) and `REFERENCES.md` (the graded index).

### Stage 2 — Judging the boundary and the goal

Three things are settled here. The learner profile is fixed, the final goal is nailed
down as a **capability sentence** ("when this is over I must be able to ___"), and the
topic map is drawn.

The boundary is not drawn by the name of a field. **It is drawn by capability.** Within
the same field, what is already known and what is to be learned are mixed together. A
boundary of the form "I know this field, so do not explain it" will certainly go wrong,
while one written as a capability — "I am used to handling one such object, but placing
several of them against each other is new to me" — holds. The depth of explanation
(whether as far as the mathematical derivation or as far as the concept) is contracted at
this stage too.

The artifact of this stage is **normally rewritten twice or more** on the learner's
corrections.

### Stage 3 — The plan

The unit of the plan is not "what to read" but **"what you can do when the session
ends."** Work backward from the target capability to lay out sessions, and plant one
diagnostic drill in each. A diagnostic drill is a question that makes the learner name
the cause when a result comes out wrong ("halving this value changed the result — why?").
Practical capability is decided not by the power to build but by the power to narrow down
causes when things do not fit, so a plan without this question ends as knowledge transfer.
What counts as a correct answer to that question is fixed here as well, in the plan,
alongside the question — for the same reason the graduation criteria are written in
advance at this stage rather than at the end.

The delivery channel is settled at this stage too. The channel is decided not by the
maker's convenience but by **the recipient's authentication and device environment.** Test
each candidate first on "does it open without a login." Measured, the channel was
overturned twice, and all of that thrashing came from doing this test late.

Procedure: the [`curriculum-design`](../skills/curriculum-design/SKILL.md) skill, the [`drill-designer`](../skills/drill-designer/SKILL.md) agent.
Artifact: `docs/curriculum.md`.

### Stage 4 — Running it, and the feedback loop

Write the textbook, send it, take questions, and correct the textbook with those
questions. Most of the kit's labor is here.

The textbook is written for a **dual audience.** A textbook fitted to one person alone
fills up with sentences that presume that person's background and becomes a thing that
cannot be reused; but pull the fundamentals out of the body into isolated "groundwork"
boxes and the same textbook becomes a body without padding for the learner and a
self-standing textbook for another reader. Isolation is the core technique of the dual
audience.

A question from the learner is not a shortfall in the learner but **a signal of a defect
in the textbook.** When a question comes, do not stop at answering it; trace back "which
sentence in the textbook produced this misunderstanding" and write the corrected wording
into the pending-revisions document. With the wording written, the revision work ends in
assembly alone; without it, the question disappears.

Manage the textbook by edition and automate distribution. Since folding and unfolding the
answers to the review questions is all it takes to get two editions, exercise and answer,
issue both from the same master to match the learner's circumstances (questions only in
scraps of time, answers included in a focused sitting).

Procedure: the [`textbook-authoring`](../skills/textbook-authoring/SKILL.md) · [`textbook-revision`](../skills/textbook-revision/SKILL.md) · [`textbook-publish`](../skills/textbook-publish/SKILL.md) skills,
the [`textbook-auditor`](../skills/textbook-auditor/SKILL.md) · [`comprehension-auditor`](../skills/comprehension-auditor/SKILL.md) agents.
Artifacts: `docs/textbook.html` (master), the published editions, `docs/textbook-revisions.md` (pending revisions), `docs/notes/` (study notes).

### Stage 5 — Finishing and review

Completion is judged not by material covered but by **whether the graduation questions
can be answered.** The criteria are written in advance at stage 3 by splitting the target
capability. In the review, record what worked and what was waste, grounded in the toolbox
log — improvement for the next learner comes only from there.

Part of what that log holds is about the kit rather than about the subject, and those entries
help improve the kit for whoever studies next. There is a route for sending them back
(<https://github.com/H-Hur/study-kit/issues/new/choose>); it takes the entry, never the study
material.

## The rule for placing tools

**If it needs conversation, the main session owns it; if it means reading a lot and
checking, it is a specialist role.** The [runtime notes](codex-runtime.md) describe how
each host exposes those roles. In this kit, delegated roles report to the main
session instead of conducting learner decisions, so anything that cannot
proceed without the learner answering — intake, converging on a plan, question and answer
— is carried out by the conductor (the main session) as a skill. Conversely, work with a
lot to read where only the conclusion is needed — collating dozens of sources, combing a
conversation record, checking a whole textbook against the conventions — goes to an agent
so that the conductor's context is spent elsewhere.

Specialist agents are designed not as independent actors but as **helpers the conductor
calls.** The context of the study has to sit in one place, and the loop from a question
straight through to a textbook revision holds only on the side that has the context.

## The discipline the kit keeps

- **The subject is settled by asking.** No skill and no agent assumes a field. Every
  topic, boundary, and depth comes from `docs/learner-profile.md`.
- **Draw the boundary by capability, and treat it as a hypothesis.** Redraw it when
  questions arrive.
- **Quarantine secondary material.** Do not use it as fact before confirming the original.
- **Attach quantitative verification to conversion and restoration.** Work that changes
  format quietly loses content. A conversion is not finished until size and a sample have
  been compared against the original.
- **A question back is a signal.** Always attach an actual quoted utterance as the basis
  for the judgment.
- **Write explanations as continuous prose.** Terms laid out as bullets are not study
  material. Use tables and lists only to summarize what has already been explained.
- **The recipient decides the channel.** Test "does it open without a login" first.
- **Record tool use.** Note it whenever a new tool is used or an effect or trap is
  established. This kit itself came out of records like that.
