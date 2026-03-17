"""
============================================================
EXERCISE 01 — Type Hints: Basic Annotations & Functions
============================================================
Problem: Build a student grade management system with proper type hints.

Requirements:
  1. Create a function that adds a student with name and grade
  2. Create a function that retrieves a student's grade by name
  3. Create a function that calculates the average grade
  4. All functions must have complete type hints (parameters + return)
  5. Handle the case where a student doesn't exist (use Optional)

Hint: Use Dict[str, float] to store name -> grade mapping
      Use Optional[float] when grade might not exist
      Make sure all functions have -> ReturnType hints
============================================================
"""

# Import required types
from typing import Dict, Optional, List

# TODO: Create your StudentGradeManager class or functions below

# Step 1: Create a dictionary to store student grades
# Example structure: {"Alice": 95.5, "Bob": 87.0}

# Step 2: Write function to add a student
# def add_student(grades: Dict[str, float], name: str, grade: float) -> None:
#     """Add a student with their grade."""
#     pass

# Step 3: Write function to get a student's grade
# def get_grade(grades: Dict[str, float], name: str) -> Optional[float]:
#     """Get a student's grade by name. Return None if not found."""
#     pass

# Step 4: Write function to calculate average
# def get_average(grades: Dict[str, float]) -> float:
#     """Calculate average grade of all students."""
#     pass

# Step 5: Write function to get top performer
# def get_top_student(grades: Dict[str, float]) -> Optional[str]:
#     """Get name of student with highest grade. Return None if empty."""
#     pass

# Step 6: Test your functions
if __name__ == "__main__":
    print("=" * 60)
    print("EXERCISE 01 - Student Grade Management")
    print("=" * 60)

    # Create a grades dictionary
    # TODO: Add students and test your functions

    # Example usage (uncomment after implementing):
    # add_student(grades, "Alice", 95.5)
    # add_student(grades, "Bob", 87.0)
    # print(f"Alice's grade: {get_grade(grades, 'Alice')}")
    # print(f"Average: {get_average(grades):.2f}")
    # print(f"Top student: {get_top_student(grades)}")

    print("\nImplementation pending...")
