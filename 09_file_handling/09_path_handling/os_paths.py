# ─────────────────────────────────────────────
# File Path Handling — os and os.path
# ─────────────────────────────────────────────

import os

# ── Current directory ─────────────────────────
print("cwd:", os.getcwd())
os.chdir(os.getcwd())           # change directory (no-op here)

# ── Path building ─────────────────────────────
# NEVER use string concatenation — use os.path.join
path = os.path.join("folder", "sub", "file.txt")
print("join     :", path)       # folder/sub/file.txt (or folder\sub\file.txt on Windows)

# ── Path components ───────────────────────────
full = "/home/jay/projects/app/main.py"
print("dirname  :", os.path.dirname(full))   # /home/jay/projects/app
print("basename :", os.path.basename(full))  # main.py
print("split    :", os.path.split(full))     # ('/home/jay/projects/app', 'main.py')
print("splitext :", os.path.splitext(full))  # ('/home/jay/projects/app/main', '.py')

name, ext = os.path.splitext("report.pdf")
print(f"name={name!r}  ext={ext!r}")

# ── Path checks ───────────────────────────────
print("\nexists   :", os.path.exists("."))
print("isfile   :", os.path.isfile("os_paths.py"))
print("isdir    :", os.path.isdir("."))
print("isabs    :", os.path.isabs("/home/jay"))   # True for absolute paths

# ── Absolute path ─────────────────────────────
relative = "data/file.txt"
print("abspath  :", os.path.abspath(relative))

# ── Directory operations ──────────────────────
os.makedirs("output/nested/deep", exist_ok=True)   # create all intermediate dirs
print("created nested dirs")

entries = os.listdir(".")       # list files/folders in directory
print("listdir  :", entries[:5])

# os.walk — recurse all files in a tree
print("\n=== os.walk ===")
for root, dirs, files in os.walk("."):
    level = root.replace(".", "").count(os.sep)
    indent = "  " * level
    print(f"{indent}{os.path.basename(root)}/")
    for file in files:
        print(f"{indent}  {file}")
    if level >= 1:              # limit depth for demo
        break

# ── File info ────────────────────────────────
import time
stat = os.stat("os_paths.py")
print("\n=== File stats ===")
print("Size  :", stat.st_size, "bytes")
print("Mtime :", time.ctime(stat.st_mtime))  # last modified

# ── Rename, move, remove ──────────────────────
with open("output/old.txt", "w") as f:
    f.write("data")

os.rename("output/old.txt", "output/new.txt")    # rename / move
print("renamed old.txt → new.txt")

os.remove("output/new.txt")                       # delete a file
print("deleted new.txt")

os.rmdir("output/nested/deep")                    # remove empty dir
import shutil
shutil.rmtree("output")                            # remove dir tree

# ── Environment variables ─────────────────────
home = os.environ.get("HOME") or os.environ.get("USERPROFILE")  # Linux/Windows
print("\nHome dir :", home)
print("PATH     :", os.environ.get("PATH", "not set")[:60] + "...")

# os.path.expanduser — ~ shortcut
print("expanduser:", os.path.expanduser("~"))
print("expandvars:", os.path.expandvars("$HOME"))   # or %USERPROFILE% on Windows
