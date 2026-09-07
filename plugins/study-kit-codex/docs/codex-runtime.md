# Running Study Kit in Codex

Read these notes once per task before following a bundled skill, including a
specialist role. They govern Codex execution of [the shared method](method.md)
and [budget notes](budget.md). The same repository also ships the Claude Code
edition with its own commands, agents, and model guidance.

## Models and reasoning

For source judgment, curriculum design, textbook writing, revisions, and audits,
recommend **GPT-6 Astra (`gpt-6-astra`) with High (`high`) reasoning**. For a
particularly difficult derivation or conflicting sources, Extra High (`xhigh`)
is an option. **GPT-5.6 Sol (`gpt-5.6-sol`) with High** is the alternative when
Astra is unavailable or the learner prefers lower usage. Prefer scripts for
mechanical conversion and file handling.

This is a recommendation based on task requirements and current official model
positioning, not a measured Study Kit comparison. Availability depends on the
account and client. Respect a model choice the learner has already made. Do not
claim to switch the active model by reading this file, edit global configuration,
or silently substitute a model. When a recommended model is not selected, state
that once and continue with the selected model unless a real limitation prevents
progress. The learner controls model selection through the host.

For delegated judgment work, inherit the parent's selected model and reasoning
unless the learner has chosen a different configuration. Check for a configured
subagent override before relying on inheritance; do not silently downgrade a
specialist or raise usage above the learner's choice. Full-history inheritance
and explicit model overrides may have different spawn requirements in different
clients; follow the tools actually exposed by the active host.

## Package files and study files

Resolve bundled Markdown links relative to the document containing the link. From
`skills/<name>/SKILL.md`, the installed plugin root is two directories up. Resolve
it from the actual skill path supplied by Codex, never from the working directory
or a guessed cache path. This package does not require a plugin-root environment
variable.

Bare paths such as `docs/learner-profile.md`, `docs/textbook.html`, `REFERENCES.md`,
and `references/` refer to the learner's study project. Keep that project separate
from both the kit repository and its installed cache. Use the learner's chosen
folder, or settle a separate destination when starting a course.

When creating the project, fill in the bundled `templates/PROJECT-AGENTS.md` as
the study project's `AGENTS.md`. Copy the bundled style rules to
`docs/study-kit-style-rules.md`; the project instructions then keep working without
a path into a particular installed plugin version. Fill in the work log, toolbox
log, and inbox README as well. Merge with existing project instructions when
present rather than replacing them wholesale.

## Entry points and learning skills

Use the skill picker or ask for the named workflow in ordinary language. Read the
linked procedure before executing a step; a reference to a skill is not itself a
tool invocation. The four entry points and six learning skills are:

| Purpose | Installed skill |
|---|---|
| Start intake and a study project | [study-start](../skills/study-start/SKILL.md) |
| Prepare a session | [study-session](../skills/study-session/SKILL.md) |
| Review comprehension | [study-review](../skills/study-review/SKILL.md) |
| Integrate revisions and publish | [study-publish](../skills/study-publish/SKILL.md) |
| Establish the learner profile | [learner-intake](../skills/learner-intake/SKILL.md) |
| Acquire and grade sources | [source-index](../skills/source-index/SKILL.md) |
| Design the learning sequence | [curriculum-design](../skills/curriculum-design/SKILL.md) |
| Write the textbook | [textbook-authoring](../skills/textbook-authoring/SKILL.md) |
| Draft changes from questions | [textbook-revision](../skills/textbook-revision/SKILL.md) |
| Produce and verify editions | [textbook-publish](../skills/textbook-publish/SKILL.md) |

Intake, learner decisions, answering questions, and integrating revisions belong
to the main conversation. Do not send the learner to another task to answer an
intake question. The Claude slash-command syntax is not required in Codex.

## Specialist skills and subagents

The four specialist procedures below are installed as skills. They are not
registered named Codex custom agents merely because a skill has the same name.
This package does not install files into a user's `.codex/agents/` or change
agent configuration. A normal available Codex subagent can execute a role by
reading its installed skill; no custom-agent setup is required for that route.

| Role | Supply as inputs | Permitted writes and return |
|---|---|---|
| [source-scout](../skills/source-scout/SKILL.md) | Bounded seed list, profile, existing source index, acquisition scope | Acquired originals and normalized copies under `references/`, assigned updates to `REFERENCES.md`; return verified index entries, citation corrections, failures and missing coverage |
| [drill-designer](../skills/drill-designer/SKILL.md) | Profile, session of curriculum, relevant chapter and verified sources | Return questions, answers, diagnostic criterion and unresolved checks; the main conversation incorporates them into the textbook and curriculum |
| [textbook-auditor](../skills/textbook-auditor/SKILL.md) | Profile, bundled style rules, named chapter or textbook, pending revisions | One new report under `docs/reports/`; return locations and replacement wording, without editing existing study files |
| [comprehension-auditor](../skills/comprehension-auditor/SKILL.md) | Profile, actual study conversation evidence, notes, recovered questions, pending revisions and work log | One new report under `docs/notes/comprehension/`; return quoted evidence, proposed re-explanations and evidence gaps, without editing existing study files |

