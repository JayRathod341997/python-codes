# ============================================================
# Exercise: Bitwise Operators
# ============================================================

# ----------------------------------------------------------
# Q1. Given a = 12 (1100) and b = 10 (1010), compute:
#     a) a & b
#     b) a | b
#     c) a ^ b
#     d) ~a
#     Verify your mental calculation by printing bin() of each.
# ----------------------------------------------------------

a = 12      # 1100
b = 10      # 1010

result_and = None   # TODO
result_or  = None   # TODO
result_xor = None   # TODO
result_not = None   # TODO

print(result_and, bin(result_and))   # 8  0b1000
print(result_or,  bin(result_or))    # 14 0b1110
print(result_xor, bin(result_xor))   # 6  0b110
print(result_not)                    # -13


# ----------------------------------------------------------
# Q2. Use left/right shift to:
#     a) Multiply 7 by 4 using <<
#     b) Divide 96 by 8 using >>
# ----------------------------------------------------------

n1 = 7
n2 = 96

mul = None          # TODO: shift n1 left by 2
div = None          # TODO: shift n2 right by 3

print(mul)          # 28
print(div)          # 12


# ----------------------------------------------------------
# Q3. Use bitwise AND to check if the following numbers are
#     odd or even. Print "odd" or "even".
# ----------------------------------------------------------

numbers = [4, 7, 12, 15, 0, 99]

for num in numbers:
    pass            # TODO: use num & 1 to determine odd/even

# Expected output:
# 4 even
# 7 odd
# 12 even
# 15 odd
# 0 even
# 99 odd


# ----------------------------------------------------------
# Q4. Bitmask / permissions exercise.
#
#     Flags defined below:
#       NOTIFY  = bit 0  (0001)
#       PREMIUM = bit 1  (0010)
#       ADMIN   = bit 2  (0100)
#       BANNED  = bit 3  (1000)
#
#     a) Create user1 with NOTIFY and PREMIUM permissions.
#     b) Create user2 with ADMIN permission only.
#     c) Check if user1 is ADMIN.
#     d) Grant user2 NOTIFY.
#     e) Ban user1 (add BANNED flag).
#     f) Check if user1 is BANNED.
# ----------------------------------------------------------

NOTIFY  = 0b0001
PREMIUM = 0b0010
ADMIN   = 0b0100
BANNED  = 0b1000

user1 = None        # TODO (a)
user2 = None        # TODO (b)

is_admin  = None    # TODO (c): check user1 & ADMIN
print(bool(is_admin))       # False

# TODO (d): grant user2 NOTIFY using |=

# TODO (e): ban user1 using |=

is_banned = None    # TODO (f)
print(bool(is_banned))      # True


# ----------------------------------------------------------
# BONUS: XOR swap — swap x and y WITHOUT using a temp var.
# ----------------------------------------------------------

x = 42
y = 17

# TODO: swap using XOR (3 lines)

print(x)    # 17
print(y)    # 42
