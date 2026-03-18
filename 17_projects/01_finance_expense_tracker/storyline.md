# Project 01 — Month-End Budget Report for a Salaried Employee

## The Real-Life Problem

Riya is a fresh data analyst at a leading bank. She earns a fixed monthly salary of ₹75,000 and has various monthly expenses: rent (₹25,000), groceries (₹8,000), transportation (₹3,000), entertainment (₹5,000), and utilities (₹2,000). At the end of every month, she wants to know:

1. Did she spend less than she earned? (surplus or deficit?)
2. What percentage of her income went to each category?
3. Is her financial health "Excellent" (save >30%), "Good" (save 15-30%), "Warning" (save 5-15%), or "Critical" (save <5%)?

Currently, she manually scribbles down numbers on paper and takes 30 minutes to compute this. As a data analyst, she knows there must be a better way.

## Domain Context

**Industry**: Personal Finance / Banking
**Role**: Salaried Employee (who also happens to be a data analyst)
**Tools in the real world**: Excel, Google Sheets, YNAB (You Need A Budget), or personal finance dashboards
**Why Python is used here**: Python's simple arithmetic and string formatting make it perfect for a quick budget script. In production, companies like NerdWallet use Python backends to process millions of budget calculations.

## The Python Solution Approach

We represent Riya's financial data as individual variables (income and expenses). We compute category totals by simple addition. We calculate what percentage each category represents using division. We compare her net savings (income minus total expenses) to classify her financial health. Finally, we format everything into a readable report using f-strings with proper alignment.

The logic is purely procedural: read data → compute totals → compute percentages → classify health → print report.

## Python Concepts You Will Practice

| Concept | Where It Appears |
|---|---|
| Variables and assignment | Section 1: Setting up income and expense variables |
| Arithmetic operators (+, -, *, /) | Sections 2–3: Computing totals, percentages, net savings |
| Operator precedence | Section 3: Order of operations in percentage calculation |
| Comparison operators (>, <, ==) | Section 4: Comparing net savings against thresholds |
| if/elif/else control flow | Section 4: Classifying financial health into categories |
| f-string formatting | Sections 2, 4–5: Printing the budget report with alignment |
| Type conversion (implicit) | Section 3: Division returns float automatically |

## How to Use This Project

1. Read this file fully to understand Riya's situation
2. Open `solution.py` and run it — observe each section's output
3. Study how variables are named (descriptive names like `rent` not `r`)
4. Look at the if/elif/else logic — how does it classify financial health?
5. Attempt the exercises in `exercise.py` without looking at the solution
6. After completing exercises, compare your approach with `exercises/solutions/solution_ex.py`

## Extension Ideas

- **Bonus tracking**: Add a `bonus` variable and recompute savings percentage after bonus is included
- **Inflation adjustment**: If expenses increase by 5% next month, how does the surplus change?
- **Savings goal**: Define a goal to save 25% of income, and compute how much she needs to cut from entertainment to achieve it
- **Multi-month comparison**: Read income and expenses for three months, compute average, identify the best month

## Real-World Equivalent

This project mimics the logic behind personal finance dashboards like:
- **YNAB (You Need A Budget)**: where every transaction is categorized and reports are computed on-the-fly
- **Bank mobile apps**: many banks show a "spending breakdown by category" chart computed server-side with Python
- **Google Sheets personal finance templates**: where formulas compute category percentages and health scores
