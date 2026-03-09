# ─────────────────────────────────────────────
# String Methods
# All methods return NEW strings — strings are immutable
# ─────────────────────────────────────────────

s = "  Hello, Python World!  "

# ── Case ─────────────────────────────────────
print(s.upper())            # "  HELLO, PYTHON WORLD!  "
print(s.lower())            # "  hello, python world!  "
print(s.title())            # "  Hello, Python World!  "
print(s.capitalize())       # "  hello, python world!  " → only first char
print(s.swapcase())         # swaps upper↔lower

# ── Stripping whitespace ──────────────────────
print(s.strip())            # "Hello, Python World!"
print(s.lstrip())           # "Hello, Python World!  "
print(s.rstrip())           # "  Hello, Python World!"
print("***hi***".strip("*")) # "hi"  — strip specific char

# ── Search & check ────────────────────────────
text = "Hello, Python World!"
print(text.find("Python"))      # 7   — index, -1 if not found
print(text.index("Python"))     # 7   — index, raises ValueError if not found
print(text.find("Java"))        # -1
print(text.count("l"))          # 3
print(text.startswith("Hello")) # True
print(text.endswith("!"))       # True

# ── Replace ───────────────────────────────────
print(text.replace("Python", "Java"))           # replaces all
print(text.replace("l", "L", 2))               # replace max 2 times

# ── Split & join ─────────────────────────────
csv = "apple,banana,cherry"
parts = csv.split(",")
print(parts)                # ['apple', 'banana', 'cherry']

lines = "line1\nline2\nline3"
print(lines.splitlines())   # ['line1', 'line2', 'line3']

words = ["Python", "is", "fun"]
print(" ".join(words))      # "Python is fun"
print("-".join(words))      # "Python-is-fun"
print("".join(words))       # "Pythonisfun"

# ── Padding & alignment ───────────────────────
print("42".zfill(5))        # "00042"  — zero-pad on left
print("hi".center(10))      # "    hi    "
print("hi".ljust(10, "-"))  # "hi--------"
print("hi".rjust(10, "-"))  # "--------hi"

# ── Validation checks ────────────────────────
print("abc123".isalnum())   # True  — only letters and digits
print("abc".isalpha())      # True  — only letters
print("123".isdigit())      # True  — only digits
print("  ".isspace())       # True  — only whitespace
print("Hello".istitle())    # True  — title case
print("HELLO".isupper())    # True
print("hello".islower())    # True

# ── Encode / decode ───────────────────────────
encoded = "hello".encode("utf-8")   # bytes
decoded = encoded.decode("utf-8")   # back to str
print(encoded, decoded)
