# Install Study Kit in desktop apps

Checked against official documentation on 2026-09-08. These steps cover local
Codex tasks and Claude Code desktop sessions. Menu labels can vary by app version.
The learning project belongs in a separate folder from the downloaded kit.

| Host | Marketplace | Plugin to install | Start in a new conversation |
|---|---|---|---|
| Codex desktop | `study-kit` / Study Kit | `study-kit-codex` / Study Kit | Ask for the Study Kit `study-start` skill |
| Claude Code desktop, Code tab | `study-kit` | `study-kit` | `/study-kit:study-start` |

## Codex desktop

### Desktop menus

1. Open **Plugins** and look for the Study Kit marketplace/source. It is a repo
   marketplace, separate from the public plugin catalog.
2. If the source is missing and the Codex CLI is available, run this in a terminal:

   ```bash
   codex plugin marketplace add H-Hur/study-kit
   ```

3. Restart the desktop app after registering the source. Open **Plugins**, choose
   Study Kit, open **Study Kit** (`study-kit-codex`), and select the install button.
4. Start a new local task in a separate study folder. Ask: "Use Study Kit's
   study-start skill to help me begin a course of study."

A CLI install is also supported when `codex plugin add --help` is available:

```bash
codex plugin add study-kit-codex@study-kit
```

### Ask in chat

In a local Codex task that can run commands, paste:

> Install the Codex edition of Study Kit from https://github.com/H-Hur/study-kit.
> Check whether the Codex plugin CLI is available, register the marketplace, and
> install study-kit-codex@study-kit. Preserve my other installed plugins and
> settings. Verify installation and tell me how to start it in a new task.

The agent needs access to the installation tools and destination directories.
It may need an app permission approval. A natural-language request does not
itself install a plugin: require a successful install result, then check
**Plugins → Installed** and start a new task. If the CLI is unavailable, use the
local marketplace route below; do not paste shell commands as if they were
built-in chat commands.

## Claude Code desktop

### Desktop menus

1. Open Claude desktop's **Code** tab and choose a **Local** session.
2. Open **+ → Plugins → Add plugin**. This lists configured marketplaces.
3. If `study-kit` is absent, register it in a terminal with the Claude Code CLI:

   ```bash
   claude plugin marketplace add H-Hur/study-kit
   ```

4. Reopen the plugin browser (restart the app if necessary), select `study-kit`
   from the `study-kit` marketplace, and install for your user account to use it
   across study projects.
5. Start a new local session in a separate study folder and run
   `/study-kit:study-start`.

To install from the terminal instead of the menu:

```bash
claude plugin install study-kit@study-kit --scope user
```

The README's `/plugin marketplace add` and `/plugin install` examples are
interactive Claude Code CLI commands. Use the `claude plugin ...` shell forms
above in a terminal; do not assume the desktop composer supports every CLI slash
command. The documented desktop plugin browser also supports SSH sessions;
cloud and WSL sessions have different limitations and are outside this guide.

### Ask in chat

In a local **Code** session, paste:

> Install the Claude Code edition of Study Kit from
> https://github.com/H-Hur/study-kit for my user account. Check whether the Claude
> Code CLI is available, register the marketplace, and install study-kit@study-kit.
> Preserve my other plugins and settings. Verify installation and tell me how to
> start /study-kit:study-start in a new local session.

This is an agent-assisted installation request, conditional on tools and
permissions, rather than a guaranteed one-message installer. Confirm the plugin
appears in **+ → Plugins** after installation.

## Download and install files

Download the **whole repository** using
[GitHub → Code → Download ZIP](https://github.com/H-Hur/study-kit), extract it,
and keep the extracted folder in a stable location. Use the folder containing
`README.md`, `.agents/`, `.claude-plugin/`, and `plugins/`; preserve hidden files.
No build step is required. A single README or a chat attachment is not the plugin.

### Codex: downloaded repository

With the CLI, replace the example path with the extracted repository root:

```bash
codex plugin marketplace add "/absolute/path/to/study-kit-main"
codex plugin add study-kit-codex@study-kit
```

Without the CLI, add/open the extracted repository as a local Codex project. It
already contains `.agents/plugins/marketplace.json` pointing to the generated
Codex package. Restart the app, open that project, then use **Plugins** to select
its Study Kit marketplace and install. After installation, start a new task in
an independent study folder.

If you have only the Codex plugin package ZIP, extract it and ask the built-in
`plugin-creator` skill to register the existing plugin folder in a personal
marketplace, preserving existing entries. Restart the app and install from that
source. The repository ZIP is simpler because its marketplace is already included.
Do not manually copy files into the plugin cache.

### Claude Code: downloaded repository

Register the extracted repository using the Claude Code CLI, then install:

```bash
claude plugin marketplace add "/absolute/path/to/study-kit-main"
claude plugin install study-kit@study-kit --scope user
```

Return to the desktop **Code** tab, start a new local session, and check that
`/study-kit:study-start` is available. If the CLI is unavailable, these commands
cannot run; the official Code desktop guide does not establish a ZIP-upload
installer for its local plugin browser.

### Claude Chat and Cowork are separate

Cowork documents **Customize → Plugins**, adding a Git repository marketplace,
and uploading a plugin package. That account-level surface is separate from the
local Claude Code plugin installation. A repository ZIP containing two editions
is not the same as a single Claude plugin package. This kit's Claude edition is
maintained for Claude Code; this guide does not claim that its complete workflow
has been validated in Chat or Cowork.

## Check installation and updates

- Confirm the installed host and package match the table above. A chat reply
  saying it read the README is not installation evidence.
- Start a new conversation after installation. If skills are absent, check that
  the plugin is enabled and that the app uses the same account/local environment
  as the installer.
- If `study-kit` was already registered, inspect the existing source before
  switching between a downloaded folder and GitHub. Use
  `codex plugin marketplace list` or `claude plugin marketplace list`.
- Downloaded folders do not track GitHub updates. Replace/update the source and
  refresh/reinstall through the host. Keep the folder available for future
  refreshes. See [distribution](distribution.md#install-and-update) for Codex
  refresh commands.

## Sources and verification scope

- [OpenAI: Plugins](https://learn.chatgpt.com/docs/plugins): desktop installation
  and starting a new chat.
- [OpenAI: Package your plugin](https://developers.openai.com/plugins/build/plugins):
  Git/local marketplace registration, repo discovery, personal marketplaces.
- [Anthropic: Claude Code desktop](https://code.claude.com/docs/en/desktop#install-plugins):
  Code-tab plugin menus and session limitations.
- [Anthropic: Discover plugins](https://code.claude.com/docs/en/discover-plugins):
  marketplace sources, local paths, installation scopes.
- [Anthropic: Cowork plugins](https://claude.com/docs/cowork/guide/plugins):
  the separate repository and file-upload installation surface.

The package paths and CLI command syntax were checked locally. Menu procedures
are based on the official documentation; this documentation update does not
represent a fresh end-to-end installation test in both desktop apps.
