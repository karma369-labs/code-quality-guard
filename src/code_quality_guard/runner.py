from __future__ import annotations

import subprocess
import time
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class CommandResult:
    command: list[str]
    passed: bool
    exit_code: int
    stdout: str
    stderr: str
    duration_seconds: float


class SubprocessRunner:
    def run(self, command: list[str], cwd: Path | None = None) -> CommandResult:
        started = time.perf_counter()
        try:
            completed = subprocess.run(
                command, cwd=cwd, capture_output=True, text=True, check=False
            )
            stdout, stderr, exit_code = completed.stdout, completed.stderr, completed.returncode
        except FileNotFoundError as error:
            stdout, stderr, exit_code = (
                "",
                f"Command not found: {error.filename or command[0]}",
                127,
            )
        return CommandResult(
            command=command,
            passed=exit_code == 0,
            exit_code=exit_code,
            stdout=stdout,
            stderr=stderr,
            duration_seconds=time.perf_counter() - started,
        )
