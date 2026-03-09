# ─────────────────────────────────────────────
# Exercises — collections
# ─────────────────────────────────────────────

from collections import Counter, defaultdict, deque, namedtuple, OrderedDict

# ── Exercise 1: Log Analyser (Counter) ────────
# Real-life: Web server / app monitoring
# Given the access log below, use Counter to:
#   a) Count requests per endpoint
#   b) Count requests per HTTP status code
#   c) Find the top-3 most accessed endpoints
#   d) Find how many unique IPs made requests
#   e) Count requests per hour (extract hour from timestamp)

logs = [
    {"ip": "192.168.1.1", "ts": "2024-01-15 09:12:33", "endpoint": "/home",     "status": 200},
    {"ip": "192.168.1.2", "ts": "2024-01-15 09:45:01", "endpoint": "/login",    "status": 200},
    {"ip": "192.168.1.1", "ts": "2024-01-15 10:02:15", "endpoint": "/products", "status": 200},
    {"ip": "192.168.1.3", "ts": "2024-01-15 10:15:44", "endpoint": "/login",    "status": 401},
    {"ip": "192.168.1.2", "ts": "2024-01-15 10:30:22", "endpoint": "/home",     "status": 200},
    {"ip": "192.168.1.4", "ts": "2024-01-15 11:00:05", "endpoint": "/cart",     "status": 200},
    {"ip": "192.168.1.1", "ts": "2024-01-15 11:22:10", "endpoint": "/home",     "status": 200},
    {"ip": "192.168.1.3", "ts": "2024-01-15 11:45:33", "endpoint": "/login",    "status": 200},
    {"ip": "192.168.1.5", "ts": "2024-01-15 11:59:59", "endpoint": "/products", "status": 404},
]

# --- your code here ---


# ── Exercise 2: Student Grade Book (defaultdict) ─
# Real-life: School management system
# Use defaultdict to:
#   a) Group students by subject (each student takes multiple subjects)
#   b) Build a grade index: {student: [list of (subject, score) tuples]}
#   c) Compute each student's average score
#   d) Find which students failed any subject (score < 40)
#
# Print a report card for each student.

results = [
    ("Alice", "Math",    88), ("Alice", "Science", 72), ("Alice", "English", 91),
    ("Bob",   "Math",    55), ("Bob",   "Science", 38), ("Bob",   "English", 67),
    ("Carol", "Math",    95), ("Carol", "Science", 88), ("Carol", "English", 79),
    ("Dave",  "Math",    32), ("Dave",  "Science", 45), ("Dave",  "English", 50),
]

# --- your code here ---


# ── Exercise 3: Browser History (deque) ───────
# Real-life: Web browser back/forward navigation
# Implement a BrowserHistory class using two deques:
#   back_stack  (deque)
#   forward_stack (deque)
#
# Methods:
#   visit(url)    — go to new URL, clear forward history
#   back()        — go back one page (print current page or "No history")
#   forward()     — go forward one page
#   current()     — print current page
#
# Simulate:
#   visit("google.com")
#   visit("youtube.com")
#   visit("github.com")
#   back()      → youtube.com
#   back()      → google.com
#   forward()   → youtube.com
#   visit("stackoverflow.com")   # clears forward
#   forward()   → "No forward history"

# --- your code here ---


# ── Exercise 4: Product Catalogue (namedtuple) ─
# Real-life: E-commerce inventory system
# Define a namedtuple Product(id, name, category, price, stock)
# and OrderItem(product, quantity, discount_pct)
#
# Functions:
#   line_total(item: OrderItem) → price * qty * (1 - discount/100)
#   order_summary(items: list[OrderItem]) → print formatted invoice
#
# Inventory:
#   P001 Laptop     Electronics  75000  10
#   P002 Mouse      Accessories    799  50
#   P003 Keyboard   Accessories   2499  30
#   P004 Monitor    Electronics  22000   8
#
# Create an order: 1×Laptop(5% off), 2×Mouse(10% off), 1×Keyboard
# Print:
#   ─────────────────────────────────────────
#   Order Invoice
#   ─────────────────────────────────────────
#   Product          Qty  Price    Disc  Total
#   Laptop             1  ₹75,000   5%  ₹71,250.00
#   Mouse              2  ₹799     10%  ₹1,438.20
#   Keyboard           1  ₹2,499    0%  ₹2,499.00
#   ─────────────────────────────────────────
#   Grand Total                         ₹75,187.20

Product   = namedtuple("Product",   ["id", "name", "category", "price", "stock"])
OrderItem = namedtuple("OrderItem", ["product", "quantity", "discount_pct"], defaults=[0])

# --- your code here ---


# ── Exercise 5: Sliding Window Analytics (deque) ─
# Real-life: Real-time metrics dashboard (CPU, stock price, sensor data)
# Write a function stream_stats(data, window_size) that processes
# a stream of values and at each step prints:
#
#   Step  5 | Window: [102, 98, 105, 110, 108] | Avg: 104.6 | Min: 98  | Max: 110
#   Step  6 | Window: [98, 105, 110, 108, 115]  | Avg: 107.2 | Min: 98  | Max: 115
#   ...
#
# Use deque(maxlen=window_size) for the sliding window.
# Test with stock prices and window=5:

stock_prices = [100, 102, 98, 105, 110, 108, 115, 112, 118, 120, 117, 122]

# --- your code here ---


# ─────────────────────────────────────────────
# Expected outputs (for self-check):
# Ex1: endpoint counts | status counts | top-3 | unique IPs | hourly
# Ex2: report cards with avg and fail flags
# Ex3: browser navigation works correctly
# Ex4: formatted invoice with correct totals
# Ex5: sliding window stats for each step
# ─────────────────────────────────────────────
