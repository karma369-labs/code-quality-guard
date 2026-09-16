# Code Quality Guard

[![CI](https://github.com/karma369-labs/code-quality-guard/actions/workflows/ci.yml/badge.svg)](https://github.com/karma369-labs/code-quality-guard/actions/workflows/ci.yml)
[![PyPI](https://img.shields.io/pypi/v/code-quality-guard)](https://pypi.org/project/code-quality-guard/)
[![Python](https://img.shields.io/badge/python-3.12%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Ruff](https://img.shields.io/badge/linter-Ruff-D7FF64?logo=ruff&logoColor=black)](https://docs.astral.sh/ruff/)
[![Mypy](https://img.shields.io/badge/type%20checker-Mypy-4B8BBE?logo=mypy&logoColor=white)](https://mypy-lang.org/)

`code-quality-guard` is a CI-friendly command-line quality gate for Python
projects. It runs Ruff linting, Ruff formatting, and Mypy through one
consistent interface, with human-readable or JSON output for local workflows
and automation.

## Features

- Run Ruff, Ruff format, and Mypy independently or together.
- Check a project directory or a single file.
- Apply Ruff fixes when supported.
- Forward additional arguments to each selected tool.
- Emit text for developers or JSON for scripts and CI integrations.
- Return a non-zero exit code when any selected check fails.

## Requirements

- Python 3.12 or newer
- Ruff and Mypy are installed automatically with the package

## Installation

Install the latest release from PyPI in an active virtual environment:

```bash
python -m pip install code-quality-guard
```

For local development with `uv`:

```bash
uv sync --dev
```

## Pre-commit Hook

Add `code-quality-guard` to a project-level `.pre-commit-config.yaml`:

```yaml
repos:
	- repo: https://github.com/karma369-labs/code-quality-guard
		rev: v0.1.0
		hooks:
			- id: cqg
```

Install the hook and run it against the repository:

```bash
python -m pip install pre-commit
pre-commit install
pre-commit run --all-files
```

The `cqg` hook runs Ruff linting, Ruff formatting checks, and Mypy over the
project. To use a newer release, update `rev` to the corresponding package
release tag.

## Usage

Run all checks against the current directory:

```bash
code-quality-guard .
```

Run selected tools:

```bash
code-quality-guard --tool ruff --tool mypy src/
```

Check formatting without changing files:

```bash
code-quality-guard --tool ruff-format --check-only .
```

Apply supported fixes:

```bash
code-quality-guard --tool ruff --tool ruff-format --fix .
```

Produce machine-readable output:

```bash
code-quality-guard --output json .
```

Pass an additional argument to a selected tool. Repeat `--tool-arg` as
needed:

```bash
code-quality-guard \
	--tool ruff \
	--tool-arg ruff --select \
	--tool-arg ruff E,F \
	.
```

Run `code-quality-guard --help` for the complete option reference.

## Development

Install the development dependencies and run the test suite:

```bash
uv sync --dev
uv run pytest
```

The repository uses pre-commit for linting, formatting, type checking, and
other repository checks:

```bash
uv run pre-commit install
uv run pre-commit run --all-files
```

Pull requests targeting `main` run the same pre-commit checks in GitHub Actions.

## Project Layout

```text
src/code_quality_guard/
├── application/   Orchestration for quality checks
├── config/        Runtime settings
├── reporter/      Text and JSON output
├── tools/         Ruff and Mypy integrations
└── cli.py         Click command-line interface
tests/             Automated tests
```

## License

License information has not yet been published for this repository.
