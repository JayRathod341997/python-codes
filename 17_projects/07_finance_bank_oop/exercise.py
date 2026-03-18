# ───────────────────────────────────────────────────────────────
# Exercises — Project 07: Banking with Inheritance
# ───────────────────────────────────────────────────────────────

# ── Exercise 1: Create Custom Account and Demonstrate Polymorphism ─
# Task: Create a new account type "StudentAccount" that inherits from
#       BankAccount. Override withdraw() to allow free withdrawals up to
#       ₹10,000/month, then charge 1% fee on excess.
#
# Requirements:
#   - Define StudentAccount class with __init__
#   - Override withdraw() with monthly limit logic
#   - Create instance, perform deposits/withdrawals
#   - Show that polymorphism works (call same method on different types)
#
# Hint: Track monthly withdrawal total. Charge fee if exceeded.

# --- your code here ---




# ── Exercise 2: Interest Comparison ────────────────────────────────
# Task: Create 3 accounts with same initial balance (₹10,000):
#       - Savings Account (4% interest)
#       - FD (7% interest for 1 year)
#       - Current Account (0% interest)
#
#       Compare interest earned in 1 year.
#
# Requirements:
#   - Create all three accounts
#   - Call calculate_interest() on each
#   - Display interest earned and final balance
#   - Show which account earned most interest
#
# Hint: Use a loop to calculate interest for each account.

# --- your code here ---




# ── Exercise 3: Transaction Log and Balance Verification ────────────
# Task: Create an account, perform 5 transactions (deposits/withdrawals),
#       track all transactions, and verify final balance.
#
# Requirements:
#   - Create SavingsAccount with ₹5,000
#   - Perform: deposit 2000, withdraw 1000, deposit 500, withdraw 800, withdraw 500
#   - Print transaction log with running balance
#   - Verify final balance = 5000 + 2000 - 1000 + 500 - 800 - 500
#
# Hint: Manually track transactions in a list of (type, amount, balance) tuples.

# --- your code here ---




# ───────────────────────────────────────────────────────────────
# Expected outputs (for self-check):
#
# Ex1: StudentAccount with monthly limit
#      Multiple accounts listed with polymorphic behavior shown
#
# Ex2: Interest comparison for 3 accounts
#      FD: ₹11,700 (interest ₹1,700)
#      Savings: ₹10,400 (interest ₹400)
#      Current: ₹10,000 - 500 = ₹9,500 (fee deducted, no interest)
#
# Ex3: Transaction log with 5 transactions
#      Final balance: ₹4,200
#      Verification: 5000 + 2000 - 1000 + 500 - 800 - 500 = 4200 ✓
# ───────────────────────────────────────────────────────────────
