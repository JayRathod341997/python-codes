# ─────────────────────────────────────────────
# complex — Complex Number Type
# ─────────────────────────────────────────────

# ── Creating complex numbers ─────────────────
c1 = 3 + 4j         # j (not i) is the imaginary unit
c2 = complex(2, -5) # complex(real, imag)
c3 = 5j             # purely imaginary

print(type(c1))     # <class 'complex'>
print(c1)           # (3+4j)
print(c2)           # (2-5j)

# ── Accessing parts ───────────────────────────
print(c1.real)      # 3.0  ← always float
print(c1.imag)      # 4.0  ← always float

# ── Arithmetic ───────────────────────────────
print(c1 + c2)      # (5-1j)
print(c1 - c2)      # (1+9j)
print(c1 * c2)      # (26-7j)
print(c1 / c2)      # complex division

# No < > comparisons — complex numbers have no ordering
# print(c1 > c2)    # TypeError!

# ── Conjugate ────────────────────────────────
print(c1.conjugate())   # (3-4j)  — flips sign of imaginary part

# ── Magnitude (absolute value) ────────────────
import math
print(abs(c1))          # 5.0  — sqrt(3² + 4²) = 5

# ── cmath — math for complex numbers ──────────
import cmath

print(cmath.sqrt(-1))       # 1j
print(cmath.sqrt(-16))      # 4j
print(cmath.phase(c1))      # angle in radians
print(cmath.polar(c1))      # (magnitude, angle)

r, theta = cmath.polar(c1)
print(cmath.rect(r, theta)) # back to rectangular form

# ── Practical note ───────────────────────────
# Complex numbers are used in:
# - signal processing (FFT)
# - electrical engineering
# - quantum computing simulations
