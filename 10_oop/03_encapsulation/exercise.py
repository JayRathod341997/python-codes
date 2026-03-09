# ─────────────────────────────────────────────
# Exercises — Encapsulation
# ─────────────────────────────────────────────

# ── Exercise 1: Secure ATM ────────────────────
# Real-life: ATM / banking app
# Create a class ATM with:
#   __init__(self, account_holder, initial_balance, pin)
#     store pin as __pin (private)
#     store balance as __balance (private)
#   method check_balance(pin) → prints balance if pin matches, else "Wrong PIN"
#   method deposit(amount, pin) → validates pin, validates amount>0, adds to balance
#   method withdraw(amount, pin) → validates pin, checks sufficient funds, deducts
#   method change_pin(old_pin, new_pin) → validates old pin, sets new pin
#     (new_pin must be 4 digits — use a static/private helper to validate)
#
# Simulate: deposit, withdraw, wrong pin attempt, pin change, balance check.

# --- your code here ---


# ── Exercise 2: Employee Salary System ───────
# Real-life: HR / payroll management
# Create a class Employee with:
#   __init__(self, emp_id, name, base_salary)
#     use @property + setter for base_salary:
#       must be > 0; store as private
#   @property salary_after_tax → base_salary * 0.80 (20% tax, read-only)
#   @property annual_ctc       → base_salary * 12 (read-only)
#   method give_raise(pct)     → increases base_salary by pct%
#   method pay_slip()          → prints:
#       Employee ID  : E001
#       Name         : Priya Sharma
#       Base Salary  : ₹80,000.00
#       Tax (20%)    : ₹16,000.00
#       Net Salary   : ₹64,000.00
#       Annual CTC   : ₹9,60,000.00
#
# Create 2 employees, give one a raise, print both pay slips.

# --- your code here ---


# ── Exercise 3: Smart Thermostat ──────────────
# Real-life: IoT home automation
# Create a class Thermostat with:
#   __init__(self, room, current_temp)
#     store temperature as __temperature (private)
#   @property temperature → return __temperature
#   @temperature.setter   → validate: must be between 10 and 35 °C
#   @property mode        → read-only; returns:
#       "Heating" if __temperature < 20
#       "Cooling" if __temperature > 26
#       "Idle"    otherwise
#   method set_schedule(time_str, target_temp) →
#       stores (time_str, target_temp) in a list __schedule
#   method show_schedule() → prints all scheduled settings
#
# Create a thermostat, set valid and invalid temperatures, show schedule.

# --- your code here ---


# ── Exercise 4: Social Media Post ────────────
# Real-life: Instagram / Twitter-like post object
# Create a class Post with:
#   __init__(self, author, content)
#     content stored as __content (private)
#     __likes = 0  (private)
#     __comments = []  (private)
#   @property content → returns __content
#   @content.setter   → content must be non-empty and ≤ 280 chars
#   @property likes   → read-only
#   method like()     → increment __likes
#   method unlike()   → decrement (min 0)
#   method add_comment(user, text) → appends to __comments
#   method display()  → prints the post, likes count, and comments
#
# Create a post, like it multiple times, add comments, edit content, display.

# --- your code here ---


# ── Exercise 5: Hospital Patient Record ──────
# Real-life: Hospital management system
# Create a class PatientRecord with:
#   __init__(self, patient_id, name, dob)
#     blood_pressure stored as __bp (private, default None)
#     __prescriptions = []  (private)
#     __access_log = []     (private, tracks who accessed the record)
#   @property blood_pressure → returns __bp
#   @blood_pressure.setter   → validate format "systolic/diastolic"
#                              both numbers must be > 0
#   method add_prescription(doctor, medication, dosage) →
#       appends to __prescriptions, logs the access
#   method view_record(doctor_name) →
#       logs the access, prints patient info + prescriptions
#   method access_history() → prints who accessed and when (use index as "time")
#
# Create a patient, add prescriptions from 2 doctors, view record, show history.

# --- your code here ---


# ─────────────────────────────────────────────
# Expected outputs (for self-check):
# Ex1: Wrong PIN rejected; deposit/withdraw work; PIN changed; balance shown
# Ex2: Pay slips with correct tax/net/annual calculations
# Ex3: Temp set; ValueError for out-of-range; mode shown; schedule displayed
# Ex4: Post with likes, comments; content validation; 280-char limit enforced
# Ex5: Prescriptions added; access log maintained; record printed
# ─────────────────────────────────────────────
