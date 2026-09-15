from __future__ import annotations

from rich.console import Console
from rich.table import Table

from code_quality_guard.runner import CommandResult


def render_console(results: dict[str, CommandResult]) -> None:
    console = Console()
    table = Table(title="Code Quality Guard")
    table.add_column("Check")
    table.add_column("Status")
    table.add_column("Duration")
    for name, result in results.items():
        status = "PASS" if result.passed else "FAIL"
        table.add_row(name, status, f"{result.duration_seconds:.2f}s")
    console.print(table)
