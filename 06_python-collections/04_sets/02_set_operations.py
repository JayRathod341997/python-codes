# ============================================================
#  SET OPERATIONS (Operators & Methods)
#  Real-world context: Social media friend recommendations
# ============================================================

# Friends of each user
alice_friends = {"Bob", "Carol", "Dave", "Eve", "Frank"}
bob_friends   = {"Alice", "Carol", "Eve", "Grace", "Hank"}
carol_friends = {"Alice", "Bob", "Dave", "Grace", "Ivy"}

print(f"Alice's friends: {alice_friends}")
print(f"Bob's friends  : {bob_friends}")
print(f"Carol's friends: {carol_friends}")

# ============================================================
#  1. UNION  |  (everyone combined)
# ============================================================

print("\n=== UNION | ===")
# All people known by Alice OR Bob
all_contacts = alice_friends | bob_friends
print("Alice | Bob (everyone they know):", sorted(all_contacts))

# Three-way union
everyone = alice_friends | bob_friends | carol_friends
print("All three | combined:", sorted(everyone))

# Method form
print("Via method .union():", sorted(alice_friends.union(bob_friends)))

# ============================================================
#  2. INTERSECTION  &  (common elements)
# ============================================================

print("\n=== INTERSECTION & ===")
# Friends BOTH Alice AND Bob know → recommend to each other
mutual = alice_friends & bob_friends
print("Alice & Bob mutual friends:", mutual)

# People all three know
all_mutual = alice_friends & bob_friends & carol_friends
print("Known by all three        :", all_mutual)

print("Via method .intersection():", alice_friends.intersection(bob_friends))

# ============================================================
#  3. DIFFERENCE  -  (in A but not B)
# ============================================================

print("\n=== DIFFERENCE - ===")
# Friends Alice has that Bob doesn't → suggest to Bob
alice_exclusive = alice_friends - bob_friends
print("Alice's exclusive friends (suggest to Bob):", alice_exclusive)

# Bob's exclusive friends (suggest to Alice)
bob_exclusive = bob_friends - alice_friends
print("Bob's exclusive friends (suggest to Alice) :", bob_exclusive)

print("Via method .difference():", alice_friends.difference(bob_friends))

# ============================================================
#  4. SYMMETRIC DIFFERENCE  ^  (in one but not both)
# ============================================================

print("\n=== SYMMETRIC DIFFERENCE ^ ===")
# Friends known by EITHER Alice or Bob but NOT both
unique_to_each = alice_friends ^ bob_friends
print("Known by Alice OR Bob (not both):", sorted(unique_to_each))

print("Via method .symmetric_difference():",
      sorted(alice_friends.symmetric_difference(bob_friends)))

# ============================================================
#  5. SUBSET and SUPERSET checks
# ============================================================

print("\n=== SUBSET / SUPERSET ===")

python_devs  = {"Alice", "Bob", "Carol", "Dave"}
backend_devs = {"Bob", "Carol", "Eve"}
full_team    = {"Alice", "Bob", "Carol", "Dave", "Eve", "Frank"}

# Is backend_devs a subset of full_team? (all backend devs in full team?)
print("backend ⊆ full_team :", backend_devs.issubset(full_team))     # True
print("backend ⊆ full_team :", backend_devs <= full_team)            # operator form

# Is full_team a superset of python_devs?
print("full_team ⊇ python  :", full_team.issuperset(python_devs))    # True
print("full_team ⊇ python  :", full_team >= python_devs)             # operator form

# Proper subset (subset but NOT equal)
print("backend < backend   :", backend_devs < backend_devs)   # False (equal)
print("backend < full_team :", backend_devs < full_team)       # True (proper subset)

# ============================================================
#  6. DISJOINT — no elements in common
# ============================================================

print("\n=== DISJOINT ===")

frontend = {"Alice", "Frank"}
backend  = {"Bob", "Carol"}
overlap  = {"Alice", "Bob"}

print("frontend & backend disjoint:", frontend.isdisjoint(backend))   # True
print("frontend & overlap disjoint:", frontend.isdisjoint(overlap))   # False

# ============================================================
#  KEY POINTS
#  |  or .union()                → combine all elements
#  &  or .intersection()         → common elements only
#  -  or .difference()           → in A, not in B
#  ^  or .symmetric_difference() → in one but not both
#  .issubset() / <=              → A ⊆ B
#  .issuperset() / >=            → A ⊇ B
#  .isdisjoint()                 → no overlap
# ============================================================
