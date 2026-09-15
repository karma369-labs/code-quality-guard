from __future__ import annotations

import json
from dataclasses import asdict
from typing import Any

from code_quality_guard.runner import CommandResult


def render_json(results: dict[str, CommandResult]) -> str:
    payload: dict[str, Any] = {
        "checks": {name: asdict(result) for name, result in results.items()},
        "passed": all(result.passed for result in results.values()),
    }
    return json.dumps(payload, indent=2, sort_keys=True)
