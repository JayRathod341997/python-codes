# ─────────────────────────────────────────────
# str — String Type Basics
# ─────────────────────────────────────────────

# ── Creating strings ─────────────────────────
s1 = 'single quotes'
s2 = "double quotes"
s3 = '''triple single — spans
multiple lines'''
s4 = """triple double — also
multiple lines"""

raw = r"C:\Users\name\folder"   # raw string — backslashes are literal
print(raw)

byte_str = b"bytes, not str"    # bytes literal (type: bytes)
print(type(byte_str))           # <class 'bytes'>

# ── String is a sequence ──────────────────────
word = "Python"
print(len(word))        # 6
print(word[0])          # 'P'   — indexing
print(word[-1])         # 'n'   — negative index from end
print(word[1:4])        # 'yth' — slicing [start:stop]
print(word[::2])        # 'Pto' — every 2nd character
print(word[::-1])       # 'nohtyP' — reversed

# ── Immutability ─────────────────────────────
# word[0] = "J"   # TypeError! strings cannot be changed in place

# ── Concatenation & repetition ────────────────
greeting = "Hello" + ", " + "World!"
print(greeting)

repeat = "ha" * 3
print(repeat)           # 'hahaha'

# ── Membership test ───────────────────────────
print("Py"  in  "Python")   # True
print("py"  in  "Python")   # False — case sensitive
print("xyz" not in "Python")# True

# ── Multiline strings ─────────────────────────
address = (
    "123 Main St\n"
    "Springfield\n"
    "USA"
)
print(address)

# ── Escape characters ─────────────────────────
print("Tab:\there")
print("Newline:\nhere")
print("Quote: \"quoted\"")
print("Backslash: \\")
print("Unicode: \u2764")    # ❤
