# ─────────────────────────────────────────────────────────────────
# Project 08 — HR — Payroll CSV to JSON
# Concepts  : csv, json, pathlib, with statement, exception handling
# Difficulty: Intermediate
# ─────────────────────────────────────────────────────────────────

import csv
import json
from pathlib import Path

# ── Section 1: Create Sample Data ──────────────────────────────────
print("\n" + "="*70)
print("PAYROLL SYSTEM — CSV TO JSON PROCESSING")
print("="*70)

# Create data directory
data_dir = Path("data")
data_dir.mkdir(exist_ok=True)

# Write sample employees.csv
employees_data = [
    ["emp_id", "name", "salary"],
    [101, "Aditya Kumar", 85000],
    [102, "Bhavna Sharma", 92000],
    [103, "Chirag Patel", 65000],
    [104, "Deepika Singh", 55000],
    [105, "Eshan Verma", 78000],
]

csv_file = data_dir / "employees.csv"
with open(csv_file, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(employees_data)

print(f"✓ Created {csv_file}")

# ── Section 2: Deduction Functions ────────────────────────────────
def calculate_pf(salary):
    """PF = 12% of salary"""
    return salary * 0.12

def calculate_tds(salary):
    """Tax slab-based TDS"""
    if salary <= 50000:
        return 0
    elif salary <= 100000:
        return (salary - 50000) * 0.10
    else:
        return 5000 + (salary - 100000) * 0.20

# ── Section 3: Process Payroll ────────────────────────────────────
payslips = []

with open(csv_file, "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        emp_id = int(row["emp_id"])
        name = row["name"]
        salary = float(row["salary"])

        pf = calculate_pf(salary)
        tds = calculate_tds(salary)
        net_salary = salary - pf - tds

        payslips.append({
            "emp_id": emp_id,
            "name": name,
            "gross_salary": salary,
            "pf": pf,
            "tds": tds,
            "net_salary": net_salary,
        })

# ── Section 4: Write to CSV (Payslips) ────────────────────────────
payslips_csv = data_dir / "payslips.csv"
with open(payslips_csv, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=payslips[0].keys())
    writer.writeheader()
    writer.writerows(payslips)

print(f"✓ Generated {payslips_csv}")

# ── Section 5: Write to JSON (Payroll Summary) ────────────────────
payroll_summary = {
    "total_employees": len(payslips),
    "total_gross": sum(p["gross_salary"] for p in payslips),
    "total_pf": sum(p["pf"] for p in payslips),
    "total_tds": sum(p["tds"] for p in payslips),
    "total_net": sum(p["net_salary"] for p in payslips),
    "payslips": payslips,
}

payroll_json = data_dir / "payroll_summary.json"
with open(payroll_json, "w") as f:
    json.dump(payroll_summary, f, indent=2)

print(f"✓ Generated {payroll_json}")

# ── Section 6: Display Summary ────────────────────────────────────
print("\nPAYROLL SUMMARY:")
print("─" * 70)
print(f"{'Employee':<20} {'Gross':>12} {'PF':>12} {'TDS':>12} {'Net':>12}")
print("─" * 70)

for slip in payslips:
    print(f"{slip['name']:<20} ₹{slip['gross_salary']:>11,.0f} ₹{slip['pf']:>11,.0f} ₹{slip['tds']:>11,.0f} ₹{slip['net_salary']:>11,.0f}")

print("─" * 70)
print(f"{'TOTAL':<20} ₹{payroll_summary['total_gross']:>11,.0f} ₹{payroll_summary['total_pf']:>11,.0f} ₹{payroll_summary['total_tds']:>11,.0f} ₹{payroll_summary['total_net']:>11,.0f}")

print("\n" + "="*70)
print("In production, you'd integrate with accounting software (Tally, SAP).")
print("="*70 + "\n")
