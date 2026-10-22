#!/usr/bin/env python3
"""Opt-in daily per-user auto-update scheduler, Windows/macOS/Linux. No admin rights."""
import argparse
import pathlib
import platform
import plistlib
import shutil
import subprocess
import sys
import xml.sax.saxutils

def run(*args):
    subprocess.run(list(args), check=True, timeout=30)

def main():
    p = argparse.ArgumentParser()
    p.add_argument("action", choices=["enable", "disable"])
    a = p.parse_args()
    updater = pathlib.Path(__file__).resolve().with_name("skill_updater.py")
    if not updater.is_file():
        raise RuntimeError("Missing updater in scripts directory")
    python = str(pathlib.Path(sys.executable).resolve())
    system = platform.system()
    home = pathlib.Path.home()
    if system == "Windows":
        name = "SecureCodingSkillDailyUpdate"
        if a.action == "disable":
            run("schtasks", "/Delete", "/TN", name, "/F")
        else:
            command = '"' + python + '" "' + str(updater) + '"'
            run("schtasks", "/Create", "/F", "/SC", "DAILY", "/ST", "09:00", "/TN", name, "/TR", command)
    elif system == "Darwin":
        label = "io.github.ruma-lk.secure-coding-update"
        location = home / "Library/LaunchAgents" / (label + ".plist")
        if a.action == "disable":
            if location.exists():
                run("launchctl", "unload", str(location))
                location.unlink()
        else:
            location.parent.mkdir(parents=True, exist_ok=True)
            doc = {
                "Label": label, "ProgramArguments": [python, str(updater)],
                "StartCalendarInterval": {"Hour": 9, "Minute": 0},
                "RunAtLoad": True,
                "StandardOutPath": str(home / "Library/Logs/secure-coding-update.log"),
                "StandardErrorPath": str(home / "Library/Logs/secure-coding-update-error.log"),
            }
            location.write_bytes(plistlib.dumps(doc))
            run("launchctl", "load", "-w", str(location))
    elif system == "Linux":
        if not shutil.which("systemctl"):
            raise RuntimeError("Linux systemd user service unavailable. Use OS-native cron as an alternative.")
        directory = home / ".config/systemd/user"
        service = directory / "secure-coding-update.service"
        timer = directory / "secure-coding-update.timer"
        if a.action == "disable":
            run("systemctl", "--user", "disable", "--now", timer.name)
            service.unlink(missing_ok=True)
            timer.unlink(missing_ok=True)
            run("systemctl", "--user", "daemon-reload")
        else:
            directory.mkdir(parents=True, exist_ok=True)
            service.write_text("[Unit]\nDescription=Update installed secure coding agent skills\n[Service]\nType=oneshot\nExecStart=" + python + " " + str(updater) + "\n", encoding="utf-8")
            timer.write_text("[Unit]\nDescription=Daily secure coding skill update\n[Timer]\nOnCalendar=*-*-* 09:00:00\nPersistent=true\n[Install]\nWantedBy=timers.target\n", encoding="utf-8")
            run("systemctl", "--user", "daemon-reload")
            run("systemctl", "--user", "enable", "--now", timer.name)
    else:
        raise RuntimeError("Unsupported OS: " + system)
    print("Auto-update " + ("enabled" if a.action == "enable" else "disabled") + " for " + system)

if __name__ == "__main__":
    try:
        main()
    except (RuntimeError, OSError, subprocess.CalledProcessError) as error:
        print("Scheduler setup failed: " + str(error), file=sys.stderr)
        sys.exit(1)
