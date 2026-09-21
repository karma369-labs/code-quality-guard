import sys
from pathlib import Path

from code_quality_guard.config.settings import Settings
from code_quality_guard.runner import CommandResult
from code_quality_guard.tools.mypy import MypyTool
from code_quality_guard.tools.ruff import RuffTool
from code_quality_guard.tools.ruff_format import RuffFormatTool

RUFF_EXECUTABLE = str(Path(sys.executable).with_name("ruff"))
MYPY_EXECUTABLE = str(Path(sys.executable).with_name("mypy"))


class FakeRunner:
    def __init__(self) -> None:
        self.commands: list[list[str]] = []

    def run(self, command: list[str], cwd: Path | None = None) -> CommandResult:
        self.commands.append(command)
        return CommandResult(command, True, 0, "", "", 0.0)


def test_ruff_forwards_fix_and_tool_arguments(tmp_path: Path) -> None:
    runner = FakeRunner()
    settings = Settings(target=tmp_path, fix=True, tool_args={"ruff": ("--select", "E")})

    RuffTool(runner).run(settings)

    assert runner.commands == [[RUFF_EXECUTABLE, "check", str(tmp_path), "--fix", "--select", "E"]]


def test_ruff_format_checks_by_default(tmp_path: Path) -> None:
    runner = FakeRunner()
    settings = Settings(target=tmp_path)

    RuffFormatTool(runner).run(settings)

    assert runner.commands == [[RUFF_EXECUTABLE, "format", str(tmp_path), "--check"]]


def test_ruff_format_only_fixes_with_fix_flag(tmp_path: Path) -> None:
    runner = FakeRunner()
    settings = Settings(target=tmp_path, fix=True)

    RuffFormatTool(runner).run(settings)

    assert runner.commands == [[RUFF_EXECUTABLE, "format", str(tmp_path)]]


def test_mypy_forwards_tool_arguments(tmp_path: Path) -> None:
    runner = FakeRunner()
    settings = Settings(target=tmp_path, tool_args={"mypy": ("--strict",)})

    MypyTool(runner).run(settings)

    assert runner.commands == [[MYPY_EXECUTABLE, str(tmp_path), "--strict"]]
