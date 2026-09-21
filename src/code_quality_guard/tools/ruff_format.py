from __future__ import annotations

from code_quality_guard.config.settings import Settings
from code_quality_guard.runner import CommandResult, SubprocessRunner
from code_quality_guard.tools.command import resolve_executable


class RuffFormatTool:
    name = "ruff-format"

    def __init__(self, runner: SubprocessRunner | None = None) -> None:
        self.runner = runner or SubprocessRunner()

    def run(self, settings: Settings) -> CommandResult:
        command = [resolve_executable("ruff"), "format", str(settings.target)]
        if not settings.fix or settings.check_only:
            command.append("--check")
        command.extend(settings.tool_args.get(self.name, ()))
        cwd = settings.target if settings.target.is_dir() else settings.target.parent
        return self.runner.run(command, cwd=cwd)
