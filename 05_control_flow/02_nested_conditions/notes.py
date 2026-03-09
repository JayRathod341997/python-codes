# ─────────────────────────────────────────────
# Nested Conditions
# ─────────────────────────────────────────────

# Nesting = placing an if block INSIDE another if block
# Use when decisions depend on multiple layered criteria

# ── Basic nesting ────────────────────────────
# Real-life: Online loan eligibility
age    = 28
salary = 55000      # monthly ₹
cibil  = 720        # credit score

if age >= 21:
    if salary >= 30000:
        if cibil >= 700:
            print("Loan APPROVED ✓")
        else:
            print("Loan denied — low credit score.")
    else:
        print("Loan denied — insufficient salary.")
else:
    print("Loan denied — must be 21 or older.")

# ── Combining nested + elif ───────────────────
# Real-life: Airport check-in
has_passport  = True
visa_valid    = True
flight_status = "on_time"   # "on_time" | "delayed" | "cancelled"

if has_passport:
    if visa_valid:
        if flight_status == "on_time":
            print("Proceed to gate.")
        elif flight_status == "delayed":
            print("Flight delayed. Wait in lounge.")
        else:
            print("Flight cancelled. Contact airline.")
    else:
        print("Check-in denied — visa not valid.")
else:
    print("Check-in denied — passport required.")

# ── Real-life: E-commerce return policy ──────
days_since_purchase = 20
item_condition      = "unopened"    # "unopened" | "opened" | "damaged"
has_receipt         = True

if days_since_purchase <= 30:
    if has_receipt:
        if item_condition == "unopened":
            print("Full refund approved.")
        elif item_condition == "opened":
            print("Exchange only — item was opened.")
        else:
            print("Return denied — item is damaged.")
    else:
        print("Return denied — receipt required.")
else:
    print("Return window closed (30 days exceeded).")

# ── Avoid deep nesting — flatten with 'and' ──
# The above loan check rewritten cleanly:
if age >= 21 and salary >= 30000 and cibil >= 700:
    print("Loan APPROVED (flat version) ✓")
else:
    print("Loan denied — check eligibility criteria.")

# ── When nesting IS appropriate ──────────────
# Use nesting when different branches need DIFFERENT sub-conditions.
# Flat and/or can't distinguish which specific check failed.

# Real-life: Student grade + attendance check
marks      = 72
attendance = 60     # percent

if marks >= 40:
    print("Passed marks.")
    if attendance >= 75:
        print("Eligible to sit for exam.")
    else:
        print(f"Low attendance ({attendance}%). Detained.")
else:
    print("Failed. Must re-appear in supplementary exam.")

# ── Key points ───────────────────────────────
# • Each level of nesting adds 4 spaces of indentation
# • Deep nesting (> 3 levels) makes code hard to read — refactor with functions
# • Use 'and'/'or' to flatten when the same result applies across conditions
# • Use nesting when you need to DISTINGUISH which specific sub-check failed
