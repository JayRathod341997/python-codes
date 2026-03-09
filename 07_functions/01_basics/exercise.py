# ─────────────────────────────────────────────
# Exercises — Function Basics
# ─────────────────────────────────────────────

# ── Exercise 1: Temperature Converter ────────
# Real-life: Weather app unit toggle
# Write a function celsius_to_fahrenheit(c) that converts
# Celsius to Fahrenheit using: F = (C × 9/5) + 32
# Print the result for 0°C, 37°C, and 100°C.

# --- your code here ---


# ── Exercise 2: Discount Price Calculator ────
# Real-life: E-commerce product page
# Write a function final_price(original, discount_pct)
# that returns the price after applying the discount.
# Print final price for:
#   original=1200, discount=15%
#   original=4999, discount=30%

# --- your code here ---


# ── Exercise 3: OTP Generator ────────────────
# Real-life: Banking / login OTP
# Write a function generate_otp(length) that returns a
# random numeric string of the given length.
# Hint: use random.randint(0, 9) in a loop, or random.choices.
# Print two 6-digit OTPs.

import random

# --- your code here ---


# ── Exercise 4: Loan EMI Summary ─────────────
# Real-life: Bank loan application screen
# Write a function loan_summary(principal, annual_rate, months)
# that prints a formatted summary:
#
#   Loan Summary
#   ─────────────────────────
#   Principal  : ₹5,00,000
#   Rate       : 8.5% p.a.
#   Tenure     : 60 months
#   Monthly EMI: ₹10,245.64
#   Total Pay  : ₹6,14,738.40
#   Interest   : ₹1,14,738.40
#
# EMI formula: P × r × (1+r)^n / ((1+r)^n − 1)  where r = annual_rate/12/100

# --- your code here ---


# ── Exercise 5: Password Strength Checker ────
# Real-life: Sign-up form validation
# Write a function check_password_strength(password) that
# returns one of: "Weak", "Medium", "Strong"
#
# Rules:
#   Weak   — length < 6
#   Medium — length 6-11  OR  no digit/special char
#   Strong — length ≥ 12  AND has digit AND has special char (!@#$%^&*)
#
# Include a proper docstring.
# Test with: "abc", "hello123", "MyP@ssw0rd2024!"

# --- your code here ---


# ─────────────────────────────────────────────
# Expected outputs (for self-check):
# Ex1: 32.0°F  |  98.6°F  |  212.0°F
# Ex2: ₹1020.0  |  ₹3499.3
# Ex3: Any two 6-digit random number strings
# Ex4: Formatted block as shown above
# Ex5: Weak  |  Medium  |  Strong
# ─────────────────────────────────────────────
