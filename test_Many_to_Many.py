#!/usr/bin/python3
"""
To test many to many realtionship between patient and doctor

To execute this file run this command in terminal:
HBNB_MYSQL_USER=Name HBNB_MYSQL_PWD=Password HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=Healixra HBNB_TYPE_STORAGE=db ./test_Many_to_Many.py 
"""



from models.base_model import BaseModel
from models.patient import Patient
from models.doctor import Doctor
from models import storage

patient1 = Patient(
    first_name='Mohammed', last_name='Ahmed', email='Mohammed@ex.com', gender='male',
    phone='010165', password='test0234'
)
patient2 = Patient(
    first_name='Ahmed', last_name='Khaled', email='Ahmed@ex.com', gender='male',
    phone='010325', password='2332p'
)
patient3 = Patient(
    first_name='Mona', last_name='elhennawy', email='Mona@ex.com', gender='female',
    phone='01034165', password='213-test'
)

# Save patients
patient1.save()
patient2.save()
patient3.save()

doctor1 = Doctor(first_name='Hazem', last_name='elmashad')

# Save doctor before appending patients
doctor1.save()

# Append patients to doctor
doctor1.patients.append(patient3)
doctor1.patients.append(patient2)
doctor1.patients.append(patient1)

# Commit the changes to the database
storage.save()

print("OK")
