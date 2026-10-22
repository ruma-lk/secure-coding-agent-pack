# Update only the secure-coding skill from the trusted configured GitHub repo.
# Run with normal user permissions. Requires git and access to GitHub.
[CmdletBinding()]
param(
    [string]$RepositoryPath = (Join-Path $HOME "secure-coding-agent-pack"),
    [string]$SkillDestination = (Join-Path $HOME ".claude\skills\secure-coding"),
    [string]$Branch = "main"
)
$ErrorActionPreference = "Stop"
$remote = "https://github.com/ruma-lk/secure-coding-agent-pack.git"
if (-not (Get-Command git -ErrorAction SilentlyContinue)) { throw "Git is required." }
if (-not (Test-Path -LiteralPath $RepositoryPath -PathType Container)) {
    git clone --branch $Branch --single-branch $remote $RepositoryPath
    if ($LASTEXITCODE -ne 0) { throw "Clone failed." }
}
$actualRemote = (git -C $RepositoryPath remote get-url origin).Trim()
if ($LASTEXITCODE -ne 0 -or $actualRemote -ne $remote) {
    throw "Unexpected repository origin. Refusing to update: $actualRemote"
}
$actualBranch = (git -C $RepositoryPath branch --show-current).Trim()
if ($actualBranch -ne $Branch) { throw "Unexpected local branch: $actualBranch" }
$dirty = @(git -C $RepositoryPath status --porcelain)
if ($LASTEXITCODE -ne 0 -or $dirty.Count -ne 0) {
    throw "Local repository modifications detected. Refusing automatic update."
}
git -C $RepositoryPath pull --ff-only origin $Branch
if ($LASTEXITCODE -ne 0) { throw "Fast-forward update failed; installed skill unchanged." }
$source = Join-Path $RepositoryPath "skills\secure-coding"
$entry = Join-Path $source "SKILL.md"
if (-not (Test-Path -LiteralPath $entry -PathType Leaf)) { throw "Source skill missing SKILL.md" }
$parent = Split-Path -Parent $SkillDestination
New-Item -Path $parent -ItemType Directory -Force | Out-Null
$stage = Join-Path $parent ("secure-coding.stage." + [guid]::NewGuid().ToString("N"))
$backup = Join-Path $parent ("secure-coding.backup." + [guid]::NewGuid().ToString("N"))
$hadPrevious = Test-Path -LiteralPath $SkillDestination
try {
    Copy-Item -LiteralPath $source -Destination $stage -Recurse -Force
    if (-not (Test-Path -LiteralPath (Join-Path $stage "SKILL.md"))) { throw "Staged skill invalid" }
    if ($hadPrevious) { Move-Item -LiteralPath $SkillDestination -Destination $backup }
    try {
        Move-Item -LiteralPath $stage -Destination $SkillDestination
        Write-Host ("Secure coding skill updated to " + (git -C $RepositoryPath rev-parse --short HEAD))
        if ($hadPrevious) { Remove-Item -LiteralPath $backup -Recurse -Force }
    } catch {
        if (Test-Path -LiteralPath $SkillDestination) { Remove-Item -LiteralPath $SkillDestination -Recurse -Force }
        if (Test-Path -LiteralPath $backup) { Move-Item -LiteralPath $backup -Destination $SkillDestination }
        throw
    }
} finally {
    if (Test-Path -LiteralPath $stage) { Remove-Item -LiteralPath $stage -Recurse -Force }
}
