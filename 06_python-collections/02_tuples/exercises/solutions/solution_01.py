# ============================================================
#  SOLUTION 1 — Tuples
#  Scenario: Train Ticket Booking System
# ============================================================

from collections import namedtuple

trains = [
    (12001, "Shatabdi Express", "Mumbai", "Pune",    "06:00", 45),
    (12002, "Rajdhani Express", "Delhi",  "Mumbai",  "16:30", 12),
    (12003, "Duronto Express",  "Chennai","Kolkata",  "22:00",  0),
    (12004, "Jan Shatabdi",     "Pune",   "Nashik",  "07:15", 80),
    (12005, "Deccan Queen",     "Mumbai", "Pune",    "17:00",  3),
]

# ---- Task 1: Unpack first train ----
train_no, name, source, destination, departure, seats = trains[0]
print("Task 1:")
print(f"  Train No  : {train_no}")
print(f"  Name      : {name}")
print(f"  From      : {source}")
print(f"  To        : {destination}")
print(f"  Departs   : {departure}")
print(f"  Seats     : {seats}")

# ---- Task 2: Loop with unpacking ----
print("\nTask 2:")
for t_no, t_name, src, dst, dep, seats_avail in trains:
    print(f"  Train {t_no} ({t_name}): {src} → {dst} at {dep} | Seats: {seats_avail}")

# ---- Task 3: Trains with available seats ----
print("\nTask 3 — Available trains:")
available_trains = [t for t in trains if t[5] > 0]
for t in available_trains:
    print(f"  {t[0]} {t[1]} — {t[5]} seats")

# ---- Task 4: Sort by seats descending ----
print("\nTask 4 — Sorted by seats (desc):")
sorted_trains = sorted(trains, key=lambda t: t[5], reverse=True)
for t in sorted_trains:
    print(f"  {t[0]} {t[1]:<22} seats={t[5]}")

# ---- Task 5: Function returning tuple ----
def get_route_info(train_tuple):
    _, _, source, destination, _, _ = train_tuple
    return (source, destination, "journey in progress")

print("\nTask 5:")
route = get_route_info(trains[0])
src, dst, msg = route
print(f"  Route: {src} → {dst} | Status: {msg}")

# ---- Task 6: Dict comprehension ----
train_map = {t[0]: t[1] for t in trains}
print("\nTask 6:", train_map)

# ---- Task 7: Named tuple ----
TrainTicket = namedtuple("TrainTicket", ["pnr", "passenger_name", "train_no", "seat_no", "class_type"])

t1 = TrainTicket(pnr="PNR001", passenger_name="Alice", train_no=12001, seat_no="A12", class_type="1A")
t2 = TrainTicket(pnr="PNR002", passenger_name="Bob",   train_no=12002, seat_no="B07", class_type="2A")

print("\nTask 7:")
for ticket in [t1, t2]:
    print(f"  PNR: {ticket.pnr}  Passenger: {ticket.passenger_name:<8} "
          f"Train: {ticket.train_no}  Seat: {ticket.seat_no}  Class: {ticket.class_type}")

# ---- Task 8: Extended unpacking ----
train_no, *details, seats = trains[0]
print(f"\nTask 8:")
print(f"  Train No : {train_no}")
print(f"  Details  : {details}")
print(f"  Seats    : {seats}")
