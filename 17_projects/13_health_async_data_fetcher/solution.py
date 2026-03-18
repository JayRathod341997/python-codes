# ─────────────────────────────────────────────────────────────────
# Project 13 — Health — Async Patient Data Fetcher
# Concepts  : async/await, asyncio.gather, dataclasses, type hints
# Difficulty: Advanced
# ─────────────────────────────────────────────────────────────────

import asyncio
from dataclasses import dataclass
from typing import Optional, List

print("\n" + "="*75)
print("ASYNC PATIENT DATA AGGREGATION")
print("="*75)

# ── Section 1: PatientRecord Dataclass ────────────────────────────
@dataclass
class PatientRecord:
    """Patient data with all records."""
    patient_id: int
    name: str
    lab_results: Optional[List[str]] = None
    prescriptions: Optional[List[str]] = None
    imaging: Optional[List[str]] = None
    vitals: Optional[dict] = None
    insurance: Optional[str] = None

# ── Section 2: Simulated API Calls ────────────────────────────────
async def fetch_lab_results(patient_id):
    """Simulate API call to fetch lab results (1 sec delay)."""
    await asyncio.sleep(1)
    return [f"Hemoglobin: 13.5 g/dL", f"Glucose: 95 mg/dL"]

async def fetch_prescriptions(patient_id):
    """Simulate API call to fetch prescriptions (1 sec delay)."""
    await asyncio.sleep(1)
    return [f"Aspirin 100mg daily", f"Lisinopril 10mg daily"]

async def fetch_imaging(patient_id):
    """Simulate API call to fetch imaging (1 sec delay)."""
    await asyncio.sleep(1)
    return [f"Chest X-ray: Normal", f"ECG: No abnormalities"]

async def fetch_vitals(patient_id):
    """Simulate API call to fetch vitals (1 sec delay)."""
    await asyncio.sleep(1)
    return {"BP": "120/80", "HR": "72 bpm", "Temp": "98.6°F"}

async def fetch_insurance(patient_id):
    """Simulate API call to fetch insurance (1 sec delay)."""
    await asyncio.sleep(1)
    return "Aetna Premium Plan"

# ── Section 3: Async Patient Aggregator ────────────────────────────
class AsyncPatientAggregator:
    """Fetch all patient data concurrently."""

    async def fetch_patient(self, patient_id, name):
        """Fetch all data for one patient concurrently."""
        # Use asyncio.gather to run all tasks concurrently
        lab, rx, imaging, vitals, insurance = await asyncio.gather(
            fetch_lab_results(patient_id),
            fetch_prescriptions(patient_id),
            fetch_imaging(patient_id),
            fetch_vitals(patient_id),
            fetch_insurance(patient_id),
        )

        return PatientRecord(
            patient_id=patient_id,
            name=name,
            lab_results=lab,
            prescriptions=rx,
            imaging=imaging,
            vitals=vitals,
            insurance=insurance,
        )

    async def fetch_all_patients(self, patients):
        """Fetch data for multiple patients concurrently."""
        tasks = [self.fetch_patient(pid, name) for pid, name in patients]
        return await asyncio.gather(*tasks)

# ── Section 4: Synchronous Version (for comparison) ────────────────
async def fetch_patient_serial(patient_id, name):
    """Fetch data serially (one at a time)."""
    lab = await fetch_lab_results(patient_id)
    rx = await fetch_prescriptions(patient_id)
    imaging = await fetch_imaging(patient_id)
    vitals = await fetch_vitals(patient_id)
    insurance = await fetch_insurance(patient_id)

    return PatientRecord(
        patient_id=patient_id, name=name,
        lab_results=lab, prescriptions=rx,
        imaging=imaging, vitals=vitals, insurance=insurance,
    )

# ── Section 5: Demo ────────────────────────────────────────────────
async def main():
    """Run async demo."""
    aggregator = AsyncPatientAggregator()
    patients = [(101, "Alice"), (102, "Bob"), (103, "Charlie")]

    print("\n--- CONCURRENT FETCHING (async) ---")
    start = time.time()
    records = await aggregator.fetch_all_patients(patients)
    duration = time.time() - start
    print(f"Fetched {len(records)} patients in {duration:.2f}s")

    print("\n--- SERIAL FETCHING (sync comparison) ---")
    start = time.time()
    serial_records = await asyncio.gather(
        *[fetch_patient_serial(pid, name) for pid, name in patients]
    )
    duration_serial = time.time() - start
    print(f"Fetched {len(serial_records)} patients in {duration_serial:.2f}s")

    print(f"\n✓ Concurrent is {duration_serial / duration:.1f}x faster!")

    print("\n--- SAMPLE PATIENT DATA ---")
    patient = records[0]
    print(f"\n{patient.name} (ID: {patient.patient_id})")
    print(f"  Lab: {patient.lab_results}")
    print(f"  Rx: {patient.prescriptions}")
    print(f"  Imaging: {patient.imaging}")
    print(f"  Vitals: {patient.vitals}")
    print(f"  Insurance: {patient.insurance}")

# ── Section 6: Entry Point ────────────────────────────────────────
import time
if __name__ == "__main__":
    asyncio.run(main())

print("\n" + "="*75 + "\n")
