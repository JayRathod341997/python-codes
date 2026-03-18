# Solutions — Project 11: Generators

from itertools import islice

print("\n" + "="*70)
print("EXERCISE 1 SOLUTION: Generator & Filter")
print("="*70 + "\n")

transactions = [
    {"id": 1, "amount": 3000},
    {"id": 2, "amount": 8000},
    {"id": 3, "amount": 4500},
    {"id": 4, "amount": 12000},
    {"id": 5, "amount": 2000},
]

def transaction_gen(trans):
    for t in trans:
        yield t

def filter_amount(gen, threshold):
    for t in gen:
        if t["amount"] > threshold:
            yield t

filtered = filter_amount(transaction_gen(transactions), 5000)
print("Transactions > ₹5000:")
for t in filtered:
    print(f"  ID {t['id']}: ₹{t['amount']:,.0f}")

print("\n" + "="*70)
print("EXERCISE 2 SOLUTION: Risk Score Pipeline")
print("="*70 + "\n")

def score_risk(gen):
    for t in gen:
        score = 0
        if t["amount"] > 1000:
            score += 10
        if t["amount"] > 5000:
            score += 20
        t["risk"] = score
        yield t

scored = score_risk(transaction_gen(transactions))
high_risk = (t for t in scored if t["risk"] >= 20)

print("High-risk transactions (score >= 20):")
for t in islice(high_risk, 5):
    print(f"  ID {t['id']}: ₹{t['amount']:,.0f}, Risk: {t['risk']}")

print("\n" + "="*70 + "\n")
