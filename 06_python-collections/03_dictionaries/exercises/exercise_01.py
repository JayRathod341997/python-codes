# ============================================================
#  EXERCISE 1 — Dictionaries
#  Scenario: Library Management System
# ============================================================

# A library stores books in a dictionary:
# Key = ISBN,  Value = book details dict

library = {
    "978-0-13-468599-1": {
        "title"    : "Clean Code",
        "author"   : "Robert C. Martin",
        "genre"    : "Programming",
        "available": True,
        "copies"   : 3,
    },
    "978-0-596-51774-8": {
        "title"    : "Learning Python",
        "author"   : "Mark Lutz",
        "genre"    : "Programming",
        "available": True,
        "copies"   : 2,
    },
    "978-0-7432-7356-5": {
        "title"    : "The Great Gatsby",
        "author"   : "F. Scott Fitzgerald",
        "genre"    : "Fiction",
        "available": False,
        "copies"   : 1,
    },
    "978-0-7432-7357-2": {
        "title"    : "To Kill a Mockingbird",
        "author"   : "Harper Lee",
        "genre"    : "Fiction",
        "available": True,
        "copies"   : 4,
    },
    "978-0-316-76948-0": {
        "title"    : "The Catcher in the Rye",
        "author"   : "J.D. Salinger",
        "genre"    : "Fiction",
        "available": True,
        "copies"   : 2,
    },
}

# ---- Task 1 ----
# Print all ISBNs (keys) in the library.
# YOUR CODE HERE:


# ---- Task 2 ----
# Print ALL book titles using .values() or .items().
# YOUR CODE HERE:


# ---- Task 3 ----
# Use .get() to safely retrieve the title of ISBN "978-0-999-99999-9"
# (which doesn't exist). Print "Book not found" if missing.
# YOUR CODE HERE:


# ---- Task 4 ----
# A member borrowed "The Great Gatsby" (mark as unavailable, reduce copies by 1).
# Modify the dict accordingly.
# YOUR CODE HERE:


# ---- Task 5 ----
# Add a NEW book to the library:
# ISBN: "978-0-14-028329-7"
# Title: "Animal Farm", Author: "George Orwell",
# Genre: "Fiction", available: True, copies: 3
# YOUR CODE HERE:


# ---- Task 6 ----
# Print only books that are currently AVAILABLE.
# Format: "Title - Author (copies: N)"
# YOUR CODE HERE:


# ---- Task 7 ----
# Group books by genre using a defaultdict(list).
# Print each genre with the list of titles under it.
# YOUR CODE HERE:


# ---- Task 8 ----
# Find the genre with the MOST books.
# Hint: use max() with a key on the grouped dict.
# YOUR CODE HERE:


# ---- Task 9 ----
# Build a new dict mapping book TITLE → AUTHOR
# for all books in the library (using dict comprehension).
# YOUR CODE HERE:


# ---- Task 10 ----
# Count how many books each author has using a defaultdict(int).
# Print each author and their count.
# YOUR CODE HERE:

