# ─────────────────────────────────────────────
# Useful Standard Libraries — math & random
# ─────────────────────────────────────────────

import math
import random

# ══════════════════════════════════════════════
# math — Mathematical functions
# ══════════════════════════════════════════════

# ── Constants ─────────────────────────────────
print(f"π  = {math.pi}")           # 3.141592653589793
print(f"e  = {math.e}")            # 2.718281828459045
print(f"τ  = {math.tau}")          # 6.283185307179586 (2π)
print(f"∞  = {math.inf}")          # inf
print(f"nan= {math.nan}")          # nan


# ── Rounding & absolute value ─────────────────
print(math.floor(4.9))      # 4   — round down
print(math.ceil(4.1))       # 5   — round up
print(math.trunc(4.9))      # 4   — towards zero
print(math.fabs(-7.5))      # 7.5 — float absolute value


# ── Power & logarithm ─────────────────────────
print(math.sqrt(144))       # 12.0
print(math.pow(2, 10))      # 1024.0  (returns float)
print(math.log(math.e))     # 1.0     (natural log)
print(math.log10(1000))     # 3.0
print(math.log2(1024))      # 10.0
print(math.log(81, 3))      # 4.0     (log base 3)


# ── Trigonometry ──────────────────────────────
# Input in radians; convert with math.radians(degrees)
angle_deg = 45
angle_rad = math.radians(angle_deg)
print(f"sin(45°) = {math.sin(angle_rad):.4f}")    # 0.7071
print(f"cos(45°) = {math.cos(angle_rad):.4f}")    # 0.7071
print(f"tan(45°) = {math.tan(angle_rad):.4f}")    # 1.0
print(f"degrees of π/2 = {math.degrees(math.pi/2)}")  # 90.0


# ── Number theory ─────────────────────────────
print(math.gcd(48, 64))                 # 16
print(math.lcm(4, 6))                   # 12  (Python 3.9+)
print(math.factorial(10))               # 3628800
print(math.comb(10, 3))                 # 120  (combinations nCr)
print(math.perm(10, 3))                 # 720  (permutations nPr)
print(math.isfinite(math.inf))          # False
print(math.isnan(float("nan")))         # True


# ── Hypot & distance ──────────────────────────
# Real-life: GPS distance (flat earth approx), game collision
print(math.hypot(3, 4))                 # 5.0  (√(3²+4²))
print(math.dist([0, 0], [3, 4]))        # 5.0  (Euclidean, Python 3.8+)


# ── Real-life examples ────────────────────────
# Loan EMI
def emi(principal, annual_rate, months):
    r = annual_rate / 12 / 100
    return principal * r * math.pow(1 + r, months) / (math.pow(1 + r, months) - 1)

print(f"EMI: ₹{emi(500_000, 8.5, 60):.2f}")

# Circle sector area (pizza slice)
def sector_area(radius, angle_deg):
    return 0.5 * radius**2 * math.radians(angle_deg)

print(f"Pizza slice area: {sector_area(15, 45):.2f} cm²")

# Signal decibels (audio engineering)
def to_db(power_ratio):
    return 10 * math.log10(power_ratio)

print(f"3dB ≈ power ratio of 2: {to_db(2):.2f} dB")


# ══════════════════════════════════════════════
# random — Pseudo-random number generation
# ══════════════════════════════════════════════

# ── random.seed() — reproducibility ──────────
random.seed(42)      # same seed → same sequence (useful for testing)


# ── Floats ────────────────────────────────────
print(random.random())              # [0.0, 1.0)
print(random.uniform(10, 20))       # float in [10, 20]


# ── Integers ──────────────────────────────────
print(random.randint(1, 6))         # int in [1, 6] inclusive — dice
print(random.randrange(0, 100, 5))  # multiple of 5 in [0, 100)


# ── Sequences ─────────────────────────────────
cards = ["A♠", "K♠", "Q♠", "J♠", "10♠"]

print(random.choice(cards))         # single random pick
print(random.choices(cards, k=3))   # 3 picks WITH replacement
print(random.sample(cards, 3))      # 3 picks WITHOUT replacement

random.shuffle(cards)               # in-place shuffle
print(cards)


# ── Real-life examples ────────────────────────

# OTP generator
def generate_otp(length=6):
    return "".join(random.choices("0123456789", k=length))

print(f"OTP: {generate_otp()}")

# Secure random — use secrets module for security-critical tokens
import secrets
token = secrets.token_hex(16)           # 32 hex chars
print(f"Secure token: {token}")

# Password generator
def generate_password(length=12):
    import string
    chars = string.ascii_letters + string.digits + "!@#$%"
    # secrets.choice is cryptographically secure
    return "".join(secrets.choice(chars) for _ in range(length))

print(f"Password: {generate_password()}")

# Weighted random — e.g. A/B testing split
outcomes = ["variant_A", "variant_B", "control"]
weights  = [0.4, 0.4, 0.2]         # 40% / 40% / 20%
sample   = random.choices(outcomes, weights=weights, k=10)
from collections import Counter
print(Counter(sample))

# Random simulation — coin flip experiment
flips   = [random.choice(["H", "T"]) for _ in range(1000)]
heads   = flips.count("H")
print(f"Heads: {heads}/1000  ({heads/10}%)")   # should be ~50%


# ── Key points ────────────────────────────────
# math:
#   math.sqrt, pow, log, log2, log10, exp
#   math.floor, ceil, trunc, fabs
#   math.sin, cos, tan, radians, degrees
#   math.gcd, lcm, factorial, comb, perm
#   math.pi, math.e, math.inf, math.nan
# random:
#   random.random()          → float [0,1)
#   random.uniform(a,b)      → float [a,b]
#   random.randint(a,b)      → int [a,b] inclusive
#   random.choice(seq)       → one item
#   random.choices(seq, k=n) → n items with replacement
#   random.sample(seq, n)    → n items without replacement
#   random.shuffle(lst)      → in-place shuffle
#   random.seed(n)           → reproducible sequences
#   secrets module           → cryptographically secure random
