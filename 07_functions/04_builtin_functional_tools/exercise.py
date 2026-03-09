# ─────────────────────────────────────────────
# Exercises — map / filter / reduce
# ─────────────────────────────────────────────

from functools import reduce

# ── Exercise 1: Payroll Calculator (map) ──────
# Real-life: HR payroll system
# Given employee records below, use map() to produce a new list
# of dicts with an added "net_salary" key:
#   net_salary = gross - (gross * tax_rate / 100) - pf_deduction
# where pf_deduction = 1800 (fixed) for all.
# Print each employee's name and net_salary.
#
# Expected:
#   Alice   → ₹62,200.00
#   Bob     → ₹80,200.00
#   Carol   → ₹44,200.00

employees = [
    {"name": "Alice", "gross": 75000, "tax_rate": 15},
    {"name": "Bob",   "gross": 95000, "tax_rate": 12},
    {"name": "Carol", "gross": 52000, "tax_rate": 10},
]

# --- your code here ---


# ── Exercise 2: Product Filter (filter) ───────
# Real-life: Mobile shopping app with filters
# From the products list, use filter() to extract:
#   a) Products with price ≤ 1500  AND  rating ≥ 4.3
#   b) Products whose name contains "Pro" (case-insensitive)
# Print both filtered lists.

products = [
    {"name": "AirBuds Pro",    "price": 1299, "rating": 4.6},
    {"name": "SmartWatch",     "price": 3999, "rating": 4.4},
    {"name": "Neckband Plus",  "price": 799,  "rating": 4.1},
    {"name": "Speaker Pro",    "price": 1499, "rating": 4.5},
    {"name": "Fitness Band",   "price": 2499, "rating": 4.2},
    {"name": "Earphones",      "price": 599,  "rating": 4.3},
]

# --- your code here ---


# ── Exercise 3: Invoice Total (reduce) ────────
# Real-life: Billing system
# Use reduce() to:
#   a) Sum up all invoice amounts
#   b) Find the invoice with the maximum amount (as a dict)
#   c) Concatenate all invoice IDs into one string: "INV001-INV002-INV003-..."
# Print all three results.

invoices = [
    {"id": "INV001", "amount": 4500},
    {"id": "INV002", "amount": 12000},
    {"id": "INV003", "amount": 850},
    {"id": "INV004", "amount": 7300},
    {"id": "INV005", "amount": 3200},
]

# --- your code here ---


# ── Exercise 4: Pipeline — Sales Report ───────
# Real-life: Monthly sales analytics
# Using map(), filter(), and reduce() together (no list comprehensions):
#
# From transactions below:
#   1. filter  — keep only "completed" transactions
#   2. map     — apply 5% platform fee: net = amount * 0.95
#   3. reduce  — sum all net amounts → total_payout
#
# Also find the average net payout per completed transaction.
# Print total and average rounded to 2 decimal places.

transactions = [
    {"id": "T01", "status": "completed", "amount": 8500},
    {"id": "T02", "status": "refunded",  "amount": 1200},
    {"id": "T03", "status": "completed", "amount": 4300},
    {"id": "T04", "status": "pending",   "amount": 950},
    {"id": "T05", "status": "completed", "amount": 6700},
    {"id": "T06", "status": "completed", "amount": 2100},
    {"id": "T07", "status": "refunded",  "amount": 3400},
]

# --- your code here ---


# ── Exercise 5: Grade Report (all three) ──────
# Real-life: School management system
# Given student records:
#   1. map     — add "grade" key: A(≥85), B(70-84), C(55-69), D(<55)
#   2. filter  — keep only students who passed (score ≥ 55)
#   3. reduce  — compute class average score of passing students
# Print the final list of passing students with their grade,
# then print the class average.

students = [
    {"name": "Riya",   "score": 91},
    {"name": "Arjun",  "score": 48},
    {"name": "Priya",  "score": 73},
    {"name": "Dev",    "score": 55},
    {"name": "Meera",  "score": 82},
    {"name": "Karan",  "score": 38},
    {"name": "Sneha",  "score": 67},
]

# --- your code here ---


# ─────────────────────────────────────────────
# Expected outputs (for self-check):
# Ex1: Alice ₹62,200.00 | Bob ₹80,200.00 | Carol ₹44,200.00
# Ex2a: AirBuds Pro, Speaker Pro, Earphones
# Ex2b: AirBuds Pro, Speaker Pro
# Ex3a: ₹27,850  Ex3b: INV002  Ex3c: INV001-INV002-INV003-INV004-INV005
# Ex4: Total payout ₹20,425.00 | Average ₹5,106.25
# Ex5: Riya A | Priya B | Dev C | Meera B | Sneha C | Class avg: 73.6
# ─────────────────────────────────────────────
