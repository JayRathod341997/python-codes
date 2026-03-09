# ─────────────────────────────────────────────
# OOP Basics — Classes, Objects, __init__,
#              Instance & Class Variables
# ─────────────────────────────────────────────

# ── What is OOP? ──────────────────────────────
# Object-Oriented Programming models real-world entities as "objects"
# that bundle data (attributes) + behaviour (methods) together.
#
# Real-life analogy:
#   Blueprint  →  Class       (recipe for a bank account)
#   House      →  Object      (an actual account created from the blueprint)
#
# Four pillars: Encapsulation, Inheritance, Polymorphism, Abstraction


# ── Defining a Class ──────────────────────────
# Syntax:
#   class ClassName:
#       body

class Dog:
    pass        # empty class — valid Python

fido = Dog()    # create an object (instance) from the class
print(type(fido))       # <class '__main__.Dog'>
print(isinstance(fido, Dog))    # True


# ── __init__ — The Constructor ────────────────
# __init__ runs automatically when a new object is created.
# Use it to initialise the object's starting state.
#
# Real-life: Opening a bank account — initial setup (name, balance)

class BankAccount:
    def __init__(self, owner, balance=0.0):
        # 'self' refers to the new object being created
        self.owner   = owner        # instance variable
        self.balance = balance      # instance variable

    def deposit(self, amount):
        self.balance += amount
        print(f"  ✓ Deposited ₹{amount:.2f}  |  Balance: ₹{self.balance:.2f}")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"  ✗ Insufficient funds (balance ₹{self.balance:.2f})")
        else:
            self.balance -= amount
            print(f"  ✓ Withdrew  ₹{amount:.2f}  |  Balance: ₹{self.balance:.2f}")

    def show(self):
        print(f"Account[{self.owner}] → ₹{self.balance:.2f}")

acc1 = BankAccount("Alice", 10_000)
acc2 = BankAccount("Bob")               # default balance = 0.0

acc1.deposit(5_000)
acc1.withdraw(2_000)
acc2.deposit(1_500)
acc1.show()
acc2.show()


# ── Instance Variables ────────────────────────
# Defined inside __init__ with self.name = value
# Each object gets its OWN copy — changes don't affect other objects.

class Product:
    def __init__(self, name, price, stock):
        self.name  = name
        self.price = price
        self.stock = stock

    def sell(self, qty):
        if qty > self.stock:
            print(f"Only {self.stock} units of '{self.name}' left.")
        else:
            self.stock -= qty
            print(f"Sold {qty}x '{self.name}'  |  Remaining: {self.stock}")

laptop = Product("Laptop", 75_000, 10)
phone  = Product("Phone",  25_000, 50)

laptop.sell(3)      # Sold 3x 'Laptop'  |  Remaining: 7
phone.sell(20)      # Sold 20x 'Phone'  |  Remaining: 30
laptop.sell(10)     # Only 7 units of 'Laptop' left.

# Accessing + modifying attributes directly
print(laptop.name, laptop.price)    # Laptop 75000
laptop.price = 72_000               # price drop
print(laptop.price)                 # 72000


# ── Class Variables ───────────────────────────
# Defined OUTSIDE __init__, at class level.
# SHARED across all instances — one copy for the whole class.
#
# Real-life: A bank has one fixed interest rate for all savings accounts.

class SavingsAccount:
    interest_rate = 0.04        # class variable — 4% for everyone
    account_count = 0           # tracks total accounts created

    def __init__(self, owner, balance):
        self.owner   = owner    # instance variable
        self.balance = balance  # instance variable
        SavingsAccount.account_count += 1   # update class variable

    def add_interest(self):
        interest = self.balance * SavingsAccount.interest_rate
        self.balance += interest
        print(f"{self.owner}: +₹{interest:.2f} interest → ₹{self.balance:.2f}")

s1 = SavingsAccount("Alice", 50_000)
s2 = SavingsAccount("Bob",   30_000)
s3 = SavingsAccount("Carol", 80_000)

s1.add_interest()   # Alice:  +₹2000.00 interest → ₹52000.00
s2.add_interest()   # Bob:    +₹1200.00 interest → ₹31200.00
s3.add_interest()   # Carol:  +₹3200.00 interest → ₹83200.00

# Change rate — affects ALL existing instances
SavingsAccount.interest_rate = 0.05
s1.add_interest()   # now at 5%

print(f"Total accounts: {SavingsAccount.account_count}")    # 3

# Class variable vs instance variable
print(s1.interest_rate)             # 0.05  (looks up class)
s1.interest_rate = 0.06             # ← creates an INSTANCE variable, shadows class var
print(s1.interest_rate)             # 0.06  (instance)
print(s2.interest_rate)             # 0.05  (class — unchanged)
print(SavingsAccount.interest_rate) # 0.05  (class — unchanged)


# ── Putting it all together: Employee ────────
# Real-life: HR system

class Employee:
    company   = "TechCorp Ltd."     # class variable
    headcount = 0                   # class variable

    def __init__(self, name, role, salary):
        self.name   = name          # instance variable
        self.role   = role          # instance variable
        self.salary = salary        # instance variable
        Employee.headcount += 1

    def give_raise(self, pct):
        hike = self.salary * pct / 100
        self.salary += hike
        print(f"{self.name} got {pct}% raise → ₹{self.salary:,.0f}")

    def info(self):
        print(f"[{Employee.company}]  {self.name} | {self.role} | ₹{self.salary:,.0f}")

e1 = Employee("Priya",  "Engineer",     80_000)
e2 = Employee("Rahul",  "Designer",     65_000)
e3 = Employee("Sneha",  "Manager",     1_20_000)

for emp in (e1, e2, e3):
    emp.info()

e1.give_raise(10)
print(f"Total employees: {Employee.headcount}")


# ── Key points ────────────────────────────────
# • class defines a blueprint; an object is a concrete instance
# • __init__ initialises an object's state; 'self' is the object itself
# • Instance variables  → unique per object  (self.x = ...)
# • Class variables     → shared by all      (ClassName.x = ...)
# • Modifying a class variable via an instance creates a shadow copy
