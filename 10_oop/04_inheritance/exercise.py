# ─────────────────────────────────────────────
# Exercises — Inheritance & Method Overriding
# ─────────────────────────────────────────────

# ── Exercise 1: Online Course Platform ───────
# Real-life: Udemy / Coursera-style platform
# Create a base class Course with:
#   __init__(self, title, instructor, duration_hrs, price)
#   method enroll(student_name) → prints enrollment confirmation
#   method certificate_text()  → returns "Certificate of Completion for <title>"
#
# Create subclasses:
#   VideoCourse(Course):
#     extra: num_videos
#     override certificate_text() → adds "Video Course | X videos"
#   LiveCourse(Course):
#     extra: schedule (list of dates as strings)
#     override enroll() → super().enroll() + prints schedule
#     override certificate_text() → adds "Live Instructor-Led"
#   FreeCourse(Course):
#     price is always 0
#     override certificate_text() → returns None (no certificate)
#     override enroll() → prints "Enrolled in FREE course: <title>"
#
# Create one of each, enroll a student, print certificate text.

# --- your code here ---


# ── Exercise 2: Animal Shelter ─────────────────
# Real-life: Pet adoption system
# Create a base class Animal with:
#   __init__(self, name, age, breed)
#   method speak() → prints "..."  (to be overridden)
#   method profile() → prints name, age, breed, and calls speak()
#
# Create subclasses:
#   Dog(Animal):  speak() → "{name} says: Woof!"
#     extra: is_trained (bool)
#     add method fetch()
#   Cat(Animal):  speak() → "{name} says: Meow!"
#     extra: indoor_only (bool)
#   Parrot(Animal): speak() → "{name} says: {phrase}!"
#     extra: phrase (custom thing it says)
#
# Create 2 dogs, 1 cat, 1 parrot.
# Print profiles of all using a loop.
# Use isinstance() to print "Trained: Yes/No" only for Dogs.

# --- your code here ---


# ── Exercise 3: Bank Account Hierarchy ────────
# Real-life: Banking product types
# Create a base class BankAccount with:
#   __init__(self, owner, account_no, balance=0)
#   method deposit(amount)
#   method withdraw(amount)  → checks balance
#   method statement()       → prints balance
#   method annual_benefit()  → prints "Standard account: no benefit"
#
# Create subclasses:
#   SavingsAccount(BankAccount):
#     extra: interest_rate (default 4%)
#     override annual_benefit() → adds interest to balance, prints benefit
#   CurrentAccount(BankAccount):
#     extra: overdraft_limit (default 10000)
#     override withdraw() → allows going below 0 up to overdraft_limit
#     override annual_benefit() → "Current account: no interest"
#   FixedDeposit(BankAccount):
#     extra: tenure_months, fd_rate (default 7%)
#     no withdraw allowed → override to print "Cannot withdraw from FD"
#     override annual_benefit() → computes and prints maturity amount
#
# Create one of each, demonstrate key features, print statements.

# --- your code here ---


# ── Exercise 4: Notification System ──────────
# Real-life: App notification service (email, SMS, push)
# Create a base class Notification with:
#   __init__(self, recipient, message)
#   method send() → prints "Sending notification to <recipient>"
#   method log()  → prints "[LOG] Notification sent via <channel> to <recipient>"
#   property channel → returns "Unknown" (override in subclasses)
#
# Create subclasses:
#   EmailNotification(Notification):
#     extra: subject, sender_email
#     override send() → super().send() + prints email details
#     override channel property → "Email"
#   SMSNotification(Notification):
#     extra: phone_number
#     override send() → super().send() + prints SMS details
#     override channel property → "SMS"
#   PushNotification(Notification):
#     extra: app_name, device_token
#     override send() → super().send() + prints push details
#     override channel property → "Push"
#
# Create one of each, send all, log all.

# --- your code here ---


# ── Exercise 5: Vehicle Insurance ─────────────
# Real-life: Insurance premium calculator
# Create a base class InsurancePolicy with:
#   __init__(self, policy_no, holder_name, vehicle_value)
#   method base_premium() → returns vehicle_value * 0.02
#   method add_ons_cost()  → returns 0 (override in subclasses)
#   method total_premium() → base_premium() + add_ons_cost()
#   method policy_summary() → prints full breakdown
#
# Create subclasses:
#   ThirdPartyPolicy(InsurancePolicy):
#     override base_premium() → vehicle_value * 0.01  (cheaper)
#     add_ons_cost() → 0
#   ComprehensivePolicy(InsurancePolicy):
#     extra: add_ons (list of strings like ["Zero Depreciation", "Roadside Assist"])
#     add_ons_cost() → 500 per add-on
#   ElectricVehiclePolicy(ComprehensivePolicy):
#     extra: battery_value
#     override base_premium() → (vehicle_value + battery_value) * 0.015
#
# Create one of each for a car worth ₹8,00,000, print summaries.

# --- your code here ---


# ─────────────────────────────────────────────
# Expected outputs (for self-check):
# Ex1: Correct certificate text per type; LiveCourse prints schedule; FreeCourse → no cert
# Ex2: Each animal speaks differently; only Dog shows training status
# Ex3: SavingsAccount earns interest; CurrentAccount allows overdraft; FD blocks withdraw
# Ex4: Each notification sends with channel-specific details + logs correctly
# Ex5: Premiums differ per policy type; EV policy includes battery in calculation
# ─────────────────────────────────────────────
