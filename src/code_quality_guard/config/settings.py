from pathlib import Path
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


class Settings(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    target: Path = Field(default_factory=Path.cwd)
    tools: tuple[str, ...] = ("ruff", "mypy")
    fix: bool = False
    check_only: bool = False
    output: Literal["text", "json"] = "text"
    tool_args: dict[str, tuple[str, ...]] = Field(default_factory=dict)
