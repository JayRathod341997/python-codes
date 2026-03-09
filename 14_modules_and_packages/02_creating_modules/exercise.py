# ─────────────────────────────────────────────
# Exercises — Creating Modules
# ─────────────────────────────────────────────

# ── Exercise 1: Use math_utils ────────────────
# Real-life: Investment dashboard
# Import math_utils (it lives in this same folder).
# Use it to answer:
#   a) What is the area of a circle with radius 12?
#   b) If you invest ₹2,00,000 at 9% p.a. for 15 years (monthly compounding),
#      what is the final amount?
#   c) A product price went from ₹1,200 to ₹960. What is the % change?
#   d) A sensor reads 112. Clamp it to range [0, 100].

import math_utils

# --- your code here ---

# Expected: 452.39  |  ₹7,17,...  |  -20.0%  |  100


# ── Exercise 2: Create string_utils.py ────────
# Real-life: User data formatting
# CREATE a new file string_utils.py in THIS folder with these functions:
#
#   slugify(text)
#     — lowercase, replace spaces with "-", strip leading/trailing spaces
#     — "Hello World" → "hello-world"
#
#   truncate(text, max_len, suffix="...")
#     — if len(text) > max_len, return text[:max_len] + suffix
#     — "Hello World" truncated to 7 → "Hello W..."
#
#   title_case(text)
#     — capitalize first letter of each word
#     — "the quick brown fox" → "The Quick Brown Fox"
#
#   mask_email(email)
#     — "alice@example.com" → "a***@example.com"
#
# Then import and test all four functions here.

# --- create string_utils.py, then ---
# import string_utils
# --- your test code here ---


# ── Exercise 3: Create validators.py ─────────
# Real-life: Sign-up form backend
# CREATE validators.py in THIS folder with:
#
#   is_valid_email(email)   → bool (must have "@" and "." after @)
#   is_strong_password(pw)  → bool (≥8 chars, has digit, has upper, has special)
#   is_valid_phone(phone)   → bool (10 digits, may start with +91)
#   is_valid_pincode(code)  → bool (exactly 6 digits, India)
#
# Each function returns True/False.
# Test with:
#   is_valid_email("jay@example.com")     → True
#   is_valid_email("notanemail")          → False
#   is_strong_password("Passw0rd!")       → True
#   is_strong_password("password")        → False
#   is_valid_phone("+919876543210")       → True
#   is_valid_pincode("400001")            → True
#   is_valid_pincode("40001")             → False

# --- create validators.py, then ---
# import validators
# --- your test code here ---


# ── Exercise 4: Combine modules ───────────────
# Real-life: User profile generator
# Using ALL three modules (math_utils, string_utils, validators),
# write a function create_profile(name, email, phone, investment):
#   - slugify the name for a username
#   - validate email and phone (print warning if invalid)
#   - compute compound interest on investment (8% for 10 years)
#   - print a formatted profile card:
#
#   ─────────────────────────────────
#   Profile Card
#   ─────────────────────────────────
#   Name      : Jay Rathod
#   Username  : jay-rathod
#   Email     : j***@gmail.com
#   Phone     : Valid ✓
#   Investment: ₹1,00,000 → ₹2,21,964.00 (10 yrs @ 8%)
#   ─────────────────────────────────

# --- your code here ---


# ─────────────────────────────────────────────
# Expected outputs (for self-check):
# Ex1: 452.39  |  varies  |  -20.0  |  100
# Ex2: all four functions work as described
# Ex3: True/False as described
# Ex4: formatted profile card
# ─────────────────────────────────────────────
