# ============================================================
#  defaultdict — Overview
#  Real-world context: Log analysis & grouping system
# ============================================================

from collections import defaultdict

# ============================================================
#  The problem with regular dict
# ============================================================

print("=== The Problem defaultdict Solves ===")

# Log entries: (user_id, action)
logs = [
    ("alice", "login"),  ("bob", "login"),   ("alice", "view_product"),
    ("carol", "login"),  ("alice", "add_cart"), ("bob", "view_product"),
    ("bob",   "logout"), ("alice", "purchase"), ("carol", "view_product"),
    ("carol", "logout"),
]

# REGULAR DICT — need to check if key exists first
user_actions_regular = {}
for user, action in logs:
    if user not in user_actions_regular:
        user_actions_regular[user] = []       # manually initialize
    user_actions_regular[user].append(action)

print("Regular dict result:", dict(user_actions_regular))

# ============================================================
#  defaultdict(list) — auto-initializes with empty list
# ============================================================

print("\n=== defaultdict(list) ===")

user_actions = defaultdict(list)    # default factory = list

for user, action in logs:
    user_actions[user].append(action)   # no KeyError, no if check!

print("User actions:")
for user, actions in sorted(user_actions.items()):
    print(f"  {user:<8}: {actions}")

# ============================================================
#  defaultdict(int) — default value = 0 (counter)
# ============================================================

print("\n=== defaultdict(int) — Counting ===")

# Count how many times each action was performed
action_count = defaultdict(int)
for _, action in logs:
    action_count[action] += 1   # starts at 0 automatically

print("Action frequencies:")
for action, count in sorted(action_count.items(), key=lambda x: -x[1]):
    bar = "█" * count
    print(f"  {action:<15} {count:>2}  {bar}")

# ============================================================
#  defaultdict(set) — group unique values
# ============================================================

print("\n=== defaultdict(set) — Unique Grouping ===")

# Which pages did each user visit (unique only)
page_visits = [
    ("alice", "/home"), ("bob", "/home"),    ("alice", "/products"),
    ("alice", "/home"), ("carol", "/about"),  ("bob", "/products"),
    ("bob",   "/home"), ("carol", "/home"),   ("alice", "/checkout"),
]

user_pages = defaultdict(set)
for user, page in page_visits:
    user_pages[user].add(page)

print("Unique pages per user:")
for user, pages in sorted(user_pages.items()):
    print(f"  {user:<8}: {sorted(pages)}")

# ============================================================
#  defaultdict(dict) — nested grouping
# ============================================================

print("\n=== defaultdict(dict) — Nested ===")

sales_data = [
    ("Electronics", "Laptop",  3),
    ("Electronics", "Mouse",  15),
    ("Furniture",   "Chair",   5),
    ("Electronics", "Tablet",  7),
    ("Furniture",   "Desk",    2),
    ("Electronics", "Mouse",   8),
]

# Group: category → {product: total_units_sold}
category_sales = defaultdict(lambda: defaultdict(int))

for category, product, units in sales_data:
    category_sales[category][product] += units

print("Category sales:")
for category, products in sorted(category_sales.items()):
    print(f"  [{category}]")
    for product, units in sorted(products.items()):
        print(f"    {product:<10} {units} units")

# ============================================================
#  defaultdict vs setdefault vs get
# ============================================================

print("\n=== Comparison ===")

text = "python is great python is fun python"
words = text.split()

# Using get()
count1 = {}
for w in words:
    count1[w] = count1.get(w, 0) + 1

# Using setdefault()
count2 = {}
for w in words:
    count2.setdefault(w, 0)
    count2[w] += 1

# Using defaultdict
count3 = defaultdict(int)
for w in words:
    count3[w] += 1

print("get()        :", dict(sorted(count1.items())))
print("setdefault() :", dict(sorted(count2.items())))
print("defaultdict  :", dict(sorted(count3.items())))

# ============================================================
#  KEY POINTS
#  defaultdict(list)   → auto empty list for new keys
#  defaultdict(int)    → auto 0 for new keys (counting)
#  defaultdict(set)    → auto empty set for new keys
#  defaultdict(dict)   → auto empty dict (nested grouping)
#  defaultdict(lambda: <val>) → any custom default
#  Eliminates manual key-existence checks before appending
# ============================================================
