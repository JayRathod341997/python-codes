# ───────────────────────────────────────────────────────────────
# Exercises — Project 04: HR Employee Directory
# ───────────────────────────────────────────────────────────────

# Use the employee database from solution.py or define your own with 10 employees.

# ── Exercise 1: Find All Employees Earning Above ₹80,000 ────────────
# Real-life: HR wants to identify high earners for an executive summary.
#
# Task: Create a function that filters employees by minimum salary.
#       Return a list of all employees earning ≥ ₹80,000.
#
# Requirements:
#   - Use a for loop to iterate through employees
#   - Collect those with salary >= 80000 into a list
#   - Return the list
#   - Print the results with formatting
#
# Hint: Similar to get_employees_by_dept(), but use salary comparison instead.

# --- your code here ---




# ── Exercise 2: List All Departments and Count Employees ────────────
# Real-life: HR manager needs a quick view of team sizes.
#
# Task: Create a report showing each department with headcount.
#
# Requirements:
#   - Extract unique departments (use set() or a dict)
#   - For each department, count employees
#   - Print formatted as: "Department (n=count)"
#   - Sort departments alphabetically
#
# Hint: Use a set to collect unique dept names, then loop through each
#       and call a counting function (or use len(get_employees_by_dept(dept))).

# --- your code here ---




# ── Exercise 3: Salary Analysis for a Specific Department ────────────
# Real-life: Engineering manager wants to understand salary distribution.
#
# Task: For the "Engineering" department, compute and display:
#       - Total employees
#       - Average salary
#       - Min/max salary
#       - List all employees sorted by salary (descending)
#
# Requirements:
#   - Use functions from solution.py (or create similar ones)
#   - Compute avg, min, max, and count
#   - Use sorted() to rank employees by salary
#   - Print a formatted report
#
# Hint: Combine multiple functions: get_employees_by_dept(), avg_salary_by_dept(),
#       and sorted() with a custom key.

# --- your code here ---




# ───────────────────────────────────────────────────────────────
# Expected outputs (for self-check):
#
# Ex1: Employees earning ≥ ₹80,000
#      Aditya Kumar — ₹85,000
#      Bhavna Sharma — ₹92,000
#      Jatin Mehta — ₹88,000
#      (Count: 3 employees)
#
# Ex2: Departments with headcount
#      Engineering (n=4)
#      HR (n=2)
#      Marketing (n=2)
#      Sales (n=2)
#
# Ex3: Engineering Department Report
#      Total: 4 employees
#      Average: ₹85,750
#      Range: ₹78,000–₹92,000
#      Salary ranking:
#        1. Bhavna Sharma — ₹92,000
#        2. Jatin Mehta — ₹88,000
#        3. Aditya Kumar — ₹85,000
#        4. Eshan Verma — ₹78,000
# ───────────────────────────────────────────────────────────────
