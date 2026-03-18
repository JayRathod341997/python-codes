# ───────────────────────────────────────────────────────────────
# Exercises — Project 02: Patient Vitals Screening
# ───────────────────────────────────────────────────────────────

# ── Exercise 1: Classify a Single Patient's Vitals ────────────────
# Real-life: A new patient, Anita (age 28), walks into the clinic.
# Her measurements: height 165 cm, weight 72 kg, HR 78 bpm, BP 118/76
#
# Task: Compute her BMI, classify it, evaluate her heart rate and BP,
#       and determine if she needs a doctor consultation.
#
# Requirements:
#   - Use the BMI formula: bmi = weight / (height_in_meters)²
#   - Classify BMI using match/case or if/elif logic
#   - Check heart rate against age-normal range
#   - Check blood pressure using compound boolean logic
#   - Determine overall risk (use OR logic: if ANY vital is abnormal → flag)
#
# Hint: Follow the structure of solution.py, copy the functions,
#       then call them with Anita's data.

# --- your code here ---




# ── Exercise 2: Assess Multiple Patients and Count Abnormalities ────
# Real-life: Dr. Mehta screened 5 employees. You must categorize each
# and count how many need doctor consultations.
#
# Employee data (name, height_cm, weight_kg, age, sys_bp, dia_bp, hr):
#   - Suresh: 180, 75, 40, 128, 82, 68
#   - Maya: 158, 58, 31, 110, 70, 65
#   - Arjun: 172, 95, 52, 145, 92, 88
#   - Neha: 170, 64, 25, 115, 75, 72
#   - Rahim: 175, 88, 60, 152, 98, 96
#
# Task: For each employee, compute and classify vitals, then print
#       a summary: "X out of 5 employees need doctor consultation"
#
# Requirements:
#   - Use a loop or multiple function calls
#   - Count patients flagged for doctor attention
#   - Print a summary table or list
#
# Hint: Create a list of patient tuples, loop through, and track the count.

# --- your code here ---




# ── Exercise 3: BMI vs Age Analysis ────────────────────────────────
# Real-life: Two patients have the same BMI (25.5) but different ages.
# How does age affect their health assessment (especially heart rate)?
#
# Patient A: age 25, height 170 cm, weight 73.5 kg, HR 68 bpm, BP 120/78
# Patient B: age 65, height 170 cm, weight 73.5 kg, HR 68 bpm, BP 120/78
#
# Task: Assess both patients. Explain how age changes the assessment.
#
# Requirements:
#   - Compute BMI for both (should be identical)
#   - Evaluate heart rate for both using age-based zones
#   - Show that both BMI and BP are identical, but HR assessment differs
#   - Print comparison: "Patient A: HR assessment is X, Patient B: HR assessment is Y"
#
# Hint: Heart rate norms vary by age. Younger people can have higher resting HR.
#       Older adults may have lower resting HR. The same HR value may be
#       "normal" for one age but "abnormal" for another.

# --- your code here ---




# ───────────────────────────────────────────────────────────────
# Expected outputs (for self-check):
#
# Ex1: Anita's report
#      BMI: 26.5 (OVERWEIGHT)
#      HR: 78 bpm (NORMAL for age 28)
#      BP: 118/76 (NORMAL)
#      Risk: ✓ ALL VITALS NORMAL OR ⚠ NEEDS DOCTOR CONSULTATION (for BMI)
#
# Ex2: Summary of 5 employees
#      Count of employees needing doctor consultation: 2 (Arjun, Rahim)
#      Or a formatted table showing each employee's status
#
# Ex3: Age comparison (both have BMI 25.5)
#      Patient A (age 25): HR 68 is NORMAL for their age
#      Patient B (age 65): HR 68 is NORMAL (maybe slightly low, but acceptable)
#      Same BMI, same vitals, but different age contexts
# ───────────────────────────────────────────────────────────────
