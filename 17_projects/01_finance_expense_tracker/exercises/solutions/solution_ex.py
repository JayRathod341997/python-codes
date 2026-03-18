# ───────────────────────────────────────────────────────────────
# Solutions — Project 01: Month-End Budget Report
# ───────────────────────────────────────────────────────────────

print("\n" + "="*70)
print("EXERCISE 1 SOLUTION: Arun's Budget Analysis")
print("="*70 + "\n")

# ── Exercise 1 Solution ────────────────────────────────────────────
monthly_income_arun = 120000
rent_arun = 50000
groceries_arun = 10000
transportation_arun = 5000
entertainment_arun = 8000
utilities_arun = 3000

total_expenses_arun = (rent_arun + groceries_arun + transportation_arun +
                       entertainment_arun + utilities_arun)
net_savings_arun = monthly_income_arun - total_expenses_arun
savings_percentage_arun = (net_savings_arun / monthly_income_arun) * 100

print(f"Monthly Income: ₹{monthly_income_arun:>10,.0f}")
print(f"Total Expenses: ₹{total_expenses_arun:>10,.0f}")
print(f"Net Savings   : ₹{net_savings_arun:>10,.0f}")
print(f"Savings %     : {savings_percentage_arun:>6.1f}%")

if savings_percentage_arun > 30:
    health_arun = "EXCELLENT"
elif savings_percentage_arun >= 15:
    health_arun = "GOOD"
elif savings_percentage_arun >= 5:
    health_arun = "WARNING"
else:
    health_arun = "CRITICAL"

print(f"Financial Health: {health_arun}")
print(f"\nInterpretation: Arun earns ₹1,20,000 and saves {savings_percentage_arun:.1f}% —")
print(f"more than Riya's {(27000/75000)*100:.1f}%. He's in {health_arun} financial health!")

print("\n" + "="*70)
print("EXERCISE 2 SOLUTION: Riya's Budget with Bonus")
print("="*70 + "\n")

# ── Exercise 2 Solution ────────────────────────────────────────────
# Original Riya data from solution.py
monthly_income = 75000
rent = 25000
groceries = 8000
transportation = 3000
entertainment = 5000
utilities = 2000
total_expenses = rent + groceries + transportation + entertainment + utilities

# Original savings
net_savings_orig = monthly_income - total_expenses
savings_percentage_orig = (net_savings_orig / monthly_income) * 100

# Classify original
if savings_percentage_orig > 30:
    health_orig = "EXCELLENT"
elif savings_percentage_orig >= 15:
    health_orig = "GOOD"
elif savings_percentage_orig >= 5:
    health_orig = "WARNING"
else:
    health_orig = "CRITICAL"

# With bonus
bonus_amount = 30000
total_income_with_bonus = monthly_income + bonus_amount
net_savings_with_bonus = total_income_with_bonus - total_expenses
savings_percentage_with_bonus = (net_savings_with_bonus / total_income_with_bonus) * 100

# Classify with bonus
if savings_percentage_with_bonus > 30:
    health_bonus = "EXCELLENT"
elif savings_percentage_with_bonus >= 15:
    health_bonus = "GOOD"
elif savings_percentage_with_bonus >= 5:
    health_bonus = "WARNING"
else:
    health_bonus = "CRITICAL"

print(f"WITHOUT BONUS:")
print(f"  Income        : ₹{monthly_income:>10,.0f}")
print(f"  Expenses      : ₹{total_expenses:>10,.0f}")
print(f"  Net Savings   : ₹{net_savings_orig:>10,.0f}")
print(f"  Savings %     : {savings_percentage_orig:>6.1f}%")
print(f"  Health Status : {health_orig}")

print(f"\nWITH ₹{bonus_amount:,.0f} BONUS:")
print(f"  Income        : ₹{total_income_with_bonus:>10,.0f}")
print(f"  Expenses      : ₹{total_expenses:>10,.0f}")
print(f"  Net Savings   : ₹{net_savings_with_bonus:>10,.0f}")
print(f"  Savings %     : {savings_percentage_with_bonus:>6.1f}%")
print(f"  Health Status : {health_bonus}")

print(f"\nCHANGE DUE TO BONUS:")
print(f"  Savings increased by: ₹{net_savings_with_bonus - net_savings_orig:,.0f}")
print(f"  Health improved from {health_orig} to {health_bonus}")
if health_bonus != health_orig:
    print(f"  ✓ The bonus moved her to a better financial category!")
else:
    print(f"  ✓ She remained in {health_orig} category.")

print("\n" + "="*70)
print("EXERCISE 3 SOLUTION: Savings Goal Constraint")
print("="*70 + "\n")

# ── Exercise 3 Solution ────────────────────────────────────────────
# Riya wants to save 25% of her ₹75,000 income = ₹18,750

required_savings = 0.25 * monthly_income  # ₹18,750
fixed_expenses = rent + utilities         # ₹27,000
current_variable = groceries + transportation + entertainment  # ₹16,000

# Available for variable expenses = Income - Fixed - Required_Savings
allowable_variable = monthly_income - fixed_expenses - required_savings

# How much can she spend on entertainment within the allowable variable?
# Assuming groceries and transportation stay same, what's left for entertainment?
fixed_variable = groceries + transportation  # ₹11,000
allowable_entertainment = allowable_variable - fixed_variable

# How much reduction is needed?
entertainment_reduction = entertainment - allowable_entertainment

print(f"Goal: Save {0.25*100:.0f}% of income each month")
print(f"\nIncome breakdown:")
print(f"  Monthly Income     : ₹{monthly_income:>10,.0f}")
print(f"  Fixed Expenses     : ₹{fixed_expenses:>10,.0f}  (Rent + Utilities)")
print(f"  Required Savings   : ₹{required_savings:>10,.0f}  ({required_savings/monthly_income*100:.0f}% goal)")
print(f"  Variable Budget    : ₹{allowable_variable:>10,.0f}  (remaining)")

print(f"\nVariable expenses breakdown:")
print(f"  Groceries+Transport: ₹{fixed_variable:>10,.0f}  (mostly fixed)")
print(f"  Entertainment      : ₹{entertainment:>10,.0f}  (current)")
print(f"  Max Entertainment  : ₹{max(0, allowable_entertainment):>10,.0f}  (to meet goal)")

if entertainment_reduction > 0:
    print(f"\nShe needs to cut: ₹{entertainment_reduction:,.0f} from entertainment")
else:
    print(f"\nGood news! She has ₹{abs(entertainment_reduction):,.0f} extra cushion")
    print(f"and can achieve her 25% savings goal WITHOUT cutting entertainment!")

# Summary table
print(f"\nSUMMARY TABLE:")
print(f"  Current situation    : {health_orig} ({savings_percentage_orig:.1f}% savings)")
print(f"  If 25% savings goal  : Entertainment budget is ₹{max(0, allowable_entertainment):,.0f}")
print(f"  vs current ₹{entertainment:,.0f}, change needed: ₹{-entertainment_reduction:,.0f}")

print("\n" + "="*70 + "\n")
