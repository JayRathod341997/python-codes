# ─────────────────────────────────────────────
# Exercises — math & random
# ─────────────────────────────────────────────

import math
import random
import secrets

# ── Exercise 1: Financial Calculator ─────────
# Real-life: Banking / investment app
# Write these functions using the math module:
#
# a) future_value(principal, annual_rate, years, n=12)
#    → compound interest, compounded n times per year
#    → returns final amount rounded to 2 decimal places
#
# b) break_even_units(fixed_cost, selling_price, variable_cost)
#    → units = math.ceil(fixed_cost / (selling_price - variable_cost))
#
# c) loan_interest_total(principal, annual_rate, months)
#    → total interest paid over loan life
#    → use EMI formula: P·r·(1+r)^n / ((1+r)^n − 1)
#    → total_paid = emi * months; interest = total_paid - principal
#
# Test:
#   future_value(100_000, 8, 10)        → ₹2,21,964.00
#   break_even_units(50000, 250, 150)   → 500 units
#   loan_interest_total(5_00_000, 9, 60)→ Interest: ₹1,25,226.72

# --- your code here ---


# ── Exercise 2: Geometry Toolkit ─────────────
# Real-life: Architecture / game dev / CAD tool
# Write a function shape_report(shape, **dims) that computes
# area and perimeter for:
#   circle(radius)
#   rectangle(width, height)
#   triangle(a, b, c)   — sides; area via Heron's formula
#   sector(radius, angle_deg)  — pizza slice
#
# Use math.pi, math.sqrt, math.radians, math.sin.
# Print:
#   Shape     : Circle
#   Radius    : 7
#   Area      : 153.94 cm²
#   Perimeter : 43.98 cm

# --- your code here ---


# ── Exercise 3: Secure Token Generator ───────
# Real-life: Auth service — tokens, OTPs, passwords, UUIDs
# Write:
#   generate_otp(length=6)      → numeric string (use random.choices)
#   generate_token(bytes=32)    → hex token (use secrets.token_hex)
#   generate_password(length=16)→ mix of upper, lower, digits, symbols
#                                  (use secrets.choice, ensure at least
#                                   1 upper, 1 lower, 1 digit, 1 symbol)
#   roll_dice(n=1, sides=6)     → list of n dice rolls
#
# Print samples of each.
# Run generate_otp() 5 times with seed=99 — show reproducibility.

# --- your code here ---


# ── Exercise 4: Random Simulation ────────────
# Real-life: Monte Carlo method — estimate π
# The area of a unit circle = π. If we randomly scatter N points
# in a 1×1 square, the fraction that falls inside the quarter-circle
# (x²+y²≤1) ≈ π/4.
#
# Write monte_carlo_pi(n_points) that:
#   - generates n_points random (x, y) pairs in [0,1]×[0,1]
#   - counts how many satisfy x²+y² ≤ 1
#   - returns the π estimate = 4 * inside / n_points
#
# Print estimates for n = 1_000, 10_000, 100_000, 1_000_000
# Show error vs math.pi for each.
# (Use random.seed(0) for reproducibility.)

# --- your code here ---


# ── Exercise 5: Weighted Lucky Draw ──────────
# Real-life: E-commerce spin-to-win / lottery feature
# Define prizes with weights (higher weight = more likely):
#
#   prizes = [
#       ("₹5,000 cash",    1),
#       ("₹500 coupon",    5),
#       ("Free shipping",  20),
#       ("10% off",        40),
#       ("Better luck!",   34),
#   ]
#
# a) Simulate 10,000 spins and print how many times each prize was won
#    as count and percentage.
# b) Write a function spin_wheel(prizes) → single result using
#    random.choices with weights.
# c) Find the minimum number of spins needed to win ₹5,000 at least once
#    (simulate until it happens, print spin count).
#    Run 5 trials, print each count.

prizes = [
    ("₹5,000 cash",    1),
    ("₹500 coupon",    5),
    ("Free shipping",  20),
    ("10% off",        40),
    ("Better luck!",   34),
]

# --- your code here ---


# ─────────────────────────────────────────────
# Expected outputs (for self-check):
# Ex1: ₹2,21,964.00 | 500 units | ₹1,25,226.72 interest
# Ex2: Correct areas/perimeters for each shape
# Ex3: Sample OTPs, tokens, passwords; same OTPs with seed=99
# Ex4: π estimates converging toward 3.14159... as N increases
# Ex5: Distribution close to weights; spin_wheel works; trial counts vary
# ─────────────────────────────────────────────
