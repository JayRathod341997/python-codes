# ─────────────────────────────────────────────
# Error Handling — Exceptions & try / except
# ─────────────────────────────────────────────

# ── What is an Exception? ─────────────────────
# An exception is an event that disrupts normal program flow.
# Python raises an exception object; if not caught, the program crashes.

# Common built-in exceptions:
#   ZeroDivisionError   — dividing by zero
#   TypeError           — wrong type for an operation
#   ValueError          — right type, bad value  (int("abc"))
#   IndexError          — list index out of range
#   KeyError            — dict key not found
#   FileNotFoundError   — file doesn't exist
#   AttributeError      — object has no such attribute
#   NameError           — variable not defined
#   ImportError         — module not found

# Without exception handling — program crashes:
# print(10 / 0)   # ZeroDivisionError: division by zero


# ── Basic try / except ────────────────────────
# Syntax:
#   try:
#       <risky code>
#   except ExceptionType:
#       <recovery code>

# Real-life: ATM division — compute per-person share
def split_bill(total, people):
    try:
        share = total / people
        print(f"Each person pays: ₹{share:.2f}")
    except ZeroDivisionError:
        print("Error: Cannot split bill among 0 people.")

split_bill(1500, 3)     # Each person pays: ₹500.00
split_bill(1500, 0)     # Error: Cannot split bill among 0 people.


# ── Catching the exception object with `as` ───
# Real-life: User age input parser
def parse_age(raw):
    try:
        age = int(raw)
        print(f"Age registered: {age}")
    except ValueError as e:
        print(f"Invalid input: '{raw}' → {e}")

parse_age("25")
parse_age("twenty")
parse_age("12.5")


# ── Exception hierarchy ────────────────────────
# BaseException
#   └── Exception
#         ├── ArithmeticError
#         │     └── ZeroDivisionError
#         ├── LookupError
#         │     ├── IndexError
#         │     └── KeyError
#         ├── ValueError
#         ├── TypeError
#         └── ... (many more)
#
# Catching a parent catches all its children:

try:
    x = [1, 2, 3]
    print(x[10])
except LookupError as e:        # catches IndexError AND KeyError
    print(f"Lookup failed: {e}")


# ── Real-life: File reader with fallback ──────
def read_config(path):
    try:
        with open(path) as f:
            content = f.read()
            print(f"Config loaded ({len(content)} bytes)")
            return content
    except FileNotFoundError:
        print(f"Config file '{path}' not found. Using defaults.")
        return {}

read_config("app_config.json")
read_config("settings.yaml")


# ── Real-life: API response parser ───────────
import json

def parse_response(raw_json):
    try:
        data = json.loads(raw_json)
        user = data["user"]["name"]
        print(f"Logged in as: {user}")
    except json.JSONDecodeError as e:
        print(f"Invalid JSON: {e}")
    except KeyError as e:
        print(f"Missing field in response: {e}")

parse_response('{"user": {"name": "Alice", "id": 42}}')   # OK
parse_response('not-json-at-all')                          # JSONDecodeError
parse_response('{"status": "ok"}')                        # KeyError: 'user'


# ── Bare except (avoid!) ──────────────────────
# except:  ← catches EVERYTHING including KeyboardInterrupt, SystemExit
# This hides bugs. Always catch specific exceptions.

# ── except Exception (acceptable catch-all) ───
def safe_run(func, *args):
    try:
        return func(*args)
    except Exception as e:
        print(f"[{type(e).__name__}] {e}")
        return None

safe_run(int, "abc")        # [ValueError] ...
safe_run(lambda: 1/0)       # [ZeroDivisionError] ...


# ── Key points ────────────────────────────────
# • try block: code that might raise an exception
# • except block: runs only if the matching exception is raised
# • Use `as e` to access the exception message/object
# • Always catch specific exceptions — avoid bare `except:`
# • The exception object has .args and meaningful __str__
