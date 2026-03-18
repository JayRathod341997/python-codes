# Solutions — Project 08: HR Payroll Files

import csv
import json
from pathlib import Path

def calculate_pf(salary):
    return salary * 0.12

def calculate_tds(salary):
    if salary <= 50000:
        return 0
    elif salary <= 100000:
        return (salary - 50000) * 0.10
    else:
        return 5000 + (salary - 100000) * 0.20

print("\n" + "="*70)
print("EXERCISE 1 SOLUTION: Payslips with Bonus")
print("="*70 + "\n")

data_dir = Path("data")
employees_csv = data_dir / "employees.csv"

bonus = 5000
payslips_bonus = []

with open(employees_csv, "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        emp_id = int(row["emp_id"])
        name = row["name"]
        salary = float(row["salary"]) + bonus
        pf = calculate_pf(salary)
        tds = calculate_tds(salary)
        net = salary - pf - tds
        payslips_bonus.append({"emp_id": emp_id, "name": name, "gross": salary, "pf": pf, "tds": tds, "net": net})

with open(data_dir / "bonus_payslips.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=payslips_bonus[0].keys())
    writer.writeheader()
    writer.writerows(payslips_bonus)

print("Payslips with ₹5000 bonus:")
for slip in payslips_bonus:
    print(f"  {slip['name']}: ₹{slip['gross']:.0f} → Net ₹{slip['net']:.0f}")

print("\n" + "="*70)
print("EXERCISE 2 SOLUTION: High Earners Export to JSON")
print("="*70 + "\n")

high_earners = []
with open(employees_csv, "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if float(row["salary"]) > 80000:
            high_earners.append({"emp_id": int(row["emp_id"]), "name": row["name"], "salary": float(row["salary"])})

with open(data_dir / "high_earners.json", "w") as f:
    json.dump({"count": len(high_earners), "employees": high_earners}, f, indent=2)

print(f"Found {len(high_earners)} high earners (>₹80,000):")
for emp in high_earners:
    print(f"  {emp['name']}: ₹{emp['salary']:,.0f}")

print("\n" + "="*70 + "\n")
