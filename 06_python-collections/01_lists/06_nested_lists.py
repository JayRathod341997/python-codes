# ============================================================
#  NESTED LISTS (Lists of Lists)
#  Real-world context: Cinema seat booking system
# ============================================================

# ============================================================
#  Creating a 2D grid — cinema hall (5 rows x 8 seats)
#  'O' = available,  'X' = booked
# ============================================================

ROWS = 5
COLS = 8

# Create fresh hall using list comprehension
hall = [["O"] * COLS for _ in range(ROWS)]

def display_hall(hall):
    print("    " + "  ".join(str(c+1) for c in range(COLS)))
    for r, row in enumerate(hall):
        label = chr(65 + r)   # A, B, C, D, E
        print(f" {label}  " + "  ".join(row))
    print()

print("=== Cinema Hall (Initial) ===")
display_hall(hall)

# ============================================================
#  Accessing elements — hall[row][col]
# ============================================================

print("Seat B3 status:", hall[1][2])   # row B = index 1, seat 3 = index 2

# ============================================================
#  Booking seats
# ============================================================

def book_seat(hall, row_letter, col_number):
    row = ord(row_letter.upper()) - 65
    col = col_number - 1
    if hall[row][col] == "X":
        print(f"  Seat {row_letter}{col_number} already booked!")
    else:
        hall[row][col] = "X"
        print(f"  Seat {row_letter}{col_number} booked successfully.")

book_seat(hall, "A", 3)
book_seat(hall, "A", 4)
book_seat(hall, "B", 1)
book_seat(hall, "C", 5)
book_seat(hall, "A", 3)   # try booking again

print("\n=== Cinema Hall (After Booking) ===")
display_hall(hall)

# ============================================================
#  Counting available and booked seats
# ============================================================

available = sum(row.count("O") for row in hall)
booked    = sum(row.count("X") for row in hall)
print(f"Available: {available}  |  Booked: {booked}  |  Total: {available + booked}")

# ============================================================
#  Iterating nested lists
# ============================================================

print("\n--- Row-by-row iteration ---")
for r_idx, row in enumerate(hall):
    row_label = chr(65 + r_idx)
    booked_seats = [i+1 for i, s in enumerate(row) if s == "X"]
    if booked_seats:
        print(f"  Row {row_label}: booked seats → {booked_seats}")

# ============================================================
#  Practical: Matrix multiplication concept
# ============================================================

print("\n--- Matrix (Grade table) ---")

# grades[student][subject]  subjects: Math, Science, English
grade_table = [
    [85, 90, 78],   # Student 0 — Alice
    [72, 65, 88],   # Student 1 — Bob
    [91, 87, 93],   # Student 2 — Carol
]
subjects = ["Math", "Science", "English"]
names    = ["Alice", "Bob", "Carol"]

print(f"{'Student':<10}", " ".join(f"{s:<10}" for s in subjects), "Average")
print("-" * 52)
for i, row in enumerate(grade_table):
    avg = sum(row) / len(row)
    print(f"{names[i]:<10}", " ".join(f"{g:<10}" for g in row), f"{avg:.1f}")

# Column average (per subject)
print("-" * 52)
print(f"{'Avg':<10}", end=" ")
for col in range(len(subjects)):
    col_avg = sum(grade_table[r][col] for r in range(len(grade_table))) / len(grade_table)
    print(f"{col_avg:<10.1f}", end="")
print()

# ============================================================
#  KEY POINTS
#  - nested list = list of lists (2D structure)
#  - Access with [row][col]
#  - Create with: [[val]*cols for _ in range(rows)]  ← CORRECT
#    NOT [[val]*cols] * rows  ← shares inner lists (BUG!)
# ============================================================

print("\n--- Common Mistake ---")
wrong = [["O"] * 3] * 3     # all rows are the SAME object
wrong[0][0] = "X"
print("Wrong (shared rows):", wrong)   # All rows changed!

correct = [["O"] * 3 for _ in range(3)]
correct[0][0] = "X"
print("Correct (independent rows):", correct)
