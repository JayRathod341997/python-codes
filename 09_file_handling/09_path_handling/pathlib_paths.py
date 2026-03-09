# ─────────────────────────────────────────────
# File Path Handling — pathlib (Python 3.4+)
# Modern, OOP approach — preferred over os.path
# ─────────────────────────────────────────────

from pathlib import Path
import shutil

# ── Creating paths ────────────────────────────
p = Path("folder/sub/file.txt")     # relative
a = Path("/home/jay/projects")      # absolute
h = Path.home()                     # home directory
c = Path.cwd()                      # current working directory

print("relative :", p)
print("home     :", h)
print("cwd      :", c)

# ── / operator — join paths ───────────────────
base = Path("output")
full = base / "data" / "report.csv"    # much nicer than os.path.join!
print("joined   :", full)

# ── Path components ───────────────────────────
path = Path("/home/jay/projects/app/main.py")
print("\nname    :", path.name)         # main.py
print("stem    :", path.stem)           # main
print("suffix  :", path.suffix)         # .py
print("suffixes:", path.suffixes)       # ['.py']
print("parent  :", path.parent)         # /home/jay/projects/app
print("parents :", list(path.parents))  # all parent paths
print("parts   :", path.parts)          # ('/', 'home', 'jay', ...)

# ── Checks ────────────────────────────────────
print("\nexists  :", c.exists())
print("is_file :", c.is_file())
print("is_dir  :", c.is_dir())
print("is_abs  :", path.is_absolute())

# ── Creating directories ──────────────────────
output = Path("output")
output.mkdir(parents=True, exist_ok=True)
(output / "nested" / "deep").mkdir(parents=True, exist_ok=True)
print("\nCreated:", output / "nested" / "deep")

# ── Reading and writing ───────────────────────
file = output / "notes.txt"

# Write — no need for open()!
file.write_text("Hello from pathlib!\nSecond line\n", encoding="utf-8")

# Read
content = file.read_text(encoding="utf-8")
print("\nRead:", content)

# Binary
bin_file = output / "data.bin"
bin_file.write_bytes(b"\x00\x01\x02\x03")
print("Binary:", bin_file.read_bytes())

# ── Listing directory contents ────────────────
print("\n=== iterdir() ===")
for item in c.iterdir():
    kind = "DIR " if item.is_dir() else "FILE"
    print(f"  {kind}  {item.name}")

# ── Glob patterns ─────────────────────────────
print("\n=== glob ===")
# Find all .py files in current directory
for py_file in c.glob("*.py"):
    print(f"  {py_file.name}")

# ** = recursive
for py_file in c.glob("**/*.py"):
    print(f"  {py_file}")

# ── File stats ────────────────────────────────
import time
stat = file.stat()
print(f"\nSize  : {stat.st_size} bytes")
print(f"Mtime : {time.ctime(stat.st_mtime)}")

# ── Rename, replace, unlink ───────────────────
src = output / "old.txt"
dst = output / "new.txt"
src.write_text("temp", encoding="utf-8")
src.rename(dst)         # rename/move
print("\nRenamed:", src, "→", dst)

dst.unlink()            # delete the file
print("Deleted:", dst)

# ── Resolve — absolute + normalize ────────────
relative = Path("../pathlib_paths.py")
# print("Resolved:", relative.resolve())   # uncomment to see full absolute path

# ── with_name / with_suffix ───────────────────
p = Path("report.txt")
print(p.with_name("summary.txt"))      # report.txt → summary.txt
print(p.with_suffix(".pdf"))           # report.txt → report.pdf
print(p.with_stem("final"))            # report.txt → final.txt (Python 3.9+)

# ── os.path vs pathlib quick comparison ───────
print("\n=== os.path vs pathlib ===")
comparisons = [
    ("os.path.join(a, b)",  "Path(a) / b"),
    ("os.path.basename(p)", "p.name"),
    ("os.path.dirname(p)",  "p.parent"),
    ("os.path.splitext(p)", "p.stem, p.suffix"),
    ("os.path.exists(p)",   "p.exists()"),
    ("os.makedirs(p)",      "p.mkdir(parents=True)"),
    ("open(p).read()",      "p.read_text()"),
]
for old, new in comparisons:
    print(f"  {old:<30} →  {new}")

# Cleanup
shutil.rmtree("output")
