# ============================================================
# Exercise: Assignment Operators
# ============================================================

# ----------------------------------------------------------
# Q1. Start with balance = 1000.
#     Apply the following transactions using compound operators:
#     - Deposit 500
#     - Withdraw 200
#     - Apply 10% interest (multiply by 1.10)
#     - Apply a fee of 50
#     Print the final balance.
# ----------------------------------------------------------

balance = 1000

# TODO: deposit 500 using +=
# TODO: withdraw 200 using -=
# TODO: apply 10% interest using *=
# TODO: apply fee of 50 using -=

print(balance)      # 1270.0


# ----------------------------------------------------------
# Q2. Use the accumulator pattern to sum all even numbers
#     from 1 to 20 (inclusive). Use += inside a loop.
# ----------------------------------------------------------

total = 0

for i in range(1, 21):
    pass            # TODO: add i to total if i is even

print(total)        # 110


# ----------------------------------------------------------
# Q3. Trace through the following operations manually
#     (predict each print), then verify by running.
# ----------------------------------------------------------

n = 100
n //= 3
print(n)            # ?

n %= 7
print(n)            # ?

n **= 2
print(n)            # ?


# ----------------------------------------------------------
# Q4. Use **= to compute 3 to the power of 5 starting
#     from base = 3. Build up the exponent using *=.
#     (Start with result = 1 and multiply 5 times.)
# ----------------------------------------------------------

result = 1
base = 3

# TODO: multiply result by base five times using *=
# (use a loop or write it out five times)

print(result)       # 243


# ----------------------------------------------------------
# Q5. Walrus operator — rewrite the following without using
#     a separate variable assignment before the if statement.
# ----------------------------------------------------------

# Original code:
items = ["apple", "banana", "kiwi", "strawberry", "fig"]
for word in items:
    upper = word.upper()
    if len(upper) > 5:
        print(upper)    # BANANA  STRAWBERRY

# TODO: rewrite the loop above using walrus := so that
#       upper is assigned inside the if condition.


# ----------------------------------------------------------
# BONUS: What is the difference between = and :=?
#        Write a short comment explaining.
# ----------------------------------------------------------

# Your explanation here:
# =  →
# := →
