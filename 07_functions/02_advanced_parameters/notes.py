# ─────────────────────────────────────────────
# Functions — Advanced Parameters
# ─────────────────────────────────────────────

# ── 1. Positional Arguments ───────────────────
# Values matched to parameters by position (left → right).

def transfer_money(sender, receiver, amount):
    print(f"₹{amount} sent from {sender} to {receiver}")

transfer_money("Alice", "Bob", 5000)    # order matters!
# transfer_money("Bob", 5000, "Alice")  # ← wrong order = wrong meaning


# ── 2. Default Arguments ──────────────────────
# A parameter gets a value if the caller doesn't supply one.
# Real-life: Email with default subject

def send_email(to, subject="No Subject", body=""):
    print(f"To: {to}")
    print(f"Subject: {subject}")
    print(f"Body: {body or '(empty)'}")
    print()

send_email("alice@example.com")
send_email("bob@example.com", "Meeting at 3 PM", "Please join the Zoom call.")

# ⚠ Mutable default argument trap — NEVER do this:
# def append_to(item, lst=[]):   ← lst is shared across all calls!
#     lst.append(item)
#     return lst
# Safe pattern:
def append_to(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst

print(append_to(1))     # [1]
print(append_to(2))     # [2]  ← independent list each time


# ── 3. Keyword Arguments ──────────────────────
# Pass arguments by name — order doesn't matter.
# Real-life: HTTP request builder

def make_request(url, method="GET", timeout=30, verify_ssl=True):
    print(f"{method} {url}  timeout={timeout}s  ssl={verify_ssl}")

make_request("https://api.example.com/users")
make_request("https://api.example.com/data", method="POST", timeout=10)
make_request("https://internal.corp/api", verify_ssl=False, timeout=5)


# ── 4. *args — Variable Positional Arguments ──
# Collects extra positional args into a TUPLE.
# Real-life: Shopping cart — add any number of items

def add_to_cart(*items):
    print("Cart:")
    for i, item in enumerate(items, 1):
        print(f"  {i}. {item}")
    print(f"  Total items: {len(items)}\n")

add_to_cart("Laptop")
add_to_cart("Mouse", "Keyboard", "Monitor", "Webcam")

# Unpacking a list into *args
wishlist = ["Headphones", "Mic Stand", "LED Light"]
add_to_cart(*wishlist)      # * unpacks the list


# ── 5. **kwargs — Variable Keyword Arguments ──
# Collects extra keyword args into a DICT.
# Real-life: User profile builder

def create_profile(username, **details):
    print(f"Profile: @{username}")
    for key, value in details.items():
        print(f"  {key}: {value}")
    print()

create_profile("jay_dev", age=22, city="Mumbai", role="Backend Dev")
create_profile("alice99", email="alice@example.com", plan="Pro")

# Unpacking a dict into **kwargs
extra = {"phone": "+91-9876543210", "verified": True}
create_profile("bob_smith", **extra)


# ── 6. Combining all parameter types ─────────
# Order must be: positional → *args → keyword/default → **kwargs
# Real-life: Logging function

def log(level, *messages, separator=" | ", **metadata):
    msg = separator.join(str(m) for m in messages)
    meta = "  ".join(f"{k}={v}" for k, v in metadata.items())
    print(f"[{level.upper()}] {msg}  {meta}")

log("info", "Server started", "Port 8080")
log("error", "DB timeout", "Retrying...", separator=" → ", host="db01", retry=3)


# ── 7. Keyword-only Arguments ─────────────────
# Placed AFTER * (or *args) — MUST be passed by name.
# Real-life: File writer where encoding must always be explicit

def write_file(path, data, *, encoding="utf-8", overwrite=False):
    mode = "w" if overwrite else "a"
    print(f"Writing to '{path}' [{encoding}] mode={mode}")
    # open(path, mode, encoding=encoding).write(data)  ← real impl

write_file("/tmp/log.txt", "Error occurred")
write_file("/tmp/out.txt", "Results", encoding="ascii", overwrite=True)
# write_file("/tmp/x.txt", "data", "latin-1")  # ← TypeError! encoding is keyword-only


# ── 8. Positional-only Arguments (Python 3.8+) ─
# Placed BEFORE / — MUST be passed positionally.
# Useful in library APIs to allow renaming internal parameters.

def circle_area(radius, /, precision=2):
    import math
    return round(math.pi * radius ** 2, precision)

print(circle_area(5))           # OK
print(circle_area(5, precision=4))  # OK
# circle_area(radius=5)         # ← TypeError! radius is positional-only


# ── Key points ────────────────────────────────
# • Default args must come after non-default args
# • *args → tuple of extra positionals
# • **kwargs → dict of extra keywords
# • Keyword-only: placed after * or *args
# • Positional-only: placed before /
# • Full order: pos-only / positional, *args, keyword-only, **kwargs
