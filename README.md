# Secure Coding Agent Pack

Reusable security-first instructions for Claude Code, Codex and coding agents working with React, Laravel, Node.js, PHP, Python, Java, Go, Ruby, React Native, Flutter, and mixed stacks.

> Starter security policy and checks, **not a security guarantee**. Combine with CI, least-privilege permissions, peer review and penetration testing.

## Contents
- `skills/secure-coding/SKILL.md` — main skill
- `skills/secure-coding/references/` — stack-specific policies
- `templates/CLAUDE.md`, `templates/AGENTS.md` — project instructions
- Stack references: Python, Java, Go, Ruby, React Native and Flutter
- `scripts/security_check.py` — optional read-only scanner
- `INSTALL.md` — installation steps

## Install from GitHub (Windows PowerShell)

```powershell
git clone https://github.com/ruma-lk/secure-coding-agent-pack.git "$env:TEMP\secure-coding-agent-pack"
New-Item -ItemType Directory -Force "$env:USERPROFILE\.claude\skills" | Out-Null
Copy-Item "$env:TEMP\secure-coding-agent-pack\skills\secure-coding" "$env:USERPROFILE\.claude\skills\secure-coding" -Recurse -Force
```

Restart Claude Code and use `/secure-coding`.

To update: run `git -C "$env:TEMP\secure-coding-agent-pack" pull`, and repeat the copy. Existing installed skills do not automatically update.

## Project install
Copy `skills/secure-coding` to `.claude/skills/secure-coding` in the target project. Merge the provided `CLAUDE.md` with existing instructions; never overwrite existing security rules.

For Codex and other agents, adapt their skill discovery paths and merge `templates/AGENTS.md` into the project root.

## Run checks
```powershell
python scripts/security_check.py PATH_TO_PROJECT
```

A missing scanner is **NOT RUN**, not a pass. Branch protection, human review, dependency/secret scanning and negative authorization tests remain essential.
