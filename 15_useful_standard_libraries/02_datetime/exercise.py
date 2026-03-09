# ─────────────────────────────────────────────
# Exercises — datetime
# ─────────────────────────────────────────────

from datetime import date, time, datetime, timedelta, timezone

# ── Exercise 1: Age & Birthday Calculator ────
# Real-life: User profile — age verification
# Write a function profile_dates(name, dob_str) where dob_str is "DD/MM/YYYY".
# Print:
#
#   Name            : Jay Rathod
#   Date of Birth   : 15 Aug 1998
#   Age             : 25 years, 4 months, 12 days
#   Days lived      : 9,269
#   Next birthday   : 15 Aug 2025  (in 127 days)
#   Day of birth    : Saturday
#
# Test with at least 2 profiles.

# --- your code here ---


# ── Exercise 2: Meeting Scheduler ────────────
# Real-life: Calendar / scheduling app
# Write a function schedule_slots(start_dt_str, num_slots,
#                                  duration_min=30, gap_min=15):
# Given a start datetime string "YYYY-MM-DD HH:MM", generate
# num_slots meeting time slots.
# Print:
#
#   Slot 1 : 10:00 AM – 10:30 AM  (Mon, 15 Jan 2024)
#   Slot 2 : 10:45 AM – 11:15 AM  (Mon, 15 Jan 2024)
#   Slot 3 : 11:30 AM – 12:00 PM  (Mon, 15 Jan 2024)
#   ...

# --- your code here ---


# ── Exercise 3: Subscription Expiry System ────
# Real-life: SaaS billing / membership
# Write a function subscription_status(start_date_str, plan):
# Plans: {"monthly": 30, "quarterly": 90, "annual": 365} days
# Print:
#
#   Plan       : Annual
#   Started    : 01 Jan 2024
#   Expires    : 31 Dec 2024
#   Status     : Active  (215 days remaining)
#   Renewal on : 01 Jan 2025
#
# If expired, show "Status: Expired (N days ago)"
# Test with a start date that gives an active and an expired subscription.

# --- your code here ---


# ── Exercise 4: Working Hours Calculator ──────
# Real-life: Freelancer invoice / timesheet
# Write a function work_summary(sessions: list[dict]) where each session is:
#   {"date": "2024-01-15", "start": "09:30", "end": "13:45"}
#
# Print:
#   Date         Start   End     Hours
#   ─────────────────────────────────
#   Mon 15 Jan   09:30   13:45   4h 15m
#   Tue 16 Jan   10:00   18:30   8h 30m
#   ─────────────────────────────────
#   Total                        12h 45m
#   Billable (₹1500/hr)          ₹19,125.00

sessions = [
    {"date": "2024-01-15", "start": "09:30", "end": "13:45"},
    {"date": "2024-01-16", "start": "10:00", "end": "18:30"},
    {"date": "2024-01-17", "start": "08:00", "end": "12:00"},
]
RATE_PER_HOUR = 1500

# --- your code here ---


# ── Exercise 5: Time Zone Converter ──────────
# Real-life: Global team stand-up scheduler
# Write a function show_meeting_times(utc_datetime_str, cities: dict):
# cities = {"Mumbai": 5.5, "London": 0, "New York": -5, "Tokyo": 9}
# (offsets in hours from UTC)
#
# Given UTC datetime, show local time for each city:
#
#   Meeting Time Across Cities
#   UTC       : 2024-01-15 10:00
#   ────────────────────────────
#   Mumbai    : 15:30  Mon 15 Jan
#   London    : 10:00  Mon 15 Jan
#   New York  : 05:00  Mon 15 Jan
#   Tokyo     : 19:00  Mon 15 Jan

# --- your code here ---


# ─────────────────────────────────────────────
# Expected outputs (for self-check):
# Ex1: Two formatted profile cards with correct ages/days
# Ex2: N slots with correct start/end times and gaps
# Ex3: Active subscription + expired subscription status
# Ex4: Table with per-session hours + total + billing amount
# Ex5: Correct local times for all four cities
# ─────────────────────────────────────────────
