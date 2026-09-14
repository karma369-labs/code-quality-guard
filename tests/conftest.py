from pathlib import Path

import pytest


@pytest.fixture
def source_path(tmp_path: Path) -> Path:
    return tmp_path / "sample.py"
