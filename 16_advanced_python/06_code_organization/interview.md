# Interview Q&A - Code Organization

## Q1. What is SOLID and why is it important?

**A:** SOLID is 5 design principles: Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, Dependency Inversion. They make code maintainable, testable, and flexible.

---

## Q2. Explain Single Responsibility Principle with an example.

**A:** A class should have one reason to change. Bad: User class handling saving, emailing, and validation. Good: Separate User, UserRepository, EmailService, EmailValidator classes.

---

## Q3. How does Dependency Injection improve code?

**A:** Instead of creating dependencies inside a class, pass them as parameters. Makes code testable (inject mocks) and flexible (swap implementations).

---

## Q4. What's the difference between Composition and Inheritance?

**A:** Inheritance is "is-a" (Dog is Animal), Composition is "has-a" (Car has Engine). Composition is more flexible and avoids deep inheritance hierarchies.

---

## Q5. When would you use Factory Pattern?

**A:** When object creation is complex or depends on runtime conditions. Example: PaymentFactory creates CardPayment or WalletPayment based on payment method.

---

## Q6. Explain Strategy Pattern.

**A:** Strategy encapsulates different algorithms in classes. Instead of multiple if-statements, inject the strategy. Example: SortingContext with QuickSort, MergeSort strategies.

---

## Q7. What's the benefit of using Dataclasses?

**A:** Automatic generation of __init__, __repr__, __eq__ methods. Less boilerplate, type hints, and optional validators.

---

## Q8. How do you prevent circular imports?

**A:** Use TYPE_CHECKING for type hints, import inside functions, or restructure code so dependencies flow one direction only.

---

## Q9. What should __all__ contain?

**A:** List of public API (functions, classes, constants) that are part of the module's contract. Hides implementation details.

---

## Q10. How do you structure a Python package?

**A:** models/ for data, services/ for business logic, api/ for routes/controllers, tests/ for tests. Clear separation of concerns.

---

## Q11. When would you use Abstract Base Classes?

**A:** When enforcing a contract that subclasses MUST implement. Example: all payment processors must have pay() and refund() methods.

---

## Q12. What's a God Object and how do you avoid it?

**A:** A class doing too much. Avoid by splitting into smaller classes with single responsibilities. Every class should be easy to understand.
