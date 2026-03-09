# ============================================================
#  IMMUTABLE NATURE OF TUPLES
#  Real-world context: Bank transaction records & config
# ============================================================

# ============================================================
#  Tuples CANNOT be changed after creation
# ============================================================

print("=== Immutability ===")

transaction = ("TXN001", "2024-01-15", 5000.00, "CREDIT")

# Attempting to modify raises TypeError
try:
    transaction[2] = 9999.00
except TypeError as e:
    print(f"Cannot modify tuple: {e}")

# Attempting to append raises AttributeError
try:
    transaction.append("EXTRA")
except AttributeError as e:
    print(f"No append method   : {e}")

print("Transaction (unchanged):", transaction)

# ============================================================
#  WHY immutability matters — real use cases
# ============================================================

print("\n=== Why Immutability is Useful ===")

# 1. DATABASE RECORD INTEGRITY
#    Transaction records must NEVER be altered after creation
transactions = [
    ("TXN001", "2024-01-15", 5000.00,  "CREDIT"),
    ("TXN002", "2024-01-16", 1500.00,  "DEBIT"),
    ("TXN003", "2024-01-17", 20000.00, "CREDIT"),
]
print("Immutable transaction log:")
for txn in transactions:
    txn_id, date, amount, txn_type = txn
    sign = "+" if txn_type == "CREDIT" else "-"
    print(f"  {txn_id}  {date}  {sign}₹{amount:>10,.2f}  [{txn_type}]")

# 2. CONFIGURATION — settings that must not change at runtime
DB_CONFIG = ("localhost", 5432, "mydb", "readonly_user")
HOST, PORT, DB, USER = DB_CONFIG
print(f"\nDB Config: {HOST}:{PORT}/{DB} as {USER}")

# 3. CONSTANTS / ENUMS
DAYS_OF_WEEK   = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")
MONTHS         = ("Jan","Feb","Mar","Apr","May","Jun",
                  "Jul","Aug","Sep","Oct","Nov","Dec")
HTTP_METHODS   = ("GET", "POST", "PUT", "PATCH", "DELETE")

print("\nWeekdays:", DAYS_OF_WEEK[:5])
print("HTTP Methods:", HTTP_METHODS)

# ============================================================
#  Tuples as Dictionary Keys (lists CANNOT be keys)
# ============================================================

print("\n=== Tuples as Dictionary Keys ===")

# Grid-based game: store piece at each (row, col) position
board = {}
board[(0, 0)] = "King"
board[(0, 7)] = "Rook"
board[(7, 3)] = "Queen"
board[(1, 4)] = "Pawn"

print("Chess board positions:")
for pos, piece in board.items():
    print(f"  {pos} → {piece}")

# IP address → location mapping
ip_to_location = {
    (192, 168, 1,  1): "Router",
    (192, 168, 1, 10): "Laptop",
    (192, 168, 1, 20): "Printer",
}
lookup = (192, 168, 1, 10)
print(f"\n{lookup} is '{ip_to_location[lookup]}'")

# This would FAIL with lists — lists are not hashable:
try:
    bad_dict = {}
    bad_dict[[1, 2]] = "value"
except TypeError as e:
    print(f"\nList as key fails: {e}")

# ============================================================
#  Tuples are HASHABLE — can be stored in sets
# ============================================================

visited_coords = {(19.07, 72.87), (28.61, 77.20), (12.97, 77.59)}
new_coord = (19.07, 72.87)
print("\nAlready visited?", new_coord in visited_coords)

# ============================================================
#  Tuple containing a mutable object
# ============================================================

print("\n=== Tuple with Mutable Content ===")

# The tuple reference is immutable, but inner list content can change
student = ("Alice", [85, 90, 78])   # name and grades

try:
    student[1] = [100, 100, 100]    # replace the list — FAILS
except TypeError as e:
    print(f"Cannot replace inner list: {e}")

student[1].append(95)               # mutate the list — WORKS
print("After appending grade:", student)

# ============================================================
#  KEY POINTS
#  - Tuples are immutable — no modification after creation
#  - Use for data that should never change (config, records)
#  - Hashable → can be used as dict keys or in sets
#  - More memory-efficient and slightly faster than lists
# ============================================================
