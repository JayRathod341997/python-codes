"""
============================================================
TOPIC: 02_collections_typing.py
Real-world context: E-commerce system handling product lists,
inventory dictionaries, and order tuples.
============================================================
"""

from typing import List, Dict, Set, Tuple, Sequence

# ============================================================
# SECTION 1: Typing Lists
# ============================================================
print("=" * 60)
print("SECTION 1: Typing Lists")
print("=" * 60)

# List[str] means "list of strings"
product_names: List[str] = ["Laptop", "Mouse", "Keyboard"]
print(f"Products: {product_names}")
print(f"Type: {type(product_names).__name__}, Elements: {[type(x).__name__ for x in product_names]}")

# List[int] means "list of integers"
prices: List[int] = [50000, 500, 1500]
print(f"\nPrices: {prices}")
print(f"Type: {type(prices).__name__}, Elements: {[type(x).__name__ for x in prices]}")

# List[float] for decimal values
ratings: List[float] = [4.5, 3.8, 4.9]
print(f"\nRatings: {ratings}")

# Function that works with lists
def total_price(items: List[int]) -> int:
    """Calculate total price from list of item prices."""
    return sum(items)

total = total_price(prices)
print(f"Total price: Rs{total}")

# Function that modifies a list
def add_product(products: List[str], name: str) -> None:
    """Add a product to the list."""
    products.append(name)
    print(f"  -> Added '{name}' to inventory")

inventory: List[str] = ["Phone", "Tablet"]
add_product(inventory, "Headphones")
print(f"Updated inventory: {inventory}")


# ============================================================
# SECTION 2: Typing Dictionaries
# ============================================================
print("\n" + "=" * 60)
print("SECTION 2: Typing Dictionaries")
print("=" * 60)

# Dict[str, int] means "dictionary with string keys and integer values"
student_scores: Dict[str, int] = {
    "Alice": 95,
    "Bob": 87,
    "Charlie": 92
}
print(f"Scores: {student_scores}")
print(f"Type: Dict[str, int]")

# Dict[str, str] for string keys and values
user_emails: Dict[str, str] = {
    "user1": "alice@example.com",
    "user2": "bob@example.com"
}
print(f"\nUser Emails: {user_emails}")

# Dict[int, str] for integer keys and string values
product_by_id: Dict[int, str] = {
    101: "Laptop",
    102: "Mouse",
    103: "Keyboard"
}
print(f"\nProducts by ID: {product_by_id}")

# More complex: Dict[str, List[int]] (string -> list of ints)
team_scores: Dict[str, List[int]] = {
    "Team A": [85, 90, 88],
    "Team B": [92, 88, 95],
    "Team C": [78, 82, 80]
}
print(f"\nTeam Scores: {team_scores}")

# Function working with dictionaries
def get_average_score(scores: Dict[str, int]) -> float:
    """Calculate average score from scores dictionary."""
    total = sum(scores.values())
    count = len(scores)
    return total / count if count > 0 else 0

avg = get_average_score(student_scores)
print(f"\nAverage score: {avg:.2f}")

# Function that modifies dictionary
def add_student(scores: Dict[str, int], name: str, score: int) -> None:
    """Add a student's score."""
    scores[name] = score
    print(f"  -> Added {name} with score {score}")

add_student(student_scores, "Diana", 89)
print(f"Updated scores: {student_scores}")


# ============================================================
# SECTION 3: Typing Sets
# ============================================================
print("\n" + "=" * 60)
print("SECTION 3: Typing Sets")
print("=" * 60)

# Set[str] means "set of unique strings"
user_tags: Set[str] = {"python", "django", "fastapi"}
print(f"Tags: {user_tags}")
print(f"Type: Set[str]")

# Set[int] for unique integers
unique_ages: Set[int] = {25, 30, 28, 25, 30}  # Duplicates removed
print(f"Unique ages: {unique_ages}")

# Function working with sets
def find_common_skills(skills1: Set[str], skills2: Set[str]) -> Set[str]:
    """Find common skills between two people."""
    return skills1 & skills2

alice_skills = {"Python", "JavaScript", "SQL"}
bob_skills = {"Python", "Java", "SQL"}
common = find_common_skills(alice_skills, bob_skills)
print(f"\nAlice's skills: {alice_skills}")
print(f"Bob's skills: {bob_skills}")
print(f"Common skills: {common}")


# ============================================================
# SECTION 4: Typing Tuples
# ============================================================
print("\n" + "=" * 60)
print("SECTION 4: Typing Tuples")
print("=" * 60)

