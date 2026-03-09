# ─────────────────────────────────────────────
# File Iteration
# Files are iterators — loop line by line
# ─────────────────────────────────────────────

import os

os.makedirs("output", exist_ok=True)

# Create a sample file
SAMPLE = "output/data.txt"
with open(SAMPLE, "w", encoding="utf-8") as f:
    f.write("Alice,30,Engineer\n")
    f.write("Bob,25,Designer\n")
    f.write("# this is a comment\n")
    f.write("Charlie,35,Manager\n")
    f.write("\n")                   # blank line
    f.write("Diana,28,Developer\n")

# ── 1. Direct iteration — most Pythonic ───────
print("=== Direct iteration ===")
with open(SAMPLE, "r", encoding="utf-8") as f:
    for line in f:                  # f IS an iterator
        print(repr(line))

# ── 2. Strip newlines while iterating ─────────
print("\n=== Clean lines ===")
with open(SAMPLE, "r", encoding="utf-8") as f:
    for line in f:
        clean = line.rstrip("\n")   # or .strip() to also remove leading space
        print(clean)

# ── 3. Skip comments and blank lines ──────────
print("\n=== Skip comments & blanks ===")
with open(SAMPLE, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        print(line)

# ── 4. Enumerate — line numbers ───────────────
print("\n=== With line numbers ===")
with open(SAMPLE, "r", encoding="utf-8") as f:
    for num, line in enumerate(f, start=1):
        print(f"{num:3}: {line}", end="")

# ── 5. Process only first N lines ─────────────
print("\n\n=== First 2 lines only ===")
from itertools import islice
with open(SAMPLE, "r", encoding="utf-8") as f:
    for line in islice(f, 2):
        print(line, end="")

# ── 6. Filter lines with generator ────────────
def data_lines(filepath):
    """Yield only non-blank, non-comment lines."""
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#"):
                yield line

print("\n\n=== Generator filter ===")
for line in data_lines(SAMPLE):
    name, age, role = line.split(",")
    print(f"  {name} ({age}) — {role}")

# ── 7. Large file — memory-efficient reading ──
# Never use readlines() on huge files — it loads everything into RAM
# Instead, iterate line by line:
print("\n=== Memory-efficient large file handling ===")
count = 0
with open(SAMPLE, "r", encoding="utf-8") as f:
    for line in f:                  # only one line in memory at a time
        if line.strip() and not line.startswith("#"):
            count += 1
print(f"Data lines found: {count}")

# ── 8. iter() with sentinel ───────────────────
# Read chunks until empty string (EOF)
print("\n=== Chunk iteration ===")
with open(SAMPLE, "rb") as f:
    for chunk in iter(lambda: f.read(20), b""):   # reads 20 bytes at a time
        print(f"Chunk: {chunk!r}")

# Cleanup
import shutil
shutil.rmtree("output")
