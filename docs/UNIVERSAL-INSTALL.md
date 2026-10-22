# Universal agent installation and updates

Use this same text in Claude Code, Codex or OpenCode with repository/filesystem access:

> Install the Secure Coding Agent Skill from https://github.com/ruma-lk/secure-coding-agent-pack . Identify my agent and OS, inspect the repository and SKILL.md, install the complete skills/secure-coding folder in the correct user-level skills directory, preserve existing files, verify installation and report how to invoke it. If it exists, review changes and update safely. Do not run remote scripts blindly. Ask before enabling scheduled unattended updates.

## Native install paths

| Agent | User/global skill directory | Project skill directory |
|---|---|---|
| Claude Code | `~/.claude/skills/secure-coding/` | `.claude/skills/secure-coding/` |
| Codex | `~/.agents/skills/secure-coding/` | `.agents/skills/secure-coding/` |
| OpenCode | `~/.config/opencode/skills/secure-coding/` | `.opencode/skills/secure-coding/` |

OpenCode also scans the Claude-compatible and agent-compatible locations in its documented configurations. Do not install the same skill multiple times for a single agent unless explicitly requested.

## Safer updating
1. Fetch the remote Git reference and compare with the pinned/installed commit.
2. Review changes to SKILL.md, references, scripts and instructions; do not execute scripts from unreviewed revisions.
3. For an update, replace **only** the secure-coding skill directory with verified contents; preserve other skills and settings.
4. Back up the prior skill and rollback if validation fails.
5. Restart the agent session for skill discovery when necessary.
6. Report source, version/commit SHA, destination and verification outcome.

**Automatic unattended execution is opt-in**, not triggered just by installing a skill. Agents cannot monitor a GitHub repository while inactive. For automatic checks configure the OS-native scheduler (cron/systemd timer/launchd/Windows Task Scheduler) or an agent-native startup mechanism, and always obtain explicit approval first. Treat main-branch instructions as supply-chain executable authority; prefer protected releases/tags or commit pins for production use.

## Native options
- Codex has `$skill-installer` for installing remote skills; pass the GitHub directory link to the installer if available.
- Other agents can clone/fetch the repository and copy the folder to the discovery directory.
- A GitHub URL in a normal agent chat is an **installation instruction**, not a universal built-in URL-install API.
- Official references: https://learn.chatgpt.com/docs/build-skills , https://docs.opencode.ai/docs/skills/ , https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview
