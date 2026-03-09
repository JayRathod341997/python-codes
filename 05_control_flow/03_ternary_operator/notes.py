# ─────────────────────────────────────────────
# Ternary Operator (Conditional Expression)
# ─────────────────────────────────────────────

# ── Syntax ───────────────────────────────────
# value_if_true  if  condition  else  value_if_false
#
# Reads naturally: "give me X if condition else give me Y"

# ── Basics ───────────────────────────────────
age = 20
status = "Adult" if age >= 18 else "Minor"
print(status)                   # Adult

# Equivalent if/else — ternary is just shorter:
# if age >= 18:
#     status = "Adult"
# else:
#     status = "Minor"

# ── Real-life: Discount label ────────────────
is_member = True
discount  = "10% member discount" if is_member else "No discount"
print(discount)

# ── Real-life: Even / Odd ────────────────────
number = 17
parity = "Even" if number % 2 == 0 else "Odd"
print(f"{number} is {parity}")

# ── Real-life: Pass / Fail grade ─────────────
marks = 72
result = "Pass" if marks >= 40 else "Fail"
print(f"Marks: {marks} → {result}")

# ── Real-life: Stock availability ────────────
stock = 0
availability = "In Stock" if stock > 0 else "Out of Stock"
print(availability)

# ── In f-strings (very common pattern) ───────
temperature = 38.2
print(f"Status: {'Fever' if temperature > 37.5 else 'Normal'}")

# ── Assigning default values ─────────────────
# Real-life: Config fallback
user_theme = None
theme = user_theme if user_theme else "dark"    # default to dark
print(f"Theme: {theme}")

# Pythonic equivalent using 'or':
theme = user_theme or "dark"
print(f"Theme (using or): {theme}")

# ── Chained ternary (use sparingly) ──────────
# Real-life: Traffic signal
speed = 85      # km/h

zone = "school zone" if speed <= 30 else "residential" if speed <= 60 else "highway"
print(f"Zone type: {zone}")

# Above equals:
# if speed <= 30:   zone = "school zone"
# elif speed <= 60: zone = "residential"
# else:             zone = "highway"

# ── Inside function calls ────────────────────
items = [3, 1, 4, 1, 5]
print(f"List has {'many' if len(items) > 3 else 'few'} items.")

# ── Key points ───────────────────────────────
# • Best for SIMPLE, single-value assignments — avoids boilerplate
# • Do NOT use for complex logic — hurts readability
# • Ternary does NOT replace if/else for blocks with multiple statements
# • Chaining more than 2 levels is a code smell — use if/elif instead
