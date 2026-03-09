# ─────────────────────────────────────────────
# Appending Data to Files
# Mode "a" — adds to end, never overwrites
# ─────────────────────────────────────────────

import os
from datetime import datetime

os.makedirs("output", exist_ok=True)
LOG_FILE = "output/app.log"

# ── 1. Basic append ───────────────────────────
# First write — creates the file
with open(LOG_FILE, "w", encoding="utf-8") as f:
    f.write("=== Log Started ===\n")

# Subsequent appends — file grows each time
for i in range(1, 4):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"Event {i}: something happened\n")

with open(LOG_FILE, "r", encoding="utf-8") as f:
    print(f.read())

# ── 2. Append vs Write — key difference ───────
# "w" — truncates (deletes old content) before writing
# "a" — seeks to end, preserves old content

with open("output/demo.txt", "w", encoding="utf-8") as f:
    f.write("original content\n")

with open("output/demo.txt", "a", encoding="utf-8") as f:
    f.write("appended line\n")

with open("output/demo.txt", "r", encoding="utf-8") as f:
    print(f.read())

# ── 3. Simple logger function ─────────────────
def log(message, filepath=LOG_FILE):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(filepath, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {message}\n")

log("User logged in")
log("File uploaded: photo.jpg")
log("User logged out")

print("\nLog after logger calls:")
with open(LOG_FILE, "r", encoding="utf-8") as f:
    print(f.read())

# ── 4. a+ mode — append and read ─────────────
# Write to end, but can also seek back and read
with open("output/notes.txt", "a+", encoding="utf-8") as f:
    f.write("New note added\n")
    f.seek(0)                       # rewind to start to read
    print("All notes:")
    print(f.read())

# ── 5. Append lines from a list ───────────────
new_entries = ["Alice,30\n", "Bob,25\n", "Charlie,35\n"]
with open("output/users.csv", "a", encoding="utf-8") as f:
    f.writelines(new_entries)

print("Appended users:")
with open("output/users.csv", "r", encoding="utf-8") as f:
    print(f.read())

# Cleanup
import shutil
shutil.rmtree("output")
