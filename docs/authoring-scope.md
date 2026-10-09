# Decision: two modes in one plugin

Updated — 2026-10-09, [issue #1](https://github.com/H-Hur/study-kit/issues/1).
The user selected **learning and authoring modes in the same plugin**. This supersedes
the earlier separate-plugin recommendation. Shared fixes should be maintained once,
without coordinating patches across separate learning and authoring products.

The implemented [mode contract](../plugins/study-kit/docs/project-modes.md) defines
entry routing, intended-reader versus requester profiles, supplied-draft boundaries,
and scope/publication authority. Intake and project templates record the mode. Session
and review commands branch for authoring; shared source, textbook, revision, and
publication procedures remain single-source. Comprehension review requires actual
learner evidence and does not classify the author's editorial remarks as learning gaps.

Claude Code and Codex continue to be runtime distributions of the same source and
release version. No additional product plugin or independently maintained procedure
copy is introduced. The current 2.1.0 release includes this decision.

The final intake order is explicit: first ask personal learning versus teaching.
For personal learning, ask only learner level. For teaching, ask instructor and learner
levels separately, then choose assistance within instructor knowledge or a bounded
researched extension. Record and reuse that content-scope decision.
