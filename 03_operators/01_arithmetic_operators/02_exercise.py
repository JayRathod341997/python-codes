# ============================================================
# Exercise: Arithmetic Operators
# ============================================================
# Solve each problem using arithmetic operators.
# Expected output is shown as a comment after each print().
# ============================================================

# ----------------------------------------------------------
# Q1. You have 250 candies to distribute equally among
#     12 children. How many candies does each child get,
#     and how many are left over?
# ----------------------------------------------------------

candies = 250
children = 12

each_gets = None        # TODO: use floor division
leftover  = None        # TODO: use modulus

print(each_gets)        # 20
print(leftover)         # 10


# ----------------------------------------------------------
# Q2. A rectangle has width = 7.5 and height = 4.
#     Calculate its area and perimeter.
# ----------------------------------------------------------

width  = 7.5
height = 4

area      = None        # TODO
perimeter = None        # TODO

print(area)             # 30.0
print(perimeter)        # 23.0


# ----------------------------------------------------------
# Q3. A pizza is cut into 8 slices. 3 friends each eat
#     3 slices. How many slices remain?
# ----------------------------------------------------------

slices  = 8
friends = 3
eaten_each = 3

remaining = None        # TODO

print(remaining)        # -1  (they over-ate — that's okay, let Python show it!)


# ----------------------------------------------------------
# Q4. What is 2 raised to the power of 10?
# ----------------------------------------------------------

result = None           # TODO: use **

print(result)           # 1024


# ----------------------------------------------------------
# Q5. A car travels 345 km on a full tank of 45 litres.
#     Calculate mileage (km per litre) rounded to 2 decimal
#     places.
# ----------------------------------------------------------

distance = 345
fuel     = 45

mileage = None          # TODO: regular division, then round()

print(mileage)          # 7.67


# ----------------------------------------------------------
# Q6. Convert 275 minutes into hours and remaining minutes.
# ----------------------------------------------------------

total_minutes = 275

hours   = None          # TODO: floor division by 60
minutes = None          # TODO: modulus 60

print(hours)            # 4
print(minutes)          # 35


# ----------------------------------------------------------
# BONUS: Without running the code, predict the output, then
#        verify by running.
# ----------------------------------------------------------

print(-9 // 2)          # ?
print(-9 % 2)           # ?
print(9 % -2)           # ?
