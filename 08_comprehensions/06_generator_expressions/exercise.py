# ─────────────────────────────────────────────
# Exercises — Generator Expressions
# ─────────────────────────────────────────────

# ── Exercise 1: Total Revenue (large dataset) ─
# Real-life: Sales analytics
# Use a generator expression with sum() to calculate total revenue.
# Do NOT use a list comprehension — avoid building an intermediate list.

sales = [1500, 2300, 800, 4500, 300, 1200, 6700, 950]

# --- your code here ---
# total_revenue = sum(...)


# ── Exercise 2: Any Failed Payment? ───────────
# Real-life: Payment gateway monitor
# Use any() with a generator to check if any transaction has status "failed".
# Print True/False.

transactions = [
    {"id": "T1", "amount": 500,  "status": "success"},
    {"id": "T2", "amount": 200,  "status": "success"},
    {"id": "T3", "amount": 1500, "status": "pending"},
    {"id": "T4", "amount": 300,  "status": "success"},
]

# --- your code here ---


# ── Exercise 3: All Deliveries On Time? ───────
# Real-life: Logistics dashboard
# Use all() with a generator to check if every delivery arrived on or before
# its deadline (arrived_day <= deadline_day).

deliveries = [
    {"id": "D1", "arrived": 3, "deadline": 5},
    {"id": "D2", "arrived": 6, "deadline": 5},
    {"id": "D3", "arrived": 4, "deadline": 4},
]

# --- your code here ---


# ── Exercise 4: First Suspicious Login ────────
# Real-life: Security — find the first login attempt from an unknown device
# Use next() with a generator to get the first record where
# known_device is False. If none found, return "All devices recognised".

logins = [
    {"user": "alice", "known_device": True},
    {"user": "bob",   "known_device": True},
    {"user": "carol", "known_device": False},
    {"user": "dave",  "known_device": False},
]

# --- your code here ---
# Hint: next((item for item in ... if ...), default_value)


# ── Exercise 5: Lazy Email Pipeline ───────────
# Real-life: Newsletter service
# Chain three generator expressions (do NOT use list comprehensions):
#   Step 1 — strip whitespace from each email
#   Step 2 — convert to lowercase
#   Step 3 — keep only emails that contain "@"
# Finally convert to a list and print.

raw_emails = ["  ALICE@Gmail.com", "not-an-email  ", " BOB@Yahoo.COM ", "broken"]

# --- your code here ---
# step1 = (... for e in raw_emails)
# step2 = (... for e in step1)
# step3 = (... for e in step2 if ...)
# print(list(step3))


# ─────────────────────────────────────────────
# Expected outputs (for self-check):
# Ex1: 18250
# Ex2: False
# Ex3: False  (D2 arrived late)
# Ex4: {'user': 'carol', 'known_device': False}
# Ex5: ['alice@gmail.com', 'bob@yahoo.com']
# ─────────────────────────────────────────────
