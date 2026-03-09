# ============================================================
#  TUPLE BASICS
#  Real-world context: GPS / Location services
# ============================================================

# ============================================================
#  Creating tuples
# ============================================================

# Coordinates — perfect for tuples (lat, lon should never change)
home       = (19.0760, 72.8777)    # Mumbai
office     = (28.6139, 77.2090)    # New Delhi
restaurant = (12.9716, 77.5946)    # Bangalore

print("Home     :", home)
print("Office   :", office)
print("Restaurant:", restaurant)

# Single-element tuple — MUST have trailing comma
single = (42,)
not_a_tuple = (42)    # this is just an int!
print("\nSingle-element tuple:", single, type(single))
print("Without comma       :", not_a_tuple, type(not_a_tuple))

# Tuple without parentheses (packing)
point = 3.14, 2.71
print("Packed tuple        :", point, type(point))

# From other iterables
from_list  = tuple([1, 2, 3])
from_range = tuple(range(1, 6))
from_str   = tuple("hello")
print("From list  :", from_list)
print("From range :", from_range)
print("From string:", from_str)

# ============================================================
#  Accessing elements
# ============================================================

print("\n--- Accessing ---")

lat, lon = home
print(f"Latitude : {lat}")
print(f"Longitude: {lon}")

# Indexing (same as lists)
print("home[0]  :", home[0])
print("home[-1] :", home[-1])

# Slicing
rgb = (255, 128, 0)       # orange color
print("\nRGB       :", rgb)
print("RG only   :", rgb[:2])

# ============================================================
#  Tuple methods (only 2: count, index)
# ============================================================

print("\n--- Tuple Methods ---")

route = ("Delhi", "Agra", "Jaipur", "Agra", "Delhi")
print("Route        :", route)
print("Count 'Agra' :", route.count("Agra"))
print("Index 'Jaipur':", route.index("Jaipur"))

# ============================================================
#  Comparing tuples
# ============================================================

print("\n--- Comparison ---")

score_a = (92, "Alice")
score_b = (88, "Bob")
score_c = (92, "Adam")

print("score_a > score_b:", score_a > score_b)   # 92 > 88
print("score_a > score_c:", score_a > score_c)   # 92==92, then 'Alice' > 'Adam'

# ============================================================
#  Iteration
# ============================================================

print("\n--- Iteration ---")

waypoints = [
    ("Start",  19.0760, 72.8777),
    ("Stop 1", 20.0000, 73.0000),
    ("Stop 2", 21.1458, 79.0882),
    ("End",    22.7196, 75.8577),
]

print("Trip waypoints:")
for name, lat, lon in waypoints:
    print(f"  {name:<8} → lat={lat:.4f}, lon={lon:.4f}")

# ============================================================
#  KEY POINTS
#  - Tuples use () or just commas
#  - Single element: (val,) — trailing comma is required
#  - Indexed and sliced just like lists
#  - Only 2 methods: count() and index()
#  - Immutable (cannot change after creation)
# ============================================================
