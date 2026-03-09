# ============================================================
#  EXERCISE 1 — Sets
#  Scenario: Streaming Platform (like Netflix/Spotify)
# ============================================================

# Users and the content they have watched/listened to
user_watched = {
    "alice" : {"Inception", "Dark", "Money Heist", "Breaking Bad", "Ozark"},
    "bob"   : {"Dark", "Stranger Things", "Money Heist", "The Crown", "Ozark"},
    "carol" : {"Breaking Bad", "Better Call Saul", "Ozark", "Dark", "Mindhunter"},
    "dave"  : {"Inception", "Interstellar", "Tenet", "Dark", "Arrival"},
}

# ---- Task 1 ----
# Find all titles watched by BOTH Alice AND Bob.
# (use intersection)
# YOUR CODE HERE:


# ---- Task 2 ----
# Find all unique titles watched across ALL users combined.
# (use union)
# YOUR CODE HERE:


# ---- Task 3 ----
# Find titles Alice watched that Bob has NOT watched yet.
# (these are titles to recommend to Bob)
# YOUR CODE HERE:


# ---- Task 4 ----
# Find titles watched by Alice OR Bob, but NOT both.
# (symmetric difference)
# YOUR CODE HERE:


# ---- Task 5 ----
# Check if Carol's watchlist is a subset of
# the combined watchlist of Alice and Bob.
# Print True or False with an explanation.
# YOUR CODE HERE:


# ---- Task 6 ----
# The following list has duplicate titles.
# Use a set to deduplicate and print the unique titles.
new_releases = [
    "Dark", "Squid Game", "Squid Game", "Dark",
    "The Witcher", "Bridgerton", "The Witcher", "Lupin"
]
# YOUR CODE HERE:


# ---- Task 7 ----
# Build a 'recommended' set for each user:
# titles watched by at least 2 OTHER users, but NOT by this user.
# Print recommendations for Alice only.
# YOUR CODE HERE:


# ---- Task 8 ----
# Create a frozenset of "premium_titles" = {"Dark", "Money Heist", "Breaking Bad"}
# Use it as a dictionary key mapping to a price: 199.
# Look it up and print the price.
# YOUR CODE HERE:


# ---- Task 9 ----
# Write a function  common_with_all(user, user_watched)
# that returns the set of titles the given user has in common
# with EVERY other user.
# Test it with "alice".
# YOUR CODE HERE:


# ---- Task 10 ----
# Add "Squid Game" to Alice's watchlist using .add()
# Then remove "Ozark" using discard().
# Try to discard "NonExistentShow" safely (should not raise an error).
# Print Alice's final watchlist.
# YOUR CODE HERE:

