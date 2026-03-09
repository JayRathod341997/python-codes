# ─────────────────────────────────────────────
# Python REPL (Read-Eval-Print Loop)
# ─────────────────────────────────────────────

# The REPL is the interactive Python shell.
# Start it by typing: python  (or python3)
# Exit with: exit() or Ctrl+D

# ── What REPL looks like ─────────────────────
# $ python
# >>> 2 + 2
# 4
# >>> name = "Jay"
# >>> print(f"Hello, {name}")
# Hello, Jay
# >>> import math
# >>> math.sqrt(16)
# 4.0

# ── REPL tricks ──────────────────────────────
# _  refers to the last result
# >>> 5 * 5
# 25
# >>> _ + 10
# 35

# help() — built-in documentation
# >>> help(str.split)
# >>> help(list)

# dir() — list attributes/methods
# >>> dir(str)
# >>> dir([])

# ── ipython (enhanced REPL) ──────────────────
# pip install ipython
# ipython
# Features: syntax highlighting, auto-complete,
#           history, magic commands (%timeit, %run)

# ── When to use REPL ─────────────────────────
# - Quick experiments and calculations
# - Exploring a new library
# - Checking syntax
# - Debugging a small piece of logic

print("This file explains the REPL — run it or read it!")

# Simulate REPL-style evaluation
expressions = [
    "2 ** 10",
    "len('hello world')",
    "'python'.upper()",
    "[x**2 for x in range(5)]",
]

for expr in expressions:
    result = eval(expr)
    print(f">>> {expr}")
    print(f"{result}\n")
