# ─────────────────────────────────────────────
# Writing Files
# ─────────────────────────────────────────────

import os
import json

os.makedirs("output", exist_ok=True)

# ── 1. write() — write a string ──────────────
with open("output/hello.txt", "w", encoding="utf-8") as f:
    f.write("Hello, World!\n")
    f.write("Second line\n")
    f.write("Third line\n")

print("wrote hello.txt")

# ── 2. writelines() — write a list of strings ─
# Note: writelines does NOT add newlines automatically
lines = [
    "Apple\n",
    "Banana\n",
    "Cherry\n",
]

with open("output/fruits.txt", "w", encoding="utf-8") as f:
    f.writelines(lines)

print("wrote fruits.txt")

# ── 3. print() to a file ─────────────────────
with open("output/logged.txt", "w", encoding="utf-8") as f:
    print("This goes to the file", file=f)
    print("So does this", file=f)
    print(42, True, [1, 2, 3], file=f)  # print handles types automatically

print("wrote logged.txt")

# ── 4. write() returns number of chars written ─
with open("output/count_test.txt", "w", encoding="utf-8") as f:
    n = f.write("Hello!")
    print(f"Wrote {n} characters")

# ── 5. Overwrite behaviour ────────────────────
# "w" mode always starts fresh — previous content is GONE
with open("output/overwrite.txt", "w", encoding="utf-8") as f:
    f.write("First write\n")

with open("output/overwrite.txt", "w", encoding="utf-8") as f:
    f.write("Second write\n")    # First write is gone!

with open("output/overwrite.txt", "r", encoding="utf-8") as f:
    print("After overwrite:", f.read())

# ── 6. Write binary files ─────────────────────
data = bytes([0x50, 0x79, 0x74, 0x68, 0x6F, 0x6E])  # "Python" in bytes
with open("output/binary.bin", "wb") as f:
    f.write(data)

with open("output/binary.bin", "rb") as f:
    print("Binary read back:", f.read().decode("ascii"))

# ── 7. Safe write — write to temp then rename ─
# Prevents partial writes if program crashes mid-write
import tempfile
import shutil

TARGET = "output/safe_output.txt"
content = "Important data\n" * 5

# Write to temp file first
with tempfile.NamedTemporaryFile("w", delete=False,
                                  suffix=".tmp", encoding="utf-8") as tmp:
    tmp.write(content)
    tmp_path = tmp.name

# Atomically replace target with temp file
shutil.move(tmp_path, TARGET)
print(f"Safe write complete: {TARGET}")

# Cleanup
shutil.rmtree("output")
