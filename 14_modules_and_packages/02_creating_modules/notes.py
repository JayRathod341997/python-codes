# ─────────────────────────────────────────────
# Modules & Packages — Creating Your Own Module
# ─────────────────────────────────────────────

# ── What makes a module? ──────────────────────
# Any .py file is a module. The filename (without .py) is the module name.
# In this folder: math_utils.py is our custom module.

# ── Importing our custom module ───────────────
import math_utils                     # file: math_utils.py (same directory)

print(math_utils.PI)                  # 3.141592653589793
print(math_utils.circle_area(5))      # 78.54...
print(math_utils.compound_interest(100_000, 8.5, 10))  # ₹228,388.49
print(math_utils.percentage_change(80, 100))            # 25.0


# ── from import ───────────────────────────────
from math_utils import compound_interest, percentage_change

# Use directly, no prefix needed
amount = compound_interest(50_000, 7.2, 5)
print(f"Invested ₹50,000 → ₹{amount:,} after 5 years")

change = percentage_change(250, 310)
print(f"Price change: {change}%")


# ── Module attributes ─────────────────────────
print(math_utils.__name__)     # 'math_utils'
print(math_utils.__file__)     # absolute path to math_utils.py
print(math_utils.__doc__)      # module-level docstring
print(dir(math_utils))         # all public names


# ── How module execution works ────────────────
# When you `import math_utils`:
#   1. Python finds math_utils.py in sys.path
#   2. Executes the file top to bottom
#   3. Binds the resulting namespace to the name `math_utils`
#   4. Caches it in sys.modules — subsequent imports reuse it

import sys
print("math_utils" in sys.modules)    # True after first import
import math_utils as mu2              # same object — not re-executed
print(mu2 is math_utils)              # True


# ── Module-level variables as constants ───────
# Convention: UPPER_CASE for module-level constants
# math_utils.PI, math_utils._version (leading _ = private by convention)
print(math_utils._version)   # still accessible, but signals "internal"


# ── Structuring a real utility module ─────────
# Good practice:
#   • Group related functions
#   • Write docstrings on every function
#   • Keep side-effects minimal at module level
#   • Use __all__ to control what `from module import *` exports

# math_utils.py could add:
#   __all__ = ["circle_area", "compound_interest", "percentage_change", "clamp"]


# ── Real-life: building a project toolkit ─────
# project/
#   main.py
#   utils/
#     math_utils.py     ← financial/math helpers
#     string_utils.py   ← text formatting
#     date_utils.py     ← date arithmetic
#     validators.py     ← input validation
#
# In main.py:
#   from utils.math_utils import compound_interest
#   from utils.validators import validate_email


# ── Key points ────────────────────────────────
# • Any .py file is a module — just name it well
# • Module code runs once on first import; cached in sys.modules
# • Use __all__ to define the public API
# • Leading underscore = private by convention (not enforced)
# • Module attributes: __name__, __file__, __doc__
# • Keep module-level side-effects minimal (no heavy computation/I/O)
