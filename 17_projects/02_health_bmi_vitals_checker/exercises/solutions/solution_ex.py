# ───────────────────────────────────────────────────────────────
# Solutions — Project 02: Patient Vitals Screening
# ───────────────────────────────────────────────────────────────

print("\n" + "="*70)
print("EXERCISE 1 SOLUTION: Anita's Vitals Assessment")
print("="*70 + "\n")

# ── Exercise 1 Solution ────────────────────────────────────────────
def calculate_bmi(height_cm, weight_kg):
    height_m = height_cm / 100
    return weight_kg / (height_m ** 2)

def classify_bmi(bmi):
    match bmi:
        case bmi if bmi < 18.5:
            return "UNDERWEIGHT", "Health risk due to low weight"
        case bmi if bmi < 25:
            return "NORMAL", "Healthy weight range"
        case bmi if bmi < 30:
            return "OVERWEIGHT", "Increased health risk"
        case _:
            return "OBESE", "High health risk — doctor consultation needed"

def classify_heart_rate(heart_rate, age):
    if age < 30:
        normal_min, normal_max = 60, 100
    elif age < 50:
        normal_min, normal_max = 60, 100
    else:
        normal_min, normal_max = 50, 95

    if normal_min <= heart_rate <= normal_max:
        return "NORMAL", f"HR {heart_rate} bpm is normal for age {age}"
    elif heart_rate < normal_min:
        return "LOW", f"HR {heart_rate} bpm is below normal"
    else:
        return "HIGH", f"HR {heart_rate} bpm is above normal"

def classify_blood_pressure(sys, dia):
    if sys < 120 and dia < 80:
        return "NORMAL", f"BP {sys}/{dia} — good health"
    elif sys <= 129 and dia < 80:
        return "ELEVATED", f"BP {sys}/{dia} — monitor and reduce salt"
    elif (sys >= 130 and sys < 140) or (dia >= 80 and dia < 90):
        return "STAGE 1", f"BP {sys}/{dia} — consult doctor for lifestyle changes"
    else:
        return "STAGE 2", f"BP {sys}/{dia} — URGENT doctor consultation needed"

def assess_risk(bmi_category, bp_category, hr_category):
    abnormal_vitals = []
    if bmi_category != "NORMAL":
        abnormal_vitals.append(f"BMI ({bmi_category})")
    if bp_category not in ["NORMAL", "ELEVATED"]:
        abnormal_vitals.append(f"BP ({bp_category})")
    if hr_category != "NORMAL":
        abnormal_vitals.append(f"HR ({hr_category})")

    if abnormal_vitals:
        return "⚠ NEEDS DOCTOR CONSULTATION", abnormal_vitals
    else:
        return "✓ ALL VITALS NORMAL", []

# Anita's data
height_cm = 165
weight_kg = 72
age = 28
sys_bp = 118
dia_bp = 76
heart_rate = 78

bmi = calculate_bmi(height_cm, weight_kg)
bmi_cat, bmi_msg = classify_bmi(bmi)
hr_cat, hr_msg = classify_heart_rate(heart_rate, age)
bp_cat, bp_msg = classify_blood_pressure(sys_bp, dia_bp)
risk_status, issues = assess_risk(bmi_cat, bp_cat, hr_cat)

print(f"Patient: Anita (Age {age})")
print("─" * 70)
print(f"Height: {height_cm} cm | Weight: {weight_kg} kg | BMI: {bmi:.1f} ({bmi_cat})")
print(f"  → {bmi_msg}")
print(f"Vitals: HR {heart_rate} bpm ({hr_cat}) | BP {sys_bp}/{dia_bp} ({bp_cat})")
print(f"  → {hr_msg}")
print(f"  → {bp_msg}")
print(f"\nRisk Assessment: {risk_status}")
if issues:
    for issue in issues:
        print(f"  • {issue}")

print("\n" + "="*70)
print("EXERCISE 2 SOLUTION: 5 Employees Health Screening")
print("="*70 + "\n")

# ── Exercise 2 Solution ────────────────────────────────────────────
employees = [
    ("Suresh", 180, 75, 40, 128, 82, 68),
    ("Maya", 158, 58, 31, 110, 70, 65),
    ("Arjun", 172, 95, 52, 145, 92, 88),
    ("Neha", 170, 64, 25, 115, 75, 72),
    ("Rahim", 175, 88, 60, 152, 98, 96),
]

needs_doctor = 0

print("Individual Assessments:")
print("─" * 70)

for name, height, weight, age, sys, dia, hr in employees:
    bmi = calculate_bmi(height, weight)
    bmi_cat, _ = classify_bmi(bmi)
    hr_cat, _ = classify_heart_rate(hr, age)
    bp_cat, _ = classify_blood_pressure(sys, dia)
    risk_status, issues = assess_risk(bmi_cat, bp_cat, hr_cat)

    # Check if this employee needs doctor consultation
    if "NEEDS DOCTOR" in risk_status:
        needs_doctor += 1
        flag = "⚠"
    else:
        flag = "✓"

    print(f"{flag} {name:8} | BMI {bmi:5.1f} ({bmi_cat:10}) | BP {sys:3}/{dia} ({bp_cat:8}) | HR {hr:3} ({hr_cat:6})")

print("─" * 70)
print(f"\nSUMMARY: {needs_doctor} out of {len(employees)} employees need doctor consultation")

print("\n" + "="*70)
print("EXERCISE 3 SOLUTION: Age-Based Assessment (Same BMI, Different Ages)")
print("="*70 + "\n")

# ── Exercise 3 Solution ────────────────────────────────────────────
# Both patients have the same height, weight, HR, and BP
# But they have different ages

patient_a = ("Patient A", 170, 73.5, 25, 120, 78, 68)
patient_b = ("Patient B", 170, 73.5, 65, 120, 78, 68)

for name, height, weight, age, sys, dia, hr in [patient_a, patient_b]:
    bmi = calculate_bmi(height, weight)
    bmi_cat, bmi_msg = classify_bmi(bmi)
    hr_cat, hr_msg = classify_heart_rate(hr, age)
    bp_cat, bp_msg = classify_blood_pressure(sys, dia)

    print(f"{name} (Age {age})")
    print("─" * 70)
    print(f"Height: {height} cm | Weight: {weight} kg | BMI: {bmi:.1f} ({bmi_cat})")
    print(f"HR: {hr} bpm | BP {sys}/{dia}")
    print(f"\nAssessment:")
    print(f"  BMI: {bmi_cat} — {bmi_msg}")
    print(f"  HR:  {hr_cat} — {hr_msg}")
    print(f"  BP:  {bp_cat} — {bp_msg}")
    print()

print("KEY INSIGHT:")
print("─" * 70)
print("Both patients have IDENTICAL:")
print("  • BMI (26.2) — both OVERWEIGHT")
print("  • Blood Pressure (120/78) — both NORMAL")
print("  • Heart Rate value (68 bpm)")
print()
print("BUT their HR assessment differs by AGE:")
print("  • Patient A (age 25): 68 bpm is NORMAL for their age (60-100 range)")
print("  • Patient B (age 65): 68 bpm is NORMAL for their age (50-95 range)")
print()
print("This shows that health assessment must be CONTEXT-AWARE (age-dependent).")
print("The same vital value can be 'normal' or 'abnormal' depending on patient age.")

print("\n" + "="*70 + "\n")
