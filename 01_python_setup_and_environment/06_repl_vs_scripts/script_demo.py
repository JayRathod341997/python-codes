# ─────────────────────────────────────────────
# Running Python Scripts
# Run this file: python script_demo.py
# ─────────────────────────────────────────────

import sys

# ── __name__ guard ────────────────────────────
# Code inside this block runs ONLY when the
# file is executed directly, NOT when imported.

def greet(name):
    return f"Hello, {name}!"

def add(a, b):
    return a + b

if __name__ == "__main__":
    print(greet("Jay"))
    print("2 + 3 =", add(2, 3))

    # sys.argv contains command-line arguments
    # Run: python script_demo.py Alice 30
    print("\nCommand-line args:", sys.argv)
    # sys.argv[0] is always the script name

# ── Script vs REPL comparison ─────────────────
# REPL                  | Script
# ──────────────────────|────────────────────────
# Interactive           | Runs top to bottom
# Results shown auto    | Must use print()
# Lost after exit       | Saved as .py file
# Great for exploration | Great for automation
# No __name__ guard     | Use __name__ guard
