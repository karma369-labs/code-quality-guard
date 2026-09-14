from __future__ import annotations

from typing import Protocol

from code_quality_guard.config.settings import Settings
from code_quality_guard.runner import CommandResult


class Tool(Protocol):
    name: str

    def run(self, settings: Settings) -> CommandResult:
        """Run the tool for the configured target."""
