# ─────────────────────────────────────────────
# Exercises — Nested Loops
# ─────────────────────────────────────────────

# ── Exercise 1: Restaurant Bill Splitter ──────
# Real-life: Group dining app
# tables = list of tables, each with a list of orders (prices)
# For each table:
#   - Sum all orders at that table
#   - Print each order and the total
# Format:
#   Table 1:
#     Order: ₹250
#     Order: ₹180
#     Table Total: ₹430

tables = [
    [250, 180, 320],
    [99,  450, 200, 150],
    [600, 350],
]

# --- your nested loop here ---


# ── Exercise 2: Attendance Matrix ─────────────
# Real-life: School attendance tracking
# attendance[student][day] = True/False
# Print a grid showing P (Present) or A (Absent)
# Also print each student's attendance percentage.

students = ["Alice", "Bob", "Charlie"]
# Each inner list = Mon to Fri
attendance = [
    [True,  True,  False, True,  True ],   # Alice
    [True,  False, False, True,  False],   # Bob
    [True,  True,  True,  True,  True ],   # Charlie
]
days = ["Mon", "Tue", "Wed", "Thu", "Fri"]

# --- your nested loop here ---
# Expected format:
#           Mon  Tue  Wed  Thu  Fri   %
# Alice     P    P    A    P    P    80%
# Bob       P    A    A    P    A    40%
# Charlie   P    P    P    P    P   100%


# ── Exercise 3: Password Brute-Force Simulator ─
# Real-life: Security research / understanding why weak passwords fail
# Generate all 2-digit PINs (00–99) and check against target.
# Print total attempts when found.
# (Educational: shows why short PINs are insecure)

target_pin = "47"       # simulated target

digits  = "0123456789"
attempts = 0

for first in digits:
    for second in digits:
        attempts += 1
        candidate = first + second
        if candidate == target_pin:
            print(f"PIN '{target_pin}' found after {attempts} attempts.")
            break
    else:
        continue
    break               # break outer loop too when found


# ── Exercise 4: Sales Region Heatmap ──────────
# Real-life: Business intelligence dashboard
# sales[region][month] = revenue in lakhs
# Find and print the top-performing region-month combination.

regions = ["North", "South", "East", "West"]
months  = ["Jan", "Feb", "Mar", "Apr"]
sales   = [
    [45, 52, 60, 58],   # North
    [38, 41, 47, 55],   # South
    [62, 58, 70, 65],   # East
    [30, 35, 40, 44],   # West
]

# Print full grid first, then find and print the max.
# Grid format:
#         Jan   Feb   Mar   Apr
# North   45    52    60    58
# ...

# --- your nested loop here ---


# ── Exercise 5: Sudoku Row Validator ──────────
# Real-life: Game logic validation
# A valid Sudoku row has digits 1–9 with no repeats.
# Validate each row of this partial board:
# For each row: check if any number appears more than once.
# Print "Row {i}: Valid" or "Row {i}: Invalid (duplicate: {num})"

board = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],   # valid
    [6, 7, 2, 1, 9, 5, 3, 4, 8],   # valid
    [1, 9, 8, 3, 4, 2, 5, 6, 7],   # valid
    [8, 5, 9, 7, 6, 1, 4, 2, 3],   # valid
    [4, 2, 6, 8, 5, 3, 7, 9, 1],   # valid
    [7, 1, 3, 9, 2, 4, 8, 5, 5],   # INVALID — duplicate 5
]

# --- your nested loop here ---


# ─────────────────────────────────────────────
# Expected key outputs:
# Ex1: Table totals — ₹750, ₹899, ₹950
# Ex2: Charlie = 100%, Bob = 40%
# Ex3: PIN '47' found after 48 attempts.
# Ex4: Top performer: East — Mar ₹70 Lakh
# Ex5: Row 6: Invalid (duplicate: 5)
# ─────────────────────────────────────────────
