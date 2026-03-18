# Project 02 — Patient Vitals Screening at a Corporate Health Camp

## The Real-Life Problem

Dr. Mehta conducts annual health screenings at a 1000-person tech company. Every employee comes in, gets measured (height, weight, blood pressure, age, heart rate), and Dr. Mehta needs a quick tool to screen each person and flag those needing immediate doctor attention.

Without automation, each screening takes 10 minutes due to manual lookups. With a Python script, Dr. Mehta can run vitals through the program and get an instant health assessment with a risk flag. The tool must categorize BMI (Underweight/Normal/Overweight/Obese), evaluate resting heart rate zone, and check blood pressure against guidelines.

## Domain Context

**Industry**: Healthcare / Preventive Medicine
**Role**: Corporate Health Officer / Occupational Physician
**Tools in the real world**: Electronic Health Records (EHR) systems, Fitbit/Oura Ring APIs, hospital management software
**Why Python is used here**: Hospital backends use Python for rapid health assessments. Tools like Django + Python power many telemedicine platforms. This script mimics the "patient vitals assessment" module you'd find in any hospital system.

## The Python Solution Approach

We receive patient data: height (cm), weight (kg), age, blood pressure (sys/dia), and resting heart rate. We compute BMI using the formula: BMI = weight(kg) / height(m)². We classify the BMI using nested conditions (match/case in Python 3.10+). We check heart rate against age-based zones (normal for age 40 is 60-100 bpm, but for age 70 it's 50-90 bpm). We evaluate blood pressure using compound boolean logic (both systolic AND diastolic must pass). Finally, we flag the patient for doctor attention if ANY of BMI, heart rate, or blood pressure is abnormal.

## Python Concepts You Will Practice

| Concept | Where It Appears |
|---|---|
| Variables and data types | Section 1: Patient data (height, weight, age, BP, HR) |
| Arithmetic operators | Section 2: BMI calculation (weight/height²) |
| Comparison operators | Sections 3–5: Evaluating thresholds (systolic > 140?) |
| Boolean logic (and, or, not) | Sections 4–5: Compound conditions (sys > 140 AND dia > 90?) |
| match/case (Python 3.10+) | Section 3: BMI classification (Underweight/Normal/Overweight/Obese) |
| Nested if/elif/else | Sections 4–5: Heart rate and BP classification |
| f-string formatting | Section 6: Formatted health report output |

## How to Use This Project

1. Read the storyline to understand corporate health screening context
2. Run `solution.py` and observe how vitals are assessed for multiple patients
3. Pay attention to the match/case block (new in Python 3.10) — this is a modern alternative to if/elif chains
4. Notice the compound boolean conditions (and, or) — these are essential for real health checks
5. Attempt exercises without looking at the solution
6. Compare your approach with `exercises/solutions/solution_ex.py`

## Extension Ideas

- **Age-adjusted thresholds**: Modify heart rate and blood pressure limits based on age (over 65 gets different thresholds)
- **Risk scoring**: Assign points for each abnormal vital (BMI +10pts, High BP +5pts, High HR +5pts) and flag if total > 20
- **Medication recommendations**: Based on vitals, suggest lifestyle changes or recommend doctor consultation for medication
- **Statistical summary**: Process 10 employees and compute average BMI, percentage with high BP, etc.

## Real-World Equivalent

This project mimics:
- **Hospital EHR systems** (Epic, Cerner): where patient vitals trigger automated alerts
- **Telemedicine platforms** (1mg, Practo): where vitals are screened before doctor consultation
- **Fitness tracker APIs** (Apple Health, Google Fit): which process resting heart rate and alert if abnormal
- **Public health dashboards** (WHO, national health ministries): which categorize populations by BMI and BP
