# ─────────────────────────────────────────────
# Methods — Instance, Class & Static
# ─────────────────────────────────────────────

# ── Three kinds of methods ────────────────────
#
#   Instance method  → works with a specific object  (self)
#   Class method     → works with the class itself   (cls)  @classmethod
#   Static method    → utility; no access to obj/class      @staticmethod


# ══ 1. Instance Methods ═══════════════════════
# • First parameter is always 'self' (the object calling the method)
# • Can read/write instance AND class variables
# • Most common kind
#
# Real-life: Each order at a restaurant belongs to a specific table (object)

class Order:
    def __init__(self, table_no):
        self.table_no = table_no
        self.items    = []          # per-order list

    # instance method — operates on self
    def add_item(self, name, price):
        self.items.append({"name": name, "price": price})
        print(f"  Added: {name}  ₹{price}")

    def total(self):
        return sum(i["price"] for i in self.items)

    def print_bill(self):
        print(f"\n  ── Bill for Table {self.table_no} ──")
        for item in self.items:
            print(f"  {item['name']:20s} ₹{item['price']:.2f}")
        print(f"  {'TOTAL':20s} ₹{self.total():.2f}")

o1 = Order(5)
o1.add_item("Paneer Butter Masala", 320)
o1.add_item("Garlic Naan",          60)
o1.add_item("Mango Lassi",          120)
o1.print_bill()


# ══ 2. Class Methods ══════════════════════════
# • Decorated with @classmethod
# • First parameter is 'cls' (the class itself, not an instance)
# • Cannot access instance variables (no 'self')
# • Common use: alternative constructors (factory methods)
#
# Real-life: Parsing a CSV row to create an Employee object

class Employee:
    company = "TechCorp"

    def __init__(self, name, role, salary):
        self.name   = name
        self.role   = role
        self.salary = salary

    # ── alternative constructor (class method) ──
    @classmethod
    def from_csv(cls, csv_string):
        """Create an Employee from a CSV line: 'Name,Role,Salary'"""
        name, role, salary = csv_string.split(",")
        return cls(name.strip(), role.strip(), float(salary.strip()))

    @classmethod
    def from_dict(cls, data: dict):
        """Create an Employee from a dictionary."""
        return cls(data["name"], data["role"], data["salary"])

    @classmethod
    def change_company(cls, new_name):
        cls.company = new_name

    def info(self):
        print(f"[{Employee.company}] {self.name} | {self.role} | ₹{self.salary:,.0f}")

# Regular construction
e1 = Employee("Priya", "Engineer", 80_000)

# Factory methods — same class, different input formats
e2 = Employee.from_csv("Rahul, Designer, 65000")
e3 = Employee.from_dict({"name": "Sneha", "role": "Manager", "salary": 1_20_000})

e1.info()
e2.info()
e3.info()

Employee.change_company("InnovateTech")
e1.info()   # company name updated for all


# ══ 3. Static Methods ═════════════════════════
# • Decorated with @staticmethod
# • No 'self' or 'cls' parameter
# • Cannot access instance or class data
# • Use for utility/helper functions that logically belong in the class
#
# Real-life: A MathUtils class with helper calculations — no object needed

class TaxCalculator:
    GST_RATE = 0.18

    def __init__(self, product, price):
        self.product = product
        self.price   = price

    # ── static method — pure utility ────────────
    @staticmethod
    def add_gst(amount, rate=0.18):
        """Return amount + GST (no class/instance state needed)."""
        return round(amount * (1 + rate), 2)

    @staticmethod
    def gst_breakdown(amount, rate=0.18):
        """Return (base, tax, total) as a tuple."""
        tax   = round(amount * rate, 2)
        total = round(amount + tax, 2)
        return amount, tax, total

    def final_price(self):
        return TaxCalculator.add_gst(self.price, TaxCalculator.GST_RATE)

# Call static method on the class — no object needed
print(TaxCalculator.add_gst(1000))          # 1180.0
print(TaxCalculator.gst_breakdown(500))     # (500, 90.0, 590.0)

# Can also call on instance (but 'self' is not passed)
item = TaxCalculator("USB Hub", 999)
print(item.final_price())                   # 1178.82
print(item.add_gst(2000))                   # 2360.0


# ══ Comparison Side-by-Side ═══════════════════
#
#   Method type      Decorator        1st param    Accesses
#   ─────────────    ─────────────    ─────────    ──────────────────────
#   Instance         (none)           self         instance + class data
#   Class            @classmethod     cls          class data only
#   Static           @staticmethod    (none)       nothing (pure utility)


# ══ Real-life: Date class with all three ══════
# Real-life: A date utility used in a booking system

class DateUtil:
    DEFAULT_FORMAT = "DD/MM/YYYY"   # class variable

    def __init__(self, day, month, year):
        self.day   = day
        self.month = month
        self.year  = year

    # instance method
    def display(self):
        print(f"{self.day:02d}/{self.month:02d}/{self.year}")

    # class method — alternative constructor
    @classmethod
    def from_string(cls, date_str):
        """Parse DD-MM-YYYY string."""
        d, m, y = map(int, date_str.split("-"))
        return cls(d, m, y)

    # static method — pure validation utility
    @staticmethod
    def is_leap_year(year):
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    @staticmethod
    def days_in_month(month, year):
        days = [0,31,28,31,30,31,30,31,31,30,31,30,31]
        if month == 2 and DateUtil.is_leap_year(year):
            return 29
        return days[month]

d1 = DateUtil(15, 8, 2024)
d1.display()                                    # 15/08/2024

d2 = DateUtil.from_string("26-01-2025")
d2.display()                                    # 26/01/2025

print(DateUtil.is_leap_year(2024))              # True
print(DateUtil.is_leap_year(2023))              # False
print(DateUtil.days_in_month(2, 2024))          # 29 (leap)
print(DateUtil.days_in_month(2, 2023))          # 28


# ── Key points ────────────────────────────────
# • Instance methods  → default; use when you need self (object state)
# • Class methods     → use when you need cls (factory constructors, class state)
# • Static methods    → use when neither self nor cls is needed (utility/helper)
# • All three can be defined in the same class
