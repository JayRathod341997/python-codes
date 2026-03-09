# ─────────────────────────────────────────────
# Exercises — Conditional Comprehensions
# ─────────────────────────────────────────────

# ── Exercise 1: Filter Passing Scores ─────────
# Real-life: Exam result processing
# Keep only scores ≥ 40 (passing mark).

scores = [85, 32, 67, 40, 19, 90, 55, 38, 72]

# --- your code here ---


# ── Exercise 2: Classify Temperatures ────────
# Real-life: Weather app alerts
# Label each temperature:
#   >= 40  → "Extreme Heat"
#   >= 30  → "Hot"
#   >= 20  → "Warm"
#   else   → "Cool"
# Return a list of labels (same length as input).

temps = [15, 22, 35, 42, 28, 18, 39]

# --- your code here ---


# ── Exercise 3: Premium Customers ─────────────
# Real-life: CRM — identify customers who spent > ₹5000
# Return a list of their names only.

customers = [
    {"name": "Riya",    "total_spent": 8500},
    {"name": "Arjun",   "total_spent": 3200},
    {"name": "Meera",   "total_spent": 12000},
    {"name": "Kabir",   "total_spent": 4999},
    {"name": "Sneha",   "total_spent": 6700},
]

# --- your code here ---


# ── Exercise 4: Password Strength Tagger ──────
# Real-life: Sign-up form validation
# Tag each password: "strong" if len >= 8 AND has a digit, else "weak".

passwords = ["abc123", "hello", "P@ssw0rd", "12345678", "qwerty1!", "hi"]

# --- your code here ---
# Hint: use any(c.isdigit() for c in p) to check for digits


# ── Exercise 5: Discount Pricing ──────────────
# Real-life: Flash sale — items priced > ₹500 get 20% off; others stay the same.
# Return a new price list (round to 2 decimal places).

prices = [199, 599, 999, 349, 1200, 450, 750]

# --- your code here ---


# ─────────────────────────────────────────────
# Expected outputs (for self-check):
# Ex1: [85, 67, 40, 90, 55, 72]
# Ex2: ['Cool', 'Warm', 'Hot', 'Extreme Heat', 'Warm', 'Cool', 'Hot']
# Ex3: ['Riya', 'Meera', 'Sneha']
# Ex4: ['strong', 'weak', 'strong', 'strong', 'strong', 'weak']
# Ex5: [199, 479.2, 799.2, 349, 960.0, 450, 600.0]
# ─────────────────────────────────────────────
