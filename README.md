# Secure Coding Agent Pack

**Security-first coding skills for Claude Code, OpenAI Codex, OpenCode and other compatible agents — Windows, macOS and Linux.**

[Main skill](skills/secure-coding/SKILL.md) · [Security references](skills/secure-coding/references) · [Security checker](scripts/security_check.py)

> This pack provides agent guidance and optional checks, **not a guarantee of security**. Use human review, CI, protected branches and tests before production deployment.

## Install with one prompt — all operating systems

Open **Claude Code, Codex or OpenCode** in a workspace where the agent has terminal/filesystem access. Paste this message:

```text
Install or update the Secure Coding Agent Skill from:
https://github.com/ruma-lk/secure-coding-agent-pack

Detect the current agent (Claude Code, Codex or OpenCode), operating system
(Windows, macOS or Linux), and the correct user-level skill discovery path.

Read the repository README and skills/secure-coding/SKILL.md first.
Fetch only the trusted repository. Install the entire
skills/secure-coding directory, including references, into the appropriate
user-level skills directory without overwriting other skills or settings.

For an existing installation, compare versions, review the changes,
back up the current skill, and update it safely.
Verify SKILL.md and all references exist after installation.
Report the installation path, source commit and how to invoke the skill.

Do not run downloaded scripts blindly, expose secrets, or enable
unattended/scheduled updates without my approval.
```

**Prerequisites:** Your agent must be able to access GitHub and write to its local skill directory. Git may be needed. The prompt is a portable *agent instruction*, not a universal built-in install command; installations may require approving filesystem/terminal actions.

### Install directories (same layout on Windows, macOS and Linux)

The agent chooses the correct home directory and path syntax for your OS:

| Agent | User-level skill path | Project-level skill path |
|---|---|---|
| Claude Code | `~/.claude/skills/secure-coding/` | `.claude/skills/secure-coding/` |
| Codex | `~/.agents/skills/secure-coding/` | `.agents/skills/secure-coding/` |
| OpenCode | `~/.config/opencode/skills/secure-coding/` | `.opencode/skills/secure-coding/` |

`~` means the current user's home directory (including on Windows). To use project scope, ask your agent: **"Install this secure-coding skill only in the current project."** Verify your agent version's discovery conventions if customized.

Restart or start a fresh agent session if it does not immediately discover the skill. In Claude Code, try `/secure-coding`. In other agents, ask: **"Use the secure-coding skill to audit this project."**

## Update via the agent (Windows / macOS / Linux)

Paste into the same coding agent:

```text
Update my installed secure-coding skill using
https://github.com/ruma-lk/secure-coding-agent-pack .
Review upstream differences, preserve unrelated files, back up the old skill,
install the verified version, and report the source commit and changes.
```

Updates to GitHub **do not automatically update your device**. A session can check on demand. Background auto-update requires an explicitly authorized startup hook or OS scheduler (Windows Task Scheduler, macOS launchd, Linux systemd timer/cron). For security-sensitive use, prefer pinned or reviewed releases over silently executing instructions from the latest main branch. Optional legacy Windows-only scripts are available under `scripts/`, but **are not required** for installation.

## Coverage

| Stack | Reference |
|---|---|
| Universal practices | [universal.md](skills/secure-coding/references/universal.md) |
| React | [react.md](skills/secure-coding/references/react.md) |
| Laravel | [laravel.md](skills/secure-coding/references/laravel.md) |
| Node.js | [node.md](skills/secure-coding/references/node.md) |
| PHP | [php.md](skills/secure-coding/references/php.md) |
| Python | [python.md](skills/secure-coding/references/python.md) |
| Java | [java.md](skills/secure-coding/references/java.md) |
| Go | [go.md](skills/secure-coding/references/go.md) |
| Ruby | [ruby.md](skills/secure-coding/references/ruby.md) |
| React Native | [react-native.md](skills/secure-coding/references/react-native.md) |
| Flutter | [flutter.md](skills/secure-coding/references/flutter.md) |
| Rate limits / abuse | [rate-limits-and-abuse.md](skills/secure-coding/references/rate-limits-and-abuse.md) |
| Bounded concurrency / resources | [concurrency-and-resource-safety.md](skills/secure-coding/references/concurrency-and-resource-safety.md) |
| Python threads / workers / asyncio | [python-concurrency.md](skills/secure-coding/references/python-concurrency.md) |

## Security workflow

1. Identify framework, trust boundaries, actors, secrets and attack surface.
2. Threat-model changed flows and enforce server-side authorization and validation.
3. Review authentication, session safety, injection, SSRF, uploads, permissions and dependencies.
4. Check rate limits, worker/thread caps, **bounded task queues**, timeouts, cancellation, retries, backpressure and graceful shutdown.
5. Run applicable unit/integration/security tests and review the diff.
6. Report **PASS / FAIL / NOT RUN**, severity, affected locations and remaining risks.

## Optional local checker

From the cloned repository, run:

```sh
python scripts/security_check.py PATH_TO_PROJECT
```

Some systems use `python3` instead of `python`. The checker runs applicable locally available tools and may invoke dependency auditing; it does not install scanners automatically. **NOT RUN is never PASS.**

## Repository structure

```text
skills/secure-coding/
  SKILL.md
  references/
    universal.md
    react.md  laravel.md  node.md  php.md
    python.md  java.md  go.md  ruby.md
    react-native.md  flutter.md
    rate-limits-and-abuse.md
    concurrency-and-resource-safety.md
    python-concurrency.md
scripts/
  security_check.py
  update-skill.ps1               # legacy, optional Windows helper
  enable-windows-auto-update.ps1 # legacy, optional Windows helper
templates/
  CLAUDE.md
  AGENTS.md
```

**Security note:** Review upstream changes before installing or enabling updates. A coding agent cannot guarantee zero vulnerabilities and does not replace professional security testing.
