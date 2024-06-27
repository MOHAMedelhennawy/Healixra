#!/usr/bin/python3
"""
Test database
Tables: Location, Doctor, Patient, Specialization.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.patient import Patient
from models.doctor import Doctor
from models.location import Location
from models.specialization import Specialization
from models import storage

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

i = 1
# List all doctors
for doctor in session.query(Doctor).all():
    print("=============== Doctor {} ===============".format(i))
    print(doctor)
    i += 1

doctor = session.query(Doctor).first()


i = 1
patients = doctor.patients
# List all patients related to doctor
for patient in patients:
    print("=============== patient {} ===============".format(i))
    print(patient)
    i += 1

print('+' * 100)
print('+' * 100)

print(doctor.specialization.specialization_name)
print(doctor.specialization_id)
print(doctor.specialization)


