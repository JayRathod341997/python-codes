# ─────────────────────────────────────────────
# Useful Standard Libraries — os & sys
# ─────────────────────────────────────────────

import os
import sys

# ══════════════════════════════════════════════
# os — Operating System Interface
# ══════════════════════════════════════════════

# ── Current directory ─────────────────────────
cwd = os.getcwd()
print(f"Current directory: {cwd}")

os.chdir(cwd)               # change working directory (reset to same here)
print(f"Back to: {os.getcwd()}")


# ── Directory listing ─────────────────────────
entries = os.listdir(".")           # names only
print(f"Entries in '.': {entries[:4]}...")

# Walk a directory tree recursively
# Real-life: find all .py files in a project
for root, dirs, files in os.walk("."):
    for f in files:
        if f.endswith(".py"):
            print(os.path.join(root, f))
    break       # only show first level for demo


# ── Create & remove directories ───────────────
# os.mkdir("new_dir")               # single level
# os.makedirs("a/b/c", exist_ok=True)  # nested, no error if exists
# os.rmdir("new_dir")               # remove empty dir
# os.removedirs("a/b/c")           # remove nested empty dirs


# ── File operations ───────────────────────────
# os.rename("old.txt", "new.txt")
# os.remove("file.txt")             # delete file

# Check existence
print(os.path.exists("notes.py"))   # True
print(os.path.isfile("notes.py"))   # True
print(os.path.isdir(".."))          # True

# Path manipulation
full_path  = os.path.abspath("notes.py")
dir_name   = os.path.dirname(full_path)
base_name  = os.path.basename(full_path)
name, ext  = os.path.splitext(base_name)

print(f"Full : {full_path}")
print(f"Dir  : {dir_name}")
print(f"Base : {base_name}")
print(f"Name : {name}  Ext: {ext}")

# Build paths safely (handles / vs \ on Windows/Linux)
config_path = os.path.join(dir_name, "config", "settings.json")
print(f"Config: {config_path}")

# File size
size_bytes = os.path.getsize("notes.py")
print(f"notes.py size: {size_bytes} bytes")


# ── Environment variables ─────────────────────
# Real-life: Read secrets / config from environment (12-factor apps)
home    = os.environ.get("HOME") or os.environ.get("USERPROFILE", "unknown")
python  = os.environ.get("PYTHONPATH", "not set")

print(f"HOME  : {home}")
print(f"PYTHONPATH: {python}")

# Set (affects only this process)
os.environ["MY_APP_ENV"] = "development"
print(os.environ["MY_APP_ENV"])


# ── Running shell commands ─────────────────────
# Real-life: Trigger a build, run a linter, etc.
exit_code = os.system("python --version")      # runs in shell, prints output
print(f"Exit code: {exit_code}")

# Better: subprocess (more control)
import subprocess
result = subprocess.run(
    ["python", "--version"],
    capture_output=True, text=True
)
print(f"Version: {result.stdout.strip()}")


# ── os.path quick reference ───────────────────
# os.path.join(a, b)      → combine paths
# os.path.exists(p)       → True if exists
# os.path.isfile(p)       → True if file
# os.path.isdir(p)        → True if directory
# os.path.abspath(p)      → absolute path
# os.path.basename(p)     → filename from path
# os.path.dirname(p)      → directory from path
# os.path.splitext(p)     → (name, ".ext")
# os.path.getsize(p)      → file size in bytes


# ══════════════════════════════════════════════
# sys — System-specific parameters and functions
# ══════════════════════════════════════════════

# ── Python version ────────────────────────────
print(f"Python version : {sys.version}")
print(f"Version info   : {sys.version_info}")
print(f"Platform       : {sys.platform}")    # 'win32', 'linux', 'darwin'

# Version guard — ensure minimum Python version
if sys.version_info < (3, 8):
    print("Python 3.8+ required")
    # sys.exit(1)


# ── Command-line arguments ────────────────────
# Real-life: script.py --env production --port 8080
# sys.argv[0] = script name, sys.argv[1:] = args
print(f"sys.argv: {sys.argv}")
# Run: python notes.py hello world → ['notes.py', 'hello', 'world']


# ── Standard streams ─────────────────────────
# sys.stdin   — read from keyboard / pipe
# sys.stdout  — default print target
# sys.stderr  — for errors (goes to terminal even if stdout is redirected)

print("Normal output", file=sys.stdout)
print("Error message", file=sys.stderr)


# ── sys.path — module search path ─────────────
print(f"Search paths (first 3): {sys.path[:3]}")

# Add a path at runtime
# sys.path.insert(0, "/my/libs")


# ── sys.exit() — exit the interpreter ─────────
# sys.exit(0)   → clean exit (code 0 = success)
# sys.exit(1)   → exit with error code 1
# Real-life: CLI tools that exit with meaningful codes


# ── sys.getsizeof() — memory size ─────────────
print(f"Size of int 0   : {sys.getsizeof(0)} bytes")
print(f"Size of 'hello' : {sys.getsizeof('hello')} bytes")
print(f"Size of []      : {sys.getsizeof([])} bytes")
print(f"Size of {}      : {sys.getsizeof({})} bytes")


# ── sys.modules — imported module cache ────────
print("os" in sys.modules)          # True — already imported
print("numpy" in sys.modules)       # False — not imported


# ── Key points ────────────────────────────────
# os:
#   • File system: listdir, walk, makedirs, remove, rename
#   • Paths: os.path.join, exists, isfile, isdir, abspath, getsize
#   • Env vars: os.environ.get("KEY", default)
#   • Run commands: os.system() or subprocess.run()
# sys:
#   • sys.argv    — CLI arguments
#   • sys.path    — module search paths
#   • sys.version — Python version
#   • sys.exit()  — exit with code
#   • sys.stdin/stdout/stderr — standard streams
#   • sys.getsizeof() — memory footprint of objects
