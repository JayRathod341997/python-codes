# ============================================================
# Variable Reassignment
# ============================================================
# Python variables can be reassigned to a completely new value
# at any time — even a value of a different type.
# The old object may be garbage-collected if nothing else
# holds a reference to it.
# ============================================================

score = 100
print("Initial score:", score)

score = 200             # reassign to a new integer
print("After first reassign:", score)

score = score + 50      # reassign using its own value
print("After increment:", score)

score = "N/A"           # reassign to a completely different type
print("After type change:", score)

# --- Augmented assignment operators ---
x = 10
x += 5    # same as x = x + 5
print("+=:", x)

x -= 3
print("-=:", x)

x *= 2
print("*=:", x)

x //= 4   # floor division
print("//=:", x)

x **= 2   # exponentiation
print("**=:", x)

x %= 5    # modulo
print("%=:", x)
