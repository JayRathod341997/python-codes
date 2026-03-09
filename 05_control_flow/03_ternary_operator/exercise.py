# ─────────────────────────────────────────────
# Exercises — Ternary Operator
# ─────────────────────────────────────────────

# Rules: Solve EACH exercise using a single ternary expression.
# No if/else blocks — just one line per answer.

# ── Exercise 1: Login Status ──────────────────
# Real-life: Website header
# If is_logged_in → show "Welcome back, {username}!"
# Else            → show "Please log in."

is_logged_in = True
username     = "Jay"

message = ...       # your ternary here
print(message)


# ── Exercise 2: Seat Availability ─────────────
# Real-life: Bus/Train booking
# available_seats > 0 → "Book Now"
# Else               → "Sold Out"

available_seats = 0

seat_status = ...   # your ternary here
print(seat_status)


# ── Exercise 3: Temperature Advisory ─────────
# Real-life: Weather app notification
# temp >= 40 → "Extreme heat! Stay indoors."
# Else       → "Weather is manageable."

temp = 42

advisory = ...      # your ternary here
print(advisory)


# ── Exercise 4: Subscription Plan Label ──────
# Real-life: SaaS pricing page
# is_annual → "Annual plan — save 20%"
# Else      → "Monthly plan"

is_annual = False

plan_label = ...    # your ternary here
print(plan_label)


# ── Exercise 5: Upload Size Validator ─────────
# Real-life: File upload system (inside an f-string)
# file_size_mb > 10 → include "❌ Too large" in message
# Else              → include "✓ OK" in message
# Full message: "File size: {file_size_mb}MB — ✓ OK"  or "...— ❌ Too large"

file_size_mb = 7.5

print(...)          # your f-string with embedded ternary


# ── Exercise 6: Grade String ──────────────────
# Real-life: School report card
# Convert numeric score to letter using CHAINED ternary:
# >= 90 → "A"
# >= 75 → "B"
# >= 60 → "C"
# >= 40 → "D"
# else  → "F"

score = 82

grade = ...         # your chained ternary here
print(f"Score {score} → Grade {grade}")


# ─────────────────────────────────────────────
# Expected outputs:
# Ex1: Welcome back, Jay!
# Ex2: Sold Out
# Ex3: Extreme heat! Stay indoors.
# Ex4: Monthly plan
# Ex5: File size: 7.5MB — ✓ OK
# Ex6: Score 82 → Grade B
# ─────────────────────────────────────────────
