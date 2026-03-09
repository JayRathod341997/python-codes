# ============================================================
#  EXERCISE 1 — Tuples
#  Scenario: Train Ticket Booking System
# ============================================================

# A railway booking system stores train journey data as tuples.
# Complete each task below.

# Train record: (train_no, name, source, destination, departure, seats_available)
trains = [
    (12001, "Shatabdi Express", "Mumbai", "Pune",   "06:00", 45),
    (12002, "Rajdhani Express", "Delhi",  "Mumbai", "16:30", 12),
    (12003, "Duronto Express",  "Chennai","Kolkata", "22:00",  0),
    (12004, "Jan Shatabdi",     "Pune",   "Nashik", "07:15", 80),
    (12005, "Deccan Queen",     "Mumbai", "Pune",   "17:00",  3),
]

# ---- Task 1 ----
# Unpack the FIRST train's data into separate variables and print each one.
# YOUR CODE HERE:


# ---- Task 2 ----
# Use a loop and unpacking to print:
# "Train 12001 (Shatabdi Express): Mumbai → Pune at 06:00 | Seats: 45"
# for all trains.
# YOUR CODE HERE:


# ---- Task 3 ----
# Find and print all trains that have seats available (seats > 0).
# YOUR CODE HERE:


# ---- Task 4 ----
# Sort the trains by seats_available in descending order
# and print the sorted list.
# Hint: use sorted() with a key.
# YOUR CODE HERE:


# ---- Task 5 ----
# Write a function get_route_info(train_tuple) that returns a tuple:
#   (source, destination, duration_message)
# where duration_message is just the string "journey in progress".
# Test it on trains[0].
# YOUR CODE HERE:


# ---- Task 6 ----
# Create a dictionary where key = train_no, value = train_name
# using a dict comprehension over the trains list.
# Print the dictionary.
# YOUR CODE HERE:


# ---- Task 7 ----
# Create a named tuple 'TrainTicket' with fields:
#   pnr, passenger_name, train_no, seat_no, class_type
# Create 2 ticket instances and print them.
# YOUR CODE HERE:


# ---- Task 8 ----
# Using extended unpacking, unpack the first train record so that:
#   - train_no gets the first element
#   - last gets the last element  (seats_available)
#   - details gets everything in between as a list
# Print all three.
# YOUR CODE HERE:

