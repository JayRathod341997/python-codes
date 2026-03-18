# ─────────────────────────────────────────────────────────────────
# Project 07 — Finance — Banking with Inheritance
# Concepts  : inheritance, super().__init__(), method overriding
# Difficulty: Intermediate
# ─────────────────────────────────────────────────────────────────

# ── Section 1: Base Class BankAccount ──────────────────────────────
class BankAccount:
    """Base class for all bank accounts."""

    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance
        self.account_type = "Generic"

    def deposit(self, amount):
        """Deposit money into account."""
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount
        print(f"  ✓ {self.account_holder} deposited ₹{amount:,.0f} → Balance: ₹{self.balance:,.0f}")

    def withdraw(self, amount):
        """Withdraw money (to be overridden by subclasses)."""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise ValueError(f"Insufficient funds. Balance: ₹{self.balance:,.0f}")
        self.balance -= amount
        print(f"  ✓ {self.account_holder} withdrew ₹{amount:,.0f} → Balance: ₹{self.balance:,.0f}")

    def calculate_interest(self):
        """Calculate and add interest (to be overridden by subclasses)."""
        return 0


# ── Section 2: SavingsAccount (Subclass) ──────────────────────────
class SavingsAccount(BankAccount):
    """Savings account with interest and minimum balance requirement."""

    def __init__(self, account_holder, initial_balance=0):
        super().__init__(account_holder, initial_balance)
        self.account_type = "Savings"
        self.min_balance = 1000
        self.interest_rate = 0.04  # 4% per annum

    def withdraw(self, amount):
        """Override: Check if balance would go below minimum."""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if self.balance - amount < self.min_balance:
            raise ValueError(f"Cannot withdraw. Minimum balance ₹{self.min_balance:,.0f} required. Current: ₹{self.balance:,.0f}")
        self.balance -= amount
        print(f"  ✓ {self.account_holder} withdrew ₹{amount:,.0f} → Balance: ₹{self.balance:,.0f}")

    def calculate_interest(self):
        """Override: Calculate interest at 4% per annum."""
        interest = self.balance * self.interest_rate
        self.balance += interest
        return interest


# ── Section 3: CurrentAccount (Subclass) ──────────────────────────
class CurrentAccount(BankAccount):
    """Current account with unlimited withdrawals, no interest."""

    def __init__(self, account_holder, initial_balance=0):
        super().__init__(account_holder, initial_balance)
        self.account_type = "Current"
        self.monthly_fee = 500

    def withdraw(self, amount):
        """Override: Allow unlimited withdrawals (no minimum balance)."""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise ValueError(f"Insufficient funds. Balance: ₹{self.balance:,.0f}")
        self.balance -= amount
        print(f"  ✓ {self.account_holder} withdrew ₹{amount:,.0f} → Balance: ₹{self.balance:,.0f}")

    def deduct_monthly_fee(self):
        """Deduct monthly maintenance fee."""
        self.balance -= self.monthly_fee
        print(f"  ✗ {self.account_holder}: Monthly fee ₹{self.monthly_fee:,.0f} deducted → Balance: ₹{self.balance:,.0f}")

    def calculate_interest(self):
        """Override: No interest on current account, but deduct fee."""
        self.deduct_monthly_fee()
        return 0


# ── Section 4: FixedDeposit (Subclass) ────────────────────────────
class FixedDeposit(BankAccount):
    """Fixed Deposit with locked-in period and fixed interest."""

    def __init__(self, account_holder, amount, tenure_years=1):
        super().__init__(account_holder, amount)
        self.account_type = "Fixed Deposit"
        self.principal = amount
        self.tenure_years = tenure_years
        self.interest_rate = 0.07  # 7% per annum
        self.maturity_amount = amount * (1 + self.interest_rate * tenure_years)

    def withdraw(self, amount):
        """Override: Can only withdraw at maturity."""
        raise ValueError(f"Cannot withdraw from FD before maturity. Maturity amount: ₹{self.maturity_amount:,.0f}")

    def withdraw_at_maturity(self):
        """Withdraw entire FD amount at maturity."""
        self.balance = self.maturity_amount
        print(f"  ✓ {self.account_holder}: FD matured. Withdrawn ₹{self.balance:,.0f} (Principal: ₹{self.principal:,.0f} + Interest: ₹{self.maturity_amount - self.principal:,.0f})")
        return self.balance

    def calculate_interest(self):
        """Override: FD interest is pre-calculated at maturity."""
        return self.maturity_amount - self.principal


# ── Section 5: Demonstration ───────────────────────────────────────
print("\n" + "="*75)
print("BANKING SYSTEM — ACCOUNT POLYMORPHISM DEMO")
print("="*75)

# Create accounts
saving_account = SavingsAccount("Arun", 5000)
current_account = CurrentAccount("Bhavna", 10000)
fd_account = FixedDeposit("Chirag", 50000, tenure_years=2)

# Create a list with mixed account types (Polymorphism!)
accounts = [saving_account, current_account, fd_account]

# ── Section 6: Operations on Each Account ──────────────────────────
print("\n--- SAVINGS ACCOUNT (Arun) ---")
saving_account.deposit(2000)
saving_account.withdraw(1000)
interest = saving_account.calculate_interest()
print(f"  Interest earned: ₹{interest:,.0f}")

print("\n--- CURRENT ACCOUNT (Bhavna) ---")
current_account.deposit(5000)
current_account.withdraw(3000)
current_account.calculate_interest()

print("\n--- FIXED DEPOSIT (Chirag) ---")
print(f"  Principal: ₹{fd_account.principal:,.0f}")
print(f"  Tenure: {fd_account.tenure_years} year(s)")
print(f"  Interest Rate: {fd_account.interest_rate*100:.0f}% p.a.")
print(f"  Maturity Amount: ₹{fd_account.maturity_amount:,.0f}")
try:
    fd_account.withdraw(10000)
except ValueError as e:
    print(f"  ✗ Error: {e}")

fd_account.withdraw_at_maturity()

# ── Section 7: Summary Using Polymorphism ─────────────────────────
print("\n--- ACCOUNT SUMMARY (Polymorphism) ---")
print(f"{'Account Type':<15} {'Holder':<15} {'Balance':>15} {'Account Type':>15}")
print("─" * 75)

for account in accounts:
    print(f"{account.account_type:<15} {account.account_holder:<15} ₹{account.balance:>14,.0f} {type(account).__name__:>15}")

# ── Section 8: Interest Calculation for All (Polymorphic Call) ─────
print("\n--- ANNUAL INTEREST ACCRUAL (Polymorphic Method Call) ---")
accounts = [saving_account, current_account]  # FD already calculated
total_interest = 0
for account in accounts:
    interest = account.calculate_interest()
    total_interest += interest
    print(f"  {account.account_holder}: ₹{interest:,.0f}")

print(f"\n  Total interest earned: ₹{total_interest:,.0f}")

print("\n" + "="*75 + "\n")

# ── KEY POINTS ──────────────────────────────────────────────────────
# 1. Inheritance allows code reuse: all accounts share deposit/withdraw interface
# 2. super().__init__() calls parent constructor to initialize base attributes
# 3. Method overriding: each subclass provides its own withdraw/calculate_interest
# 4. Polymorphism: calling the same method on different account types yields different behavior
# 5. The list of mixed account types is possible because of inheritance
# 6. Abstract concept: BankAccount defines the "contract"; subclasses fulfill it
# ────────────────────────────────────────────────────────────────────
