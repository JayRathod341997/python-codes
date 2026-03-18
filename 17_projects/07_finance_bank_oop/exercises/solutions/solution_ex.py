# Solutions — Project 07: Banking with Inheritance

class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance
        self.account_type = "Generic"

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0 or amount > self.balance:
            raise ValueError("Invalid withdrawal")
        self.balance -= amount

    def calculate_interest(self):
        return 0

class SavingsAccount(BankAccount):
    def __init__(self, account_holder, initial_balance=0):
        super().__init__(account_holder, initial_balance)
        self.account_type = "Savings"
        self.min_balance = 1000
        self.interest_rate = 0.04

    def calculate_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        return interest

class CurrentAccount(BankAccount):
    def __init__(self, account_holder, initial_balance=0):
        super().__init__(account_holder, initial_balance)
        self.account_type = "Current"
        self.monthly_fee = 500

    def calculate_interest(self):
        self.balance -= self.monthly_fee
        return 0

class StudentAccount(BankAccount):
    def __init__(self, account_holder, initial_balance=0):
        super().__init__(account_holder, initial_balance)
        self.account_type = "Student"
        self.monthly_limit = 10000
        self.monthly_withdrawn = 0

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        
        if self.monthly_withdrawn + amount <= self.monthly_limit:
            self.balance -= amount
            self.monthly_withdrawn += amount
        else:
            excess = (self.monthly_withdrawn + amount) - self.monthly_limit
            fee = excess * 0.01
            self.balance -= amount + fee
            self.monthly_withdrawn += amount

print("\n" + "="*70)
print("EXERCISE 1 SOLUTION: StudentAccount")
print("="*70 + "\n")

s = StudentAccount("Deepak", 20000)
s.withdraw(8000)
s.withdraw(3000)
try:
    s.withdraw(1000)
except ValueError as e:
    print(f"  Fee charged: ₹{1000 * 0.01:.0f}")

print(f"Balance: ₹{s.balance:,.0f}")

print("\n" + "="*70)
print("EXERCISE 2 SOLUTION: Interest Comparison")
print("="*70 + "\n")

accounts = [
    SavingsAccount("Alice", 10000),
    CurrentAccount("Bob", 10000),
]

print("Starting balance: ₹10,000 for all")
print()

for acc in accounts:
    interest = acc.calculate_interest()
    print(f"{acc.account_type:<15}: Interest ₹{interest:>8,.0f} → Balance ₹{acc.balance:>10,.0f}")

fd = FixedDeposit("Charlie", 10000, 1)
fd_interest = fd.calculate_interest()
print(f"{'Fixed Deposit':<15}: Interest ₹{fd_interest:>8,.0f} → Balance ₹{fd.maturity_amount:>10,.0f}")

print("\n" + "="*70)
print("EXERCISE 3 SOLUTION: Transaction Log")
print("="*70 + "\n")

acc = SavingsAccount("Eve", 5000)
transactions = []

# Transaction 1: Deposit 2000
acc.deposit(2000)
transactions.append(("Deposit", 2000, acc.balance))

# Transaction 2: Withdraw 1000
acc.withdraw(1000)
transactions.append(("Withdraw", 1000, acc.balance))

# Transaction 3: Deposit 500
acc.deposit(500)
transactions.append(("Deposit", 500, acc.balance))

# Transaction 4: Withdraw 800
acc.withdraw(800)
transactions.append(("Withdraw", 800, acc.balance))

# Transaction 5: Withdraw 500
acc.withdraw(500)
transactions.append(("Withdraw", 500, acc.balance))

print("Transaction Log:")
print(f"{'#':<3} {'Type':<10} {'Amount':>10} {'Balance':>12}")
print("─" * 40)

running_balance = 5000
for i, (t_type, amount, balance) in enumerate(transactions, 1):
    print(f"{i:<3} {t_type:<10} ₹{amount:>9,.0f} ₹{balance:>11,.0f}")

expected_balance = 5000 + 2000 - 1000 + 500 - 800 - 500
print(f"\nFinal Balance: ₹{acc.balance:,.0f}")
print(f"Expected:     ₹{expected_balance:,.0f}")
print(f"Verification: {'✓ PASS' if acc.balance == expected_balance else '✗ FAIL'}")

print("\n" + "="*70 + "\n")

class FixedDeposit(BankAccount):
    def __init__(self, account_holder, amount, tenure_years=1):
        super().__init__(account_holder, amount)
        self.principal = amount
        self.tenure_years = tenure_years
        self.interest_rate = 0.07
        self.maturity_amount = amount * (1 + self.interest_rate * tenure_years)

    def calculate_interest(self):
        return self.maturity_amount - self.principal
