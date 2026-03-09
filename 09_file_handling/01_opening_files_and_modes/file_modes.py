# ─────────────────────────────────────────────
# File Modes — open(file, mode, encoding)
# ─────────────────────────────────────────────

# Syntax:
#   f = open(filename, mode, encoding="utf-8")

# ── Text Modes ────────────────────────────────
#
#  "r"   read       — default; error if file doesn't exist
#  "w"   write      — creates file; OVERWRITES if exists
#  "a"   append     — creates file; adds to end if exists
#  "x"   exclusive  — creates file; error if already exists
#  "r+"  read+write — file must exist; doesn't truncate
#  "w+"  read+write — creates/truncates file
#  "a+"  read+append— creates file; reads from start, writes at end

# ── Binary Modes ─────────────────────────────
#
#  "rb"  read binary
#  "wb"  write binary  — images, PDFs, audio, etc.
#  "ab"  append binary
#  "rb+" read+write binary

# ── Mode behaviour summary ───────────────────
modes = {
    "r" : ("read",        "must exist",  "no",  "start"),
    "w" : ("write",       "creates",     "yes", "start"),
    "a" : ("append",      "creates",     "no",  "end"),
    "x" : ("exclusive",   "error exist", "yes", "start"),
    "r+": ("read+write",  "must exist",  "no",  "start"),
    "w+": ("read+write",  "creates",     "yes", "start"),
    "a+": ("read+append", "creates",     "no",  "end"),
}

header = f"  {'Mode':<4} {'Access':<12} {'File':<13} {'Truncate':<10} {'Pointer'}"
print(header)
print("  " + "-" * 55)
for mode, (access, file_req, truncate, pointer) in modes.items():
    print(f"  {mode!r:<4} {access:<12} {file_req:<13} {truncate:<10} {pointer}")

# ── Always specify encoding for text files ────
# Default encoding varies by OS — always be explicit
#   open("file.txt", "r", encoding="utf-8")

# ── File object attributes ────────────────────
import os
os.makedirs("temp_demo", exist_ok=True)
with open("temp_demo/demo.txt", "w", encoding="utf-8") as f:
    f.write("demo content")
    print("\nFile object attributes:")
    print("  f.name    :", f.name)
    print("  f.mode    :", f.mode)
    print("  f.closed  :", f.closed)
    print("  f.encoding:", f.encoding)

print("  f.closed after with:", f.closed)   # True — auto-closed

# Cleanup
import shutil
shutil.rmtree("temp_demo")
