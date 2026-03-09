# ─────────────────────────────────────────────
# break, continue, pass
# Loop Control Statements
# ─────────────────────────────────────────────

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  break — exit the loop immediately
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# ── Real-life: Security scan — stop at first virus ──
files = ["report.pdf", "notes.txt", "malware.exe", "photo.jpg", "doc.docx"]

print("Scanning files:")
for file in files:
    print(f"  Scanning {file}...")
    if "malware" in file or file.endswith(".exe"):
        print(f"  ⛔ Threat detected: {file}! Quarantined. Scan aborted.")
        break
else:
    print("  ✓ All files clean.")

# ── Real-life: Search — stop when item found ─
products = ["Shoes", "Bag", "Watch", "Laptop", "Phone"]
search   = "Laptop"

for product in products:
    if product == search:
        print(f"'{search}' found in inventory!")
        break
else:
    print(f"'{search}' not found.")

# ── break in while — ATM limit ───────────────
# Real-life: Daily withdrawal cap
withdrawn   = 0
daily_limit = 10000
transactions = [2000, 3000, 2500, 4000, 1500]   # simulated withdrawals

for amount in transactions:
    if withdrawn + amount > daily_limit:
        print(f"Cannot withdraw ₹{amount}. Daily limit (₹{daily_limit}) would be exceeded.")
        break
    withdrawn += amount
    print(f"Withdrew ₹{amount}. Total withdrawn: ₹{withdrawn}")

print(f"Session ended. Total: ₹{withdrawn}")


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  continue — skip rest of THIS iteration, go to next
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# ── Real-life: Skip blocked users in notification system ──
users = [
    {"name": "Alice",   "blocked": False},
    {"name": "Bob",     "blocked": True},
    {"name": "Charlie", "blocked": False},
    {"name": "Diana",   "blocked": True},
    {"name": "Eve",     "blocked": False},
]

print("\nSending newsletter:")
for user in users:
    if user["blocked"]:
        print(f"  Skipping {user['name']} (blocked).")
        continue                    # skip blocked users
    print(f"  Email sent to {user['name']}.")

# ── Real-life: Skip invalid data in a dataset ─
raw_data = [23, None, 45, -1, 67, None, 12, -5, 89]

print("\nValid readings:")
valid_total = 0
count       = 0
for value in raw_data:
    if value is None or value < 0:
        continue                    # skip corrupt/invalid sensor readings
    valid_total += value
    count       += 1
    print(f"  {value}")

print(f"Average valid reading: {valid_total / count:.1f}")

# ── Real-life: Skip even numbers ─────────────
# Processing only odd transaction IDs
print("\nOdd transaction IDs:")
for txn_id in range(1001, 1015):
    if txn_id % 2 == 0:
        continue
    print(f"  Processing TXN-{txn_id}")


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  pass — do nothing (placeholder)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# pass makes a block syntactically valid without doing anything.
# Used as a placeholder during development.

# ── Placeholder function ──────────────────────
def send_email():
    pass            # TODO: implement SMTP logic later

def process_payment():
    pass            # TODO: integrate payment gateway

# ── Placeholder class ────────────────────────
class DatabaseConnection:
    pass            # will add methods later

# ── Ignore specific exceptions (rare but valid) ──
# Real-life: Try to delete a file; if it doesn't exist, silently ignore
import os

try:
    os.remove("temp_file.txt")
except FileNotFoundError:
    pass            # file didn't exist — that's fine

# ── pass in a condition — log-only branch ────
# Real-life: Monitoring system — react only to errors
status = "ok"

if status == "error":
    print("Alert sent to admin!")
elif status == "warning":
    print("Warning logged.")
else:
    pass            # all good, nothing to do

# ── Key points ───────────────────────────────
# break    → exits the innermost loop entirely
# continue → skips to the next iteration of the innermost loop
# pass     → syntactic no-op; use as placeholder during development
# Both break and continue only affect the INNERMOST loop
