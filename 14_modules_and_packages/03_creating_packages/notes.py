# ─────────────────────────────────────────────
# Modules & Packages — Creating Packages
# ─────────────────────────────────────────────

# ── What is a package? ────────────────────────
# A package is a directory containing:
#   __init__.py        (required in Python 3 for regular packages)
#   one or more .py module files
#
# This folder contains the `myapp` package:
#
#   myapp/
#   ├── __init__.py       ← makes it a package; runs on import
#   ├── validators.py     ← sub-module
#   └── formatters.py     ← sub-module


# ── Importing from a package ──────────────────

# 1. Import the package itself (runs __init__.py)
import myapp

print(myapp.__version__)        # "1.0.0"
print(myapp.__author__)         # "Jay Rathod"
print(myapp.__doc__)


# 2. Use names re-exported from __init__.py
print(myapp.validate_email("jay@example.com"))     # True
print(myapp.format_currency(49999))                # ₹49,999.00


# 3. Import a specific sub-module
from myapp import validators, formatters

print(validators.validate_phone("+919876543210"))  # True
print(validators.validate_pincode("400001"))       # True
print(formatters.mask_card("4111 1111 1111 1234")) # **** **** **** 1234
print(formatters.truncate("The quick brown fox", 10))  # "The quick..."


# 4. Import directly from a sub-module
from myapp.validators import validate_email
from myapp.formatters import format_currency, mask_card

print(validate_email("bad-email"))                 # False
print(format_currency(1_23_456.78, symbol="$"))   # $1,23,456.78


# ── __init__.py controls the public API ───────
# What's in __init__.py:
#
#   from myapp.validators import validate_email, validate_phone
#   from myapp.formatters import format_currency, mask_card
#   __all__ = [...]
#
# This means:
#   from myapp import validate_email   ← works (re-exported)
#   from myapp import validate_pincode ← AttributeError (not in __init__)
#   from myapp.validators import validate_pincode ← works (direct sub-module)


# ── Namespace packages (Python 3.3+) ──────────
# A directory WITHOUT __init__.py is a "namespace package".
# Used for splitting a package across multiple directories (advanced).
# For normal use, always include __init__.py.


# ── Package structure in real projects ────────
#
#   project/
#   ├── main.py
#   ├── requirements.txt
#   └── myapp/
#       ├── __init__.py
#       ├── validators.py
#       ├── formatters.py
#       ├── models/               ← sub-package
#       │   ├── __init__.py
#       │   ├── user.py
#       │   └── order.py
#       └── services/             ← sub-package
#           ├── __init__.py
#           ├── email_service.py
#           └── payment_service.py
#
# In main.py:
#   from myapp.models.user import User
#   from myapp.services.payment_service import charge_card


# ── Relative imports (inside a package) ───────
# Used WITHIN a package to import sibling modules.
# Example in myapp/formatters.py:
#   from .validators import validate_email   ← relative: same package
#   from ..utils import helper               ← relative: parent package
#
# Use absolute imports (from myapp.validators import ...) from outside
# the package. Use relative imports from inside.


# ── Key points ────────────────────────────────
# • Package = directory + __init__.py
# • __init__.py runs on import; use it to set up the public API
# • Sub-modules: import sub_module or from package import sub_module
# • __all__ in __init__.py defines what `from package import *` exports
# • Relative imports (.module) only valid inside a package
# • Real-world projects always use packages — not a pile of loose .py files
