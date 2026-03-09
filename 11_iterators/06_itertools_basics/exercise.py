# ─────────────────────────────────────────────
# Exercises — itertools Basics
# ─────────────────────────────────────────────
import itertools

# ── Exercise 1: Auto-numbered order IDs ───────
# Real-life: e-commerce — assign sequential IDs to incoming orders
# Use itertools.count(1001) to number each order below.

orders = ["Laptop", "Phone", "Headphones", "Keyboard"]

# --- your code here ---
# Pair each order name with an ID from count(1001) using zip()
# Print: "Order #1001: Laptop" etc.

# Expected:
# Order #1001: Laptop
# Order #1002: Phone
# Order #1003: Headphones
# Order #1004: Keyboard


# ── Exercise 2: Round-robin task scheduler ────
# Real-life: distributing background jobs across 3 workers
# Use itertools.cycle() to assign each task to a worker.

workers = ["worker-1", "worker-2", "worker-3"]
tasks   = ["task_A", "task_B", "task_C", "task_D", "task_E", "task_F", "task_G"]

# --- your code here ---

# Expected:
# task_A → worker-1
# task_B → worker-2
# task_C → worker-3
# task_D → worker-1
# task_E → worker-2
# task_F → worker-3
# task_G → worker-1


# ── Exercise 3: Paginated results ─────────────
# Real-life: API that returns 5 results per page
# Use islice() to slice a large dataset into pages of 5.
# Print page 1, page 2, and page 3.

dataset = list(range(1, 21))        # 20 records

# --- your code here ---
# page1 = list(islice(dataset, 0, 5))
# page2 = ...
# page3 = ...

# Expected:
# Page 1: [1, 2, 3, 4, 5]
# Page 2: [6, 7, 8, 9, 10]
# Page 3: [11, 12, 13, 14, 15]


# ── Exercise 4: Merging monthly reports ───────
# Real-life: finance — combine transactions from three months
# Use itertools.chain() to merge the lists and compute the total.

january  = [12000, 8500, 3200]
february = [9400, 11000]
march    = [7800, 6500, 14000, 3100]

# --- your code here ---
# Use chain() to merge, then sum() to get total.

# Expected:
# All transactions: [12000, 8500, 3200, 9400, 11000, 7800, 6500, 14000, 3100]
# Total: 75500


# ── Exercise 5: Survey response alignment ─────
# Real-life: survey tool merging answers from optional questions
# Three question responses have different lengths.
# Use zip_longest() with fillvalue="N/A" to align them.

q1_responses = ["Yes", "No", "Yes", "Yes"]
q2_responses = ["Daily", "Weekly"]
q3_responses = ["Happy", "Neutral", "Happy"]

# --- your code here ---
# for row in zip_longest(...):
#     print(row)

# Expected:
# ('Yes', 'Daily', 'Happy')
# ('No', 'Weekly', 'Neutral')
# ('Yes', 'N/A', 'Happy')
# ('Yes', 'N/A', 'N/A')


# ── Exercise 6: Log reader ────────────────────
# Real-life: reading a log file — skip comments, stop at first CRITICAL
# Use dropwhile() to skip comment lines, then takewhile() to stop
# at the first line containing "CRITICAL".

log_lines = [
    "# system log v2",
    "# generated: 2025-01-01",
    "INFO  app started",
    "INFO  connected to DB",
    "WARNING high memory",
    "CRITICAL out of disk space",
    "INFO  attempting recovery",
]

# --- your code here ---
# Step 1: skip lines starting with "#" using dropwhile
# Step 2: stop before "CRITICAL" using takewhile
# Step 3: print remaining lines

# Expected:
# INFO  app started
# INFO  connected to DB
# WARNING high memory


# ── Exercise 7: Running cashbook ──────────────
# Real-life: accounting — cumulative balance after each transaction
# Use itertools.accumulate() to compute the running total.

transactions = [5000, -1200, -300, 8000, -450, 2000, -750]
opening_balance = 10000

# --- your code here ---
# Prepend opening_balance to transactions, then accumulate
# Print each day's closing balance.

# Expected:
# Day 0: ₹10000
# Day 1: ₹15000
# Day 2: ₹13800
# Day 3: ₹13500
# Day 4: ₹21500
# Day 5: ₹21050
# Day 6: ₹23050
# Day 7: ₹22300


# ── Exercise 8: Product catalogue variants ────
# Real-life: generating all size/colour/material combinations
# Use itertools.product() to list every variant of a T-shirt.

sizes     = ["S", "M", "L", "XL"]
colours   = ["Black", "White", "Navy"]
materials = ["Cotton", "Polyester"]

# --- your code here ---
# variants = list(product(sizes, colours, materials))
# print(f"Total variants: {len(variants)}")
# Print the first 5 variants.

# Expected:
# Total variants: 24
# ('S', 'Black', 'Cotton')
# ('S', 'Black', 'Polyester')
# ('S', 'White', 'Cotton')
# ('S', 'White', 'Polyester')
# ('S', 'Navy', 'Cotton')


# ── Exercise 9: Team selection ────────────────
# Real-life: hackathon — pick every possible pair from 5 participants
# Use itertools.combinations(participants, 2) and count the pairs.

participants = ["Aarav", "Bhavna", "Chirag", "Divya", "Eshan"]

# --- your code here ---
# pairs = list(combinations(participants, 2))
# print total pairs and list them all

# Expected:
# Total pairs: 10
# ('Aarav', 'Bhavna')
# ...all 10 pairs...


# ─────────────────────────────────────────────
# Expected outputs (for self-check): see per exercise above
# ─────────────────────────────────────────────
