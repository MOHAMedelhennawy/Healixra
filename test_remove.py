#!/usr/bin/python3
"""
Test to remove doctor from database and all patient related to this doctor
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.patient import Patient
from models.doctor import Doctor
from models.specialization import Specialization

HBNB_MYSQL_USER = 'Name'
HBNB_MYSQL_PWD = 'Password'
HBNB_MYSQL_HOST = 'localhost'
HBNB_MYSQL_DB = 'Healixra'
# Database connection setup (adjust connection string as needed)
engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(HBNB_MYSQL_USER,
                                             HBNB_MYSQL_PWD,
                                             HBNB_MYSQL_HOST,
                                             HBNB_MYSQL_DB))

# Create a configured "Session" class
Session = sessionmaker(bind=engine)

# Create a Session
session = Session()

print("Before deleting:\n")

i = 1
# List all patient
patients = session.query(Patient).all()
for patient in patients:
    print("================= Patient {} =================".format(i))
    print(patient)
    print
    i += 1

# List doctor with id
i = 1
doctors = session.query(Doctor).all()
for doctor in doctors:
    print("================= Doctor {} =================".format(i))
    print(doctor)


print("Before deleting:\n\
      Number of all patients is: {}\n\
      And Number of all doctors: {}".format(len(patients), len(doctors)))


session.delete(doctor)
session.commit()

print("Afte deleting:\n")

i = 1
# List all patient
patients = session.query(Patient).all()
for patient in patients:
    print("================= Patient {} =================".format(i))
    print(patient)
    print
    i += 1

# List doctor with id
i = 1
doctors = session.query(Doctor).all()
for doctor in doctors:
    print("================= Doctor {} =================".format(i))
    print(doctor)

print("After deleting:\n\
      Number of all patients is: {}\n\
      And Number of all doctors: {}".format(len(patients), len(doctors)))