#!/usr/bin/env python3
"""Cross-platform update for already-installed secure-coding skills. Python 3.9+, git."""
import argparse
import json
import pathlib
import shutil
import subprocess
import sys
import tempfile
import uuid

REMOTE = "https://github.com/ruma-lk/secure-coding-agent-pack.git"
PATHS = {
    "claude": ".claude/skills/secure-coding",
    "codex": ".agents/skills/secure-coding",
    "opencode": ".config/opencode/skills/secure-coding",
}
REQUIRED = ("universal.md", "cache-security.md", "payment-security.md", "esms-security.md")

def git(*args, cwd=None):
    p = subprocess.run(["git", *args], cwd=cwd, capture_output=True, text=True, timeout=120, check=True)
    return p.stdout.strip()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--agents", nargs="+", choices=[*PATHS, "all"], default=["all"])
    parser.add_argument("--home", type=pathlib.Path, default=pathlib.Path.home())
    args = parser.parse_args()
    if not shutil.which("git"):
        print("Missing git", file=sys.stderr)
        return 2
    selected = list(PATHS) if "all" in args.agents else args.agents
    targets = [(name, args.home / PATHS[name]) for name in selected if (args.home / PATHS[name]).is_dir()]
    if not targets:
        print("No installed secure-coding skills detected. Install first using README instructions.")
        return 0
    try:
        with tempfile.TemporaryDirectory(prefix="secure-coding-fetch-") as temp:
            repo = pathlib.Path(temp) / "repo"
            git("clone", "--quiet", "--depth", "1", "--branch", "main", REMOTE, str(repo))
            sha = git("rev-parse", "HEAD", cwd=repo)
            source = repo / "skills" / "secure-coding"
            if not (source / "SKILL.md").is_file():
                raise RuntimeError("Invalid source: SKILL.md missing")
            for filename in REQUIRED:
                if not (source / "references" / filename).is_file():
                    raise RuntimeError("Invalid source: missing " + filename)
            for name, dest in targets:
                metadata = dest / ".updater-version.json"
                try:
                    previous = json.loads(metadata.read_text(encoding="utf-8")).get("sha")
                except (OSError, ValueError, AttributeError):
                    previous = None
                if previous == sha:
                    print(name + ": current " + sha[:12])
                    continue
                if args.check:
                    print(name + ": update available " + sha[:12])
                    continue
                parent = dest.parent
                stage = parent / (".skill-stage-" + uuid.uuid4().hex)
                backup = parent / (".skill-backup-" + uuid.uuid4().hex)
                try:
                    shutil.copytree(source, stage)
                    (stage / ".updater-version.json").write_text(json.dumps({"sha": sha, "repository": REMOTE}), encoding="utf-8")
                    dest.rename(backup)
                    try:
                        stage.rename(dest)
                    except Exception:
                        backup.rename(dest)
                        raise
                    shutil.rmtree(backup)
                    print(name + ": updated " + sha[:12])
                finally:
                    if stage.exists():
                        shutil.rmtree(stage)
    except (OSError, ValueError, RuntimeError, subprocess.CalledProcessError, subprocess.TimeoutExpired) as error:
        print("Update failed: " + str(error), file=sys.stderr)
        return 1
    return 0

if __name__ == "__main__":
    sys.exit(main())
