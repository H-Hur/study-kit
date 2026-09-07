# Try Study Kit with your own learning goal

Study Kit helps you turn an existing area of expertise into a starting point for
learning an adjacent field. It asks about your background and goal, checks sources,
builds a plan and textbook, and carries questions back into textbook revisions.

Start with the [public demo](https://study-kit-demo.gjgusdh.chatgpt.site).
It is a Korean-language illustrative walkthrough, with a learner brief, a short
plan, a textbook passage, a question, and a revised explanation. The example is
newly written demonstration content, not a real learner record or evidence of
learning outcomes. Reading it requires no installation; it does not run a model.
Study Kit itself can produce material in the learner's chosen language.

## Who should try it first

Use it when you want to get oriented in a field quickly but do not have time to
work carefully through an entire textbook and all its exercises. Start from what
you already know, skip familiar material, and focus on what you need for your goal.
The scope and depth follow your available time and target capability; this is an
intended use, not a promise of a fixed learning speed or a substitute for practice
when the goal requires it.

You already use Claude Code or Codex, know one field well, and have a specific reason
to learn something nearby. Bring a goal phrased as something you want to be able to
do, rather than only the name of a topic.

The kit is available for noncommercial use under its [component licenses](../LICENSE):
PolyForm Noncommercial 1.0.0 for code and CC BY-NC-SA 4.0 for documents and prompts.
Commercial use outside those grants requires separate permission. Running it uses
your host's account and model allowance. Preparation time and usage depend on the
scope, sources, and model; there is no verified universal time or cost estimate.

## Install and begin

Follow the [installation instructions](../README.md#install) for your host, then
open a new conversation in a separate study project. Keep your learning files out of
the kit repository.

Tell the agent:

> I work in [the field I already know]. I want to learn [the adjacent field] well
> enough to [what I must be able to do when it is over]. Start a course of study
> with Study Kit.

The opening exchange settles your background, goal, available time, preferred
explanation style, and delivery needs. Review the profile and plan with the agent
before it proceeds. During study, ask about a passage that does not land and use
the review and publishing workflow to carry that question into the next edition.

The [distribution guide](distribution.md) covers updates and optional conversion
dependencies. The plugin keeps study artifacts in your project and has no telemetry;
your AI host's own data handling still applies.

## Tell us where the procedure broke

One concrete point is enough: an installation failure, an explanation that assumed
too much, or a step where the procedure stopped helping. Use the relevant
[issue form](https://github.com/H-Hur/study-kit/issues/new/choose), or reply in the
community post where you found the kit. GitHub feedback requires a GitHub account.

Describe the shape of the problem without uploading your textbook, profile, notes,
or private conversation. See [Contributing](../CONTRIBUTING.md) for examples.

## What has been tried

The original procedures came from one real course of study in Claude Code. The
repository records eight textbook revisions, two delivery-channel changes, and a
conversion that lost text. These are the origin of maintenance rules, not evidence
of broad effectiveness. The Codex edition adapts the shared procedures for its host;
those original measurements are not Codex measurements.

Public demo and first-use guide added on 2026-09-06. This introduces an entry point
for readers, not a new measured learning procedure.
