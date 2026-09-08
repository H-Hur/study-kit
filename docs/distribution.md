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
a Chrome-compatible browser and Poppler, or an equivalent host PDF workflow.
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
