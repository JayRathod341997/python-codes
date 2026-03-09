# ─────────────────────────────────────────────
# Exercises — break, continue, pass
# ─────────────────────────────────────────────

# ── Exercise 1: Quality Control Line ──────────
# Real-life: Factory assembly line
# items = list of weights in grams
# Acceptable range: 95g – 105g
# Use continue to skip items outside range (mark as rejected)
# Use break if 3 consecutive items are rejected (halt the line)
# Print each item's status and final summary.

items = [100, 98, 103, 88, 92, 112, 99, 101, 97]

rejected_streak  = 0
total_accepted   = 0
total_rejected   = 0

# --- your for loop with break/continue here ---


# ── Exercise 2: Duplicate Transaction Detector ─
# Real-life: Banking fraud detection
# transactions = list of (txn_id, amount) tuples
# Skip (continue) any txn with amount <= 0 (invalid)
# Stop (break) immediately when a duplicate txn_id is found, print alert
# Print all valid, non-duplicate transactions

transactions = [
    ("T001", 500),
    ("T002", 1200),
    ("T003", -50),      # invalid
    ("T004", 800),
    ("T002", 1200),     # duplicate!
    ("T005", 300),
]

seen_ids = set()

# --- your for loop here ---


# ── Exercise 3: Prime Number Finder ───────────
# Real-life: Cryptography key generation
# Find all prime numbers between 2 and 50.
# For each number, use a for loop with break to check divisibility.
# If divisible by any number → not prime (break early).

primes = []

for num in range(2, 51):
    # --- inner loop with break ---
    pass    # replace pass with your logic

print(f"Primes up to 50: {primes}")
# Expected: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]


# ── Exercise 4: CSV Data Cleaner ──────────────
# Real-life: Data pipeline preprocessing
# raw_rows = list of strings (simulated CSV rows)
# Rules:
#   - Skip rows that start with "#" (comments)   → continue
#   - Skip empty rows ("")                         → continue
#   - Stop processing if row contains "EOF"        → break
#   - Otherwise, strip and print the row

raw_rows = [
    "# This is a header comment",
    "Jay,28,Developer",
    "",
    "Priya,25,Designer",
    "# Another comment",
    "Rohan,30,Manager",
    "EOF",
    "This should not appear",
]

print("Cleaned data:")
# --- your for loop here ---


# ── Exercise 5: Stub Out Feature Flags ────────
# Real-life: Feature flag system during development
# features = list of feature names
# For each feature:
#   - "dark_mode"   → print "Dark mode enabled"
#   - "beta_chat"   → pass (not implemented yet)
#   - "analytics"   → print "Analytics dashboard loaded"
#   - anything else → pass (unknown feature, ignore)

features = ["dark_mode", "beta_chat", "analytics", "experimental_ai"]

for feature in features:
    # --- your if/elif chain with pass here ---
    pass


# ─────────────────────────────────────────────
# Expected outputs (key lines):
# Ex1: Line halted after 3 consecutive rejections
# Ex2: Duplicate detected! TXN T002 — fraud alert raised.
# Ex3: Primes up to 50: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
# Ex4: 4 data rows printed (no comments, no empty, no EOF or after)
# Ex5: Dark mode enabled / Analytics dashboard loaded (beta_chat silently skipped)
# ─────────────────────────────────────────────
