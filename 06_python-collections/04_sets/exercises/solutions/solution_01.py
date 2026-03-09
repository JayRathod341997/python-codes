# ============================================================
#  SOLUTION 1 — Sets
#  Scenario: Streaming Platform
# ============================================================

user_watched = {
    "alice" : {"Inception", "Dark", "Money Heist", "Breaking Bad", "Ozark"},
    "bob"   : {"Dark", "Stranger Things", "Money Heist", "The Crown", "Ozark"},
    "carol" : {"Breaking Bad", "Better Call Saul", "Ozark", "Dark", "Mindhunter"},
    "dave"  : {"Inception", "Interstellar", "Tenet", "Dark", "Arrival"},
}

# ---- Task 1: Alice AND Bob both watched ----
mutual_ab = user_watched["alice"] & user_watched["bob"]
print("Task 1 — Alice & Bob both watched:", mutual_ab)

# ---- Task 2: All unique titles combined ----
all_titles = set()
for titles in user_watched.values():
    all_titles |= titles
print("\nTask 2 — All unique titles:", sorted(all_titles))
print("         Total:", len(all_titles))

# ---- Task 3: Alice watched, Bob hasn't (recommend to Bob) ----
recommend_to_bob = user_watched["alice"] - user_watched["bob"]
print("\nTask 3 — Recommend to Bob:", recommend_to_bob)

# ---- Task 4: Alice OR Bob but NOT both ----
alice_or_bob_exclusive = user_watched["alice"] ^ user_watched["bob"]
print("\nTask 4 — Symmetric diff (Alice ^ Bob):", alice_or_bob_exclusive)

# ---- Task 5: Is Carol's list a subset of Alice+Bob combined? ----
alice_and_bob = user_watched["alice"] | user_watched["bob"]
is_subset = user_watched["carol"].issubset(alice_and_bob)
print(f"\nTask 5 — Carol's watchlist ⊆ (Alice ∪ Bob)? {is_subset}")
if not is_subset:
    missing = user_watched["carol"] - alice_and_bob
    print(f"         Carol watched these exclusively: {missing}")

# ---- Task 6: Deduplicate new releases ----
new_releases = [
    "Dark", "Squid Game", "Squid Game", "Dark",
    "The Witcher", "Bridgerton", "The Witcher", "Lupin"
]
unique_releases = set(new_releases)
print("\nTask 6 — Unique new releases:", unique_releases)
print("         Duplicates removed:", len(new_releases) - len(unique_releases))

# ---- Task 7: Recommendations for Alice ----
def get_recommendations(user, user_watched):
    others = {u: t for u, t in user_watched.items() if u != user}
    # Titles watched by at least 2 other users
    from collections import Counter
    count = Counter()
    for titles in others.values():
        count.update(titles)
    popular_by_others = {title for title, c in count.items() if c >= 2}
    # Remove what the user already watched
    return popular_by_others - user_watched[user]

alice_recs = get_recommendations("alice", user_watched)
print("\nTask 7 — Recommendations for Alice:", alice_recs)

# ---- Task 8: frozenset as dict key ----
premium_titles = frozenset({"Dark", "Money Heist", "Breaking Bad"})
pricing = {premium_titles: 199}
print("\nTask 8 — Premium plan price: ₹", pricing[premium_titles])

# ---- Task 9: Common with ALL other users ----
def common_with_all(user, user_watched):
    others = [t for u, t in user_watched.items() if u != user]
    result = others[0].copy()
    for titles in others[1:]:
        result &= titles
    return result & user_watched[user]

common = common_with_all("alice", user_watched)
print("\nTask 9 — Alice's titles in common with ALL others:", common)

# ---- Task 10: Modify Alice's watchlist ----
user_watched["alice"].add("Squid Game")
user_watched["alice"].discard("Ozark")
user_watched["alice"].discard("NonExistentShow")   # no error
print("\nTask 10 — Alice's final watchlist:", sorted(user_watched["alice"]))
