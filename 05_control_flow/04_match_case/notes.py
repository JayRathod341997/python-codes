# ─────────────────────────────────────────────
# match-case  (Python 3.10+)
# Structural Pattern Matching
# ─────────────────────────────────────────────

# ── What is it? ──────────────────────────────
# match-case is Python's equivalent of switch-case in other languages,
# but far more powerful — it can match values, types, sequences,
# mappings, and even destructure objects.

# ── Syntax ───────────────────────────────────
# match subject:
#     case pattern1:
#         ...
#     case pattern2:
#         ...
#     case _:         ← wildcard (default)
#         ...

# ── 1. Matching literal values ───────────────
# Real-life: HTTP status code handler
status_code = 404

match status_code:
    case 200:
        print("200 OK — Request successful.")
    case 201:
        print("201 Created — Resource created.")
    case 400:
        print("400 Bad Request — Check your input.")
    case 401:
        print("401 Unauthorized — Login required.")
    case 403:
        print("403 Forbidden — Access denied.")
    case 404:
        print("404 Not Found — Resource doesn't exist.")
    case 500:
        print("500 Internal Server Error — Try later.")
    case _:
        print(f"Unknown status code: {status_code}")

# ── 2. Matching strings ───────────────────────
# Real-life: Chatbot command router
command = "/help"

match command:
    case "/start":
        print("Bot started. Type /help for commands.")
    case "/help":
        print("Commands: /start, /stop, /status, /help")
    case "/stop":
        print("Bot stopped.")
    case "/status":
        print("Bot is running normally.")
    case _:
        print(f"Unknown command: {command}")

# ── 3. OR patterns with | ────────────────────
# Real-life: Day-type classifier
day = "Saturday"

match day:
    case "Saturday" | "Sunday":
        print(f"{day}: Weekend — offices closed.")
    case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
        print(f"{day}: Weekday — working hours.")
    case _:
        print("Invalid day.")

# ── 4. Matching sequences (lists/tuples) ─────
# Real-life: GPS coordinates parser
coordinates = (28.7041, 77.1025)    # (lat, lon)

match coordinates:
    case (0, 0):
        print("Origin — null island.")
    case (lat, 0):
        print(f"On the prime meridian, latitude {lat}")
    case (0, lon):
        print(f"On the equator, longitude {lon}")
    case (lat, lon):
        print(f"Location → Lat: {lat}, Lon: {lon}")

# ── 5. Matching with guard (if clause) ───────
# Real-life: Temperature alert levels
temp = 38.9

match temp:
    case t if t < 36.0:
        print(f"Hypothermia risk: {t}°C")
    case t if t <= 37.5:
        print(f"Normal: {t}°C")
    case t if t <= 39.0:
        print(f"Mild fever: {t}°C — Rest and hydrate.")
    case t if t <= 40.5:
        print(f"High fever: {t}°C — See a doctor!")
    case t:
        print(f"Dangerous: {t}°C — Emergency!")

# ── 6. Matching dictionaries (mappings) ───────
# Real-life: API payload routing
request = {"method": "POST", "endpoint": "/users"}

match request:
    case {"method": "GET", "endpoint": endpoint}:
        print(f"Fetching data from {endpoint}")
    case {"method": "POST", "endpoint": endpoint}:
        print(f"Creating resource at {endpoint}")
    case {"method": "DELETE", "endpoint": endpoint}:
        print(f"Deleting resource at {endpoint}")
    case _:
        print("Unsupported request format.")

# ── Key points ───────────────────────────────
# • Requires Python 3.10+  (check: python --version)
# • case _ is the wildcard — always matches, put it last
# • Unlike switch in C/Java, match does NOT fall through
# • Guards (if ...) add extra conditions inside a case
# • Can destructure sequences and dicts — very powerful
# • match-case works on value identity and structure, not just equality
