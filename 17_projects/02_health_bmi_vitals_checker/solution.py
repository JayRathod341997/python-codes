# ─────────────────────────────────────────────────────────────────
# Project 02 — Health — Patient Vitals Screening
# Concepts  : arithmetic, match/case, nested if/elif, boolean logic
# Difficulty: Beginner/Intermediate
# ─────────────────────────────────────────────────────────────────

# ── Section 1: Patient Data ────────────────────────────────────────
# Real patient vitals from a corporate health camp
# We use multiple data types: int for height/age, float for weight/BP/HR

print("\n" + "="*70)
print("CORPORATE HEALTH SCREENING — VITALS ASSESSMENT")
print("="*70)

# Patient 1: Raj (age 35, healthy)
height_cm_1 = 175
weight_kg_1 = 70
age_1 = 35
sys_bp_1 = 120
dia_bp_1 = 80
heart_rate_1 = 72

# Patient 2: Priya (age 42, overweight)
height_cm_2 = 162
weight_kg_2 = 78
age_2 = 42
sys_bp_2 = 135
dia_bp_2 = 88
heart_rate_2 = 85

# Patient 3: Vikram (age 58, at risk)
height_cm_3 = 168
weight_kg_3 = 92
age_3 = 58
sys_bp_3 = 148
dia_bp_3 = 95
heart_rate_3 = 92

# ── Section 2: BMI Calculation ─────────────────────────────────────
# BMI = weight (kg) / height (m)²
# We convert cm to m by dividing by 100
# In production, you'd read these from an EHR database like Epic or Cerner

def calculate_bmi(height_cm, weight_kg):
    """Compute BMI from height (cm) and weight (kg)."""
    height_m = height_cm / 100
    bmi = weight_kg / (height_m ** 2)
    return bmi

bmi_1 = calculate_bmi(height_cm_1, weight_kg_1)
bmi_2 = calculate_bmi(height_cm_2, weight_kg_2)
bmi_3 = calculate_bmi(height_cm_3, weight_kg_3)

# ── Section 3: BMI Classification using match/case ─────────────────
# ── CONCEPT: match/case (Python 3.10+) ─────────────────────────────
# This is Python's modern pattern-matching alternative to if/elif chains.
# Unlike if/elif, match/case is more readable for multiple categorical matches.
# Each 'case' checks if the value falls into that pattern range.

def classify_bmi(bmi):
    """Classify BMI into health categories."""
    # match/case evaluates the expression once, then tries each case
    match bmi:
        case bmi if bmi < 18.5:
            return "UNDERWEIGHT", "Health risk due to low weight"
        case bmi if bmi < 25:
            return "NORMAL", "Healthy weight range"
        case bmi if bmi < 30:
            return "OVERWEIGHT", "Increased health risk"
        case _:  # Default case (underscore = catch-all)
            return "OBESE", "High health risk — doctor consultation needed"

bmi_cat_1, bmi_msg_1 = classify_bmi(bmi_1)
bmi_cat_2, bmi_msg_2 = classify_bmi(bmi_2)
bmi_cat_3, bmi_msg_3 = classify_bmi(bmi_3)

# ── Section 4: Heart Rate Classification ────────────────────────────
# ── CONCEPT: Age-based Resting Heart Rate Zones ─────────────────────
# For adults, typical resting heart rate is 60–100 bpm.
# However, it varies by age: older adults have lower baseline.
# Age 20–30: 60–100 bpm, Age 31–40: 60–100 bpm, Age 41–50: 60–100 bpm, etc.
# We use nested if/elif to check if HR falls in the normal range for the patient's age.

def classify_heart_rate(heart_rate, age):
    """Classify heart rate as normal or abnormal for the given age."""
    # Simplified age-based ranges
    if age < 30:
        normal_min, normal_max = 60, 100
    elif age < 50:
        normal_min, normal_max = 60, 100
    else:
        normal_min, normal_max = 50, 95  # Older adults tolerate lower HR

    if normal_min <= heart_rate <= normal_max:
        return "NORMAL", f"HR {heart_rate} bpm is normal for age {age}"
    elif heart_rate < normal_min:
        return "LOW", f"HR {heart_rate} bpm is below normal (bradycardia)"
    else:
        return "HIGH", f"HR {heart_rate} bpm is above normal (tachycardia)"

hr_cat_1, hr_msg_1 = classify_heart_rate(heart_rate_1, age_1)
hr_cat_2, hr_msg_2 = classify_heart_rate(heart_rate_2, age_2)
hr_cat_3, hr_msg_3 = classify_heart_rate(heart_rate_3, age_3)

# ── Section 5: Blood Pressure Classification ────────────────────────
# ── CONCEPT: Compound Boolean Logic (and/or) ───────────────────────
# Blood pressure is TWO values: systolic (pressure when heart beats)
# and diastolic (pressure when heart rests between beats).
# For BP to be "normal", BOTH systolic AND diastolic must be in range.
# For BP to be "elevated" or "high", we use OR logic (either/both are off).

