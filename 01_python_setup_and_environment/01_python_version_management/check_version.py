# ─────────────────────────────────────────────
# Python Version Management
# ─────────────────────────────────────────────

import sys
import platform

# Check Python version
print("Python version:", sys.version)
print("Version info :", sys.version_info)
print("Platform     :", platform.system())
print("Architecture :", platform.architecture()[0])

# Enforce minimum version at runtime
MIN_VERSION = (3, 8)
if sys.version_info < MIN_VERSION:
    raise RuntimeError(f"Python {MIN_VERSION[0]}.{MIN_VERSION[1]}+ required")
else:
    print(f"\nOK — running Python {sys.version_info.major}.{sys.version_info.minor}")
