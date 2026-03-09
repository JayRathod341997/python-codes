# ============================================================
#  SET METHODS
#  Real-world context: Access control / permission system
# ============================================================

# ============================================================
#  ADDING elements
# ============================================================

print("=== Adding Elements ===")

permissions = {"read", "write"}
print("Initial:", permissions)

# add() — add single element (no error if already present)
permissions.add("execute")
print("After add('execute'):", permissions)

permissions.add("read")   # already exists — silently ignored
print("After add('read') again:", permissions)

# update() — add multiple elements at once (from any iterable)
permissions.update(["admin", "delete"])
print("After update([admin, delete]):", permissions)

permissions.update({"audit", "read"})   # from set
print("After update({audit, read}):", permissions)

# ============================================================
#  REMOVING elements
# ============================================================

print("\n=== Removing Elements ===")

active_sessions = {"session_01", "session_02", "session_03", "session_04", "session_05"}
print("Active sessions:", active_sessions)

# remove() — raises KeyError if element not found
active_sessions.remove("session_03")
print("After remove('session_03'):", active_sessions)

try:
    active_sessions.remove("session_99")   # not found
except KeyError as e:
    print(f"KeyError with remove(): {e}")

# discard() — SAFE remove, no error if not found
active_sessions.discard("session_02")
print("After discard('session_02'):", active_sessions)

active_sessions.discard("session_99")   # no error
print("After discard missing key  :", active_sessions)

# pop() — removes and returns a RANDOM element
popped = active_sessions.pop()
print(f"Popped (random): {popped}  |  Remaining: {active_sessions}")

# clear() — removes ALL elements
temp = {"a", "b", "c"}
temp.clear()
print("After clear():", temp)

# ============================================================
#  IN-PLACE SET OPERATIONS (modify original)
# ============================================================

print("\n=== In-place Operations ===")

user_permissions  = {"read", "write", "execute"}
new_permissions   = {"write", "admin", "audit"}

print("Before — user:", user_permissions)
print("Before — new :", new_permissions)

# intersection_update() — keep only common elements
temp = user_permissions.copy()
temp.intersection_update(new_permissions)
print("intersection_update():", temp)      # only "write"

# difference_update() — remove elements found in other set
temp = user_permissions.copy()
temp.difference_update(new_permissions)
print("difference_update()  :", temp)      # read, execute (not in new_permissions)

# symmetric_difference_update() — keep only non-overlapping
temp = user_permissions.copy()
temp.symmetric_difference_update(new_permissions)
print("symmetric_diff_update:", temp)      # everything except "write"

# union in-place using |=
temp = {"read"}
temp |= {"write", "execute"}
print("|= (union in-place)  :", temp)

# intersection in-place using &=
temp &= {"read", "write"}
print("&= (intersect)       :", temp)

# ============================================================
#  COPYING
# ============================================================

print("\n=== Copying ===")

original = {"read", "write", "execute"}
copy1 = original.copy()

copy1.add("admin")
print("Original (unchanged):", original)
print("Copy (with admin)    :", copy1)

# ============================================================
#  PRACTICAL: Role-based access control (RBAC)
# ============================================================

print("\n=== RBAC Example ===")

PERMISSIONS = {
    "viewer"    : {"read"},
    "editor"    : {"read", "write"},
    "developer" : {"read", "write", "execute", "deploy"},
    "admin"     : {"read", "write", "execute", "deploy", "manage_users", "audit"},
}

def check_access(user_role, required_permissions):
    user_perms = PERMISSIONS.get(user_role, set())
    has = user_perms & required_permissions
    missing = required_permissions - user_perms
    granted = len(missing) == 0
    return granted, has, missing

actions = {
    "view dashboard"  : {"read"},
    "edit content"    : {"read", "write"},
    "deploy app"      : {"deploy", "execute"},
    "delete users"    : {"manage_users"},
}

for role in ["viewer", "editor", "developer"]:
    print(f"\nRole: {role.upper()}")
    for action, required in actions.items():
        granted, has, missing = check_access(role, required)
        status = "✓ ALLOWED" if granted else "✗ DENIED"
        print(f"  {status}  {action:<20}", end="")
        if not granted:
            print(f" (missing: {missing})", end="")
        print()

# ============================================================
#  KEY POINTS
#  add(x)                      → add single element
#  update(iterable)            → add multiple elements
#  remove(x)                   → remove, KeyError if missing
#  discard(x)                  → remove safely (no error)
#  pop()                       → remove & return random element
#  clear()                     → empty the set
#  copy()                      → shallow copy
#  intersection_update()       → keep only common (in-place)
#  difference_update()         → remove others (in-place)
#  |= &= -= ^=                → in-place operators
# ============================================================
