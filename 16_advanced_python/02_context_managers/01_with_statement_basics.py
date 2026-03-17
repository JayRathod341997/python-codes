"""
============================================================
TOPIC: 01_with_statement_basics.py
Real-world context: File handling without and with context managers.
Demonstrates why 'with' is better than manual open/close.
============================================================
"""

import os

print("=" * 60)
print("SECTION 1: File Handling WITHOUT Context Manager")
print("=" * 60)

# Create a test file
test_file = "test_data.txt"
with open(test_file, "w") as f:
    f.write("Hello, World!\nPython is awesome!\n")

# Bad way: manual open and close (error-prone)
print("\n1. Manual open/close (old way):")
f = open(test_file, "r")
content = f.read()
f.close()  # Easy to forget!
print(f"Content: {content}")

# Problem: if exception happens, file stays open
print("\n2. The problem without 'with':")
print("If an exception occurs, file doesn't close!")
try:
    f = open(test_file, "r")
    content = f.read()
    raise ValueError("Simulated error")  # File leaks!
    f.close()
except ValueError as e:
    print(f"Exception caught: {e}")
    print(f"File still open? f.closed = {f.closed}")  # True after exception
    f.close()  # Manual cleanup needed


print("\n" + "=" * 60)
print("SECTION 2: File Handling WITH Context Manager")
print("=" * 60)

print("\n1. Using 'with' (modern, safe):")
with open(test_file, "r") as f:
    content = f.read()
    print(f"Content: {content}")
print(f"After 'with' block, file closed? f.closed = {f.closed}")

print("\n2. Exception safety with 'with':")
try:
    with open(test_file, "r") as f:
        content = f.read()
        raise ValueError("Simulated error")
except ValueError as e:
    print(f"Exception caught: {e}")
    print(f"File was closed automatically! f.closed = {f.closed}")


print("\n" + "=" * 60)
print("SECTION 3: Multiple Files with Context Manager")
print("=" * 60)

# Create second test file
output_file = "output.txt"
with open(test_file, "w") as f:
    f.write("Line 1\nLine 2\nLine 3\n")

# Read from one, write to another (both auto-close)
print("\n1. Multiple context managers:")
with open(test_file, "r") as inp, open(output_file, "w") as out:
    for line in inp:
        out.write(line.upper())
    print(f"Copied and converted to uppercase")

# Verify output
with open(output_file, "r") as f:
    print(f"Output file content:\n{f.read()}")


print("\n" + "=" * 60)
print("SECTION 4: Context Manager Compared to try-finally")
print("=" * 60)

print("\n1. Using try-finally (verbose):")
f = None
try:
    f = open(test_file, "r")
    content = f.read()
    print(f"Read {len(content)} characters")
finally:
    if f:
        f.close()
    print("Cleanup code runs in finally")

print("\n2. Using 'with' (clean):")
with open(test_file, "r") as f:
    content = f.read()
    print(f"Read {len(content)} characters")
print("Cleanup happens automatically")


print("\n" + "=" * 60)
print("SECTION 5: Why Context Manager is Better")
print("=" * 60)

benefits = """
1. AUTOMATIC CLEANUP
   - No need to remember to close()
   - Works even if exception occurs
   - Less boilerplate code

2. EXCEPTION SAFE
   - __exit__ runs even on error
   - No resource leaks
   - Clear entry/exit points

3. READABLE
   - Intent is clear: resource scope
   - No try-finally clutter
   - More Pythonic

4. REUSABLE
   - One 'with' line vs 5+ lines
   - Can create custom context managers
   - Works with any resource type
"""
print(benefits)


print("\n" + "=" * 60)
print("KEY POINTS")
print("=" * 60)
print("""
1. 'with' statement = context manager
   Syntax: with resource as var:

2. Context manager handles setup + cleanup
   - __enter__ runs on entry
   - __exit__ runs on exit (even on error)

3. Always use 'with' for files
   with open(filename) as f:
       data = f.read()

4. Multiple resources in one 'with'
   with open(in) as i, open(out, 'w') as o:
       process(i, o)

5. Exception safe by default
   - File closes even if code raises error
   - No try-finally needed

6. Built-in context managers
   - open() for files
   - Lock() for threading
   - TemporaryDirectory() for temp files
""")

# Cleanup
os.remove(test_file)
os.remove(output_file)
print("\nTest files cleaned up.")
