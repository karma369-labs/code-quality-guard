from __future__ import annotations

from collections.abc import Iterable

from code_quality_guard.runner import SubprocessRunner
from code_quality_guard.tools.base import Tool
from code_quality_guard.tools.mypy import MypyTool
from code_quality_guard.tools.ruff import RuffTool
from code_quality_guard.tools.ruff_format import RuffFormatTool

TOOL_TYPES: dict[str, type[Tool]] = {
    "ruff": RuffTool,
    "ruff-format": RuffFormatTool,
    "mypy": MypyTool,
}


def build_tools(tool_names: Iterable[str], runner: SubprocessRunner | None = None) -> list[Tool]:
    shared_runner = runner or SubprocessRunner()
    return [TOOL_TYPES[name](shared_runner) for name in tool_names]
