# ─────────────────────────────────────────────
# Exercises — for Loop
# ─────────────────────────────────────────────

# ── Exercise 1: Salary Slip Generator ─────────
# Real-life: HR payroll system
# For each employee dict in the list, print a mini salary slip:
#   Name: Jay Rathod
#   Gross: ₹50,000
#   TDS (10%): ₹5,000
#   Net Pay: ₹45,000

employees = [
    {"name": "Jay Rathod",   "gross": 50_000},
    {"name": "Priya Shah",   "gross": 72_000},
    {"name": "Rohan Mehta",  "gross": 38_500},
]

TDS_RATE = 0.10

# --- your for loop here ---


# ── Exercise 2: Inventory Alert ───────────────
# Real-life: Warehouse management system
# Print items where stock < reorder_level with alert message.
# Format: "⚠ Reorder needed: {item} (Stock: {stock}, Min: {reorder})"

inventory = {
    "Laptop":    {"stock": 12, "reorder": 5},
    "Pen Drive": {"stock": 3,  "reorder": 10},
    "Monitor":   {"stock": 7,  "reorder": 7},
    "Keyboard":  {"stock": 2,  "reorder": 8},
    "Mouse":     {"stock": 15, "reorder": 10},
}

# --- your for loop here ---


# ── Exercise 3: Word Frequency Counter ────────
# Real-life: Search engine indexing / NLP preprocessing
# Count how many times each word appears in the sentence.
# (ignore case — treat "Python" and "python" as same)

sentence = "python is great and python is easy to learn and python is popular"

word_count = {}

# --- your for loop here ---
# print(word_count)
# Expected: {'python': 3, 'is': 3, 'great': 1, 'and': 2, 'easy': 1,
#            'to': 1, 'learn': 1, 'popular': 1}


# ── Exercise 4: Student Ranking ───────────────
# Real-life: School exam results
# Using enumerate, print ranked list sorted by marks (highest first).
# Format: "#1  Alice    95 marks — Gold"
# Awards: #1 → Gold, #2 → Silver, #3 → Bronze, rest → Certificate

students = [
    ("Alice",   95),
    ("Bob",     88),
    ("Charlie", 92),
    ("Diana",   78),
    ("Eve",     85),
]

# Sort by marks descending first, then enumerate
# --- your code here ---


# ── Exercise 5: FizzBuzz Pro ──────────────────
# Real-life: Common interview question / divisibility rule engine
# For numbers 1–30:
#   Divisible by 3 and 5 → "FizzBuzz"
#   Divisible by 3       → "Fizz"
#   Divisible by 5       → "Buzz"
#   Divisible by 7       → "Bazz"
#   Else                 → the number itself

# --- your for loop here ---


# ── Exercise 6: Temperature Converter Table ───
# Real-life: Scientific data export
# Print a conversion table for Celsius 0 to 100 (step 10) → Fahrenheit & Kelvin
# Formula: F = C * 9/5 + 32  |  K = C + 273.15
# Format:
# C      F       K
# 0     32.0   273.15
# 10    50.0   283.15
# ...

# --- your for loop here ---


# ─────────────────────────────────────────────
# Expected final lines for quick check:
# Ex1: Rohan Mehta Net Pay = ₹34,650
# Ex2: 3 items need reordering
# Ex3: python appears 3 times
# Ex4: #1 Alice — Gold
# Ex5: last line is "Bazz" (28÷7), then 29, then "FizzBuzz"... wait 30=FizzBuzz
# Ex6: 100  212.0  373.15
# ─────────────────────────────────────────────
