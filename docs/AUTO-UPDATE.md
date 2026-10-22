# Automatic skill updates (Windows)

GitHub updates do not automatically replace locally installed Claude Code skills. This opt-in Windows Task Scheduler setup checks the trusted repository on each sign-in and updates only the installed secure-coding folder.

## Initial setup (PowerShell)
```powershell
git clone https://github.com/ruma-lk/secure-coding-agent-pack.git "$HOME\secure-coding-agent-pack"
& "$HOME\secure-coding-agent-pack\scripts\update-skill.ps1"
& "$HOME\secure-coding-agent-pack\scripts\enable-windows-auto-update.ps1"
```
If already cloned, omit the first command. This assumes the clone resides in `$HOME\secure-coding-agent-pack`; otherwise provide `-RepositoryPath "YOUR_CLONE_PATH"` to both scripts.

## What happens next
Whenever you sign in to Windows, the task checks GitHub main using `git pull --ff-only` and copies the updated `skills/secure-coding` folder into `$HOME\.claude\skills\secure-coding`. Restart Claude Code or start a new session to load changes. The update is not real time and requires network access and read permissions.

## Run now
```powershell
& "$HOME\secure-coding-agent-pack\scripts\update-skill.ps1"
```

## Disable
```powershell
Unregister-ScheduledTask -TaskName "SecureCodingSkillUpdate" -Confirm:$false
```

## Security limits
- This is **opt-in**: registering a scheduled task executes code at login. Review scripts before enabling and only trust reviewed commits. Changes on the tracked main branch can change agent instructions.
- Do not give the update task admin rights; it runs in the logged-in user's context.
- It rejects a changed Git remote, wrong branch, local modifications, or non-fast-forward update. This is not a cryptographic signature check.
- The installer backs up the existing skill folder during replacement and restores it on copy/rename failure. It does not merge local edits inside the installed skill directory.
- Updates are not applied to already-running Claude sessions. Validate skill changes before using for sensitive production projects.
- For stronger protection use protected branches, required review, signed tags, and version pinning instead of automatically trusting all commits to main.
