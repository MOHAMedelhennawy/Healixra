import models
from models.specialization import Specialization
"""
Anesthesiology
Cardiology
Dermatology
Endocrinology
Family Medicine
Gastroenterology
Geriatrics
Hematology
Hepatology
Infectious Diseases
Nephrology
Neurology
Obstetrics and Gynecology
Oncology
Ophthalmology
Orthopedic Surgery
Otolaryngology (ENT)
Pediatrics
Pulmonology
Psychiatry
Respiratory Medicine
Rheumatology
Surgery
Urology

command:
HBNB_MYSQL_USER=Name HBNB_MYSQL_PWD=Password HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=Healixra HBNB_TYPE_STORAGE=db python3 create_fake_specializations.py  

"""
name = ' '
while name:
    name = input()
    if name is not None:
        specialization = Specialization(specialization_name=name)
        specialization.save()

models.storage.save()
print('Ok')
