# One repository, two hosts

Both editions ship in the same GitHub commit, tag, and release version. The existing
Claude Code package is the maintained source; the Codex package is a generated
adaptation. Users install the edition for their host without running a build.

| Host | Marketplace | Package | Version source |
|---|---|---|---|
| Claude Code | `.claude-plugin/marketplace.json` | `plugins/study-kit/` | `plugins/study-kit/.claude-plugin/plugin.json` |
| Codex | `.agents/plugins/marketplace.json` | `plugins/study-kit-codex/` | Generated from that same version |

The marketplace is named `study-kit` in both hosts. The Codex plugin identifier is
`study-kit-codex` so its generated directory and manifest name agree; its displayed
name is Study Kit. No second repository or independently maintained release is needed.

## Install and update

For desktop menus, agent-assisted chat requests, downloaded repository installs,
and the distinction between Claude Code and Cowork, use the
[desktop installation guide](desktop-install.md). Desktop guidance was checked
against official host documentation on 2026-09-08. The commands below remain the
CLI route.

The GitHub commands below become available after the commit containing the Codex
marketplace and generated package is published to the repository's default branch.

Claude Code:

```text
/plugin marketplace add H-Hur/study-kit
/plugin install study-kit@study-kit
```

Codex, from a terminal:

```bash
codex plugin marketplace add H-Hur/study-kit
codex plugin add study-kit-codex@study-kit
```

For an already configured GitHub marketplace, refresh its snapshot and reinstall:

```bash
codex plugin marketplace upgrade study-kit
codex plugin add study-kit-codex@study-kit
```

For a local checkout, use its repository root as the marketplace source:

```bash
codex plugin marketplace add /absolute/path/to/study-kit
codex plugin add study-kit-codex@study-kit
```

Use `codex plugin marketplace list` to see which source the name resolves to before
switching between local and GitHub testing. Start a new conversation after installing
or updating. If `codex plugin` is unavailable, update the Codex CLI to a version that
provides plugin management.

## What is adapted

Both editions remain install targets in this repository. The shared procedures
read `docs/runtime.md` in Claude Code; the generator maps that document and its
links to `docs/codex-runtime.md`, sourced from `codex/runtime.md`, for Codex.
Claude commands, agent definitions, tool lists, and runtime guidance remain in
the Claude package. Codex users receive host-specific execution instructions.

The generator retains the six skills and their templates and references, turns the
four commands and four specialist agents into eight additional skills, and rebases
the Markdown links to the resulting layout. It removes Claude's `tools` and
`argument-hint` frontmatter from the converted files.

The Codex edition resolves package files from the installed skill path, creates
`AGENTS.md` in the learner's project, and uses available conversation evidence or
exports instead of assuming Claude's session-storage path. Original model-specific
cost measurements remain attributed to Claude; they are not Codex measurements.
The full runtime adaptation is in [`../codex/runtime.md`](../codex/runtime.md).

Codex's four specialist skills are executable procedures for available subagents,
not automatically registered named custom agents. No `.codex/agents/` installation
or global configuration change is needed for the normal skill-and-subagent route.
The runtime defines inputs, output ownership, model inheritance, independent-work
conditions, result collection, and direct execution when delegation is unavailable.
Each entry links to its host runtime, and bare procedure references in Codex become
links to installed skills. Intake and learner decisions remain in the main session.

The Claude recommendation remains Opus at high reasoning. Codex recommends Astra
High, with Sol High as an alternative and Extra High for particularly difficult
reasoning. These recommendations respect the learner's selected model and do not
alter model settings merely by loading a skill. Historical token estimates and
archived operating rules are retained, but do not become fixed limits in either
host. They are separate from current instructions to save bounded work and follow
actual runtime limits.

There is no bundled MCP server or account authentication. PDF conversion requires
a Chrome-compatible browser and Poppler/PyMuPDF, or an equivalent host PDF workflow.
DOCX output uses an available document tool or Pandoc with a reference document,
plus Word or a compatible renderer for layout verification. DOCX-only output is supported.
Messaging and scheduled follow-ups require separately available tools and the
learner's request. The plugin can return the HTML master and generated files in the
conversation when those optional tools are absent.

