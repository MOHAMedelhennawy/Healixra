import models
from models.specialization import Specialization
"""
Create fake Specializations

command:
USER=Name PWD=Password HOST=localhost DB=Healixra TYPE_STORAGE=db python3 create_fake_specializations.py  

"""

medical_specialties = [
    "Anesthesiology",
    "Cardiology",
    "Dermatology",
    "Endocrinology",
    "Family Medicine",
    "Gastroenterology",
    "Geriatrics",
    "Hematology",
    "Hepatology",
    "Infectious Diseases",
    "Nephrology",
    "Neurology",
    "Obstetrics and Gynecology",
    "Oncology",
    "Ophthalmology",
    "Orthopedic Surgery",
    "Otolaryngology (ENT)",
    "Pediatrics",
    "Pulmonology",
    "Psychiatry",
    "Respiratory Medicine",
    "Rheumatology",
    "Surgery",
    "Urology"
]
for medical_specialtie in medical_specialties:
    specialization = Specialization(specialization_name=medical_specialtie)
    specialization.save()

models.storage.save()
print('Fake specializations created successfully!')
