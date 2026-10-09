# Selected editing roles and optional alternatives

Source check — 2026-10-09. This is a shortlist, not an installation requirement or
an endorsement based on comparative editing tests. Recheck upstream availability,
host support, and installation instructions when selecting a tool. Nothing listed
here is bundled or automatically installed by Study Kit.

## User-selected grammar agent and recommended style skill

Ask the user to choose one of these grammar agents during the initial style discussion,
or before the first grammar pass if no choice is recorded. Neither is preselected.
Both are called `proofreader`, so record the owner and exact source URL, not only the
agent name. Reuse the recorded choice until the user changes it.

| Grammar candidate | GitHub definition | Behavior to explain to the user |
|---|---|---|
| njjenkins — `proofreader` | [Agent file](https://github.com/njjenkins/claude-code/blob/main/.claude/agents/proofreader.md) · [Repository](https://github.com/njjenkins/claude-code) | Academic lecture material reviewer; reports grammar, typos, and consistency findings. Its slide-specific checks need to be scoped to the actual textbook. |
| Daniel Rosehill — `proofreader` | [Agent file](https://github.com/danielrosehill/Claude-Content-Writing-Plugin/blob/master/agents/proofreader.md) · [Repository](https://github.com/danielrosehill/Claude-Content-Writing-Plugin) | Minimal-intervention grammar/spelling edits that preserve terminology and voice; its workflow produces a revised copy. |

Use **American English (en-US)** explicitly in the task contract for either candidate;
this is Study Kit's required setting, not a claimed upstream default. Preserve direct
quotations, proper names, official titles, and established technical terminology.
Resolve actual host availability before execution. Neither agent is bundled here,
and the definition links do not establish an installed Codex-compatible agent.

For njjenkins, collect findings and integrate accepted changes in the main session.
For Daniel Rosehill, use a separate working copy and review the diff before integrating;
do not allow its direct-edit/versioning workflow to overwrite the authoritative source
or independently publish an edition. Preserve Study Kit's revision/publication trigger.

For sentence style, recommend Strunk's **`writing-clearly-and-concisely`**, linked below.
Once a grammar agent is chosen, use it with that skill for requested/scheduled editing
and the three-skipped-edition recommendation. Do not silently replace the chosen agent
or install anything as part of recording the selection.

## Recommended installation: writing-clearly-and-concisely

Recommend installing **`writing-clearly-and-concisely`**, the sentence-style skill
based on Strunk's *The Elements of Style*.

- Git repository: [obra/the-elements-of-style](https://github.com/obra/the-elements-of-style).
- Skill definition: [SKILL.md](https://github.com/obra/the-elements-of-style/blob/main/skills/writing-clearly-and-concisely/SKILL.md).

At project setup, check whether the skill is available. If absent, recommend installing
it and provide the repository link. Follow the repository's current installation guide
for the active host rather than invent a command. This recommendation does not install
anything automatically or make the skill a bundled dependency. If the user defers,
record it as unavailable and continue work that does not require that skill. Do not
repeat the installation recommendation each edition after the user has deferred it.

Installation recommendation recorded — 2026-10-09.

## Agent plugins and skills

| Candidate | Recommended use | Host support stated upstream | Selection notes |
|---|---|---|---|
| [The Elements of Style — writing-clearly-and-concisely](https://github.com/obra/the-elements-of-style) | First candidate for clear English explanations, usage, punctuation, and concise technical prose | Repository provides Claude Code and Codex installation guides | Based on Strunk's 1918 text. Treat its rules as suggestions subordinate to the project's terminology and teaching needs; preserve necessary explanations and qualifications. |
| [Humanizer](https://github.com/blader/humanizer) | Optional second pass for repetitive, inflated, or formulaic prose | Repository documents a Claude Code plugin and a Codex skill installation | A style-focused editor, not a substitute for a full grammar/English review or citation checking. Keep technical prose neutral and preserve factual meaning. |

These recommendations follow the maintainers' documented purposes, not a claim that
one produces objectively better manuscripts. Follow each repository's current guide;
do not assume a Claude plugin command works in Codex or that a skill is already installed.
Do not run an editor on every write merely because its own general trigger is broad:
Study Kit's recorded editing schedule and the user's instructions govern this project.

## Word-side grammar tools

These are document-editor integrations, not confirmed callable Study Kit/agent plugins.
Choose one when the user wants to review a DOCX in Word and accept suggestions there.

| Candidate | Recommended use | Verified integration reference |
|---|---|---|
| [LanguageTool](https://languagetool.org/word) | Grammar, spelling, and wording suggestions in a Word workflow; check support for the document language | [Maintainer's Word add-in instructions](https://help.languagetool.org/en/articles/311205-can-i-use-languagetool-with-microsoft-word) |
| [Grammarly](https://www.grammarly.com/microsoft-word) | English grammar and clarity review while working in Word | [Maintainer's desktop installation guide](https://support.grammarly.com/hc/en-us/articles/360047727871-How-to-install-Grammarly-on-a-desktop-computer); use the current desktop integration rather than assuming a legacy Office add-in |

The available ChatGPT plugin directory search did not return relevant grammar tools
for the queried names at this check. That is not proof none exist; the
[plugin directory](https://chatgpt.com/plugins) can change. Word integration does not
establish agent API access. Do not claim an automated pass ran when only a manual
integration is available. Preserve user edits through the direct-edit reconciliation
procedure when a Word-side tool is used.

## How to offer the shortlist

At the initial style discussion, ask the user to choose between the two grammar
agents unless a choice is already recorded. Record its owner, source URL, and en-US
setting alongside the recommended Strunk skill; do not ask again after selection. At three skipped editions, recommend a pass with the same roles.
Offer the alternatives in this list only when the user requests a change. No tool is
automatically installed, and installation does not establish that a review ran.

Record the selected name, host, actual installation/availability, reviewed scope, and
outcome. Installation and sending text to an external service are separate actions
from choosing a recommendation; proceed only within the user's authorization. Keep
source claims, quotations, numbers, citations, heading hierarchy, caption placement,
and equation/table labels intact, and verify factual rewrites afterward.

The skipped-edition counter resets only after an actual manuscript-wide grammar/language
pass. Selecting or installing a tool, accepting a few suggestions, or running only
Humanizer's style pass does not reset it. A user-completed full review may count when
they confirm its scope; record it as user-reported rather than agent-verified.


## Correction order

After content corrections, run `writing-clearly-and-concisely` first. Integrate its
accepted changes, then run the user-selected grammar agent on that resulting manuscript
in American English (en-US). Complete final audit afterward. Do not run the two editing
passes in parallel. This order does not change the on-request/scheduled editing policy.


## Installation and configuration: terminology precedence

When installing or configuring either `writing-clearly-and-concisely` or the selected
`proofreader`, carry the following contract into the study project's persistent
instructions and any supported project-level configuration for that agent/skill:

> For technical terminology and its customary phrasing, first consult the collected
> textbooks and guidebooks/handbooks issued by professional institutions in this field.
> Follow their context-appropriate usage before generic sentence-style preferences,
> everyday synonyms, or grammar-checker suggestions. Use the project's selected
> terminology references and glossary consistently. Preserve distinctions, definitions,
> and qualifications; flag conflicting conventions instead of silently replacing them.
> American English applies to general prose, while direct quotations, official names,
> and established technical expressions retain their source-appropriate forms.

Apply this contract to **both** the sentence-style skill and grammar agent, not only
to textbook authoring. Record the actual project paths for the source index, glossary
or terminology guide, and relevant original textbook/handbook passages (edition and
page/section). If sources have not been collected yet, record that pending input and
resolve it when available; do not invent references or treat general model knowledge
as a collected source.

Use supported project instructions or configuration rather than editing managed plugin
cache files that updates replace. If a tool has no persistent project override, save
the contract in the project's instructions and pass it explicitly in every invocation
with the relevant source excerpts or accessible paths. A delegated grammar agent must
receive those materials; do not assume it inherits the main conversation's context.
Verify that both roles can access the contract and references before claiming setup is
complete. After an update, recheck the configuration used by the installed version.

At invocation, ask each role to justify proposed changes to technical expressions
against those references and leave unsupported substitutions unapplied. The main
session checks the proposed edits or diff. Source conventions do not make surrounding
grammar immune to correction: fix grammar while preserving the technical meaning.
Installing/configuring these tools still requires the user's authorization; this
section defines the configuration to apply when that action is authorized.


During installation/configuration, connect both editing roles to the project's
`docs/editing-conflicts.md` under the [conflict-record procedure](editing-conflicts.md).
Create it from the supplied template if absent; preserve existing records on updates.
Load relevant confirmed exceptions with source evidence before each pass, and route
new conflicts back to the main session for validation. External tools without this
input capability require manual suggestion review against the record.