# Tuple with fixed length and specific types
# Tuple[int, int] = tuple with 2 integers
coordinates: Tuple[int, int] = (10, 20)
print(f"Coordinates: {coordinates}")
print(f"Type: Tuple[int, int]")

# Tuple with different types: (name, age, email)
user_record: Tuple[str, int, str] = ("Alice", 28, "alice@example.com")
print(f"\nUser record: {user_record}")
print(f"Name: {user_record[0]}, Age: {user_record[1]}, Email: {user_record[2]}")

# Tuple[str, int, bool] - mixed types
product: Tuple[str, int, bool] = ("Laptop", 50000, True)  # (name, price, in_stock)
print(f"\nProduct: {product}")

# Tuple with variable length: Tuple[str, ...] means "any number of strings"
product_colors: Tuple[str, ...] = ("Red", "Blue", "Green", "Black")
print(f"\nAvailable colors: {product_colors}")

# Function returning a tuple
def get_user_info(user_id: int) -> Tuple[str, int]:
    """Return (name, age) tuple for a user."""
    users = {1: ("Alice", 28), 2: ("Bob", 32)}
    return users.get(user_id, ("Unknown", 0))

name, age = get_user_info(1)
print(f"\nUser info: Name={name}, Age={age}")

# Function taking a tuple parameter
def calculate_distance(point1: Tuple[int, int], point2: Tuple[int, int]) -> float:
    """Calculate Euclidean distance between two points."""
    import math
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

p1 = (0, 0)
p2 = (3, 4)
distance = calculate_distance(p1, p2)
print(f"Distance from {p1} to {p2}: {distance}")


# ============================================================
# SECTION 5: Using Sequence (Generic Iterator)
# ============================================================
print("\n" + "=" * 60)
print("SECTION 5: Sequence (Read-only Collections)")
print("=" * 60)

# Sequence[T] is more flexible - accepts lists, tuples, etc.
def print_items(items: Sequence[str]) -> None:
    """Print items - accepts both list and tuple."""
    for i, item in enumerate(items, 1):
        print(f"  {i}. {item}")

print("Using Sequence with list:")
print_items(["Apple", "Banana", "Cherry"])

print("\nUsing Sequence with tuple:")
print_items(("Mango", "Pineapple", "Papaya"))


# ============================================================
# SECTION 6: Complex Nested Types
# ============================================================
print("\n" + "=" * 60)
print("SECTION 6: Complex Nested Types")
print("=" * 60)

# List of dictionaries: List[Dict[str, int]]
# Real-world: List of student records
students: List[Dict[str, int]] = [
    {"id": 1, "score": 95},
    {"id": 2, "score": 87},
    {"id": 3, "score": 92}
]
print(f"Students: {students}")

# Dict with list values: Dict[str, List[str]]
# Real-world: Department -> list of employees
departments: Dict[str, List[str]] = {
    "Engineering": ["Alice", "Bob", "Charlie"],
    "Sales": ["Diana", "Eve"],
    "HR": ["Frank"]
}
print(f"\nDepartments: {departments}")

# Function with nested types
def get_department_size(depts: Dict[str, List[str]], dept_name: str) -> int:
    """Get number of employees in a department."""
    return len(depts.get(dept_name, []))

engineering_count = get_department_size(departments, "Engineering")
print(f"Engineering team size: {engineering_count}")

sales_count = get_department_size(departments, "Sales")
print(f"Sales team size: {sales_count}")


# ============================================================
# KEY POINTS
# ============================================================
print("\n" + "=" * 60)
print("KEY POINTS")
print("=" * 60)
print("""
1. List[T]: List of elements of type T
   Example: List[str], List[int], List[Dict[str, int]]

2. Dict[K, V]: Dictionary with key type K and value type V
   Example: Dict[str, int], Dict[int, str], Dict[str, List[int]]

3. Set[T]: Set of unique elements of type T
   Example: Set[str], Set[int]

4. Tuple[T1, T2, ...]: Fixed-length tuple with specific types
   Example: Tuple[str, int, bool] = ("Alice", 28, True)

5. Tuple[T, ...]: Variable-length tuple of type T
   Example: Tuple[int, ...] = (1, 2, 3, 4, 5)

6. Sequence[T]: Any sequence (list, tuple) - better for parameters

7. Complex types: List[Dict[str, int]], Dict[str, List[str]], etc.

8. These are just type hints - Python doesn't enforce them at runtime
""")
