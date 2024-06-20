#!/usr/bin/python3
"""
Test to remove doctor from database and all patient related to this doctor
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.patient import Patient
from models.doctor import Doctor

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
# List all patient
patients = session.query(Patient).all()
for patient in patients:
    print("================= Row {} =================".format(i))
    print(patient)
    print
    i += 1

# List doctor with id
# Don't forget to change doctor id
doctor = session.query(Doctor).filter_by(id='2cb68ee6-a4c6-448b-aa2d-703a6bd95e56').first()
print("================= doctor =================")
print("doctor with id {}:\n{}".format(doctor.id, doctor))


session.delete(doctor)
session.commit()

i = 1
# List all patient
patients = session.query(Patient).all()
for patient in patients:
    print("================= Row {} =================".format(i))
    print(patient)
    print
    i += 1

# List doctor with id 
# Don't forget to change doctor id
doctor = session.query(Doctor).filter_by(id='2cb68ee6-a4c6-448b-aa2d-703a6bd95e56').first()
print("================= doctor =================")
print("doctor with id {}:\n{}".format(doctor.id, doctor))