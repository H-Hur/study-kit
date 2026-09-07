---
name: learner-intake
description: The procedure for receiving a new learner and building the starting point of a study plan. Use it first for requests like "let's start studying", "what should I learn first", or "put a curriculum together for me", and whenever a new study project is opened. It covers the five things to ask, why the answers are treated as hypotheses, how to draw the boundary by capability, and the specification of the artifact learner-profile.md.
---

Read the [runtime notes](../../docs/codex-runtime.md) once per task before following this procedure.


# Learner intake — what to ask before anything else

## Why the conductor must do this directly

Intake is an exchange with the learner. In this kit, delegated roles report to the
main session; **the main session conducts intake and learner decisions directly.** Hand it to an agent and
you get a profile with invented answers or skipped questions, and every curriculum built
on that profile is wrong.

## Procedure

### 1. Ask first — do not wait for the learner to volunteer

A learner putting their background in the first message is luck, not procedure. **The kit
asks first.** There are five things to ask.

**① Who is the learner.** What field are they an expert in, and what are the specifics of
that expertise (the theory, tools, and practice they handle well)? How far does their
adjacent knowledge reach into the field they want to learn?
— This answer sets the floor of explanation. Explaining what is already known is wasted
page and discourtesy.

**② What do they want to learn.** The target field, and the goal as a **capability
sentence**: "when this is over I must be able to ___."
— "I want to understand X" is not a goal. Convert it into what they will be able to do.
This sentence is the starting point for working the curriculum backward and the original
of the graduation criteria.
— **Measured**: a learner entering an adjacent field often cannot state this goal, because
they do not yet know the terrain well enough to say what is worth being able to do. Asking
"what do you want to know" produced nothing usable through several exchanges. What finally
produced the sentence was asking **how it differs from what they already know** — the goal
arrived as a comparison against their own familiar tools. For an adjacent-field learner,
**"tell me what you want to understand" is a worse question than "tell me what you want to
know the difference of."**

**③ How much, and how deep.** Take the time budget split into total, cadence, and session
length (e.g. 3 times a week × 2 hours × 4 weeks). Contract the depth of understanding
explicitly: as far as the mathematical derivation, or as far as concept and intuition.
Execution: implementing directly, or collaborating with an agent.
— Without contracting depth, you renegotiate it at every explanation.

**④ Environment and constraints.** The character of the available time (are there scraps
of time such as commuting, and how long), the receiving device and authentication
constraints (must it open without a login, will it be read offline), tools and assets
already held (licenses, existing projects, reusable code).
— This answer sets the delivery channel. Ask it late and you rebuild the channel.
— **Measured**: this is nominally a question about environment, but it works as a question
that **reopens ②**. Listing what they own leads a learner to say what they intend to do with
it, and that intention turns out to belong in the goal. In one intake, answering ④ added a
whole practical strand to the goal that ② had not surfaced. So when asking about assets, do
not stop at "what do you have" — **follow it with "and what do you mean to do with it."**

**⑤ Preferred style of explanation.** Style (bulleted lists or continuous prose),
language, preference for visuals, phrasing to avoid.
— Learners usually do not mention this unprompted. That is exactly why it must be asked.

### 2. How to ask

Do not pour out all five at once. **Ask ① and ② first, and move on to ③④⑤ after the
answers come back** — the later questions change depending on the earlier answers. For
items whose options are obvious (depth, execution, channel candidates), do not ask in open
prose — **lay out concrete options and have the learner choose.** Spelling the decisions
out in detail and having them pick is what settled the plan fastest, measured.

**But options are a matter of content, not of form.** Measured, a learner stopped an intake
that presented its options as a selection form and answered in plain prose instead; the
answers came immediately once the same options were written into the sentences of the
message. The clause asks for the decision to be spelled out, not for a widget. **Put the
options in prose unless the learner has said they prefer otherwise.**

Do not re-ask what the learner has already answered. If the first message carries their
background, lay out what was understood and ask **only for what is missing.**

### 3. Record the answers as hypotheses

**Learners do not know the boundary of their own knowledge precisely either.** Measured,
this boundary was corrected twice after the study had begun, and both times it surfaced
because the learner said, while reading an explanation, "I already know that" or "this is
new to me." So **write the boundary items into the profile as hypotheses, not settled
facts**, and make room in advance for a record of corrections.

### 4. Rewrite the boundary in units of capability

Do not transcribe the answers as given; **translate them into capabilities.** A boundary
drawn by the name of a field will certainly go wrong, because within the same field what
is known and what is to be learned are mixed together.

- Bad boundary: "I know field A, no need to explain it"
  → half the subtopics of that field may be the subject of study.
- Good boundary: "I am used to handling one such object. Placing several of them against
  each other is the subject of study, even within the same field."

When writing the boundary, **attach one example on each side** — an instance of what will
be explained and of what will not, so that the judgment can be reproduced later.

### 5. Write the profile and get it confirmed

Build `docs/learner-profile.md` from
[`templates/learner-profile.md`](templates/learner-profile.md) and **show it to the
learner before settling it.** Have the target capability sentence and the boundary
corrected in the learner's own words.

## Re-adjusting the boundary — intake does not end in one pass

Even after the study has begun, when the following signals arrive, go back to the profile,
correct the boundary, and leave the date and the trigger in the record of corrections.

- The learner says "I already know that" → move the boundary up.
- The learner asks back about something they said they knew → move the boundary down.
  This is the more common direction.
- Dissatisfaction with the depth of explanation appears ("pictures, not equations", "tell
  me why") → amend the depth contract.

When the boundary changes, the effect propagates into the curriculum and the textbook.
Put the changed boundary into the pending-revisions document
(`docs/textbook-revisions.md`) as an item as well.

## Do not

- Do not fill in the profile by guessing at the learner's background. If it is unknown,
  leave it blank and ask.
- Do not skip intake and start with the curriculum. The cost of undoing that is far larger.
- Do not accept "understanding" as a goal. Always convert it into something they will be
  able to do.
