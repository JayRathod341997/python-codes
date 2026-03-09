# ─────────────────────────────────────────────
# Exercises — Importing Modules
# ─────────────────────────────────────────────

# ── Exercise 1: Math Toolkit ──────────────────
# Real-life: Engineering calculator
# Using ONLY the math module (import math):
#   a) Print the area of a circle with radius 7  (π r²)
#   b) Print the hypotenuse of a right triangle with legs 9 and 40
#      (use math.hypot)
#   c) Print log base 2 of 1024  (use math.log2)
#   d) Print math.tau (2π) rounded to 4 decimal places

import math

# --- your code here ---

# Expected: 153.938  |  41.0  |  10.0  |  6.2832


# ── Exercise 2: Random Data Generator ────────
# Real-life: Test data / mock API response generator
# Using `from random import ...` (import only what you need):
#   a) Generate a random float between 10.0 and 99.99 (simulate a temperature)
#   b) Pick a random status from ["active", "inactive", "pending", "banned"]
#   c) Generate a random 6-digit OTP using random.choices with digits
#   d) Shuffle a deck of 5 cards and print the top 2

# --- your code here ---


# ── Exercise 3: Path & OS Operations ─────────
# Real-life: File management utility
# Using os and os.path (import os):
#   a) Print the current working directory
#   b) Print all entries in the current directory using os.listdir(".")
#   c) Print whether "notes.py" exists in the current folder
#   d) Build a path string: join cwd + "reports" + "2024" + "jan.csv"
#      using os.path.join — print it (no need to create it)

import os

# --- your code here ---


# ── Exercise 4: datetime Aliases ──────────────
# Real-life: Scheduling system
# Practice import aliases:
#   import datetime as dt
#   from datetime import timedelta as td
#   a) Print today's date
#   b) Print the date 30 days from now
#   c) Print the date 90 days ago
#   d) Print how many days until New Year 2027

import datetime as dt
from datetime import timedelta as td

# --- your code here ---


# ── Exercise 5: Explore a Module ──────────────
# Real-life: Learning a new library
# Do the following using the `json` module:
#   a) Print the number of public names in the json module (len(dir(json)))
#   b) Print all names that contain "load" (hint: filter dir())
#   c) Print the first line of json.dumps.__doc__
#   d) Convert this dict to a JSON string (indent=2):
#      {"name": "Jay", "skills": ["Python", "Git"], "level": 3}
#   e) Parse it back to a Python dict and print type + value

import json

# --- your code here ---


# ─────────────────────────────────────────────
# Expected outputs (for self-check):
# Ex1: 153.94  |  41.0  |  10.0  |  6.2832
# Ex2: Random values each run
# Ex3: cwd path  |  directory listing  |  True/False  |  joined path
# Ex4: Today + 30d + 90d ago + days until Jan 1 2027
# Ex5: a) ~25  b) ['load', 'loads']  c) first docstring line  d+e) JSON round-trip
# ─────────────────────────────────────────────
