# ─────────────────────────────────────────────
# Opening Files — the open() built-in
# ─────────────────────────────────────────────

import os

# Create a sample file to work with
os.makedirs("temp_demo", exist_ok=True)
FILEPATH = "temp_demo/sample.txt"

with open(FILEPATH, "w", encoding="utf-8") as f:
    f.write("Line 1: Hello, World!\n")
    f.write("Line 2: Python file handling\n")
    f.write("Line 3: End of file\n")

# ── Method 1: Manual open/close (NOT recommended) ─
f = open(FILEPATH, "r", encoding="utf-8")
content = f.read()
f.close()               # MUST close manually — if exception occurs before this,
print("Manual open:")   # file stays open (resource leak)
print(content)

# ── Method 2: with statement (ALWAYS preferred) ───
with open(FILEPATH, "r", encoding="utf-8") as f:
    content = f.read()
# File is auto-closed here even if an error occurs inside
print("With statement:")
print(content)

# ── File not found ────────────────────────────
try:
    with open("nonexistent.txt", "r") as f:
        pass
except FileNotFoundError as e:
    print(f"Error: {e}")

# ── File already exists — exclusive mode ──────
try:
    with open(FILEPATH, "x") as f:   # "x" = create new only
        pass
except FileExistsError as e:
    print(f"Error: {e}")

# ── open() full signature ─────────────────────
# open(file, mode='r', buffering=-1, encoding=None,
#      errors=None, newline=None, closefd=True, opener=None)

# encoding   : "utf-8", "latin-1", "ascii", etc.
# errors     : "strict"(default), "ignore", "replace"
# newline    : None, "", "\n", "\r", "\r\n"

# Cleanup
import shutil
shutil.rmtree("temp_demo")
