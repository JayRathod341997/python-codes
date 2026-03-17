# Interview Q&A - Dependency Injection

## Q1. What is Dependency Injection and why is it important?

**A:** DI is passing dependencies to objects instead of having them create their own. Makes code testable (inject mocks), flexible (swap implementations), and loosely coupled.

---

## Q2. What are the main DI patterns?

**A:** Constructor injection (pass via __init__), setter injection (set after creation), interface injection (via injector), factory pattern (factory creates).

---

## Q3. Why is constructor injection preferred?

**A:** Dependencies are visible at a glance, enforced at creation time, and clear what the object needs. Immutable and testable.

---

## Q4. How does DI improve testability?

**A:** Inject mock objects instead of real ones. Test service logic without real database/network. Isolate code under test.

---

## Q5. What's a DI Container and when do you need one?

**A:** Container manages object creation and injection. Useful for complex apps with many interdependent objects. Overkill for simple apps.

---

## Q6. Explain the difference between DI and Service Locator.

**A:** DI explicitly passes dependencies (good). Service Locator hides dependencies with global lookups (bad). DI is clearer.

---

## Q7. How do you avoid circular dependencies?

**A:** Restructure code so dependencies flow one direction. Use interfaces/protocols instead of concrete classes. Consider if design is wrong.

---

## Q8. What's a Protocol and how does it relate to DI?

**A:** Protocol defines expected methods without inheritance. Inject anything matching the protocol. Provides flexibility without tight coupling.

---

## Q9. Explain FastAPI's Depends pattern.

**A:** Function-based DI using Depends(). Inject dependencies into route handlers. FastAPI handles creation and cleanup.

---

## Q10. When should you use a DI framework vs manual injection?

**A:** Manual injection is simpler for small apps. Use framework (dependency-injector, pytest) when managing many objects with complex relationships.

---

## Q11. How do you test code that uses DI?

**A:** Create mock implementations of dependencies and inject them. Test service independently without external resources.

---

## Q12. What's the relationship between DI and Interface Segregation Principle?

**A:** Both encourage depending on abstractions. DI injects abstractions (interfaces/protocols). Clients depend on what they need, not concrete implementations.
