# ─────────────────────────────────────────────
# Exercises — Built-in Iterators
# ─────────────────────────────────────────────

# ── Exercise 1: Numbered invoice ──────────────
# Real-life: billing system
# Given a list of items and prices, print a numbered invoice
# using enumerate() starting from 1.

items  = ["Laptop", "Mouse", "HDMI Cable", "USB Hub"]
prices = [75000, 800, 350, 1200]

# --- your code here ---

# Expected:
# 1. Laptop         ₹75000
# 2. Mouse          ₹800
# 3. HDMI Cable     ₹350
# 4. USB Hub        ₹1200


# ── Exercise 2: Score card ────────────────────
# Real-life: exam result system
# Pair student names with their scores using zip().
# Print: "<name>: <score> — <PASS/FAIL>" (pass mark: 50)

names  = ["Arjun", "Priya", "Karan", "Sneha", "Dev"]
scores = [72, 45, 88, 51, 39]

# --- your code here ---

# Expected:
# Arjun: 72 — PASS
# Priya: 45 — FAIL
# Karan: 88 — PASS
# Sneha: 51 — PASS
# Dev:   39 — FAIL


# ── Exercise 3: Price converter ───────────────
# Real-life: e-commerce — convert USD prices to INR
# Use map() to multiply each price by the exchange rate (83.5).
# Round to 2 decimal places.

usd_prices   = [9.99, 29.99, 4.49, 14.99, 49.99]
exchange_rate = 83.5

# --- your code here ---
# inr_prices = list(map(...))
# print(inr_prices)

# Expected: [834.17, 2503.17, 374.92, 1251.67, 4174.17]


# ── Exercise 4: Active users only ─────────────
# Real-life: sending a newsletter to active subscribers
# Use filter() to keep only users where "active" is True,
# then print their names.

users = [
    {"name": "Alice",   "active": True},
    {"name": "Bob",     "active": False},
    {"name": "Carol",   "active": True},
    {"name": "Dave",    "active": False},
    {"name": "Eve",     "active": True},
]

# --- your code here ---
# active_users = list(filter(...))
# for u in active_users: print(u["name"])

# Expected:
# Alice
# Carol
# Eve


# ── Exercise 5: Undo history ──────────────────
# Real-life: text editor — show last N actions in reverse order
# Use reversed() to display the last 3 actions in reverse.

actions = ["open_file", "type_text", "apply_bold", "save", "undo", "redo"]

# --- your code here ---
# Print last 3 actions (from the end) in reverse using reversed()

# Expected:
# redo
# undo
# save


# ── Exercise 6: Config diff ───────────────────
# Real-life: deployment tool comparing old vs new config
# Given two config dicts, use zip(dict.items()) or map()
# to find keys whose values changed.

old_config = {"host": "localhost", "port": 8080, "debug": True,  "timeout": 30}
new_config = {"host": "localhost", "port": 9090, "debug": False, "timeout": 30}

# --- your code here ---
# Compare key by key using zip(old_config.items(), new_config.items())
# Print only the keys that changed and their old → new values.

# Expected:
# port    changed: 8080 → 9090
# debug   changed: True → False


# ── Exercise 7: Lazy pipeline ─────────────────
# Real-life: data processing — chain map + filter + enumerate lazily
# Start with raw log entries. Use map to strip whitespace,
# filter to keep only lines containing "ERROR",
# then enumerate to number them.

raw_logs = [
    "  INFO: server started  ",
    "  ERROR: connection refused  ",
    "  INFO: health check ok  ",
    "  ERROR: timeout exceeded  ",
    "  WARNING: high memory  ",
    "  ERROR: disk full  ",
]

# --- your code here ---
# 1. stripped  = map(str.strip, raw_logs)
# 2. errors    = filter(lambda line: "ERROR" in line, stripped)
# 3. numbered  = enumerate(errors, start=1)
# for i, line in numbered: print(i, line)

# Expected:
# 1 ERROR: connection refused
# 2 ERROR: timeout exceeded
# 3 ERROR: disk full


# ─────────────────────────────────────────────
# Expected outputs (for self-check): see above per exercise
# ─────────────────────────────────────────────
