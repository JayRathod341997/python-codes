# ============================================================
#  PACKING & UNPACKING
#  Real-world context: Flight booking & data parsing
# ============================================================

# ============================================================
#  PACKING — combine multiple values into a tuple
# ============================================================

print("=== Packing ===")

# Packing flight details
flight = ("AI-202", "Mumbai", "New Delhi", "08:30", "10:45")
print("Flight record:", flight)

# Packing a database row result
employee_row = 1001, "Alice Johnson", "Engineering", 95000.0
print("DB row:", employee_row)

# ============================================================
#  UNPACKING — extract values into separate variables
# ============================================================

print("\n=== Unpacking ===")

flight_no, origin, destination, depart, arrive = flight
print(f"Flight  : {flight_no}")
print(f"From    : {origin}  →  {destination}")
print(f"Departs : {depart}  |  Arrives: {arrive}")

emp_id, name, dept, salary = employee_row
print(f"\n{name} works in {dept} earning ₹{salary:,.0f}")

# ============================================================
#  SWAP VARIABLES — classic Python trick using unpacking
# ============================================================

print("\n=== Variable Swap ===")

a, b = 10, 20
print(f"Before: a={a}, b={b}")
a, b = b, a    # unpack right side first, then assign
print(f"After : a={a}, b={b}")

# ============================================================
#  EXTENDED UNPACKING — using * (star)
# ============================================================

print("\n=== Extended Unpacking (*) ===")

# First and last passenger, everyone else in between
passengers = ("Alice", "Bob", "Carol", "Dave", "Eve")

first, *middle, last = passengers
print("First    :", first)
print("Middle   :", middle)
print("Last     :", last)

# Skipping values with _
_, city, _, time, _ = ("AI-202", "Mumbai", "New Delhi", "08:30", "10:45")
print("\nCity:", city, "| Time:", time)

# ============================================================
#  UNPACKING IN LOOPS
# ============================================================

print("\n=== Unpacking in Loops ===")

flight_schedule = [
    ("AI-101", "Mumbai",    "Chennai",   "06:00"),
    ("AI-202", "Delhi",     "Kolkata",   "08:30"),
    ("AI-303", "Bangalore", "Hyderabad", "11:15"),
    ("AI-404", "Pune",      "Goa",       "14:00"),
]

print(f"{'Flight':<10} {'From':<12} {'To':<12} {'Departs'}")
print("-" * 45)
for fno, src, dst, dep in flight_schedule:
    print(f"{fno:<10} {src:<12} {dst:<12} {dep}")

# ============================================================
#  FUNCTION RETURNING MULTIPLE VALUES (uses packing)
# ============================================================

print("\n=== Function with multiple returns ===")

def get_min_max(numbers):
    return min(numbers), max(numbers)   # returns a tuple

data = [34, 67, 12, 89, 45, 23, 78]
minimum, maximum = get_min_max(data)    # unpacking
print(f"Data: {data}")
print(f"Min: {minimum}  |  Max: {maximum}")

def parse_name(full_name):
    parts = full_name.split()
    if len(parts) == 2:
        return parts[0], parts[1]
    return parts[0], " ".join(parts[1:])

first, last = parse_name("Alice Johnson")
print(f"\nFirst: {first}  Last: {last}")

first, last = parse_name("Robert De Niro")
print(f"First: {first}  Last: {last}")

# ============================================================
#  KEY POINTS
#  - Packing  : a, b, c = 1, 2, 3   or   t = (1, 2, 3)
#  - Unpacking: x, y, z = t
#  - Extended : first, *rest, last = t
#  - Use _ to skip values you don't need
#  - Functions return tuples when returning multiple values
# ============================================================
