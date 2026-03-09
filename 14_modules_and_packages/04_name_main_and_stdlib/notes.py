# ─────────────────────────────────────────────
# Modules & Packages — __name__ == "__main__" & stdlib overview
# ─────────────────────────────────────────────

# ── __name__ — the module's own name ──────────
# Every module has a built-in __name__ attribute.
# When a file is RUN directly:   __name__ == "__main__"
# When a file is IMPORTED:       __name__ == the filename (without .py)

print(f"This file's __name__: {__name__}")
# Running directly → "__main__"
# Importing it     → "notes"  (or whatever the file is named)


# ── The if __name__ == "__main__" guard ───────
# Code inside this block runs ONLY when the file is executed directly.
# It does NOT run when the file is imported as a module.
# This is the standard way to write "runnable + importable" files.

def greet(name):
    return f"Hello, {name}!"

def add(a, b):
    return a + b

if __name__ == "__main__":
    # This block is skipped when imported
    print(greet("Jay"))
    print(add(3, 7))
    print("Running as a script!")


# ── Real-life: utility module that can also run standalone ────
# Pattern seen in Django, Flask, data-science scripts, CLI tools.

# calculator.py (hypothetical):
#
#   def compute(expr):
#       return eval(expr)
#
#   if __name__ == "__main__":
#       import sys
#       if len(sys.argv) > 1:
#           result = compute(sys.argv[1])
#           print(f"Result: {result}")
#       else:
#           print("Usage: python calculator.py '3 + 4 * 2'")


# ── Why it matters ────────────────────────────
# Without the guard, any top-level code runs on import.
# Example of BAD practice:
#
#   # bad_module.py
#   def my_func(): ...
#   print("I run when imported!")   ← annoying side-effect on import
#   my_func()                       ← runs on import too!
#
# With the guard:
#   if __name__ == "__main__":
#       my_func()                   ← only runs when script is executed


# ── Python Standard Library overview ─────────
# The stdlib ships with Python — no pip install needed.

# ── I/O & Files ───────────────────────────────
import pathlib
p = pathlib.Path(".")
print(list(p.glob("*.py"))[:3])     # .py files in current dir

import json
data = json.dumps({"name": "Jay", "score": 99}, indent=2)
print(data)

import csv
# with open("data.csv", newline="") as f:
#     for row in csv.DictReader(f): print(row)

# ── System & OS ───────────────────────────────
import os, sys, platform
print(platform.system())            # Windows / Linux / Darwin
print(sys.version)
print(os.getenv("PATH", "not set")[:60])

# ── Date & Time ───────────────────────────────
from datetime import datetime, timedelta, date
print(datetime.now().strftime("%d %b %Y %H:%M"))
print(date.today() + timedelta(days=30))

# ── Math & Numbers ────────────────────────────
import math, decimal, fractions
print(math.gcd(48, 64))            # 16
print(decimal.Decimal("0.1") + decimal.Decimal("0.2"))  # 0.3 (precise!)
print(fractions.Fraction(1, 3) + fractions.Fraction(1, 6))  # 1/2

# ── Data Structures ───────────────────────────
from collections import Counter, defaultdict, deque, namedtuple
from itertools import chain, islice, groupby
from functools import partial, lru_cache

# ── Text & Regex ──────────────────────────────
import re, textwrap, string
print(re.findall(r"\d+", "Order 1042 placed on 15-01-2024"))   # ['1042','15','01','2024']
print(textwrap.fill("Python " * 10, width=40))
print(string.ascii_uppercase)      # ABCDEFGHIJKLMNOPQRSTUVWXYZ

# ── Networking & Web ──────────────────────────
import urllib.parse
params = urllib.parse.urlencode({"q": "python modules", "page": 2})
print(f"https://example.com/search?{params}")

import urllib.request
# with urllib.request.urlopen("https://httpbin.org/get") as r:
#     print(r.read().decode())

# ── Concurrency ───────────────────────────────
import threading, concurrent.futures
# ThreadPoolExecutor, ProcessPoolExecutor, asyncio

# ── Compression & Archiving ───────────────────
import zipfile, gzip
# zipfile.ZipFile, gzip.open

# ── Hashing & Security ────────────────────────
import hashlib, secrets
pwd_hash = hashlib.sha256(b"my_password").hexdigest()
print(f"SHA-256: {pwd_hash[:20]}...")
token = secrets.token_hex(16)
print(f"Secure token: {token}")

# ── Testing ───────────────────────────────────
import unittest, doctest
# unittest.TestCase, doctest.testmod()

# ── Useful lesser-known stdlib modules ────────
import pprint, copy, uuid, enum, dataclasses

import uuid
print(uuid.uuid4())    # random UUID — great for unique IDs

import enum
class Status(enum.Enum):
    PENDING  = "pending"
    ACTIVE   = "active"
    INACTIVE = "inactive"

print(Status.ACTIVE.value)


# ── Key points ────────────────────────────────
# • __name__ == "__main__" → file is running directly (not imported)
# • Always guard test/demo code with this check in reusable modules
# • stdlib is vast — you rarely need a third-party lib for common tasks
# • Essential modules: os, sys, pathlib, json, datetime, re, collections,
#   itertools, functools, logging, unittest, threading, hashlib