## Build and release

The generator requires Python 3.9 or newer and no third-party packages.

1. Edit the shared source or the Codex adaptation, and raise the source plugin's
   version for a release affecting either edition.
2. Generate and check the Codex edition:

   ```bash
   python3 scripts/build_codex.py
   python3 -m unittest discover -s tests -v
   python3 scripts/build_codex.py --check --archive
   ```

3. Review the changed source and generated package together. Commit both packages,
   both marketplace catalogs, and the shared documentation in one commit. Tag that
   commit with the common version, for example `v1.2.0`.
4. Publish that commit/tag to GitHub. GitHub-based installations read the committed
   package directly. The optional `dist/study-kit-codex-<version>.zip` contains just
   the Codex plugin and its license and may be attached to the same GitHub release.

`--check` fails on stale generated files, missing bundled links or host runtime
references, absent specialist execution contracts, unconverted Claude paths or
frontmatter, invalid skill names, or an unexpected number of skills. Regression
checks cover relocated installs, workflow links, role handoffs, both model guides,
historical budget attribution, and preservation of the Claude package. The archive is built
from the same validated files with stable ordering and timestamps. CI runs the
check on pushes and pull requests; it does not publish releases automatically.

After installing a release in a new conversation, check these workflows against a
separate scratch study project: start an intake without an existing profile, prepare
a session from a supplied plan, audit a chapter against the bundled style rules,
review only the conversation evidence actually provided, and produce the two PDF
editions when the conversion dependencies are present. Package validation alone
does not establish the quality of a complete learning session.

## Public OpenAI directory

Repository distribution is separate from a listing in the public directory shared
by ChatGPT and Codex. Public listing goes through the OpenAI submission portal and
review; publishing this repository does not create that listing. For a public
submission, use the generated ZIP, review the skills-only path, and supply the
publisher identity, listing assets, policy URLs, and test cases requested there.
This kit uses local files and conversion tools, so confirm the applicable review
path for local execution before making claims about availability on other surfaces.

The packaging decisions were checked on 2026-09-06 against official OpenAI documentation:

