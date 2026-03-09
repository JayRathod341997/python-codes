# ============================================================
# Multiple Assignment
# ============================================================
# Python allows several convenient ways to assign values to
# multiple variables in a single statement.
# ============================================================

# --- Assign same value to multiple variables ---
a = b = c = 0
print(a, b, c)          # 0 0 0

# --- Tuple unpacking (most common form) ---
x, y, z = 1, 2, 3
print(x, y, z)          # 1 2 3

# --- Swap two variables without a temp variable ---
p, q = 10, 20
print("Before swap:", p, q)
p, q = q, p
print("After swap:", p, q)

# --- Unpack from a list or tuple ---
coordinates = (40.7128, -74.0060)
latitude, longitude = coordinates
print("Lat:", latitude, "| Lon:", longitude)

# --- Extended unpacking with * (star expression) ---
first, *middle, last = [1, 2, 3, 4, 5]
print("First:", first)
print("Middle:", middle)    # [2, 3, 4]
print("Last:", last)

# --- Ignore values with _ (convention) ---
_, important, _ = (10, 42, 99)
print("Important value:", important)

# --- Unpack from a function returning multiple values ---
def get_dimensions():
    return 1920, 1080

width, height = get_dimensions()
print(f"Width: {width}, Height: {height}")
