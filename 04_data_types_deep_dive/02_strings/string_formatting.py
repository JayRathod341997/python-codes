# ─────────────────────────────────────────────
# String Formatting
# Three styles: %, .format(), f-strings
# ─────────────────────────────────────────────

name  = "Jay"
age   = 25
score = 98.567
pi    = 3.14159265

# ── 1. f-strings (Python 3.6+) — PREFERRED ───
print(f"Hello, {name}!")
print(f"Age: {age}, Score: {score:.2f}")

# Expressions inside f-strings
print(f"2 + 2 = {2 + 2}")
print(f"Upper: {name.upper()}")
print(f"Pi approx: {pi:.4f}")

# Formatting numbers
print(f"{1234567:,}")           # 1,234,567  — thousand separator
print(f"{0.456:.1%}")           # 45.6%      — percentage
print(f"{255:#010b}")           # 0b11111111 — binary with prefix
print(f"{255:#04x}")            # 0xff       — hex with prefix

# Alignment inside f-strings
print(f"{'left':<10}|")         # left-aligned
print(f"{'right':>10}|")        # right-aligned
print(f"{'center':^10}|")       # center-aligned
print(f"{'padded':*^10}|")      # custom fill char

# Debug shortcut (Python 3.8+): name=
x = 42
print(f"{x = }")                # x = 42

# ── 2. str.format() ───────────────────────────
print("\n--- .format() ---")
print("Hello, {}!".format(name))
print("Name: {0}, Age: {1}".format(name, age))
print("Name: {n}, Age: {a}".format(n=name, a=age))
print("Score: {:.2f}".format(score))
print("{:>10}".format("right"))

# ── 3. % formatting (old style) ───────────────
print("\n--- % formatting ---")
print("Hello, %s!" % name)
print("Age: %d, Score: %.2f" % (age, score))
print("%(name)s is %(age)d years old" % {"name": name, "age": age})

# ── Format spec mini-language summary ─────────
print("\n--- Format spec reference ---")
data = [
    ("Integer"        , f"{1234:d}"),
    ("Float 2dp"      , f"{pi:.2f}"),
    ("Scientific"     , f"{pi:.2e}"),
    ("Percentage"     , f"{0.856:.1%}"),
    ("Width 10"       , f"{'hi':10}"),
    ("Zero-padded"    , f"{42:05d}"),
    ("Thousands sep"  , f"{1234567:,}"),
    ("Binary"         , f"{10:b}"),
    ("Hex"            , f"{255:x}"),
    ("Octal"          , f"{8:o}"),
]
for label, result in data:
    print(f"  {label:<16} → {result}")
