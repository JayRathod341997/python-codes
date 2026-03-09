# ─────────────────────────────────────────────
# Exercises — OOP Basics
# ─────────────────────────────────────────────

# ── Exercise 1: Library Book ──────────────────
# Real-life: Library management system
# Create a class Book with:
#   __init__(self, title, author, pages)
#   a method summary() that prints:
#       "Title  : Python Crash Course"
#       "Author : Eric Matthes"
#       "Pages  : 544"
# Create 3 Book objects and call summary() on each.

# --- your code here ---


# ── Exercise 2: Movie Ticket Booking ─────────
# Real-life: Multiplex booking system
# Create a class MovieTicket with:
#   class variable  : gst_rate = 0.18
#   __init__(self, movie, seat_type, base_price)
#     seat_type options: "standard", "premium", "recliner"
#   method final_price() → returns base_price + 18% GST
#   method receipt() → prints a formatted ticket receipt
#
# Create tickets:
#   "Interstellar", "premium",  350
#   "Inception",    "standard", 200
#   "Dune",         "recliner", 600
# Call receipt() on all three.

# --- your code here ---


# ── Exercise 3: Vehicle Fleet ─────────────────
# Real-life: Cab aggregator (Ola/Uber) fleet tracker
# Create a class Vehicle with:
#   class variable  : total_vehicles = 0  (auto-increments on each __init__)
#   __init__(self, vehicle_id, driver, type_)
#     type_ options: "mini", "sedan", "suv"
#   instance variable: is_available = True  (set in __init__)
#   method assign_ride(passenger) → sets is_available=False, prints assignment
#   method complete_ride()        → sets is_available=True, prints completion
#   method status()               → prints vehicle info + availability
#
# Create 3 vehicles, assign rides to 2, complete 1 ride, print status of all.

# --- your code here ---


# ── Exercise 4: Student Grade Book ───────────
# Real-life: School/college management system
# Create a class Student with:
#   __init__(self, name, roll_no)
#   method add_marks(subject, marks) → stores in a dict self.marks
#   method percentage()  → returns average of all marks
#   method grade()       → returns "A+" / "A" / "B" / "C" / "F"
#                          (≥90 / ≥80 / ≥70 / ≥50 / <50)
#   method report_card() → prints formatted report
#
# Create 2 students, add 5 subjects each, print report cards.

# --- your code here ---


# ── Exercise 5: Parking Lot ───────────────────
# Real-life: Mall parking management
# Create a class ParkingLot with:
#   class variable  : rate_per_hour = 50  (₹ per hour)
#   __init__(self, name, total_slots)
#   method park(vehicle_no)      → occupies a slot, records entry time (use int counter)
#   method unpark(vehicle_no, hours) → frees slot, prints bill
#   method lot_status()          → prints slots used / total, list of parked vehicles
#
# Simulate: create lot with 5 slots, park 3 vehicles, unpark 1, show status.

# --- your code here ---


# ─────────────────────────────────────────────
# Expected outputs (for self-check):
# Ex1: 3 book summaries printed
# Ex2: Receipts showing base + GST + total for each ticket
# Ex3: 3 vehicles tracked; 2 assigned, 1 completed; status shows availability
# Ex4: 2 report cards with subjects, marks, %, grade
# Ex5: Parking bill for unparked vehicle; status shows 2 occupied / 5 total
# ─────────────────────────────────────────────
