# ─────────────────────────────────────────────
# Dictionary Comprehension
# ─────────────────────────────────────────────

# ── Syntax ───────────────────────────────────
# {key_expr: value_expr  for  item  in  iterable}
# Short for:
#   result = {}
#   for item in iterable:
#       result[key_expr] = value_expr

# ── Basic example ─────────────────────────────
squares = {x: x ** 2 for x in range(1, 6)}
print(squares)      # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# ── Real-life 1: Config key normalisation ────
# DevOps — environment variables come in as uppercase strings,
# normalise to lowercase keys mapped to same value
env_vars = {"PORT": "8080", "HOST": "0.0.0.0", "DEBUG": "true"}
normalised = {k.lower(): v for k, v in env_vars.items()}
print(normalised)   # {'port': '8080', 'host': '0.0.0.0', 'debug': 'true'}

# ── Real-life 2: Product catalogue lookup ────
# E-commerce — build a fast O(1) lookup by product ID
products = [
    {"id": "P001", "name": "Laptop",  "price": 55000},
    {"id": "P002", "name": "Mouse",   "price":  799},
    {"id": "P003", "name": "Monitor", "price": 14999},
]
catalogue = {p["id"]: p for p in products}
print(catalogue["P002"])    # {'id': 'P002', 'name': 'Mouse', 'price': 799}

# ── Real-life 3: Word frequency counter ──────
# NLP / Search — count occurrences of each word
sentence = "to be or not to be that is the question to ask"
words    = sentence.split()
freq     = {word: words.count(word) for word in set(words)}
print(freq)     # {'to': 3, 'be': 2, 'or': 1, ...}

# ── Real-life 4: Score → grade mapping ───────
# School system — convert numeric scores to letter grades
scores = {"Alice": 92, "Bob": 74, "Carol": 55, "Dave": 88}

def grade(s):
    return "A" if s >= 90 else "B" if s >= 75 else "C" if s >= 60 else "F"

grades = {name: grade(score) for name, score in scores.items()}
print(grades)   # {'Alice': 'A', 'Bob': 'C', 'Carol': 'F', 'Dave': 'B'}

# ── Real-life 5: Invert a dictionary ─────────
# Reverse lookup — swap keys and values
country_code = {"India": "IN", "USA": "US", "Germany": "DE"}
code_country = {v: k for k, v in country_code.items()}
print(code_country)     # {'IN': 'India', 'US': 'USA', 'DE': 'Germany'}

# ── Building from two parallel lists ─────────
# zip() is very common with dict comprehensions
cities  = ["Mumbai", "Delhi", "Bangalore"]
temps   = [32, 28, 25]
weather = {city: temp for city, temp in zip(cities, temps)}
print(weather)  # {'Mumbai': 32, 'Delhi': 28, 'Bangalore': 25}

# ── Key points ───────────────────────────────
# • Keys must be hashable (str, int, tuple — not list or dict)
# • Duplicate keys: last value wins (same as regular dict assignment)
# • .items() gives (key, value) pairs — use tuple unpacking
# • zip() pairs two iterables — great for building dicts from parallel lists
# • Dict comprehensions preserve insertion order (Python 3.7+)
