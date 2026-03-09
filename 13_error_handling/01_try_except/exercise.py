# ─────────────────────────────────────────────
# Exercises — try / except
# ─────────────────────────────────────────────

# ── Exercise 1: Safe Type Converter ──────────
# Real-life: Form input parsing
# Write a function safe_convert(value, to_type) that converts
# `value` to `to_type` (int, float, bool) and returns the result.
# If conversion fails, return None and print a clear error message.
#
# Test:
#   safe_convert("42",    int)    → 42
#   safe_convert("3.14",  float)  → 3.14
#   safe_convert("hello", int)    → None  + "Cannot convert 'hello' to int"
#   safe_convert(None,    float)  → None  + error message

# --- your code here ---


# ── Exercise 2: Dictionary Safe Lookup ────────
# Real-life: Product catalogue API response
# Write a function get_field(data, *keys) that safely traverses
# nested dicts using the provided key path.
# Return the value if found, or None with a message if any key is missing.
#
# Test:
#   response = {"product": {"name": "Laptop", "price": 75000,
#                            "specs": {"ram": "16GB"}}}
#   get_field(response, "product", "name")          → "Laptop"
#   get_field(response, "product", "specs", "ram")  → "16GB"
#   get_field(response, "product", "discount")      → None + "Key 'discount' not found"
#   get_field(response, "seller", "rating")         → None + "Key 'seller' not found"

# --- your code here ---


# ── Exercise 3: CSV Row Parser ────────────────
# Real-life: Data import validation
# Write a function parse_row(row) where row is a string like
# "Alice,28,72500.50"  (name, age, salary).
# Return a dict {"name": str, "age": int, "salary": float}.
# Handle: wrong number of columns, age not an int, salary not a float.
# Print a descriptive error and return None on failure.
#
# Test rows:
#   "Alice,28,72500.50"  → {"name": "Alice", "age": 28, "salary": 72500.5}
#   "Bob,twenty,50000"   → error: age must be integer
#   "Carol,25"           → error: expected 3 columns
#   "Dave,30,not_a_num"  → error: salary must be a number

# --- your code here ---


# ── Exercise 4: Index-safe List Operations ────
# Real-life: Carousel / pagination component
# Write a function get_page(items, page, size=5) that returns a
# slice of items for the given page (1-indexed).
# Catch IndexError if page is out of range and print a helpful message.
# Also catch TypeError if page or size is not an integer.
#
# Test:
#   data = list(range(1, 22))   # 21 items
#   get_page(data, 1)    → [1, 2, 3, 4, 5]
#   get_page(data, 5)    → [21]
#   get_page(data, 6)    → error: page 6 out of range (max 5)
#   get_page(data, "two")→ error: page and size must be integers

# --- your code here ---


# ── Exercise 5: Multi-source Config Loader ────
# Real-life: App startup — try env var, then file, then default
# Write a function load_setting(key, filepath, default=None):
#   1. Try os.environ[key]          → return it  (use KeyError)
#   2. Try reading filepath as JSON → return data[key]  (FileNotFoundError, KeyError, json.JSONDecodeError)
#   3. Fall back to default
# Print which source was used.
#
# Test (set no env var, use a non-existent file):
#   load_setting("DB_HOST", "config.json", default="localhost")
#   → "Using default: localhost"
#
# (Optionally: write a temp config.json and test the file path too)

import os, json

# --- your code here ---


# ─────────────────────────────────────────────
# Expected outputs (for self-check):
# Ex1: 42  |  3.14  |  None (with message)  |  None (with message)
# Ex2: "Laptop"  |  "16GB"  |  None (with messages)
# Ex3: dict  |  three error messages
# Ex4: [1..5]  |  [21]  |  out-of-range message  |  type message
# Ex5: "Using default: localhost"
# ─────────────────────────────────────────────
