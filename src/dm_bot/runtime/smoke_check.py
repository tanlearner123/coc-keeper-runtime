from __future__ import annotations

import subprocess
import sys
import time
import os
from pathlib import Path


def ready_seen_in_log(log_path: Path) -> bool:
    if not log_path.exists():
        return False
    try:
        return "READY " in log_path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return False


def terminate_existing_bot_processes(*, current_pid: int) -> None:
    command = (
        "Get-CimInstance Win32_Process | "
        "Where-Object { $_.CommandLine -match 'dm_bot\\.main run-bot' } | "
        f"Where-Object {{ $_.ProcessId -ne {current_pid} }} | "
        "ForEach-Object { Stop-Process -Id $_.ProcessId -Force }"
    )
    subprocess.run(
        ["powershell", "-NoProfile", "-Command", command],
        check=False,
        capture_output=True,
        text=True,
    )


def run_local_smoke_check(*, cwd: Path, wait_seconds: int = 8) -> int:
    test_result = subprocess.run(
        [sys.executable, "-m", "pytest", "-q"],
        cwd=cwd,
        check=False,
    )
    if test_result.returncode != 0:
        return test_result.returncode

    terminate_existing_bot_processes(current_pid=os.getpid())
    log_path = cwd / "bot.smoke.log"
    if log_path.exists():
        log_path.unlink()

    env = dict(os.environ)
    env["PYTHONUNBUFFERED"] = "1"
    process = subprocess.Popen(
        [sys.executable, "-m", "dm_bot.main", "run-bot"],
        cwd=str(cwd),
        env=env,
        stdout=log_path.open("w", encoding="utf-8"),
        stderr=subprocess.STDOUT,
    )
    try:
        deadline = time.time() + max(wait_seconds, 15)
        ready = False
        while time.time() < deadline:
            if process.poll() is not None:
                return 1
            if ready_seen_in_log(log_path):
                ready = True
                break
            time.sleep(0.5)
        if not ready:
            return 1
        time.sleep(5)
        if process.poll() is not None:
            return 1
        return 0
    finally:
        if process.poll() is None:
            process.terminate()
            try:
                process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                process.kill()
