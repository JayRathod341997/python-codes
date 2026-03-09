# ─────────────────────────────────────────────
# Inheritance & Method Overriding
# ─────────────────────────────────────────────

# ── What is Inheritance? ──────────────────────
# A child class (subclass) automatically gets all attributes and methods
# of its parent class (superclass) — and can add/override things.
#
# Real-life analogy:
#   Vehicle (parent) → Car, Truck, Motorcycle (children)
#   All share: engine, wheels, fuel
#   Each adds: car doors, truck payload, motorcycle handlebar
#
# Syntax:
#   class Child(Parent):
#       ...


# ══ Basic Inheritance ═════════════════════════
# Real-life: Employee types in a company

class Employee:
    """Base class for all employees."""
    company = "TechCorp"

    def __init__(self, name, emp_id, salary):
        self.name    = name
        self.emp_id  = emp_id
        self.salary  = salary

    def work(self):
        print(f"{self.name} is working.")

    def info(self):
        print(f"[{self.emp_id}] {self.name}  |  ₹{self.salary:,.0f}")


class Developer(Employee):
    """Developer inherits everything from Employee + adds tech_stack."""

    def __init__(self, name, emp_id, salary, tech_stack):
        super().__init__(name, emp_id, salary)  # call parent __init__
        self.tech_stack = tech_stack            # extra attribute

    def code(self):             # new method
        print(f"{self.name} is coding in {', '.join(self.tech_stack)}.")


class Manager(Employee):
    """Manager inherits + manages a team."""

    def __init__(self, name, emp_id, salary, team):
        super().__init__(name, emp_id, salary)
        self.team = team

    def conduct_meeting(self):
        print(f"{self.name} is running a meeting with: {', '.join(self.team)}")


dev  = Developer("Priya",  "D001", 90_000, ["Python", "Django", "React"])
mgr  = Manager("Rahul",   "M001", 1_50_000, ["Priya", "Sneha", "Arjun"])

dev.info()              # inherited from Employee
dev.work()              # inherited from Employee
dev.code()              # Developer's own method

mgr.info()              # inherited
mgr.conduct_meeting()   # Manager's own method

# isinstance checks
print(isinstance(dev, Developer))   # True
print(isinstance(dev, Employee))    # True — dev IS-A Employee
print(isinstance(mgr, Developer))   # False


# ══ super() — Calling Parent Methods ══════════
# super() lets you call a method from the parent class.
# Essential in __init__ to initialise inherited attributes.

class Animal:
    def __init__(self, name, species):
        self.name    = name
        self.species = species

    def breathe(self):
        print(f"{self.name} breathes.")

    def describe(self):
        print(f"{self.name} is a {self.species}.")


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Canis lupus familiaris")   # parent __init__
        self.breed = breed

    def describe(self):
        super().describe()                  # call parent version first
        print(f"Breed: {self.breed}")       # add extra info

    def fetch(self):
        print(f"{self.name} fetches the ball!")

rex = Dog("Rex", "German Shepherd")
rex.breathe()       # inherited — Animal.breathe
rex.describe()      # overridden — calls super().describe() then adds breed
rex.fetch()


# ══ Method Overriding ══════════════════════════
# A child class can redefine a method from the parent.
# The child version replaces the parent's version for that class.
#
# Real-life: Different payment types calculate fees differently

class Payment:
    def __init__(self, amount):
        self.amount = amount

    def process(self):
        print(f"Processing payment of ₹{self.amount:.2f}")

    def fee(self):
        return 0.0      # base: no fee

    def summary(self):
        total = self.amount + self.fee()
        print(f"  Amount : ₹{self.amount:.2f}")
        print(f"  Fee    : ₹{self.fee():.2f}")
        print(f"  Total  : ₹{total:.2f}")


class CreditCardPayment(Payment):
    FEE_RATE = 0.02     # 2% processing fee

    def process(self):
        # override: add fee logic before calling common logic
        print("Contacting card network...")
        super().process()   # reuse parent message

    def fee(self):
        return round(self.amount * self.FEE_RATE, 2)  # override


class UPIPayment(Payment):
    def process(self):
        print("Sending UPI request...")
        super().process()

    def fee(self):
        return 0.0      # UPI is free (same as base, but explicit)


class WalletPayment(Payment):
    CASHBACK_RATE = 0.01    # 1% cashback (negative fee)

    def process(self):
        print("Deducting from wallet...")
        super().process()

    def fee(self):
        return -round(self.amount * self.CASHBACK_RATE, 2)  # negative = cashback


for pay in [CreditCardPayment(5000), UPIPayment(2000), WalletPayment(3000)]:
    print(f"\n── {type(pay).__name__} ──")
    pay.process()
    pay.summary()


# ══ Multi-level Inheritance ═══════════════════
# A → B → C (chain of inheritance)
# Real-life: Vehicle → MotorVehicle → Car

class Vehicle:
    def __init__(self, make, model, year):
        self.make  = make
        self.model = model
        self.year  = year

    def start(self):
        print(f"{self.make} {self.model} engine started.")


class MotorVehicle(Vehicle):
    def __init__(self, make, model, year, engine_cc):
        super().__init__(make, model, year)
        self.engine_cc = engine_cc

    def fuel_status(self, litres):
        print(f"Fuel level: {litres}L")


class ElectricCar(MotorVehicle):
    def __init__(self, make, model, year, battery_kwh):
        super().__init__(make, model, year, engine_cc=0)  # no combustion engine
        self.battery_kwh = battery_kwh

    def start(self):    # override
        print(f"{self.make} {self.model} silently powers on. 🔋")

    def charge_status(self, pct):
        print(f"Battery: {pct}%  ({self.battery_kwh * pct / 100:.1f} kWh remaining)")


tesla = ElectricCar("Tesla", "Model 3", 2024, 82)
tesla.start()
tesla.charge_status(75)
print(tesla.make, tesla.year)   # inherited from Vehicle

# MRO — method resolution order
print(ElectricCar.__mro__)


# ── Key points ────────────────────────────────
# • class Child(Parent): gives Child everything Parent has
# • super() calls the parent class — always use in overridden __init__
# • Method overriding: child version replaces parent version for that type
# • super().method() lets you call the parent version explicitly
# • isinstance(obj, Parent) is True for child objects too (IS-A relationship)
# • Multi-level: A → B → C; each level builds on the previous
