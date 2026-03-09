# ─────────────────────────────────────────────
# The with Statement — Context Manager
# ─────────────────────────────────────────────

import os

os.makedirs("output", exist_ok=True)

# ── Why with? ────────────────────────────────
# Files must be closed after use. Manual approach is fragile:

def bad_way():
    f = open("output/test.txt", "w", encoding="utf-8")
    f.write("data")
    # If an exception happens here, f.close() is NEVER called
    # → resource leak (file stays locked)
    f.close()

# with guarantees __exit__ (which closes file) runs no matter what:
def good_way():
    with open("output/test.txt", "w", encoding="utf-8") as f:
        f.write("data")
    # f is closed here — even if an exception was raised inside

# ── Basic usage ───────────────────────────────
with open("output/hello.txt", "w", encoding="utf-8") as f:
    f.write("Hello from with statement!\n")

with open("output/hello.txt", "r", encoding="utf-8") as f:
    print(f.read())

# ── Multiple files in one with ────────────────
with (
    open("output/source.txt", "w", encoding="utf-8") as src,
    open("output/dest.txt",   "w", encoding="utf-8") as dst,
):
    src.write("source content\n")
    dst.write("destination content\n")

print("Both files closed:", src.closed, dst.closed)

# ── with still catches the error ─────────────
# Even when an exception occurs, the file is properly closed
try:
    with open("output/error_test.txt", "w", encoding="utf-8") as f:
        f.write("before error\n")
        raise ValueError("something went wrong")
except ValueError as e:
    print(f"Caught: {e}")
    print("File closed despite error:", f.closed)   # True

# ── How it works — __enter__ and __exit__ ─────
class ManagedFile:
    def __init__(self, path, mode):
        self.path = path
        self.mode = mode
        self.file = None

    def __enter__(self):
        print("Opening file...")
        self.file = open(self.path, self.mode, encoding="utf-8")
        return self.file             # bound to 'as' variable

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Closing file...")
        if self.file:
            self.file.close()
        return False                 # False = don't suppress exceptions

with ManagedFile("output/managed.txt", "w") as f:
    f.write("written via custom context manager\n")

# ── contextlib.contextmanager — simpler way ───
from contextlib import contextmanager

@contextmanager
def open_file(path, mode, encoding="utf-8"):
    f = open(path, mode, encoding=encoding)
    try:
        yield f          # everything before yield is __enter__
    finally:
        f.close()        # everything in finally is __exit__

with open_file("output/ctx.txt", "w") as f:
    f.write("written via @contextmanager\n")

print("ctx.txt closed:", f.closed)

# Cleanup
import shutil
shutil.rmtree("output")
