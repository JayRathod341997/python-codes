# ─────────────────────────────────────────────
# Encapsulation
# ─────────────────────────────────────────────

# ── What is Encapsulation? ────────────────────
# Bundling data (attributes) + the methods that operate on that data
# inside a single unit (class), and controlling access to internals.
#
# Real-life analogy:
#   ATM machine — you can check balance, deposit, withdraw
#   BUT you cannot directly reach inside and change the balance number.
#   The machine controls HOW you interact with the data.
#
# Benefits:
#   • Prevents accidental/invalid modifications
#   • Hides implementation details
#   • Provides a clean public interface


# ── Access Levels (Convention-based in Python) ─
#
#   public    →  name        accessible everywhere
#   protected →  _name       "internal use" — accessible but signalled as private
#   private   →  __name      name-mangled → hard (but not impossible) to access outside


# ══ Public Attributes ══════════════════════════
class Car:
    def __init__(self, brand, model):
        self.brand = brand      # public — anyone can read/write
        self.model = model      # public

c = Car("Toyota", "Camry")
print(c.brand)          # Toyota   ← fine
c.brand = "Honda"       # also fine — public allows this


# ══ Protected Attributes (_name) ══════════════
# Convention: prefix with single underscore
# Meaning: "don't use this outside the class / subclass"
# Python does NOT enforce it — it's a gentleman's agreement.

class DatabaseConnection:
    def __init__(self, host, port, password):
        self.host      = host       # public — ok to read
        self._port     = port       # protected — internal detail
        self._password = password   # protected — shouldn't be used outside

    def connect(self):
        print(f"Connecting to {self.host}:{self._port} ...")
        # _password used internally; callers don't need to know about it

db = DatabaseConnection("localhost", 5432, "secret123")
print(db.host)          # fine — public
print(db._port)         # works, but convention says "don't do this externally"


# ══ Private Attributes (__name) ════════════════
# Double underscore triggers Python's name-mangling:
#   __balance inside class Account → stored as _Account__balance
# Makes accidental access from outside much harder.
#
# Real-life: Bank account balance — should ONLY change through deposit/withdraw

class BankAccount:
    def __init__(self, owner, balance):
        self.owner    = owner
        self.__balance = balance    # private — protected from outside modification

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive.")
        if amount > self.__balance:
            raise ValueError("Insufficient balance.")
        self.__balance -= amount

    def get_balance(self):          # controlled read access
        return self.__balance

    def statement(self):
        print(f"{self.owner}'s balance: ₹{self.__balance:,.2f}")

acc = BankAccount("Alice", 50_000)
acc.deposit(10_000)
acc.withdraw(5_000)
acc.statement()         # Alice's balance: ₹55,000.00

# Direct access fails due to name mangling:
# print(acc.__balance)          # AttributeError
print(acc._BankAccount__balance)  # ₹55000.0 — possible but BAD practice

# Proper way: use the public method
print(acc.get_balance())          # ₹55000.0


# ══ Properties (@property) ════════════════════
# Python's elegant way to implement getters/setters.
# Looks like attribute access from outside, but runs method code.
#
# Real-life: User profile — email must be validated before saving

class UserProfile:
    def __init__(self, name, email, age):
        self.name   = name
        self.email  = email     # goes through setter
        self.age    = age       # goes through setter

    # ── email property ──────────────────────────
    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        if "@" not in value or "." not in value:
            raise ValueError(f"Invalid email: {value}")
        self.__email = value.lower().strip()

    # ── age property ────────────────────────────
    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if not (0 < value < 130):
            raise ValueError(f"Age must be between 1 and 129, got {value}")
        self.__age = value

    # ── read-only property (no setter) ──────────
    @property
    def display_name(self):
        return f"{self.name} ({self.__age})"

    def __repr__(self):
        return f"UserProfile(name={self.name!r}, email={self.__email!r}, age={self.__age})"

u = UserProfile("Alice", "Alice@Email.COM", 28)
print(u.email)          # alice@email.com  (normalised by setter)
print(u.age)            # 28
print(u.display_name)   # Alice (28)
print(repr(u))

u.email = "alice@newdomain.in"  # setter validates + normalises
print(u.email)

# u.age = -5            # raises ValueError
# u.age = 200           # raises ValueError
# u.display_name = "x"  # AttributeError — read-only property


# ══ Real-life Full Example: Product Inventory ═
# Real-life: E-commerce warehouse stock management

class InventoryItem:
    def __init__(self, sku, name, price, stock):
        self.sku    = sku
        self.name   = name
        self.price  = price     # setter validates
        self.__stock = 0
        self.restock(stock)     # reuse validation logic

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self.__price = round(value, 2)

    @property
    def stock(self):
        return self.__stock

    @property
    def in_stock(self):         # read-only derived property
        return self.__stock > 0

    def restock(self, qty):
        if qty < 0:
            raise ValueError("Restock quantity cannot be negative.")
        self.__stock += qty
        print(f"  [{self.sku}] Restocked {qty} units → total {self.__stock}")

    def sell(self, qty):
        if qty > self.__stock:
            raise ValueError(f"Only {self.__stock} units available.")
        self.__stock -= qty
        revenue = qty * self.__price
        print(f"  [{self.sku}] Sold {qty} units @ ₹{self.__price} → ₹{revenue:.2f}")
        return revenue

    def info(self):
        status = "✓ In Stock" if self.in_stock else "✗ Out of Stock"
        print(f"  {self.sku}  {self.name:20s}  ₹{self.__price:>8.2f}  {self.__stock:>4} units  {status}")

item = InventoryItem("USB-001", "USB-C Hub", 1_299.00, 100)
item.sell(30)
item.sell(15)
item.restock(20)
item.info()

item.price = 1_199.00   # price drop
item.info()
# item.price = -50      # raises ValueError
# item.stock = 999      # AttributeError — no setter for stock


# ── Key points ────────────────────────────────
# • public   → no prefix; accessible anywhere (default)
# • protected → _name; convention only; "handle with care"
# • private   → __name; name-mangled; hard to access from outside
# • @property → clean getter; @x.setter → validation on write
# • Use properties over raw getters/setters (more Pythonic)
# • Encapsulation = data hiding + controlled interface
