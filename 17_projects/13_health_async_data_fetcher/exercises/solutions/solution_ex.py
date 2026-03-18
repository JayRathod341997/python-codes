# Solutions — Project 13: Async/Await

import asyncio
from dataclasses import dataclass
from typing import Optional, List

@dataclass
class PatientRecord:
    patient_id: int
    name: str
    lab_results: Optional[List[str]] = None
    vitals: Optional[dict] = None

print("\n" + "="*70)
print("EXERCISE 1 SOLUTION: PatientRecord with @dataclass")
print("="*70 + "\n")

async def fetch_lab(pid):
    await asyncio.sleep(0.5)
    return ["Glucose: 95", "BP: 120/80"]

async def fetch_vitals(pid):
    await asyncio.sleep(0.5)
    return {"HR": "72 bpm", "Temp": "98.6°F"}

async def fetch_patient(patient_id, name):
    lab, vitals = await asyncio.gather(
        fetch_lab(patient_id),
        fetch_vitals(patient_id),
    )
    return PatientRecord(
        patient_id=patient_id, name=name,
        lab_results=lab, vitals=vitals
    )

async def main():
    patient = await fetch_patient(101, "Alice")
    print(f"Patient: {patient.name}")
    print(f"  Lab: {patient.lab_results}")
    print(f"  Vitals: {patient.vitals}")

asyncio.run(main())

print("\n" + "="*70)
print("EXERCISE 2 SOLUTION: Multiple Patients (Concurrent vs Serial)")
print("="*70 + "\n")

async def fetch_all_concurrent(patients):
    tasks = [fetch_patient(pid, name) for pid, name in patients]
    return await asyncio.gather(*tasks)

async def fetch_all_serial(patients):
    results = []
    for pid, name in patients:
        result = await fetch_patient(pid, name)
        results.append(result)
    return results

async def compare():
    patients = [(101, "Alice"), (102, "Bob")]

    print("Concurrent:")
    start = time.time()
    results_c = await fetch_all_concurrent(patients)
    time_c = time.time() - start
    print(f"  Time: {time_c:.2f}s")

    print("Serial:")
    start = time.time()
    results_s = await fetch_all_serial(patients)
    time_s = time.time() - start
    print(f"  Time: {time_s:.2f}s")

    print(f"\n  Speedup: {time_s / time_c:.1f}x faster")

import time
asyncio.run(compare())

print("\n" + "="*70 + "\n")
