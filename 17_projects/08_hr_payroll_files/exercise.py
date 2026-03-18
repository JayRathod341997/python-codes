# ───────────────────────────────────────────────────────────────
# Exercises — Project 08: HR Payroll Files
# ───────────────────────────────────────────────────────────────

# ── Exercise 1: Add Bonus and Recompute Payslips ────────────────────
# Task: Read employees.csv, add ₹5,000 bonus to each, recompute deductions.
#       Write updated payslips to bonus_payslips.csv.
#
# Requirements:
#   - Read employees.csv
#   - Add bonus to gross salary
#   - Recompute PF (12%) and TDS on new salary
#   - Write to bonus_payslips.csv with all fields
#
# Hint: Bonus increases salary, so TDS may increase too.

# --- your code here ---




# ── Exercise 2: Filter High Earners and Export to JSON ─────────────
# Task: Identify employees earning > ₹80,000. Export only their details
#       to high_earners.json with formatted output.
#
# Requirements:
#   - Read employees.csv
#   - Filter salary > 80000
#   - Create dict with emp_id, name, salary
#   - Export to high_earners.json using json.dump()
#
# Hint: Use conditional logic to filter, then convert to JSON.

# --- your code here ---




# ── Exercise 3: Monthly Salary Analytics Report ───────────────────
# Task: Read payslips.csv. Generate a JSON report with:
#       - Average net salary
#       - Highest and lowest earner
#       - Total deductions per employee
#
# Requirements:
#   - Read payslips.csv (from solution.py output)
#   - Compute statistics
#   - Export to analytics_report.json
#
# Hint: Use max/min with key parameter, or manual iteration.

# --- your code here ---




# ───────────────────────────────────────────────────────────────
# Expected outputs (for self-check):
#
# Ex1: Bonus payslips
#      Each employee salary +5000, deductions recalculated
#      File: bonus_payslips.csv
#
# Ex2: High earners export
#      Only employees with salary > 80000
#      File: high_earners.json
#
# Ex3: Analytics report
#      Average net salary, min/max earners, total deductions
#      File: analytics_report.json
# ───────────────────────────────────────────────────────────────
