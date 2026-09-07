# Running Study Kit in Claude Code

Read these notes once per task before using an entry point, skill, or specialist
agent. They cover this host's execution; [the method](method.md) contains the
shared learning procedure. The repository also ships a Codex edition with its own
runtime notes. Installing one edition does not change the other.

## Models

For source judgment, curriculum design, textbook writing, and audits, the Claude
Code recommendation is **Opus at high reasoning**. This retains the original
kit's quality-first model guidance. Use the model and effort controls supported
by the installed Claude Code version. Respect the user's explicit model choice;
these instructions are not a mechanism for changing the active model.

Apply the same quality guidance to judgment-heavy specialist work. Prefer scripts
for mechanical conversion and file handling. The original Opus token estimates
in [budget.md](budget.md) describe one historical run, not a limit or guarantee
for every present-day Claude session.

## Commands, skills, and agents

Start with `/study-kit:study-start`, `/study-kit:study-session`,
`/study-kit:study-review`, or `/study-kit:study-publish`. The six learning skills
hold the shared procedures. The four registered agents are `source-scout`,
`drill-designer`, `textbook-auditor`, and `comprehension-auditor`.

The main conversation owns intake, learner decisions, and integration of findings.
Delegate bounded specialist work through available host tools when useful. Give
an agent the study directory, task scope, needed inputs, permitted output paths,
and the required report. Collect the actual result before using it. Keep parallel
writers on disjoint files; serialize changes to the shared source index, textbook,
profile, and pending revisions. If delegation is unavailable, follow the agent's
procedure in the main conversation in manageable batches and disclose the mode.

## Files and evidence

Resolve package files from the installed plugin root, using
`${CLAUDE_PLUGIN_ROOT}` where the host expands it, or relative to the installed
procedure's actual location. Resolve bare study paths from the separate study
project. Use `templates/PROJECT-CLAUDE.md` as that project's `CLAUDE.md`.

For comprehension review, use evidence from the current study conversation,
provided exports, and study notes. The Claude-specific storage path in the agent
is an example for that host; use it only when it exists and can be tied to this
study project. Do not inspect unrelated conversation records. Mark incomplete
evidence explicitly and never manufacture learner quotations.

## Tools, limits, and delivery

Use limits reported by this session and the current-work rules in the budget
notes. Historical estimates do not establish the remaining allowance or a fixed
context/output ceiling. Save bounded results and continue authorized work when
an exact remaining token count is unavailable.

Locate available conversion tools or use an equivalent host PDF workflow. This
plugin bundles no converter, messaging account, or scheduler. Return files in
the conversation by default. External sending requires the learner's authorization
and an available tool. Schedule future work only when the learner requests it;
verify registration through a tool result. Otherwise record the next action in
the work log without claiming that work will run automatically.

Runtime separation update — 2026-09-06. These are host execution instructions,
not newly measured learning procedures.
