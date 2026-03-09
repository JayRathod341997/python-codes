# ─────────────────────────────────────────────
# Exercises — Nested Conditions
# ─────────────────────────────────────────────

# ── Exercise 1: Hotel Room Booking ───────────
# Real-life: Hotel reservation system
# Rules:
#   - Must be 18+ to book
#   - If 18+, check room availability (is_available = True/False)
#   - If available, check payment status ("paid" | "pending")
#     - "paid"    → "Booking confirmed. Room {room_number} assigned."
#     - "pending" → "Room held for 15 mins. Complete payment."
#   - If not available → "No rooms available. Join waitlist?"

guest_age    = 25
is_available = True
payment      = "paid"
room_number  = 304

# --- your code here ---


# ── Exercise 2: Job Application Filter ───────
# Real-life: HR screening system
# Requirements:
#   - Minimum degree: "bachelor" or "master" or "phd"
#   - If qualified degree:
#       - Experience >= 2 years → "Shortlisted for interview"
#       - Experience < 2 years and has_internship → "Shortlisted (fresher track)"
#       - Experience < 2 years and no internship  → "Not enough experience"
#   - If degree is "high_school" or "diploma" → "Minimum qualification not met"

degree        = "bachelor"
experience    = 1           # years
has_internship = True

# --- your code here ---


# ── Exercise 3: Parental Control System ──────
# Real-life: Streaming app content filter
# content_rating: "U" | "UA" | "A" | "S" (adult/restricted)
# Rules:
#   - Age < 13: only "U" allowed
#   - Age 13–17:
#       - "U" and "UA" allowed
#       - "A" or "S" → "Parental approval needed"
#   - Age 18+: all content allowed except "S" requires subscription
#     - has_subscription True  → allowed
#     - has_subscription False → "Subscribe to watch this content"

viewer_age       = 16
content_rating   = "A"
has_subscription = False

# --- your code here ---


# ── Exercise 4: Smart Irrigation System ──────
# Real-life: IoT agriculture controller
# Rules:
#   - If soil is dry (soil_moisture < 30):
#       - If it is raining → "Rain detected. Skipping irrigation."
#       - Else if tank level > 20% → "Irrigating field..."
#       - Else → "Tank empty! Send alert to farmer."
#   - If soil is moist (30–70) → "Soil moisture OK. No irrigation needed."
#   - If soil is wet (> 70) → "Field over-irrigated. Check drainage."

soil_moisture = 20      # percentage
is_raining    = False
tank_level    = 45      # percentage

# --- your code here ---


# ─────────────────────────────────────────────
# Expected outputs:
# Ex1: Booking confirmed. Room 304 assigned.
# Ex2: Shortlisted (fresher track)
# Ex3: Parental approval needed
# Ex4: Irrigating field...
# ─────────────────────────────────────────────
