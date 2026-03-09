# ============================================================
#  SOLUTION 1 — Dictionaries
#  Scenario: Library Management System
# ============================================================

from collections import defaultdict

library = {
    "978-0-13-468599-1": {"title": "Clean Code",              "author": "Robert C. Martin",   "genre": "Programming", "available": True,  "copies": 3},
    "978-0-596-51774-8": {"title": "Learning Python",         "author": "Mark Lutz",          "genre": "Programming", "available": True,  "copies": 2},
    "978-0-7432-7356-5": {"title": "The Great Gatsby",        "author": "F. Scott Fitzgerald","genre": "Fiction",     "available": False, "copies": 1},
    "978-0-7432-7357-2": {"title": "To Kill a Mockingbird",   "author": "Harper Lee",         "genre": "Fiction",     "available": True,  "copies": 4},
    "978-0-316-76948-0": {"title": "The Catcher in the Rye",  "author": "J.D. Salinger",      "genre": "Fiction",     "available": True,  "copies": 2},
}

# ---- Task 1: Print all ISBNs ----
print("Task 1 — ISBNs:")
for isbn in library.keys():
    print(f"  {isbn}")

# ---- Task 2: Print all titles ----
print("\nTask 2 — Titles:")
for book in library.values():
    print(f"  {book['title']}")

# ---- Task 3: Safe get ----
missing = library.get("978-0-999-99999-9")
print("\nTask 3:", missing if missing else "Book not found")

# ---- Task 4: Borrow "The Great Gatsby" ----
for isbn, book in library.items():
    if book["title"] == "The Great Gatsby":
        book["available"] = False
        book["copies"] -= 1
        break
print("\nTask 4 — Great Gatsby:", library["978-0-7432-7356-5"])

# ---- Task 5: Add new book ----
library["978-0-14-028329-7"] = {
    "title"    : "Animal Farm",
    "author"   : "George Orwell",
    "genre"    : "Fiction",
    "available": True,
    "copies"   : 3,
}
print(f"\nTask 5 — Library now has {len(library)} books")

# ---- Task 6: Available books ----
print("\nTask 6 — Available books:")
for book in library.values():
    if book["available"]:
        print(f"  {book['title']} - {book['author']} (copies: {book['copies']})")

# ---- Task 7: Group by genre ----
genre_groups = defaultdict(list)
for book in library.values():
    genre_groups[book["genre"]].append(book["title"])

print("\nTask 7 — By genre:")
for genre, titles in sorted(genre_groups.items()):
    print(f"  [{genre}]")
    for t in titles:
        print(f"    - {t}")

# ---- Task 8: Genre with most books ----
biggest_genre = max(genre_groups, key=lambda g: len(genre_groups[g]))
print(f"\nTask 8 — Most books: '{biggest_genre}' ({len(genre_groups[biggest_genre])} books)")

# ---- Task 9: Title → Author mapping ----
title_author = {book["title"]: book["author"] for book in library.values()}
print("\nTask 9 — Title → Author:")
for title, author in title_author.items():
    print(f"  {title:<35} → {author}")

# ---- Task 10: Books per author ----
author_count = defaultdict(int)
for book in library.values():
    author_count[book["author"]] += 1

print("\nTask 10 — Books per author:")
for author, count in sorted(author_count.items(), key=lambda x: -x[1]):
    print(f"  {author:<25} {count} book(s)")
