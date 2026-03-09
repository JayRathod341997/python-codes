# Python Collections — Hands-On Module

Estimated time: ~3 hours
Each file is self-contained and runnable with `python filename.py`

---

## Folder Structure

```
python-collections/
│
├── 01_lists/
│   ├── 01_list_creation.py          # Creating lists — grocery app
│   ├── 02_indexing_slicing.py       # Index & slice — exam results
│   ├── 03_list_methods.py           # append/remove/sort — task manager
│   ├── 04_list_copying.py           # Shallow vs deep copy — timetable
│   ├── 05_sorting.py                # sort() vs sorted() — e-commerce
│   ├── 06_nested_lists.py           # 2D lists — cinema seat booking
│   └── exercises/
│       ├── exercise_01.py           # Food delivery order system
│       └── solutions/solution_01.py
│
├── 02_tuples/
│   ├── 01_tuple_basics.py           # Basics — GPS coordinates
│   ├── 02_packing_unpacking.py      # Packing/unpacking — flight booking
│   ├── 03_immutable_nature.py       # Immutability — bank transactions
│   ├── 04_tuple_use_cases.py        # namedtuple, multi-return, zip
│   └── exercises/
│       ├── exercise_01.py           # Train ticket booking system
│       └── solutions/solution_01.py
│
├── 03_dictionaries/
│   ├── 01_dict_creation.py          # Creating dicts — user profile
│   ├── 02_accessing_values.py       # Access & update — product catalog
│   ├── 03_dict_methods.py           # All methods — grade management
│   ├── 04_iterating_dicts.py        # Iteration patterns — sales analytics
│   ├── 05_nested_dicts.py           # Nested dicts — hospital patients
│   ├── 06_get_items_keys_values.py  # Deep dive — inventory system
│   ├── 07_defaultdict.py            # defaultdict — log analysis
│   └── exercises/
│       ├── exercise_01.py           # Library management system
│       └── solutions/solution_01.py
│
└── 04_sets/
    ├── 01_set_creation.py           # Creating sets — user tags
    ├── 02_set_operations.py         # Operators — friend recommendations
    ├── 03_union_intersection_difference.py  # Applied — skill analysis
    ├── 04_set_methods.py            # Methods — RBAC permissions
    ├── 05_frozen_sets.py            # frozenset — network security
    └── exercises/
        ├── exercise_01.py           # Streaming platform
        └── solutions/solution_01.py
```

---

## Learning Path

| # | Topic | Key Concepts | Real-World Scenario |
|---|-------|-------------|---------------------|
| 1 | List Creation | `[]`, `list()`, comprehension | Grocery app |
| 2 | Indexing & Slicing | `[i]`, `[s:e:step]`, negative index | Exam results |
| 3 | List Methods | append, extend, insert, remove, pop, sort | Task manager |
| 4 | List Copying | shallow vs deep, `copy.deepcopy()` | School timetable |
| 5 | Sorting | `sort()`, `sorted()`, `key=`, multi-key | E-commerce catalog |
| 6 | Nested Lists | 2D grids, `[row][col]` | Cinema booking |
| 7 | Tuple Basics | `()`, index, count, iterate | GPS coordinates |
| 8 | Packing & Unpacking | `a,b = t`, `*rest`, `_` | Flight booking |
| 9 | Immutable Nature | hashable, dict keys, frozenset | Bank records |
| 10 | Tuple Use Cases | namedtuple, multi-return, zip | Named data records |
| 11 | Dict Creation | `{}`, `dict()`, fromkeys, comprehension | User profile |
| 12 | Accessing Values | `[]`, `.get()`, `update()`, `del`, `pop()` | Product catalog |
| 13 | Dict Methods | All 10+ methods | Grade management |
| 14 | Iterating Dicts | keys, values, items, filter, comprehension | Sales analytics |
| 15 | Nested Dicts | deep access, safe traversal, dynamic build | Hospital system |
| 16 | get/items/keys/values | View objects, patterns | Inventory system |
| 17 | defaultdict | list, int, set, dict factories | Log analysis |
| 18 | Set Creation | `{}`, `set()`, comprehension, dedup | User tags |
| 19 | Set Operations | `\|`, `&`, `-`, `^`, subset, superset | Friend suggestions |
| 20 | Union/Intersection/Diff | Applied to real data | Skill gap analysis |
| 21 | Set Methods | add, remove, discard, update, pop | Access control |
| 22 | Frozen Sets | immutable set, hashable, dict key | Network security |

---

## How to Use This Module

1. **Read** the concept file top to bottom
2. **Run** it: `python 01_list_creation.py`
3. **Modify** values and re-run to experiment
4. **Attempt** the exercise without looking at the solution
5. **Compare** your solution with the provided one

---

## Quick Reference

```python
# Lists
lst = [1, 2, 3]          lst.append(4)         lst[1:3]
lst.sort(key=fn)         sorted(lst, reverse=True)

# Tuples
t = (1, 2, 3)            a, b, c = t           a, *rest = t
Point = namedtuple("Point", ["x","y"])

# Dictionaries
d = {"k": "v"}           d.get("k", default)   d.items()
{k:v for k,v in d.items() if condition}        defaultdict(list)

# Sets
s = {1, 2, 3}            s.add(4)              s.discard(99)
A | B   A & B   A - B   A ^ B                  frozenset(s)
```
