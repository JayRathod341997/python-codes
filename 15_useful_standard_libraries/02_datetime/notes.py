# ─────────────────────────────────────────────
# Useful Standard Libraries — datetime
# ─────────────────────────────────────────────

from datetime import date, time, datetime, timedelta, timezone
import datetime as dt

# ══════════════════════════════════════════════
# date — calendar date (year, month, day)
# ══════════════════════════════════════════════

today = date.today()
print(f"Today    : {today}")               # 2024-01-15
print(f"Year     : {today.year}")
print(f"Month    : {today.month}")
print(f"Day      : {today.day}")
print(f"Weekday  : {today.weekday()}")     # 0=Mon … 6=Sun
print(f"isoformat: {today.isoformat()}")   # '2024-01-15'

# Construct a specific date
dob = date(1995, 8, 15)
print(f"DoB: {dob}")

# Date arithmetic
delta = today - dob
print(f"Age in days: {delta.days}")
print(f"Age in years: {delta.days // 365}")

# Next birthday
this_year_bday = dob.replace(year=today.year)
if this_year_bday < today:
    next_bday = dob.replace(year=today.year + 1)
else:
    next_bday = this_year_bday
print(f"Days until next birthday: {(next_bday - today).days}")


# ══════════════════════════════════════════════
# time — time of day (hour, minute, second, microsecond)
# ══════════════════════════════════════════════

t = time(14, 30, 45)
print(f"Time   : {t}")              # 14:30:45
print(f"Hour   : {t.hour}")
print(f"Minute : {t.minute}")

# Store-open check
def is_store_open(check_time):
    opens  = time(9, 0)
    closes = time(21, 0)
    return opens <= check_time <= closes

print(is_store_open(time(10, 30)))  # True
print(is_store_open(time(22, 0)))   # False


# ══════════════════════════════════════════════
# datetime — date + time combined
# ══════════════════════════════════════════════

now = datetime.now()
print(f"Now    : {now}")
print(f"UTC now: {datetime.utcnow()}")

# Construct
dt_obj = datetime(2024, 1, 15, 14, 30, 0)
print(f"Custom : {dt_obj}")

# Components
print(f"Date part: {now.date()}")
print(f"Time part: {now.time()}")

# ── strftime — datetime → string ──────────────
# Real-life: Formatting timestamps in reports / logs

formats = [
    ("%Y-%m-%d",           "ISO date"),
    ("%d/%m/%Y",           "DD/MM/YYYY"),
    ("%d %b %Y",           "Human date"),
    ("%I:%M %p",           "12-hour time"),
    ("%d %b %Y %H:%M:%S", "Full datetime"),
    ("%A, %d %B %Y",       "Full verbose"),
]
for fmt, label in formats:
    print(f"  {label:20s}: {now.strftime(fmt)}")

# Common format codes:
# %Y=4-digit year  %m=month(01-12)  %d=day(01-31)
# %H=hour(00-23)   %M=minute        %S=second
# %I=hour(01-12)   %p=AM/PM
# %A=weekday name  %B=month name    %a=short weekday  %b=short month


# ── strptime — string → datetime ──────────────
# Real-life: Parse dates from user input / CSV / API

raw_dates = [
    ("2024-01-15",          "%Y-%m-%d"),
    ("15/01/2024",          "%d/%m/%Y"),
    ("Jan 15, 2024",        "%b %d, %Y"),
    ("15 January 2024 14:30", "%d %B %Y %H:%M"),
]
for raw, fmt in raw_dates:
    parsed = datetime.strptime(raw, fmt)
    print(f"  '{raw}' → {parsed}")


# ══════════════════════════════════════════════
# timedelta — duration / time difference
# ══════════════════════════════════════════════

# Real-life: Subscription expiry, delivery estimates, meeting scheduling

one_week  = timedelta(weeks=1)
one_month = timedelta(days=30)
two_hours = timedelta(hours=2)

print(f"One week from now : {now + one_week}")
print(f"30 days from now  : {now + one_month}")
print(f"2 hours ago       : {now - two_hours}")

# Duration between two datetimes
order_placed  = datetime(2024, 1, 10, 9, 0, 0)
order_shipped = datetime(2024, 1, 13, 14, 30, 0)
duration = order_shipped - order_placed
print(f"Processing time: {duration.days} days {duration.seconds // 3600} hours")

# OTP / token expiry
otp_created = datetime.now()
otp_expires = otp_created + timedelta(minutes=10)
print(f"OTP valid until: {otp_expires.strftime('%H:%M:%S')}")


# ══════════════════════════════════════════════
# timezone-aware datetimes
# ══════════════════════════════════════════════
# Real-life: Global apps that must handle multiple time zones

utc_now = datetime.now(tz=timezone.utc)
print(f"UTC: {utc_now}")

# IST = UTC+5:30
IST = timezone(timedelta(hours=5, minutes=30))
ist_now = utc_now.astimezone(IST)
print(f"IST: {ist_now.strftime('%d %b %Y %H:%M %Z')}")


# ── Key points ────────────────────────────────
# date(y, m, d)              — calendar date, no time
# time(H, M, S)              — time of day, no date
# datetime(y,m,d,H,M,S)      — date + time
# timedelta(days, hours, ...) — duration, supports +/- with datetimes
# datetime.now()             — current local datetime
# datetime.utcnow()          — current UTC datetime
# strftime(fmt)              — datetime → formatted string
# datetime.strptime(s, fmt)  — string → datetime
# timezone(timedelta(...))   — create timezone object
