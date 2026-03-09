# ─────────────────────────────────────────────
# Exercises — Multiple Exceptions, else, finally
# ─────────────────────────────────────────────

# ── Exercise 1: File Word Counter ────────────
# Real-life: Document analytics tool
# Write a function count_words(filepath) that:
#   try    — open file and count words
#   except FileNotFoundError  — print "File not found"
#   except PermissionError    — print "No read permission"
#   else   — print "File has N words"   (only on success)
#   finally— print "Done." always
#
# Test with: "notes.py" (exists), "ghost.txt" (missing)

# --- your code here ---


# ── Exercise 2: Safe Calculator ───────────────
# Real-life: Scientific calculator app
# Write a function calculate(expr) that evaluates a string
# like "10 + 5", "9 / 0", "4 ** 0.5", "abc + 1".
# Use eval() inside try, catch:
#   ZeroDivisionError → "Cannot divide by zero"
#   NameError         → "Unknown variable in expression"
#   SyntaxError       → "Invalid expression syntax"
# else  → print "Result: <value>"
# finally → print "Calculation attempt finished"
#
# Test: "10 + 5", "9 / 0", "x + 1", "10 +"

# --- your code here ---


# ── Exercise 3: Database Transaction Simulator ─
# Real-life: Order placement with DB transaction
# Simulate a transaction with these steps inside try:
#   1. Connect to DB (just print "[DB] Connected")
#   2. Begin transaction (print "[DB] Transaction started")
#   3. Insert order — raise RuntimeError("Duplicate order ID") if
#      order_id is in existing_orders set
#   4. Commit (print "[DB] Committed")
# except RuntimeError  → print error, print "[DB] Rolled back"
# else                 → print "[ORDER] Placed successfully"
# finally             → print "[DB] Connection closed"
#
# existing_orders = {1001, 1002, 1003}
# Test with order_id=1004 (success) and order_id=1002 (duplicate)

# --- your code here ---


# ── Exercise 4: Network Request Simulator ─────
# Real-life: HTTP client with timeout and error handling
# Write a function fetch(url, timeout=5):
# Simulate different failures based on url:
#   url containing "timeout"    → raise TimeoutError("Request timed out")
#   url containing "forbidden"  → raise PermissionError("403 Forbidden")
#   url containing "notfound"   → raise FileNotFoundError("404 Not Found")
#   anything else               → success, return fake JSON string
#
# In the caller:
#   except TimeoutError    → "Retry after a moment"
#   except PermissionError → "Check your API key"
#   except FileNotFoundError→"Wrong endpoint URL"
#   except Exception as e  → "Unexpected error: {e}"
#   else                   → "Response received: {data[:30]}..."
#   finally                → "Request to {url} completed"
#
# Test all four cases.

# --- your code here ---


# ── Exercise 5: User Registration Pipeline ────
# Real-life: Sign-up form with multi-step validation
# Write a function register_user(data: dict):
# Steps (each in its own try/except):
#   Step 1 — validate email: must contain "@" → ValueError
#   Step 2 — validate age: must be int ≥ 18   → TypeError / ValueError
#   Step 3 — check username availability (fake set of taken names)
#             → raise RuntimeError if taken
#   Step 4 — "save to DB" (just print success)
# After all steps succeed (else) → print "Registration complete!"
# Use a finally to always print "--- Validation finished ---"
#
# Test:
#   {"email": "bad", "age": 22, "username": "alice"}
#   {"email": "a@b.com", "age": 16, "username": "alice"}
#   {"email": "a@b.com", "age": 22, "username": "admin"}   ← taken
#   {"email": "a@b.com", "age": 22, "username": "newuser"} ← success

TAKEN_USERNAMES = {"admin", "root", "superuser", "guest"}

# --- your code here ---


# ─────────────────────────────────────────────
# Expected outputs (for self-check):
# Ex1: word count + "Done."  OR  error + "Done."
# Ex2: Results/errors + "Calculation attempt finished" for each
# Ex3: Success path: Connected→Started→Committed→Placed→Closed
#      Failure path: Connected→Started→Rolled back→Closed
# Ex4: Four different responses + "Request to {url} completed" each
# Ex5: Four runs — first 3 fail at different steps, last succeeds
# ─────────────────────────────────────────────
