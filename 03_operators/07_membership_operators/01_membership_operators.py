# ============================================================
# Membership Operators: in, not in
# ============================================================
# Membership operators test whether a value exists inside
# a sequence or collection.
#
#   in      → True if the value IS found in the sequence
#   not in  → True if the value is NOT found in the sequence
#
# Works with: str, list, tuple, set, dict, range
# ============================================================

# ============================================================
# Strings
# ============================================================

message = "Hello, Python!"

print("Python" in message)          # True
print("Java" in message)            # False
print("Hello" not in message)       # False
print("java" in message)            # False  (case-sensitive)

# Substring check
email = "user@example.com"
print("@" in email)                 # True
print(".com" in email)              # True

# ============================================================
# Lists and Tuples
# ============================================================

fruits = ["apple", "banana", "cherry"]

print("banana" in fruits)           # True
print("grape" in fruits)            # False
print("grape" not in fruits)        # True

# With tuples
primes = (2, 3, 5, 7, 11)
print(5 in primes)                  # True
print(4 in primes)                  # False

# ============================================================
# Sets (O(1) lookup — fastest for membership)
# ============================================================

allowed_users = {"alice", "bob", "carol"}

print("alice" in allowed_users)     # True
print("dave" in allowed_users)      # False

# ============================================================
# Dictionaries
# ============================================================
# 'in' on a dict checks KEYS, not values.

config = {"host": "localhost", "port": 8080, "debug": True}

print("host" in config)             # True
print("localhost" in config)        # False  (not a key!)
print("localhost" in config.values()) # True  (check values explicitly)
print("port" not in config)         # False

# ============================================================
# Range
# ============================================================

print(5 in range(1, 10))            # True
print(10 in range(1, 10))           # False  (10 is exclusive)
print(0 in range(0, 5))             # True

# ============================================================
# Practical uses
# ============================================================

# Validate user input
valid_choices = ["yes", "no", "maybe"]
user_input = "yes"
if user_input in valid_choices:
    print("Valid choice")           # Valid choice

# Guard against missing key before accessing dict
data = {"name": "Jay", "age": 22}
if "email" not in data:
    print("Email not provided")     # Email not provided

# Filter items using membership
blocked_words = {"spam", "scam", "fraud"}
message = "this is a scam offer"
words = message.split()
contains_blocked = any(word in blocked_words for word in words)
print(contains_blocked)             # True

# Check vowel
char = "e"
print(char in "aeiou")              # True
