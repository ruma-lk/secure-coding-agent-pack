# Register an at-logon update (current user only). No administrator permissions needed.
# Review scripts/update-skill.ps1 and only enable for a repository you trust.
[CmdletBinding()]
param([string]$RepositoryPath = (Join-Path $HOME "secure-coding-agent-pack"))
$ErrorActionPreference = "Stop"
$updater = Join-Path $RepositoryPath "scripts\update-skill.ps1"
if (-not (Test-Path -LiteralPath $updater)) { throw "Clone repo to $RepositoryPath first." }
if (-not (Get-Command Register-ScheduledTask -ErrorAction SilentlyContinue)) {
    throw "Windows ScheduledTasks module is required."
}
$taskName = "SecureCodingSkillUpdate"
$quotedUpdater = '"' + $updater + '"'
$quotedRepo = '"' + $RepositoryPath + '"'
$action = New-ScheduledTaskAction -Execute "powershell.exe" -Argument ("-NoProfile -NonInteractive -File " + $quotedUpdater + " -RepositoryPath " + $quotedRepo)
$trigger = New-ScheduledTaskTrigger -AtLogOn -User ([System.Security.Principal.WindowsIdentity]::GetCurrent().Name)
$settings = New-ScheduledTaskSettingsSet -ExecutionTimeLimit (New-TimeSpan -Minutes 5) -StartWhenAvailable
Register-ScheduledTask -TaskName $taskName -Action $action -Trigger $trigger -Settings $settings -Description "Update secure-coding Claude skill from trusted GitHub repository at sign in" -Force | Out-Null
Write-Host "Registered $taskName. Updates occur after future Windows logins."
Write-Host "To remove: Unregister-ScheduledTask -TaskName '$taskName' -Confirm:\$false"
