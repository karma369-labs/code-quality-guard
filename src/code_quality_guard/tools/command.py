from __future__ import annotations

import shutil
import sys
from pathlib import Path


def resolve_executable(name: str) -> str:
    environment_executable = Path(sys.executable).with_name(name)
    if environment_executable.exists():
        return str(environment_executable)
    return shutil.which(name) or name
