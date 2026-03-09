#!/bin/bash
# ─────────────────────────────────────────────
# UV — Ultra-fast Python package manager
# Much faster drop-in replacement for pip + venv
# ─────────────────────────────────────────────

# ── Install UV ───────────────────────────────
# Windows (PowerShell):
#   powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
# Linux / macOS:
#   curl -Ls https://astral.sh/uv/install.sh | sh

uv --version

# ── Project setup (recommended way) ──────────
uv init my_project           # create new project with pyproject.toml
cd my_project
uv run python main.py        # run script (auto-manages venv)

# ── Package management ───────────────────────
uv add requests              # add dependency (updates pyproject.toml)
uv add "httpx>=0.24"         # with version constraint
uv add --dev pytest ruff     # add dev-only dependency
uv remove requests           # remove a package

# ── Virtual environments ──────────────────────
uv venv                      # create .venv in current folder
uv venv --python 3.11        # use specific Python version
source .venv/bin/activate    # activate (Linux/macOS)
.venv\Scripts\activate       # activate (Windows)

# ── pip-compatible commands ───────────────────
uv pip install requests              # same as pip install
uv pip install -r requirements.txt   # from file
uv pip freeze                        # list installed packages
uv pip list                          # list with versions

# ── Python version management ─────────────────
uv python install 3.11       # install a Python version
uv python install 3.12
uv python list               # list available/installed versions
uv python pin 3.11           # pin version for current project

# ── Sync from pyproject.toml ──────────────────
uv sync                      # install all dependencies
uv sync --dev                # include dev dependencies

# ── Run tools without installing ──────────────
uvx black .                  # run black formatter once, no install
uvx ruff check .             # run ruff linter once
uvx pytest                   # run tests
