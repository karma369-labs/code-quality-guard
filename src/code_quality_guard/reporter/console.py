from __future__ import annotations

from rich.console import Console

from code_quality_guard.runner import CommandResult


def render_console(results: dict[str, CommandResult]) -> None:
    console = Console()
    for name, result in results.items():
        status = "PASS" if result.passed else "FAIL"
        color = "green" if result.passed else "red"
        console.print(
            f"[{color}][{status}][/{color}] {name} ({result.duration_seconds:.2f}s)"
        )
        diagnostics = "\n".join(
            output.strip() for output in (result.stdout, result.stderr) if output.strip()
        )
        if diagnostics:
            console.print(diagnostics, markup=False)
