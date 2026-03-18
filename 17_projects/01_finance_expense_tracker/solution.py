# ─────────────────────────────────────────────────────────────────
# Project 01 — Finance — Month-End Budget Report
# Concepts  : variables, operators, if/elif/else, f-string formatting
# Difficulty: Beginner
# ─────────────────────────────────────────────────────────────────

# ── Section 1: Define Income and Expenses ──────────────────────────
# Each variable holds a specific amount in Indian Rupees (₹)
monthly_income = 75000          # Riya's fixed monthly salary
rent = 25000                    # Largest expense: housing
groceries = 8000               # Food and household essentials
transportation = 3000          # Daily commute costs
entertainment = 5000           # Movies, outings, hobbies
utilities = 2000               # Electricity, water, internet

print("\n" + "="*60)
print("RIYA'S MONTHLY BUDGET REPORT")
print("="*60)
print(f"\nMonthly Income: ₹{monthly_income:>10,.0f}")
print("\nExpenses by Category:")
print(f"  Rent           : ₹{rent:>10,.0f}")
print(f"  Groceries      : ₹{groceries:>10,.0f}")
print(f"  Transportation : ₹{transportation:>10,.0f}")
print(f"  Entertainment  : ₹{entertainment:>10,.0f}")
print(f"  Utilities      : ₹{utilities:>10,.0f}")

# ── Section 2: Compute Total Expenses ──────────────────────────────
# We add all expenses using the + operator
# Note: In production, you'd typically use pandas to read expenses from a CSV
total_expenses = rent + groceries + transportation + entertainment + utilities
print(f"\nTotal Expenses : ₹{total_expenses:>10,.0f}")

# ── Section 3: Compute Category Percentages ────────────────────────
# Percentage = (expense / total_income) * 100
# We use f-string with .1f to show one decimal place
rent_pct = (rent / monthly_income) * 100
groceries_pct = (groceries / monthly_income) * 100
transportation_pct = (transportation / monthly_income) * 100
entertainment_pct = (entertainment / monthly_income) * 100
utilities_pct = (utilities / monthly_income) * 100

print(f"\nPercentage of Income Spent:")
print(f"  Rent           : {rent_pct:>6.1f}%")
print(f"  Groceries      : {groceries_pct:>6.1f}%")
print(f"  Transportation : {transportation_pct:>6.1f}%")
print(f"  Entertainment  : {entertainment_pct:>6.1f}%")
print(f"  Utilities      : {utilities_pct:>6.1f}%")

# ── Section 4: Compute Net Savings and Health Classification ──────
# Savings = Income - Expenses
# We use this to determine if Riya is in good financial health
net_savings = monthly_income - total_expenses
savings_percentage = (net_savings / monthly_income) * 100

print(f"\n" + "─"*60)
print(f"Net Savings    : ₹{net_savings:>10,.0f}")
print(f"Savings %      : {savings_percentage:>6.1f}%")

# ── CONCEPT: if/elif/else Control Flow ─────────────────────────────
# We use conditional statements to classify financial health
# The conditions are evaluated top-to-bottom; the FIRST true condition wins
# This is a common pattern: define categories by thresholds
if savings_percentage > 30:
    health_status = "EXCELLENT"
    advice = "You're saving well! Consider investing excess savings."
elif savings_percentage >= 15:
    health_status = "GOOD"
    advice = "You're on track. Monitor entertainment expenses."
elif savings_percentage >= 5:
    health_status = "WARNING"
    advice = "Savings are thin. Try reducing discretionary spending."
else:
    health_status = "CRITICAL"
    advice = "You're spending more than you earn! Cut expenses urgently."

print(f"\nFinancial Health: {health_status}")
print(f"Advice: {advice}")
print("="*60 + "\n")

# ── Section 5: Identify Largest Expense Category ────────────────────
# We compute which category uses the most money
# In real applications, you might use max() with a dictionary,
# but here we keep it simple for clarity
expenses_list = [
    ("Rent", rent),
    ("Groceries", groceries),
    ("Transportation", transportation),
    ("Entertainment", entertainment),
    ("Utilities", utilities)
]

# Find the category with the highest expense (simple max by second element)
largest_category, largest_amount = max(expenses_list, key=lambda x: x[1])
largest_pct = (largest_amount / monthly_income) * 100

print(f"Largest Expense: {largest_category} (₹{largest_amount:,.0f}, {largest_pct:.1f}% of income)")

# ── Section 6: Surplus/Deficit Summary ──────────────────────────────
print(f"\nSummary:")
if net_savings >= 0:
    print(f"✓ SURPLUS: Riya saved ₹{net_savings:,.0f} this month!")
else:
    print(f"✗ DEFICIT: Riya overspent by ₹{abs(net_savings):,.0f} this month!")

print("\n" + "="*60 + "\n")

# ── KEY POINTS ──────────────────────────────────────────────────────
# 1. Variables store data values that we use repeatedly throughout the code
# 2. Arithmetic operators (+, -, *, /) combine and transform data
# 3. Comparison operators (>, <, >=, ==) test relationships
# 4. if/elif/else chains categorize situations into distinct buckets
# 5. f-strings format output with alignment (:>10), thousands separator (,), and decimals (.1f)
# 6. The same calculation can be reused (savings_percentage is computed, then used to classify health)
# ────────────────────────────────────────────────────────────────────
