# ─────────────────────────────────────────────
# Error Handling — Debugging Basics
# ─────────────────────────────────────────────

# ── 1. Reading a Traceback ────────────────────
# When Python crashes it prints a traceback — read it BOTTOM UP.
#
# Example traceback:
#   Traceback (most recent call last):
#     File "app.py", line 12, in <module>
#       result = calculate(data)
#     File "app.py", line 7, in calculate
#       return total / count          ← actual error line
#   ZeroDivisionError: division by zero
#
# Steps to read:
#   1. Look at the LAST line → exception type + message
#   2. Look at the line ABOVE it → exact file + line number
#   3. Walk up the call stack to understand what triggered it


# ── 2. Print Debugging ────────────────────────
# Fastest first resort — add strategic print() calls.

def calculate_discount(price, discount_pct):
    print(f"[DEBUG] price={price}, discount_pct={discount_pct}")  # ← debug print
    discounted = price - (price * discount_pct)                    # Bug: should be /100
    print(f"[DEBUG] discounted={discounted}")
    return discounted

result = calculate_discount(1000, 10)
print(f"Final price: {result}")
# [DEBUG] shows 10% was applied as 10x, not 10%
# Fix: price * discount_pct / 100


# ── 3. assert — Defensive programming ────────
# assert <condition>, "message"
# Raises AssertionError if condition is False.
# Use during development to catch logic bugs early.
# Real-life: Validate function preconditions

def compute_interest(principal, rate, years):
    assert principal > 0,  f"Principal must be positive, got {principal}"
    assert 0 < rate < 100, f"Rate must be 0–100%, got {rate}"
    assert years > 0,      f"Years must be positive, got {years}"
    return principal * (1 + rate / 100) ** years

print(f"₹{compute_interest(10_000, 8, 5):.2f}")

try:
    compute_interest(-1000, 8, 5)
except AssertionError as e:
    print(f"Assertion failed: {e}")

# ⚠ Note: assert statements are disabled when Python runs with -O flag.
#   Use raise ValueError for user-facing validations, not assert.
#   assert = developer safety net; raise = user-facing contract.


# ── 4. Common Exceptions & Quick Fixes ────────

# NameError — typo in variable/function name
# x = 10
# print(X)  # NameError: name 'X' is not defined
# Fix: check spelling and scope

# TypeError — wrong type in operation
# "Total: " + 100   # TypeError: can only concatenate str (not "int") to str
# Fix: str(100) or f-string

# AttributeError — method doesn't exist on that type
# "hello".append("!")  # AttributeError: 'str' has no attribute 'append'
# Fix: check the correct method (str is immutable; use + or f-string)

# IndexError — list out of range
# lst = [1, 2, 3]; lst[5]  # IndexError: list index out of range
# Fix: check len(lst) before indexing

# KeyError — dict key missing
# d = {"a": 1}; d["b"]  # KeyError: 'b'
# Fix: use d.get("b") or "b" in d check

# UnboundLocalError — assigned and referenced before assignment
# def f():
#     print(x)    # reads x → UnboundLocalError
#     x = 10      # same x is now local
# Fix: declare x before use, or use global/nonlocal


# ── 5. breakpoint() — Built-in debugger ───────
# Drops into the Python Debugger (pdb) at that line.
# Available since Python 3.7 (before: import pdb; pdb.set_trace()).
#
# Key pdb commands:
#   n (next)       — execute current line
#   s (step)       — step into function call
#   c (continue)   — run until next breakpoint
#   p <expr>       — print value of expression
#   l (list)       — show surrounding code
#   q (quit)       — exit pdb
#   pp <expr>      — pretty-print
#   b <line>       — set breakpoint at line
#   where          — show call stack

def buggy_total(prices):
    total = 0
    for price in prices:
        # breakpoint()     ← uncomment to step through loop
        total += price
    return total

print(buggy_total([100, 200, 300]))


# ── 6. logging module (vs print) ──────────────
# Real-life: Production apps use logging, not print.
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)s | %(funcName)s | %(message)s"
)

def process_order(order_id, amount):
    logging.debug(f"Processing order {order_id} for ₹{amount}")
    if amount <= 0:
        logging.error(f"Order {order_id} has invalid amount: {amount}")
        return False
    logging.info(f"Order {order_id} processed successfully")
    return True

process_order("ORD001", 1500)
process_order("ORD002", -50)

# Levels (lowest → highest):
#   DEBUG    — detailed diagnostic info
#   INFO     — confirmation things work
#   WARNING  — something unexpected, but still working
#   ERROR    — error, function failed
#   CRITICAL — serious error, program may crash


# ── 7. Practical Debugging Checklist ──────────
# 1. Read the traceback bottom-up — find file, line, exception
# 2. Add print() around the failing line to inspect values
# 3. Use assert to check assumptions at function entry points
# 4. Narrow down: comment out code, use minimal reproducible example
# 5. Use breakpoint() to step through execution interactively
# 6. Check Python docs for the exact exception meaning
# 7. Search the error message — StackOverflow / docs usually help


# ── Key points ────────────────────────────────
# • Tracebacks: always read from the bottom up
# • print() debugging: quick but messy; remove before production
# • assert: catch your own logic bugs during development
# • breakpoint(): step-by-step interactive debugging
# • logging: structured, level-based — use in real projects
# • Common bugs: NameError (typo), TypeError (wrong type),
#   IndexError (bounds), KeyError (missing key), UnboundLocalError (scope)
