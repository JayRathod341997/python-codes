# ─────────────────────────────────────────────
# Working with CSV Files
# csv module — built-in, no install needed
# ─────────────────────────────────────────────

import csv
import os

os.makedirs("output", exist_ok=True)
SAMPLE = "sample.csv"           # make sure sample.csv is in same folder

# ── 1. Read with csv.reader ───────────────────
print("=== csv.reader ===")
with open(SAMPLE, "r", encoding="utf-8", newline="") as f:
    reader = csv.reader(f)
    header = next(reader)       # first row = header
    print("Headers:", header)
    for row in reader:
        print(row)              # list of strings

# ── 2. Read with csv.DictReader ───────────────
# Each row becomes an OrderedDict with header keys
print("\n=== csv.DictReader ===")
with open(SAMPLE, "r", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"  {row['name']:10} age={row['age']}  city={row['city']}")

# ── 3. Filter / process while reading ────────
print("\n=== Filtered read (salary > 70000) ===")
with open(SAMPLE, "r", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    high_earners = [row for row in reader if int(row["salary"]) > 70000]

for p in high_earners:
    print(f"  {p['name']} — ${p['salary']}")

# ── 4. Write with csv.writer ──────────────────
print("\n=== csv.writer ===")
OUTPUT = "output/employees.csv"

data = [
    ["id", "name", "department"],
    [1, "Jay",   "Engineering"],
    [2, "Sara",  "Design"],
    [3, "Alex",  "Marketing"],
]

with open(OUTPUT, "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(data[0])        # write header
    writer.writerows(data[1:])      # write all data rows at once

print(f"Wrote {OUTPUT}")

# ── 5. Write with csv.DictWriter ─────────────
print("\n=== csv.DictWriter ===")
DICT_OUT = "output/products.csv"

products = [
    {"name": "Laptop",  "price": 999.99, "stock": 50},
    {"name": "Mouse",   "price":  29.99, "stock": 200},
    {"name": "Monitor", "price": 349.99, "stock": 30},
]

fields = ["name", "price", "stock"]
with open(DICT_OUT, "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()            # writes header row
    writer.writerows(products)

print(f"Wrote {DICT_OUT}")

# ── 6. Read it back ───────────────────────────
with open(DICT_OUT, "r", encoding="utf-8", newline="") as f:
    for row in csv.DictReader(f):
        print(f"  {row['name']:<10} ${float(row['price']):.2f}")

# ── 7. Handle special cases ───────────────────
print("\n=== Special cases ===")

# Data with commas inside fields — csv handles quoting automatically
tricky = [
    ["product", "description", "price"],
    ["Widget", "A nice, useful widget", 9.99],
    ["Gadget", 'Has "scare quotes"', 14.99],
]

with open("output/tricky.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
    writer.writerows(tricky)

with open("output/tricky.csv", "r", encoding="utf-8", newline="") as f:
    print(f.read())

# ── 8. Custom delimiter (TSV, pipe, etc.) ─────
with open("output/data.tsv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f, delimiter="\t")
    writer.writerow(["col1", "col2", "col3"])
    writer.writerow(["a", "b", "c"])

print("TSV written")

# Cleanup
import shutil
shutil.rmtree("output")
