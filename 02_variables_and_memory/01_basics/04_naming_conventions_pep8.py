# ============================================================
# Naming Conventions — PEP 8
# ============================================================
# PEP 8 is Python's official style guide. Following it makes
# code readable and consistent across the Python community.
# ============================================================

# --- snake_case: variables, functions, modules ---
user_name = "Jay"
max_retry_count = 3
total_price = 99.99

def calculate_area(length, width):
    return length * width

# --- UPPER_SNAKE_CASE: constants ---
PI = 3.14159
MAX_CONNECTIONS = 100
DEFAULT_TIMEOUT = 30

# --- CamelCase (PascalCase): classes ---
class BankAccount:
    pass

class HttpRequestHandler:
    pass

# --- _single_leading_underscore: "internal use" hint ---
_internal_cache = {}

# --- __double_leading_underscore: name mangling in classes ---
class MyClass:
    def __init__(self):
        self.__private_data = 42

# --- __dunder__ (double under on both sides): special/magic names ---
# Examples: __init__, __str__, __len__ — never invent your own.

# --- Avoid these (shadow built-ins) ---
# list = [1, 2, 3]   # BAD — shadows built-in 'list'
# id = 5             # BAD — shadows built-in 'id'
# type = "admin"     # BAD — shadows built-in 'type'

# --- Good vs bad names ---
# BAD
x = 86400
d = "John"
tmp = calculate_area(5, 3)

# GOOD
seconds_per_day = 86400
customer_name = "John"
room_area = calculate_area(5, 3)

print(customer_name, seconds_per_day, room_area)

# --- Meaningful boolean names ---
is_active = True
has_permission = False
can_edit = True

print(is_active, has_permission, can_edit)
