# ─────────────────────────────────────────────
# Exercises — while Loop
# ─────────────────────────────────────────────

# ── Exercise 1: Bank Loan EMI Tracker ─────────
# Real-life: Loan amortization
# Loan amount: ₹100,000
# Monthly EMI: ₹5,000
# Monthly interest rate: 1% (applied on remaining balance BEFORE EMI)
# Print each month: month number, interest charged, EMI paid, remaining balance
# Stop when balance reaches 0 or below.

balance  = 100_000
emi      = 5_000
rate     = 0.01       # 1% per month
month    = 0

# --- your while loop here ---
# Expected format per line:
# Month 1: Interest=₹1000.00, EMI=₹5000, Balance=₹96000.00


# ── Exercise 2: Number Guessing Game ──────────
# Real-life: Classic game logic
# secret = 42
# Simulate guesses from a list: [10, 55, 42]
# Each guess:
#   - Too low  → "Too low! Try higher."
#   - Too high → "Too high! Try lower."
#   - Correct  → "Correct! You guessed it in {attempts} attempt(s)."

secret  = 42
guesses = [10, 55, 42]
idx     = 0

# --- your while loop here ---


# ── Exercise 3: Stock Price Monitor ───────────
# Real-life: Algorithmic trading trigger
# prices = [980, 995, 1010, 1025, 1048, 1052, 1060]
# Watch price until it crosses ₹1050 (target) or falls below ₹970 (stop-loss)
# Print each price and the final action taken.

prices     = [980, 995, 1010, 1025, 1048, 1052, 1060]
target     = 1050
stop_loss  = 970
idx        = 0

# --- your while loop here ---
# Expected last line: "Target hit at ₹1052 — SELL order placed!"


# ── Exercise 4: String Reversal (Manual) ──────
# Real-life: Understanding how reversal algorithms work
# Reverse the string "python" character by character using a while loop.
# Do NOT use slicing [::-1] or reversed().

word    = "python"
result  = ""
idx     = len(word) - 1

# --- your while loop here ---
# print(result)   # → "nohtyp"


# ── Exercise 5: Digital Root Calculator ───────
# Real-life: Used in numerology apps and checksum validation
# Keep summing the digits of a number until you get a single digit.
# Example: 9875 → 9+8+7+5=29 → 2+9=11 → 1+1=2  → digital root = 2

number = 9875

# --- your while loop here ---
# print(f"Digital root of {9875} = {result}")


# ─────────────────────────────────────────────
# Expected outputs (final lines):
# Ex1: Loan fully paid in N months (varies by implementation)
# Ex2: Correct! You guessed it in 3 attempt(s).
# Ex3: Target hit at ₹1052 — SELL order placed!
# Ex4: nohtyp
# Ex5: Digital root of 9875 = 2
# ─────────────────────────────────────────────
