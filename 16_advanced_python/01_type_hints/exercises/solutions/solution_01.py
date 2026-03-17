"""
============================================================
SOLUTION 01 — Type Hints: Basic Annotations & Functions
============================================================
Complete solution with proper type hints for student grade management.
============================================================
"""

from typing import Dict, Optional

# Store grades: student name -> grade
grades: Dict[str, float] = {}


def add_student(name: str, grade: float) -> None:
    """
    Add a student with their grade.

    Args:
        name: Student's name
        grade: Numerical grade (0-100)
    """
    grades[name] = grade
    print(f"[OK] Added {name} with grade {grade}")


def get_grade(name: str) -> Optional[float]:
    """
    Get a student's grade by name.

    Args:
        name: Student's name

    Returns:
        The grade if found, None otherwise
    """
    return grades.get(name)


def get_average() -> float:
    """
    Calculate average grade of all students.

    Returns:
        Average grade (0 if no students)
    """
    if not grades:
        return 0.0
    return sum(grades.values()) / len(grades)


def get_top_student() -> Optional[str]:
    """
    Get name of student with highest grade.

    Returns:
        Name of top student, None if no students
    """
    if not grades:
        return None
    # Find student with highest grade
    top_student = None
    max_grade = -1.0
    for name, grade in grades.items():
        if grade > max_grade:
            max_grade = grade
            top_student = name
    return top_student


def remove_student(name: str) -> bool:
    """
    Remove a student from the system.

    Args:
        name: Student's name

    Returns:
        True if removed, False if not found
    """
    if name in grades:
        del grades[name]
        print(f"[OK] Removed {name}")
        return True
    print(f"✗ {name} not found")
    return False


def get_all_students() -> Dict[str, float]:
    """
    Get all students and their grades.

    Returns:
        Dictionary of name -> grade
    """
    return grades.copy()


if __name__ == "__main__":
    print("=" * 60)
    print("SOLUTION 01 - Student Grade Management")
    print("=" * 60)

    # Test 1: Add students
    print("\n1. Adding students:")
    add_student("Alice", 95.5)
    add_student("Bob", 87.0)
    add_student("Charlie", 92.5)
    add_student("Diana", 88.0)

    # Test 2: Get individual grades
    print("\n2. Getting individual grades:")
    alice_grade = get_grade("Alice")
    print(f"Alice's grade: {alice_grade}")

    unknown_grade = get_grade("Unknown")
    print(f"Unknown student's grade: {unknown_grade}")

    # Test 3: Calculate average
    print("\n3. Average grade:")
    average = get_average()
    print(f"Average: {average:.2f}")

    # Test 4: Find top student
    print("\n4. Top performer:")
    top = get_top_student()
    print(f"Top student: {top}")

    # Test 5: Display all students
    print("\n5. All students:")
    all_students = get_all_students()
    for name, grade in sorted(all_students.items(), key=lambda x: x[1], reverse=True):
        print(f"  {name}: {grade}")

    # Test 6: Remove a student
    print("\n6. Removing a student:")
    remove_student("Bob")
    print(f"New average: {get_average():.2f}")

    # Test 7: Type safety example
    print("\n7. Type safety demonstration:")
    print("[OK] All functions have proper type hints")
    print("[OK] Type checker can verify correct usage")
    print("[OK] IDE provides autocompletion and error detection")
