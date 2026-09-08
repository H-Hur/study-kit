# Desktop installation test — 2026-09-08

Package under test: Study Kit 2.0.0 from the public `H-Hur/study-kit` main branch.
Environment: macOS; Codex CLI 0.153.4; Claude Code CLI 2.1.260;
Claude desktop 1.46388.3. The initial documentation-only deployment was `ff09b21`.
This follow-up records actual tests and corrects claims that exceeded coverage.

| Test | Result | Evidence |
|---|---|---|
| Codex GitHub marketplace registration and install | Passed | CLI returned installed package `study-kit-codex`, version `2.0.0` |
| Codex extracted repository ZIP registration and install | Passed | Actual GitHub main ZIP was extracted, registered by local path, and installed |
| Codex new-session skill execution | Passed in CLI | Fresh `codex exec` outside the kit read `skills/study-start/SKILL.md` from the installed `2.0.0` cache, then runtime/intake instructions, and returned the first two Korean intake questions |
| Codex source switch from GitHub to downloaded folder | Initially failed; recovery passed | Duplicate marketplace name rejected; removing only `study-kit`, registering the local folder, and installing worked; GitHub source was restored afterward |
| Codex desktop menu install and fresh desktop invocation | Blocked | Computer Use explicitly denied control of the Codex application; no alternate UI-control mechanism was used |
| Claude GitHub refresh and update | Passed | Marketplace update succeeded; installed version changed from `1.1.0` to `2.0.0` |
| Claude extracted repository ZIP install | Passed at local scope | Local marketplace registration and `claude plugin install study-kit@study-kit --scope local` succeeded in a separate temporary test folder |
| Claude fresh CLI inference | Blocked | OAuth session expired and could not be refreshed; no login credentials were changed |
| Claude fresh Code desktop invocation | Passed | New Local session in an empty test folder showed the actual `study-kit:study-start` skill tool call, loaded `commands/study-start.md` from the `2.0.0` installed cache, read runtime/method/intake files, and returned the first two Korean intake questions |
| Claude desktop menu navigation | Inspected | `+ → Plugins` showed Study kit; Browse plugins opened Customize; Add plugin offered Add marketplace and Upload plugin |
| Full menu-only installation, either app | Not tested | Inspecting a menu is not an installation test |
| Natural-language installation request, either app | Not tested end to end | Direct CLI operations were tested; the documented agent installation prompts were not executed as fresh installation conversations |
| Plugin-only ZIP / personal marketplace / Cowork | Not tested | These alternatives must not be presented as validated Study Kit workflows |

Both invocation tests requested only the opening intake questions. No learner
profile, curriculum, textbook, or research artifacts were created. Tests did not
validate all learning workflows, PDF conversion, or a complete study session.

The tests installed Codex Study Kit 2.0.0 and updated the existing Claude user
installation to 2.0.0. A separate local-scope Claude install belongs only to the
temporary test folder. Other plugins were not intentionally changed.

## Corrections made from the tests

- Recommend the tested CLI-assisted route; label desktop-only and agent-assisted
  installation alternatives with their actual verification status.
- Use the observed Claude Browse plugins/Customize labels and avoid claiming
  that the catalog's upload control establishes a local Code installation.
- Explain the Codex marketplace-name conflict and explicit source-switch steps.
- Distinguish successful desktop authentication from the separate expired CLI
  inference session; do not tell users every install failure is a package defect.
