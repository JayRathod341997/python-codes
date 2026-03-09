# ─────────────────────────────────────────────
# if / elif / else — Conditional Statements
# ─────────────────────────────────────────────

# ── Syntax ───────────────────────────────────
# if <condition>:
#     <block>
# elif <condition>:
#     <block>
# else:
#     <block>

# Python uses INDENTATION (4 spaces) to define blocks — no braces!

# ── Simple if ────────────────────────────────
temperature = 38.5          # body temperature in °C

if temperature > 37.5:
    print("Fever detected. Please see a doctor.")

# ── if / else ────────────────────────────────
age = 20

if age >= 18:
    print("Access granted — Adult content.")
else:
    print("Access denied — Minors not allowed.")

# ── if / elif / else ─────────────────────────
# Real-life: E-commerce discount tiers
cart_total = 4500           # ₹

if cart_total >= 5000:
    discount = 20           # 20% off
elif cart_total >= 3000:
    discount = 10           # 10% off
elif cart_total >= 1000:
    discount = 5            # 5% off
else:
    discount = 0            # no discount

print(f"Cart: ₹{cart_total} → Discount: {discount}%")
print(f"You pay: ₹{cart_total * (1 - discount / 100):.2f}")

# ── Conditions can be any truthy expression ──
username = ""

if username:                # empty string is falsy
    print(f"Welcome, {username}!")
else:
    print("Please enter a username.")

# ── Multiple conditions with and / or / not ──
# Real-life: Flight boarding check
has_ticket   = True
id_verified  = True
bag_checked  = False

if has_ticket and id_verified and bag_checked:
    print("You may board the flight.")
elif has_ticket and id_verified and not bag_checked:
    print("Please check your baggage first.")
else:
    print("You cannot board. Check requirements.")

# ── Comparing strings ────────────────────────
# Real-life: Login system
stored_password = "Secure@2024"
entered_password = "secure@2024"       # case mismatch

if entered_password == stored_password:
    print("Login successful.")
elif entered_password.lower() == stored_password.lower():
    print("Wrong case — passwords are case-sensitive.")
else:
    print("Incorrect password.")

# ── Checking membership with 'in' ────────────
# Real-life: Role-based access
user_role = "editor"
allowed_roles = ["admin", "editor", "moderator"]

if user_role in allowed_roles:
    print(f"Role '{user_role}' has access.")
else:
    print("Unauthorized role.")

# ── None check ───────────────────────────────
# Real-life: API response validation
api_response = None

if api_response is None:
    print("No data received from server.")
else:
    print(f"Data: {api_response}")

# ── Key points ───────────────────────────────
# • Only ONE branch executes — the first True condition wins
# • elif is optional; you can have as many as needed
# • else is optional; catches everything not caught above
# • Conditions are evaluated top to bottom
