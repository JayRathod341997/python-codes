# ─────────────────────────────────────────────
# Detect whether a virtual environment is active
# ─────────────────────────────────────────────

import sys
import os

def is_venv_active():
    return hasattr(sys, "real_prefix") or (
        hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix
    )

if is_venv_active():
    print("Virtual environment is ACTIVE")
    print("  venv path  :", sys.prefix)
    print("  Python     :", sys.executable)
else:
    print("No virtual environment active — using system Python")
    print("  Python     :", sys.executable)

# Show VIRTUAL_ENV environment variable (set by activate script)
venv_env = os.environ.get("VIRTUAL_ENV")
print("\nVIRTUAL_ENV =", venv_env if venv_env else "not set")
