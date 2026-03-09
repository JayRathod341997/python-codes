# ============================================================
#  TUPLE USE CASES
#  Real-world context: Multiple practical scenarios
# ============================================================

from collections import namedtuple

# ============================================================
#  USE CASE 1: Returning multiple values from functions
# ============================================================

print("=== 1. Multiple Return Values ===")

def calculate_stats(numbers):
    n    = len(numbers)
    mean = sum(numbers) / n
    minimum = min(numbers)
    maximum = max(numbers)
    variance = sum((x - mean) ** 2 for x in numbers) / n
    std_dev = variance ** 0.5
    return mean, minimum, maximum, round(std_dev, 2)

test_scores = [78, 85, 92, 67, 88, 71, 95, 80]
mean, low, high, std = calculate_stats(test_scores)
print(f"Scores : {test_scores}")
print(f"Mean   : {mean:.2f}  Low: {low}  High: {high}  StdDev: {std}")

# ============================================================
#  USE CASE 2: Named tuples — readable record structures
# ============================================================

print("\n=== 2. Named Tuples ===")

# Regular tuple — hard to remember index meanings
raw = ("Alice", 28, "Engineering", 95000)
print("Raw tuple salary:", raw[3])    # what is index 3?

# Named tuple — self-documenting
Employee = namedtuple("Employee", ["name", "age", "department", "salary"])

alice = Employee(name="Alice", age=28, department="Engineering", salary=95000)
bob   = Employee("Bob", 32, "Marketing", 72000)

print(f"\nEmployee: {alice.name}, Dept: {alice.department}, Salary: ₹{alice.salary:,}")
print(f"Employee: {bob.name},   Dept: {bob.department}, Salary: ₹{bob.salary:,}")

# Still works like a tuple
print("Index access:", alice[0], alice[2])

# ============================================================
#  USE CASE 3: Structured records / rows in data processing
# ============================================================

print("\n=== 3. Data Records ===")

Point   = namedtuple("Point", ["x", "y"])
Color   = namedtuple("Color", ["r", "g", "b", "name"])

palette = [
    Color(255,   0,   0, "Red"    ),
    Color(  0, 255,   0, "Green"  ),
    Color(  0,   0, 255, "Blue"   ),
    Color(255, 255,   0, "Yellow" ),
    Color(128,   0, 128, "Purple" ),
]

print("Color Palette:")
for c in palette:
    print(f"  {c.name:<10} rgb({c.r:>3}, {c.g:>3}, {c.b:>3})  hex=#{c.r:02X}{c.g:02X}{c.b:02X}")

# ============================================================
#  USE CASE 4: Grouping related constants
# ============================================================

print("\n=== 4. Grouping Constants ===")

# HTTP status codes as named tuples
Status = namedtuple("Status", ["code", "message"])

HTTP_OK            = Status(200, "OK")
HTTP_NOT_FOUND     = Status(404, "Not Found")
HTTP_SERVER_ERROR  = Status(500, "Internal Server Error")
HTTP_UNAUTHORIZED  = Status(401, "Unauthorized")

def handle_request(endpoint, authenticated):
    if not authenticated:
        return HTTP_UNAUTHORIZED
    if endpoint == "/dashboard":
        return HTTP_OK
    return HTTP_NOT_FOUND

for endpoint, auth in [("/dashboard", True), ("/profile", True), ("/admin", False)]:
    result = handle_request(endpoint, auth)
    print(f"  GET {endpoint:<15} → {result.code} {result.message}")

# ============================================================
#  USE CASE 5: Zip and tuple iteration
# ============================================================

print("\n=== 5. Zip Pairing ===")

questions  = ["Name?", "Age?", "City?"]
answers    = ["Alice", "28",   "Mumbai"]

# zip produces tuples
for q, a in zip(questions, answers):
    print(f"  {q:<10} {a}")

# Create lookup from two lists
product_ids   = [101, 102, 103, 104]
product_names = ["Laptop", "Mouse", "Keyboard", "Monitor"]

product_map = dict(zip(product_ids, product_names))
print("\nProduct map:", product_map)
print("Product 103 :", product_map[103])

# ============================================================
#  USE CASE 6: Tuple as composite dictionary key
# ============================================================

print("\n=== 6. Composite Key in Dict ===")

# Store monthly sales by (year, month)
sales = {}
sales[(2024, 1)]  = 125000
sales[(2024, 2)]  = 98000
sales[(2024, 3)]  = 145000
sales[(2023, 12)] = 110000

print("Monthly Sales:")
for (year, month), amount in sorted(sales.items()):
    print(f"  {year}-{month:02d}  ₹{amount:>10,}")

# ============================================================
#  KEY POINTS SUMMARY
#  - Multiple returns → automatically packed as tuple
#  - Named tuples  → readable, self-documenting records
#  - Constants     → group related values that never change
#  - Dict keys     → tuples as composite keys
#  - zip()         → produces tuples for parallel iteration
# ============================================================
