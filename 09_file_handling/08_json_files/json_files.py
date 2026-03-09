# ─────────────────────────────────────────────
# Working with JSON Files
# json module — built-in, no install needed
# ─────────────────────────────────────────────

import json
import os

os.makedirs("output", exist_ok=True)

# ── JSON ↔ Python type mapping ────────────────
# JSON           Python
# object    →    dict
# array     →    list
# string    →    str
# number    →    int / float
# true/false →   True / False
# null      →    None

# ── 1. Load from file — json.load() ──────────
print("=== json.load() ===")
with open("sample.json", "r", encoding="utf-8") as f:
    data = json.load(f)             # file → Python dict/list

print(type(data))                   # <class 'dict'>
print(data["total"])                # 3
print(data["users"][0]["name"])     # Alice

for user in data["users"]:
    status = "active" if user["active"] else "inactive"
    print(f"  {user['name']:10} ({user['age']}) — {status}")

# ── 2. Parse JSON string — json.loads() ───────
print("\n=== json.loads() ===")    # loads = load string
json_string = '{"name": "Jay", "score": 98.5, "passed": true}'
obj = json.loads(json_string)
print(obj)
print(obj["passed"])    # True (Python bool, not string)

# ── 3. Write to file — json.dump() ───────────
print("\n=== json.dump() ===")
config = {
    "app_name": "MyApp",
    "version": "1.0.0",
    "debug": False,
    "db": {
        "host": "localhost",
        "port": 5432
    },
    "allowed_hosts": ["127.0.0.1", "localhost"]
}

with open("output/config.json", "w", encoding="utf-8") as f:
    json.dump(config, f, indent=4)          # indent=4 for pretty print

print("Wrote config.json")

# ── 4. Serialize to string — json.dumps() ─────
print("\n=== json.dumps() ===")    # dumps = dump to string
raw = json.dumps(config)
print("Compact:", raw[:60] + "...")

pretty = json.dumps(config, indent=2)
print("\nPretty:\n", pretty)

# ── 5. Formatting options ─────────────────────
data_to_write = {"z": 3, "a": 1, "m": 2}

# sort_keys — alphabetical key order
print(json.dumps(data_to_write, sort_keys=True))

# separators — compact with no extra spaces
print(json.dumps(data_to_write, separators=(",", ":")))

# ensure_ascii=False — keep Unicode characters
text = {"greeting": "こんにちは", "emoji": "❤"}
print(json.dumps(text, ensure_ascii=False))

# ── 6. Handle types JSON can't serialize ──────
from datetime import datetime, date

def json_serializer(obj):
    """Custom serializer for types json can't handle."""
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError(f"Not serializable: {type(obj)}")

event = {
    "name": "Conference",
    "date": date(2025, 6, 15),
    "created_at": datetime.now(),
}

serialized = json.dumps(event, default=json_serializer, indent=2)
print("\nWith custom serializer:\n", serialized)

# ── 7. Update / patch a JSON file ────────────
CONFIG_FILE = "output/settings.json"

# Create initial
with open(CONFIG_FILE, "w", encoding="utf-8") as f:
    json.dump({"theme": "light", "lang": "en"}, f, indent=2)

# Read → modify → write back
with open(CONFIG_FILE, "r", encoding="utf-8") as f:
    settings = json.load(f)

settings["theme"] = "dark"
settings["notifications"] = True

with open(CONFIG_FILE, "w", encoding="utf-8") as f:
    json.dump(settings, f, indent=2)

with open(CONFIG_FILE, "r", encoding="utf-8") as f:
    print("\nUpdated settings:")
    print(f.read())

# ── 8. Handle JSON errors ─────────────────────
bad_jsons = [
    '{"name": "Jay",}',     # trailing comma (invalid JSON)
    "{'key': 'value'}",     # single quotes (invalid JSON)
    "",                     # empty string
]

for s in bad_jsons:
    try:
        json.loads(s)
    except json.JSONDecodeError as e:
        print(f"JSONDecodeError: {e.msg} at line {e.lineno} col {e.colno}")

# Cleanup
import shutil
shutil.rmtree("output")