def classify_blood_pressure(sys, dia):
    """
    Classify blood pressure using compound boolean logic.

    Guidelines:
    - Normal: Sys < 120 AND Dia < 80
    - Elevated: Sys 120–129 AND Dia < 80
    - Stage 1 High: Sys 130–139 OR Dia 80–89
    - Stage 2 High: Sys >= 140 OR Dia >= 90
    """
    # We use compound boolean conditions (and, or)
    if sys < 120 and dia < 80:
        return "NORMAL", f"BP {sys}/{dia} — good health"
    elif sys <= 129 and dia < 80:
        return "ELEVATED", f"BP {sys}/{dia} — monitor and reduce salt"
    elif (sys >= 130 and sys < 140) or (dia >= 80 and dia < 90):
        return "STAGE 1", f"BP {sys}/{dia} — consult doctor for lifestyle changes"
    else:  # sys >= 140 or dia >= 90
        return "STAGE 2", f"BP {sys}/{dia} — URGENT doctor consultation needed"

bp_cat_1, bp_msg_1 = classify_blood_pressure(sys_bp_1, dia_bp_1)
bp_cat_2, bp_msg_2 = classify_blood_pressure(sys_bp_2, dia_bp_2)
bp_cat_3, bp_msg_3 = classify_blood_pressure(sys_bp_3, dia_bp_3)

# ── Section 6: Overall Risk Assessment ──────────────────────────────
# A patient is flagged for doctor attention if ANY vital is abnormal.
# We use compound OR logic: flag if BMI is abnormal OR BP is high OR HR is abnormal

def assess_risk(bmi_category, bp_category, hr_category):
    """Determine if patient needs doctor attention."""
    # If any vital is abnormal (not "NORMAL"), flag the patient
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

risk_1, issues_1 = assess_risk(bmi_cat_1, bp_cat_1, hr_cat_1)
risk_2, issues_2 = assess_risk(bmi_cat_2, bp_cat_2, hr_cat_2)
risk_3, issues_3 = assess_risk(bmi_cat_3, bp_cat_3, hr_cat_3)

# ── Section 7: Formatted Health Report ──────────────────────────────
def print_patient_report(patient_name, height, weight, age, sys_bp, dia_bp, hr,
                         bmi, bmi_cat, bmi_msg, hr_cat, hr_msg, bp_cat, bp_msg,
                         risk_status, issues):
    """Print a formatted health report for one patient."""
    print(f"\n{patient_name} (Age {age})")
    print("─" * 70)
    print(f"Height: {height} cm | Weight: {weight} kg | BMI: {bmi:.1f} ({bmi_cat})")
    print(f"  → {bmi_msg}")
    print(f"Vitals: HR {hr} bpm ({hr_cat}) | BP {sys_bp}/{dia_bp} ({bp_cat})")
    print(f"  → {hr_msg}")
    print(f"  → {bp_msg}")
    print(f"\nRisk Assessment: {risk_status}")
    if issues:
        for issue in issues:
            print(f"  • {issue}")

print_patient_report("Patient 1: Raj", height_cm_1, weight_kg_1, age_1,
                     sys_bp_1, dia_bp_1, heart_rate_1,
                     bmi_1, bmi_cat_1, bmi_msg_1, hr_cat_1, hr_msg_1,
                     bp_cat_1, bp_msg_1, risk_1, issues_1)

print_patient_report("Patient 2: Priya", height_cm_2, weight_kg_2, age_2,
                     sys_bp_2, dia_bp_2, heart_rate_2,
                     bmi_2, bmi_cat_2, bmi_msg_2, hr_cat_2, hr_msg_2,
                     bp_cat_2, bp_msg_2, risk_2, issues_2)

print_patient_report("Patient 3: Vikram", height_cm_3, weight_kg_3, age_3,
                     sys_bp_3, dia_bp_3, heart_rate_3,
                     bmi_3, bmi_cat_3, bmi_msg_3, hr_cat_3, hr_msg_3,
                     bp_cat_3, bp_msg_3, risk_3, issues_3)

print("\n" + "="*70 + "\n")

# ── KEY POINTS ──────────────────────────────────────────────────────
# 1. Functions encapsulate logic (classify_bmi, classify_blood_pressure)
#    so we can reuse them for multiple patients without duplicating code
# 2. match/case is Python 3.10+ syntax for cleaner pattern matching
#    (older Python versions use if/elif instead)
# 3. Compound boolean logic (and, or) is essential for health checks:
#    BMI is ONE value, but BP is TWO values that must both be checked
# 4. Nested conditions help with age-based thresholds (HR depends on age)
# 5. A patient's overall risk is determined by ANY abnormal vital
#    (we use OR logic to flag if health is compromised)
# ────────────────────────────────────────────────────────────────────
