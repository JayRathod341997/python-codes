# ─────────────────────────────────────────────
# while Loop
# ─────────────────────────────────────────────

# ── Syntax ───────────────────────────────────
# while <condition>:
#     <block>          ← repeats as long as condition is True

# Use while when you DON'T know in advance how many iterations you need.

# ── Basic while ──────────────────────────────
# Real-life: ATM PIN retry system
correct_pin  = 1234
attempts     = 0
max_attempts = 3

pin = int(input("Enter PIN: ") if False else "1234")  # simulated input

while pin != correct_pin and attempts < max_attempts:
    attempts += 1
    print(f"Wrong PIN. Attempt {attempts}/{max_attempts}.")
    if attempts < max_attempts:
        pin = int(input("Try again: ") if False else "1234")

if pin == correct_pin:
    print("Access granted.")
else:
    print("Card blocked after 3 failed attempts.")

# ── Countdown timer ──────────────────────────
# Real-life: Rocket launch / exam timer
import time

countdown = 5
print("Launch sequence initiated:")
while countdown > 0:
    print(f"  T-{countdown}...")
    countdown -= 1
    # time.sleep(1)     # uncomment for real countdown

print("Liftoff!")

# ── Accumulator pattern ──────────────────────
# Real-life: Running total (cashier POS system)
# Simulated items scanned at checkout
items  = [120, 350, 89, 450, 25]
total  = 0
index  = 0

while index < len(items):
    total += items[index]
    print(f"  Scanned item #{index + 1}: ₹{items[index]}  |  Running total: ₹{total}")
    index += 1

print(f"Final bill: ₹{total}")

# ── Input validation loop ─────────────────────
# Real-life: Sign-up form — enforce strong password
# (simulated without real input)
passwords_to_try = ["abc", "short1", "StrongPass@9"]   # simulate attempts
i = 0

password = passwords_to_try[i]
while len(password) < 8 or not any(c.isupper() for c in password):
    print(f"  '{password}' is too weak. Must be 8+ chars with an uppercase letter.")
    i += 1
    password = passwords_to_try[i]

print(f"  Password '{password}' accepted!")

# ── while True — run until explicit break ─────
# Real-life: Server listening for requests (simplified)
requests_received = ["ping", "data", "data", "shutdown"]
idx = 0

while True:
    request = requests_received[idx]
    idx += 1
    print(f"Received: {request}")

    if request == "shutdown":
        print("Server shutting down.")
        break           # exit the loop

# ── Key points ───────────────────────────────
# • Always ensure the condition eventually becomes False — avoid infinite loops
# • Common bugs: forgetting to update the loop variable (infinite loop)
# • while True + break is idiomatic for "run until a stop condition"
# • Prefer for loops when you know the number of iterations upfront
