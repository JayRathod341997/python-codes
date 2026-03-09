# ─────────────────────────────────────────────
# Reading Files — read, readline, readlines
# ─────────────────────────────────────────────

FILE = "sample.txt"     # make sure sample.txt is in the same folder

# ── 1. read() — entire file as one string ─────
with open(FILE, "r", encoding="utf-8") as f:
    content = f.read()
print("=== read() ===")
print(content)

# read(n) — read only n characters
with open(FILE, "r", encoding="utf-8") as f:
    chunk = f.read(20)
print(f"First 20 chars: {chunk!r}")

# ── 2. readline() — one line at a time ────────
print("\n=== readline() ===")
with open(FILE, "r", encoding="utf-8") as f:
    line1 = f.readline()    # reads up to and including \n
    line2 = f.readline()
    print(repr(line1))
    print(repr(line2))

# Read all lines manually with readline()
with open(FILE, "r", encoding="utf-8") as f:
    while True:
        line = f.readline()
        if not line:        # empty string = end of file
            break
        print(line, end="") # line already has \n

# ── 3. readlines() — all lines as a list ──────
print("\n=== readlines() ===")
with open(FILE, "r", encoding="utf-8") as f:
    lines = f.readlines()   # list of strings, each ending with \n

print(lines)
print(f"Total lines: {len(lines)}")

# Strip newlines
clean = [line.rstrip("\n") for line in lines]
print(clean)

# ── 4. File pointer — tell() and seek() ───────
print("\n=== tell() and seek() ===")
with open(FILE, "r", encoding="utf-8") as f:
    print("Position:", f.tell())        # 0 — start
    f.read(10)
    print("After read(10):", f.tell())  # 10

    f.seek(0)                           # rewind to start
    print("After seek(0):", f.tell())   # 0

    f.seek(0, 2)                        # seek to end (whence=2)
    print("End position:", f.tell())    # file size in bytes

# ── 5. Reading binary files ───────────────────
print("\n=== Binary read ===")
with open(FILE, "rb") as f:             # 'rb' = read binary
    raw = f.read()

print(f"Bytes type: {type(raw)}")
print(f"First 20 bytes: {raw[:20]}")
print(f"Decoded: {raw[:20].decode('utf-8')!r}")

# ── 6. Read with size limit (memory safe) ─────
print("\n=== Chunked reading ===")
CHUNK = 30  # read 30 bytes at a time
with open(FILE, "r", encoding="utf-8") as f:
    while chunk := f.read(CHUNK):       # walrus operator
        print(f"Chunk: {chunk!r}")
