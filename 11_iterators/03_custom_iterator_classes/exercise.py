# ─────────────────────────────────────────────
# Exercises — Custom Iterator Classes
# ─────────────────────────────────────────────
import itertools

# ── Exercise 1: EvenNumbers ───────────────────
# Real-life: generating even-indexed items in a data pipeline
# Build an iterator that yields even numbers from 0 up to (not including) limit.

class EvenNumbers:
    def __init__(self, limit):
        pass                        # TODO: store limit, set current = 0

    def __iter__(self):
        pass                        # TODO

    def __next__(self):
        pass                        # TODO: yield 0, 2, 4, ... stop at limit

# --- your code here ---

print(list(EvenNumbers(10)))        # [0, 2, 4, 6, 8]
print(list(EvenNumbers(1)))         # []


# ── Exercise 2: Fibonacci ─────────────────────
# Real-life: generating Fibonacci numbers for a sequence visualiser
# Build a finite Fibonacci iterator that yields the first n numbers.

class Fibonacci:
    def __init__(self, n):
        pass                        # TODO: store n, initialise a=0, b=1, count=0

    def __iter__(self):
        pass

    def __next__(self):
        pass                        # TODO: yield next Fibonacci, stop after n values

# --- your code here ---

print(list(Fibonacci(8)))           # [0, 1, 1, 2, 3, 5, 8, 13]


# ── Exercise 3: OrderIDGenerator ──────────────
# Real-life: e-commerce platform generating unique order IDs
# Build an INFINITE iterator that produces IDs like:
#   ORD-0001, ORD-0002, ORD-0003, …

class OrderIDGenerator:
    def __init__(self):
        pass                        # TODO

    def __iter__(self):
        pass

    def __next__(self):
        pass                        # TODO: formatted string ORD-XXXX

# --- your code here ---

gen = OrderIDGenerator()
for _ in range(5):
    print(next(gen))

# Expected:
# ORD-0001
# ORD-0002
# ORD-0003
# ORD-0004
# ORD-0005


# ── Exercise 4: WordIterator ──────────────────
# Real-life: NLP pre-processing — iterate over words in a sentence
# Build an iterator that splits a sentence and yields one word at a time.

class WordIterator:
    def __init__(self, sentence):
        pass                        # TODO: split sentence into words, store index

    def __iter__(self):
        pass

    def __next__(self):
        pass                        # TODO: return next word, raise StopIteration at end

# --- your code here ---

sentence = "The quick brown fox jumps over the lazy dog"
for word in WordIterator(sentence):
    print(word, end=" ")
print()
# The quick brown fox jumps over the lazy dog


# ── Exercise 5: CircularPlaylist ──────────────
# Real-life: music player that loops through a playlist endlessly
# Build an infinite circular iterator over a list of songs.
# Use itertools.islice to take the first 7 plays.

class CircularPlaylist:
    def __init__(self, songs):
        pass                        # TODO

    def __iter__(self):
        pass

    def __next__(self):
        pass                        # TODO: cycle through songs infinitely

# --- your code here ---

playlist = CircularPlaylist(["Song A", "Song B", "Song C"])
plays    = list(itertools.islice(playlist, 7))
print(plays)

# Expected:
# ['Song A', 'Song B', 'Song C', 'Song A', 'Song B', 'Song C', 'Song A']


# ─────────────────────────────────────────────
# Expected outputs (for self-check):
# Ex1: [0, 2, 4, 6, 8]  |  []
# Ex2: [0, 1, 1, 2, 3, 5, 8, 13]
# Ex3: ORD-0001 to ORD-0005
# Ex4: full sentence word by word
# Ex5: 7 songs cycling A→B→C→A→B→C→A
# ─────────────────────────────────────────────
