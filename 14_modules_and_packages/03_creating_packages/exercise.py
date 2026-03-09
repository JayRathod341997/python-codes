# ─────────────────────────────────────────────
# Exercises — Creating Packages
# ─────────────────────────────────────────────

# ── Exercise 1: Use the myapp package ─────────
# Real-life: User registration validation
# Import from the myapp package and validate this sign-up data:
#
#   name  = "Riya Sharma"
#   email = "riya.sharma@gmail.com"
#   phone = "+919876543210"
#   pin   = "400001"
#   card  = "4532 0151 1283 0366"
#
# Print:
#   Email valid   : True
#   Phone valid   : True
#   Pincode valid : True
#   Card (masked) : **** **** **** 0366
#   Balance       : ₹24,999.00

from myapp import validate_email, validate_phone
from myapp.validators import validate_pincode
from myapp.formatters import mask_card, format_currency

# --- your code here ---


# ── Exercise 2: Extend myapp — add math_helpers.py
# Real-life: Financial services module
# CREATE myapp/math_helpers.py with:
#
#   emi(principal, annual_rate, months)
#       → monthly EMI rounded to 2 decimal places
#       → formula: P·r·(1+r)^n / ((1+r)^n − 1), r = annual_rate/12/100
#
#   gst_breakdown(base_price, rate=18)
#       → returns dict: {"base": base_price, "gst": ..., "total": ...}
#
#   discount_price(price, pct)
#       → price after pct% discount
#
# Then update myapp/__init__.py to re-export emi and gst_breakdown.
# Test all three functions here.

# --- create the file, update __init__.py, then ---
# from myapp import emi, gst_breakdown
# from myapp.math_helpers import discount_price
# --- your test code here ---


# ── Exercise 3: Build a shopkit package ───────
# Real-life: E-commerce backend toolkit
# CREATE a brand-new package: shopkit/
#   shopkit/__init__.py
#   shopkit/inventory.py   — functions: add_item, remove_item, get_stock
#   shopkit/pricing.py     — functions: apply_coupon, calculate_total
#
# inventory.py:
#   STOCK = {}  (module-level dict)
#   add_item(name, qty)    → STOCK[name] = STOCK.get(name, 0) + qty
#   remove_item(name, qty) → subtract; raise ValueError if insufficient
#   get_stock(name)        → return current qty or 0
#
# pricing.py:
#   COUPONS = {"SAVE10": 10, "HALF50": 50, "FLAT100": None}
#   apply_coupon(total, code)
#       → SAVE10: 10% off, HALF50: 50% off, FLAT100: ₹100 flat off
#       → raise KeyError if invalid code
#   calculate_total(items: dict)
#       → items = {"Laptop": 2, "Mouse": 3}  (name → qty)
#       → use a PRICE dict inside pricing.py
#       → return sum of (price * qty) for all items
#
# Test from here after creating the package.

# --- your code here ---


# ── Exercise 4: __all__ control ───────────────
# Real-life: Library API design
# In myapp/__init__.py, ensure __all__ is defined.
# Then demonstrate the difference:
#
#   from myapp import *         ← only exports in __all__
#   from myapp.validators import *  ← all public names in validators
#
# Print what names become available with each form of import.
# (Hint: check dir() before and after each import in a fresh namespace,
#  or just print which names you expect and verify by using them.)

# --- your code here ---


# ─────────────────────────────────────────────
# Expected outputs (for self-check):
# Ex1: True / True / True / **** **** **** 0366 / ₹24,999.00
# Ex2: EMI, gst_breakdown, discount_price all produce correct values
# Ex3: shopkit package works with add/remove/coupon/total operations
# Ex4: __all__ controls star-import visibility
# ─────────────────────────────────────────────
