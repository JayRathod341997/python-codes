# ─────────────────────────────────────────────
# myapp/__init__.py
# ─────────────────────────────────────────────
# This file makes the `myapp` directory a Python package.
# It runs when `import myapp` or `from myapp import ...` is executed.

"""
myapp — A sample e-commerce utility package.

Sub-modules:
    myapp.validators  — input validation helpers
    myapp.formatters  — output formatting helpers
"""

__version__ = "1.0.0"
__author__  = "Jay Rathod"

# Expose key names at the package level so users can write:
#   from myapp import validate_email
# instead of:
#   from myapp.validators import validate_email

from myapp.validators import validate_email, validate_phone
from myapp.formatters import format_currency, mask_card

__all__ = ["validate_email", "validate_phone", "format_currency", "mask_card"]
