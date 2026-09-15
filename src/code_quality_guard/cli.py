from __future__ import annotations

from pathlib import Path

import click

from code_quality_guard.application.service import run_quality_checks
from code_quality_guard.config.settings import Settings
from code_quality_guard.reporter.console import render_console
from code_quality_guard.reporter.json import render_json

TOOL_NAMES = ["ruff", "ruff-format", "mypy"]


@click.command()
@click.argument("target", type=click.Path(path_type=Path, exists=True), default=Path.cwd())
@click.option("--tool", "tools", multiple=True, type=click.Choice(TOOL_NAMES))
@click.option("--fix", is_flag=True, help="Apply supported fixes.")
@click.option("--check-only", is_flag=True, help="Check formatting without changing files.")
@click.option("--output", type=click.Choice(["text", "json"]), default="text", show_default=True)
@click.option(
    "--tool-arg",
    "tool_args",
    nargs=2,
    multiple=True,
    metavar="TOOL ARG",
    help="Pass an additional argument to a tool; repeat as needed.",
)
def main(
    target: Path,
    tools: tuple[str, ...],
    fix: bool,
    check_only: bool,
    output: str,
    tool_args: tuple[tuple[str, str], ...],
) -> None:
    """Run selected code quality tools against TARGET."""
    selected_tools = tools or tuple(TOOL_NAMES)
    args_by_tool: dict[str, tuple[str, ...]] = {}
    for tool_name, argument in tool_args:
        if tool_name not in selected_tools:
            raise click.BadParameter(f"{tool_name!r} is not selected with --tool")
        args_by_tool[tool_name] = (*args_by_tool.get(tool_name, ()), argument)
    settings = Settings(
        target=target.resolve(),
        tools=selected_tools,
        fix=fix,
        check_only=check_only,
        output=output,
        tool_args=args_by_tool,
    )
    results = run_quality_checks(settings)
    if settings.output == "json":
        click.echo(render_json(results))
    else:
        render_console(results)
    if not all(result.passed for result in results.values()):
        raise click.exceptions.Exit(1)
