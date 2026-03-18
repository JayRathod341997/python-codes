# Project 04 — HR Employee Directory and Salary Analysis

## The Real-Life Problem

Raj works in HR at TechCorp, a 200-person tech startup. HR needs a tool to:
- Look up employee details by ID or name
- Filter employees by department
- Calculate average salary per department
- Identify top earners
- Generate reports for payroll and planning

Currently, this is all done in Excel, which is slow and error-prone. With Python, Raj can instantly query the employee database, slice it by department, and generate insights.

## Domain Context

**Industry**: Human Resources / Payroll
**Role**: HR Manager / Payroll Analyst
**Tools in the real world**: ATS systems (Workday, BambooHR, SAP), HR databases
**Why Python is used here**: HR systems use Python/SQL backends to process employee data, compute payroll, and generate compliance reports.

## The Python Solution Approach

We store employees as a list of dictionaries (emp_id, name, dept, salary). We create functions to:
- Look up an employee by ID or name using a for loop with early exit
- Filter employees by department using a for loop collecting matches
- Compute average salary using sum() and division
- Find top earners using enumerate() and comparison logic

This is procedural with loops and functions. (In Project 10, we'll refactor with comprehensions.)

## Python Concepts You Will Practice

| Concept | Where It Appears |
|---|---|
| List of dictionaries | Section 1: Employee records |
| Functions | Sections 2–5: Modular lookup and analysis |
| for loops | Sections 2–5: Iterating through employees |
| Conditional logic (if/elif) | Sections 2–5: Filtering and comparisons |
| sorted() function | Section 5: Sorting employees by salary |
| enumerate() | Section 5: Pairing index with employee |
| max/min functions | Sections 4–5: Finding highest/lowest salary |
| String methods (lower, in) | Section 2: Case-insensitive search |
| f-string formatting | Section 6: Formatted reports |

## How to Use This Project

1. Read this file to understand the employee directory structure
2. Run `solution.py` and observe the queries and reports
3. Notice how functions encapsulate logic for reusability
4. Pay attention to the for loops—how do they filter or find specific employees?
5. Attempt exercises without looking at the solution
6. Compare your approach with `exercises/solutions/solution_ex.py`

## Extension Ideas

- **Salary ranges**: Filter employees earning between ₹X and ₹Y
- **Tenure calculation**: Add hire_date and compute years of service
- **Department statistics**: Show headcount, avg salary, salary range per department
- **Bonus calculation**: Add bonus percentage and compute total compensation

## Real-World Equivalent

This project mimics:
- **HRIS systems** (Workday, PeopleSoft): employee lookups and reports
- **Payroll software** (SAP HR, Tally): salary calculations by department
- **LinkedIn-style employee directories**: filtering and sorting
- **Analytics dashboards**: computing averages, finding outliers
