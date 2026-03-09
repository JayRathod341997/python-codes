# ============================================================
# Garbage Collection Basics
# ============================================================
# Python automatically manages memory via:
#   1. Reference counting (primary mechanism)
#   2. Cyclic garbage collector (handles reference cycles)
#
# You rarely need to manage memory manually in Python.
# ============================================================

import sys
import gc

print("=" * 55)
print("1. REFERENCE COUNTING")
print("=" * 55)

# Every object has a reference count (how many names point to it).
# When the count drops to 0, CPython immediately frees the memory.

data = [1, 2, 3]
print(f"ref count of data: {sys.getrefcount(data)}")
# Note: getrefcount itself adds 1 temporary reference

alias1 = data
alias2 = data
print(f"ref count with 2 aliases: {sys.getrefcount(data)}")

del alias1
print(f"ref count after del alias1: {sys.getrefcount(data)}")

del alias2
print(f"ref count after del alias2: {sys.getrefcount(data)}")

# When all references are removed, object is collected:
del data
# data is now freed (reference count hit 0)

print("\n" + "=" * 55)
print("2. REFERENCE CYCLES (why we need the GC)")
print("=" * 55)

# Reference counting alone can't handle cycles.
# Example: A → B → A  (both have ref count 1, but are unreachable)

class Node:
    def __init__(self, name):
        self.name = name
        self.next = None

    def __del__(self):
        print(f"  Node '{self.name}' deleted")

print("Creating cyclic reference...")
node_a = Node("A")
node_b = Node("B")
node_a.next = node_b    # A → B
node_b.next = node_a    # B → A  ← cycle!

# Even after del, ref counts stay > 0 (each holds the other)
del node_a
del node_b
# Objects might not be freed immediately due to cycle

print("Running garbage collector...")
collected = gc.collect()
print(f"GC collected {collected} objects")

print("\n" + "=" * 55)
print("3. GARBAGE COLLECTOR CONTROL")
print("=" * 55)

# --- Check if GC is enabled ---
print(f"GC enabled: {gc.isenabled()}")

# --- GC generations (0, 1, 2) ---
# New objects start in generation 0.
# Objects that survive collection are promoted to higher gens.
print(f"GC thresholds (gen0, gen1, gen2): {gc.get_threshold()}")
print(f"GC counts: {gc.get_count()}")

# --- Manual collection (rarely needed) ---
gc.collect(0)   # collect only generation 0
gc.collect()    # collect all generations

# --- Disable/enable GC (advanced use case) ---
# gc.disable()    # turns off cyclic GC (ref counting still works)
# gc.enable()     # re-enable

print("\n" + "=" * 55)
print("4. MEMORY-RELATED BUILTINS")
print("=" * 55)

# sys.getsizeof: size in bytes of an object (shallow)
print(f"size of int 0:       {sys.getsizeof(0)} bytes")
print(f"size of int 1000:    {sys.getsizeof(1000)} bytes")
print(f"size of empty list:  {sys.getsizeof([])} bytes")
print(f"size of empty dict:  {sys.getsizeof({})} bytes")
print(f"size of empty str:   {sys.getsizeof('')} bytes")
print(f"size of 'hello':     {sys.getsizeof('hello')} bytes")

# --- del keyword removes a NAME (binding), not necessarily the object ---
x = [1, 2, 3]
y = x
del x               # removes name 'x'; object still alive via 'y'
print(f"\ny still works: {y}")

print("\n--- Key takeaways ---")
print("• Reference counting frees most objects immediately.")
print("• The GC handles cycles reference counting can't resolve.")
print("• Use 'del' to remove a name; let the runtime handle memory.")
print("• Avoid creating large cycles; prefer weak references if needed.")
