# ───────────────────────────────────────────────────────────────
# Exercises — Project 01: Month-End Budget Report
# ───────────────────────────────────────────────────────────────

# ── Exercise 1: Compute Budget for a Different Person ────────────
# Real-life: Arun is a software engineer earning ₹1,20,000/month
#
# Create a similar budget analysis for Arun with these expenses:
#   - Rent: ₹50,000
#   - Groceries: ₹10,000
#   - Transportation: ₹5,000
#   - Entertainment: ₹8,000
#   - Utilities: ₹3,000
#
# Requirements:
#   - Compute total expenses
#   - Compute percentage of income for each category
#   - Classify financial health (Excellent/Good/Warning/Critical)
#   - Print a formatted report (like the solution)
#
# Hint: Copy the structure from solution.py, replace variable values,
#       then adjust the if/elif/else thresholds if needed

# --- your code here ---




# ── Exercise 2: Add a Bonus and Recompute ────────────────────────
# Real-life: Riya received a year-end bonus of ₹30,000
#
# Using the original values from solution.py (₹75,000 base income):
#   - Define a bonus_amount variable (₹30,000)
#   - Recompute total_income = monthly_income + bonus_amount
#   - Recompute net_savings with the new total_income
#   - Recompute savings_percentage with new values
#   - Classify financial health based on new savings_percentage
#
# Requirements:
#   - Print the original and new financial health status side-by-side
#   - Show how much the health classification changed due to the bonus
#
# Hint: After bonus, expenses stay the same, but income is higher.
#       This might move her from "Good" to "Excellent" — see if it does!

# --- your code here ---




# ── Exercise 3: Savings Goal Constraint ────────────────────────────
# Real-life: Riya wants to save 25% of her income each month (₹18,750)
#
# Her fixed expenses (Rent + Utilities) are: ₹27,000
# Variable expenses (Groceries + Transportation + Entertainment) are flexible.
#
# Question: By how much must she reduce "Entertainment" spending to hit
#           her 25% savings goal? (Assume other variable expenses stay same)
#
# Requirements:
#   - Define required_savings = 0.25 * monthly_income (₹18,750)
#   - Compute current_fixed = rent + utilities
#   - Compute current_variable = groceries + transportation + entertainment
#   - Compute allowable_variable = monthly_income - required_savings - fixed_expenses
#   - Compute entertainment_reduction = current_entertainment - allowable_entertainment
#   - Print how much less she needs to spend on entertainment
#
# Hint: Think about it as: Income = Fixed + Variable + Savings
#       So: Variable = Income - Fixed - Savings
#       Then: Entertainment_reduction = Current_Entertainment - (allowable_variable)

# --- your code here ---




# ───────────────────────────────────────────────────────────────
# Expected outputs (for self-check):
#
# Ex1: Arun's financial health classification, with his income/expenses
#      Total expenses: ₹76,000, Net savings: ₹44,000
#      Savings percentage: 36.7% → "EXCELLENT"
#
# Ex2: Riya's health before bonus (e.g., "GOOD") vs after bonus
#      With ₹30k bonus, total income becomes ₹105,000
#      Savings goes from ₹27,000 (36%) to ₹57,000 (54.3%)
#      Classification moves from "GOOD" to "EXCELLENT"
#
# Ex3: Entertainment reduction needed for 25% savings goal
#      Allowable variable expenses: ₹36,250 (= 75k - 27k - 18.75k)
#      Current variable: ₹16,000
#      She actually has ₹20,250 extra — no reduction needed!
#      If goal was 30% savings, she'd need to cut ₹4,000 from entertainment
# ───────────────────────────────────────────────────────────────
