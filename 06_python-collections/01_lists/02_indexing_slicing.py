# ============================================================
#  INDEXING & SLICING
#  Real-world context: Exam results management system
# ============================================================

scores = [45, 67, 82, 91, 55, 73, 88, 60, 95, 78]
students = ["Alice", "Bob", "Carol", "Dave", "Eve",
            "Frank", "Grace", "Hank", "Ivy", "Jack"]

print("All scores:", scores)
print("All students:", students)

# ============================================================
#  INDEXING  (0-based from start, -1-based from end)
# ============================================================

# First and last student
print("\n--- Indexing ---")
print("First student:", students[0], "| Score:", scores[0])
print("Last student :", students[-1], "| Score:", scores[-1])
print("3rd student  :", students[2], "| Score:", scores[2])

# ============================================================
#  SLICING  list[start : stop : step]
#   - stop index is EXCLUDED
#   - omitting start defaults to 0
#   - omitting stop  defaults to end
# ============================================================

print("\n--- Slicing ---")

# Top 3 students (indices 0,1,2)
print("First 3 scores :", scores[:3])

# Scores from index 5 onwards
print("From index 5   :", scores[5:])

# Middle section (index 3 to 7)
print("Middle scores  :", scores[3:7])

# Every other score (step=2)
print("Every 2nd score:", scores[::2])

# Reversed list (step=-1)
print("Reversed scores:", scores[::-1])

# Last 3 scores
print("Last 3 scores  :", scores[-3:])

# ============================================================
#  PRACTICAL USE: Find top & bottom performers
# ============================================================

print("\n--- Performance Analysis ---")

combined = list(zip(students, scores))
combined.sort(key=lambda x: x[1], reverse=True)

sorted_students = [s for s, _ in combined]
sorted_scores   = [sc for _, sc in combined]

print("Ranked students:", sorted_students)
print("Ranked scores  :", sorted_scores)

print("\nTop 3 performers:", sorted_students[:3])
print("Need support    :", sorted_students[-3:])

# ============================================================
#  MODIFYING via index
# ============================================================

print("\n--- Modifying via index ---")
print("Before:", scores)
scores[0] = 50     # Alice retook the exam
print("After (Alice corrected to 50):", scores)

# Slice assignment — replace multiple values at once
scores[1:3] = [70, 85]
print("After slice assignment [1:3]:", scores)

# ============================================================
#  KEY POINTS
#  - Positive index: left to right  (0, 1, 2 ...)
#  - Negative index: right to left  (-1, -2, -3 ...)
#  - slice[start:stop:step] — stop is exclusive
#  - Slice assignment modifies list in-place
# ============================================================
