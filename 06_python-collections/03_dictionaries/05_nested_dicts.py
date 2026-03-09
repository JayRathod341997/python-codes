# ============================================================
#  NESTED DICTIONARIES
#  Real-world context: Hospital patient management system
# ============================================================

# ============================================================
#  Creating nested dicts
# ============================================================

patients = {
    "P001": {
        "name"    : "Alice Kumar",
        "age"     : 34,
        "blood_type": "O+",
        "contact" : {
            "phone": "9876543210",
            "email": "alice@example.com",
            "address": {
                "city"   : "Mumbai",
                "state"  : "Maharashtra",
                "pincode": "400001",
            }
        },
        "diagnoses": ["Hypertension", "Diabetes Type 2"],
        "vitals"   : {"bp": "120/80", "sugar": 105, "weight": 62},
    },
    "P002": {
        "name"    : "Bob Sharma",
        "age"     : 52,
        "blood_type": "A+",
        "contact" : {
            "phone": "9123456789",
            "email": "bob@example.com",
            "address": {"city": "Delhi", "state": "Delhi", "pincode": "110001"}
        },
        "diagnoses": ["Back Pain"],
        "vitals"   : {"bp": "130/85", "sugar": 90, "weight": 78},
    },
}

# ============================================================
#  Accessing nested values (chained keys)
# ============================================================

print("=== Accessing Nested Values ===")

# Level 1
print("Patient name    :", patients["P001"]["name"])

# Level 2
print("Phone number    :", patients["P001"]["contact"]["phone"])

# Level 3
print("City            :", patients["P001"]["contact"]["address"]["city"])

# List inside dict
print("First diagnosis :", patients["P001"]["diagnoses"][0])

# Numeric value inside nested dict
print("Blood sugar     :", patients["P001"]["vitals"]["sugar"])

# ============================================================
#  Safe access with .get() for nested
# ============================================================

print("\n=== Safe Nested Access ===")

def safe_get(d, *keys, default=None):
    """Safely traverse nested dicts with multiple keys."""
    for key in keys:
        if isinstance(d, dict):
            d = d.get(key, default)
        else:
            return default
    return d

print("Email  :", safe_get(patients, "P001", "contact", "email"))
print("Missing:", safe_get(patients, "P001", "insurance", "policy_no", default="N/A"))

# ============================================================
#  Modifying nested values
# ============================================================

print("\n=== Modifying Nested Values ===")

# Update a vital sign
patients["P001"]["vitals"]["bp"] = "118/78"
print("Updated BP:", patients["P001"]["vitals"]["bp"])

# Add a new diagnosis
patients["P001"]["diagnoses"].append("Obesity")
print("Diagnoses:", patients["P001"]["diagnoses"])

# Add a new nested field
patients["P001"]["insurance"] = {
    "provider"  : "HealthCare Plus",
    "policy_no" : "HC-2024-001",
    "coverage"  : 500000,
}
print("Insurance added:", patients["P001"]["insurance"]["provider"])

# ============================================================
#  Iterating nested dicts
# ============================================================

print("\n=== Patient Summary Report ===")
print(f"{'ID':<6}  {'Name':<18}  {'Age':>4}  {'Blood':>5}  {'City':<12}  Diagnoses")
print("-" * 70)

for pid, info in patients.items():
    city   = info["contact"]["address"]["city"]
    diags  = ", ".join(info["diagnoses"])
    print(f"{pid:<6}  {info['name']:<18}  {info['age']:>4}  "
          f"{info['blood_type']:>5}  {city:<12}  {diags}")

# ============================================================
#  Building nested dicts programmatically
# ============================================================

print("\n=== Building Nested Dict Dynamically ===")

# Department → Employee → Details
company = {}
raw_data = [
    ("Engineering", "Alice",  95000, "Senior"),
    ("Engineering", "Bob",    72000, "Junior"),
    ("Marketing",   "Carol",  68000, "Senior"),
    ("Marketing",   "Dave",   55000, "Junior"),
    ("HR",          "Eve",    60000, "Senior"),
]

for dept, name, salary, level in raw_data:
    if dept not in company:
        company[dept] = {}
    company[dept][name] = {"salary": salary, "level": level}

# Print the structure
for dept, employees in company.items():
    print(f"\n  [{dept}]")
    for name, details in employees.items():
        print(f"    {name:<8} ₹{details['salary']:,}  ({details['level']})")

# ============================================================
#  KEY POINTS
#  - Nest with d[k1][k2][k3] or d[k1].get(k2, {}).get(k3)
#  - Use helper function for deep safe access
#  - Build dynamically using setdefault or 'if key not in'
#  - Great for config files, JSON responses, hierarchical data
# ============================================================
