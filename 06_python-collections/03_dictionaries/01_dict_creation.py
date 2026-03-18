# ============================================================
#  DICTIONARY CREATION
#  Real-world context: User profile / contact book
# ============================================================

# ============================================================
#  Ways to create a dictionary
# ============================================================

print("=== Creating Dictionaries ===")

# 1. Literal with curly braces
user = {
    "name": "Alice Johnson",
    "email": "alice@example.com",
    "age": 28,
    "verified": True,
}
print("1. Literal:", user)

# 2. dict() constructor with keyword args
config = dict(host="localhost", port=5432, database="appdb")
print("2. dict()  :", config)

# 3. dict() from list of (key, value) pairs
fields = [("username", "alice99"), ("country", "India"), ("plan", "premium")]
profile = dict(fields)
print("3. From pairs:", profile)

# 4. dict comprehension
# Square of numbers 1-5
squares = {n: n**2 for n in range(1, 6)}
print("4. Comprehension:", squares)

# 5. fromkeys() — same default value for multiple keys
permissions = dict.fromkeys(["read", "write", "delete", "admin"], False)
print("5. fromkeys()   :", permissions)

# Grant permissions
permissions["read"] = True
permissions["write"] = True
print("   After update :", permissions)

# 6. Merging two dicts (Python 3.9+: | operator)
base_info = {"name": "Bob", "age": 30}
extra_info = {"email": "bob@example.com", "city": "Delhi"}

merged = base_info | extra_info  # creates new dict
print("6. Merged (|)  :", merged)

base_info |= extra_info  # updates in-place
print("   Updated (|=) :", base_info)

# ============================================================
#  Key rules
# ============================================================

print("\n=== Key Rules ===")

# Keys must be UNIQUE — duplicate overwrites
d = {"a": 1, "b": 2, "a": 99}
print("Duplicate key (last wins):", d)

# Keys must be HASHABLE (immutable)
valid_keys = {
    1: "integer key",
    "hello": "string key",
    (1, 2): "tuple key",
    True: "bool key",
}
print("Valid key types:", list(valid_keys.keys()))

# Values can be ANYTHING — even other dicts or lists
complex_val = {
    "scores": [85, 90, 78],
    "address": {"city": "Mumbai", "pin": "400001"},
    "active": True,
}
print("Complex values:", complex_val)

# ============================================================
#  Empty dict
# ============================================================

empty1 = {}
empty2 = dict()
print("\nEmpty dict:", empty1, type(empty1))
print("Empty dict:", empty2, type(empty2))

# ============================================================
#  KEY POINTS
#  - {} or dict() to create
#  - Keys: unique, hashable (str, int, tuple, bool)
#  - Values: any type, duplicates allowed
#  - dict comprehension: {k: v for ...}
#  - fromkeys(): same default for many keys
# ============================================================
