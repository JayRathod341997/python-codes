# ─────────────────────────────────────────────
# Exercises — if / elif / else
# ─────────────────────────────────────────────

# ── Exercise 1: Traffic Light System ─────────
# Real-life: Road signal controller
# Given a signal color, print the driver instruction.
# "red"    → "Stop"
# "yellow" → "Get ready"
# "green"  → "Go"
# anything else → "Invalid signal"

signal = "green"

# --- your code here ---


# ── Exercise 2: ATM PIN Validator ─────────────
# Real-life: ATM security
# correct_pin = 4821
# If entered_pin matches → "Transaction approved"
# If entered_pin is within 1000 of correct → "Almost! But wrong pin"
# Else → "Access denied. Card blocked after 3 attempts."

correct_pin   = 4821
entered_pin   = 4800

# --- your code here ---


# ── Exercise 3: Electricity Bill Calculator ───
# Real-life: DISCOM billing slab system (India)
# Units consumed → Rate per unit
#   0  – 100  →  ₹3.00
#  101 – 300  →  ₹5.00
#  301 – 500  →  ₹7.00
#  500+       →  ₹10.00
# Print the bill amount.

units = 450

# --- your code here ---


# ── Exercise 4: BMI Category ──────────────────
# Real-life: Health app
# BMI = weight(kg) / height(m)^2
# < 18.5   → Underweight
# 18.5–24.9 → Normal weight
# 25–29.9  → Overweight
# ≥ 30     → Obese

weight = 72     # kg
height = 1.75   # m

# --- your code here ---


# ── Exercise 5: Movie Ticket Pricing ─────────
# Real-life: Cinema booking system
# Age < 5          → Free
# Age 5–12         → ₹100 (child)
# Age 13–59        → ₹250 (adult)
# Age 60+          → ₹150 (senior)
# If it's weekend (is_weekend=True) add ₹50 surcharge to all paid tickets

age        = 35
is_weekend = True

# --- your code here ---


# ─────────────────────────────────────────────
# Expected outputs (for self-check):
# Ex1: Go
# Ex2: Almost! But wrong pin
# Ex3: ₹2750.00   (first 100 @ ₹3 + next 200 @ ₹5 + remaining 150 @ ₹7)
# Ex4: Normal weight
# Ex5: ₹300.00
# ─────────────────────────────────────────────
