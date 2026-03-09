# ============================================================
#  LIST METHODS
#  Real-world context: Task / To-Do Manager
# ============================================================

tasks = ["Buy groceries", "Pay bills", "Call dentist"]
print("Initial tasks:", tasks)

# ============================================================
#  ADDING ITEMS
# ============================================================

print("\n--- Adding ---")

# append() — add single item to end  (O(1))
tasks.append("Schedule meeting")
print("After append :", tasks)

# insert() — add at specific position
tasks.insert(1, "Reply emails")   # urgent task at position 1
print("After insert :", tasks)

# extend() — add multiple items at once
new_tasks = ["Buy birthday gift", "Book flight"]
tasks.extend(new_tasks)
print("After extend :", tasks)

# ============================================================
#  REMOVING ITEMS
# ============================================================

print("\n--- Removing ---")

# remove() — removes FIRST matching value
tasks.remove("Pay bills")
print("After remove('Pay bills') :", tasks)

# pop() — removes and returns item at index (default: last)
completed = tasks.pop()
print(f"Completed task (popped)   : '{completed}'")
print("After pop()               :", tasks)

completed2 = tasks.pop(0)
print(f"Completed task (pop 0)    : '{completed2}'")
print("After pop(0)              :", tasks)

# clear() — remove ALL items (reset the list)
temp = ["a", "b", "c"]
temp.clear()
print("After clear()             :", temp)

# ============================================================
#  SEARCHING
# ============================================================

print("\n--- Searching ---")

tasks = ["Buy groceries", "Reply emails", "Call dentist", "Reply emails"]

# index() — position of FIRST match (raises ValueError if not found)
pos = tasks.index("Call dentist")
print("'Call dentist' is at index:", pos)

# count() — how many times a value appears
duplicates = tasks.count("Reply emails")
print("'Reply emails' appears    :", duplicates, "times")

# Use 'in' to safely check before index()
search = "Buy groceries"
if search in tasks:
    print(f"'{search}' found at index {tasks.index(search)}")

# ============================================================
#  ORDERING & REVERSING
# ============================================================

print("\n--- Ordering ---")

priorities = [3, 1, 4, 1, 5, 9, 2, 6]

# reverse() — reverses IN PLACE
priorities.reverse()
print("After reverse():", priorities)

# sort()    — sorts IN PLACE (ascending default)
priorities.sort()
print("After sort()   :", priorities)

priorities.sort(reverse=True)
print("Sort descending:", priorities)

# sorted()  — returns NEW sorted list, original unchanged
words = ["Banana", "apple", "Cherry", "date"]
print("sorted() case-sensitive :", sorted(words))
print("sorted() case-insensitive:", sorted(words, key=str.lower))
print("Original unchanged       :", words)

# ============================================================
#  OTHER USEFUL METHODS
# ============================================================

print("\n--- Other Methods ---")

nums = [1, 2, 3]
nums_copy = nums.copy()   # shallow copy
nums_copy.append(99)
print("Original:", nums)       # unaffected
print("Copy    :", nums_copy)

print("Min score:", min([45, 67, 82, 91, 55]))
print("Max score:", max([45, 67, 82, 91, 55]))
print("Total    :", sum([45, 67, 82, 91, 55]))
print("Length   :", len([45, 67, 82, 91, 55]))

# ============================================================
#  KEY POINTS
#  append / insert / extend  — add items
#  remove / pop / clear      — remove items
#  index / count / in        — search items
#  sort / reverse            — order items (in-place)
#  sorted()                  — returns new sorted list
# ============================================================
