# ─────────────────────────────────────────────
# Error Handling — Multiple Exceptions, else, finally
# ─────────────────────────────────────────────

# ── Multiple except blocks ────────────────────
# Handle different exceptions differently.
# Real-life: Bank transfer validation

def transfer(account_data, amount):
    try:
        balance = account_data["balance"]   # KeyError?
        result  = balance - float(amount)   # ValueError? TypeError?
        if result < 0:
            raise ValueError("Insufficient funds")
        print(f"Transfer OK — Remaining: ₹{result:.2f}")
    except KeyError as e:
        print(f"Account field missing: {e}")
    except (TypeError, ValueError) as e:
        print(f"Invalid transfer: {e}")

transfer({"balance": 5000}, 1500)       # OK
transfer({"balance": 5000}, "abc")      # ValueError
transfer({}, 1500)                       # KeyError
transfer({"balance": 500}, 1500)        # ValueError: Insufficient funds


# ── Catching multiple in one except ──────────
# Use a tuple of exception types.

def safe_divide(a, b):
    try:
        return a / b
    except (ZeroDivisionError, TypeError) as e:
        print(f"Cannot divide: {e}")
        return None

print(safe_divide(10, 2))       # 5.0
print(safe_divide(10, 0))       # Cannot divide
print(safe_divide(10, "x"))     # Cannot divide


# ── else block ────────────────────────────────
# Runs ONLY if NO exception was raised in try.
# Use it for code that should run on success — keeps try block minimal.
# Real-life: Database record fetch

def get_user(user_id, database):
    try:
        user = database[user_id]
    except KeyError:
        print(f"User {user_id} not found.")
    else:
        # Runs only if lookup succeeded
        print(f"Welcome back, {user['name']}! Last login: {user['last_login']}")

db = {
    101: {"name": "Alice", "last_login": "2024-01-10"},
    102: {"name": "Bob",   "last_login": "2024-01-12"},
}

get_user(101, db)   # Welcome back, Alice!
get_user(999, db)   # User 999 not found.


# ── finally block ─────────────────────────────
# Runs ALWAYS — whether exception occurred or not.
# Real-life: Resource cleanup (file, DB, network connection)

def process_file(path):
    f = None
    try:
        f = open(path)
        data = f.read()
        print(f"Processed {len(data)} bytes")
    except FileNotFoundError:
        print(f"File not found: {path}")
    finally:
        if f:
            f.close()
            print("File closed.")    # always executes

process_file("notes.py")
process_file("missing.txt")


# ── Full structure: try / except / else / finally ─
# Real-life: API call with connection management

class FakeDB:
    connected = False
    def connect(self):
        self.connected = True
        print("[DB] Connection opened")
    def query(self, sql):
        if "DROP" in sql.upper():
            raise PermissionError("DROP not allowed")
        return [{"id": 1, "name": "Alice"}]
    def close(self):
        self.connected = False
        print("[DB] Connection closed")

def run_query(sql):
    db = FakeDB()
    result = None
    try:
        db.connect()
        result = db.query(sql)
    except PermissionError as e:
        print(f"[ERROR] {e}")
    else:
        print(f"[OK] Rows returned: {len(result)}")
    finally:
        db.close()          # always close, even on error
    return result

run_query("SELECT * FROM users")
print()
run_query("DROP TABLE users")


# ── Order of execution summary ─────────────────
#
#   try block
#     ├── exception raised?
#     │     Yes → matching except block → finally
#     │     No  → else block            → finally
#     └── finally always runs
#
#   If an exception happens in except/else → finally still runs first,
#   then the new exception propagates.


# ── Nested try blocks ─────────────────────────
# Real-life: Retry logic with fallback

def load_data(sources):
    for source in sources:
        try:
            if source == "cache":
                raise ConnectionError("Cache miss")
            if source == "primary_db":
                raise TimeoutError("DB timeout")
            # "backup_db" succeeds
            print(f"Loaded from: {source}")
            return {"data": "..."}
        except (ConnectionError, TimeoutError) as e:
            print(f"Source '{source}' failed: {e} — trying next...")
    return None

result = load_data(["cache", "primary_db", "backup_db"])
print(f"Result: {result}")


# ── Key points ────────────────────────────────
# • Multiple except: handle different failures differently
# • except (A, B): handle multiple exceptions the same way
# • else: success-only code — keeps try block minimal and clear
# • finally: cleanup code — file close, DB disconnect, lock release
# • finally runs even if try/except has a return or re-raises
