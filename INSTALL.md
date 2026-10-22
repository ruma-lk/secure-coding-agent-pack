# Installation

## Windows / Claude Code (global)
Run from PowerShell:
```powershell
git clone https://github.com/ruma-lk/secure-coding-agent-pack.git "$env:TEMP\secure-coding-agent-pack"
New-Item -ItemType Directory -Force "$env:USERPROFILE\.claude\skills" | Out-Null
Copy-Item "$env:TEMP\secure-coding-agent-pack\skills\secure-coding" "$env:USERPROFILE\.claude\skills\secure-coding" -Recurse -Force
```
Restart Claude Code and run `/secure-coding`.

## Project-specific
Copy the skill directory to `PROJECT/.claude/skills/secure-coding` and merge `templates/CLAUDE.md` with your project's instructions.

## Codex
Merge `templates/AGENTS.md` into your project and place the skill where your agent expects skills. Discovery and command conventions vary by tool.

## Update
```powershell
git -C "$env:TEMP\secure-coding-agent-pack" pull
Copy-Item "$env:TEMP\secure-coding-agent-pack\skills\secure-coding" "$env:USERPROFILE\.claude\skills\secure-coding" -Recurse -Force
```

## Scanners
Run `python scripts/security_check.py PATH_TO_PROJECT` after reviewing the script. It may invoke installed scanners and network-backed dependency audits. NOT RUN never means PASS.

Use CI, protected branches, peer review and manual risk acceptance for unresolved high-severity issues. Never grant coding agents unreviewed production permissions.

## References
- https://code.claude.com/docs/en/skills
- https://owasp.org/www-project-application-security-verification-standard/
- https://cheatsheetseries.owasp.org/

## Newly supported stacks
The skill includes guides for Python, Java, Go, Ruby, React Native and Flutter under `skills/secure-coding/references/`. Agents choose the applicable reference after detecting the project stack.
