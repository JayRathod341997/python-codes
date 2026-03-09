# ============================================================
#  SET CREATION
#  Real-world context: User tag & interest system
# ============================================================

# ============================================================
#  Creating sets
# ============================================================

print("=== Creating Sets ===")

# 1. Curly braces — a user's interest tags
interests = {"python", "data-science", "machine-learning", "python", "web-dev"}
print("1. From literal (duplicates removed):", interests)

# 2. set() from list (deduplicate)
raw_tags = ["travel", "food", "fitness", "travel", "food", "photography"]
unique_tags = set(raw_tags)
print("2. From list   :", unique_tags)

# 3. set() from string (unique characters)
chars = set("banana")
print("3. From string :", chars)

# 4. set() from range
even_nums = set(range(0, 20, 2))
print("4. From range  :", even_nums)

# 5. Set comprehension
squares = {x**2 for x in range(1, 8)}
print("5. Comprehension:", squares)

# 6. Empty set — MUST use set(), NOT {}
empty_set  = set()
empty_dict = {}     # this is a dict, NOT a set!
print("6. Empty set :", empty_set,  type(empty_set))
print("   Empty dict:", empty_dict, type(empty_dict))

# ============================================================
#  Sets are UNORDERED — no guaranteed order
# ============================================================

print("\n=== Unordered Nature ===")
s = {3, 1, 4, 1, 5, 9, 2, 6, 5, 3}
print("Set (no duplicates, unordered):", s)
print("Sorted output:", sorted(s))   # use sorted() if you need order

# ============================================================
#  Sets allow only HASHABLE elements
# ============================================================

print("\n=== Hashable Elements Only ===")

valid_set = {1, "hello", (1, 2), True, 3.14}
print("Valid set:", valid_set)

try:
    invalid = {1, [2, 3]}    # list is not hashable
except TypeError as e:
    print(f"Lists not allowed: {e}")

# ============================================================
#  Real-world: Deduplication of database records
# ============================================================

print("\n=== Deduplication Use Case ===")

# Email newsletter — remove duplicate subscribers
subscribers_raw = [
    "alice@mail.com", "bob@mail.com", "alice@mail.com",
    "carol@mail.com", "bob@mail.com", "dave@mail.com",
]
print("Raw list     :", subscribers_raw)
print("Raw count    :", len(subscribers_raw))

unique_subscribers = set(subscribers_raw)
print("Unique emails:", sorted(unique_subscribers))
print("Unique count :", len(unique_subscribers))
print("Duplicates   :", len(subscribers_raw) - len(unique_subscribers))

# ============================================================
#  Checking membership — O(1) average vs O(n) for list
# ============================================================

print("\n=== Membership Check ===")

banned_words = {"spam", "scam", "fake", "fraud", "hack"}
message = "this is a totally legitimate offer, not a scam at all"

found = [w for w in message.split() if w in banned_words]
print("Banned words in message:", found)
print("Message flagged:", len(found) > 0)

# ============================================================
#  KEY POINTS
#  - Created with {} or set()
#  - Empty set: MUST use set()  (not {})
#  - Unordered — no indexing, no slicing
#  - No duplicates — automatically unique
#  - Elements must be hashable (no lists, no dicts)
#  - O(1) membership check — much faster than lists
# ============================================================
