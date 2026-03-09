# ============================================================
# Reference vs Copy
# ============================================================
# Assignment creates a REFERENCE (alias), not a copy.
# To get independent copies, you must explicitly copy.
#
# Shallow copy: copies the outer object, but nested objects
#               are still shared.
# Deep copy:    copies everything, including nested objects.
# ============================================================

import copy

print("=" * 55)
print("1. REFERENCE (alias) — no copy")
print("=" * 55)

original = [1, 2, 3]
alias = original            # both point to same list

alias.append(4)
print(f"original: {original}")  # [1, 2, 3, 4] — changed!
print(f"alias:    {alias}")
print(f"Same object: {original is alias}")

print("\n" + "=" * 55)
print("2. SHALLOW COPY — 3 ways")
print("=" * 55)

data = [1, 2, 3]
copy1 = data.copy()         # list method
copy2 = list(data)          # list constructor
copy3 = data[:]             # slice syntax

copy1.append(99)
print(f"data:  {data}")     # unchanged
print(f"copy1: {copy1}")
print(f"copy2: {copy2}")
print(f"copy3: {copy3}")
print(f"data is copy1: {data is copy1}")    # False

print("\n--- Shallow copy limitation (nested objects) ---")
nested = [[1, 2], [3, 4], [5, 6]]
shallow = nested.copy()

shallow[0].append(99)       # modifies the SAME inner list!
print(f"nested:  {nested}")     # [[1, 2, 99], [3, 4], [5, 6]] ← changed!
print(f"shallow: {shallow}")    # [[1, 2, 99], [3, 4], [5, 6]]

shallow.append([7, 8])      # outer list is independent
print(f"\nnested (after outer change):  {nested}")   # still 3 items
print(f"shallow (after outer change): {shallow}")   # 4 items

print("\n" + "=" * 55)
print("3. DEEP COPY — fully independent")
print("=" * 55)

nested2 = [[1, 2], [3, 4], [5, 6]]
deep = copy.deepcopy(nested2)

deep[0].append(99)          # inner list is independent now
print(f"nested2: {nested2}")    # [[1, 2], [3, 4], [5, 6]] ← unchanged!
print(f"deep:    {deep}")       # [[1, 2, 99], [3, 4], [5, 6]]

print("\n" + "=" * 55)
print("4. DICT COPIES")
print("=" * 55)

config = {"host": "localhost", "port": 5432, "options": {"timeout": 30}}

ref = config                    # reference
shallow_dict = config.copy()    # shallow copy
deep_dict = copy.deepcopy(config)

config["host"] = "production"
config["options"]["timeout"] = 60

print(f"ref['host']:          {ref['host']}")           # production
print(f"shallow_dict['host']: {shallow_dict['host']}")  # localhost (top-level copied)
print(f"deep_dict['host']:    {deep_dict['host']}")     # localhost

print(f"ref options timeout:          {ref['options']['timeout']}")          # 60
print(f"shallow_dict options timeout: {shallow_dict['options']['timeout']}")  # 60 (nested shared!)
print(f"deep_dict options timeout:    {deep_dict['options']['timeout']}")     # 30 (fully independent)

print("\n--- Summary ---")
print("reference   → same object (id identical)")
print("shallow copy → new outer object, shared inner objects")
print("deep copy   → new everything, fully independent")
