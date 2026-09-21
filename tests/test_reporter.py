from code_quality_guard.reporter.console import render_console
from code_quality_guard.runner import CommandResult


def test_console_reports_tool_diagnostics_without_a_table(capsys) -> None:
    render_console(
        {
            "ruff": CommandResult(
                ["ruff"], False, 1, "src/app.py:1:1: error", "", 0.12
            ),
            "mypy": CommandResult(["mypy"], True, 0, "", "", 0.08),
        }
    )

    output = capsys.readouterr().out
    assert "[FAIL] ruff" in output
    assert "src/app.py:1:1: error" in output
    assert "[PASS] mypy" in output
    assert "Check" not in output
    assert "Status" not in output