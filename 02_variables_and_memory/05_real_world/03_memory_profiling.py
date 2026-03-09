# ============================================================
# Real World Example 3: Memory-Efficient Data Processing
# ============================================================
# Demonstrates: sys.getsizeof, generators vs lists, object
# identity, reference counting insight, and gc usage.
# ============================================================

import sys
import gc

# ---- Helper to print size nicely ----
def size_of(label: str, obj) -> None:
    print(f"  {label:<35s} {sys.getsizeof(obj):>8,} bytes")


print("=" * 55)
print("1. COMPARING MEMORY: list vs generator")
print("=" * 55)

N = 1_000_000

# List: all N integers created and stored at once
big_list = list(range(N))

# Generator: produces values on demand — only stores iterator state
big_gen = (x for x in range(N))

size_of("list of 1,000,000 integers", big_list)
size_of("generator (same range)",     big_gen)

# --- Use the generator (consumed once) ---
total = sum(big_gen)
print(f"\n  Sum via generator: {total:,}")

del big_list            # free memory immediately
gc.collect()


print("\n" + "=" * 55)
print("2. STRING BUILDING: + vs join")
print("=" * 55)

words = ["Python", "is", "awesome", "and", "memory-efficient"]

# BAD: creates N intermediate string objects
result_concat = ""
for w in words:
    result_concat = result_concat + " " + w   # new object each iteration

# GOOD: single join — one allocation
result_join = " ".join(words)

print(f"  concat result: {result_concat.strip()!r}")
print(f"  join   result: {result_join!r}")

size_of("concat result string", result_concat)
size_of("join   result string", result_join)


print("\n" + "=" * 55)
print("3. SLOTS: reducing per-instance memory")
print("=" * 55)

class WithDict:
    """Normal class — each instance has a __dict__ (flexible but heavy)."""
    def __init__(self, x, y):
        self.x = x
        self.y = y

class WithSlots:
    """Slots class — fixed attributes, no __dict__ per instance."""
    __slots__ = ("x", "y")
    def __init__(self, x, y):
        self.x = x
        self.y = y

obj_dict  = WithDict(1, 2)
obj_slots = WithSlots(1, 2)

size_of("instance with __dict__",  obj_dict)
size_of("instance with __slots__", obj_slots)
print(f"\n  __dict__ overhead: {sys.getsizeof(obj_dict.__dict__)} bytes")
print(f"  __slots__ has no __dict__: {not hasattr(obj_slots, '__dict__')}")


print("\n" + "=" * 55)
print("4. REFERENCE COUNTING INSIGHT")
print("=" * 55)

# Create a large object and track references
import sys

large = [0] * 10_000
print(f"  ref count (with getrefcount call): {sys.getrefcount(large)}")

alias_a = large
alias_b = large
print(f"  ref count with 2 aliases: {sys.getrefcount(large)}")

del alias_a
del alias_b
print(f"  ref count after deleting aliases: {sys.getrefcount(large)}")
print(f"  size: {sys.getsizeof(large):,} bytes")
del large


print("\n" + "=" * 55)
print("5. PRACTICAL TIPS")
print("=" * 55)
tips = [
    "Use generators for large sequences you iterate once.",
    "Use __slots__ for classes with many instances.",
    "Avoid accumulating data you no longer need; del or reassign.",
    "Prefer ''.join() over + for building strings in loops.",
    "Use gc.collect() after bulk deletion of cyclic structures.",
]
for i, tip in enumerate(tips, 1):
    print(f"  {i}. {tip}")
