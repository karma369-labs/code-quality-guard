from pathlib import Path

from code_quality_guard.runner import SubprocessRunner


def test_runner_handles_missing_binary() -> None:
    result = SubprocessRunner().run(["definitely-missing-code-quality-tool"], cwd=Path.cwd())
    assert result.passed is False
    assert result.exit_code == 127
    assert "Command not found" in result.stderr
