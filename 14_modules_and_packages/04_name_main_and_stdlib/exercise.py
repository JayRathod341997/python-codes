# ─────────────────────────────────────────────
# Exercises — __name__ == "__main__" & stdlib
# ─────────────────────────────────────────────

# ── Exercise 1: Runnable module pattern ───────
# Real-life: CLI utility that is also importable
# Create a new file `bmi_tool.py` in this folder with:
#
#   def bmi(weight_kg, height_m):
#       """Return BMI value."""
#       ...
#
#   def category(bmi_value):
#       """Return 'Underweight'/'Normal'/'Overweight'/'Obese'."""
#       ...
#
#   if __name__ == "__main__":
#       weight = float(input("Weight (kg): "))
#       height = float(input("Height (m) : "))
#       b = bmi(weight, height)
#       print(f"BMI: {b:.1f} — {category(b)}")
#
# Then import bmi_tool HERE and use its functions without triggering the input():
# Test:
#   bmi_tool.bmi(72, 1.75)       → 23.51 (Normal)
#   bmi_tool.bmi(50, 1.75)       → 16.33 (Underweight)
#   bmi_tool.bmi(100, 1.75)      → 32.65 (Obese)

# --- create bmi_tool.py, then ---
# import bmi_tool
# --- your test code here ---


# ── Exercise 2: JSON config system ───────────
# Real-life: Application settings management
# Write a module-style script (with __main__ guard) that:
#   1. Has a function load_config(path) → returns dict (json.loads)
#      or returns {} if file missing
#   2. Has a function save_config(path, data) → writes JSON with indent=2
#   3. Has a function merge_config(base, override) → merged dict
#      (override values take priority)
#
# Under __name__ == "__main__":
#   - Define a default config dict
#   - Save it to "config.json"
#   - Load it back
#   - Merge with {"debug": True, "port": 9000}
#   - Print final config
#
# Write all this in THIS file (not a separate file).

import json, os

def load_config(path):
    pass  # your code here

def save_config(path, data):
    pass  # your code here

def merge_config(base, override):
    pass  # your code here

if __name__ == "__main__":
    default = {
        "host": "localhost",
        "port": 8000,
        "debug": False,
        "db": "sqlite:///app.db"
    }
    # --- complete the __main__ block ---


# ── Exercise 3: stdlib exploration ───────────
# Real-life: Building a report generator utility
# Using ONLY the standard library, do the following:

import os, sys, platform, hashlib, uuid
from datetime import datetime

# a) Print a system info report:
#    OS, Python version, current user (os.getlogin() or os.environ),
#    current datetime formatted as "DD Mon YYYY HH:MM:SS"

# --- your code here ---

# b) Generate 5 unique order IDs using uuid4 and store in a list.
#    Print them all.

# --- your code here ---

# c) Hash a "password" string with SHA-256 and print first 16 hex chars.
#    (Use hashlib.sha256(password.encode()).hexdigest())

# --- your code here ---

# d) Using re, extract all amounts (numbers preceded by ₹ or $) from:
#    text = "Invoice: ₹12,500 paid. Refund of $45.00 processed. Tax: ₹225"
#    Print: ['12,500', '45.00', '225']

import re
text = "Invoice: ₹12,500 paid. Refund of $45.00 processed. Tax: ₹225"
# --- your code here ---


# ── Exercise 4: pathlib file manager ─────────
# Real-life: Log archiver script
# Using pathlib (no os.path), write functions:
#
#   list_py_files(directory)
#       → return list of all .py file names (not full paths) in directory
#
#   file_summary(filepath)
#       → return dict: {"name": ..., "size_kb": ..., "lines": ...}
#
# Test with the current directory.
# Print a table:
#   File               Size(KB)  Lines
#   ────────────────────────────────
#   notes.py           2.1       85
#   exercise.py        1.4       60

from pathlib import Path

def list_py_files(directory):
    pass  # your code here

def file_summary(filepath):
    pass  # your code here

if __name__ == "__main__":
    # --- your test code here ---
    pass


# ─────────────────────────────────────────────
# Expected outputs (for self-check):
# Ex1: 23.51 Normal | 16.33 Underweight | 32.65 Obese
# Ex2: merged config printed with debug=True and port=9000
# Ex3: system report | 5 UUIDs | hash | ['12,500', '45.00', '225']
# Ex4: table of .py files in current directory
# ─────────────────────────────────────────────
