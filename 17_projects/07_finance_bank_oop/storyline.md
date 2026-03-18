# Project 07 — Banking with Inheritance

## The Real-Life Problem

A bank has different account types: Savings Accounts (earn interest, limited withdrawals), Current Accounts (no interest, unlimited withdrawals), and Fixed Deposits (locked-in term, fixed interest). Each account has different rules for withdrawals and interest calculation.

Without inheritance, we'd duplicate a lot of code. With inheritance, we model a base BankAccount class and subclass specific account types. Each overrides withdraw() and calculate_interest() to implement their own rules.

## Domain Context

**Industry**: Banking / Finance
**Role**: Bank Software Engineer
**Tools in the real world**: Banking platforms (ICICI, HDFC backends), fintech apps
**Why Python is used here**: Core banking systems use OOP to model account polymorphism.

## The Python Solution Approach

We define:
1. **BankAccount** (base class): account_holder, balance, __init__, withdraw(), calculate_interest()
2. **SavingsAccount** (subclass): withdraw() checks if balance > min_balance; calculate_interest() applies savings rate (4% p.a.)
3. **CurrentAccount** (subclass): withdraw() allows unlimited withdrawals; calculate_interest() returns 0
4. **FixedDeposit** (subclass): withdraw() only after maturity; calculate_interest() applies FD rate (7% p.a.)

We demonstrate polymorphism by creating a mixed list and calling methods on each account.

## Python Concepts You Will Practice

| Concept | Where It Appears |
|---|---|
| Class inheritance | Section 1: Subclasses inherit from BankAccount |
| super().__init__() | Section 1: Subclass initialization |
| Method overriding | Sections 2–4: Each account type overrides withdraw/calculate_interest |
| Polymorphism | Section 5: Calling methods on mixed list of account types |
| Instance variables | Throughout: balance, account_holder |
| Instance methods | Throughout: withdraw(), calculate_interest() |
| Property access | Sections 2–5: account.balance |
| Abstraction | The base class defines the interface; subclasses provide implementation |

## How to Use This Project

1. Read this file to understand banking account types
2. Run `solution.py` and observe polymorphism in action
3. Notice how subclasses override withdraw() and calculate_interest()
4. See how a single list can hold different account types
5. Attempt exercises without looking at the solution
6. Compare your approach with `exercises/solutions/solution_ex.py`

## Extension Ideas

- **Credit Cards**: Add credit limit, interest on unpaid balance
- **Overdraft**: Allow Current Account to go negative (with interest penalty)
- **Interest compounds**: Modify calculate_interest to compound monthly/daily
- **Transaction history**: Track deposits and withdrawals with timestamps

## Real-World Equivalent

This project mimics:
- **Banking core systems**: modeling account types with rules
- **Fintech platforms**: different product types with different behaviors
- **Investment platforms**: modeling different instrument types
