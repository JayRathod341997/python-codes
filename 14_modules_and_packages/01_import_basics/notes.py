# ─────────────────────────────────────────────
# Modules & Packages — Importing Modules
# ─────────────────────────────────────────────

# ── What is a module? ─────────────────────────
# A module is any .py file. Importing it runs the file and gives
# you access to the names (functions, classes, variables) it defines.

# ── 1. import module ──────────────────────────
# Imports the entire module; access names with dot notation.

import math

print(math.pi)              # 3.141592653589793
print(math.sqrt(144))       # 12.0
print(math.floor(9.7))      # 9

# The module name is the namespace — no name conflicts:
import random
print(random.randint(1, 6))         # random die roll

import os
print(os.getcwd())                  # current working directory


# ── 2. from module import name ────────────────
# Import specific names directly into current namespace.
# No dot needed — but watch for name collisions.

from math import pi, sqrt, ceil

print(pi)                   # 3.14159...  (no "math." prefix)
print(sqrt(256))            # 16.0
print(ceil(4.1))            # 5

from random import choice, shuffle

cards = ["A", "K", "Q", "J", "10"]
shuffle(cards)
print(choice(cards))        # random card


# ── 3. import module as alias ─────────────────
# Rename the module to a shorter or clearer name.

import datetime as dt
import collections as col

today = dt.date.today()
print(f"Today: {today}")

counter = col.Counter("banana")
print(counter)              # Counter({'a': 3, 'n': 2, 'b': 1})


# ── 4. from module import name as alias ───────
# Import a specific name and rename it.

from math import factorial as fact
from os.path import join as path_join

print(fact(10))             # 3628800
print(path_join("/home", "user", "docs"))


# ── 5. from module import * ───────────────────
# Imports ALL public names from the module into current namespace.
# ⚠ AVOID in production — pollutes namespace, hides where names come from.

# from math import *     # now pi, sqrt, sin, cos... are all in scope
# Acceptable only in interactive REPL sessions or very small scripts.


# ── 6. How Python finds modules (sys.path) ────
import sys

# Python searches these directories in order:
# 1. The script's own directory
# 2. Directories in PYTHONPATH environment variable
# 3. Standard library directories
# 4. site-packages (installed third-party packages)

print(sys.path[:3])         # first 3 search locations

# Add a custom path at runtime (not recommended for production):
# sys.path.insert(0, "/my/custom/lib")


# ── 7. Checking what's inside a module ────────
import json

print(dir(json))            # list of all names in the module
help(json.dumps)            # full docstring (press q to exit in terminal)

# Useful module attributes:
print(json.__name__)        # 'json'
print(json.__file__)        # path to json.py on disk
print(json.__doc__[:80])    # first 80 chars of module docstring


# ── 8. Importing sub-modules ──────────────────
# Some modules are packages with sub-modules.

import os.path
print(os.path.exists("/tmp"))

from email.mime.text import MIMEText   # deep sub-module import
# from urllib.parse import urlencode


# ── Real-life summary ─────────────────────────
# import json                        ← working with API responses
# from pathlib import Path           ← modern file path handling
# import logging                     ← structured logs
# from datetime import datetime      ← timestamps
# import re                          ← regex
# from collections import defaultdict← grouped data
# import csv                         ← CSV I/O


# ── Key points ────────────────────────────────
# • import math          → use math.sqrt()        — safest, clear origin
# • from math import sqrt→ use sqrt()             — convenient, watch collisions
# • import math as m     → use m.sqrt()           — shorter alias
# • from math import *   → avoid in real code
# • sys.path controls where Python looks for modules
# • Use dir() and help() to explore any module interactively
