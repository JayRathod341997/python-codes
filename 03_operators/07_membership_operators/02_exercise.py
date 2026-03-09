# ============================================================
# Exercise: Membership Operators (in, not in)
# ============================================================

# ----------------------------------------------------------
# Q1. Check if each item is present in the shopping cart.
# ----------------------------------------------------------

cart = ["milk", "bread", "eggs", "butter"]

# TODO: check if "eggs" is in cart
# TODO: check if "cheese" is not in cart

print(None)         # True
print(None)         # True


# ----------------------------------------------------------
# Q2. Validate that a username contains only allowed
#     characters. Allowed characters are lowercase a-z
#     and digits 0-9. Check for each character in username.
# ----------------------------------------------------------

username = "jay_123"
allowed  = "abcdefghijklmnopqrstuvwxyz0123456789"

is_valid = True
for char in username:
    pass            # TODO: if char not in allowed, set is_valid = False

print(is_valid)     # False  (underscore is not in allowed)


# ----------------------------------------------------------
# Q3. A dictionary stores student grades.
#     Before accessing a grade, check if the student exists.
# ----------------------------------------------------------

grades = {"Alice": 88, "Bob": 73, "Carol": 95}

students_to_check = ["Alice", "Dave", "Carol"]

for student in students_to_check:
    pass            # TODO: if student in grades, print their grade
                    #       else print "<student> not found"

# Expected:
# Alice: 88
# Dave not found
# Carol: 95


# ----------------------------------------------------------
# Q4. Use 'in' with range to check which numbers between
#     1 and 10 are in the Fibonacci sequence.
#     Fibonacci numbers up to 10: {1, 2, 3, 5, 8}
# ----------------------------------------------------------

fibonacci = {1, 2, 3, 5, 8}

for n in range(1, 11):
    pass            # TODO: print n and whether it is in fibonacci

# Expected:
# 1 True
# 2 True
# 3 True
# 4 False
# 5 True
# 6 False
# 7 False
# 8 True
# 9 False
# 10 False


# ----------------------------------------------------------
# Q5. Given a sentence, count how many vowels it contains.
# ----------------------------------------------------------

sentence = "The quick brown fox jumps over the lazy dog"
vowels   = "aeiouAEIOU"

vowel_count = 0
for char in sentence:
    pass            # TODO: use 'in' to check if char is a vowel

print(vowel_count)  # 11


# ----------------------------------------------------------
# BONUS: Find words in a sentence that are NOT in a
#        given dictionary (i.e., possibly misspelled).
# ----------------------------------------------------------

dictionary = {"the", "quick", "brown", "fox", "jumps", "over", "lazy", "dog"}
sentence   = "The quikc brwon fox jmps over the lazy dog"

words = sentence.lower().split()
misspelled = []

for word in words:
    pass            # TODO: add word to misspelled if not in dictionary

print(misspelled)   # ['quikc', 'brwon', 'jmps']