- [Models](https://learn.chatgpt.com/docs/models)
- [Subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents)
- [Package your plugin](https://developers.openai.com/plugins/build/plugins)
- [Submit a Claude Code plugin](https://developers.openai.com/plugins/guides/submit-claude-plugin)
- [Submit plugins](https://developers.openai.com/plugins/deploy/submission)

## Version 2.0.0 — licensing and intended use (2026-09-08)

This release changes the offered license terms: code uses PolyForm Noncommercial
1.0.0; documents and prompts use CC BY-NC-SA 4.0. The manifest expression uses AND
because each license governs its assigned components, not because recipients may
choose either license for any file. See the [scope notice](../plugins/study-kit/LICENSE).
Prior MIT permissions for previously published material remain in effect.

The maintained notice and official license texts live in `plugins/study-kit/LICENSE`
and `plugins/study-kit/licenses/`. The generator copies them unchanged into the
Codex package and archive, so both installed editions retain their terms without
needing the repository root. Keep these texts intact when redistributing. Edit
licensing sources only in the maintained package and regenerate Codex.

The introduction now explains the intended use: quickly orient yourself in an
adjacent field when time does not permit an entire textbook and all its exercises,
skipping familiar material and focusing on the target capability. This clarifies
the existing scope; it does not add a measured learning-speed claim.


## Version 2.1.0 — publication feedback (2026-10-09)

Issues #2, #3, #5, #6, and #9 are incorporated in the maintained learning procedures
and generated Codex package: separate conversation/document language contracts;
queued corrections and recorded publication triggers; immutable timestamped edition
folders and edition READMEs; selectable PDF/DOCX formats; and Windows conversion
fallbacks with explicit UTF-8 and bounded Word automation. These changes document
reported workflow failures; they do not claim a new end-to-end Windows validation run.

Issue #1 now uses learning and authoring modes inside one plugin, per the user's
decision: see [the authoring scope decision](authoring-scope.md).
Issues #4, #7, #8, and #10 are implemented after the revised
[feedback review](feedback-review.md): direct-edit reconciliation, source/derivation
evidence, safe reference renumbering, and a recorded language-editing policy.
Mode intake now asks personal learning versus teaching first; teaching records both
instructor and learner levels, then selects instructor-bounded content or a bounded
researched extension. These changes remain part of the 2.1.0 release.


Document editing update — 2026-10-09 (included in the 2.1.0 release):
headings use title phrases and hierarchical numbers; figure captions follow figures,
table captions precede tables; object/caption blocks have one body line of separation
from prose; table headers and first-column data cells receive column/row prefixes.
The shared style guide, HTML template, project template, DOCX procedure, and auditor
carry the same rules. The three key summary sentences remain complete sentences.

Equation numbering update — 2026-10-09: only standalone display equations receive
parenthesized numbers at the far right; inline mathematics remains unnumbered.
Shared authoring, project instructions, HTML template, DOCX conversion, and audit
rules carry this requirement in the 2.1.0 release.


Publication review update — 2026-10-09: every updated edition checks numbering and
citations before publication. Grammar/English polishing is not required each time;
a recorded count triggers a recommendation at three consecutive skipped editions.
Counts advance only for successful editions and reset after a full editing pass.
This remains part of the 2.1.0 release.


Editing-tool shortlist — 2026-10-09: the shared package now carries optional agent
plugin/skill recommendations (Elements of Style, Humanizer) and separately identified
Word integrations (LanguageTool, Grammarly), with upstream sources and availability
limits. Intake and skipped-editing recommendations can use this list. No tool is
bundled or installed; a style-only pass does not reset the grammar-review counter.
Included in the 2.1.0 release.


Terminology update — 2026-10-09: original textbooks and professional institutions'
handbooks/guidebooks are the first references for technical usage and expression
conventions. Source collection, authoring, language editing, audit, and project
instructions now preserve those conventions and record their source locations.
Included in the 2.1.0 release.


Editor selection — 2026-10-09: the user selected `english-proofreader` for English
grammar and Strunk-based `writing-clearly-and-concisely` for sentence style. Intake,
project instructions, editing policy, recommendations, and edition records now use
that pairing. They remain external dependencies whose availability must be verified;
no installation or executed editing pass is claimed. Existing cadence is unchanged.
Included in the 2.1.0 release.


Style-skill installation recommendation — 2026-10-09: project setup now recommends
`writing-clearly-and-concisely` when absent and links to its Git repository,
[obra/the-elements-of-style](https://github.com/obra/the-elements-of-style). The bundled
editing-tool reference retains both the repository and skill-definition links. No
automatic installation is performed. Included in the 2.1.0 release.


Grammar-agent selection update — 2026-10-09: supersedes the earlier unresolved
`english-proofreader` designation. Users choose njjenkins's or Daniel Rosehill's
`proofreader`, with both exact GitHub definition links saved in the bundled tool
reference. Project records identify the owner/source and require American English
(en-US). No agent is preselected or installed. The recommended Strunk skill and
three-skipped-edition policy remain unchanged. Included in version 2.1.0.


Correction-order clarification — 2026-10-09: content corrections precede
`writing-clearly-and-concisely`; the selected grammar agent then checks the resulting
manuscript in American English, followed by final audit. Passes are sequential.
Included in the 2.1.0 release.


Editing-tool configuration update — 2026-10-09: installation/configuration instructions
now carry collected textbooks and professional-institution guidebook/handbook usage
precedence into both the Strunk style skill and the selected grammar agent. Persistent
project settings or explicit invocation contracts supply the reference paths and
passages; managed plugin caches are not patched. Included in version 2.1.0.


Recurring editing-conflict update — 2026-10-09: study projects now retain a scoped,
source-backed exception ledger at `docs/editing-conflicts.md`. Style and grammar
passes receive confirmed entries in sequence; the main session validates new cases
and records deduplicated recurrence history. Audits detect regressions, and changed
source conventions trigger revalidation rather than permanent blanket exemptions.
The package supplies the empty template and procedure; no learner data is bundled.
Included in the 2.1.0 release.
