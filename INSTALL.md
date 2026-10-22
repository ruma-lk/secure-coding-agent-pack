# Installation

**Recommended for all platforms:** See [README.md](README.md#install-with-one-prompt--all-operating-systems). Paste the repository installation prompt into Claude Code, Codex, or OpenCode on Windows, macOS or Linux. The agent chooses its skill directory and performs a verified installation with your permission.

To update, use the [README update prompt](README.md#update-via-the-agent-windows--macos--linux). GitHub changes are not pushed automatically to devices; unattended updates are opt-in and require an OS scheduler or agent startup integration.

The PowerShell helpers in `scripts/` are optional legacy Windows utilities, not the standard installation method.

Run the optional scanner from a local checkout using `python scripts/security_check.py PATH_TO_PROJECT` (or `python3`). A missing scan is NOT RUN, never PASS.
