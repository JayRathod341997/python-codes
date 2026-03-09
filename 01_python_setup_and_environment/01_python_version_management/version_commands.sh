#!/bin/bash
# ─────────────────────────────────────────────
# Common Python Version Management Commands
# Run each line manually in your terminal
# ─────────────────────────────────────────────

# Check installed Python version
python --version
python3 --version

# Check exact path of Python being used
which python
which python3          # Linux/macOS
where python           # Windows

# List all Python versions (if pyenv installed)
pyenv versions

# ── pyenv (Linux/macOS) ──────────────────────
# Install pyenv:
#   curl https://pyenv.run | bash

# Install a specific Python version
pyenv install 3.11.0
pyenv install 3.12.0

# Set global default version
pyenv global 3.11.0

# Set version only for current project folder
pyenv local 3.10.0

# ── py launcher (Windows) ────────────────────
# List all installed versions
py --list

# Run a specific version
py -3.11 script.py
py -3.10 --version
