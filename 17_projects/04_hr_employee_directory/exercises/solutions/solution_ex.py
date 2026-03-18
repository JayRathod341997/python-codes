# ───────────────────────────────────────────────────────────────
# Solutions — Project 04: HR Employee Directory
# ───────────────────────────────────────────────────────────────

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
print("EXERCISE 1 SOLUTION: High Earners (≥ ₹80,000)")
print("="*70 + "\n")

def get_employees_by_min_salary(min_salary):
    """Filter employees earning at least min_salary."""
    results = []
    for emp in employees:
        if emp["salary"] >= min_salary:
            results.append(emp)
    return results

high_earners = get_employees_by_min_salary(80000)
print(f"Employees earning ≥ ₹80,000:")
for emp in sorted(high_earners, key=lambda x: x["salary"], reverse=True):
    print(f"  {emp['name']:<20} ({emp['dept']:<12}) — ₹{emp['salary']:>10,.0f}")
print(f"\nTotal: {len(high_earners)} employees\n")

print("="*70)
print("EXERCISE 2 SOLUTION: Department Headcount")
print("="*70 + "\n")

def get_employees_by_dept(dept_name):
    results = []
    for emp in employees:
        if emp["dept"] == dept_name:
            results.append(emp)
    return results

departments = set()
for emp in employees:
    departments.add(emp["dept"])

print("Department Headcount:")
for dept in sorted(departments):
    count = len(get_employees_by_dept(dept))
    print(f"  {dept:<15} (n={count})")

print(f"\nTotal employees: {len(employees)}")
print(f"Total departments: {len(departments)}\n")

print("="*70)
print("EXERCISE 3 SOLUTION: Engineering Department Analysis")
print("="*70 + "\n")

eng_employees = get_employees_by_dept("Engineering")

if len(eng_employees) > 0:
    total = len(eng_employees)
    total_sal = sum(emp["salary"] for emp in eng_employees)
    avg_sal = total_sal / total
    salaries = [emp["salary"] for emp in eng_employees]
    min_sal = min(salaries)
    max_sal = max(salaries)

    print(f"ENGINEERING DEPARTMENT REPORT:")
    print(f"  Total Employees: {total}")
    print(f"  Average Salary:  ₹{avg_sal:>10,.0f}")
    print(f"  Min Salary:      ₹{min_sal:>10,.0f}")
    print(f"  Max Salary:      ₹{max_sal:>10,.0f}")
    print(f"  Range:           ₹{max_sal - min_sal:>10,.0f}")
    print()

    sorted_eng = sorted(eng_employees, key=lambda x: x["salary"], reverse=True)
    print(f"  Employees (sorted by salary):")
    for rank, emp in enumerate(sorted_eng, start=1):
        print(f"    {rank}. {emp['name']:<20} — ₹{emp['salary']:>10,.0f}")

print("\n" + "="*70 + "\n")
