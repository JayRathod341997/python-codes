# ─────────────────────────────────────────────────────────────────
# Project 04 — HR — Employee Directory & Salary Analysis
# Concepts  : list of dicts, functions, for loops, sorted(), enumerate()
# Difficulty: Intermediate
# ─────────────────────────────────────────────────────────────────

# ── Section 1: Employee Database ───────────────────────────────────
# 10 employees as a list of dictionaries
# Each dict: emp_id, name, department, salary (in ₹)
# In production, you'd read this from a database using SQL

employees = [
    {"emp_id": 101, "name": "Aditya Kumar", "dept": "Engineering", "salary": 85000},
    {"emp_id": 102, "name": "Bhavna Sharma", "dept": "Engineering", "salary": 92000},
    {"emp_id": 103, "name": "Chirag Patel", "dept": "Sales", "salary": 65000},
    {"emp_id": 104, "name": "Deepika Singh", "dept": "HR", "salary": 55000},
    {"emp_id": 105, "name": "Eshan Verma", "dept": "Engineering", "salary": 78000},
    {"emp_id": 106, "name": "Fiona Das", "dept": "Marketing", "salary": 62000},
    {"emp_id": 107, "name": "Ganesh Rao", "dept": "Sales", "salary": 70000},
    {"emp_id": 108, "name": "Hiral Joshi", "dept": "HR", "salary": 52000},
    {"emp_id": 109, "name": "Iris Wong", "dept": "Marketing", "salary": 68000},
    {"emp_id": 110, "name": "Jatin Mehta", "dept": "Engineering", "salary": 88000},
]

print("\n" + "="*70)
print("TECHCORP — EMPLOYEE DIRECTORY & SALARY ANALYSIS")
print("="*70)

# ── Section 2: Lookup Employee by ID ───────────────────────────────
# ── CONCEPT: for loop with early exit ──────────────────────────────
# We loop through employees until we find a match, then return immediately.
# This is more efficient than storing in a dict, especially for learning.

def lookup_employee_by_id(emp_id):
    """Find employee by ID using a for loop with early exit."""
    for emp in employees:
        if emp["emp_id"] == emp_id:
            return emp
    return None  # Not found

def lookup_employee_by_name(name):
    """Find employee by name (case-insensitive substring match)."""
    name_lower = name.lower()
    for emp in employees:
        if name_lower in emp["name"].lower():
            return emp
    return None

print("\nLOOKUP EXAMPLES:")
print("─" * 70)

emp_found = lookup_employee_by_id(105)
if emp_found:
    print(f"Employee ID 105: {emp_found['name']} ({emp_found['dept']}) — ₹{emp_found['salary']:,.0f}")

emp_found = lookup_employee_by_name("Aditya")
if emp_found:
    print(f"Search 'Aditya': {emp_found['name']} (ID: {emp_found['emp_id']}) — ₹{emp_found['salary']:,.0f}")

# ── Section 3: Filter by Department ────────────────────────────────
# ── CONCEPT: for loop collecting matches into a list ───────────────
# We iterate through all employees and build a new list of those
# matching the department filter.

def get_employees_by_dept(dept_name):
    """Return all employees in a given department."""
    results = []
    for emp in employees:
        if emp["dept"] == dept_name:
            results.append(emp)
    return results

print("\nENGINEERING DEPARTMENT:")
print("─" * 70)

eng_employees = get_employees_by_dept("Engineering")
for emp in eng_employees:
    print(f"  {emp['name']:<20} (ID: {emp['emp_id']}) — ₹{emp['salary']:>8,.0f}")

# ── Section 4: Average Salary by Department ────────────────────────
# ── CONCEPT: sum() and division pattern ────────────────────────────
# We use sum() with a manual loop to add up salaries,
# then divide by count. In Project 10, we'll use sum(comprehension).

def avg_salary_by_dept(dept_name):
    """Compute average salary for a department."""
    dept_employees = get_employees_by_dept(dept_name)
    if len(dept_employees) == 0:
        return 0
    total_salary = sum(emp["salary"] for emp in dept_employees)
    return total_salary / len(dept_employees)

print("\nAVERAGE SALARY BY DEPARTMENT:")
print("─" * 70)

# Get unique departments
departments = set()
for emp in employees:
    departments.add(emp["dept"])

for dept in sorted(departments):
    avg_sal = avg_salary_by_dept(dept)
    count = len(get_employees_by_dept(dept))
    print(f"  {dept:<15} (n={count}): ₹{avg_sal:>10,.0f}")

# ── Section 5: Top Earners (sorted + enumerate) ────────────────────
# ── CONCEPT: sorted() with custom key ──────────────────────────────
# We use sorted(employees, key=...) to sort by salary in descending order.
# enumerate() pairs each employee with their rank (0, 1, 2, ...).

print("\nTOP 5 EARNERS:")
print("─" * 70)

sorted_employees = sorted(employees, key=lambda x: x["salary"], reverse=True)

for rank, emp in enumerate(sorted_employees[:5], start=1):
    print(f"  {rank}. {emp['name']:<20} ({emp['dept']:<12}) — ₹{emp['salary']:>10,.0f}")

# ── Section 6: Salary Range by Department ──────────────────────────
# ── CONCEPT: max() and min() on salary values ──────────────────────

def get_salary_range_by_dept(dept_name):
    """Return min and max salary for a department."""
    dept_employees = get_employees_by_dept(dept_name)
    if len(dept_employees) == 0:
        return 0, 0
    salaries = [emp["salary"] for emp in dept_employees]
    return min(salaries), max(salaries)

print("\nSALARY RANGE BY DEPARTMENT:")
print("─" * 70)

for dept in sorted(departments):
    min_sal, max_sal = get_salary_range_by_dept(dept)
    range_val = max_sal - min_sal
    print(f"  {dept:<15} | Min: ₹{min_sal:>10,.0f} | Max: ₹{max_sal:>10,.0f} | Range: ₹{range_val:>10,.0f}")

# ── Section 7: Summary Statistics ──────────────────────────────────
print("\nCOMPANY-WIDE STATISTICS:")
print("─" * 70)

all_salaries = [emp["salary"] for emp in employees]
avg_salary = sum(all_salaries) / len(all_salaries)
median_idx = len(all_salaries) // 2
median_salary = sorted(all_salaries)[median_idx]

print(f"  Total employees: {len(employees)}")
print(f"  Average salary:  ₹{avg_salary:>10,.0f}")
print(f"  Median salary:   ₹{median_salary:>10,.0f}")
print(f"  Highest salary:  ₹{max(all_salaries):>10,.0f}")
print(f"  Lowest salary:   ₹{min(all_salaries):>10,.0f}")
print(f"  Salary range:    ₹{max(all_salaries) - min(all_salaries):>10,.0f}")

print("\n" + "="*70)
print("\nNOTE: We'll replace these loops in Project 10 using list comprehensions.")
print("Comprehensions are more Pythonic and often faster for filtering/transforming.")
print("="*70 + "\n")

# ── KEY POINTS ──────────────────────────────────────────────────────
# 1. List of dicts is a simple but powerful data structure for storing
#    records (much like database rows)
# 2. Functions make the code reusable (lookup, filter, compute)
# 3. for loops are fundamental for iteration and filtering
# 4. sorted() with a key function (lambda) is powerful for ranking
# 5. enumerate() gives us both the index and value in one loop
# 6. In real systems, you'd use ORM frameworks like SQLAlchemy
#    to query a real database instead of looping in Python
# ────────────────────────────────────────────────────────────────────
