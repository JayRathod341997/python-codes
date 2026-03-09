# ============================================================
#  FROZEN SETS — Immutable Sets
#  Real-world context: Network security & config management
# ============================================================

# ============================================================
#  Creating frozensets
# ============================================================

print("=== Creating Frozen Sets ===")

# Regular set — mutable
regular_set = {"python", "java", "go"}
regular_set.add("rust")
print("Regular set (mutable):", regular_set)

# frozenset — immutable
ALLOWED_METHODS = frozenset({"GET", "POST", "PUT", "PATCH", "DELETE"})
print("Frozen set:", ALLOWED_METHODS)

# From list
SUPPORTED_EXTENSIONS = frozenset([".py", ".js", ".ts", ".go", ".rs"])
print("Extensions :", SUPPORTED_EXTENSIONS)

# From string
VOWELS = frozenset("aeiouAEIOU")
print("Vowels     :", VOWELS)

# Empty frozenset
empty_fs = frozenset()
print("Empty frozenset:", empty_fs)

# ============================================================
#  Immutability — cannot modify frozenset
# ============================================================

print("\n=== Immutability ===")

fs = frozenset({1, 2, 3})
try:
    fs.add(4)
except AttributeError as e:
    print(f"Cannot add   : {e}")

try:
    fs.remove(1)
except AttributeError as e:
    print(f"Cannot remove: {e}")

# ============================================================
#  frozenset as dictionary KEY (unlike regular set)
# ============================================================

print("\n=== frozenset as Dictionary Key ===")

# Map permission groups to roles
role_permissions = {
    frozenset({"read"})                              : "Viewer",
    frozenset({"read", "write"})                     : "Editor",
    frozenset({"read", "write", "execute"})          : "Developer",
    frozenset({"read", "write", "execute", "admin"}) : "Admin",
}

def get_role(user_permissions):
    key = frozenset(user_permissions)
    return role_permissions.get(key, "Unknown Role")

print("read only          →", get_role({"read"}))
print("read+write         →", get_role({"write", "read"}))
print("read+write+execute →", get_role({"execute", "read", "write"}))
print("random permissions →", get_role({"fly", "jump"}))

# This would FAIL with regular sets (not hashable):
try:
    bad = {}
    bad[{"read"}] = "Viewer"
except TypeError as e:
    print(f"\nRegular set as key: {e}")

# ============================================================
#  frozenset in another set (nested sets — not possible with regular sets)
# ============================================================

print("\n=== Nested Frozensets ===")

# Represent network subnets as frozensets of IPs
subnet_a = frozenset({"192.168.1.1", "192.168.1.2", "192.168.1.3"})
subnet_b = frozenset({"10.0.0.1", "10.0.0.2"})
subnet_c = frozenset({"172.16.0.1", "172.16.0.2"})

# A set of subnets (frozensets inside a set — works!)
network = {subnet_a, subnet_b, subnet_c}
print(f"Network has {len(network)} subnets")

# ============================================================
#  All set operations work on frozensets (read-only result)
# ============================================================

print("\n=== Operations on Frozen Sets ===")

backend_skills  = frozenset({"Python", "SQL", "Docker", "Linux"})
frontend_skills = frozenset({"JavaScript", "React", "CSS", "Python"})

print("Union       :", backend_skills | frontend_skills)
print("Intersection:", backend_skills & frontend_skills)
print("Difference  :", backend_skills - frontend_skills)

# Checking membership
print("\n'Python' in backend_skills:", "Python" in backend_skills)
print("'React' in backend_skills :", "React" in backend_skills)

# ============================================================
#  Regular set vs frozenset — when to use which
# ============================================================

print("\n=== When to Use Each ===")

comparison = [
    ("Feature",          "set",       "frozenset"),
    ("Mutable",          "Yes",       "No"),
    ("Hashable",         "No",        "Yes"),
    ("Dict key",         "No",        "Yes"),
    ("Element of set",   "No",        "Yes"),
    ("Set operations",   "Yes",       "Yes (returns frozenset)"),
    ("Use for",          "Dynamic",   "Constants/config"),
]

col = [22, 18, 30]
for row in comparison:
    print(" | ".join(str(v).ljust(w) for v, w in zip(row, col)))

# ============================================================
#  KEY POINTS
#  frozenset = immutable version of set
#  Created with frozenset(iterable)
#  Can be used as dict keys or elements of other sets
#  Supports all read operations: in, |, &, -, ^, subset checks
#  Cannot: add, remove, update, clear, pop
# ============================================================
