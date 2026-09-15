from click.testing import CliRunner

from code_quality_guard import cli
from code_quality_guard.runner import CommandResult


def test_cli_routes_tool_arguments_and_emits_json(monkeypatch) -> None:
    captured = {}

    def fake_run(settings):
        captured["settings"] = settings
        return {"ruff": CommandResult(["ruff"], True, 0, "", "", 0.0)}

    monkeypatch.setattr(cli, "run_quality_checks", fake_run)
    result = CliRunner().invoke(
        cli.main,
        ["--tool", "ruff", "--tool-arg", "ruff", "--select", "--output", "json", "."],
    )

    assert result.exit_code == 0
    assert captured["settings"].tools == ("ruff",)
    assert captured["settings"].tool_args == {"ruff": ("--select",)}
    assert '"passed": true' in result.output


def test_cli_rejects_arguments_for_unselected_tools() -> None:
    result = CliRunner().invoke(
        cli.main,
        ["--tool", "ruff", "--tool-arg", "mypy", "--strict", "."],
    )

    assert result.exit_code != 0
    assert "not selected" in result.output
