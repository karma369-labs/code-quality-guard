from __future__ import annotations

from code_quality_guard.config.settings import Settings
from code_quality_guard.runner import CommandResult
from code_quality_guard.tools.registry import build_tools


def run_quality_checks(settings: Settings) -> dict[str, CommandResult]:
    return {tool.name: tool.run(settings) for tool in build_tools(settings.tools)}
