#!/usr/bin/env python3
"""Read-only local security checks. Does not install dependencies or automatically fix issues."""
import argparse
import pathlib
import shutil
import subprocess
import sys

def run(name, cmd, cwd):
    if not shutil.which(cmd[0]):
        return name, "NOT RUN", f"Missing tool: {cmd[0]}"
    try:
        p = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, timeout=120, stdin=subprocess.DEVNULL)
        return name, ("PASS" if p.returncode == 0 else "FINDINGS/ERROR"), (p.stdout + "\n" + p.stderr)[-8000:]
    except (OSError, subprocess.TimeoutExpired) as exc:
        return name, "NOT RUN", str(exc)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("project", nargs="?", default=".")
    args = ap.parse_args()
    p = pathlib.Path(args.project).resolve()
    if not p.is_dir():
        print("Not a directory")
        return 2
    checks = []
    if (p / "package-lock.json").exists() or (p / "npm-shrinkwrap.json").exists():
        checks.append(("npm audit", ["npm", "audit", "--audit-level=high", "--ignore-scripts", "--no-fund"]))
    elif (p / "package.json").exists():
        print("NOTE: JavaScript manifest without npm lockfile; audit with your actual package manager. NOT RUN.")
    if (p / "composer.lock").exists():
        checks.append(("composer audit", ["composer", "audit", "--locked", "--no-interaction"]))
    elif (p / "composer.json").exists():
        print("NOTE: Composer manifest without lockfile; Composer audit NOT RUN.")
    if shutil.which("gitleaks") and (p / ".git").exists():
        checks.append(("gitleaks directory", ["gitleaks", "dir", "--source", ".", "--no-banner"]))
    else:
        print("NOTE: Gitleaks missing or .git absent; secrets scan NOT RUN.")
    if shutil.which("semgrep"):
        checks.append(("semgrep", ["semgrep", "scan", "--config", "auto", "--error", "--quiet", "."]))
    else:
        print("NOTE: Semgrep missing; SAST NOT RUN.")
    if not checks:
        print("All automated checks NOT RUN.")
        return 0
    failed = False
    for name, cmd in checks:
        label, status, output = run(name, cmd, str(p))
        print(f"\n## {label}: {status}\n{output}")
        if status != "PASS":
            failed = True
    return 1 if failed else 0

if __name__ == "__main__":
    sys.exit(main())
