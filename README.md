# study-kit — a study support bundle

**Build a textbook around what you already know, then revise it from the questions
you ask while studying.**

[Read the public demo](https://study-kit-demo.gjgusdh.chatgpt.site) ·
[Try it with your own goal](docs/try-study-kit.md) · [Install](#install)

The demo is a Korean-language illustrative walkthrough: a learner brief, a short
plan, and a textbook passage before and after a question. It runs no AI and requires
no installation. Its example was written for demonstration, not taken from a real
learner's records. The demo lives separately from this reusable kit.

A plugin for Claude Code and Codex that packages, as reusable procedures and templates,
the procedure for helping an expert come up to working speed in an adjacent field in a
short time.

**No field of study is built in.** What to teach is settled by asking the learner. That
is the first rule, and everything else follows from it.

Use it when you want to get oriented in a field quickly but do not have time to
work carefully through an entire textbook and all its exercises. Start from what
you already know, skip familiar material, and focus on what you need for your goal.
The scope and depth follow your available time and target capability; this is an
intended use, not a promise of a fixed learning speed or a substitute for practice
when the goal requires it.

## What it does

```
0 intake → 1 sources → 2 boundary & goal → 3 plan → 4 run & feedback loop → 5 finish & review
```

It starts by asking the learner five things, builds an index of sources whose grade has
been judged, works backward from the target capability to a curriculum, writes a
textbook fitted to that person yet readable by others, and turns the learner's questions
back into revisions of the textbook. The whole procedure is in
[`plugins/study-kit/docs/method.md`](plugins/study-kit/docs/method.md).

Opening this folder in Claude Code loads [`CLAUDE.md`](CLAUDE.md); Codex reads
[`AGENTS.md`](AGENTS.md), which points to the same maintenance rules. These hold the
purpose of the folder, the opening questions to put to the learner, and the order in
which a new course of study is set up. What a piece of work costs, and whether to start it
now or split it, is in
[`plugins/study-kit/docs/budget.md`](plugins/study-kit/docs/budget.md), which ships with
the plugin.

## Install

Both editions ship from **this repository and the same release version**. Choose the
commands for your host; the learning procedures and templates come from one source.

Choose a route: **desktop menus**, **ask in a local chat**, or **download files**.
Study Kit is distributed through this repository's marketplace; a public catalog
search alone does not register it. Downloading or attaching files alone also does
not register a plugin. See the [desktop installation guide](docs/desktop-install.md)
for complete steps and troubleshooting. The guide distinguishes tested installation
routes from menu procedures that still need validation.

### Claude Code

In the desktop app, use the **Code** tab with a **Local** session. Open
**+ → Plugins** to inspect installed plugins. In the tested app, **Browse plugins**
opens Customize; labels differ from the documentation's **Add plugin** wording.
The verified route is to install/update with the Claude CLI, then start a new
Code session; see the [desktop guide](docs/desktop-install.md#claude-code-desktop).
Do not assume that an account-level Customize install is the same as a local
Claude Code installation.

In the interactive Claude Code CLI, these are slash commands:

```text
/plugin marketplace add H-Hur/study-kit
/plugin install study-kit@study-kit
```

Start a new conversation and run `/study-kit:study-start`. The Claude Code edition
retains its four commands, six skills, and four registered specialist agents.
Its model recommendation is Opus at high reasoning; see the
[Claude Code runtime notes](plugins/study-kit/docs/runtime.md).

### Codex

The commands below were tested for GitHub and downloaded-folder installation,
followed by an actual `study-start` invocation in a fresh Codex CLI session.
Desktop **Plugins** menu installation is documented by OpenAI but has not yet
been verified in this environment; see the guide before choosing that route.

To ask for help from a **local Codex task**, paste:

> Install the Codex edition of Study Kit from https://github.com/H-Hur/study-kit.
> Check whether the Codex plugin CLI is available, register the marketplace, and
> install study-kit-codex@study-kit. Preserve my other installed plugins and
> settings. Verify installation and tell me how to start it in a new task.

This asks the agent to perform setup using available tools; it is not a built-in
chat installation command. The
[downloaded-folder guide](docs/desktop-install.md#download-and-install-files)
distinguishes the tested CLI route from the unverified CLI-free menu route.

Run these in a terminal with a Codex CLI that supports `codex plugin`:

```bash
codex plugin marketplace add H-Hur/study-kit
codex plugin add study-kit-codex@study-kit
```

Start a new Codex conversation after installation. Select `study-start` from the
Study Kit skills, or ask it to start a course of study. Codex receives the six
shared skills plus skill versions of the four commands and four specialist roles.
The generated package is named `study-kit-codex`; its display name is **Study Kit**.

For judgment, writing, and audits, recommend GPT-6 Astra with High reasoning;
GPT-5.6 Sol with High is the alternative. Respect the learner's selected model.
These are recommendations, not a measured comparison of Study Kit outcomes.
See the [Codex runtime notes](plugins/study-kit-codex/docs/codex-runtime.md) for
skill discovery, delegation inputs, write boundaries, and result collection.

For local testing, updates, dependencies, and publishing, see
[`docs/distribution.md`](docs/distribution.md).

### Begin studying

Then tell it what you are after, in this shape:

> I work in ⟨the field you already know⟩. I want to learn ⟨the adjacent field⟩ well
> enough to ⟨the thing you must be able to do when it is over⟩.

The third slot is the one that matters. State it as a capability, not as a topic — that
sentence is what the whole course is worked backward from. It will ask for the rest and
build the course from there.

## What is in it

**Entry points** — Claude Code commands, also available as Codex skills with the
same names (`study-start`, `study-session`, `study-publish`, `study-review`)

| Claude Code command | Codex skill | When |
|---|---|---|
| `/study-kit:study-start` | `study-start` | Beginning a new course of study |
| `/study-kit:study-session` | `study-session` | Preparing the next session |
| `/study-kit:study-publish` | `study-publish` | Revising and publishing the textbook |
| `/study-kit:study-review` | `study-review` | Auditing comprehension |

**Skills** — work that requires talking with the learner. The conductor (the main
session) carries these out directly.

| Skill | What it does |
|---|---|
| `learner-intake` | Asks the learner five things and builds a profile |
| `source-index` | The four beats: seed → acquire → check against the original → graded index |
| `curriculum-design` | Works backward from the target capability to sessions, planting a diagnostic drill in each |
| `textbook-authoring` | Writes the dual-audience textbook and manages its editions |
| `textbook-revision` | Turns the learner's questions into drafted revisions and stacks them |
| `textbook-publish` | Produces two PDF editions, exercise and answer |

**Specialist roles** — Claude Code agents and Codex skills. These handle work with a
lot to read where only the conclusion is needed. In Codex, each specialist skill
requests bounded delegation when an independent task and useful main-session work
can run together. The worker receives the installed procedure, study directory,
inputs, write scope, and required result; the main conversation collects and
integrates the result. When delegation is unavailable or not useful, the same
procedure runs directly. These skills do not automatically register named Codex
custom agents or change the user's agent configuration.

| Agent | What it does |
|---|---|
| `source-scout` | Acquires, verifies, and normalizes sources, then lists them in the index |
| `drill-designer` | Designs review questions and diagnostic drills |
| `textbook-auditor` | Checks the textbook against the conventions and the style rules |
| `comprehension-auditor` | Finds concepts the learner has not grasped, with evidence, from the conversation record |

**Templates** — the skeleton of a new study project, and the textbook master

- `docs/method.md` · `docs/budget.md` — the six stages, and what the work costs
- `templates/` — project rules, work log, toolbox log, return mailbox
- `skills/learner-intake/templates/learner-profile.md` — learner profile
- `skills/source-index/templates/REFERENCES.md` — graded index
- `skills/curriculum-design/templates/curriculum.md` — study plan
- `skills/textbook-revision/templates/textbook-revisions.md` — pending revisions
- `skills/textbook-authoring/templates/textbook-template.html` — textbook master
  (light and dark themes, groundwork boxes, interactive figures, collapsible review
  questions, print typesetting)

## Contributing

**You do not need to write code.** What the kit is worth is the number of places where
somebody followed it and found out where it breaks, and that only comes back from the people
who used it. If a clause did not hold, if a step was missing, if a trap went unwarned — or if
you built your own way of checking whether the study had landed — [send it
back](CONTRIBUTING.md). No study material is collected: the forms ask for the shape of what
happened, with your field left out.

## Why the tools are split the way they are

**Conversation and learner decisions stay in the main session; specialist roles
handle bounded reading and checking.** Intake, converging on a plan, and
the question-and-answer work are all carried out by the conductor as skills. Conversely,
work with a lot to read — collating dozens of sources, combing through a conversation
record — goes to an agent so that the conductor's context is spent elsewhere.
The Codex edition preserves that division of work through skills; it does not depend
on Claude's agent-registration format.

## Where it came from

It came out of one real course of study. The textbook was revised eight times, the
delivery channel was overturned twice, and a body of text was lost once during a
conversion. The traps and judgments left behind by all that are the "measured" passages
in each document. Nothing about that field of study was carried over.

## License

From version **2.0.0**, code is licensed under **PolyForm Noncommercial 1.0.0**;
documents and prompts are licensed under **CC BY-NC-SA 4.0**. These apply to different
components, not as a choice. Noncommercial use, modification, and redistribution
are permitted under the respective terms. Commercial use outside those grants,
including adapting protected kit material into a commercial online service,
requires separate prior permission from the maintainer.

See the [license scope and permission process](plugins/study-kit/LICENSE) and the
bundled [code license](plugins/study-kit/licenses/PolyForm-Noncommercial-1.0.0.txt)
and [content license](plugins/study-kit/licenses/CC-BY-NC-SA-4.0.txt). PolyForm's
express permissions for listed organizations remain applicable. Previously
published material through 1.3.0 retains its existing MIT permissions. This is a
source-available distribution with noncommercial restrictions.
