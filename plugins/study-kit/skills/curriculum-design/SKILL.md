---
name: curriculum-design
description: The procedure for working a session-by-session curriculum backward from the learner profile and the source index. Use it for requests like "put a study plan together", "how many weeks should this be", or "let's settle the session structure". It covers working backward from the capability sentence, why a diagnostic drill is planted in each session and why what counts as a correct answer to it is fixed in advance, writing the graduation criteria, testing the delivery channel, and designing a secondary track for scraps of time.
---

Read the [runtime notes](../../docs/runtime.md) once per task before following this procedure.


# Curriculum design — working backward from capability

The inputs are `docs/learner-profile.md` and `REFERENCES.md`. If either is missing, do not
start here — a plan built without the profile becomes generic, and a plan built without the
sources has no basis.

## The unit of the plan is "what you will be able to do"

Do not title sessions as things to read — "Introduction to X", "Fundamentals of Y". Title
them as **"what the learner can do when this session ends."** Splitting the target
capability sentence produces that form naturally.

The backward procedure is this. Take the target capability sentence and ask what must be
doable immediately before it. Ask the same question of that answer. Stop when you reach
something the learner can already do (the boundary in the profile). Reverse the chain that
comes out and you have the session order.

If the chain is longer than the time budget, **do not cut it; bundle it.** Put two
capabilities in one session, or renegotiate the target capability itself with the learner.
A plan that skips a necessary step collapses partway.

## Plant one diagnostic drill in every session

Practical capability is decided not by the power to build but by **the power to narrow down
causes when things do not fit.** So plant, in each session, one question that presents a
result that came out wrong and asks for the cause.

- Good diagnostic drill: "Halving one setting changed the result — why?"
  (the answer points at the central trap of that session)
- Bad diagnostic drill: "Explain X" (that is a knowledge check, not a diagnosis)

The answer to a diagnostic drill is usually a **representative trap** of the field. Finding
the traps in the source index first and then placing the exercise that makes the learner hit
that trap into the session is the order that fits best.

**Fix what counts as a correct answer at the same time as the question.** Beside each
session's drill in the plan, write the one or two things the answer must name for that
session to count as landed. The reason is the one given below for the graduation criteria:
a criterion written after the answer has been heard softens to match the answer that was
given. Once written, do not revise it because the answer missed it — an answer that misses
the criterion is an item for the pending-revisions document, not a reason to lower the bar.
The criterion belongs to the learner, not to a marker. It is there so that they can tell
alone whether the session landed, and so that a miss names which part of the material to
fix.

## Fix the standard run of a session

Divide the time budget into segments and give each segment an owner. The division that
worked, measured, on a 2-hour session was 20 minutes of concept briefing (reading together a
summary **prepared before the session** and discussing it), 80 minutes of practice and
experiment, and 20 minutes of wrap-up (answering the diagnostic question alone, drafting the
study note, the work log).

The key is that **the briefing is not made during the session.** Between sessions the
conductor prepares the briefing, the scaffolding, and any slow computation, and the session
time is spent only on understanding and diagnosis.

## Write the graduation criteria now

Completion is judged not by material covered but by **whether the questions can be
answered.** Split the target capability sentence into three or four self-check questions and
write them at the end of the plan document in advance. Written at the end, the criteria
soften to match whatever was actually done.

Write the questions as **"what can you judge"**, not "what do you know."

## Test the delivery channel

The channel is decided not by the maker's convenience but by **the recipient's
authentication and device environment.** Test each candidate in order.

1. **Does it open without a login.** Most candidates drop out here. Measured, a web-published
   link was pushed out of the main channel by this test alone.
2. Does it open directly on the learner's device (does it demand a dedicated app, an
   extension, a particular browser).
3. Is it readable offline (decisive if the scraps of time are underground or in transit).
4. Is resending an updated version automatable.

Do this test late and you rebuild the channel — measured, the channel was overturned twice.

## The secondary track — scraps of time

If the scraps of time in the profile are meaningful (30 minutes each way or more), design a
secondary track. There is one rule. **Do not start a new topic on the secondary track.**
Carry only preview and review of what the sessions covered. The environment makes
concentration hard, so meeting a new concept there for the first time usually fails.

## Artifact

Build `docs/curriculum.md` from [`templates/curriculum.md`](templates/curriculum.md), and
**lay out the items that need a decision as options** for the learner to settle. Record the
settled items at the end of the document with the date — that becomes the basis for
revisiting "why was it decided this way" later.
