# ─────────────────────────────────────────────
# Exercises — match-case  (Python 3.10+)
# ─────────────────────────────────────────────

# ── Exercise 1: Payment Gateway Router ────────
# Real-life: Fintech payment system
# Route based on payment_method:
# "upi"          → "Processing UPI payment..."
# "credit_card"  → "Processing Credit Card payment..."
# "debit_card"   → "Processing Debit Card payment..."
# "net_banking"  → "Processing Net Banking payment..."
# "wallet"       → "Processing Wallet payment..."
# anything else  → "Payment method not supported."

payment_method = "upi"

# --- your match-case here ---


# ── Exercise 2: Pizza Order Size + Crust ──────
# Real-life: Food ordering app
# Match a tuple (size, crust):
# ("small",  "thin")   → "Small thin crust — ₹199"
# ("medium", "thin")   → "Medium thin crust — ₹299"
# ("medium", "thick")  → "Medium thick crust — ₹349"
# ("large",  _)        → "Large pizza (any crust) — ₹449"
# (_,         _)       → "Invalid order."

order = ("medium", "thick")

# --- your match-case here ---


# ── Exercise 3: Student Grade with Guard ──────
# Real-life: University grading system
# Use guards to assign GPA:
# marks >= 90          → "O  — Outstanding (GPA 10.0)"
# marks >= 75          → "A+ — Excellent (GPA 9.0)"
# marks >= 60          → "A  — Very Good (GPA 8.0)"
# marks >= 50          → "B+ — Good (GPA 7.0)"
# marks >= 40          → "B  — Average (GPA 6.0)"
# marks < 40           → "F  — Fail (GPA 0.0)"

marks = 78

# --- your match-case with guards here ---


# ── Exercise 4: API Response Handler ──────────
# Real-life: Backend response processor
# Match the response dict:
# {"status": "success", "data": data}  → "Data received: {data}"
# {"status": "error", "code": code}    → "Error {code}: Request failed."
# {"status": "pending"}                → "Request is processing..."
# anything else                        → "Unexpected response format."

response = {"status": "error", "code": 422}

# --- your match-case here ---


# ── Exercise 5: Weekday Scheduler ─────────────
# Real-life: Smart calendar assistant
# Match day_number (1=Mon ... 7=Sun):
# 1 | 2       → "Early week — schedule planning meetings"
# 3           → "Midweek — team stand-up day"
# 4 | 5       → "End of week — wrap up and review"
# 6 | 7       → "Weekend — no meetings scheduled"
# anything else → "Invalid day number."

day_number = 3

# --- your match-case here ---


# ─────────────────────────────────────────────
# Expected outputs:
# Ex1: Processing UPI payment...
# Ex2: Medium thick crust — ₹349
# Ex3: A+ — Excellent (GPA 9.0)
# Ex4: Error 422: Request failed.
# Ex5: Midweek — team stand-up day
# ─────────────────────────────────────────────
