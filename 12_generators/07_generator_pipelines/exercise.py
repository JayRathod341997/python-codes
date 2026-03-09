# ─────────────────────────────────────────────
# Exercises — Generator Pipelines
# ─────────────────────────────────────────────

# ── Exercise 1: Three-stage number pipeline ───
# Real-life: basic ETL understanding
# Build a three-stage pipeline using generator functions:
#   Stage 1 — source(data):        yield each item
#   Stage 2 — drop_negatives(gen): yield only items >= 0
#   Stage 3 — double(gen):         yield each item * 2
# Run it on the list below and collect into a list.

raw = [3, -1, 7, -4, 0, 5, -2, 8]

# --- your code here ---


# Expected output:
# [6, 14, 0, 10, 16]


# ── Exercise 2: CSV pipeline ──────────────────
# Real-life: importing product data from a supplier CSV
# Build a pipeline with these stages:
#   Stage 1 — skip_header(rows):      skip first row
#   Stage 2 — parse_row(rows):        split by comma, strip whitespace;
#                                      yield dict with keys: name, price, stock
#   Stage 3 — in_stock_only(records): yield only where stock > 0
#   Stage 4 — apply_discount(records, pct): reduce price by pct%
# Print name and discounted price for each in-stock item.

csv_rows = [
    "name,price,stock",
    "Laptop,   999.99, 5",
    "Mouse,     29.99, 0",
    "Monitor,  349.99, 3",
    "Keyboard,  79.99, 0",
    "Webcam,    59.99, 8",
]
DISCOUNT_PCT = 10   # 10% off

# --- your code here ---


# Expected output:
# Laptop    $899.99
# Monitor   $314.99
# Webcam     $53.99


# ── Exercise 3: Log pipeline ──────────────────
# Real-life: security audit — find unique IPs with failed logins
# Build a pipeline:
#   Stage 1 — only_failures(lines):  yield lines containing "FAILED"
#   Stage 2 — extract_ip(lines):     yield just the IP (word at index 2)
#   Stage 3 — deduplicate(ips):      yield each IP only once (preserve order)
# Collect IPs into a list.

auth_logs = [
    "Jan 10 08:01 sshd FAILED login from 192.168.1.10",
    "Jan 10 08:02 sshd ACCEPTED login from 10.0.0.1",
    "Jan 10 08:03 sshd FAILED login from 192.168.1.10",
    "Jan 10 08:04 sshd FAILED login from 172.16.0.5",
    "Jan 10 08:05 sshd ACCEPTED login from 10.0.0.2",
    "Jan 10 08:06 sshd FAILED login from 192.168.1.15",
    "Jan 10 08:07 sshd FAILED login from 172.16.0.5",
]

# --- your code here ---


# Expected output:
# ['192.168.1.10', '172.16.0.5', '192.168.1.15']


# ── Exercise 4: Infinite pipeline with take() ─
# Real-life: generating a sample of unique order IDs for load testing
# Build a pipeline from an infinite source:
#   Stage 1 — counter(start=1): infinite integer generator
#   Stage 2 — to_order_id(gen): yield "ORD-{n:04d}"
#   Stage 3 — take(n, gen):     yield only first n items
# Print the first 6 order IDs.

# --- your code here ---


# Expected output:
# ORD-0001
# ORD-0002
# ORD-0003
# ORD-0004
# ORD-0005
# ORD-0006


# ── Exercise 5: Full ETL pipeline ─────────────
# Real-life: processing an e-commerce transaction export
# Transactions below have mixed quality. Build a full pipeline:
#   Stage 1 — parse_transactions(records):
#               yield dict {id, user, amount(float), status}
#               skip any record where amount cannot be converted
#   Stage 2 — filter_status(records, allowed):
#               yield only records whose status is in 'allowed'
#   Stage 3 — flag_large(records, threshold):
#               add key "flagged": True if amount >= threshold
#   Stage 4 — format_output(records):
#               yield formatted string
#
# Count total records processed and sum of flagged amounts.

raw_transactions = [
    {"id": "T001", "user": "alice", "amount": "250.00",  "status": "completed"},
    {"id": "T002", "user": "bob",   "amount": "N/A",     "status": "completed"},
    {"id": "T003", "user": "carol", "amount": "8500.00", "status": "completed"},
    {"id": "T004", "user": "dave",  "amount": "99.00",   "status": "refunded"},
    {"id": "T005", "user": "eve",   "amount": "1200.00", "status": "completed"},
    {"id": "T006", "user": "frank", "amount": "450.00",  "status": "pending"},
    {"id": "T007", "user": "grace", "amount": "11000.00","status": "completed"},
]

ALLOWED_STATUSES = {"completed"}
FLAG_THRESHOLD   = 1000.0

# --- your code here ---


# Expected output:
# T001  alice    $   250.00  [ ]
# T003  carol    $  8500.00  [FLAGGED]
# T005  eve      $  1200.00  [FLAGGED]
# T007  grace    $ 11000.00  [FLAGGED]
#
# Total processed : 4
# Total flagged $ : $20700.00


# ─────────────────────────────────────────────
# Self-check:
# Ex1: [6, 14, 0, 10, 16]
# Ex2: 3 items with discounted prices
# Ex3: 3 unique IPs in order of first appearance
# Ex4: ORD-0001 through ORD-0006
# Ex5: 4 completed records, 3 flagged, $20700.00
# ─────────────────────────────────────────────
