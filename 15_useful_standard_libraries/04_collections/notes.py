# ─────────────────────────────────────────────
# Useful Standard Libraries — collections
# ─────────────────────────────────────────────

from collections import (
    Counter, defaultdict, OrderedDict,
    deque, namedtuple, ChainMap
)

# ══════════════════════════════════════════════
# Counter — count elements in an iterable
# ══════════════════════════════════════════════
# Real-life: word frequency, vote counting, inventory

# From an iterable
word_counts = Counter("mississippi".split())
# Better: count letters
letter_counts = Counter("mississippi")
print(letter_counts)
# Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})

# Most common
print(letter_counts.most_common(3))    # [('i',4), ('s',4), ('p',2)]

# From a list — vote tally
votes = ["Alice", "Bob", "Alice", "Carol", "Bob", "Alice", "Bob", "Alice"]
tally = Counter(votes)
print(tally)
winner = tally.most_common(1)[0]
print(f"Winner: {winner[0]} with {winner[1]} votes")

# Arithmetic on counters
stock_a = Counter({"apples": 10, "bananas": 5, "oranges": 3})
sold    = Counter({"apples":  4, "bananas": 5, "oranges": 1})
remaining = stock_a - sold
print(remaining)    # Counter({'apples': 6, 'oranges': 2})

# Update — add more counts
stock_a.update({"apples": 20, "grapes": 8})
print(stock_a)


# ══════════════════════════════════════════════
# defaultdict — dict with auto-created default values
# ══════════════════════════════════════════════
# Real-life: grouping, graph adjacency lists, index building

# Group students by grade (without defaultdict you need .setdefault or if checks)
students = [
    ("Alice", "A"), ("Bob", "B"), ("Carol", "A"),
    ("Dave", "C"),  ("Eve",  "B"), ("Frank","A"),
]

by_grade = defaultdict(list)
for name, grade in students:
    by_grade[grade].append(name)

print(dict(by_grade))
# {'A': ['Alice','Carol','Frank'], 'B': ['Bob','Eve'], 'C': ['Dave']}

# defaultdict(int) — word frequency without missing-key errors
text = "the quick brown fox jumps over the lazy dog the"
freq = defaultdict(int)
for word in text.split():
    freq[word] += 1

print(sorted(freq.items(), key=lambda x: -x[1])[:3])
# [('the', 3), ('quick', 1), ...]

# defaultdict(set) — unique tags per article
article_tags = defaultdict(set)
events = [
    ("article1", "python"), ("article1", "programming"),
    ("article2", "python"), ("article2", "web"),
    ("article1", "tips"),
]
for article, tag in events:
    article_tags[article].add(tag)
print(dict(article_tags))


# ══════════════════════════════════════════════
# deque — double-ended queue
# ══════════════════════════════════════════════
# Real-life: browser history, undo/redo, sliding window, task queue
# O(1) append/pop from BOTH ends (list.insert(0) is O(n))

history = deque(maxlen=5)       # keeps last 5 items only
for page in ["home", "products", "cart", "checkout", "confirm", "receipt"]:
    history.append(page)
print(history)  # deque(['products','cart','checkout','confirm','receipt'])

# Stack (LIFO)
stack = deque()
stack.append("task1")
stack.append("task2")
stack.append("task3")
print(stack.pop())              # task3 — last in, first out

# Queue (FIFO)
queue = deque()
queue.append("req1")
queue.append("req2")
queue.append("req3")
print(queue.popleft())          # req1 — first in, first out

# appendleft / extendleft
notifications = deque()
notifications.appendleft("Alert: Server down")
notifications.appendleft("Alert: High CPU")
print(notifications)

# Sliding window average
def sliding_avg(data, window):
    d = deque(maxlen=window)
    avgs = []
    for x in data:
        d.append(x)
        avgs.append(sum(d) / len(d))
    return avgs

prices = [100, 102, 98, 105, 110, 108, 115]
print(sliding_avg(prices, 3))


# ══════════════════════════════════════════════
# namedtuple — tuple with field names
# ══════════════════════════════════════════════
# Real-life: lightweight record / value object — more readable than plain tuple

Point   = namedtuple("Point",   ["x", "y"])
Employee= namedtuple("Employee",["name", "dept", "salary"])
Color   = namedtuple("Color",   ["r", "g", "b"], defaults=[255])  # b defaults to 255

p = Point(3, 4)
print(f"Point: ({p.x}, {p.y})")
print(f"Distance from origin: {(p.x**2 + p.y**2)**0.5:.2f}")

emp = Employee("Alice", "Engineering", 85000)
print(f"{emp.name} works in {emp.dept}, earns ₹{emp.salary:,}")

# Still a tuple — supports index access and unpacking
x, y = p
print(x, y)

# Convert to dict
print(emp._asdict())

# Real-life: CSV row as named record
import csv, io
data = "Alice,28,72500\nBob,35,95000\n"
Row = namedtuple("Row", ["name", "age", "salary"])
for row in csv.reader(io.StringIO(data)):
    r = Row(*row)
    print(f"{r.name} age {r.age} earns {r.salary}")


# ══════════════════════════════════════════════
# OrderedDict — dict that remembers insertion order
# ══════════════════════════════════════════════
# Note: Since Python 3.7+, regular dict also maintains order.
# OrderedDict is still useful for its move_to_end() and popitem().

cache = OrderedDict()
for key, val in [("a", 1), ("b", 2), ("c", 3)]:
    cache[key] = val

cache.move_to_end("a")          # move "a" to the end
print(list(cache))              # ['b', 'c', 'a']

cache.move_to_end("b", last=False)  # move "b" to the front
print(list(cache))              # ['b', 'c', 'a']

# LRU cache implementation (simplified)
class LRUCache:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.cap   = capacity
    def get(self, key):
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]
    def put(self, key, val):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = val
        if len(self.cache) > self.cap:
            self.cache.popitem(last=False)  # evict oldest

lru = LRUCache(3)
lru.put("a", 1); lru.put("b", 2); lru.put("c", 3)
print(lru.get("a"))     # 1  (moves a to end)
lru.put("d", 4)         # evicts "b" (oldest unused)
print(lru.get("b"))     # -1


# ── Key points ────────────────────────────────
# Counter        — count items; arithmetic; most_common
# defaultdict    — auto-create missing keys; use for grouping
# deque          — O(1) both-end ops; maxlen for sliding window
# namedtuple     — readable tuple with field names; lightweight record
# OrderedDict    — ordered dict with move_to_end/popitem; useful for LRU
# ChainMap       — look up keys across multiple dicts in order
