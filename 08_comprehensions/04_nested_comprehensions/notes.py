# ─────────────────────────────────────────────
# Nested Comprehensions
# ─────────────────────────────────────────────

# ── Syntax ───────────────────────────────────
# [expr  for outer in outer_iter  for inner in inner_iter]
# Equivalent loop order (OUTER first, then INNER — left to right):
#   result = []
#   for outer in outer_iter:
#       for inner in inner_iter:
#           result.append(expr)

# ── Flatten a 2-D list ────────────────────────
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat   = [num for row in matrix for num in row]
print(flat)     # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# ── Real-life 1: Sales data roll-up ──────────
# Retail — each store has a list of daily sales figures.
# Flatten all sales into one list for global analysis.
store_sales = [
    [1200, 1500, 900],      # Store A — Mon, Tue, Wed
    [800,  1100, 1300],     # Store B
    [2000, 1800, 1600],     # Store C
]
all_sales = [sale for store in store_sales for sale in store]
print(all_sales)        # [1200, 1500, 900, 800, 1100, 1300, 2000, 1800, 1600]
print(f"Total revenue: ₹{sum(all_sales):,}")    # ₹12,200

# ── Real-life 2: Seating chart ────────────────
# Cinema / stadium — generate all seat labels (Row A-C, Seat 1-5)
rows  = ["A", "B", "C"]
seats = [1, 2, 3, 4, 5]
seat_labels = [f"{row}{seat}" for row in rows for seat in seats]
print(seat_labels)
# ['A1', 'A2', 'A3', 'A4', 'A5', 'B1', ..., 'C5']

# ── Real-life 3: Tag list from blog posts ─────
# CMS — each post has multiple tags; flatten to one list
posts = [
    {"title": "Python Tips",    "tags": ["python", "tips"]},
    {"title": "Git Workflow",   "tags": ["git", "devops", "tips"]},
    {"title": "SQL Basics",     "tags": ["sql", "database"]},
]
all_tags = [tag for post in posts for tag in post["tags"]]
print(all_tags)     # ['python', 'tips', 'git', 'devops', 'tips', 'sql', 'database']

# ── Nested comprehension (list of lists) ─────
# Transpose a matrix — rows become columns
matrix   = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed = [[row[i] for row in matrix] for i in range(3)]
print(transposed)   # [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

# ── Real-life 4: Multiplication table ────────
# Education app
table = [[i * j for j in range(1, 6)] for i in range(1, 6)]
for row in table:
    print(row)
# [1, 2, 3, 4, 5]
# [2, 4, 6, 8, 10]
# ...

# ── Real-life 5: Flatten order line items ─────
# E-commerce — each order has multiple items; get all item names
orders = [
    {"order_id": "ORD01", "items": ["Laptop", "Mouse"]},
    {"order_id": "ORD02", "items": ["Pen", "Notebook", "Eraser"]},
    {"order_id": "ORD03", "items": ["Keyboard"]},
]
all_items = [item for order in orders for item in order["items"]]
print(all_items)    # ['Laptop', 'Mouse', 'Pen', 'Notebook', 'Eraser', 'Keyboard']

# ── Key points ───────────────────────────────
# • Read the for clauses left-to-right — same order as nested loops
# • Two patterns:
#     [expr for a in A for b in B]     → flat list (like nested loops)
#     [[expr for b in B] for a in A]   → list of lists (2-D structure)
# • Don't nest more than 2 levels — readability suffers; use a function instead
# • The outer comprehension is evaluated first (leftmost for clause)
