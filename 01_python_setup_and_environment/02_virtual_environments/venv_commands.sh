#!/bin/bash
# ─────────────────────────────────────────────
# Virtual Environment — venv
# ─────────────────────────────────────────────

# WHY use venv?
# Each project gets its own isolated packages.
# Avoids version conflicts between projects.

# ── Create ───────────────────────────────────
python -m venv venv              # creates a folder named "venv"
python -m venv .venv             # hidden folder (common convention)
python3.11 -m venv venv          # use a specific Python version

# ── Activate ─────────────────────────────────
source venv/bin/activate         # Linux / macOS
venv\Scripts\activate            # Windows (Command Prompt)
venv\Scripts\Activate.ps1        # Windows (PowerShell)

# ── After activation ─────────────────────────
python --version                 # confirms venv's Python
pip list                         # packages in this venv only

# ── Deactivate ───────────────────────────────
deactivate

# ── Delete ───────────────────────────────────
rm -rf venv                      # Linux/macOS
rmdir /s /q venv                 # Windows

# NOTE: Never commit the venv/ folder to git.
# Add it to .gitignore:  echo "venv/" >> .gitignore
