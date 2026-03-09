# ─────────────────────────────────────────────
# Loop else
# ─────────────────────────────────────────────

# Python's loops have an optional else clause.
# The else block runs ONLY if the loop completes NORMALLY
# (i.e., it was NOT terminated by a break).

# ── Syntax ───────────────────────────────────
# for item in iterable:
#     if condition:
#         break
# else:
#     # runs only if break was NEVER hit

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  for...else
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# ── Real-life: Product search ────────────────
catalog   = ["Laptop", "Phone", "Tablet", "Watch"]
searched  = "Camera"

for item in catalog:
    if item == searched:
        print(f"'{searched}' found in catalog!")
        break
else:
    print(f"'{searched}' not found. Would you like to add it?")
    # → runs because break was never hit

# Compare: same with a found item
searched = "Phone"
for item in catalog:
    if item == searched:
        print(f"'{searched}' found in catalog!")
        break
else:
    print(f"'{searched}' not found.")
    # → does NOT run because break was hit

# ── Real-life: User authentication ───────────
users_db = [
    {"username": "alice", "password": "pass123"},
    {"username": "bob",   "password": "qwerty"},
]

login_user = "charlie"
login_pass = "secret"

for user in users_db:
    if user["username"] == login_user and user["password"] == login_pass:
        print(f"Login successful! Welcome, {login_user}.")
        break
else:
    print("Login failed. Username or password incorrect.")
    # → runs because charlie isn't in the db

# ── Real-life: Prime checker using loop else ──
# Classic idiom — the else runs only if no factor was found
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            print(f"{n} is NOT prime (divisible by {i}).")
            break
    else:
        print(f"{n} IS prime.")
        return True
    return False

is_prime(17)    # IS prime
is_prime(18)    # NOT prime (divisible by 2)
is_prime(97)    # IS prime

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  while...else
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# ── Real-life: Retry mechanism ───────────────
# Simulated API call — succeeds on 3rd attempt
import random
random.seed(42)

attempt  = 0
max_tries = 5
succeeded = False

# Simulate: fail, fail, succeed
responses = [False, False, True, False, False]

while attempt < max_tries:
    response_ok = responses[attempt]
    attempt += 1
    print(f"  API call attempt {attempt}... {'OK' if response_ok else 'Failed'}")

    if response_ok:
        print("  Connection established!")
        break
else:
    # All attempts exhausted without a break
    print("  All retries failed. Service unavailable. Alert sent to ops team.")

# ── Real-life: Queue drain ───────────────────
# Process a job queue — else runs when queue is fully processed
job_queue = ["resize_image", "send_email", "generate_report"]

while job_queue:
    job = job_queue.pop(0)
    print(f"Executing: {job}")
    # no break here
else:
    print("All jobs completed. Queue is empty.")

# ── When break IS hit — else skipped ─────────
data_stream = [10, 20, -999, 30, 40]   # -999 is sentinel (end-of-stream)
total = 0

for val in data_stream:
    if val == -999:
        print("Sentinel reached. Stream truncated.")
        break
    total += val
else:
    print(f"Stream fully processed. Total = {total}")

# → else does NOT run because break was hit

# ── Key points ───────────────────────────────
# • else runs if the loop finishes WITHOUT a break
# • else does NOT mean "if loop body didn't execute even once"
# • Mental model: read it as "no break" not "else"
# • Use case: searching + acting on "not found" without a found_flag variable