### Dispatch and collect

These instructions request delegation for bounded specialist work when it can
run independently alongside useful main-session work and the active host exposes
subagent tools. They do not require delegation when it is unavailable or would
only duplicate the main session's work.

1. Resolve the role's skill to an absolute installed path. Supply that path and
   the runtime notes, the absolute study directory, relevant input paths or
   evidence excerpts, the requested scope, allowed writes, and expected return.
   Do not assume a child can see the parent's entire conversation or skill list.
2. Spawn through the host's actual subagent facility using an available agent
   type. Do not pass a specialist skill name as a registered agent type unless
   the host reports such a custom agent. An example task instruction is:

   > Read the installed source-scout skill at [resolved absolute path] and its
   > runtime notes. Work in [absolute study directory] on [this bounded seed
   > list]. Read [profile and index paths]. Write only [assigned paths]. Return
   > verified index entries, citation corrections, acquisition failures, and
   > unresolved checks. Do not make learner decisions or edit other files.

3. Create required parent directories within the permitted study paths before
   writing originals, normalized copies, or reports. Give each worker disjoint
   outputs. Serialize writers to `REFERENCES.md` or
   have workers return proposed entries for the main session to merge. Use a
   distinct report filename if the role's dated report already exists. Do not
   overwrite an earlier report or have workers edit the textbook concurrently.
4. Continue independent main-session work, then wait for actual completion using
   the returned handle. A successful spawn is not a completed report. If a worker
   fails, surface the gap and retry a bounded part or perform it directly. Do not
   fabricate findings from a worker that has not returned.
5. Inspect the returned evidence and outputs. The main conversation resolves
   conflicting findings, updates the profile or pending revisions, and decides
   with the learner what belongs in the next edition.

When a specialist skill is invoked directly in the main conversation, apply this
same dispatch decision. When already running as the delegated specialist, execute
the procedure there and return; do not spawn a second agent for the same role.
If delegation is unavailable, slots are exhausted, or no independent main-session
work remains, execute the same procedure directly in bounded batches. State the
execution mode and retain the role's input, output, and write restrictions.
Use subagents rather than creating new user-owned tasks for internal role work.

## Conversation evidence

Use the current study conversation, notes, recovered questions, or an export
supplied for this course. For a child without the current conversation, include
actual relevant excerpts with source labels or provide an authorized export path.
If evidence is missing, state the gap and ask for the relevant material only when
needed. Do not guess the host's private storage layout, inspect unrelated projects,
or invent learner quotations. A file-only review must identify its narrower scope.

## Tools, budgets, and delivery

The plugin bundles instructions and templates, not a browser, PDF converter,
messenger account, or scheduler. The local PDF examples require a Chrome-compatible
browser and Poppler (`pdftotext` and `pdfinfo`); locate actual executables and follow
the active host's tool policy before using them. Prefer an available host PDF
workflow when it preserves exercise/answer separation and verification. If no
converter is available, return the HTML master and state that PDFs were not made.

The token counts in the budget and source-index notes are historical Claude Code
estimates, not Codex benchmarks or limits. Use the current-work rules and actual
host limits. Do not require 150k remaining tokens or stop merely because no exact
budget is exposed. Save bounded artifacts and continue the authorized scope;
context management, account allowance, and output limits must be treated separately.

Return generated files in the current conversation by default. Use an external
delivery channel only when the learner has authorized that delivery and a suitable
tool is available. The messenger variables in the example come from the learner's
setup. If a channel is unavailable, return files for manual delivery and state
that they have not been sent.

Schedule follow-up work only when the learner asks and the host supports it.
Otherwise record the next action in the work log. Do not claim an automatic
follow-up, delivery, or background task was registered without a confirming result.

## Basis and validation

Updated 2026-09-06 against official [model guidance](https://learn.chatgpt.com/docs/models),
[subagent guidance](https://learn.chatgpt.com/docs/agent-configuration/subagents),
and [plugin structure](https://developers.openai.com/plugins/build/plugins).
These are execution adaptations. Package checks establish file structure and
handoff contracts, not the quality or successful execution of a complete course.
