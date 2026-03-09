#!/bin/bash
# ─────────────────────────────────────────────
# pip — Python Package Manager
# ─────────────────────────────────────────────

# ── Check pip ────────────────────────────────
pip --version
pip3 --version

# ── Install packages ─────────────────────────
pip install requests                    # latest version
pip install requests==2.31.0            # exact version
pip install "requests>=2.28,<3.0"       # version range
pip install requests httpx rich         # multiple at once

# ── Upgrade ──────────────────────────────────
pip install --upgrade requests          # upgrade a package
pip install --upgrade pip               # upgrade pip itself

# ── Uninstall ────────────────────────────────
pip uninstall requests
pip uninstall requests httpx -y         # -y skips confirmation

# ── List & inspect ───────────────────────────
pip list                                # all installed packages
pip list --outdated                     # packages with newer versions
pip show requests                       # details about a package
pip show requests | grep Location       # find install path

# ── Search (requires pip < 21 or use PyPI website) ──
pip index versions requests             # available versions

# ── Install from file ────────────────────────
pip install -r requirements.txt
pip install -r requirements-dev.txt

# ── Save installed packages ──────────────────
pip freeze > requirements.txt
